"""Prove check_tracker.py catches rule breaks: each case breaks one rule and must FAIL."""
import copy
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SD = os.path.join(ROOT, "tests", "sample-data")
BUILD = os.path.join(ROOT, "tests", "build")
before = json.load(open(os.path.join(SD, "tracker-before.json"), encoding="utf-8"))
good = json.load(open(os.path.join(SD, "tracker-after-fit.json"), encoding="utf-8"))
APPLIED = "meridian-health-plans-r5521"


def L(d, lid):
    return [l for l in d["listings"] if l["id"] == lid][0]


def case_notes(d): L(d, APPLIED)["yourNotes"] = "Claude wrote here"
def case_history_rewrite(d): L(d, APPLIED)["history"] = "2026-09-29 cleaned up history."
def case_sweep_expires_applied(d):
    L(d, APPLIED)["status"] = "expired"; L(d, APPLIED)["history"] += " | 2026-09-29 gone on Indeed."
def case_new_missing_posting_text(d): d["listings"][-1]["postingText"] = ""
def case_new_wrong_status(d): d["listings"][-1]["status"] = "Review fit"
def case_company_misspelled(d): d["listings"][-1]["company"] = "Kestrel TeleHealth Inc"
def case_password_in_answers(d): d["answers"].append({"id": "pw", "topic": "Account", "question": "Workday password", "answer": "password: hunter2"})
def case_deleted_listing(d): d["listings"] = [l for l in d["listings"] if l["id"] != APPLIED]
def case_undated_history(d): L(d, "brightline-charting-bc-1042")["history"] += " | checked again"
def case_settings_changed(d): d["settings"][0]["excludedIndustries"] = "Staffing"

CASES = [(f.__name__[5:], f, "sweep") for f in [case_notes, case_history_rewrite, case_sweep_expires_applied,
         case_new_missing_posting_text, case_new_wrong_status, case_company_misspelled, case_password_in_answers,
         case_deleted_listing, case_undated_history, case_settings_changed]]
CASES.append(("password_in_answers_apply", case_password_in_answers, "apply"))
def case_applied_no_upload_method(d):
    l = L(d, "kestrel-telehealth-kt-3315"); l["status"] = "Applied"; l["appliedDate"] = "2026-09-30"
    l["history"] += " | 2026-09-30 applied, req KT-3315, confirmation KT-1."
CASES.append(("applied_no_upload_method", case_applied_no_upload_method, "apply"))
def good_apply(d):
    l = L(d, "kestrel-telehealth-kt-3315"); l["status"] = "Applied"; l["appliedDate"] = "2026-09-30"
    l["history"] += " | 2026-09-30 applied, req KT-3315, confirmation KT-1; upload: hidden file input."


def run(after, stage):
    # Sweep cases start from Maya's first tracker; later stages start from the tracker after the sweep.
    base = os.path.join(SD, "tracker-before.json" if stage == "sweep" else "tracker-after-fit.json")
    p = os.path.join(BUILD, "selftest-after.json")
    json.dump(after, open(p, "w", encoding="utf-8"))
    r = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "check_tracker.py"), "check",
                        base, p, "--stage", stage], capture_output=True, text=True)
    return r.returncode, r.stdout


os.makedirs(BUILD, exist_ok=True)
ok = True
code, _ = run(good, "sweep")
print("%-28s expect PASS -> %s" % ("good session", "PASS" if code == 0 else "FAIL"))
ok &= code == 0
for name, fn, stage in CASES:
    d = copy.deepcopy(good)
    fn(d)
    code, out = run(d, stage)
    first = [l for l in out.splitlines() if "FAIL " in l][:1]
    print("%-28s expect FAIL -> %s  %s" % (name, "FAIL" if code else "PASS (MISSED)", first[0].strip() if first else ""))
    ok &= code != 0
def research_adds_listing(d):
    d["listings"].append(dict(L(d, "kestrel-telehealth-kt-3315"), id="new-co-1", status="To apply", history="2026-09-30 added."))
CASES2 = [("research_adds_listing", research_adds_listing, "research")]
for name, fn, stage in CASES2:
    d = copy.deepcopy(good); fn(d); code, out = run(d, stage)
    first = [l for l in out.splitlines() if "FAIL " in l][:1]
    print("%-28s expect FAIL -> %s  %s" % (name, "FAIL" if code else "PASS (MISSED)", first[0].strip() if first else ""))
    ok &= code != 0
d = copy.deepcopy(good)
d["companies"].append({"id": "wrenford-digital-health", "company": "Wrenford Digital Health", "careersSite": "https://wrenford-dh.example/careers",
                       "tier": "C", "industry": "Digital health", "keepAnyway": "no", "onHold": "no", "added": "2026-09-30"})
code, _ = run(d, "research")
print("%-28s expect PASS -> %s" % ("research adds an employer", "PASS" if code == 0 else "FAIL"))
ok &= code == 0
# More cases: (name, change, stage, expect pass?). Stages other than sweep start from the tracker after the sweep.
def fit_adds_company_and_listing(d):
    d["companies"].append({"id": "new-health-co", "company": "New Health Co", "careersSite": "https://new-health.example/jobs",
                           "tier": "B", "industry": "Health tech", "keepAnyway": "no", "onHold": "no", "added": "2026-09-30"})
    d["listings"].append(dict(L(d, "kestrel-telehealth-kt-3315"), id="new-health-co-nh-1", company="New Health Co", reqId="NH-1",
                              history="2026-09-30 added from the employer's own site by fit review."))
def mailbox(approved):
    def f(d):
        l = L(d, APPLIED); l["status"] = "Interview"
        l["history"] += " | 2026-09-30 interview request for 10/3 at 9am" + (", from email dated 2026-09-30, approved by the user." if approved else ".")
    return f
def intake_settings(d): d["settings"][0]["tierA"] = "Employer in my home city"
def intake_touches_listing(d):
    l = L(d, "kestrel-telehealth-kt-3315"); l["priority"] = "Low"; l["history"] += " | 2026-09-30 priority changed."
def bad_tier(d): d["companies"][0]["tier"] = "Z"
def family_with_star(d):
    l = L(d, "kestrel-telehealth-kt-3315"); l["family"] = "Account executive*"; l["history"] += " | 2026-09-30 family set."
MORE = [
    ("fit adds employer + listing", fit_adds_company_and_listing, "fit", True),
    ("mailbox change with approval", mailbox(True), "mailbox", True),
    ("mailbox change, no approval text", mailbox(False), "mailbox", False),
    ("intake writes settings", intake_settings, "intake", True),
    ("intake touches a listing", intake_touches_listing, "intake", False),
    ("employer tier not A/B/C", bad_tier, "user", False),
    ("family written with the *", family_with_star, "user", False),
]
for name, fn, stage, expect in MORE:
    d = copy.deepcopy(good); fn(d); code, out = run(d, stage)
    got = code == 0
    first = [l for l in out.splitlines() if "FAIL " in l][:1]
    print("%-28s expect %s -> %s  %s" % (name, "PASS" if expect else "FAIL", "PASS" if got else "FAIL",
                                         "" if got == expect and expect else (first[0].strip() if first else "")))
    ok &= got == expect

# Snapshot formats: {"docs": [...]} and {id: {...}} load the same as a plain list, and snapshot-dir round-trips.
import shutil
sys.path.insert(0, os.path.join(ROOT, "tools"))
import check_tracker as ct
docs = {k: {"docs": v} for k, v in good.items()}
byid = {k: {r["id"]: {x: y for x, y in r.items() if x != "id"} for r in v} for k, v in good.items()}
p1, p2 = os.path.join(BUILD, "shape-docs.json"), os.path.join(BUILD, "shape-byid.json")
json.dump(docs, open(p1, "w", encoding="utf-8")); json.dump(byid, open(p2, "w", encoding="utf-8"))
same_shapes = ct.load(p1) == ct.load(p2) == ct.load(os.path.join(SD, "tracker-after-fit.json"))
folder = os.path.join(BUILD, "snapdir")
shutil.rmtree(folder, ignore_errors=True)
for col, rows in good.items():
    os.makedirs(os.path.join(folder, col))
    for r in rows:
        json.dump({k: v for k, v in r.items() if k != "id"}, open(os.path.join(folder, col, r["id"] + ".json"), "w", encoding="utf-8"))
p3 = os.path.join(BUILD, "snapdir.json")
import contextlib, io
with contextlib.redirect_stdout(io.StringIO()):
    ct.snapshot_dir(folder, p3)
roundtrip = ct.load(p3) == ct.load(os.path.join(SD, "tracker-after-fit.json"))
print("%-28s expect PASS -> %s" % ("snapshot shapes load alike", "PASS" if same_shapes else "FAIL"))
print("%-28s expect PASS -> %s" % ("snapshot-dir round trip", "PASS" if roundtrip else "FAIL"))
ok &= same_shapes and roundtrip

d = copy.deepcopy(good); good_apply(d); code, _ = run(d, "apply")
print("%-28s expect PASS -> %s" % ("good apply", "PASS" if code == 0 else "FAIL"))
ok &= code == 0
print("SELF-TEST:", "ALL CAUGHT" if ok else "SOMETHING WAS MISSED")
sys.exit(0 if ok else 1)
