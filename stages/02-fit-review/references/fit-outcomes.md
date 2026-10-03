# Fit outcomes

What to write for each result of a fit review. Column meanings are in `shared/tracker-columns.md`.

## Pass: a new listings row

- `id`: `<company-slug>-<req id or short title slug>`, lowercase, letters, numbers and hyphens only. Check no other row uses it.
- `company`: spelled exactly as in `companies`.
- `title`, `location` (the posting's own location detail), `url` (employer's own site), `reqId`, `industry`, `posted` (date as shown, or blank).
- `pay`: the posted pay as written, or "not posted".
- `why`: one or two sentences on the fit, any reach (years, industry), and anything the user should know.
- `teaches`: what the role would teach the user, starting "Stated:" (the posting says so), "Not stated." or "Not read."
- `family`: one of `settings.roleFamilies`, written without the `*`. `track`: one of `settings.tracks`.
- `priority`: `High` (clear fit, pay at or above the floor), `Medium` (fits with a reach), `Low` (fits on paper, weaker on taste or pay), or `On hold`.
- `postingText`: the posting's full text, copied from the employer's own page (title, location, pay, duties, requirements). This lets later stages work after the posting is taken down. If the page is too long, keep at least the duties, requirements and pay.
- `status`: `To apply`.
- `history`: `YYYY-MM-DD added from the employer's own site by fit review.` If it was judged on pasted text: `YYYY-MM-DD added from pasted posting text by fit review; not confirmed live on the employer's site.`, and `why` ends with "Not confirmed live."
- `yourNotes`: leave empty.

## Fail

One line in the employer's `coverage.skipped`: title, req id, reason. Run alone, for an employer with no `coverage` row: record the skip only in the fit report, and never create a coverage row outside a sweep (a coverage row means the employer was swept).

## A matter of taste, not a rule

For example a commission-only role when the user's rules say nothing about commission. Do not add it. List it in the session report for the user, in this shape, so they can decide from it alone:

1. **Flag:** what made it a close call.
2. **Posting says:** the exact requirement or fact, quoted short, marked required or preferred.
3. **You have:** how the user's background compares, from the resume, the answer bank and the experience section of `my-rules.md` only.
4. **Teaches:** what the role would build.
5. **Pay and next step:** posted pay or "not posted", and any named next role.
6. **Lean:** Apply or Skip, with one sentence of reasoning.
7. **Decide:** the one question the user needs to answer.

## The person decides a close call

When the person answers a close call (in the session or a later one), record it, so it is never asked again. Take a snapshot first and check with `--stage fit` after.

- **Apply:** first re-open the posting on the employer's own site to confirm it is live and copy `postingText` (if it cannot be opened, ask for the employer's link first, as in the CONTEXT step on pasted postings, and record "not confirmed live"). Then write the listing as in "Pass", with history `YYYY-MM-DD added after the user's close-call decision.` (add "; not confirmed live on the employer's site" when it was judged on pasted text) If the employer has a `coverage` row, set its `result` to `HIT`.
- **Skip:** if the employer has a `coverage` row, add `title, req id, skipped by the user's decision YYYY-MM-DD` to its `skipped` and set `result` to `NONE` unless something else there is still waiting. Keep every earlier line of `skipped` when you add one (read the cell fresh and write it back with the new line at the end), and add a dated line to the start of `detail` saying the close call was decided. If it has no coverage row, do not create one: add `YYYY-MM-DD decided: skip` under that close call in its report instead (with no folder, give the updated report as a download so the mark is kept).

A close call that is already a listing and that the person now drops is a status change to `Closed`: do it as a direct request with its own snapshot and a `--stage user` check (`shared/tracker-access.md`, "Direct requests"), not inside the `--stage fit` check.

A close call counts as decided when its req id (or, with none, its title and location) is in `listings` or `coverage.skipped`, or its report marks it decided.

## A closed listing that is live again

Do not reopen it. List it in the report. The user decides.
