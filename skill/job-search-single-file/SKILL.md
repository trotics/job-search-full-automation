---
name: job-search
description: Runs a job search with the user. Use for the setup interview, resume building, finding and researching employers, sweeps of employer career sites, fit calls on postings, applications, hiring-manager outreach drafts, interview prep, and mailbox checks that read or write the user's job search tracker.
---

<!-- Built by tools/build_single_file.py from skill/job-search/. Do not edit by hand. -->

# Job search: the map

This Skill helps one person run their job search. It builds a resume from the user's own facts, finds and researches employers, finds openings on employers' own career sites, decides which ones fit the user's rules, keeps a tracker up to date, fills in applications with the user, drafts outreach for the user to send, and prepares the user for interviews.

The user stays in charge. Claude never submits an application without the user's review, never sends a message, and never handles passwords, codes, ID numbers or CAPTCHAs.

This one file holds everything: the map, the rules, the stage contracts and the references. Where a section names a file such as `stages/01-sweep.md` or `rules.md`, read the section of that name below.

## Where things live

Everything personal lives in the user's **job search folder**, not in this Skill:

| What | Where |
|---|---|
| The user's own rules (target roles, place, pay, industries and the rest) | `my-files/my-rules.md` |
| Resume to upload | `my-files/resume.pdf` |
| Resume as text, for filling forms | `my-files/resume.md` |
| Facts the resume is built from (stage 07) | `my-files/resume-facts.md` |
| Tailored resumes for single listings | `my-files/resumes/` |
| Session reports and interview prep | `reports/` |
| Backups of the tracker | `backups/` |

**No job search folder?** On Claude on the web or a tablet there may be no folder Claude can read and write. Then: ask the user to attach `my-rules.md` (and `resume-facts.md` for stage 07) at the start of each chat, or keep them in the files of a Claude Project so every chat sees them. Give every file you create or change as a download, and tell the user to save it and attach it next time. Stages that need a browser Claude can control (sweeps of most career sites, and applying) need the desktop app.

**The tracker** is the single source of truth for employers, sweeps, listings, status and the answer bank. It is one of two kinds. `my-rules.md` says which one, and where:

- **Artifact tracker (main):** a Claude artifact page the user published from `tracker-page.html`, with its own database. Read and write it with the `ArtifactData` tool, using the artifact link in `my-rules.md`. Collections: `companies`, `coverage`, `listings`, `answers`, `settings`.
- **Spreadsheet tracker (fallback):** `my-files/job-search-tracker.xlsx`, with tabs of the same names and the same columns. Read and write it with Python and openpyxl, or with `tools/sheet.py` when the repo is in the folder. The user must close the file in Excel before a session writes to it.

Every column is described in `references/tracker-columns.md`. The two trackers use the same names, so every rule in this Skill applies to both.

If the tracker and a file disagree on status, the tracker wins. If anything disagrees with `rules.md` or `my-rules.md`, those win. If `rules.md` and `my-rules.md` disagree, `my-rules.md` wins for the user's own preferences (roles, place, pay, industries) and `rules.md` wins for safety. Safety rules never bend.

## Every session

1. If `my-files/my-rules.md` does not exist, the user is new. Run `stages/00-intake.md` and nothing else.
2. If `my-rules.md` exists but has no working tracker link or file, set up the tracker with the user first (intake question 1 says how) before any stage that writes.
3. Read `rules.md` (this Skill) and `my-files/my-rules.md` in full. They apply to every stage.
4. Load only the stage file for the task:

| Task | Load |
|---|---|
| First-time setup, or the user wants to change their rules | `stages/00-intake.md` |
| Check employers for new listings, confirm listings are still open | `stages/01-sweep.md` |
| Decide whether a posting fits | `stages/02-fit-review.md` (the sweep calls it) |
| Fill in applications for listings at To apply, with the user | `stages/03-apply.md` |
| Hiring-manager outreach drafts (only when the user starts it by name) | `stages/04-outreach.md` |
| Prepare for an interview | `stages/05-interview-prep.md` |
| Check the user's email for employer replies and update statuses | `stages/06-mailbox-check.md` |
| Build or improve a resume, or make a tailored version for one listing | `stages/07-resume.md` |
| Find employers, research a company, map an industry, research a role | `stages/08-company-research.md` |

5. Read `references/recurring-mistakes.md` before any tracker write.
6. Do only the task asked. Never start another stage on your own.
7. A stage is done only when every item on its "Done when" list is checked. Say plainly which items were not.
8. Every stage is started by the user in a live session. Nothing in this Skill runs on a schedule or unattended.

## Scripts

Stages run small Python scripts in `tools/` (in the user's job search folder) to check their work and build files. They need Python 3 with openpyxl and reportlab (`python -m pip install -r requirements.txt`). If Python or a package is missing, say so plainly and offer to install it. Never skip a check silently: a stage whose check could not run is not done.

## References

- `references/tracker-columns.md`: every tab and column, in plain words.
- `references/answer-bank.md`: how to use the answer bank.
- `references/application-techniques.md`: how upload controls and form auto-fill behave.
- `references/recurring-mistakes.md`: mistakes that have happened before.
- `references/sample-resume.md`: a made-up resume showing the format `my-files/resume.md` should follow.
- `references/resume-guide.md`: resume rules, examples by field, and the default (stage 07).
- `references/resume-facts-template.md`: the shape of the resume facts file (stage 07).
- `references/prompts.md`: what the user can say to start each kind of session.

---

<!-- rules.md -->

## Rules

Stable rules for every stage. They work together with the user's own `my-files/my-rules.md`, which holds everything personal: target roles, place, pay, industries, experience stretch, hard noes, employers on hold, autonomy and writing style. Where this file says "the user's rules", it means `my-rules.md`.

When two rules conflict and nothing here settles it, the newest dated rule in `my-rules.md` wins, and you tell the user about the conflict. Safety rules (section 9) always win.

### 1. What counts as a target role

- A role is a target only if it matches the **target roles** and **seniority** in the user's rules.
- Roles the user's rules list as **out** are out, even when the title sounds close.
- **Industries and products:** an employer or posting in an industry the user's rules list as **out** is a no. An industry listed as **in** is a yes on this check. An industry on neither list: decide from the user's stated reasons, and if it is a real judgment call, list it in the report for the user rather than adding it.
- **Excluded industries in the tracker.** The `settings` record lists `excludedIndustries`. Employers in those industries are skipped in sweeps unless their `keepAnyway` column says yes. Only the user reopens an industry.

### 2. Pay

- The user's rules set a **pay floor** and say what counts toward it (for example base salary only, or total pay including commission or bonus).
- The top of the posted range, or the posted total pay, must reach the floor. A whole range under the floor is a no.
- No posted pay: decide whether the floor is plausible from the role type, level and anything else posted. Never invent a figure. Write "not posted" in `pay` and give your reasoning in `why`.
- How the user states pay on forms comes from the answer bank (`answers`, topic Pay). Never make up a number.

### 3. Experience

- A "preferred" line never fails a posting.
- The user's rules say how far they **stretch** on required years. Inside that stretch, required years are not a reason to skip: the listing goes to To apply with the reach named in `why`.
- A license required **before hire** that the user does not hold is a no, unless the user's rules say otherwise. A license obtained after hire is fine.
- A required degree in a specific field the user does not have is a no, unless the user's rules say otherwise.
- Any other hard noes in the user's rules (for example part-time, travel over a set share, shift work) are a no.

### 4. Place

- The user's rules list where they will work: home metro, allowed territories, remote rules, any nearby cities allowed only above a pay bar, and whether they will relocate.
- Check the posting's own location detail, not the headline tag. "Remote" that requires residence in a list of states the user is not in is a no.
- When the user's rules allow a place only above a pay bar, no posted pay there is a no.

### 5. Other clear noes

- Closed, expired or filled postings.
- **Employers on hold** (listed in the user's rules and marked `onHold` yes in `companies`): they may be swept and listings may be added, but no applying without the user's go-ahead in the session.

### 6. Evidence

- A listing is real only when confirmed on the **employer's own careers site or applicant tracking system** (the employer's own job board, often run by a service like Workday, Greenhouse, Lever, iCIMS or similar).
- Job aggregators (Indeed, Glassdoor, ZipRecruiter, LinkedIn job listings and the like) are leads, never proof, for adding, expiring or filling anything.
- One exception: an employer with no job board of its own that posts only on its own verified company page on one aggregator. The user lists these in their rules by name.

### 7. Who writes what in the tracker

Column names are in `references/tracker-columns.md`. They are the same in the artifact and the spreadsheet.

- `yourNotes` belongs to the user. **Never write it.** Read it when it holds something useful.
- `history` is the log. Sessions only **append**, one entry per action, in the form ` | YYYY-MM-DD what happened`. Never rewrite or delete earlier entries.
- `status`:
  - Sweeps may set **expired** or **filled** on listings at To apply, after confirming on the employer's own site, with a history entry.
  - Fit review sets **To apply** on new listings.
  - The apply stage sets **Applied**, and only after the user reviewed the filled form and the application was submitted. It may also set **expired** or **filled** on a listing at To apply when the employer's own site shows the posting is gone, with a history entry.
  - The mailbox check (stage 06) may set **Followed up**, **Interview**, **Rejected** or **Offer**, only after the user says yes to each change in that session.
  - The user may ask for any status change directly.
  - Nothing else changes a status.
- Never change a listing at Applied, Followed up, Interview or Offer except as above.
- **Re-read before writing.** Read the row fresh just before you change it, and write only the fields you changed. If the row changed since you last read it, stop and read it again.
- **Back up before bulk writes.** Before writing more than five rows in one session, save a copy of the whole tracker to `backups/`:
  - Artifact: list every collection with `ArtifactData` and save them together as `backups/tracker-backup-<YYYY-MM-DD>-<HHMM>.json`.
  - Spreadsheet: copy the file to `backups/tracker-backup-<YYYY-MM-DD>-<HHMM>.xlsx`.
- **Check by script.** Before and after any session that writes, save a snapshot and run `tools/check_tracker.py` (see `references/tracker-columns.md`). A stage is not done until the check passes.

### 8. Autonomy

The user's rules set how much each stage may do alone. These limits apply no matter what the user's rules say:

| Stage | Most it may ever do alone |
|---|---|
| Intake | Asks questions. Saves `my-rules.md` only after the user approves the full text. |
| Sweep | Reads employer sites and writes the tracker within these rules. Started by the user. |
| Fit review | Adds listings that pass every check. Brings the user any call that depends on taste. |
| Apply | Fills forms. **Submits nothing without the user's review**, unless the user turns on auto-submit for that one session in writing (see stage 03). |
| Outreach | Drafts only. Runs only when the user starts it by name. The user sends everything. |
| Interview prep | Runs when the user asks, for a named interview. |
| Resume | Writes only from facts the user approved. The user approves the facts file, each section, and the final PDF. Never rewrites a resume the user opted to keep. |
| Company research | Adds employers to the target list only after the user approves each one. |
| Mailbox check | Reads email. Proposes status changes. Writes only what the user approves. Never replies, sends, deletes, labels or moves email. |
| Changes to this Skill, `my-rules.md` or the tracker page | The user approves every change. |

Any grant of extra autonomy lasts for one session only. Past grants never carry over.

### 9. Safety

- Never create an account, set or enter a password, or read a password field.
- Never enter a Social Security number or other government ID, driver's license, bank account or card number.
- Never solve or try to get past a CAPTCHA, bot check or one-time code.
- Never send an email, message or form on the user's behalf. The only exception is submitting an application after the user's review, or under auto-submit the user turned on for this session.
- Assessments, aptitude tests, criminal-history questions, non-compete and non-solicitation questions are the user's to answer.
- Never contact the user's current employer. Never use the user's work email, work phone or work accounts.
- **Site terms.** LinkedIn and some job boards forbid automated access in their terms of use. This system never automates LinkedIn in any way: no scraping, no automated profile visits, no messages, and no opening linkedin.com pages. The user is responsible for following each site's terms.

### 10. Writing

- Follow the writing style in the user's rules.
- Plain language. No em dashes or en dashes. No stock phrases that sound machine-written.
- Anything sent under the user's name must read like a person wrote it.
- The resume is submitted as-is and never rewritten unless the user asks in that session. When the user asks, stage 07 builds it only from facts they approved.

### 11. Files

- Session reports go to `reports/` in the job search folder, named `<stage>-<YYYY-MM-DD>.md`.
- Backups go to `backups/`.
- When a file changes, give the complete new version, never a list of edits.

---

<!-- stages/00-intake.md -->

## Stage 00: Intake interview

Set up a new user, or change an existing user's rules. Ends with `my-files/my-rules.md` saved, the tracker's `settings` record filled, and, if the user wants them, a starter answer bank, a resume (stage 07) and a first list of employers (stage 08).

### How to run it

- Ask **one question at a time**. Wait for the answer before asking the next one.
- Keep each question short. Give one or two examples so the user knows what kind of answer fits. Examples should not lead the user toward any industry.
- If an answer is vague, ask one follow-up. If it is still vague, write down what they said and move on.
- Never guess an answer. If the user skips a question, write "None" or "Not decided" in that line.
- If `my-files/my-rules.md` already exists, read it first. Only ask about the parts the user wants to change, then add a dated line to section 10.

### Inputs

- `references/my-rules-template.md`: the shape of the finished file.
- `rules.md`: the general rules, so you can explain them when asked.
- `stages/07-resume.md` and `stages/08-company-research.md`, which the intake can hand off to at the end.

### Questions

Ask them in this order. The number in brackets is the section of `my-rules.md` it fills.

**Tracker**
1. "Will you keep your tracker as a Claude artifact (a web page in your Claude account) or as a spreadsheet file?" [Tracker]
   - **Artifact, already published:** "Paste the link." Save it.
   - **Artifact, not published yet:** offer to publish it now, together: publish `tracker/tracker-page.html` as a new artifact with the `db` capability (README, "Set up your tracker"), show the user the empty tracker, and save the link. If publishing is not possible here (for example on a device without that feature), offer the spreadsheet for now.
   - **Spreadsheet:** copy `tracker/spreadsheet/job-search-tracker.xlsx` to `my-files/` and save that path.
   - The tracker must exist before step 4 below writes `settings` and `answers` to it. If it still does not exist by then, keep those values in the chat, tell the user, and write them the first time the tracker exists.

**Target roles**
2. "What kind of job are you looking for? Name a few titles if you can." [1]
3. "What level: entry, mid, senior, or a range?" [1]
4. "Are there roles with similar titles that you do not want? For example, a title that sounds right but is really support or admin work." [1]
5. "In a sentence or two, what does a good fit look like to you?" [1]

**Place**
6. "Where do you live? A city or metro area is enough." [2]
7. "Which of these work for you: jobs in your home metro, a territory based out of your home metro, a territory covering several states, fully remote?" [2]
8. "For remote jobs, are there limits? For example, some remote jobs only hire in certain states." [2]
9. "Are any nearby cities OK only if the pay is high enough? If so, which cities and what pay?" [2]
10. "Would you move for the right job? If yes, where?" [2]

**Pay**
11. "What is the lowest pay you will accept? Say whether that is per year or per hour." [3]
12. "Does that floor count base salary only, or base plus commission or bonus?" [3]
13. "When a form lets you type your pay expectation, how do you want it worded?" [3]
14. "When a form needs a single number, what number?" [3]

**Industries and products**
15. "Which industries or kinds of products are you most interested in?" [4]
16. "Which industries or products are out for you, and why?" [4]
17. "Of the ones that are out, which should be hidden in your tracker entirely?" These become `excludedIndustries`. [4]

**Experience**
18. "How many years of experience do you have in the kind of work you are targeting? What counts?" [5]
19. "If a posting asks for more years than you have, how far would you still apply? For example, up to two more years." [5]
20. "What licenses or certifications do you hold?" [5]
21. "What degrees do you hold, and in what field?" [5]

**Hard noes**
22. "Anything that is an automatic no? For example: part-time, contract, commission only, night shifts, heavy travel, a license you would need before starting." [6]

**Employers**
23. "Are there employers you want tracked but not applied to yet?" These go on hold. [7]
24. "Who must never be contacted? Your current employer goes here if you have one." [7]
25. "Any employer that only posts jobs on one job site (like Indeed) and has no job board of its own?" [7]

**Autonomy**
26. "When I sweep employer sites, should I add fitting listings on my own, or ask you before writing anything?" [8]
27. "When a posting is a close call, should I decide by your rules, or bring every close call to you?" [8]
28. Tell the user, do not ask: "For applications, I fill in the form and you review it before anything is submitted. You can turn on auto-submit for one session by writing it out, but it is off by default." [8]
29. "Do you want hiring-manager outreach drafts? I only draft. You send everything yourself." [8]
30. "Do you have an email connector set up in Claude (for example Gmail or Outlook)? If yes, I can check for employer replies when you ask and suggest status updates." [8]

**Writing style**
31. "How should anything written for you sound? For example: short and direct, warm, formal. Any words or habits to avoid?" [9]

### After the last question

1. Write the full `my-rules.md` from the template and the answers. Use the user's own words where you can.
2. **Show the whole file** to the user and ask: "Is this right? Tell me anything to change, or say approve." Make changes and show the whole file again until they approve.
3. Only after approval, save it to `my-files/my-rules.md`.
4. Write the tracker's `settings` record (see `references/tracker-columns.md`). Show the values first and save after the user says yes:
   - `tierA`, `tierB`, `tierC`: what each employer tier means for this user. Default: A "Employer based in my home metro", B "Employer elsewhere with jobs open to my area", C "Other allowed place".
   - `industryOrder`: the "in" industries, most wanted first.
   - `excludedIndustries`: from question 17.
   - `roleFamilies`: the kinds of role from questions 2 to 4, with a `*` after the ones that are targets.
   - `tracks`: leave as `Main` unless the user is searching for two quite different kinds of role.
   - `priorities`: leave as `High; Medium; Low; On hold` unless the user asks.
5. Ask: "Do you want to start your answer bank now? It holds the answers you give on most forms: contact details, work history, years of experience in the work you are targeting, work authorization, references, pay wording and the optional diversity questions. You can also fill it later." If yes, ask one item at a time and save each to `answers` after the user confirms it. Never ask for or store passwords, ID numbers or bank details.
6. **Resume.** Ask: "Do you already have a resume you are happy with?" Offer three answers, and respect the choice:
   - **"Yes, use mine as it is"** (opt out): ask them to put it in `my-files/resume.pdf`. Offer to make the text copy `my-files/resume.md` from it, and show the copy before saving. Do not rewrite or critique it. Stage 07 never runs unless they ask later.
   - **"Yes, but I want it improved"**: run `stages/07-resume.md`, starting from their file. Their resume is a source of facts, and nothing changes without their yes.
   - **"No" or "I need a new one"**: run `stages/07-resume.md` from the start.
   Tell them they can skip this for now and say "build my resume" any time.
7. **Employers.** Ask: "Do you already have a list of employers you want to work for?" If yes, add them with sweep step 0. If no, or they want more, offer stage 08 part A ("find employers for my target list"). Do not start it unless they say yes.
8. Point them to `references/prompts.md` for what to say in later sessions.

### Outputs

- `my-files/my-rules.md`, approved by the user.
- The tracker's `settings` record.
- Answer bank entries, if the user wanted them.
- A resume from stage 07, or the user's own resume in `my-files/`, or a note that they skipped it for now.

### Done when

- [ ] Every question was asked, one at a time, or the user skipped it.
- [ ] The user saw the complete `my-rules.md` and said approve before it was saved.
- [ ] `settings` was saved after the user said yes.
- [ ] No password, ID number or bank detail was asked for or stored.
- [ ] The user chose one of the three resume answers, or chose to skip for now, and that choice was respected.
- [ ] The user knows the next step (usually: add or find employers, then run a sweep) and where the prompts list is.

---

<!-- stages/01-sweep.md -->

## Stage 01: Sweep

Check employers for new listings, and confirm that listings already in the tracker are still open. The user starts every sweep. Nothing here runs on a schedule.

> **Site terms.** LinkedIn and some job boards forbid automated access in their terms. A sweep reads employers' own career sites only. It never opens LinkedIn and never uses an aggregator as a source of truth. The user is responsible for following each site's terms.

### Tracker access

- **Artifact:** read `companies`, `coverage`, `listings` and `settings` with `ArtifactData` (`list`). Write one row at a time with `update` (or `set` for a new row), after reading it fresh.
- **Spreadsheet:** read and write the tabs of the same names in `my-files/job-search-tracker.xlsx` with `tools/sheet.py` or openpyxl. Ask the user to close the file in Excel first.

### Inputs

- `rules.md` and `my-files/my-rules.md`.
- Tracker: `companies`, `coverage`, `listings`, `settings`.
- The session's scope, from the user: which employers, how many, or which listings to recheck. If the user gives no scope, offer: "the 10 employers swept longest ago, plus a recheck of every listing at To apply".

### Steps

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

### Outputs

- New listings at To apply (from stage 02).
- Coverage rows updated for every employer touched.
- Listings set to expired or filled, each with a history entry.
- A report saved to `reports/sweep-<YYYY-MM-DD>.md`: employers checked, new listings, listings expired or filled, manual employers, anything unconfirmed, and calls for the user.

### Done when

- [ ] Every employer in scope has a dated coverage entry, or is listed in the report as not reached.
- [ ] Every new listing passed stage 02 and has all its required columns.
- [ ] No listing at Applied, Followed up, Interview or Offer was changed (`check_tracker.py`).
- [ ] No status change rests on aggregator evidence.
- [ ] `yourNotes` untouched on every row (`check_tracker.py`).
- [ ] Backup taken if more than five rows were written.
- [ ] Report saved.

---

<!-- stages/02-fit-review.md -->

## Stage 02: Fit review

Decide whether one posting goes in the tracker. The sweep calls this for every new posting. The user can also hand you a posting link and ask for a fit call.

### Tracker access

- **Artifact:** read `listings`, `companies` and `settings` with `ArtifactData`. Add a new listing with `set` (a new id), and add skipped lines to the employer's `coverage` row with `update`.
- **Spreadsheet:** the same tabs and columns in `my-files/job-search-tracker.xlsx`. Add a new row at the bottom of `listings`.

### Inputs

- `rules.md` and `my-files/my-rules.md`.
- The posting, read on the employer's own site: title, location detail, pay, requirements, work type (full-time, part-time, contract).
- The tracker: existing listings for that employer, to avoid duplicates.

### Steps

Check in this order. The first failure decides.

1. **Duplicate?** Same req id, or same title and location at the same employer, already in `listings`: stop, nothing to add.
2. **Live on the employer's own site?** If not: no.
3. **Target role?** Not one of the user's target roles, or one of their "out" roles: no (rules 1).
4. **Industry and product?** An "out" industry, or an excluded industry without `keepAnyway`: no (rules 1).
5. **Place?** Fails the user's place rules: no (rules 4).
6. **Pay?** Under the floor: no. No posted pay: decide plausibility and write the reasoning (rules 2).
7. **Hard requirements?** License before hire, a specific degree the user lacks, any hard no in the user's rules: no. Required years inside the user's stretch never fail it on their own (rules 3).
8. **On-hold employer?** Add the listing, set `priority` to `On hold`, and say so in `why`.

### Outputs

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

### Done when

- [ ] Every posting read ends as a new listing, a skipped line, or a report item for the user.
- [ ] No listings created at Review fit. Close calls go in the report instead.
- [ ] Every new listing has every column above, including `postingText`, and a unique `id`.

---

<!-- stages/03-apply.md -->

## Stage 03: Apply

Fill in applications for listings at To apply, live with the user. **The user reviews every application before it is submitted.**

### Auto-submit (off by default)

Auto-submit is off. The user can turn it on for **this session only** by writing a sentence like: "I turn on auto-submit for this session." It turns off when the session ends and never carries over. Even with auto-submit on:

- Every wall (account, password, code, CAPTCHA, ID number) is still the user's to do.
- No cover letter goes out without the user's sign-off on that letter.
- Legal text is still quoted to the user, and **Claude never ticks a legal agreement box itself**. A form with a legal agreement is never auto-submitted: the user ticks the box and submits.
- Anything not covered by the answer bank still goes to the user.

### Browser

Apply in **Claude in Chrome** when it is connected. It can upload files. The app's built-in browser pane cannot upload files, so if you start there and reach an upload, switch to Claude in Chrome (upload step 4e).

### Tracker access

- **Artifact:** read `listings` and `answers` with `ArtifactData`. Write the listing's `status`, `postingText`, `appliedDate` and `history` with `update`, after reading the row fresh. Add new accounts to `answers` with `set`.
- **Spreadsheet:** the same tabs and columns in `my-files/job-search-tracker.xlsx`.

### Inputs

- `rules.md` and `my-files/my-rules.md`.
- Listings at To apply, worked in priority order (High, then Medium, then Low), oldest `posted` first within each. Skip `On hold` listings unless the user says go.
- The answer bank: `answers` in the tracker (see `references/answer-bank.md`).
- `my-files/resume.md` for text fields, and `my-files/resume.pdf` to upload. Ask once per session for access to `my-files/` if you do not have it, then upload the resume yourself.
- `references/application-techniques.md`: how upload controls and auto-fill behave.

### Steps

1. **Still live?** Open the posting on the employer's own site. If it is gone, set `expired` or `filled` with a history entry and move on.
2. **Save the posting.** Copy the full posting text into `postingText` now, even if fit review saved it already, and append a history line: `YYYY-MM-DD posting text saved before applying.` The later copy wins, because postings change. Interview prep depends on this.
3. **Re-check the fit.** Read the posting in full before the user does anything on the site. Re-check it against the rules. If it now fails, tell the user and let them decide.
4. **Upload the resume.** Try these in order. Move to the next only if the one before it failed.
   - **Which file:** `my-files/resumes/resume-<listing id>.pdf` if the listing's history shows a tailored resume was approved (stage 07 part D), otherwise `my-files/resume.pdf`.
   - **a. File upload tool.** Use Claude in Chrome's file upload tool on the form's file input, with the full path to that file. Do not click the input first: clicking opens the computer's own file picker.
   - **b. Hidden input.** If the visible control is a button or a drag-and-drop zone, find the hidden `input[type=file]` behind it (with `read_page`, `find`, or a read-only check of the page) and use the file upload tool on that input directly.
   - **c. The computer's file picker.** If clicking a button opened the computer's own file picker, do not get stuck in it. Close it (Escape) and go back to b. Only if b finds no input: if the desktop control tool can work that dialog on this computer, use it to type the full path to `resume.pdf` and confirm. If the tool's access level blocks it, stop this option.
   - **d. Paste or type.** If the form offers "paste your resume" or "enter manually", use the text of `my-files/resume.md`, and flag this in the review summary.
   - **e. Switch browsers.** If the active browser cannot upload at all (for example the built-in browser pane), move this application to Claude in Chrome and start again at a.
   - **Never take these routes:** "Apply with LinkedIn" or any LinkedIn import; signing in to Google Drive, Dropbox or any other account to import a file; any step that needs a password, a code or a CAPTCHA. Those are walls, and walls stay the user's.
   - **Check after every upload.** The page must show the file name (or a preview of the resume it read), and it must be the file chosen above (`resume.pdf`, or the approved tailored file), not another file. If the site filled in form fields from the resume, check every one against the answer bank and fix any that are wrong. A wrong auto-fill is a common way applications go bad.
   - **Hand it to the user only when a to e all failed or hit a wall.** Say which options you tried and why each one failed, then pick up the form after the user attaches the file.
5. **Fill the form** from the answer bank and the resume. Invent nothing. For a question the answer bank does not cover, answer only if the answer is plainly safe and true from the resume. Otherwise ask the user.
   - **Optional free-text boxes** (for example "Why are you interested?"): leave them blank unless the user's rules say to fill them. If you fill one, draft it in the user's writing style and flag it in the review summary.
   - **Questions answered from the resume** rather than the answer bank (for example "years of B2B sales"): flag each one in the review summary, and offer to add it to the answer bank.
6. **Pay questions:** use the answer bank's Pay entries: the wording where text is allowed, the single number where one is required.
7. **Diversity and voluntary questions** (gender, race, veteran, disability): answer from the answer bank. If it has no entry, choose "I don't wish to answer" or the closest option, and tell the user.
8. **Links** (LinkedIn profile, portfolio): enter only when the field is required, from the answer bank. Never open LinkedIn.
9. **References:** from the answer bank, in the order it lists them. Never list the user's current employer, or anyone the user's rules say never to contact.
10. **Cover letter:** if the form requires one, draft it from the resume and the posting, in the user's writing style. Show it to the user. It is attached only after the user signs off on that letter.
11. **Legal text** (arbitration, waivers, non-compete, non-solicitation, broad permission to contact past employers): quote it to the user. **Never tick a legal agreement box yourself**, in any mode. The user reads it and ticks it, or decides not to apply.
12. **Walls** (create account, password, verification code, CAPTCHA, Social Security number or other ID): fill everything up to the wall, then hand the browser to the user. Continue after they are through. Never do the wall step yourself, and never read what they typed.
13. **Review before submit.** Show the user a summary of every answer on the form, including the upload (file name and method) and any auto-filled fields you corrected, and stop. Submit only when the user says "submit" for this application, or clicks submit themselves. Under auto-submit, still post the summary in the chat as you submit.
14. **After submitting:** capture the confirmation (confirmation page text or number). Set `status` to `Applied` and `appliedDate` to today. Append a history entry: date, req id, title, company, location, pay if posted, the application system used, the username if an account was used (never a password), the confirmation, the upload method (for example "upload: hidden file input"), and anything unusual.
15. **If blocked and the user has stepped away** (for example they left the session at a wall): leave the status at To apply and append a history entry naming the exact step that blocked. Never work around the block.
16. Add any new account to `answers` (topic `Account`, question = the site, answer = the username). Never a password.
17. If an upload control behaved in a way `references/application-techniques.md` does not cover, tell the user and suggest a line to add there. General methods only, never employer names.
18. Take an after snapshot and run `python tools/check_tracker.py check backups/before.json backups/after.json --stage apply` (snapshots: `references/tracker-columns.md`, "Checking by script").

### Dry run

If the user asks for a dry run, do steps 1 to 13 and stop at the review summary. Write nothing to the tracker except `postingText` and its history line (step 2). Close the browser tab without submitting.

### Outputs

- Listings set to Applied, each with `postingText`, `appliedDate` and a history entry that names the upload method.
- Blocked listings left at To apply, each with a history entry.
- A report saved to `reports/apply-<YYYY-MM-DD>.md`: what went through, what is blocked and why, what needs the user.

### Done when

- [ ] Every submitted application was reviewed by the user (or was under auto-submit turned on in writing this session) and has a confirmation and a history entry.
- [ ] Every listing worked has `postingText` saved.
- [ ] Every upload was checked on the page (right file name) and every auto-filled field was checked against the answer bank.
- [ ] No password, code or ID number was typed by the session or written anywhere. No LinkedIn import and no cloud-account import was used.
- [ ] No cover letter went out without the user's sign-off.
- [ ] `yourNotes` untouched (`check_tracker.py`).
- [ ] Report saved.

---

<!-- stages/04-outreach.md -->

## Stage 04: Hiring-manager outreach

**Off unless the user starts it by name in the session** ("run outreach"). Never as a side task of another stage. **Drafts only. The user sends every message.**

> **Site terms.** LinkedIn and some job boards forbid automated access in their terms. This stage never automates LinkedIn in any way: no scraping, no automated profile visits, no messages, no opening linkedin.com pages. It uses web search and the employer's own pages only. The user is responsible for following each site's terms.

### Purpose

A short, specific note to the person who runs the team can get an application read by someone who decides. This stage finds that person from public sources and drafts the note. The user decides whether and how to send it.

### Tracker access

- **Artifact:** read `listings` with `ArtifactData`. Write only the outreach columns and one history line, with `update`, after reading the row fresh.
- **Spreadsheet:** the same columns in the `listings` tab of `my-files/job-search-tracker.xlsx`.

### Inputs

- `rules.md` and `my-files/my-rules.md`.
- Listings that qualify:
  - Status To apply (any date); Applied within the last 30 days (by `appliedDate`); Rejected within the last 30 days, only if the posting is still open on the employer's own site.
  - The level the user's rules name for outreach. If they name none, use mid level and up.
  - Pay at or above the user's floor. Listings with no posted pay are included, marked "pay unverified", and worked after posted-pay listings.
  - Skip excluded industries unless the employer's `keepAnyway` is yes.
  - *Example for sales roles (change it to fit the user):* mid level means account executive, account manager, territory manager, business development manager, sales consultant, or anything titled senior, strategic or enterprise. Not mid level: sales development, business development representative, associate, trainee, coordinator, support.
- `my-files/resume.md` for facts used in messages.

### Steps

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

### Outputs

- Outreach columns filled on each researched listing.
- A report saved to `reports/outreach-<YYYY-MM-DD>.md`: each contact, confidence, and anything the user should know (wrong place, posting closed).

### Done when

- [ ] The user started this stage by name in this session.
- [ ] No LinkedIn page was opened and nothing was sent.
- [ ] Every connection note is under 300 characters and every message under 90 words, with no em dashes or en dashes.
- [ ] Only the outreach columns and history were written (`check_tracker.py`).

**The user sends every message. The session never sends anything.**

---

<!-- stages/05-interview-prep.md -->

## Stage 05: Interview prep

Prepare the user for a named interview. Run when the user asks.

### Tracker access

- **Artifact:** read the listing with `ArtifactData` (`get`). The only write is an optional history line.
- **Spreadsheet:** read the listing's row in `my-files/job-search-tracker.xlsx`.

### Inputs, and which sources count

Use only these sources:

1. **The saved posting:** the listing's `postingText`. Use it even if the live posting is gone. If `postingText` is empty and the posting is gone, say so and ask the user for a copy (an email, a PDF, a screenshot).
2. **The listing row:** title, pay, `why`, `history` (recruiter names, interview format and time) and `yourNotes` (read only).
3. **The employer's own website:** what they sell, to whom, leadership, press releases.
4. **Recent news** from established news outlets and trade publications, found by web search, each linked.
5. **The user's own record:** `my-files/resume.md` and the answer bank's work history entries. The user's stated history is the only source for their stories.

Do not use as fact: anonymous review sites, aggregator job listings, social media posts, or anything you cannot link. You may mention review-site themes only as "people say", and only if the user asks.

### Steps

1. Confirm with the user which interview, the stage (phone screen, hiring manager, panel, onsite), and who they are meeting, if known.
2. **Company brief:** what they sell, to whom, how the team does its work, recent news, and where this role sits. Every fact gets a link.
3. **Likely questions:** from the posting's requirements and the interview stage, including the hard ones the user's record invites (a short stint, a career change, a gap, missing industry experience).
4. **The user's stories:** map each likely question to a true story from the resume or the answer bank's work history. Invent nothing. Mark any gap so the user can fill it.
5. **Questions for the user to ask** the interviewer.
6. **Logistics** from the listing's history: time, format, recording notices, who to contact.

### Outputs

- A prep file saved to `reports/interview-prep-<company-slug>-<YYYY-MM-DD>.md`, in the user's job search folder. Give the user the path.
- No tracker writes, except one history line saying prep was done, if the user wants it.

### Done when

- [ ] Every fact about the company has a link to one of the allowed sources.
- [ ] Every story is one the user has stated or the resume shows.
- [ ] The file is saved in `reports/` and the user has the path.

---

<!-- stages/06-mailbox-check.md -->

## Stage 06: Mailbox check

Read the user's email for replies from employers and suggest status updates. Run only when the user asks ("check my email", "update the tracker from my email"). Optional: it needs an email connector (for example Gmail or Outlook) connected in Claude. Without one, the user can paste or forward the emails instead.

**Read only.** Never reply, send, forward, delete, archive, label, mark as read, or move any email.

### Tracker access

- **Artifact:** read `listings` and `companies` with `ArtifactData`. After the user says yes, write `status` and `history` with `update`, after reading the row fresh.
- **Spreadsheet:** the same tabs and columns in `my-files/job-search-tracker.xlsx`.

### Inputs

- `rules.md` and `my-files/my-rules.md`.
- The user's email, through their connector. The period to check is from the user, or since the last mailbox check in the history, or the last 14 days.
- Listings at Applied, Followed up and Interview. Listings at To apply only to notice a reply about them (see step 4).

### Steps

1. Take a snapshot of the tracker.
2. Search the mailbox for each employer that has a listing at Applied or later, by company name and by the application system's sender (for example messages from the employer's careers site). Read only messages in the period.
3. Match each message to one listing: same company and, where the message names it, the same title or req id. If a message could match more than one listing, do not guess. Ask the user.
4. Sort each match:
   - **Confirmation** of an application ("we received your application"): no status change. Offer a history line.
   - **Interview request or scheduling:** propose `Interview`, with the date, time, format and names in the history line.
   - **Rejection:** propose `Rejected`.
   - **Offer:** propose `Offer`.
   - **Assessment or next step that is not an interview:** no status change. Offer a history line and tell the user.
   - **A reply about a listing still at To apply** (for example the user applied outside a session): no status change from this stage. Tell the user, and offer a history line. The user can then set the status directly (`python tools/check_tracker.py check backups/before.json backups/after.json --stage user`).
5. **Show the user every proposed change in one list** before writing anything, for example: "Example Health Co, Clinical Account Executive: Applied to Interview. Email from 2026-03-14 asks for a call on 3/18 at 10am with the regional manager." Wait for the user to say yes, no, or change it for each one.
6. Write only what the user approved: `status` (if changed) and one history line per listing, ending "from email dated YYYY-MM-DD, approved by the user".
7. Never change a listing based on an email the user did not approve. Never set Applied from an email. Applied comes only from stage 03 or the user.
8. Take an after snapshot and run `python tools/check_tracker.py check backups/before.json backups/after.json --stage mailbox` (snapshots: `references/tracker-columns.md`, "Checking by script").

### Outputs

- Approved status changes and history lines.
- A report saved to `reports/mailbox-<YYYY-MM-DD>.md`: what was found, what changed, what was left alone, and anything that needs the user (interviews to confirm, assessments to take).

### Done when

- [ ] No email was sent, replied to, deleted, moved, labeled or marked as read.
- [ ] Every status change was approved by the user in this session.
- [ ] `yourNotes` untouched (`check_tracker.py`).
- [ ] Report saved.

---

<!-- stages/07-resume.md -->

## Stage 07: Resume

Build the user's resume from facts they state, shaped by what real postings for their target role ask for, and checked by script before anyone sees it as final. Also makes tailored versions for single listings. Run when the user asks, or from the intake when the user wants a new or improved resume.

**Nothing on the resume may be something the user did not say.** Every fact comes from `my-files/resume-facts.md`, which the user confirms line by line.

### When to run, and when not to

- The user said in the intake (or later) that they want a new resume, or want theirs improved: run it.
- The user has a resume they are happy with and opted out: do not run it. Never rewrite their resume unless they ask in that session. You may offer one short list of suggestions from `references/resume-guide.md`, once, and only if they want it.

### Inputs

- `rules.md` and `my-files/my-rules.md` (target roles, industries, writing style).
- `references/resume-guide.md`: the general rules, examples by field, and the default.
- `references/resume-facts-template.md`: the shape of the facts file.
- The user's current resume, if they have one (`my-files/resume.pdf` or `my-files/resume.md`), as a source of facts only.
- 3 to 5 real postings for the target role (Part B).
- For a tailored version: the listing's `postingText`.

### Part A. Collect the facts

Write to `my-files/resume-facts.md`, using the template. Ask **one question at a time** and wait for each answer.

1. If the user has a resume, read it first and fill in what it already says. Then show each job's facts and ask: "Is all of this true and current? Anything to add or remove?"
2. For each job, newest first:
   1. "What was your job title, the employer, the city, and the start and end month and year?"
   2. "In a few sentences, what did you do day to day? Who did you serve or sell to?"
   3. "What are you proudest of in this job? Results, numbers, awards, promotions, things you built or fixed."
   4. For every number the user gives: "Can you stand behind that number if an interviewer asks? Where does it come from?" Keep only numbers they confirm. Write the source next to each one.
   5. "Did you lead, train or manage anyone? How many?"
   6. "What tools, systems or software did you use?"
3. Education: school, degree, field, year (or "in progress"). Ask whether to show the year.
4. Licenses and certifications: name, issuer, state if any, year. **Never the license number.**
5. Skills the user can show in an interview.
6. Anything else worth showing: volunteer work, languages, military service, publications.
7. Gaps: "Is there any gap of six months or more you want to explain, or leave as is?" Never hide or change dates to cover a gap.
8. "Is there anything that must stay off your resume?" (for example a current employer's client names, or a job they do not want listed).
9. Show the full facts file. The user approves it before any resume is written. Every later change to a fact goes into this file first.

### Part B. Learn what employers ask for

Before writing, look at what employers actually ask for in real postings for the user's target role, so the resume puts first what matters for that job. This works the same for any job in any field. `references/resume-guide.md` has examples by field showing what a finished summary looks like.

**Every user gets a resume, in any field.** If a step below cannot be done, go to the next fallback. Never stop the resume because postings are hard to find.

1. **Pick the target.** Take the main target role and level from `my-rules.md`. If the user has two quite different targets, ask which one this resume is for. One resume per target.
2. **Gather 3 to 5 real postings for that role**, newest first, in this order of preference:
   1. Listings already in the tracker for this role that have `postingText` saved.
   2. Postings on employers' own career sites, found by web search, for this role and level in or near the user's allowed places (or remote roles open to them). Posted in the last six months where possible.
   3. Postings the user pastes or attaches.
   Never open LinkedIn. Job aggregators may be used to find which employers post the role; read the posting itself on the employer's own site when you can.
3. **Read each posting and note**, with the posting it came from:
   - Must-have credentials: licenses, degrees, certifications, clearances.
   - Tools, systems and hard skills named.
   - The results the employer cares about (for example revenue, patient outcomes, uptime, students served, safety record).
   - The words the employer uses for the work (for example "territory", "pipeline", "caseload", "care plan").
   - Seniority signals and anything that sets length (years required, scope).
   - Tone (plain, formal, technical).
   - Anything asked for beyond the resume (portfolio, writing sample, references up front).
4. **Sum up what employers ask for.** What appears in at least two postings counts; what appears in one is noted but given less weight.
   - **Section order:** which sections come first. Credentials that most postings require and the user holds go directly under the summary.
   - **What leads each job:** the kind of proof that goes first in each role's bullets, matched to the results employers asked for.
   - **Terms to mirror:** the employers' own words for the work. Mark each one "in your facts" or "not in your facts". Terms not in the facts are **never** used. List them for the user as possible gaps: if the user says one is true, add it to the facts file first (with their confirmation), then it may be used.
   - **Length and tone.**
   - **Closest example(s)** from `references/resume-guide.md`, and the career-changer notes if the user is moving fields.
5. **Show this summary to the user** in plain words, with the postings it came from (company, title, link). Ask: "Does this match the jobs you want? Anything to change?" Make their changes.
6. **Save it** in the "What employers ask for" section of `my-files/resume-facts.md`, with the date and the user's confirmation. Part C follows it.

**Fallbacks, in order, so every user gets a resume:**

- **Fewer than 3 postings found** (rare role, small market, no web access on this device): use the ones found, plus the closest example. Write that down ("Based on: 2 postings plus example").
- **No postings at all:** ask the user to describe two or three jobs they want in their own words, or to paste any job description they have seen. Build the summary from that plus the closest example ("Based on: user description plus example").
- **Still nothing:** use the "Default (any job)" in `references/resume-guide.md`. It works for every job ("Based on: default").
- In every case the user confirms the summary before Part C, and the source is written down.

**Refresh:** if the user's target role changes, or the summary is more than six months old, offer to redo Part B before making a new resume.

### Part C. Write it

1. Write `my-files/resume.md` in the exact format in `references/resume-guide.md` ("File format").
2. Follow every rule in "General rules" and the "What employers ask for" section saved in the facts file. The resume's sections must come in the section order in "What employers ask for".
3. Draft **one section at a time**, in the section order in "What employers ask for" (contact line and summary always first). Show each one and get a yes or changes before the next.
4. Then show the whole resume, and run the checks:
   - `python tools/check_resume.py my-files/resume.md --facts my-files/resume-facts.md`
   - Fix everything it reports. Do not show the resume as final until it passes.
5. Build the PDF: `python tools/build_resume.py my-files/resume.md my-files/resume.pdf`. If the user already had a `resume.pdf`, first copy it to `backups/resume-before-<YYYY-MM-DD>.pdf`.
6. Check the page count the build reports: one page for under ten years of experience, two at most otherwise. If it is over, cut the oldest or weakest bullets (ask the user which), never the font size below the minimum.
7. Ask the user to open the PDF and approve it. Only an approved PDF is used to apply.

### Part D. Tailored version for one listing (only when the user asks)

1. Read the listing's `postingText`. List the posting's top requirements in plain words.
2. Build a tailored copy from the same facts file:
   - **Allowed:** reorder bullets, choose which facts to show, shorten bullets, rewrite the summary for this role, use the posting's own words for a skill **only where the facts show that skill**.
   - **Not allowed:** any fact, number, tool, title or skill not in the facts file. Changed dates or titles. Copying sentences from the posting.
3. Show what changed compared with the main resume, in a short list.
4. Run the same checks, then build `my-files/resumes/resume-<listing id>.pdf`.
5. After the user approves it, add a history line to the listing: `YYYY-MM-DD tailored resume approved: resume-<listing id>.pdf`. Stage 03 uploads that file for that listing instead of `resume.pdf`.

### Outputs

- `my-files/resume-facts.md`, approved by the user, with a confirmed "What employers ask for" section.
- `my-files/resume.md` and `my-files/resume.pdf`, approved by the user.
- Optional: tailored PDFs in `my-files/resumes/`, each approved.
- No tracker writes, except the one history line for an approved tailored version.

### Done when

- [ ] The user approved the facts file before any resume was written.
- [ ] A "What employers ask for" section is saved in the facts file, built from 3 to 5 real postings or from a named fallback, and the user confirmed it.
- [ ] No term from the postings was used unless it is in the facts file.
- [ ] Every number, title, date, tool and skill on the resume is in the facts file (`check_resume.py`).
- [ ] `check_resume.py` passes: no dashes, no stock phrases, no first person, no personal data that does not belong on a resume, bullets a sensible length, standard headings.
- [ ] The page count is within the limit.
- [ ] The user approved the final PDF.
- [ ] Any earlier `resume.pdf` was backed up first.

---

<!-- stages/08-company-research.md -->

## Stage 08: Company research

Research sessions the user starts by asking. Four kinds:

| Kind | The user says something like | Writes to the tracker |
|---|---|---|
| A. Find employers | "Find employers for my target list" | New `companies` rows, after the user approves each one |
| B. Company deep dive | "Tell me about [company]" | Nothing (a report only) |
| C. Industry map | "Map the [industry] employers around [place]" | Nothing, unless the user then asks to add some (run A for those) |
| D. Role research | "What does a [title] do, and what does it pay around here?" | Nothing (a report only) |

Ready-to-use wording for each is in `references/prompts.md`.

> **Site terms.** LinkedIn and some job boards forbid automated access in their terms. Research uses web search, employers' own websites, and public lists. It never opens LinkedIn, never scrapes a site, and never signs in anywhere. Job aggregators are used only to learn company names, never as proof that a job exists. The user is responsible for following each site's terms.

### Rules for every research session

- **Sources:** web search results, employers' own sites (including careers and locations pages), and public lists: business journal and newspaper lists, chamber of commerce directories, economic development agency lists, industry association member lists, conference exhibitor lists, government data, company press releases. **No paid tools, no sign-ins, no LinkedIn.**
- **Every fact gets a link.** If you cannot link it, do not state it as fact.
- **Exact names.** Use the company's own spelling. Check the target list for an exact match before calling anyone new (`recurring-mistakes.md` item 7).
- **Never suggest** the user's current employer, anyone on their never-contact list, or employers in an excluded industry unless the user asks.
- **Helpers:** if you use research helpers, give each about six companies, read only, each in its own browser tab. The main session checks every result and does every write.
- **Size:** about 25 candidates per session at most, so each one gets checked properly.
- Save a report to `reports/research-<kind>-<YYYY-MM-DD>.md` with every source linked.

### A. Find employers (target list building)

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

### B. Company deep dive

For one employer the user names (often before applying or before an interview).

1. What they sell, to whom, and how (their own site).
2. Size, locations, and where the user's target role sits (their own site, press releases, government filings for public companies).
3. Recent news from the last 12 months (established news outlets and trade publications).
4. Open roles that match the user's targets, from their own careers site, with links.
5. How the user's background fits, in two or three plain sentences, using only the user's stated facts.
6. Questions worth asking them.
7. Save `reports/research-company-<company-slug>-<YYYY-MM-DD>.md`.

### C. Industry map

For one industry in or near the user's place.

1. List the main employers in that industry that the user's place rules allow, grouped by type (for example software vendors, insurers, service firms), each with a link and one line on what they do.
2. Mark which are already on the target list.
3. Note which roles in that industry match the user's targets, and where they usually sit (sales team, clinical team, operations).
4. Save the report. To add any to the target list, run part A for those names.

### D. Role research

For one job title the user asks about.

1. What the role does day to day, from three or more employers' own postings, each linked.
2. What those postings require and prefer, and how that compares with the user's stated experience (facts only).
3. Pay: only pay **posted by employers** for this role in the user's area or remote roles open to them. Give the range and the number of postings it comes from. If fewer than three postings show pay, say so. Never estimate a number without a posting behind it.
4. Typical next roles, if postings or employers' own career pages say so.
5. Save the report.

### Outputs

- Part A: approved `companies` rows, and a report.
- Parts B, C, D: a report only.

### Done when

- [ ] Every fact in the report has a link to an allowed source.
- [ ] No LinkedIn page was opened, no site required a sign-in, nothing was scraped.
- [ ] Part A: every new employer was approved by the user, has its own careers site link, and matches no existing name, excluded industry or never-contact entry. `check_tracker.py` passes.
- [ ] Report saved.

---

<!-- references/tracker-columns.md -->

## Tracker columns

The tracker has five parts. In the artifact tracker they are **collections** (each row is a record). In the spreadsheet tracker they are **tabs** (each row is a row). The names are the same in both, so every stage works with either.

Who writes: **Claude** means sessions may write it under the rules. **You** means only the user writes it. **Both** means the user may edit it, and sessions write it only as the stages say.

### companies: your target list

One row per employer.

| Column | What it holds | Who writes |
|---|---|---|
| `id` | A short name with no spaces, for example `example-health-co`. Never changes. | Claude |
| `company` | The employer's name, spelled exactly the same everywhere in the tracker. | Both |
| `careersSite` | Link to the employer's own job board. | Both |
| `tier` | `A`, `B` or `C`. What each letter means is in `settings`. | Both |
| `industry` | The employer's industry, using the same words as `settings.industryOrder` where it fits. | Both |
| `keepAnyway` | `yes` keeps this employer in sweeps even if its industry is excluded. Otherwise `no`. | You |
| `onHold` | `yes` means sweep it, but do not apply without your go-ahead. Otherwise `no`. | You |
| `added` | Date the employer was added, `YYYY-MM-DD`. | Claude |

### coverage: one row per employer, per sweep record

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

### listings: one row per job posting

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
| `family` | The kind of role, one of `settings.roleFamilies`. | Claude |
| `posted` | Date posted, as shown. | Claude |
| `pay` | Posted pay exactly as written, or "not posted". | Claude |
| `why` | One or two sentences on why it fits, and any reach. | Claude |
| `teaches` | What the role would teach you. Starts with "Stated:", "Not stated." or "Not read." | Claude |
| `priority` | `High`, `Medium`, `Low` or `On hold`. Work order for applying. | Both |
| `status` | Where it stands. See the list below. | Both, under the rules |
| `appliedDate` | Date the application went in, `YYYY-MM-DD`. | Claude |
| `postingText` | The full text of the posting, saved so it survives after the posting comes down. | Claude |
| `reviewReason` | Why a listing at Review fit needs your call. | Claude |
| `history` | Dated log of everything sessions did. **Add only, never change or delete.** Entries are separated by ` \| `. | Claude (append only) |
| `yourNotes` | Your own notes. **Claude never writes this.** | You |
| `managerName`, `managerTitle`, `howIdentified`, `confidence`, `profileUrl`, `emailOrFormat`, `connectionNote`, `longMessage` | Outreach research and drafts (stage 04). Drafts only. You send. | Claude |

**Status values:** `To apply`, `Applied`, `Followed up`, `Interview`, `Offer`, `Review fit`, `On hold`, `Rejected` (the employer said no), `Closed` (you passed), `expired` (the posting came down), `filled` (the employer says it is filled).

Listings at **Applied, Followed up, Interview or Offer** are never changed by a sweep, ever.

### answers: your answer bank

One row per answer you give on forms. See `answer-bank.md`.

| Column | What it holds | Who writes |
|---|---|---|
| `id` | Short name, for example `pay-text` or `ref-1`. | Claude |
| `topic` | `Contact`, `Work history`, `Education`, `Pay`, `Voluntary` (diversity questions), `References`, `Links`, `Work authorization`, `Account`, or `Other`. | Both |
| `question` | The question as forms usually ask it. For an `Account` row, the website. | Both |
| `answer` | Your answer. For an `Account` row, the username only. **Never a password, ID number or bank detail.** | Both |
| `useWhen` | When to use it, or when to ask you first. | Both |
| `updated` | Date last changed. | Both |

### settings: one row

The `id` is `main`. Lists are separated by `; ` (semicolon and space).

| Column | What it holds | Example |
|---|---|---|
| `id` | Always `main`. | `main` |
| `tierA`, `tierB`, `tierC` | What each employer tier means for you. | `Employer based in my home metro` |
| `industryOrder` | Industries you want, most wanted first. The tracker groups listings in this order. | `Health tech; Medical software; Health insurance` |
| `excludedIndustries` | Industries hidden from the main views and skipped in sweeps. | `Staffing; Retail` |
| `roleFamilies` | Kinds of role. A `*` after a name marks a target family. | `Account executive*; Clinical specialist*; Customer success` |
| `tracks` | Separate searches, if you run more than one. Most people have one. | `Main` |
| `priorities` | Priority groups, in work order. | `High; Medium; Low; On hold` |

### Checking by script

Every stage that writes ends with a check: `tools/check_tracker.py` compares a snapshot from before the session with one from after, and fails if any rule was broken (`yourNotes` changed, history rewritten, a listing at Applied or later touched by a sweep, a new listing missing a column, and so on).

**Spreadsheet:**

```
python tools/check_tracker.py snapshot my-files/job-search-tracker.xlsx backups/before.json
  (the session runs)
python tools/check_tracker.py snapshot my-files/job-search-tracker.xlsx backups/after.json
python tools/check_tracker.py check backups/before.json backups/after.json --stage sweep
```

**Artifact:** list each collection (`companies`, `coverage`, `listings`, `answers`, `settings`) with `ArtifactData`, and save the results together as one JSON file shaped like `{"companies": [...], "coverage": [...], "listings": [...], "answers": [...], "settings": [...]}`. Do this before and after, then run the same `check` command on the two files.

The `--stage` choices are `sweep`, `fit`, `apply`, `outreach`, `prep`, `mailbox`, `resume`, `research` and `user` (a change the user asked for directly).

---

<!-- references/answer-bank.md -->

## Answer bank

The answer bank lives in the tracker, not in this Skill: the `answers` collection (artifact) or the `answers` tab (spreadsheet). Read it fresh at the start of every application session. It is the source of truth. Nothing in this file overrides it.

### How to use it

- When a form question matches an entry, answer from it without asking.
- When a question is worded unusually, or the entry's `useWhen` says to ask, confirm with the user before using the entry.
- Pay questions use the `Pay` entries: the wording where the form takes text, the single number where it needs one.
- Voluntary diversity questions use the `Voluntary` entries. With no entry, choose "I don't wish to answer" and tell the user.
- References come only from the `References` entries, in the order listed.
- Work history comes from the `Work history` entries and `my-files/resume.md`. They must agree. If they do not, ask the user.
- Add each new application-system account as an `Account` row: the website in `question`, the username in `answer`. **Never a password.**

### What never goes in the answer bank

- Passwords, security answers, one-time codes.
- Social Security numbers or other government ID numbers, driver's license numbers.
- Bank account, routing or card numbers.

### Autonomy

Any extra autonomy the user grants (for example auto-submit) lasts for one session only and is never saved here as a standing permission.

---

<!-- references/application-techniques.md -->

## Application techniques

General methods for application forms. No employer names. Add a line when a session finds something new (stage 03, step 17), with the user's OK.

### Upload methods

Try them in the order stage 03 gives (a to e). What each looks like on the page:

- **Plain file input.** A "Choose file" control. Use the file upload tool on it directly. Never click it: clicking opens the computer's own file picker, which the browser tools cannot see.
- **Button over a hidden input.** A styled "Upload resume" or "Attach" button. The real `input[type=file]` is usually hidden next to it or inside the same form section. Find it with `read_page` (it often shows as a button with type "file"), `find` ("file input for resume"), or a read-only page check such as listing every `input[type=file]` with its id and `accept` value. Upload to that input.
- **Drag-and-drop zone.** "Drop your resume here". There is almost always a hidden file input inside the zone. Upload to that input. Dragging a file from the computer is not needed.
- **"Autofill from resume" button.** Opens the computer's file picker, then reads the resume and fills fields. Find the hidden input behind it and upload there. Afterwards, check every field it filled against the answer bank. Auto-fill often gets phone numbers, dates, job titles and school names wrong, and sometimes puts the current employer where a reference should be.
- **Paste box.** "Paste your resume" or "Enter manually". Use the text of `my-files/resume.md`. Flag it in the review summary.
- **Built-in browser pane.** It has no file upload tool. Switch the application to Claude in Chrome.

### How to tell an upload worked

- The page shows `resume.pdf` (or a preview of its contents) next to the control.
- If the control shows a different file name, a size of 0, or an error, the upload failed. Try the next method.
- Some forms only read the file when the next page loads. Check again after moving on.

### Routes that are always walls

- "Apply with LinkedIn", "Import from LinkedIn", or any LinkedIn sign-in.
- "Import from Google Drive", "Dropbox", "OneDrive" or any other account sign-in.
- Anything asking for a password, a one-time code or a CAPTCHA.

These go to the user.

---

<!-- references/recurring-mistakes.md -->

## Recurring mistakes to avoid

Each of these happened during real use of this system. Read this list before any tracker write.

1. **Aggregator pages treated as proof.** An unattended run marked a batch of listings expired because a job aggregator showed them gone. Most were still live on the employers' own sites, and some were already Applied. Only the employer's own site decides.
2. **Changing listings at Applied or later.** The same run did it. Sweeps never touch them.
3. **Starting work nobody asked for.** A session asked to do one small task ran a whole other stage and wrote to many listings. Do only the task asked.
4. **Two sessions writing the same file.** The last write silently won and the earlier work was lost. One session owns the tracker at a time. For the spreadsheet, the user's own Excel window counts as a second writer: ask them to close it.
5. **Overloaded research helpers.** Helpers given 11 or more employers silently dropped some. Keep it to about six each.
6. **Stale reads.** Values copied from an earlier read were wrong by the time of the write. Read each row fresh right before writing it, and check by script after.
7. **Loose company matching.** A first-word match filed one company's listings under a different company whose name started the same way. Match the full company name, exactly as in `companies`.
8. **A background the user wants to leave, used as a selling point.** If the user says they are moving away from a kind of work, it is never a plus in a fit call or a message.
9. **Rules left in old prompts.** Saved prompts and notes carried outdated rules that later sessions followed. The rules live only in `rules.md` and `my-files/my-rules.md`.
10. **Shared browser tabs.** Two helpers working in one browser tab overwrote each other's pages. Each helper opens its own tab.
11. **Unattended runs that could not do the work.** A scheduled run in the cloud had no browser access to employer sites and no access to the user's folder, so it wrote bad data. Every stage is started by the user, in a session that can reach the sites and files it needs.

---

<!-- references/my-rules-template.md -->

## My rules

<!-- The intake interview (stages/00-intake.md) fills this in and saves it as my-files/my-rules.md.
     Every line in [brackets] is replaced with the user's answer. Lines that do not apply say "None". -->

Last updated: [YYYY-MM-DD]

### Tracker

- Kind: [Artifact / Spreadsheet]
- Where: [artifact link, or my-files/job-search-tracker.xlsx]

### 1. Target roles

- Roles I want: [titles or kinds of role]
- Seniority: [entry, mid, senior, or a range]
- Roles that are out even if the title sounds close: [list]
- What a good role looks like, in my words: [one or two sentences]

### 2. Place

- Home base: [city or metro]
- Allowed: [home metro / a territory based out of my home metro / multi-state territory / fully remote]
- Remote rules: [for example "fully remote only if my state is allowed"]
- Nearby cities allowed only above a pay bar: [cities and the bar, or None]
- Relocation: [no / yes, to these places]

### 3. Pay

- Floor: [amount and period, for example $70,000 a year]
- What counts toward the floor: [base only / base plus commission or bonus]
- How I state pay on forms when text is allowed: [wording]
- The single number I give when a form needs one: [number]

### 4. Industries and products

- In: [list]
- Out: [list, with the reason when it helps]
- Excluded industries (also saved in the tracker settings): [list, or None]

### 5. Experience

- My years in the work I am targeting: [number, and what counts]
- How far I stretch on required years: [for example "apply if they ask for up to 3 more years than I have"]
- Licenses I hold: [list, or None]
- Degrees I hold: [degree and field]

### 6. Hard noes

- [part-time / contract / commission only / overnight shifts / travel over a set share / anything else]

### 7. Employers

- On hold (sweep, but do not apply without my go-ahead): [list, or None]
- Never contact: [my current employer, and anyone else]
- Aggregator-only exceptions (no job board of their own; their verified page on one aggregator counts): [list, or None]

### 8. Autonomy

- Sweep: [autonomous within the rules / ask before writing]
- Fit calls: [autonomous / bring me every call]
- Apply: Human review before every submission. Auto-submit is off unless I turn it on for one session in writing.
- Outreach: [off / drafts when I start it by name]
- Mailbox check: [off / on, using my email connector]

### 9. Writing style

- [for example "short and direct, no exclamation marks, sign off with my first name only"]

### 10. Dated changes

<!-- Newest first. Each line: YYYY-MM-DD what changed. -->
- [YYYY-MM-DD] Rules created by the intake interview.

---

<!-- references/sample-resume.md -->

## Sample resume (made up)

This is a made-up person, to show the exact format `my-files/resume.md` must follow. It is the same format as "File format" in `resume-guide.md`, and the one `tools/build_resume.py` and `tools/check_resume.py` read. Everything below the line is the resume.

If the user keeps their own resume (they opted out of stage 07), `my-files/resume.md` is a plain copy of their PDF's text for filling forms, and does not need to follow this format.

---

## Jordan Reyes
Larkfield, Calder | jordan.reyes@example.com | (555) 010-0199

### Summary
Operations coordinator with 5 years in a regional hospital system, moving into software customer success. Runs scheduling and vendor work for 3 clinics, and trained 40 staff on a new scheduling system.

### Experience
#### Operations Coordinator | Example Regional Health | Larkfield, Calder | 2022 to Present
- Run day-to-day scheduling and vendor contracts for 3 outpatient clinics.
- Led staff training when the clinics moved to a new scheduling system; trained 40 staff in 6 weeks.
- Cut appointment no-shows by 20% with a reminder call process.

#### Front Desk Lead | Example Family Clinic | Larkfield, Calder | 2020 to 2022
- Led a front desk team of 4.
- Handled insurance checks and patient questions for about 60 visits a day.

### Education
#### Bachelor of Science, Health Administration | Example State University | 2020

### Skills
- Systems: Scheduling systems, Electronic health record front-desk modules
- Strengths: Staff training, Vendor contracts and renewals

---

<!-- references/resume-guide.md -->

## Resume guide

Rules for every resume stage 07 writes, for any job in any field. "General rules" always apply. What goes first on a resume comes from real postings for the user's target job (stage 07 Part B). The examples by field below show finished results for common jobs; they are not a list the user must fit into. When nothing else is available, use the default, so every user gets a resume.

### General rules

**Honesty**
- Every fact comes from `my-files/resume-facts.md`. Nothing invented, nothing rounded up, no title the user did not hold, no tool they did not use.
- Numbers appear exactly as the facts file states them.
- Strong verbs only where the facts support them. "Led" needs a fact that says they led. "Managed" needs people or a budget they managed.
- Dates are real. Gaps are not hidden by changing dates.

**Format (so application systems can read it)**
- One column. No tables, text boxes, graphics, icons, photos, charts or skill-level bars.
- Standard headings: Summary, Experience, Education, Licenses and Certifications (if any), Skills. Optional: Volunteer Work, Languages, Military Service, Projects, Portfolio. Their order comes from the "What employers ask for" section of the user's facts file; the default order is Summary, Experience, Education, Licenses and Certifications, Skills.
- Plain fonts. The build script uses Helvetica, 10 to 11 point for body text, never below 9.5.
- Length: one page for under ten years of experience, two pages at most.
- Dates in one style throughout: "Mar 2021 to Present" or "2021 to Present". Words, not dashes.
- Saved as PDF with the user's name in the file name only if the user wants that. Default: `resume.pdf`.

**Contact line**
- Name, city and state, email, phone. Optional: LinkedIn or portfolio link, if the user gives it.
- Never: street address, date of birth, age, photo, marital status, nationality, Social Security or other ID numbers, license numbers, salary history.

**Summary**
- Two or three lines. Who they are in this field, their strongest proof, and what they are moving toward.
- No pronouns at all ("I", "my", "she", "her"). No buzzwords.

**Bullets**
- Start with a verb: past tense for past jobs, present tense for the current one.
- One idea per bullet. At most two lines (about 200 characters).
- Lead with the result when there is one: what changed, by how much, for whom.
- Three to six bullets for recent roles, one to three for older ones. Roles over 15 years old may be grouped under "Earlier experience" with titles only.
- Numbers as digits ("12 nurses", "$1.2 million"). Spell out an acronym once unless everyone in the field knows it.

**Words to avoid** (they read as filler and are checked by script): results-driven, detail-oriented, team player, go-getter, hard-working, self-starter, synergy, dynamic, passionate, proven track record, responsible for, duties included, think outside the box, best of breed, rockstar, ninja, guru, plus every stock phrase the project's writing rules forbid. No em dashes or en dashes.

### Default (any job)

Used when no postings can be found and the user cannot describe the jobs they want. It suits every field.

- Section order: Summary, Experience, Education, Licenses and Certifications (if any), Skills.
- Summary: the role they want, their years doing the closest work, and their strongest fact.
- Each job leads with the bullet that shows the biggest result or the most responsibility, then the work most like the target role.
- Skills: the tools and skills from the facts file that the target role most likely uses. Ask the user which those are.
- Plain tone. One page under ten years of experience.

### Examples by field

What usually goes first on a resume for some common jobs. For a real user, this always comes from postings for their own target job (stage 07 Part B). These examples help spot anything missed. A job not listed here is handled exactly the same way.

**Sales and business development**
- Summary names the kind of sale (new business or existing accounts, deal size, buyer) and the best number.
- Every role leads with quota attainment, revenue, rank or deals closed, if the facts have them, with the period ("in 2024", "first quarter").
- Show the sales cycle and buyer: who they sold to, how long deals took, what they sold.
- Skills: CRM and prospecting tools the user actually used.

**Healthcare (clinical)**
- Licenses and Certifications move up, directly under the summary. Use full names (Registered Nurse, State of Calder; Basic Life Support).
- Each role names the setting (intensive care, outpatient clinic), unit size or patient load if known, and specialties.
- Results are about safety, quality, training and process: audits passed, protocols adopted, staff trained.

**Healthcare technology or medical sales (and other industries that sell to clinicians)**
- Clinical credentials near the top, because buyers trust clinicians.
- Bullets that show persuading, training, adopting new systems, working with vendors, or leading change come first in each clinical role.
- A short "Systems" line in Skills: charting and other software used.

**Software, IT and technical roles**
- Skills section near the top, grouped (languages, tools, platforms). Only what the user can discuss in an interview.
- Bullets show what was built or fixed, scale (users, data, uptime) and the result.
- A link to a portfolio or code samples if the user has one.

**Finance, insurance and banking**
- Licenses and designations near the top (with state and status, never numbers).
- Bullets show accuracy, compliance, portfolio or book size, and client retention.
- Conservative tone. No casual phrasing.

**Education and training**
- Certifications and subjects near the top.
- Bullets show learners served, outcomes, programs built.

**Skilled trades, logistics and operations**
- Certifications, licenses and equipment near the top.
- Bullets show safety record, volume, on-time rates, cost or time saved.

**Government and nonprofit**
- Fuller detail is expected: two pages are fine with enough experience.
- Name programs, funding sources, communities served and outcomes.
- Match the posting's required qualifications in plain words where the facts support them.

**Creative, marketing and communications**
- Portfolio link in the contact line.
- Bullets show campaigns, audiences, reach and results.
- Still one column and plain fonts: the portfolio carries the visual style, the resume stays readable by systems.

### Career changers

- The summary bridges the two fields in one sentence: what they did, what carries over, what they are moving into.
- Keep the experience in time order. Do not hide the old field.
- In each past role, put first the bullets that match the new field (persuading, training, numbers, customers, systems).
- A "Relevant Skills" line can come before Experience if the user has very little direct experience. Every skill on it must appear somewhere in the facts.
- Never use a title from the new field for a job in the old field.

### File format (for `my-files/resume.md`)

The build script reads exactly this shape:

```
## Full Name
City, State | email@example.com | (555) 010-0000 | optional link

### Summary
Two or three lines of plain text.

### Licenses and Certifications
- Registered Nurse, State of Calder

### Experience
#### Job Title | Employer | City, State | 2023 to Present
- Bullet.
- Bullet.

### Education
#### Degree, Field | School | Year

### Skills
- Group: item, item, item
```

Headings use `##`. Jobs and schools use `###` with ` | ` between title, employer, place and dates. Bullets start with `- `.

---

<!-- references/resume-facts-template.md -->

## Resume facts

<!-- Stage 07 fills this in with the user, one question at a time, and saves it as my-files/resume-facts.md.
     Everything on the resume must come from this file. Every number has a source the user named.
     The user approves this file before any resume is written. -->

Last approved by the user: [YYYY-MM-DD]

### Contact (for the resume only)

- Name: [as it should appear]
- City and state: [city, state]
- Email: [address]
- Phone: [number]
- Link (optional): [portfolio or profile link, or None]

### Target

- Role: [the role this resume is for]
- Career changer: [yes / no]
- Years of experience to state on the resume: [number, and what it counts, for example "6, hospital nursing since Jun 2020"]

### What employers ask for

<!-- Built in stage 07 Part B from 3 to 5 real postings for the target role, then confirmed by the user. -->

- Based on: [postings / N postings plus example / user description plus example / default]
- Built and confirmed by the user: [YYYY-MM-DD]
- Postings used:
  - Posting: [company] | [title] | [link] | [date posted or read]
- Section order: [for example Summary, Licenses and Certifications, Experience, Education, Skills]
- What leads each job: [the kind of proof that goes first]
- Must-have credentials the postings ask for: [list, and whether the user holds each]
- Terms to mirror (in your facts): [list]
- Terms the postings use that are not in your facts (never used unless added to the facts first): [list]
- Length and tone: [one page, plain / two pages, formal]
- Closest example: [name from references/resume-guide.md, plus "career changer" if it applies]

### Jobs (newest first)

#### [Job title] | [Employer] | [City, State] | [Start month year] to [End month year or Present]

- Day to day: [what they did, in their words]
- Served or sold to: [who]
- Results:
  - [result] (number: [the number], source: [where it comes from, as the user said])
- Led, trained or managed: [who and how many, or None]
- Tools and systems: [list]
- Awards or promotions: [list, or None]

### Education

#### [Degree, field] | [School] | [Year, or "in progress"] | Show year: [yes / no]

### Licenses and certifications

- [Name], [issuer or state], [year]. Never the number.

### Skills the user can discuss in an interview

- [skill]

### Other (optional)

- Volunteer work: [ ]
- Languages: [ ]
- Military service: [ ]

### Gaps

- [dates and what the user wants said, or "leave as is"]

### Must stay off the resume

- [anything the user named, or None]

---

<!-- references/prompts.md -->

## Prompts: what to say to Claude

Copy any of these into a session. Words in [brackets] are yours to fill in. Each one starts the stage named after it, and only that stage.

### Getting set up

- "Set me up for my job search." (Stage 00: the intake interview)
- "I want to change my rules: [what changed]." (Stage 00, only the parts you name)
- "Publish tracker/tracker-page.html as a new artifact with the db capability, and give me the link." (Tracker setup, see the README)

### Resume (stage 07)

- "Build my resume." (Questions about your jobs, a quick look at real postings for the job you want, then the resume)
- "I have a resume. Read it and help me improve it." (Starts from your file; asks before changing anything)
- "Show me what my resume would look like for [role]." (A second version aimed at another kind of job)
- "Update my resume for the jobs I want now." (Looks at fresh postings; do this when your target changes or every six months)
- "Use these postings for my resume: [links or pasted text]." (Claude reads the postings you pick instead of finding its own)
- "Make a tailored resume for the [company] [title] listing." (Reorders and chooses from your facts only; you approve before it is used)
- "Add this to my resume facts: [fact]."

### Finding employers and researching them (stage 08)

- "Find employers for my target list." (Part A, using your rules)
- "Find [industry] employers in or near [place]." (Part A, narrowed)
- "Find employers like [company A] and [company B]." (Part A, starting from competitors and neighbors of good fits)
- "Find remote-friendly employers in [industry] that hire people in [state]." (Part A, remote only)
- "Tell me about [company]." (Part B, deep dive)
- "Map the [industry] employers around [place]." (Part C)
- "What does a [title] do, and what does it pay around here?" (Part D)
- "Add these employers to my target list: [names]." (Sweep step 0)

### Sweeps and fit (stages 01 and 02)

- "Run a sweep." (The employers swept longest ago, plus a recheck of open listings)
- "Sweep [company names]."
- "Recheck my To apply listings." (Confirms they are still open on the employers' own sites)
- "Is this a fit? [link to a posting on the employer's own site]"

### Applying (stage 03)

- "Let's apply." (Highest priority first; you review every form)
- "Apply to the [company] [title] listing."
- "Do a dry run on the [company] listing." (Fills everything, submits nothing)
- "I turn on auto-submit for this session." (Only if you want it; it lasts this session only)

### Outreach (stage 04)

- "Run outreach." (Drafts only; you send)
- "Run outreach on the [company] listing."

### Interviews (stage 05)

- "Prep me for my [phone screen / hiring manager / panel] interview with [company] on [day]."

### Email (stage 06)

- "Check my email for employer replies."
- "Check my email since [date]."
