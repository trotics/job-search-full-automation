"""Fictional-user test: write the fit calls into the tracker the way a sweep session would.

Reads tests/sample-data/tracker-before.json, postings.json and fit-calls.json.
Writes tests/sample-data/tracker-after-fit.json, plus a filled spreadsheet copy for the
spreadsheet-path test at tests/build/maya-tracker.xlsx.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SD = os.path.join(ROOT, "tests", "sample-data")
TODAY = "2026-09-29"


def slug(s):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")


def main():
    before = json.load(open(os.path.join(SD, "tracker-before.json"), encoding="utf-8"))
    postings = {p["n"]: p for p in json.load(open(os.path.join(SD, "postings.json"), encoding="utf-8"))}
    calls = json.load(open(os.path.join(SD, "fit-calls.json"), encoding="utf-8"))
    after = json.loads(json.dumps(before))
    companies = {c["company"]: c for c in after["companies"]}

    per_company = {}
    for c in calls["calls"]:
        p = postings[c["n"]]
        per_company.setdefault(p["company"], {"added": [], "skipped": []})
        if c["decision"] == "pass":
            lid = slug(p["company"]) + "-" + slug(p["reqId"])
            assert lid not in {l["id"] for l in after["listings"]}, lid
            after["listings"].append({
                "id": lid, "company": p["company"], "title": p["title"], "location": p["location"],
                "url": p["url"], "reqId": p["reqId"], "industry": companies[p["company"]]["industry"],
                "track": "Main", "family": c["family"], "posted": p["posted"],
                "pay": p["pay"] if p["pay"] != "Not posted" else "not posted",
                "why": c["why"], "teaches": c["teaches"], "priority": c["priority"], "status": "To apply",
                "appliedDate": "", "reviewReason": "",
                "postingText": "%s. %s. Pay: %s. %s. %s" % (p["title"], p["location"], p["pay"], p["type"], p["text"]),
                "history": "%s added from the employer's own site by fit review." % TODAY,
                "yourNotes": "", "managerName": "", "managerTitle": "", "howIdentified": "", "confidence": "",
                "profileUrl": "", "emailOrFormat": "", "connectionNote": "", "longMessage": "",
            })
            per_company[p["company"]]["added"].append(p["title"])
        else:
            per_company[p["company"]]["skipped"].append("%s, %s: %s" % (p["title"], p["reqId"], c["reason"]))

    for name, r in per_company.items():
        co = companies[name]
        found = ("Added: " + "; ".join(r["added"]) + ". ") if r["added"] else "Nothing fit. "
        after["coverage"].append({
            "id": co["id"], "company": name, "industry": co["industry"], "sweepDate": TODAY,
            "sweepState": "done", "result": "HIT" if r["added"] else "NONE",
            "detail": "%s read every posting on the employer's own site. %s" % (TODAY, found),
            "skipped": "\n".join(r["skipped"]), "sweepProgress": "",
        })

    out = os.path.join(SD, "tracker-after-fit.json")
    json.dump(after, open(out, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print("Wrote", os.path.relpath(out, ROOT))
    added = sum(len(r["added"]) for r in per_company.values())
    skipped = sum(len(r["skipped"]) for r in per_company.values())
    print("Postings read: %d | added: %d | skipped: %d | employers not swept (excluded): %d" % (
        added + skipped, added, skipped, len(calls["excluded_not_swept"])))

    sys.path.insert(0, os.path.join(ROOT, "tools"))
    from build_template import build
    os.makedirs(os.path.join(ROOT, "tests", "build"), exist_ok=True)
    build(before, os.path.join(ROOT, "tests", "build", "maya-tracker.xlsx"))
    print("Wrote tests/build/maya-tracker.xlsx (Maya's before-state, for the spreadsheet path test)")


if __name__ == "__main__":
    main()
