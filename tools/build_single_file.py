"""Build the one-file version of the Skill from the multi-file version.

Usage:
  python tools/build_single_file.py

Reads skill/job-search/ and writes skill/job-search-single-file/SKILL.md.
Edit the multi-file version, then run this. Never edit the single file by hand.
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "skill", "job-search")
OUT = os.path.join(ROOT, "skill", "job-search-single-file", "SKILL.md")

ORDER = [
    ("rules.md", "Rules"),
    ("stages/00-intake.md", None), ("stages/01-sweep.md", None), ("stages/02-fit-review.md", None),
    ("stages/03-apply.md", None), ("stages/04-outreach.md", None), ("stages/05-interview-prep.md", None),
    ("stages/06-mailbox-check.md", None), ("stages/07-resume.md", None), ("stages/08-company-research.md", None),
    ("references/tracker-columns.md", None), ("references/answer-bank.md", None), ("references/board-techniques.md", None), ("references/application-techniques.md", None),
    ("references/recurring-mistakes.md", None), ("references/my-rules-template.md", None),
    ("references/sample-resume.md", None), ("references/resume-guide.md", None),
    ("references/resume-facts-template.md", None), ("references/prompts.md", None),
]


def read(rel):
    with open(os.path.join(SRC, rel), encoding="utf-8") as f:
        return f.read()


def demote(text):
    """Push every heading down one level so each file becomes a section."""
    return re.sub(r"(?m)^(#{1,5}) ", lambda m: "#" + m.group(1) + " ", text)


def main():
    skill = read("SKILL.md")
    front, body = re.match(r"(?s)(---\n.*?\n---\n)(.*)", skill).groups()
    body = body.replace(
        "## Where things live",
        "This one file holds everything: the map, the rules, the stage contracts and the references. "
        "Where a section names a file such as `stages/01-sweep.md` or `rules.md`, read the section of that name below.\n\n"
        "## Where things live", 1)
    parts = [front, "\n<!-- Built by tools/build_single_file.py from skill/job-search/. Do not edit by hand. -->\n", body]
    for rel, _ in ORDER:
        parts.append("\n---\n\n<!-- %s -->\n\n" % rel)
        parts.append(demote(read(rel)).strip() + "\n")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("".join(parts))
    print("Wrote", os.path.relpath(OUT, ROOT))


if __name__ == "__main__":
    main()
