"""Build a plain, one-column resume PDF from stages/07-resume/output/resume.md.

Usage:
  python tools/build_resume.py stages/07-resume/output/resume.md stages/07-resume/output/resume.pdf

Needs reportlab (python -m pip install reportlab). The input format is in
stages/07-resume/references/resume-guide.md, "File format".
Prints the page count, so stage 07 can check the length limit.
"""
import os
import re
import sys
from xml.sax.saxutils import escape

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import HRFlowable, KeepTogether, Paragraph, SimpleDocTemplate, Spacer

INK = HexColor("#1F1F1F")
MUTED = HexColor("#555555")

S = {
    "name": ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=18, leading=22, textColor=INK),
    "contact": ParagraphStyle("contact", fontName="Helvetica", fontSize=10, leading=13, textColor=MUTED, spaceAfter=6),
    "h2": ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=11, leading=14, textColor=INK, spaceBefore=8, spaceAfter=2),
    "h3": ParagraphStyle("h3", fontName="Helvetica-Bold", fontSize=10.5, leading=13, textColor=INK, spaceBefore=6, spaceAfter=0),
    "meta": ParagraphStyle("meta", fontName="Helvetica", fontSize=10, leading=12.5, textColor=MUTED, spaceAfter=2),
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=10.5, leading=13.5, textColor=INK, alignment=TA_LEFT),
    "bullet": ParagraphStyle("bullet", fontName="Helvetica", fontSize=10.5, leading=13.5, textColor=INK,
                             leftIndent=12, bulletIndent=2, spaceAfter=1),
}


def job_line(text):
    """Title in bold on one line; employer, place and dates on the next, in grey."""
    parts = [p.strip() for p in text.split("|")]
    title = Paragraph("<b>%s</b>" % escape(parts[0]), S["h3"])
    if len(parts) < 2:
        return [title]
    rest = ", ".join(escape(p) for p in parts[1:-1])
    meta = (rest + " | " if rest else "") + escape(parts[-1])
    return [title, Paragraph(meta, S["meta"])]


def build(src, out):
    lines = open(src, encoding="utf-8").read().splitlines()
    story, block = [], []
    pages = {"n": 0}

    def flush():
        if block:
            story.append(KeepTogether(list(block)))
            block.clear()

    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            continue
        if line.startswith("# "):
            story.append(Paragraph(escape(line[2:].strip()), S["name"]))
        elif line.startswith("## "):
            flush()
            story.append(Paragraph(escape(line[3:].strip()).upper(), S["h2"]))
            story.append(HRFlowable(width="100%", thickness=0.6, color=MUTED, spaceBefore=1, spaceAfter=3))
        elif line.startswith("### "):
            flush()
            block.extend(job_line(line[4:].strip()))
        elif line.startswith("- "):
            (block if block else story).append(Paragraph(escape(line[2:].strip()), S["bullet"], bulletText="•"))
        elif not story or (len(story) == 1):
            story.append(Paragraph(escape(line.strip()), S["contact"]))
        else:
            flush()
            story.append(Paragraph(escape(line.strip()), S["body"]))
    flush()

    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)

    def count(canvas, doc):
        pages["n"] = doc.page

    doc = SimpleDocTemplate(out, pagesize=letter, leftMargin=0.7 * inch, rightMargin=0.7 * inch,
                            topMargin=0.6 * inch, bottomMargin=0.6 * inch,
                            title="Resume", author="", subject="", creator="")
    doc.build(story, onFirstPage=count, onLaterPages=count)
    return pages["n"]


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(2)
    n = build(sys.argv[1], sys.argv[2])
    print("Wrote %s: %d page%s" % (sys.argv[2], n, "" if n == 1 else "s"))


if __name__ == "__main__":
    main()
