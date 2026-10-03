# Rules

Stable rules for every stage. They work together with the user's own rules, `my-rules.md` (saved by the intake interview), which holds everything personal: target roles, place, pay, industries, experience stretch, hard noes, employers on hold, autonomy and writing style. Where this file says "the user's rules", it means `my-rules.md`.

If the tracker and a file disagree on status, the tracker wins. If anything disagrees with this file or `my-rules.md`, those win. If this file and `my-rules.md` disagree, `my-rules.md` wins for the user's own preferences (roles, place, pay, industries) and this file wins for safety. Safety rules never bend. For tools and connections (tracker, Python, browser, email connector), `my-setup.md` wins: it records what setup actually found.

When two rules conflict and nothing here settles it, the newest dated rule in `my-rules.md` wins, and you tell the user about the conflict. Safety rules (section 9) always win.

## 1. What counts as a target role

- A role is a target only if it matches the **target roles** and **seniority** in the user's rules.
- Roles the user's rules list as **out** are out, even when the title sounds close.
- **Industries and products:** an employer or posting in an industry the user's rules list as **out** is a no. An industry listed as **in** is a yes on this check. An industry on neither list: decide from the user's stated reasons, and if it is a real judgment call, list it in the report for the user rather than adding it.
- **Excluded industries in the tracker.** The `settings` record lists `excludedIndustries`. Employers in those industries are skipped in sweeps unless their `keepAnyway` column says yes. Only the user reopens an industry.

## 2. Pay

- The user's rules set a **pay floor** and say what counts toward it (for example base salary only, or total pay including commission or bonus).
- The top of the posted range, or the posted total pay, must reach the floor. A whole range under the floor is a no.
- **Hourly pay:** for a full-time role, multiply the hourly rate by 2,080 hours to compare with a yearly floor, and say so in `why`. For part-time, compare only if the user's rules allow part-time.
- No posted pay: decide whether the floor is plausible from the role type, level and anything else posted. Never invent a figure. Write "not posted" in `pay` and give your reasoning in `why`.
- How the user states pay on forms comes from the answer bank (`answers`, topic Pay). Never make up a number.

## 3. Experience

- A "preferred" line never fails a posting.
- The user's rules say how far they **stretch** on required years. Inside that stretch, required years are not a reason to skip: the listing goes to To apply with the reach named in `why`.
- A license required **before hire** that the user does not hold is a no, unless the user's rules say otherwise. A license obtained after hire is fine.
- A required degree in a specific field the user does not have is a no, unless the user's rules say otherwise.
- Any other hard noes in the user's rules (for example part-time, travel over a set share, shift work) are a no.

## 4. Place

- The user's rules list where they will work: home metro, allowed territories, remote rules, any nearby cities allowed only above a pay bar, and whether they will relocate.
- Check the posting's own location detail, not the headline tag. "Remote" that requires residence in a list of states the user is not in is a no.
- When the user's rules allow a place only above a pay bar, no posted pay there is a no.

## 5. Other clear noes

- Closed, expired or filled postings.
- **Employers on hold** (listed in the user's rules and marked `onHold` yes in `companies`): they may be swept and listings may be added, but no applying without the user's go-ahead in the session.

## 6. Evidence

- A listing is real only when confirmed on the **employer's own careers site or applicant tracking system** (the employer's own job board, often run by a service like Workday, Greenhouse, Lever, iCIMS or similar).
- Job aggregators (Indeed, Glassdoor, ZipRecruiter, LinkedIn job listings and the like) are leads, never proof, for adding, expiring or filling anything.
- One exception: an employer with no job board of its own that posts only on its own verified company page on one aggregator. The user lists these in their rules by name.

## 7. Who writes what in the tracker

Column names are in `tracker-columns.md`. They are the same in the artifact and the spreadsheet.

- `yourNotes` belongs to the user. **Never write it.** Read it when it holds something useful.
- `history` is the log. Sessions only **append**, one entry per action, in the form ` | YYYY-MM-DD what happened`. Never rewrite or delete earlier entries.
- `status`:
  - Sweeps may set **expired** or **filled** on listings at To apply, after confirming on the employer's own site, with a history entry.
  - Fit review sets **To apply** on new listings.
  - The apply stage sets **Applied**, and only after the user reviewed the filled form and the application was submitted. It may also set **expired** or **filled** on a listing at To apply when the employer's own site shows the posting is gone, with a history entry.
  - The mailbox check (stage 06) may set **Followed up**, **Interview**, **Rejected**, **Offer**, or **expired** (the employer cancelled the role), only after the user says yes to each change in that session.
  - The user may ask for any status change directly.
  - Nothing else changes a status.
- Never change the status of a listing at Applied, Followed up, Interview or Offer except as above. On those listings sessions may only append history lines, and stage 04 may fill the outreach columns.
- **Re-read before writing, back up before bulk writes, and check by script** before and after any session that writes. How, for both kinds of tracker, is in `tracker-access.md`. A stage is not done until the check passes.
- **When a check fails because of something the user did,** tell the user. Never undo their change, and never write `yourNotes` to make a check pass.

## 8. Autonomy

The user's rules set how much each stage may do alone. These limits apply no matter what the user's rules say:

| Stage | Most it may ever do alone |
|---|---|
| Intake | Asks questions. Saves `my-rules.md` only after the user approves the full text. |
| Sweep | Reads employer sites and writes the tracker within these rules. Started by the user. |
| Fit review | Adds listings that pass every check. Brings the user any call that depends on taste. |
| Apply | Fills forms. **Submits nothing without the user's review**, unless the user turns on auto-submit for that one session in writing. |
| Outreach | Drafts only. Runs only when the user starts it by name. The user sends everything. |
| Interview prep | Runs when the user asks, for a named interview. |
| Resume | Writes only from facts the user approved. The user approves the facts file, each section, and the final PDF. Never rewrites a resume the user opted to keep. |
| Company research | Adds employers to the target list only after the user approves each one. |
| Mailbox check | Reads email. Proposes status changes. Writes only what the user approves. Never replies, sends, deletes, labels or moves email. |
| Changes to this system's files, `my-rules.md` or the tracker page | The user approves every change. |

Any grant of extra autonomy lasts for one session only. Past grants never carry over.

## 9. Safety

- Never create an account, set or enter a password, or read a password field.
- Never enter a Social Security number or other government ID, driver's license, bank account or card number.
- Never solve or try to get past a CAPTCHA, bot check or one-time code.
- Never send an email, message or form on the user's behalf. The only exception is submitting an application after the user's review, or under auto-submit the user turned on for this session.
- Assessments, aptitude tests, criminal-history questions, and whether they would sign a future non-compete or non-solicitation agreement are the user's to answer. Whether they are bound by one now comes from the answer bank.
- Never contact the user's current employer. Never use the user's work email, work phone or work accounts.
- **Site terms.** LinkedIn and some job boards forbid automated access in their terms of use. This system never automates LinkedIn in any way: no scraping, no automated profile visits, no messages, and no opening linkedin.com pages. The user is responsible for following each site's terms.

## 10. Writing

- Follow the writing style in the user's rules.
- Plain language. No em dashes or en dashes.
- Anything sent under the user's name must read like a person wrote it.
- The resume is submitted as-is and never rewritten unless the user asks in that session. When the user asks, stage 07 builds it only from facts they approved.

## 11. Files

- Each stage saves its reports in its own `output/` folder, named as its Outputs table says. Git never shares those folders.
- Tracker backups and snapshots go to `tracker/backups/`.
- When a file changes, give the complete new version, never a list of edits.
