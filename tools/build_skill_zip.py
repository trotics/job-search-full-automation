"""Build job-search-skill.zip for uploading in the Claude app (Customize > Skills > + > Upload a skill).

The skill folder must be at the root of the ZIP, so the ZIP holds job-search/SKILL.md, job-search/rules.md and so on.

Usage:
  python tools/build_skill_zip.py
"""
import os
import shutil
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "skill", "job-search")
OUT = os.path.join(ROOT, "job-search-skill.zip")


def main():
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        for dirpath, _, files in os.walk(SRC):
            for name in sorted(files):
                full = os.path.join(dirpath, name)
                arc = os.path.join("job-search", os.path.relpath(full, SRC)).replace(os.sep, "/")
                info = zipfile.ZipInfo(arc, date_time=(2026, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                with open(full, "rb") as f:
                    # Same bytes on every computer: Windows checkouts can add CR characters.
                    z.writestr(info, f.read().replace(b"\r\n", b"\n"))
    print("Wrote", os.path.relpath(OUT, ROOT))

    # Claude Code loads skills from .claude/skills/ in the folder it opens, with no install step.
    # Keep that copy identical to skill/job-search (edit skill/job-search, never the copy).
    dest = os.path.join(ROOT, ".claude", "skills", "job-search")
    if os.path.isdir(dest):
        shutil.rmtree(dest)
    shutil.copytree(SRC, dest)
    print("Synced", os.path.relpath(dest, ROOT))


if __name__ == "__main__":
    main()
