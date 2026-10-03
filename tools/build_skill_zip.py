"""Build job-search-skill.zip for uploading in the Claude app (Customize > Skills > + > Upload a skill).

The ZIP packages the workspace's instructions as a Skill. The skill folder must be at the root of the
ZIP, so it holds job-search/SKILL.md (from tools/package/SKILL.md), job-search/CONTEXT.md,
job-search/shared/, job-search/stages/*/CONTEXT.md and references/, job-search/setup/ and the tracker page.
Stage output folders are never included.

Usage:
  python tools/build_skill_zip.py
"""
import os
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "job-search-skill.zip")


def package_files():
    """(path inside the Skill folder, file on disk) for every file the Skill holds, in a fixed order."""
    files = [("SKILL.md", os.path.join(ROOT, "tools", "package", "SKILL.md")),
             ("CONTEXT.md", os.path.join(ROOT, "CONTEXT.md")),
             ("setup/questionnaire.md", os.path.join(ROOT, "setup", "questionnaire.md")),
             ("tracker/tracker-page.html", os.path.join(ROOT, "tracker", "tracker-page.html")),
             ("tracker/spreadsheet/job-search-tracker.xlsx",
              os.path.join(ROOT, "tracker", "spreadsheet", "job-search-tracker.xlsx"))]
    for name in sorted(os.listdir(os.path.join(ROOT, "shared"))):
        if name == "my-setup.md":  # the person's own filled-in copy, never packaged
            continue
        files.append(("shared/" + name, os.path.join(ROOT, "shared", name)))
    for name in sorted(os.listdir(os.path.join(ROOT, "tools"))):
        if name.endswith(".py") and name not in ("build_skill_zip.py", "build_single_file.py", "build_template.py", "check_repo.py"):
            files.append(("tools/" + name, os.path.join(ROOT, "tools", name)))
    files.append(("requirements.txt", os.path.join(ROOT, "requirements.txt")))
    stages = os.path.join(ROOT, "stages")
    for stage in sorted(os.listdir(stages)):
        files.append(("stages/%s/CONTEXT.md" % stage, os.path.join(stages, stage, "CONTEXT.md")))
        refs = os.path.join(stages, stage, "references")
        for name in sorted(os.listdir(refs)) if os.path.isdir(refs) else []:
            files.append(("stages/%s/references/%s" % (stage, name), os.path.join(refs, name)))
    return files


def main():
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        for arc, full in package_files():
            info = zipfile.ZipInfo("job-search/" + arc, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            with open(full, "rb") as f:
                # Same bytes on every computer: Windows checkouts can add CR characters.
                data = f.read()
                if not arc.endswith(".xlsx"):  # never touch the bytes of a binary file
                    data = data.replace(b"\r\n", b"\n")
                z.writestr(info, data)
    print("Wrote", os.path.relpath(OUT, ROOT))


if __name__ == "__main__":
    main()
