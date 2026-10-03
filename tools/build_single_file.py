"""Build the one-file version of the Skill from the workspace.

Usage:
  python tools/build_single_file.py

Reads the same files as tools/build_skill_zip.py (Markdown only) and writes single-file-skill/SKILL.md.
Edit the workspace files, then run this. Never edit the single file by hand.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_skill_zip import ROOT, package_files  # noqa: E402

OUT = os.path.join(ROOT, "single-file-skill", "SKILL.md")


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def demote(text):
    """Push every heading down one level so each file becomes a section."""
    return re.sub(r"(?m)^(#{1,5}) ", lambda m: "#" + m.group(1) + " ", text)


def main():
    files = [(arc, full) for arc, full in package_files() if arc.endswith(".md")]
    skill = read(files[0][1])
    front, body = re.match(r"(?s)(---\n.*?\n---\n)(.*)", skill).groups()
    body = body.replace(
        "## Where to work",
        "This one file holds everything: the routing, the rules, the stage contracts and the references. "
        "Each file of the workspace is a section below, headed by its path in a comment. "
        "Where a section names a file such as `stages/01-sweep/CONTEXT.md` or `shared/rules.md`, read the section of that name below. "
        "The tracker page is not in this file: use the spreadsheet tracker, or get `tracker/tracker-page.html` from the full workspace.\n\n"
        "## Where to work", 1)
    parts = [front, "\n<!-- Built by tools/build_single_file.py from the workspace. Do not edit by hand. -->\n", body]
    for arc, full in files[1:]:
        parts.append("\n---\n\n<!-- %s -->\n\n" % arc)
        parts.append(demote(read(full)).strip() + "\n")
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("".join(parts))
    print("Wrote", os.path.relpath(OUT, ROOT))


if __name__ == "__main__":
    main()
