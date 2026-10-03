# Stage 08: Company research

Research sessions the user starts by asking. Four kinds:

| Kind | The user says something like | Writes to the tracker |
|---|---|---|
| A. Find employers | "Suggest employers that fit my background" | New `companies` rows, after the user approves each one |
| B. Company deep dive | "Tell me about [company]" | Nothing (a report only) |
| C. Industry map | "Map the [industry] employers around [place]" | Nothing, unless the user then asks to add some (run A for those) |
| D. Role research | "What does a [title] do, and what does it pay around here?" | Nothing (a report only) |

Ready-to-use wording for each is in `references/prompts.md`.

> **Site terms.** LinkedIn and some job boards forbid automated access in their terms. Research uses web search, employers' own websites, and public lists. It never opens LinkedIn, never scrapes a site, and never signs in anywhere. Job aggregators are used only to learn company names, never as proof that a job exists. The user is responsible for following each site's terms.

## Rules for every research session

- **Sources:** web search results, employers' own sites (including careers and locations pages), and public lists: business journal and newspaper lists, chamber of commerce directories, economic development agency lists, industry association member lists, conference exhibitor lists, government data, company press releases. **No paid tools, no sign-ins, no LinkedIn.**
- **Every fact gets a link.** If you cannot link it, do not state it as fact.
- **Exact names.** Use the company's own spelling. Check the target list for an exact match before calling anyone new (`recurring-mistakes.md` item 7).
- **Never suggest** the user's current employer, anyone on their never-contact list, or employers in an excluded industry unless the user asks.
- **Helpers:** if you use research helpers, give each about six companies, read only, each in its own browser tab. The main session checks every result and does every write.
- **Size:** about 25 candidates per session at most, so each one gets checked properly.
- Save a report to `reports/research-<kind>-<YYYY-MM-DD>.md` with every source linked.

## A. Find employers (target list building)

1. **Start from the rules.** Read the user's target roles, industries "in", place rules and excluded industries. Say in one line what you will look for, for example: "Health tech and digital health employers with offices in Larkfield, or remote roles open to Calder."
2. **Search in this order**, and note which source each name came from:
   1. Local lists: largest employers, fastest growing, best places to work, published by local business journals, newspapers, chambers of commerce and economic development agencies for the user's metro.
   2. Industry lists: association member directories, conference exhibitor and sponsor lists, and "top companies" lists for each industry the user wants.
   3. Neighbors of good fits: competitors, partners and customers of employers already on the target list (from their own sites and press releases).
   4. Remote-friendly employers: companies in the user's industries whose own careers pages show remote roles open to the user's state.
   5. Job search engines, read by hand from public search results, **only to learn company names** that post the user's target titles nearby. Never as proof that a job exists.
3. **Check every candidate** before showing it:
   - Its own careers site exists and opens. Record the link.
   - Its industry, in the words of `settings.industryOrder` where it fits.
   - It has a presence the user's place rules allow: an office in the home metro, a territory covering it, or remote roles open to the user's state. Say which, with a link.
   - It is not already on the target list (exact name), not excluded, not the current employer, not on the never-contact list.
   - It plausibly hires the user's target role. Say why in one line.
4. **Show the candidates in one table**: company, industry, proposed tier (using the user's tier meanings from `settings`), careers site, why it fits, source. Ask the user to approve, drop or change each one.
5. **Write only the approved ones** to `companies`: `id` (lowercase name with hyphens), `company`, `careersSite`, `tier`, `industry`, `keepAnyway` no, `onHold` (yes only if the user's rules put it on hold), `added` today.
6. Snapshot before and after (see `references/tracker-columns.md`, "Checking by script"), and run `python tools/check_tracker.py check backups/before.json backups/after.json --stage research`.
7. Offer a sweep of the new employers. Do not start one unless the user says yes.

## B. Company deep dive

For one employer the user names (often before applying or before an interview).

1. What they sell, to whom, and how (their own site).
2. Size, locations, and where the user's target role sits (their own site, press releases, government filings for public companies).
3. Recent news from the last 12 months (established news outlets and trade publications).
4. Open roles that match the user's targets, from their own careers site, with links.
5. How the user's background fits, in two or three plain sentences, using only the user's stated facts.
6. Questions worth asking them.
7. Save `reports/research-company-<company-slug>-<YYYY-MM-DD>.md`.

## C. Industry map

For one industry in or near the user's place.

1. List the main employers in that industry that the user's place rules allow, grouped by type (for example software vendors, insurers, service firms), each with a link and one line on what they do.
2. Mark which are already on the target list.
3. Note which roles in that industry match the user's targets, and where they usually sit (sales team, clinical team, operations).
4. Save the report. To add any to the target list, run part A for those names.

## D. Role research

For one job title the user asks about.

1. What the role does day to day, from three or more employers' own postings, each linked.
2. What those postings require and prefer, and how that compares with the user's stated experience (facts only).
3. Pay: only pay **posted by employers** for this role in the user's area or remote roles open to them. Give the range and the number of postings it comes from. If fewer than three postings show pay, say so. Never estimate a number without a posting behind it.
4. Typical next roles, if postings or employers' own career pages say so.
5. Save the report.

## Outputs

- Part A: approved `companies` rows, and a report.
- Parts B, C, D: a report only.

## Done when

- [ ] Every fact in the report has a link to an allowed source.
- [ ] No LinkedIn page was opened, no site required a sign-in, nothing was scraped.
- [ ] Part A: every new employer was approved by the user, has its own careers site link, and matches no existing name, excluded industry or never-contact entry. `check_tracker.py` passes.
- [ ] Report saved.
