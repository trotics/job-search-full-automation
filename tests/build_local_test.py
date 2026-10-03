"""Build a local test copy of the tracker page that runs against the stand-in database.

Usage:
  python tests/build_local_test.py tests/sample-data/tracker-after-fit.json
  python tests/build_local_test.py --empty

Writes tests/build/tracker-test.html. Open it in a browser (or serve the repo folder with
`python -m http.server 8765` and open http://localhost:8765/tests/build/tracker-test.html).
The published artifact never uses these files.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(ROOT, "tracker", "tracker-page.html")
STAND_IN = os.path.join(ROOT, "tests", "stand-in-db.js")
OUT_DIR = os.path.join(ROOT, "tests", "build")


def main():
    if "--empty" in sys.argv:
        data = {"companies": [], "coverage": [], "listings": [], "answers": [], "settings": []}
        name = "tracker-test-empty.html"
    else:
        with open(sys.argv[1], encoding="utf-8") as f:
            data = json.load(f)
        name = "tracker-test.html"
    with open(PAGE, encoding="utf-8") as f:
        page = f.read()
    with open(STAND_IN, encoding="utf-8") as f:
        stand_in = f.read()
    inject = (
        "<script>window.STAND_IN_DATA=" + json.dumps(data).replace("</", "<\\/") + ";</script>\n"
        "<script>" + stand_in + "</script>\n"
    )
    marker = "<script>\n(function(){"
    if marker not in page:
        sys.exit("Could not find the page script to insert the stand-in before.")
    page = page.replace(marker, inject + marker, 1)
    os.makedirs(OUT_DIR, exist_ok=True)
    out = os.path.join(OUT_DIR, name)
    with open(out, "w", encoding="utf-8") as f:
        f.write(page)
    print("Wrote", os.path.relpath(out, ROOT))


if __name__ == "__main__":
    main()
