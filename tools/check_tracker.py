"""Check a session's tracker writes against the rules.

Works with both trackers:
  - Spreadsheet: take snapshots with the `snapshot` command.
  - Artifact: list each collection with ArtifactData (out_dir set to a folder), then combine the files
    with the `snapshot-dir` command.

Commands:
  python tools/check_tracker.py snapshot tracker/my-tracker.xlsx tracker/backups/<stamp>-before.json
  python tools/check_tracker.py snapshot-dir tracker/backups/<stamp>-before-db tracker/backups/<stamp>-before.json   (artifact: after ArtifactData list with out_dir)
  python tools/check_tracker.py check tracker/backups/<stamp>-before.json tracker/backups/<stamp>-after.json --stage sweep
  python tools/check_tracker.py validate tracker/backups/<stamp>-after.json

Stages: intake, sweep, fit, apply, outreach, prep, mailbox, resume, research, user.
Exit code 0 means every check passed.
"""
import json
import os
import re
import sys

COLLECTIONS = ["companies", "coverage", "listings", "answers", "settings"]
STATUSES = ["To apply", "Applied", "Followed up", "Interview", "Offer", "Review fit", "On hold",
            "Rejected", "Closed", "expired", "filled"]
LOCKED = {"Applied", "Followed up", "Interview", "Offer"}
OUTREACH = ["managerName", "managerTitle", "howIdentified", "confidence", "profileUrl",
            "emailOrFormat", "connectionNote", "longMessage"]
NEW_LISTING_REQUIRED = ["id", "company", "title", "location", "url", "industry", "pay", "why",
                        "teaches", "priority", "status", "history", "postingText"]
SECRET_PATTERNS = [
    (re.compile(r"\b\d{3}-\d{2}-\d{4}\b"), "looks like a Social Security number"),
    (re.compile(r"password\s*[:=]", re.I), "looks like a stored password"),
    (re.compile(r"\b\d{13,19}\b"), "long number that could be a card or account number"),
    (re.compile(r"\b\d{4}(?:[ -]\d{4}){2,3}\b"), "grouped number that could be a card or account number"),
]
DATE_START = re.compile(r"\s*\d{4}-\d{2}-\d{2}\s")

# Which columns each stage may change on a listing that already existed.
STAGE_FIELDS = {
    "intake": set(),
    "sweep": {"status", "history"},
    "fit": {"history"},
    "apply": {"status", "history", "postingText", "appliedDate"},
    "outreach": set(OUTREACH) | {"history"},
    "prep": {"history"},
    "mailbox": {"status", "history"},
    "research": set(),
    "resume": {"history"},
    "user": None,  # the user asked for a change directly: only the universal rules apply
}
# Which status moves each stage may make on an existing listing.
STAGE_MOVES = {
    "intake": set(),
    "sweep": {("To apply", "expired"), ("To apply", "filled")},
    "fit": set(),
    "apply": {("To apply", "Applied"), ("To apply", "expired"), ("To apply", "filled")},
    "outreach": set(),
    "prep": set(),
    "mailbox": {(a, b) for a in ("Applied", "Followed up", "Interview")
                for b in ("Followed up", "Interview", "Rejected", "Offer", "expired") if a != b},
    "research": set(),
    "resume": set(),
    "user": None,
}
# Which stages may write each of the other collections.
WRITERS = {
    "companies": {"sweep", "fit", "research", "user"},
    "coverage": {"sweep", "fit", "user"},
    "answers": {"intake", "apply", "user"},
    "settings": {"intake", "user"},
}


def flatten(row):
    """Accept {id, ...fields} or {id, data: {...}} (as some tools return)."""
    if isinstance(row, dict) and "data" in row and isinstance(row["data"], dict):
        out = dict(row["data"])
        out["id"] = row.get("id", out.get("id"))
        return out
    return dict(row)


def load(path):
    with open(path, encoding="utf-8") as f:
        raw = json.load(f)
    snap = {}
    for name in COLLECTIONS:
        rows = raw.get(name, [])
        if isinstance(rows, dict):  # {"docs": [...]} or {id: {...}}
            rows = rows["docs"] if "docs" in rows else [dict(v, id=k) for k, v in rows.items()]
        snap[name] = {str(r["id"]): r for r in (flatten(x) for x in rows)}
    return snap


def snapshot_xlsx(xlsx_path, out_path):
    from openpyxl import load_workbook
    wb = load_workbook(xlsx_path, data_only=True)
    out = {}
    for name in COLLECTIONS:
        rows = []
        if name in wb.sheetnames:
            ws = wb[name]
            header = [c.value for c in ws[1]]
            for r in ws.iter_rows(min_row=2, values_only=True):
                if all(v is None or str(v).strip() == "" for v in r):
                    continue
                rows.append({h: ("" if v is None else str(v)) for h, v in zip(header, r) if h})
        out[name] = rows
    write_snapshot(out, out_path)


def snapshot_dir(folder, out_path):
    """Combine the files ArtifactData writes with out_dir (<folder>/<collection>/<id>.json) into one snapshot."""
    out = {}
    for name in COLLECTIONS:
        rows = []
        sub = os.path.join(folder, name)
        if os.path.isdir(sub):
            for f in sorted(os.listdir(sub)):
                if f.endswith(".json"):
                    with open(os.path.join(sub, f), encoding="utf-8") as fh:
                        row = flatten(json.load(fh))
                    row["id"] = f[:-5]
                    rows.append(row)
        out[name] = rows
    write_snapshot(out, out_path)


def write_snapshot(out, out_path):
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    print("Snapshot saved:", out_path, {k: len(v) for k, v in out.items()})


def norm(s):
    return re.sub(r"[^a-z0-9]", "", str(s or "").lower())


def entries(history):
    """History entries are separated by ' | '. An entry itself never contains '|'."""
    return [e for e in str(history or "").split("|") if e.strip()]


def split_list(v):
    return [x.strip() for x in str(v or "").split(";") if x.strip()]


def validate(snap, problems, only_ids=None, only_companies=None, only_coverage=None):
    names = {norm(c.get("company")): c.get("company") for c in snap["companies"].values()}
    settings = next(iter(snap["settings"].values()), {}) if snap["settings"] else {}
    families = [f.rstrip("*").strip() for f in split_list(settings.get("roleFamilies"))]
    tracks = split_list(settings.get("tracks"))
    priorities = split_list(settings.get("priorities")) or ["High", "Medium", "Low", "On hold"]

    for lid, l in snap["listings"].items():
        if only_ids is not None and lid not in only_ids:
            continue
        st = l.get("status", "")
        if st not in STATUSES:
            problems.append("listing %s: unknown status %r" % (lid, st))
        if l.get("company") and norm(l["company"]) in names and names[norm(l["company"])] != l["company"]:
            problems.append("listing %s: company spelled %r but target list says %r" % (lid, l["company"], names[norm(l["company"])]))
        if l.get("company") and norm(l["company"]) not in names:
            problems.append("listing %s: company %r is not on the target list (add the employer first)" % (lid, l["company"]))
        for e in entries(l.get("history")):
            if not DATE_START.match(e):
                problems.append("listing %s: history entry %r does not start with a YYYY-MM-DD date" % (lid, e.strip()[:40]))
        if l.get("priority") and l["priority"] not in priorities:
            problems.append("listing %s: priority %r is not one of %s" % (lid, l["priority"], priorities))
        if families and l.get("family") and l["family"] not in families:
            problems.append("listing %s: family %r is not in settings.roleFamilies %s (write it without the *)" % (lid, l["family"], families))
        if tracks and l.get("track") and l["track"] not in tracks:
            problems.append("listing %s: track %r is not in settings.tracks %s" % (lid, l["track"], tracks))
        for col in ("history", "why", "postingText"):
            for pat, what in SECRET_PATTERNS:
                if pat.search(str(l.get(col, ""))):
                    problems.append("listing %s: %s %s" % (lid, col, what))
    seen = {}
    for lid, l in snap["listings"].items():
        key = (norm(l.get("company")), norm(l.get("reqId"))) if l.get("reqId") else None
        if key:
            if key in seen:
                problems.append("listings %s and %s: same company and req id" % (seen[key], lid))
            seen[key] = lid

    seen_names = {}
    for cid, c in snap["companies"].items():
        n = norm(c.get("company"))
        if n in seen_names:
            problems.append("companies %s and %s: same company name" % (seen_names[n], cid))
        seen_names[n] = cid
        if only_companies is not None and cid not in only_companies:
            continue
        if not re.fullmatch(r"[a-z0-9-]+", cid):
            problems.append("company %s: id must be lowercase letters, numbers and hyphens" % cid)
        if not str(c.get("company", "")).strip():
            problems.append("company %s: no company name" % cid)
        if c.get("tier") and c["tier"] not in ("A", "B", "C"):
            problems.append("company %s: tier %r must be A, B or C" % (cid, c["tier"]))
        for col in ("keepAnyway", "onHold"):
            if c.get(col) and str(c[col]).lower() not in ("yes", "no"):
                problems.append("company %s: %s must be yes or no" % (cid, col))

    for vid, v in snap["coverage"].items():
        if only_coverage is not None and vid not in only_coverage:
            continue
        if vid not in snap["companies"]:
            problems.append("coverage %s: no company with that id" % vid)
        if v.get("sweepState") and v["sweepState"] not in ("done", "partial", "not swept", "manual"):
            problems.append("coverage %s: sweepState %r must be done, partial, not swept or manual" % (vid, v["sweepState"]))
        if v.get("result") and v["result"] not in ("HIT", "NONE", "LEAD", "PENDING"):
            problems.append("coverage %s: result %r must be HIT, NONE, LEAD or PENDING" % (vid, v["result"]))
        if v.get("sweepState") == "manual" and not re.match(r"\s*(\d{4}-\d{2}-\d{2}\s+)?MANUAL:", str(v.get("detail", ""))):
            problems.append("coverage %s: a manual employer's detail must start with MANUAL:" % vid)

    for aid, a in snap["answers"].items():
        for pat, what in SECRET_PATTERNS:
            if pat.search(str(a.get("answer", ""))) or pat.search(str(a.get("useWhen", ""))):
                problems.append("answer %s: %s" % (aid, what))
        if re.search(r"passw|\bpin\b|social security|routing", str(a.get("question", "")), re.I):
            problems.append("answer %s: the answer bank must never hold this kind of item" % aid)


def check(before, after, stage, problems):
    allowed_fields = STAGE_FIELDS[stage]
    allowed_moves = STAGE_MOVES[stage]
    b, a = before["listings"], after["listings"]

    for lid in b:
        if lid not in a:
            problems.append("listing %s was deleted" % lid)
    for lid, old in b.items():
        new = a.get(lid)
        if new is None:
            continue
        # Universal: yourNotes is never written by a session.
        if str(old.get("yourNotes", "")) != str(new.get("yourNotes", "")):
            problems.append("listing %s: yourNotes changed. Sessions never write it. If the user typed a note "
                            "during the session, that note is theirs: report it and NEVER undo it." % lid)
        # Universal: history is append-only.
        oh, nh = str(old.get("history", "")), str(new.get("history", ""))
        if not nh.startswith(oh):
            problems.append("listing %s: history was rewritten, not appended to" % lid)
        changed = {k for k in set(old) | set(new)
                   if str(old.get(k, "")) != str(new.get(k, "")) and k != "yourNotes"}
        if changed and nh == oh and stage != "user":
            problems.append("listing %s: changed %s with no history entry" % (lid, sorted(changed)))
        added = []
        if nh.startswith(oh) and nh != oh:
            added = entries(nh[len(oh):])
            if oh.strip() and not nh[len(oh):].lstrip().startswith("|"):
                problems.append("listing %s: new history entry not separated by ' | '" % lid)
            for e in added:
                if not DATE_START.match(e):
                    problems.append("listing %s: history entry %r does not start with a YYYY-MM-DD date" % (lid, e.strip()[:40]))
        if allowed_fields is not None:
            extra = changed - allowed_fields
            if extra:
                problems.append("listing %s: stage %s may not change %s" % (lid, stage, sorted(extra)))
        os_, ns = old.get("status", ""), new.get("status", "")
        if os_ != ns and allowed_moves is not None and (os_, ns) not in allowed_moves:
            problems.append("listing %s: stage %s may not move status %r to %r" % (lid, stage, os_, ns))
        if stage in ("sweep", "fit") and os_ in LOCKED and changed:
            problems.append("listing %s: at %s, a %s may not touch it" % (lid, os_, stage))
        if stage == "apply" and ns == "Applied" and os_ != "Applied":
            if not str(new.get("postingText", "")).strip():
                problems.append("listing %s: set to Applied without postingText saved" % lid)
            if not str(new.get("appliedDate", "")).strip():
                problems.append("listing %s: set to Applied without appliedDate" % lid)
            if "upload:" not in " ".join(added).lower():
                problems.append("listing %s: set to Applied without 'upload: <method>' in the new history entry" % lid)
        if stage == "mailbox" and os_ != ns and "approved by the user" not in " ".join(added).lower():
            problems.append("listing %s: mailbox status change without 'approved by the user' in the history entry" % lid)

    new_ids = set(a) - set(b)
    for lid in sorted(new_ids):
        l = a[lid]
        if stage not in ("sweep", "fit", "user"):
            problems.append("listing %s: stage %s may not add listings" % (lid, stage))
            continue
        missing = [c for c in NEW_LISTING_REQUIRED if not str(l.get(c, "")).strip()]
        if missing:
            problems.append("new listing %s: missing %s" % (lid, missing))
        if stage != "user" and l.get("status") != "To apply":
            problems.append("new listing %s: status must be To apply, not %r" % (lid, l.get("status")))
        if str(l.get("yourNotes", "")).strip():
            problems.append("new listing %s: yourNotes must be empty" % lid)
        if not re.fullmatch(r"[a-z0-9-]+", lid):
            problems.append("new listing %s: id must be lowercase letters, numbers and hyphens" % lid)

    for name, ok in WRITERS.items():
        if before[name] != after[name] and stage not in ok:
            problems.append("%s changed, but stage %s does not write it" % (name, stage))
    for cid in before["companies"]:
        if cid not in after["companies"] and stage != "user":
            problems.append("company %s was deleted" % cid)
    for cid, old in before["coverage"].items():
        new = after["coverage"].get(cid)
        if new and str(old.get("detail", "")) and old.get("detail") != new.get("detail"):
            if str(old.get("detail", "")).strip() not in str(new.get("detail", "")):
                problems.append("coverage %s: earlier detail was not kept" % cid)
        if new and str(old.get("skipped", "")).strip() and str(old.get("skipped", "")).strip() not in str(new.get("skipped", "")):
            problems.append("coverage %s: earlier skipped lines were not kept" % cid)

    changed_companies = {k for k, v in after["companies"].items() if before["companies"].get(k) != v}
    validate(after, problems, only_ids=new_ids | {k for k in a if k in b and a[k] != b[k]},
             only_companies=changed_companies,
             only_coverage={k for k, v in after["coverage"].items() if before["coverage"].get(k) != v})
    return new_ids


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(2)
    cmd = args[0]
    if cmd == "snapshot":
        snapshot_xlsx(args[1], args[2])
        return
    if cmd == "snapshot-dir":
        snapshot_dir(args[1], args[2])
        return
    problems = []
    if cmd == "validate":
        validate(load(args[1]), problems)
    elif cmd == "check":
        stage = args[args.index("--stage") + 1] if "--stage" in args else None
        if stage not in STAGE_FIELDS:
            sys.exit("Give --stage as one of: " + ", ".join(STAGE_FIELDS))
        before, after = load(args[1]), load(args[2])
        new_ids = check(before, after, stage, problems)
        changed = [k for k in after["listings"] if k in before["listings"] and after["listings"][k] != before["listings"][k]]
        print("Stage: %s | listings before %d, after %d | new %d | changed %d" % (
            stage, len(before["listings"]), len(after["listings"]), len(new_ids), len(changed)))
    else:
        sys.exit("Unknown command " + cmd)
    for p in problems:
        print("  FAIL", p)
    print("RESULT: %s (%d problem%s)" % ("PASS" if not problems else "FAIL", len(problems), "" if len(problems) == 1 else "s"))
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
