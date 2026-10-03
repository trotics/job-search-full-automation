# Outreach rules

A short, specific note to the person who runs the team can get an application read by someone who decides. This stage finds that person from public sources and drafts the note. The user decides whether and how to send it.

> **Site terms.** LinkedIn and some job boards forbid automated access in their terms. Outreach never automates LinkedIn in any way: no scraping, no automated profile visits, no messages, no opening linkedin.com pages. It uses web search and the employer's own pages only. The user is responsible for following each site's terms.

## Which listings qualify

- Status To apply (any date); Applied within the last 30 days (by `appliedDate`); Rejected within the last 30 days, only if the posting is still open on the employer's own site.
- The level the user's rules name for outreach. If they name none, use mid level and up.
- Pay at or above the user's floor. Listings with no posted pay are included, marked "pay unverified", and worked after posted-pay listings.
- Skip excluded industries unless the employer's `keepAnyway` is yes.
- *Example for sales roles (change it to fit the user):* mid level means account executive, account manager, territory manager, business development manager, sales consultant, or anything titled senior, strategic or enterprise. Not mid level: sales development, business development representative, associate, trainee, coordinator, support.

## Order

Highest pay first, employers in the user's home metro before remote ones, 10 listings per session unless the user says otherwise.

## Finding the hiring manager

- The manager or director over that team, not HR or recruiting. **Web search and the employer's own pages only.**
- Never open a linkedin.com page. Store a public profile link only if it appeared in search results. The user opens it themselves.
- **Confidence:** **high** when a public source names them over that team or region; **medium** when the title fits but the team or region is inferred; **low** when they are only a plausible senior leader at the company, or when no one was found.
- **No one found:** leave `managerName` and `managerTitle` blank, write in `howIdentified` what was searched, set `confidence` to `low`, still draft both messages with a general greeting (for example "Hello [team] hiring team"), and say so in the report.
- **Email:** record a work email only if it is publicly published. Otherwise note the company's email format if a public source documents it, marked "unverified". No paid lookup tools and no guessing beyond that.

## The drafts

Two versions per contact, in the user's writing style:

- A connection note under 300 characters.
- A longer message under 90 words, for email or after connecting.
- Specific to the role and company. The ask is a 15-minute call about the team and what they look for. Not a referral request, and not "please look at my application". Say the user applied only if the listing's status is Applied or later. For a listing at To apply, write "I plan to apply" (or suggest they apply first).

## What to write in the tracker

Only the outreach columns: `managerName`, `managerTitle`, `howIdentified`, `confidence`, `profileUrl`, `emailOrFormat`, `connectionNote`, `longMessage`. Never `status` or `yourNotes`. One dated history line per listing worked, saying outreach was drafted.
