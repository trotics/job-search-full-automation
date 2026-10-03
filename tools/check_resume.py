"""Check a resume against the rules in references/resume-guide.md.

Usage:
  python tools/check_resume.py my-files/resume.md --facts my-files/resume-facts.md [--pdf my-files/resume.pdf --years 6]

Fails if:
  - a number, job title, employer, school or skill on the resume is not in the facts file,
  - there is an em dash or en dash, or a pronoun ("I", "my", "she", "her"),
  - personal data that does not belong on a resume appears (birth date, age, street address, ID or license numbers),
  - a bullet is longer than about two lines, or the summary is too long,
  - a standard heading is missing,
  - the PDF has more pages than the limit (one page under ten years of experience, two otherwise),
  - the facts file has no confirmed "What employers ask for" section (from 3 to 5 postings, or a named fallback),
    the resume's sections are out of the order saved there, or the resume uses a posting term marked there as not in the facts.
Exit code 0 means every check passed.
"""
import re
import sys

# (pattern, what, flags). Patterns aim at personal details, not normal resume text
# ("patients age 65", "40 clients in court" and "a single platform" must pass).
PERSONAL = [
    (r"\b(date of birth|DOB|born on|birthday)\b", "birth date", re.I),
    (r"\bage\s*:\s*\d{2}\b|\bI am \d{2}\b|\b\d{2} years old\b", "age", re.I),
    (r"\bmarital status\b|\b(married|single|divorced|widowed)\s*(,|\||;|$)|\bstatus:\s*(married|single|divorced)\b", "marital status", re.I | re.M),
    (r"\b\d{3}-\d{2}-\d{4}\b", "Social Security number", 0),
    (r"\b\d{1,5}\s+[A-Z][a-z]+(\s[A-Z][a-z]+)?\s+(Street|St|Avenue|Ave|Road|Rd|Drive|Dr|Lane|Ln|Boulevard|Blvd|Court|Ct|Way)\b\.?", "street address", 0),
    (r"\blicen[cs]e\s*(no\.?|number|#)\s*:?\s*\w+", "license number", re.I),
    (r"\b(nationality|citizenship:|religion)\b", "nationality or religion", re.I),
    (r"\b(salary history|previous salary|current salary)\b", "salary history", re.I),
]
# Education is optional: many jobs need no degree, and a user without one must never invent a heading.
REQUIRED = ["Summary", "Experience", "Skills"]
EMPTY = {"none", "n/a", "na", "-", "no", ""}
NUM = re.compile(r"\$?\d[\d,]*(?:\.\d+)?%?")
WORDS = {w: str(i) for i, w in enumerate("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty".split())}


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def numbers(text):
    out = set()
    for m in NUM.finditer(text):
        n = m.group(0).replace("$", "").replace(",", "").rstrip("%")
        if n:
            out.add(n)
    for w in re.findall(r"[A-Za-z]+", text):
        if w.lower() in WORDS and w.lower() not in ("one",):
            out.add(WORDS[w.lower()])
    return out


def main():
    a = sys.argv[1:]
    if not a or "--facts" not in a:
        print(__doc__)
        sys.exit(2)
    resume = open(a[0], encoding="utf-8").read()
    facts = open(a[a.index("--facts") + 1], encoding="utf-8").read()
    # The "What employers ask for" section describes postings, not the user. Nothing in it counts as a fact about the user.
    user_facts = re.sub(r"(?ms)^## What employers ask for\s*$.*?(?=^## |\Z)", "", facts)
    facts_norm = norm(user_facts)
    facts_low = re.sub(r"\s+", " ", user_facts.lower())
    problems = []
    lines = resume.splitlines()

    # Dashes and pronouns. (No word list is banned: any word is fine when the facts back it up.)
    for ch, name in ((chr(0x2014), "em dash"), (chr(0x2013), "en dash")):
        if ch in resume:
            problems.append("%s found" % name)
    low = resume.lower()
    first_person = re.compile(r"(?<![A-Za-z'])(I|me|my|mine|we|our|My|We|Our|he|she|him|her|his|hers|He|She|His|Her)(?![A-Za-z'])")
    # A capital I after words like Level or Phase is a Roman numeral ("Level I trauma center"), not a pronoun.
    numeral_before = re.compile(r"(Level|Phase|Tier|Grade|Class|Stage|Type|Step|Part|Title|Unit|[A-Z][a-z]+ist|Nurse|Analyst|Engineer|Specialist|Technician|Associate|Representative)\s+$")
    for i, l in enumerate(lines, 1):
        if l.startswith("#"):
            continue
        for m in first_person.finditer(l):
            if m.group(1) == "I" and numeral_before.search(l[:m.start()]):
                continue
            problems.append("line %d: pronoun; resumes use none (%s)" % (i, l.strip()[:50]))
            break

    # Personal data.
    for pat, what, flags in PERSONAL:
        if re.search(pat, resume, flags):
            problems.append("personal data that does not belong on a resume: %s" % what)

    # Headings.
    heads = [l[3:].strip() for l in lines if l.startswith("## ")]
    for h in REQUIRED:
        if not any(x.lower().startswith(h.lower()) for x in heads):
            problems.append("missing heading: %s" % h)
    if not (lines and lines[0].startswith("# ")):
        problems.append("first line must be '# Full Name'")

    # Every number on the resume must be in the facts.
    fact_nums = numbers(user_facts)
    for n in sorted(numbers(resume)):
        if n not in fact_nums:
            problems.append("number %s is not in the facts file" % n)

    # Jobs, schools and skills must be in the facts.
    section = ""
    for i, l in enumerate(lines, 1):
        if l.startswith("## "):
            section = l[3:].strip().lower()
        elif l.startswith("### "):
            parts = [p.strip() for p in l[4:].split("|")]
            for p in parts[:-1]:
                if norm(p) and norm(p) not in facts_norm:
                    problems.append("line %d: %r is not in the facts file" % (i, p))
        elif l.startswith("- ") and section.startswith("skills"):
            items = l[2:].split(":", 1)[-1]
            for item in re.split(r",|;", items):
                # A skill must appear in the facts as a whole word or phrase, so "MIG" does not match inside "migration".
                phrase = re.sub(r"\s+", " ", item.strip().lower())
                if phrase and not re.search(r"(?<![a-z0-9])" + re.escape(phrase) + r"(?![a-z0-9])", facts_low):
                    problems.append("line %d: skill %r is not in the facts file" % (i, item.strip()))
        elif l.startswith("- ") and len(l) > 222:
            problems.append("line %d: bullet longer than about two lines (%d characters)" % (i, len(l) - 2))

    # Summary length.
    if "## Summary" in resume:
        summ = resume.split("## Summary", 1)[1].split("\n## ", 1)[0].strip()
        if len(summ) > 450:
            problems.append("summary is %d characters; keep it to two or three lines" % len(summ))

    # The "What employers ask for" section: every user has one, from postings or a named fallback.
    prof = re.search(r"(?ms)^## What employers ask for\s*$(.*?)(?=^## )", facts + "\n## end\n")
    if not prof:
        problems.append("facts file has no '## What employers ask for' section (stage 07 Part B)")
    else:
        p = prof.group(1)
        def field(name):
            m = re.search(r"(?m)^- " + re.escape(name) + r":\s*(.*)$", p)
            v = m.group(1).strip() if m else ""
            return "" if v.startswith("[") else v
        src = field("Based on").lower()
        postings = [l for l in re.findall(r"(?m)^\s+- Posting:\s*(.*)$", p) if l.strip() and not l.strip().startswith("[")]
        example = field("Closest example")
        if not src:
            problems.append("'What employers ask for' section: no 'Based on' line")
        elif src == "postings":
            if not 3 <= len(postings) <= 5:
                problems.append("'What employers ask for' section: source is postings but %d postings are listed (need 3 to 5)" % len(postings))
        elif "postings plus example" in src:
            if not postings or not example:
                problems.append("'What employers ask for' section: fallback needs the postings found and a closest example")
        elif "user description plus example" in src:
            if not example:
                problems.append("'What employers ask for' section: fallback needs a closest example")
        elif src != "default":
            problems.append("'What employers ask for' section: unknown 'Based on' value %r" % src)
        if not re.match(r"\d{4}-\d{2}-\d{2}", field("Built and confirmed by the user")):
            problems.append("'What employers ask for' section: no date showing the user confirmed it")
        order = [x.strip().lower() for x in field("Section order").split(",") if x.strip()]
        if order:
            seen = [h.lower() for h in heads if h.lower() in order]
            if seen != [h for h in order if h in seen]:
                problems.append("sections out of the saved order: resume has %s, the facts file says %s" % (seen, order))
        for term in [t.strip() for t in re.split(r",|;", field("Terms the postings use that are not in your facts (never used unless added to the facts first)")) if t.strip().lower().rstrip(".") not in EMPTY]:
            if re.search(r"\b" + re.escape(term.lower()) + r"\b", low):
                problems.append("uses %r, which the facts file marks as not in the facts" % term)

    # Page count.
    if "--pdf" in a:
        pdf = open(a[a.index("--pdf") + 1], "rb").read()
        pages = len(re.findall(rb"/Type\s*/Page[^s]", pdf))
        years = int(a[a.index("--years") + 1]) if "--years" in a else 0
        limit = 1 if years < 10 else 2
        print("PDF pages: %d (limit %d for %d years of experience)" % (pages, limit, years))
        if pages > limit:
            problems.append("PDF has %d pages; the limit is %d" % (pages, limit))

    for p in problems:
        print("  FAIL", p)
    print("RESULT: %s (%d problem%s)" % ("PASS" if not problems else "FAIL", len(problems), "" if len(problems) == 1 else "s"))
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
