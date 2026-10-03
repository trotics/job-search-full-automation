"""Write tests/sample-data/maya-ortell-resume.pdf: a one-page made-up resume for the test user.

Plain PDF built by hand (no extra libraries). The text is stored uncompressed so the
test form can read it back, the way real "autofill from resume" buttons do.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "tests", "sample-data", "maya-ortell-resume.pdf")

LINES = [
    (18, "Maya Ortell"),
    (11, "Larkfield, Calder | maya.ortell@example.com | (555) 010-0142"),
    (11, ""),
    (12, "SUMMARY"),
    (11, "Registered nurse with six years in hospitals, three in intensive care, moving into"),
    (11, "healthcare technology sales. Trained new nurses on two charting systems."),
    (11, ""),
    (12, "EXPERIENCE"),
    (11, "Registered Nurse, Intensive Care Unit, Pinecrest Health System, Larkfield (2023 to present)"),
    (11, "- Super-user for the unit's move to new charting software; trained 30 nurses."),
    (11, "Registered Nurse, Medical-Surgical Unit, Pinecrest Health System, Larkfield (2020 to 2023)"),
    (11, "- Charge nurse on nights for a 32-bed unit."),
    (11, ""),
    (12, "EDUCATION"),
    (11, "Bachelor of Science in Nursing, Calder State University, 2020"),
    (11, ""),
    (12, "LICENSES"),
    (11, "Registered Nurse, State of Calder"),
    (11, ""),
    (10, "Made-up resume for software testing. Not a real person."),
]


def esc(s):
    return s.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def main():
    y = 760
    ops = ["BT"]
    for size, text in LINES:
        ops.append("/F1 %d Tf 1 0 0 1 56 %d Tm (%s) Tj" % (size, y, esc(text)))
        y -= size + 8
    ops.append("ET")
    stream = "\n".join(ops).encode("latin-1")
    objs = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>",
        b"<< /Length %d >>\nstream\n" % len(stream) + stream + b"\nendstream",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
    ]
    out = bytearray(b"%PDF-1.4\n")
    offsets = []
    for i, o in enumerate(objs, start=1):
        offsets.append(len(out))
        out += b"%d 0 obj\n" % i + o + b"\nendobj\n"
    xref = len(out)
    out += b"xref\n0 %d\n0000000000 65535 f \n" % (len(objs) + 1)
    for off in offsets:
        out += b"%010d 00000 n \n" % off
    out += b"trailer\n<< /Size %d /Root 1 0 R >>\nstartxref\n%d\n%%%%EOF\n" % (len(objs) + 1, xref)
    with open(OUT, "wb") as f:
        f.write(out)
    print("Wrote", os.path.relpath(OUT, ROOT), len(out), "bytes")


if __name__ == "__main__":
    main()
