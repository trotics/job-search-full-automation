# Sweep procedure

The detail behind each step of the sweep. Board-by-board reading is in `board-techniques.md` and `board-platforms.md`.

> **Site terms.** LinkedIn and some job boards forbid automated access in their terms. A sweep reads employers' own career sites only. It never opens LinkedIn and never uses an aggregator as a source of truth. The user is responsible for following each site's terms.

## Scope

- From the user: which employers, how many, or which listings to recheck. If the user gives no scope, offer: "the 10 employers swept longest ago, plus a recheck of every listing at To apply".
- Skip employers whose `industry` is in `settings.excludedIndustries` unless `keepAnyway` is yes.
- Work only inside the target list. Employers you happen to find along the way go on a "candidates" list in the report, not into the sweep.
- `coverage` is the checkpoint: a sweep that stopped part way resumes at the first employer whose `sweepState` is `not swept` or `partial`.

## Reading one employer

1. Open its own careers site or applicant tracking system. Never sign in, never create an account. Use the board's section in `board-platforms.md`.
2. **Search by department, not only by title.** Open the board's categories that hold the user's target roles (for example Sales, Customer Service, Operations, Finance) and read every entry to mid level posting in them; titles vary too much between employers for a title search alone. Then read every posting that could match the user's target roles, with its requirements in full, and its **own** location text (many boards misreport location).
3. Large boards: read them in parts and record how far you got in `sweepProgress`, with `sweepState` `partial`.
4. A posting is new if no row in `listings` has its job number, or its title and location at that employer.
5. **If the site will not load,** first try the known workarounds (the board's public feed, an alternate host, the sitemap). If they fail, do not try to get past anything. Set `sweepState` to `manual`, `result` to `PENDING`, and start `detail` with "MANUAL:" plus the link and which kind of failure it was: a **bot check** (the user can usually open it in their own browser), a **browser refusal** (the browser tool will not open the site), or a **structural absence** (the employer has no postings of its own). Never remove an employer from the target list because its site was hard to reach.

## The coverage row

Update the employer's `coverage` row, or create it if the employer has none yet (same `id`, `company` and `industry` as in `companies`):

- `sweepDate`: today.
- `sweepState`: `done` or `partial`.
- `result`: `HIT` if a listing was added, `NONE` if nothing fit, `LEAD` if something needs the user.
- `detail`: a dated line at the start, with older text kept after "Earlier:".
- `skipped`: one line per skipped posting: title, req id, reason.

## Rechecking listings (status To apply only)

1. Open the posting on the employer's own site.
2. **Gone:** a "no longer available" or filled message; HTTP 410; on Workday a 403 on the job plus no match for the job number on the board; a Greenhouse job link that redirects to the general careers page; the job number missing from a search of the whole board while the page will not load. Set `status` to `expired` (or `filled` when the employer says filled) and append a `history` entry naming exactly what showed it.
3. **Not proof on its own:** a 404 on a saved address (job addresses change with titles: search the job number first); a slow or "initializing" page (wait and reload); one of two pages for the same job showing it closed (trust the page with an explicit closed or filled message); an aggregator showing it closed; the employer rejecting the user (the posting can stay live). Look again before changing anything.
4. **Fast-turnover boards:** a job can vanish between two reads minutes apart. Confirm twice.
5. If the employer's site cannot be read, leave the status alone and report the listing as unconfirmed.
6. Never touch a listing at Applied, Followed up, Interview or Offer, even if its posting is gone.

## Budget

Stop starting new employers at about 150 tool calls in the main session, so there is room to check, write and report. Record where you stopped in `coverage`; the next sweep resumes there.

## The report

Employers checked, new listings, listings expired or filled, manual employers, anything unconfirmed, candidates found along the way, and calls for the user.
