# Stage 01: Sweep

Check employers for new listings, and confirm that listings already in the tracker are still open. The user starts every sweep. Nothing here runs on a schedule.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| User | The session's scope | Employers, count, or listings to recheck | What this sweep covers |
| Stage 00 | `../00-intake/output/my-rules.md` | Full file | The user's rules |
| Shared | `../../shared/rules.md` | Full file | Rules for every stage |
| Shared | `../../shared/my-setup.md` | Full file | Tracker kind and location, Python command, browser, email connector |
| Shared | `../../shared/tracker-access.md` | Full file | Reading, writing, backups and the check |
| Shared | `../../shared/recurring-mistakes.md` | Full file | Read before any tracker write |
| Shared | `../../shared/adding-employers.md` | Full file | Only when the user asks to add employers |
| Shared | `../../shared/helpers.md` | Full file | Only if you use research helpers |
| Shared | `../../shared/next-steps.md` | "After a sweep or a fit call" | What to suggest when the session ends |
| Shared | `../../shared/lessons.md` | Full file | Learning from this session |
| Tracker | `companies`, `coverage`, `listings`, `settings` | All rows in scope | The target list and what is known |
| Stage 02 | `../02-fit-review/CONTEXT.md` | Full file | Run for every new posting |
| Reference | `references/sweep-procedure.md` | Full file | Scope, reading, coverage rows, rechecks, budget |
| Reference | `references/board-techniques.md` | Full file | Ground rules, location traps, signs a posting is gone |
| Reference | `references/board-platforms.md` | The section for each board | Read before reading that board |

## Process

1. Take a tracker snapshot before writing anything. If this run may write more than five rows on the spreadsheet, take a backup too (for the artifact tracker the before snapshot counts).
2. If the user asked to add employers, add them as `adding-employers.md` says.
3. Agree the scope with the user (`sweep-procedure.md`, "Scope").
4. For each employer in scope, read its own board (`sweep-procedure.md`, "Reading one employer").
5. Run stage 02 on every new posting.
6. Update the employer's `coverage` row.
7. Recheck each listing in scope at To apply (`sweep-procedure.md`, "Rechecking listings").
8. Take an after snapshot and run the check with `--stage sweep`. Fix anything it reports.
9. Run the audit below, then save the report.
10. Ask once what this session taught (`lessons.md`) and add any lesson the person approves. Then end by suggesting the next step in one or two lines (`next-steps.md`, "After a sweep or a fit call"). Suggest only; do not start it.

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 2 | Employers to add, with their careers sites | Which to add |
| 3 | The proposed scope | Go, or a different scope |

Stage 02 follows the user's autonomy lines and asks before writing when they say so. Paths in stage 02's file are relative to `stages/02-fit-review/`.

## Audit

| Check | Pass Condition |
|-------|---------------|
| Coverage | Every employer in scope has a dated coverage entry, or is listed in the report as not reached |
| Manual employers | Every one says which kind of failure it was (bot check, browser refusal or structural absence) |
| New listings | Every one passed stage 02 and has all its required columns |
| Protected listings | No listing at Applied, Followed up, Interview or Offer was changed (`check_tracker.py`) |
| Evidence | No status change rests on aggregator evidence |
| User's notes | `yourNotes` untouched on every row (`check_tracker.py`) |
| Backup | On the spreadsheet, taken if more than five rows were written |
| Lessons | The person was asked once what the session taught; only approved lessons were added |
| Next step | The session ended with the next thing to say, in quotes |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| New listings | Tracker, `listings` | Rows at To apply, from stage 02 |
| Coverage | Tracker, `coverage` | One updated row per employer touched |
| Expired or filled listings | Tracker, `listings` | Status changed, with a history entry |
| Sweep report | `output/[YYYY-MM-DD]-sweep-report.md` | Markdown, as `sweep-procedure.md` "The report" lists |
