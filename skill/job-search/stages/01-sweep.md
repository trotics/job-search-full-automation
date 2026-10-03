# Stage 01: Sweep

Check employers for new listings, and confirm that listings already in the tracker are still open. The user starts every sweep. Nothing here runs on a schedule.

> **Site terms.** LinkedIn and some job boards forbid automated access in their terms. A sweep reads employers' own career sites only. It never opens LinkedIn and never uses an aggregator as a source of truth. The user is responsible for following each site's terms.

## Tracker access

- **Artifact:** read `companies`, `coverage`, `listings` and `settings` with `ArtifactData` (`list`). Write one row at a time with `update` (or `set` for a new row), after reading it fresh.
- **Spreadsheet:** read and write the tabs of the same names in `my-files/job-search-tracker.xlsx` with `tools/sheet.py` or openpyxl. Ask the user to close the file in Excel first.

## Inputs

- `rules.md` and `my-files/my-rules.md`.
- Tracker: `companies`, `coverage`, `listings`, `settings`.
- The session's scope, from the user: which employers, how many, or which listings to recheck. If the user gives no scope, offer: "the 10 employers swept longest ago, plus a recheck of every listing at To apply".

## Steps

0. **Adding employers (only when the user asks).** For each employer the user names, or each one you find for them by web search that fits their rules, find its own careers site. Add a `companies` row with `id` (the name in lowercase with hyphens, for example `example-health-co`; check no other row uses it), `company`, `careersSite`, `tier`, `industry`, `keepAnyway` no, `onHold` (yes if on hold in the user's rules), `added` today. Show the list to the user before saving it.
1. Read the scope. Skip employers whose `industry` is in `settings.excludedIndustries` unless `keepAnyway` is yes.
2. Take a snapshot of the tracker (see `references/tracker-columns.md`, "Checking by script"). If this run may write more than five rows, take a backup too (rules 7).
3. For each employer in scope:
   1. Open its own careers site or applicant tracking system. Never sign in, never create an account.
   2. Read every posting that could match the user's target roles. Read the requirements in full.
   3. For each posting not already in `listings`, run `stages/02-fit-review.md`.
   4. If the site will not load (bot check, CAPTCHA, a refused page), do not try to get past it. Set the employer's coverage `sweepState` to `manual`, `result` to `PENDING`, and start `detail` with "MANUAL:" plus the link and what failed.
   5. Update the employer's `coverage` row, or create it if the employer has none yet (same `id`, `company` and `industry` as in `companies`): `sweepDate` today, `sweepState` (`done` or `partial`), `result` (`HIT` if a listing was added, `NONE` if nothing fit, `LEAD` if something needs the user), and a dated line at the start of `detail`, with older text kept after "Earlier:". Add one line per skipped posting to `skipped`: title, req id, reason.
4. For each listing to recheck (**status To apply only**, never Applied or later):
   1. Open the posting on the employer's own site.
   2. If it is gone (removed, "no longer available", a filled message, or an error page plus no match when searching the site by req id), set `status` to `expired` or `filled` and append a `history` entry saying what showed it.
   3. If the employer's site cannot be read, leave the status alone and report the listing as unconfirmed.
   4. An aggregator showing a posting as gone is a lead to check, never proof.
5. **Helpers.** If you use research helpers (subagents) to read sites, give each about six employers, read only. Each helper opens its own browser tab and writes its findings to a file. The main session re-checks every posting against the rules, spot-checks at least one per helper on the employer's own site, and does every tracker write itself.
6. Take an after snapshot and run `python tools/check_tracker.py check backups/before.json backups/after.json --stage sweep` (snapshots: `references/tracker-columns.md`, "Checking by script"). Fix anything it reports before calling the stage done.

## Outputs

- New listings at To apply (from stage 02).
- Coverage rows updated for every employer touched.
- Listings set to expired or filled, each with a history entry.
- A report saved to `reports/sweep-<YYYY-MM-DD>.md`: employers checked, new listings, listings expired or filled, manual employers, anything unconfirmed, and calls for the user.

## Done when

- [ ] Every employer in scope has a dated coverage entry, or is listed in the report as not reached.
- [ ] Every new listing passed stage 02 and has all its required columns.
- [ ] No listing at Applied, Followed up, Interview or Offer was changed (`check_tracker.py`).
- [ ] No status change rests on aggregator evidence.
- [ ] `yourNotes` untouched on every row (`check_tracker.py`).
- [ ] Backup taken if more than five rows were written.
- [ ] Report saved.
