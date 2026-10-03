---
name: job-search
description: Runs a job search with the user. Use for the setup interview, resume building, finding and researching employers, sweeps of employer career sites, fit calls on postings, applications, hiring-manager outreach drafts, interview prep, and mailbox checks that read or write the user's job search tracker.
---

# Job search: the map

This Skill helps one person run their job search. It builds a resume from the user's own facts, finds and researches employers, finds openings on employers' own career sites, decides which ones fit the user's rules, keeps a tracker up to date, fills in applications with the user, drafts outreach for the user to send, and prepares the user for interviews.

The user stays in charge. Claude never submits an application without the user's review, never sends a message, and never handles passwords, codes, ID numbers or CAPTCHAs.

## Where things live

Everything personal lives in the user's **job search folder**, not in this Skill:

| What | Where |
|---|---|
| The user's own rules (target roles, place, pay, industries and the rest) | `my-files/my-rules.md` |
| Resume to upload | `my-files/resume.pdf` |
| Resume as text, for filling forms | `my-files/resume.md` |
| Facts the resume is built from (stage 07) | `my-files/resume-facts.md` |
| Tailored resumes for single listings | `my-files/resumes/` |
| Session reports and interview prep | `reports/` |
| Backups of the tracker | `backups/` |

**No job search folder?** On Claude on the web or a tablet there may be no folder Claude can read and write. Then: ask the user to attach `my-rules.md` (and `resume-facts.md` for stage 07) at the start of each chat, or keep them in the files of a Claude Project so every chat sees them. Give every file you create or change as a download, and tell the user to save it and attach it next time. Stages that need a browser Claude can control (sweeps of most career sites, and applying) need the desktop app.

**The tracker** is the single source of truth for employers, sweeps, listings, status and the answer bank. It is one of two kinds. `my-rules.md` says which one, and where:

- **Artifact tracker (main):** a Claude artifact page the user published from `tracker-page.html`, with its own database. Read and write it with the `ArtifactData` tool, using the artifact link in `my-rules.md`. Collections: `companies`, `coverage`, `listings`, `answers`, `settings`.
- **Spreadsheet tracker (fallback):** `my-files/job-search-tracker.xlsx`, with tabs of the same names and the same columns. Read and write it with Python and openpyxl, or with `tools/sheet.py` when the repo is in the folder. The user must close the file in Excel before a session writes to it.

Every column is described in `references/tracker-columns.md`. The two trackers use the same names, so every rule in this Skill applies to both.

If the tracker and a file disagree on status, the tracker wins. If anything disagrees with `rules.md` or `my-rules.md`, those win. If `rules.md` and `my-rules.md` disagree, `my-rules.md` wins for the user's own preferences (roles, place, pay, industries) and `rules.md` wins for safety. Safety rules never bend.

## Every session

1. If `my-files/my-rules.md` does not exist, the user is new. Run `stages/00-intake.md` and nothing else.
2. If `my-rules.md` exists but has no working tracker link or file, set up the tracker with the user first (intake question 1 says how) before any stage that writes.
3. Read `rules.md` (this Skill) and `my-files/my-rules.md` in full. They apply to every stage.
4. Load only the stage file for the task:

| Task | Load |
|---|---|
| First-time setup, or the user wants to change their rules | `stages/00-intake.md` |
| Check employers for new listings, confirm listings are still open | `stages/01-sweep.md` |
| Decide whether a posting fits | `stages/02-fit-review.md` (the sweep calls it) |
| Fill in applications for listings at To apply, with the user | `stages/03-apply.md` |
| Hiring-manager outreach drafts (only when the user starts it by name) | `stages/04-outreach.md` |
| Prepare for an interview | `stages/05-interview-prep.md` |
| Check the user's email for employer replies and update statuses | `stages/06-mailbox-check.md` |
| Build or improve a resume, or make a tailored version for one listing | `stages/07-resume.md` |
| Find employers, research a company, map an industry, research a role | `stages/08-company-research.md` |

5. Read `references/recurring-mistakes.md` before any tracker write.
6. Do only the task asked. Never start another stage on your own.
7. A stage is done only when every item on its "Done when" list is checked. Say plainly which items were not.
8. Every stage is started by the user in a live session. Nothing in this Skill runs on a schedule or unattended.

## Scripts

Stages run small Python scripts in `tools/` (in the user's job search folder) to check their work and build files. They need Python 3 with openpyxl and reportlab (`python -m pip install -r requirements.txt`). If Python or a package is missing, say so plainly and offer to install it. Never skip a check silently: a stage whose check could not run is not done.

## References

- `references/tracker-columns.md`: every tab and column, in plain words.
- `references/answer-bank.md`: how to use the answer bank.
- `references/application-techniques.md`: how upload controls and form auto-fill behave.
- `references/recurring-mistakes.md`: mistakes that have happened before.
- `references/sample-resume.md`: a made-up resume showing the format `my-files/resume.md` should follow.
- `references/resume-guide.md`: resume rules, examples by field, and the default (stage 07).
- `references/resume-facts-template.md`: the shape of the resume facts file (stage 07).
- `references/prompts.md`: what the user can say to start each kind of session.
