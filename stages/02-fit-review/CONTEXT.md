# Stage 02: Fit review

Decide whether one posting goes in the tracker. A sweep runs this for every new posting. The user can also hand you a posting link and ask for a fit call.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| User or sweep | The posting, read on the employer's own site, or pasted by the user | Title, location detail, pay, requirements, work type | What is being judged |
| Stage 00 | `../00-intake/output/my-rules.md` | Full file | The user's rules |
| Shared | `../../shared/rules.md` | Sections 1 to 6 | The checks |
| Shared | `../../shared/my-setup.md` | Full file | Tracker kind and location, Python command, browser, email connector |
| Shared | `../../shared/tracker-access.md` | Full file | Reading, writing and the check |
| Shared | `../../shared/recurring-mistakes.md` | Full file | Read before any tracker write |
| Shared | `../../shared/adding-employers.md` | Full file | When the employer is not on the target list |
| Shared | `../../shared/next-steps.md` | "After a sweep or a fit call", "After a close-call decision" | What to suggest when the session ends |
| Shared | `../../shared/lessons.md` | Full file | Learning from this session |
| Tracker | `listings`, `companies`, `settings`, `coverage` | That employer's rows | Duplicates, spelling, settings lists |
| Previous runs | `../01-sweep/output/`, `output/` | The latest report | Close calls waiting for a decision |
| Reference | `references/fit-outcomes.md` | Full file | What to write for each result |

## Process

1. Take a tracker snapshot, unless a sweep already took one this session.
2. **Employer not on the target list** (for example the user pasted a link): ask whether to add it. If yes, add it as `adding-employers.md` says, then go on. If no, give the fit call in chat only and write nothing.
3. Check in this order. The first failure decides:
   1. **Duplicate?** Same req id, or same title and location at the same employer, already in `listings`: stop, nothing to add.
   2. **Live on the employer's own site?** If the site shows it gone: no. If you cannot open the site (no browser, or the person pasted the text), judge it on the pasted text, say "not confirmed live", and ask for the employer's link before writing a listing.
   3. **Target role?** Not one of the user's target roles, or one of their "out" roles: no (rules 1).
   4. **Industry and product?** An "out" industry, or an excluded industry without `keepAnyway`: no (rules 1).
   5. **Place?** Fails the user's place rules: no (rules 4).
   6. **Pay?** Under the floor: no. No posted pay: decide plausibility and write the reasoning (rules 2).
   7. **Hard requirements?** License before hire, a specific degree the user lacks, any hard no in the user's rules: no. Required years inside the user's stretch never fail it on their own (rules 3).
   8. **On-hold employer?** Add the listing, set `priority` to `On hold`, and say so in `why`.
4. Follow the user's autonomy lines in `my-rules.md`: if they want to be asked before listings are written, show each result and wait for their yes before writing. "Bring me every close call" applies only to close calls; clear fits are written as usual.
5. Write the result as `references/fit-outcomes.md` says: a new listing, a skipped line, or a report item for the user.
6. If no sweep is running, take an after snapshot and run the check with `--stage fit`.
7. If no sweep is running: ask once what this session taught (`lessons.md`) and add any lesson the person approves, then end by suggesting the next step (`next-steps.md`, "After a sweep or a fit call"). Inside a sweep, the sweep does this.

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 2 | Whether to add an employer not on the target list | Add it, or a chat-only fit call |
| 3 | Each result, when the user's autonomy lines say to ask | Write it, or not |
| 5 | Close calls that depend on taste, in the report | Apply or skip |

## Audit

| Check | Pass Condition |
|-------|---------------|
| Every posting | Ends as a new listing, a skipped line, or a report item for the user |
| No Review fit | No listing was created at Review fit; close calls are in the report instead |
| Columns | Every new listing has every column in `fit-outcomes.md`, including `postingText`, and a unique `id` |
| Check | `check_tracker.py` passes (`--stage fit`, or the sweep's own check) |
| Lessons | The person was asked once what the session taught; only approved lessons were added |
| Next step | The session ended with the next thing to say, in quotes |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| New listing | Tracker, `listings` | One row at To apply |
| Skipped line | Tracker, `coverage.skipped` | Title, req id, reason |
| Fit report | Inside a sweep: the sweep report. Run alone: `output/[YYYY-MM-DD]-fit-report.md`, always | Each posting and its result; close calls in the seven-part shape in `fit-outcomes.md` |
