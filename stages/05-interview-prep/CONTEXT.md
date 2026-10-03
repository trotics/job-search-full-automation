# Stage 05: Interview prep

Prepare the user for a named interview. Run when the user asks.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| User | Which interview, its stage, who they meet | The request | What to prepare for |
| Stage 00 | `../00-intake/output/my-rules.md` | Writing style | How the file reads |
| Stage 07 | `../07-resume/output/resume.md` | Full file | The user's stories come only from their own record |
| Shared | `../../shared/my-setup.md` | Full file | Tracker kind and location, Python command, browser, email connector |
| Shared | `../../shared/tracker-access.md` | Full file | Only for the optional history line |
| Shared | `../../shared/recurring-mistakes.md` | Full file | Read before any tracker write |
| Shared | `../../shared/next-steps.md` | "After interview prep" | What to suggest when the session ends |
| Tracker | `listings` (that listing), `answers` (Work history) | One row; work history entries | The saved posting, the history, the user's record |
| Reference | `references/prep-sources-and-format.md` | Full file | Which sources count, and what the file holds |

## Process

1. Confirm with the user which interview, the stage (phone screen, hiring manager, panel, onsite), the date, and who they are meeting, if known. If the listing is not at Interview yet, offer to set it, and ask when they applied so `appliedDate` is filled too (a direct request, `shared/tracker-access.md`, checked with `--stage user`).
2. Read the listing (artifact: `get`; spreadsheet: `sheet.py show`). Read its `postingText`.
3. Build the company brief from allowed sources only, every fact linked.
4. List the likely questions, including the hard ones the user's record invites.
5. Map each question to a true story from the resume or the answer bank. Mark every gap.
6. Add questions for the user to ask, and the logistics from the listing's history.
7. Run the audit below, then save the file and give the user its path.
8. If the user wants it, add one history line saying prep was done, with a snapshot before and after and the check with `--stage prep`.
9. End by suggesting the next step in one or two lines (`next-steps.md`, "After interview prep"). Suggest only; do not start it.

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 1 | Which interview and stage | Confirm or correct |
| 5 | Gaps where no true story fits | Fill the gap, or leave it marked |

## Audit

| Check | Pass Condition |
|-------|---------------|
| Company facts | Every fact about the company has a link to an allowed source |
| Stories | Every story is one the user has stated or the resume shows |
| Saved | The file is saved in `output/` and the user has the path |
| Next step | The session ended with the next thing to say, in quotes |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Prep file | `output/[company-slug]-[interview date YYYY-MM-DD]-interview-prep.md` | Markdown, in the five parts of `prep-sources-and-format.md` |
| History line (optional) | Tracker, `listings` | One line saying prep was done |
