"""Prove check_resume.py catches resume problems: each case plants one problem and must FAIL."""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EX = os.path.join(ROOT, "examples", "test-run", "resume")
BUILD = os.path.join(ROOT, "tests", "build")
if not os.path.isdir(EX):
    sys.exit("This self-test uses the made-up example in examples/test-run/resume/, which is missing from this copy.")
GOOD = open(os.path.join(EX, "resume.md"), encoding="utf-8").read()

CASES = [
    ("invented number", lambda s: s.replace("trained 30 nurses in 6 weeks", "trained 45 nurses in 6 weeks")),
    ("inflated percent", lambda s: s.replace("82% to 96%", "82% to 99%")),
    ("spelled-out number not in facts", lambda s: s.replace("six years", "eight years")),
    ("em dash", lambda s: s.replace("; 14 proposed", " " + chr(0x2014) + " 14 proposed")),
    ("first person", lambda s: s.replace("- Raised unit", "- I raised unit")),
    ("third person", lambda s: s.replace("14 proposed fixes adopted", "her 14 fixes adopted")),
    ("birth date", lambda s: s.replace("(555) 010-0142", "(555) 010-0142 | Date of birth: 1994")),
    ("street address", lambda s: s.replace("Larkfield, Calder | maya", "418 Alder Street, Larkfield, Calder | maya")),
    ("employer not in facts", lambda s: s.replace("### Registered Nurse, Medical-Surgical Unit | Pinecrest Health System",
                                                  "### Registered Nurse, Medical-Surgical Unit | Northfield Hospital")),
    ("skill not in facts", lambda s: s.replace("Vendor communication,", "Vendor communication, Salesforce,")),
    ("bullet too long", lambda s: s.replace("- Led the unit's fall-prevention project;", "- Led the unit's fall-prevention project" + ", working closely with the whole team" * 6 + ";")),
    ("missing heading", lambda s: s.replace("## Skills", "## Things")),
]


FACTS = open(os.path.join(EX, "resume-facts.md"), encoding="utf-8").read()
POSTING_LINES = [l for l in FACTS.splitlines() if l.strip().startswith("- Posting:")]


def run(text, facts=FACTS):
    os.makedirs(BUILD, exist_ok=True)
    p = os.path.join(BUILD, "resume-selftest.md")
    f = os.path.join(BUILD, "resume-facts-selftest.md")
    open(p, "w", encoding="utf-8").write(text)
    open(f, "w", encoding="utf-8").write(facts)
    r = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "check_resume.py"), p, "--facts", f],
                       capture_output=True, text=True)
    return r.returncode, r.stdout


def drop_section(f):
    start = f.index("## What employers ask for")
    return f[:start] + f[f.index("## Jobs"):]


def swap_sections(s):
    lic = s[s.index("## Licenses and Certifications"):s.index("## Experience")]
    s = s.replace(lic, "")
    return s.replace("## Education", lic + "## Education")


# What employers ask for cases: (name, change to resume, change to facts, expect pass?)
POSTINGS_CASES = [
    ("no 'What employers ask for' section", None, drop_section, False),
    ("postings source, only 2 postings", None, lambda f: f.replace(POSTING_LINES[2] + "\n", ""), False),
    ("summary not confirmed (no date)", None, lambda f: f.replace("Built and confirmed by the user: 2026-09-29", "Built and confirmed by the user: [YYYY-MM-DD]"), False),
    ("sections out of the saved order", swap_sections, None, False),
    ("uses a posting term not in facts", lambda s: s.replace("moving into healthcare technology sales", "moving into telehealth sales"), None, False),
    ("skill only in the postings", lambda s: s.replace("Vendor communication,", "Vendor communication, Acute care,"), None, False),
    ("fallback: 2 postings + example", None, lambda f: f.replace("Based on: postings", "Based on: 2 postings plus example").replace(POSTING_LINES[2] + "\n", ""), True),
    ("fallback: user description + example", None, lambda f: f.replace("Based on: postings", "Based on: user description plus example"), True),
    ("fallback: default", None, lambda f: f.replace("Based on: postings", "Based on: default"), True),
    # Normal resume text that must not be flagged.
    ("ok: Roman numeral (Level I)", lambda s: s.replace("in a 24-bed unit", "in a 24-bed Level I trauma unit"), None, True),
    ("ok: words like results-driven", lambda s: s.replace("Registered nurse with", "Results-driven, passionate registered nurse with"), None, True),
    ("ok: the word 'single'", lambda s: s.replace("on problems after go-live", "on a single list of problems after go-live"), None, True),
    # Normal text the second review found falsely flagged.
    ("ok: 'patients age 65'", lambda s: s.replace("2 critically ill patients", "2 critically ill patients age 65 and over"), lambda f: f.replace("Results:", "Results (patients age 65 and over):", 1), True),
    ("ok: '40 clients in court'", lambda s: s.replace("on a 32-bed unit", "on a 32-bed unit, 4 nurses in court"), lambda f: f.replace("Results:", "Results (4 nurses in court):", 1), True),
    ("ok: no Education section", lambda s: s[:s.index("## Education")] + s[s.index("## Skills"):], lambda f: f.replace("Section order: Summary, Licenses and Certifications, Experience, Education, Skills", "Section order: Summary, Licenses and Certifications, Experience, Skills"), True),
    ("ok: 'None' in not-in-facts line", None, lambda f: f.replace("quota, demos, telehealth, virtual nursing, acute care, B2B sales, book of accounts", "None"), True),
    ("ok: 'Microsoft Dynamics' skill", lambda s: s.replace("Vendor communication,", "Vendor communication, Microsoft Dynamics,"), lambda f: f.replace("- Vendor communication", "- Vendor communication\n- Microsoft Dynamics"), True),
    ("short skill inside a word", lambda s: s.replace("Vendor communication,", "Vendor communication, MIG,"), lambda f: f.replace("- Vendor communication", "- Vendor communication (migration of charts)"), False),
    ("real street address", lambda s: s.replace("Larkfield, Calder | maya", "418 Alder Street, Larkfield, Calder | maya"), None, False),
    ("real age", lambda s: s.replace("Larkfield, Calder | maya", "Larkfield, Calder | Age: 32 | maya"), None, False),
]


def sample_resume_case():
    """The sample in stages/07-resume/references/sample-resume.md must build and pass, so users can copy its format."""
    text = open(os.path.join(ROOT, "stages", "07-resume", "references", "sample-resume.md"), encoding="utf-8").read()
    resume = text.split("---\n", 1)[1].strip() + "\n"
    facts = resume + "\n## What employers ask for\n- Based on: default\n- Built and confirmed by the user: 2026-01-01\n"
    return resume, facts


ok = True
code, _ = run(GOOD)
print("%-34s expect PASS -> %s" % ("approved resume", "PASS" if code == 0 else "FAIL"))
ok &= code == 0
for name, fn in CASES:
    changed = fn(GOOD)
    assert changed != GOOD, "case did not change the resume: " + name
    code, out = run(changed)
    first = [l.strip() for l in out.splitlines() if "FAIL " in l][:1]
    print("%-34s expect FAIL -> %s  %s" % (name, "FAIL" if code else "PASS (MISSED)", first[0] if first else ""))
    ok &= code != 0
for name, rfn, ffn, expect_pass in POSTINGS_CASES:
    code, out = run(rfn(GOOD) if rfn else GOOD, ffn(FACTS) if ffn else FACTS)
    first = [l.strip() for l in out.splitlines() if "FAIL " in l][:1]
    want = "PASS" if expect_pass else "FAIL"
    got = "PASS" if code == 0 else "FAIL"
    print("%-34s expect %s -> %s  %s" % (name, want, got if got == want else got + " (WRONG)", first[0] if first and not expect_pass else ""))
    ok &= got == want
r, f = sample_resume_case()
code, out = run(r, f)
print("%-34s expect PASS -> %s" % ("sample resume format", "PASS" if code == 0 else "FAIL (WRONG)"))
ok &= code == 0
print("SELF-TEST:", "ALL CAUGHT" if ok else "SOMETHING WAS MISSED")
sys.exit(0 if ok else 1)
