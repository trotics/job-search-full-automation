# Tracker columns

The tracker has five parts. In the artifact tracker they are **collections** (each row is a record). In the spreadsheet tracker they are **tabs** (each row is a row). The names are the same in both, so every stage works with either.

Who writes: **Claude** means sessions may write it under the rules. **You** means only the user writes it. **Both** means the user may edit it, and sessions write it only as the stages say.

## companies: your target list

One row per employer.

| Column | What it holds | Who writes |
|---|---|---|
| `id` | A short name with no spaces, for example `example-health-co`. Never changes. | Claude |
| `company` | The employer's name, spelled exactly the same everywhere in the tracker. | Both |
| `careersSite` | Link to the employer's own job board. | Both |
| `tier` | `A`, `B` or `C`. What each letter means is in `settings`. | Both |
| `industry` | The employer's industry, using the same words as `settings.industryOrder` where it fits. | Both |
| `keepAnyway` | `yes` keeps this employer in sweeps even if its industry is excluded. Otherwise `no`. | You (Claude sets `yes` only when you ask for it) |
| `onHold` | `yes` means sweep it, but do not apply without your go-ahead. Otherwise `no`. | You (Claude sets it from your rules when adding an employer) |
| `added` | Date the employer was added, `YYYY-MM-DD`. | Claude |

## coverage: one row per employer, per sweep record

The `id` matches the employer's `id` in `companies`.

| Column | What it holds | Who writes |
|---|---|---|
| `id` | Same as the employer's `id`. | Claude |
| `company` | Same spelling as `companies`. | Claude |
| `industry` | Same as `companies`. | Claude |
| `sweepDate` | Date of the last sweep, `YYYY-MM-DD`. | Claude |
| `sweepState` | `done`, `partial`, `not swept` or `manual` (the site could not be read and needs you). | Claude |
| `result` | `HIT` (listing added), `NONE` (nothing fit), `LEAD` (something needs you), `PENDING` (not finished). | Claude |
| `detail` | What the sweep found. Newest first. Older findings are kept after "Earlier:". | Claude |
| `skipped` | One line per posting that did not fit: title, req id, reason. | Claude |
| `sweepProgress` | Optional note on a partial sweep, for example "read 2 of 5 pages". | Claude |

## listings: one row per job posting

| Column | What it holds | Who writes |
|---|---|---|
| `id` | A short name with no spaces, for example `example-health-co-r1234`. Never changes. | Claude |
| `company` | Same spelling as `companies`. | Claude |
| `title` | The job title as posted. | Claude |
| `location` | The posting's own location detail, not just "Remote". | Claude |
| `url` | Link to the posting on the employer's own site. | Claude |
| `reqId` | The employer's requisition or job number. | Claude |
| `industry` | Same as the employer's. | Claude |
| `track` | One of `settings.tracks`. Most people have one track. | Claude |
| `family` | The kind of role, one of `settings.roleFamilies`, written without the `*` (the `*` only marks targets in settings). | Claude |
| `posted` | Date posted, as shown. | Claude |
| `pay` | Posted pay exactly as written, or "not posted". | Claude |
| `why` | One or two sentences on why it fits, and any reach. | Claude |
| `teaches` | What the role would teach you. Starts with "Stated:", "Not stated." or "Not read." | Claude |
| `priority` | `High`, `Medium`, `Low` or `On hold`. Work order for applying. | Both |
| `status` | Where it stands. See the list below. | Both, under the rules |
| `appliedDate` | Date the application went in, `YYYY-MM-DD`. | Claude |
| `postingText` | The full text of the posting, saved so it survives after the posting comes down. | Claude |
| `reviewReason` | Why a listing at Review fit needs your call. | You (Claude only at your request) |
| `history` | Dated log of everything sessions did. **Add only, never change or delete.** Entries are separated by ` \| `, and each starts with a `YYYY-MM-DD` date. An entry never contains the `\|` character itself (write `/` instead). | Claude (append only) |
| `yourNotes` | Your own notes. **Claude never writes this.** | You |
| `managerName`, `managerTitle`, `howIdentified`, `confidence`, `profileUrl`, `emailOrFormat`, `connectionNote`, `longMessage` | Outreach research and drafts (stage 04). Drafts only. You send. | Claude |

**Status values:** `To apply`, `Applied`, `Followed up`, `Interview`, `Offer`, `Review fit` (set only by you, for a listing you want to think over; fit review never creates listings at this status), `On hold`, `Rejected` (the employer said no), `Closed` (you passed), `expired` (the posting came down), `filled` (the employer says it is filled).

Listings at **Applied, Followed up, Interview or Offer** are never changed by a sweep, ever.

## answers: your answer bank

One row per answer you give on forms. See `answer-bank.md`.

| Column | What it holds | Who writes |
|---|---|---|
| `id` | Short name, for example `pay-text` or `ref-1`. | Claude |
| `topic` | `Contact`, `Work history`, `Education`, `Pay`, `Voluntary` (diversity questions), `References`, `Links`, `Work authorization`, `Account`, or `Other`. | Both |
| `question` | The question as forms usually ask it. For an `Account` row, the website. | Both |
| `answer` | Your answer. For an `Account` row, the username only. **Never a password, ID number or bank detail.** | Both |
| `useWhen` | When to use it, or when to ask you first. | Both |
| `updated` | Date last changed. | Both |

## settings: one row

The `id` is `main`. Lists are separated by `; ` (semicolon and space).

| Column | What it holds | Example |
|---|---|---|
| `id` | Always `main`. | `main` |
| `tierA`, `tierB`, `tierC` | What each employer tier means for you. | `Employer based in my home metro` |
| `industryOrder` | Industries you want, most wanted first. The tracker groups listings in this order. | `Logistics software; Manufacturing; Public utilities` |
| `excludedIndustries` | Industries hidden from the main views and skipped in sweeps. | `Staffing; Retail` |
| `roleFamilies` | Kinds of role. A `*` after a name marks a target family. | `Quality inspector*; Operations analyst*; Shift supervisor` |
| `tracks` | Separate searches, if you run more than one. Most people have one. | `Main` |
| `priorities` | Priority groups, in work order. | `High; Medium; Low; On hold` |

How sessions read, write and check the tracker is in `tracker-access.md`.
