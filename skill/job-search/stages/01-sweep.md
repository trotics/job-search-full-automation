# Stage 01: Sweep

Check employers for new listings, and confirm that listings already in the tracker are still open. The user starts every sweep. Nothing here runs on a schedule.

> **Site terms.** LinkedIn and some job boards forbid automated access in their terms. A sweep reads employers' own career sites only. It never opens LinkedIn and never uses an aggregator as a source of truth. The user is responsible for following each site's terms.

## Tracker access

- **Artifact:** read `companies`, `coverage`, `listings` and `settings` with `ArtifactData` (`list`). Write one row at a time with `update` (or `set` for a new row), after reading it fresh and passing its `version` as `if_version` (a new row needs none).
- **Spreadsheet:** read and write the tabs of the same names in `my-files/job-search-tracker.xlsx` with `tools/sheet.py` or openpyxl. Ask the user to close the file in Excel first.

## Inputs

- `rules.md` and `my-files/my-rules.md`.
- Tracker: `companies`, `coverage`, `listings`, `settings`.
- The session's scope, from the user: which employers, how many, or which listings to recheck. If the user gives no scope, offer: "the 10 employers swept longest ago, plus a recheck of every listing at To apply".
- `references/board-techniques.md`: how to read each kind of job board, which boards misreport location, and the signs that a posting is gone. Read the section for each board before reading it.

## Steps

0. **Snapshot first.** Before writing anything, including step 1, take a snapshot of the tracker (see `references/tracker-columns.md`, "Checking by script"). If this run may write more than five rows, take a backup too (rules 7).
1. **Adding employers (only when the user asks).** For each employer the user names, or each one you find for them by web search that fits their rules, find its own careers site. Add a `companies` row with `id` (the name in lowercase with hyphens, for example `example-health-co`; check no other row uses it), `company`, `careersSite`, `tier`, `industry`, `keepAnyway` no, `onHold` (yes if on hold in the user's rules), `added` today. Show the list to the user before saving it.
2. Read the scope. Skip employers whose `industry` is in `settings.excludedIndustries` unless `keepAnyway` is yes. Work only inside the target list: employers you happen to find along the way go on a "candidates" list in the report, not into the sweep. `coverage` is the checkpoint: a sweep that stopped part way resumes at the first employer whose `sweepState` is `not swept` or `partial`.
3. For each employer in scope:
   1. Open its own careers site or applicant tracking system. Never sign in, never create an account. Use the board's section in `references/board-techniques.md`.
   2. **Search by department, not only by title.** Open the board's categories that hold the user's target roles (for example Sales, Customer Service, Operations, Finance) and read every entry to mid level posting in them; titles vary too much between employers for a title search alone. Then read every posting that could match the user's target roles, with its requirements in full, and its **own** location text (many boards misreport location; see `references/board-techniques.md`).
   3. Large boards: read them in parts and record how far you got in `sweepProgress`, with `sweepState` `partial`.
   4. For each posting not already in `listings` (check by job number, and by title and location), run `stages/02-fit-review.md`.
   5. **If the site will not load,** first try the known workarounds in `references/board-techniques.md` (the board's public feed, an alternate host, the sitemap). If they fail, do not try to get past anything. Set `sweepState` to `manual`, `result` to `PENDING`, and start `detail` with "MANUAL:" plus the link and which kind of failure it was: a **bot check** (the user can usually open it in their own browser), a **browser refusal** (the browser tool will not open the site), or a **structural absence** (the employer has no postings of its own). Never remove an employer from the target list because its site was hard to reach.
   6. Update the employer's `coverage` row, or create it if the employer has none yet (same `id`, `company` and `industry` as in `companies`): `sweepDate` today, `sweepState` (`done` or `partial`), `result` (`HIT` if a listing was added, `NONE` if nothing fit, `LEAD` if something needs the user), and a dated line at the start of `detail`, with older text kept after "Earlier:". Add one line per skipped posting to `skipped`: title, req id, reason.
4. For each listing to recheck (**status To apply only**, never Applied or later):
   1. Open the posting on the employer's own site.
   2. Decide with the evidence rules in `references/board-techniques.md` ("Signs a posting is gone"):
      - **Gone:** a "no longer available" or filled message; HTTP 410; on Workday a 403 on the job plus no match for the job number on the board; a Greenhouse job link that redirects to the general careers page; the job number missing from a search of the whole board while the page will not load. Set `status` to `expired` (or `filled` when the employer says filled) and append a `history` entry naming exactly what showed it.
      - **Not proof on its own:** a 404 on a saved address (job addresses change with titles: search the job number first); a slow or "initializing" page (wait and reload); one of two pages for the same job showing it closed (trust the page with an explicit closed or filled message); an aggregator showing it closed; the employer rejecting the user (the posting can stay live). Look again before changing anything.
      - **Fast-turnover boards:** a job can vanish between two reads minutes apart. Confirm twice.
   3. If the employer's site cannot be read, leave the status alone and report the listing as unconfirmed.
   4. Never touch a listing at Applied, Followed up, Interview or Offer, even if its posting is gone. Stage 06 or the user handles those.
5. **Helpers.** If you use research helpers (subagents) to read sites, follow "Working with helpers" in `references/board-techniques.md`: about six employers each, a cap of about 50 tool calls, read only, each in its own browser tab, findings written to a file with quoted requirement lines. The main session re-checks every posting against the rules, spot-checks at least one per helper on the employer's own site, and does every tracker write itself.
   **Session budget:** stop starting new employers at about 150 tool calls in the main session, so there is room to check, write and report. Record where you stopped in `coverage`; the next sweep resumes there.
6. Take an after snapshot and run `python tools/check_tracker.py check backups/before.json backups/after.json --stage sweep` (snapshots: `references/tracker-columns.md`, "Checking by script"). Fix anything it reports before calling the stage done.

## Outputs

- New listings at To apply (from stage 02).
- Coverage rows updated for every employer touched.
- Listings set to expired or filled, each with a history entry.
- A report saved to `reports/sweep-<YYYY-MM-DD>.md`: employers checked, new listings, listings expired or filled, manual employers, anything unconfirmed, and calls for the user.

## Done when

- [ ] Every employer in scope has a dated coverage entry, or is listed in the report as not reached.
- [ ] Every manual employer says which kind of failure it was (bot check, browser refusal or structural absence).
- [ ] Every new listing passed stage 02 and has all its required columns.
- [ ] No listing at Applied, Followed up, Interview or Offer was changed (`check_tracker.py`).
- [ ] No status change rests on aggregator evidence.
- [ ] `yourNotes` untouched on every row (`check_tracker.py`).
- [ ] Backup taken if more than five rows were written.
- [ ] Report saved.
