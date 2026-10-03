# Stage 04: Hiring-manager outreach

**Off unless the user starts it by name in the session** ("run outreach"). Never as a side task of another stage. **Drafts only. The user sends every message.**

> **Site terms.** LinkedIn and some job boards forbid automated access in their terms. This stage never automates LinkedIn in any way: no scraping, no automated profile visits, no messages, no opening linkedin.com pages. It uses web search and the employer's own pages only. The user is responsible for following each site's terms.

## Purpose

A short, specific note to the person who runs the team can get an application read by someone who decides. This stage finds that person from public sources and drafts the note. The user decides whether and how to send it.

## Tracker access

- **Artifact:** read `listings` with `ArtifactData`. Write only the outreach columns and one history line, with `update`, after reading the row fresh and passing its `version` as `if_version`.
- **Spreadsheet:** the same columns in the `listings` tab of `my-files/job-search-tracker.xlsx`.

## Inputs

- `rules.md` and `my-files/my-rules.md`.
- Listings that qualify:
  - Status To apply (any date); Applied within the last 30 days (by `appliedDate`); Rejected within the last 30 days, only if the posting is still open on the employer's own site.
  - The level the user's rules name for outreach. If they name none, use mid level and up.
  - Pay at or above the user's floor. Listings with no posted pay are included, marked "pay unverified", and worked after posted-pay listings.
  - Skip excluded industries unless the employer's `keepAnyway` is yes.
  - *Example for sales roles (change it to fit the user):* mid level means account executive, account manager, territory manager, business development manager, sales consultant, or anything titled senior, strategic or enterprise. Not mid level: sales development, business development representative, associate, trainee, coordinator, support.
- `my-files/resume.md` for facts used in messages.

## Steps

1. Count the qualifying listings and tell the user the number before any research.
2. Work highest pay first, employers in the user's home metro before remote ones, 10 listings per session unless the user says otherwise.
3. Find the likely hiring manager: the manager or director over that team, not HR or recruiting. **Web search and the employer's own pages only.**
4. Never open a linkedin.com page. Store a public profile link only if it appeared in search results. The user opens it themselves.
5. Confidence: **high** when a public source names them over that team or region; **medium** when the title fits but the team or region is inferred; **low** when they are only a plausible senior leader at the company.
6. Email: record a work email only if it is publicly published. Otherwise note the company's email format if a public source documents it, marked "unverified". No paid lookup tools and no guessing beyond that.
7. Draft two versions per contact, in the user's writing style:
   - A connection note under 300 characters.
   - A longer message under 90 words, for email or after connecting.
   - Specific to the role and company. The ask is a 15-minute call about the team and what they look for. Not a referral request, and not "please look at my application". For To apply listings the user applies first, so the message can say they applied.
8. Save on the listing in the outreach columns only: `managerName`, `managerTitle`, `howIdentified`, `confidence`, `profileUrl`, `emailOrFormat`, `connectionNote`, `longMessage`. Never touch `status` or `yourNotes`.
9. Append one dated history line per listing worked this session, saying outreach was drafted.
10. Take an after snapshot and run `python tools/check_tracker.py check backups/before.json backups/after.json --stage outreach` (snapshots: `references/tracker-columns.md`, "Checking by script").

## Outputs

- Outreach columns filled on each researched listing.
- A report saved to `reports/outreach-<YYYY-MM-DD>.md`: each contact, confidence, and anything the user should know (wrong place, posting closed).

## Done when

- [ ] The user started this stage by name in this session.
- [ ] No LinkedIn page was opened and nothing was sent.
- [ ] Every connection note is under 300 characters and every message under 90 words, with no em dashes or en dashes.
- [ ] Only the outreach columns and history were written (`check_tracker.py`).

**The user sends every message. The session never sends anything.**
