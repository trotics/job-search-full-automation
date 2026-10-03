# Stage 02: Fit review

Decide whether one posting goes in the tracker. The sweep calls this for every new posting. The user can also hand you a posting link and ask for a fit call.

## Tracker access

- **Artifact:** read `listings`, `companies` and `settings` with `ArtifactData`. Add a new listing with `set` (a new id), and add skipped lines to the employer's `coverage` row with `update`.
- **Spreadsheet:** the same tabs and columns in `my-files/job-search-tracker.xlsx`. Add a new row at the bottom of `listings`.

## Inputs

- `rules.md` and `my-files/my-rules.md`.
- The posting, read on the employer's own site: title, location detail, pay, requirements, work type (full-time, part-time, contract).
- The tracker: existing listings for that employer, to avoid duplicates.
- **Employer not on the target list** (for example the user pasted a link): ask the user whether to add the employer. If yes, add its `companies` row first, exactly as sweep step 1 says, then review the posting. If no, give the fit call in chat only and write nothing.
- Take a snapshot before writing, and after writing run `python tools/check_tracker.py check backups/before.json backups/after.json --stage fit` (snapshots: `references/tracker-columns.md`, "Checking by script").

## Steps

Check in this order. The first failure decides.

1. **Duplicate?** Same req id, or same title and location at the same employer, already in `listings`: stop, nothing to add.
2. **Live on the employer's own site?** If not: no.
3. **Target role?** Not one of the user's target roles, or one of their "out" roles: no (rules 1).
4. **Industry and product?** An "out" industry, or an excluded industry without `keepAnyway`: no (rules 1).
5. **Place?** Fails the user's place rules: no (rules 4).
6. **Pay?** Under the floor: no. No posted pay: decide plausibility and write the reasoning (rules 2).
7. **Hard requirements?** License before hire, a specific degree the user lacks, any hard no in the user's rules: no. Required years inside the user's stretch never fail it on their own (rules 3).
8. **On-hold employer?** Add the listing, set `priority` to `On hold`, and say so in `why`.

## Outputs

- **Pass:** a new `listings` row with:
  - `id`: `<company-slug>-<req id or short title slug>`, lowercase, letters, numbers and hyphens only. Check no other row uses it.
  - `company`: spelled exactly as in `companies`.
  - `title`, `location` (the posting's own location detail), `url` (employer's own site), `reqId`, `industry`, `posted` (date as shown, or blank).
  - `pay`: the posted pay as written, or "not posted".
  - `why`: one or two sentences on the fit, any reach (years, industry), and anything the user should know.
  - `teaches`: what the role would teach the user, starting "Stated:" (the posting says so), "Not stated." or "Not read."
  - `family`: one of `settings.roleFamilies`. `track`: one of `settings.tracks`.
  - `priority`: `High` (clear fit, pay at or above the floor), `Medium` (fits with a reach), `Low` (fits on paper, weaker on taste or pay), or `On hold`.
  - `postingText`: the posting's full text, copied from the employer's own page (title, location, pay, duties, requirements). This lets later stages work after the posting is taken down. If the page is too long, keep at least the duties, requirements and pay.
  - `status`: `To apply`.
  - `history`: `YYYY-MM-DD added from the employer's own site by fit review.`
  - `yourNotes`: leave empty.
- **Fail:** one line in the employer's `coverage.skipped`: title, req id, reason.
- **A matter of taste, not a rule** (for example a commission-only role when the user's rules say nothing about commission): do not add it. List it in the session report for the user.
- **A closed listing that is live again:** do not reopen it. List it in the report. The user decides.

## Done when

- [ ] Every posting read ends as a new listing, a skipped line, or a report item for the user.
- [ ] No listings created at Review fit. Close calls go in the report instead.
- [ ] Every new listing has every column above, including `postingText`, and a unique `id`.
