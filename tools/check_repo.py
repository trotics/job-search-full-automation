"""Repo check: run before sharing your copy of this project.

Checks every file in the repo, the inside of the .xlsx and .zip files, and the git history for:
  1. Your private strings (optional): personal details that must never be shared, such as your
     name, phone, email, street or employers. Keep them in a private file OUTSIDE the repo,
     one per line, and pass it with --banned.
     A line ending in "(whole word, case-sensitive)" matches only as a whole word with that exact case.
  2. Em dashes and en dashes.
  3. Files copied unchanged from a private folder (optional: --private-folder).

Usage:
  python tools/check_repo.py
  python tools/check_repo.py --banned ../private/banned-strings.txt
  python tools/check_repo.py --banned PATH --private-folder PATH

Exit code 0 means clean. Anything else means a check failed.
"""
import hashlib
import os
import re
import subprocess
import sys
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

WHOLE = "(whole word, case-sensitive)"

DASHES = {chr(0x2014): "em dash", chr(0x2013): "en dash"}
SKIP_DIRS = {".git", "__pycache__", "node_modules"}


def load_banned(path):
    loose, exact = [], []
    if not path:
        return loose, exact
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            if line.endswith(WHOLE):
                exact.append(line[: -len(WHOLE)].strip())
            else:
                loose.append(line.strip())
    return loose, exact


def repo_files():
    """Files git would share: tracked files plus new files git does not ignore.
    Your stage output folders, tracker copy and backups are ignored by git, so they are never shared and not checked."""
    try:
        out = subprocess.run(["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
                             cwd=ROOT, capture_output=True, check=True).stdout.decode("utf-8", "replace")
        for rel in sorted(set(p for p in out.split("\0") if p)):
            path = os.path.join(ROOT, rel)
            if os.path.isfile(path):
                yield path
        return
    except (OSError, subprocess.CalledProcessError):
        pass
    # No git: check every file except the folders git would ignore.
    ignored = SKIP_DIRS | {"output", "backups", "build"}
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in ignored]
        for name in filenames:
            if name not in ("my-tracker.xlsx", "my-setup.md"):
                yield os.path.join(dirpath, name)


def texts_of(path):
    """Yield (label, text) for a file. An .xlsx or .zip is opened and each text part inside is checked."""
    rel = os.path.relpath(path, ROOT)
    if path.endswith((".xlsx", ".zip")):
        with zipfile.ZipFile(path) as z:
            for inner in z.namelist():
                if inner.endswith((".xml", ".md", ".txt", ".json", ".html", ".py", ".csv")):
                    yield rel + "!" + inner, z.read(inner).decode("utf-8", "replace")
        return
    try:
        with open(path, encoding="utf-8") as f:
            yield rel, f.read()
    except UnicodeDecodeError:
        return


def scan_text(label, text, problems, banned, check_style=True):
    loose, exact = banned
    low = text.lower()
    for i, s in enumerate(loose, 1):
        if s.lower() in low:
            problems.append(("private", label, "private string number %d on your list" % i))
    for w in exact:
        if re.search(r"\b" + re.escape(w) + r"\b", text):
            problems.append(("private", label, "a private whole-word string"))
    if not check_style:
        return
    for ch, name in DASHES.items():
        n = text.count(ch)
        if n:
            problems.append(("dash", label, "%d %s" % (n, name)))


def scan_git(problems, banned):
    if not os.path.isdir(os.path.join(ROOT, ".git")):
        return "no git repo"
    try:
        log = subprocess.run(
            ["git", "log", "--all", "-p", "--format=AUTHOR %an <%ae> COMMITTER %cn <%ce>%n%B"],
            cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace",
        ).stdout
    except FileNotFoundError:
        return "git not installed"
    if not log.strip():
        return "no commits yet"
    scan_text("git history", log, problems, banned, check_style=False)
    return "checked"


def scan_private_copies(folder, problems):
    hashes = set()
    for dirpath, _, filenames in os.walk(folder):
        for name in filenames:
            with open(os.path.join(dirpath, name), "rb") as f:
                hashes.add(hashlib.sha256(f.read()).hexdigest())
    for p in repo_files():
        with open(p, "rb") as f:
            if hashlib.sha256(f.read()).hexdigest() in hashes:
                problems.append(("copied", os.path.relpath(p, ROOT), "same bytes as a file in the private folder"))


def arg(name):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else None


def main():
    banned_path = arg("--banned")
    banned = load_banned(banned_path)
    problems = []
    count = 0
    for path in repo_files():
        if banned_path and os.path.abspath(path) == os.path.abspath(banned_path):
            continue
        for label, text in texts_of(path):
            count += 1
            scan_text(label, text, problems, banned)
    git_state = scan_git(problems, banned)
    if arg("--private-folder"):
        scan_private_copies(arg("--private-folder"), problems)

    print("Files and parts checked: %d" % count)
    print("Git history: %s" % git_state)
    if banned_path:
        print("Private strings searched: %d (from your list)" % (len(banned[0]) + len(banned[1])))
    else:
        print("Private strings: not checked (no --banned list given)")
    for kind in ("private", "dash", "copied"):
        hits = [p for p in problems if p[0] == kind]
        print("%-8s %d hit(s)" % (kind, len(hits)))
        for _, label, what in hits:
            print("    %s: %s" % (label, what))
    if problems:
        print("RESULT: FAIL")
        sys.exit(1)
    print("RESULT: CLEAN")


if __name__ == "__main__":
    main()
