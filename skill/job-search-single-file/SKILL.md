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
- `references/board-techniques.md`: how to read each kind of job board, boards that misreport location, signs a posting is gone, and how to run research helpers.
- `references/application-techniques.md`: how each platform's application form behaves, upload methods, resume-reader mistakes, legal text to watch for, and walls by platform.
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
- **Hourly pay:** for a full-time role, multiply the hourly rate by 2,080 hours to compare with a yearly floor, and say so in `why`. For part-time, compare only if the user's rules allow part-time.
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
  - The mailbox check (stage 06) may set **Followed up**, **Interview**, **Rejected**, **Offer**, or **expired** (the employer cancelled the role), only after the user says yes to each change in that session.
  - The user may ask for any status change directly.
  - Nothing else changes a status.
- Never change the status of a listing at Applied, Followed up, Interview or Offer except as above. On those listings sessions may only append history lines, and stage 04 may fill the outreach columns.
- **Re-read before writing.** Read the row fresh just before you change it, and write only the fields you changed. In the artifact tracker, pass the `version` you read as `if_version` on every write to an existing row; the database refuses the write if the row changed since ("version_mismatch"). Then read it again and redo the write against what it holds now. In the spreadsheet, if the row changed since you read it, stop and read it again.
- **Back up before bulk writes.** Before writing more than five rows in one session, save a copy of the whole tracker to `backups/`:
  - Artifact: list every collection with `ArtifactData` (`out_dir` set to a new folder under `backups/`), then combine them with `python tools/check_tracker.py snapshot-dir <that folder> backups/tracker-backup-<YYYY-MM-DD>-<HHMM>.json`.
  - Spreadsheet: copy the file to `backups/tracker-backup-<YYYY-MM-DD>-<HHMM>.xlsx`.
- **When a check fails because of something the user did** (they typed a note, or changed a status on the tracker page during the session), tell the user. Never undo their change, and never write `yourNotes` to make a check pass.
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
- Plain language. No em dashes or en dashes.
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
- **If an answer is already known** (setup in `START-HERE.md` already chose the tracker and asked about the resume), do not ask it again. Say in one line what you have and move on.
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
1. "Will you keep your tracker as a private web page in your Claude account (recommended) or as a spreadsheet file?" [Tracker]
   - **Artifact, already published:** "Paste the link." Save it.
   - **Artifact, not published yet:** offer to publish it now, together: publish `tracker/tracker-page.html` as a new artifact with the `db` capability (README, "Step 4. Set up your tracker"), show the user the empty tracker, and save the link. If publishing is not possible here (for example on a device without that feature), offer the spreadsheet for now.
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
4. Write the tracker's `settings` record (see `references/tracker-columns.md`). Take a snapshot first (`references/tracker-columns.md`, "Checking by script"). Show the values first and save after the user says yes. The record's id is `main`. In the spreadsheet it already exists (the template has it), so **update** that row (`tools/sheet.py` op `update`, id `main`). In a new artifact tracker it does not exist yet, so create it with `set`. Afterwards, and again after any answer bank entries in step 5, take an after snapshot and run `python tools/check_tracker.py check backups/before.json backups/after.json --stage intake`. The fields:
   - `tierA`, `tierB`, `tierC`: what each employer tier means for this user. Default: A "Employer based in my home metro", B "Employer elsewhere with jobs open to my area", C "Other allowed place".
   - `industryOrder`: the "in" industries, most wanted first.
   - `excludedIndustries`: from question 17.
   - `roleFamilies`: the kinds of role from questions 2 to 4, with a `*` after the ones that are targets.
   - `tracks`: leave as `Main` unless the user is searching for two quite different kinds of role.
   - `priorities`: leave as `High; Medium; Low; On hold` unless the user asks.
5. Ask: "Do you want to start your answer bank now? It holds the answers application forms ask for again and again, so you are not asked each time. You can also fill it later." If yes, ask one item at a time, in this order, and save each to `answers` after the user confirms it. The user may skip any item.
   - **Contact:** full name, preferred name, email, phone and phone type, city and state, county (some forms require it), street address only if they want forms filled with it.
   - **Work history:** each job (title, employer, city, start and end month and year), the **reason for leaving** each one, and whether each past employer **may be contacted**; if yes, that supervisor's name, title and contact details (some forms require them).
   - **Years of experience** in the work they are targeting, and in common form categories (customer service, sales, a key tool).
   - **Education:** school, degree, field, year.
   - **Licenses and registrations:** held, and whether any was ever denied, revoked or suspended. Never the license number.
   - **Work authorization:** authorized to work in the country, needs sponsorship now or later, age 18 or over.
   - **Pay:** the text wording, the single number, and hourly or salary.
   - **Logistics:** earliest start date, willing to relocate, willing to travel (how much), overtime and shift work.
   - **Employer relationships:** currently bound by a non-compete or other restrictive agreement; ever worked for a given employer is asked per form, so note only whether they want to be asked each time.
   - **"Ever been fired or asked to resign":** the user's own answer, or "ask me each time".
   - **References:** names, relationship and contact details, in the order to use them. Never the user's current employer.
   - **Links:** LinkedIn or portfolio (used only when a form requires it).
   - **Voluntary self-identification:** gender, Hispanic or Latino, race, veteran status (and whether "protected veteran" applies), disability. "I don't wish to answer" is a full answer for each.
   - **Optional:** pronouns, consent to text messages.
   - **Always the user's, never stored as an answer:** criminal history, assessments, whether they would sign a future non-solicitation agreement. Tell the user these will always come to them on the form.
   Never ask for or store passwords, ID numbers or bank details.
6. **Resume.** Ask: "Do you already have a resume you are happy with?" Offer three answers, and respect the choice:
   - **"Yes, use mine as it is"** (opt out): ask them to put it in `my-files/resume.pdf`. Offer to make the text copy `my-files/resume.md` from it, and show the copy before saving. Do not rewrite or critique it. Stage 07 never runs unless they ask later.
   - **"Yes, but I want it improved"**: run `stages/07-resume.md`, starting from their file. Their resume is a source of facts, and nothing changes without their yes.
   - **"No" or "I need a new one"**: run `stages/07-resume.md` from the start.
   Tell them they can skip this for now and say "build my resume" any time.
7. **Employers.** Ask: "Do you already have a list of employers you want to work for?" If yes, add them as stage 01 step 1 describes (adding employers). If no, or they want more, offer stage 08 part A ("suggest employers that fit my background"). Do not start it unless they say yes.
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

- **Artifact:** read `companies`, `coverage`, `listings` and `settings` with `ArtifactData` (`list`). Write one row at a time with `update` (or `set` for a new row), after reading it fresh and passing its `version` as `if_version` (a new row needs none).
- **Spreadsheet:** read and write the tabs of the same names in `my-files/job-search-tracker.xlsx` with `tools/sheet.py` or openpyxl. Ask the user to close the file in Excel first.

### Inputs

- `rules.md` and `my-files/my-rules.md`.
- Tracker: `companies`, `coverage`, `listings`, `settings`.
- The session's scope, from the user: which employers, how many, or which listings to recheck. If the user gives no scope, offer: "the 10 employers swept longest ago, plus a recheck of every listing at To apply".
- `references/board-techniques.md`: how to read each kind of job board, which boards misreport location, and the signs that a posting is gone. Read the section for each board before reading it.

### Steps

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

### Outputs

- New listings at To apply (from stage 02).
- Coverage rows updated for every employer touched.
- Listings set to expired or filled, each with a history entry.
- A report saved to `reports/sweep-<YYYY-MM-DD>.md`: employers checked, new listings, listings expired or filled, manual employers, anything unconfirmed, and calls for the user.

### Done when

- [ ] Every employer in scope has a dated coverage entry, or is listed in the report as not reached.
- [ ] Every manual employer says which kind of failure it was (bot check, browser refusal or structural absence).
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
- **Employer not on the target list** (for example the user pasted a link): ask the user whether to add the employer. If yes, add its `companies` row first, exactly as stage 01 step 1 says (adding employers), then review the posting. If no, give the fit call in chat only and write nothing.
- Take a snapshot before writing, and after writing run `python tools/check_tracker.py check backups/before.json backups/after.json --stage fit` (snapshots: `references/tracker-columns.md`, "Checking by script").

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
- **A matter of taste, not a rule** (for example a commission-only role when the user's rules say nothing about commission): do not add it. List it in the session report for the user, in this shape, so they can decide from it alone:
  1. **Flag:** what made it a close call.
  2. **Posting says:** the exact requirement or fact, quoted short, marked required or preferred.
  3. **You have:** how the user's background compares, from the resume and answer bank only.
  4. **Teaches:** what the role would build.
  5. **Pay and next step:** posted pay or "not posted", and any named next role.
  6. **Lean:** Apply or Skip, with one sentence of reasoning.
  7. **Decide:** the one question the user needs to answer.
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

- **Artifact:** read `listings` and `answers` with `ArtifactData`. Write the listing's `status`, `postingText`, `appliedDate` and `history` with `update`, after reading the row fresh and passing its `version` as `if_version`. Add new accounts to `answers` with `set`.
- **Spreadsheet:** the same tabs and columns in `my-files/job-search-tracker.xlsx`.

### Inputs

- `rules.md` and `my-files/my-rules.md`.
- Listings at To apply, worked in priority order (High, then Medium, then Low), oldest `posted` first within each. Skip `On hold` listings unless the user says go.
- The answer bank: `answers` in the tracker (see `references/answer-bank.md`).
- `my-files/resume.md` for text fields, and `my-files/resume.pdf` to upload. Ask once per session for access to `my-files/` if you do not have it, then upload the resume yourself.
- `references/application-techniques.md`: how each platform's form behaves, how to get answers into fields, upload methods, resume-reader mistakes, the legal text to watch for, and the walls by platform. Read the platform's section before each form.

### Steps

1. **Still live?** Open the posting on the employer's own site. If it is gone, set `expired` or `filled` with a history entry and move on.
2. **Save the posting.** Copy the full posting text into `postingText` now, even if fit review saved it already, and append a history line: `YYYY-MM-DD posting text saved before applying.` The later copy wins, because postings change. Interview prep depends on this.
3. **Re-check the fit.** Read the posting in full before the user does anything on the site, so they never create an account for a job that does not fit. Re-check it against the rules. If it now fails, tell the user and let them decide.
   - **One tab per application.** Open each application in its own new tab; opening another address in a tab with a half-filled form throws the form away.
   - **Apply links that submit on their own.** On some platforms, once the user is signed in, opening another job's apply link submits that application at once from the saved profile, with no form to review (see `references/application-techniques.md`). On such a platform, opening the link **is** submitting: do it only after the user has said yes to that application, as in step 13.
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
12. **Walls** (create account, password, verification code, CAPTCHA, Social Security number or other ID): fill everything up to the wall, then hand the browser to the user. Continue after they are through. Never do the wall step yourself, and never read what they typed. After any click that sends a code, take no more clicks until the user says they are through.
13. **Review before submit.** Show the user a summary of every answer on the form, including the upload (file name and method) and any auto-filled fields you corrected, and stop. Submit only when the user says "submit" for this application, or clicks submit themselves. If a submit fails, read the error messages, fix the fields and submit **once** more; repeated failed submits can trigger a security code or a lockout. Under auto-submit, still post the summary in the chat as you submit.
14. **After submitting:** capture the confirmation (confirmation page text or number). Set `status` to `Applied` and `appliedDate` to today. Append a history entry: date, req id, title, company, location, pay if posted, the application system used, the username if an account was used (never a password), the confirmation, the upload method written exactly as `upload: <method>` (for example `upload: hidden file input`; the check looks for `upload:`), and anything unusual.
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

- **Artifact:** read `listings` with `ArtifactData`. Write only the outreach columns and one history line, with `update`, after reading the row fresh and passing its `version` as `if_version`.
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
- No tracker writes, except one history line saying prep was done, if the user wants it. For that line, take a snapshot before and after and run `python tools/check_tracker.py check backups/before.json backups/after.json --stage prep` (snapshots: `references/tracker-columns.md`, "Checking by script").

### Done when

- [ ] Every fact about the company has a link to one of the allowed sources.
- [ ] Every story is one the user has stated or the resume shows.
- [ ] The file is saved in `reports/` and the user has the path.

---

<!-- stages/06-mailbox-check.md -->

## Stage 06: Mailbox check

Read the user's email for replies from employers and suggest status updates. Run only when the user asks ("check my email", "update the tracker from my email"). It works three ways, best first:

- **An email connector** (for example Gmail or Outlook) connected in Claude.
- **The user's webmail open in the browser**, with the user signed in themselves. Claude never signs in to email.
- **The user pastes or forwards** the emails.

**Read only.** Never reply, send, forward, delete, archive, label, mark as read, or move any email.

**Codes and passwords in email.** Verification codes, sign-in links and temporary passwords often show in message previews. Never copy them into the tracker, a report or the chat.

### Tracker access

- **Artifact:** read `listings` and `companies` with `ArtifactData`. After the user says yes, write `status` and `history` with `update`, after reading the row fresh and passing its `version` as `if_version`.
- **Spreadsheet:** the same tabs and columns in `my-files/job-search-tracker.xlsx`.

### Inputs

- `rules.md` and `my-files/my-rules.md`.
- The user's email, through their connector. The period to check is from the user, or since the last mailbox check in the history, or the last 14 days.
- Listings at Applied, Followed up and Interview. Listings at To apply only to notice a reply about them (see step 4).

### Steps

1. Take a snapshot of the tracker.
2. **Cover a clear window.** Start where the last mailbox check stopped (its history lines and report say "covered <from> to <to>"), and end now. Write the window in this session's report, so the next check starts there and nothing is read twice or missed.
3. **Search every folder, not just the inbox.** Many people have rules that file job email into folders, and some mail apps split the inbox (for example Focused and Other). Search all folders by date range. Date-bounded searches one day at a time are the most reliable on a busy mailbox (for example `received:` searches in Outlook, `after:` and `before:` in Gmail).
4. Within the window, look for each employer that has a listing at Applied or later, by company name and by the application system's sender (messages often come from the platform, not the employer).
5. **Webmail in the browser:** message lists load as you scroll ("virtualized"), so collect rows by scrolling the list by script until no new rows appear, then open each relevant message by a snippet of its preview text. If the list stops loading new rows, the browser window may be covered or hidden: ask the user to bring it to the front.
6. Match each message to one listing: same company and, where the message names it, the same title or req id. If a message could match more than one listing, do not guess. Ask the user.
7. Sort each match:
   - **Confirmation** of an application ("we received your application"): no status change. Offer a history line.
   - **Interview request or scheduling:** propose `Interview`, with the date, time, format and names in the history line.
   - **Rejection,** including "we filled the position with another candidate": propose `Rejected`.
   - **The role was cancelled or is "no longer available"** (not a rejection of the user): propose `expired`.
   - **Offer:** propose `Offer`.
   - **A follow-up the user sent** (found in their sent mail, to an employer with a listing at Applied): propose `Followed up`.
   - **Assessment or next step that is not an interview** (online test, video interview, game-based assessment): no status change. Offer a history line, and put any **deadline** at the top of the report. Assessments are the user's to take.
   - **Scheduling back-and-forth** (a recruiter offering times): replies are the user's to send. List it with any deadline.
   - **Confirmations of applications:** no status change. Ask once whether the user wants these logged; many people do not.
   - **Invitations from employers not on the target list** (for example a job site's "apply to this job" message): never act on them. List them for the user's call.
   - **A reply about a listing still at To apply** (for example the user applied outside a session): no status change from this stage. Tell the user, and offer a history line. The user can then set the status directly (`python tools/check_tracker.py check backups/before.json backups/after.json --stage user`).
8. **Show the user every proposed change in one list** before writing anything, for example: "Example Health Co, Clinical Account Executive: Applied to Interview. Email from 2026-03-14 asks for a call on 3/18 at 10am with the regional manager." Wait for the user to say yes, no, or change it for each one.
9. Write only what the user approved: `status` (if changed) and one history line per listing, ending "from email dated YYYY-MM-DD, approved by the user".
10. Never change a listing based on an email the user did not approve. Never set Applied from an email. Applied comes only from stage 03 or the user.
11. Take an after snapshot and run `python tools/check_tracker.py check backups/before.json backups/after.json --stage mailbox` (snapshots: `references/tracker-columns.md`, "Checking by script").

### Outputs

- Approved status changes and history lines.
- A report saved to `reports/mailbox-<YYYY-MM-DD>.md`: the window covered (from and to), deadlines first, what was found, what changed, what was left alone, and anything that needs the user (interviews to confirm, assessments to take, replies to send).

### Done when

- [ ] No email was sent, replied to, deleted, moved, labeled or marked as read.
- [ ] Every status change was approved by the user in this session.
- [ ] `yourNotes` untouched (`check_tracker.py`).
- [ ] The window covered is written in the report, and no code, sign-in link or password was copied anywhere.
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
2. For each job, newest first (after all jobs: work out the years of experience from the dates, compare with what the user says, and if they differ ask which number to use and what it counts; write it on the "Years of experience" line):
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

1. **Pick the target.** Take the main target role and level from `my-rules.md`. If the user has two quite different targets, ask which one this resume is for. One resume per target. A resume for a second target goes to `my-files/resumes/resume-<target>.md` and `.pdf` (for example `resume-quality-inspector.md`), never over `my-files/resume.md`.
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
   - `python tools/check_resume.py my-files/resume.md --facts my-files/resume-facts.md --pdf my-files/resume.pdf --years <years from the facts file>` (run it again after step 5 builds the PDF; `--years` sets the page limit)
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
4. Write the tailored text to `my-files/resumes/resume-<listing id>.md`, run the same checks on it, then build `my-files/resumes/resume-<listing id>.pdf`. Never overwrite `my-files/resume.md`.
5. After the user approves it, take a snapshot, add a history line to the listing: `YYYY-MM-DD tailored resume approved: resume-<listing id>.pdf`, then run `python tools/check_tracker.py check backups/before.json backups/after.json --stage resume`. Stage 03 uploads that file for that listing instead of `resume.pdf`.

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
- [ ] `check_resume.py` passes: no dashes, no pronouns, no personal data that does not belong on a resume, bullets a sensible length, standard headings.
- [ ] The page count is within the limit.
- [ ] The user approved the final PDF.
- [ ] Any earlier `resume.pdf` was backed up first.

---

<!-- stages/08-company-research.md -->

## Stage 08: Company research

Research sessions the user starts by asking. Four kinds:

| Kind | The user says something like | Writes to the tracker |
|---|---|---|
| A. Find employers | "Suggest employers that fit my background" | New `companies` rows, after the user approves each one |
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

1. **Start from the rules.** Read the user's target roles, industries "in", place rules and excluded industries. Say in one line what you will look for, for example: "Health tech employers with offices in [your city], or remote roles open to people in [your state]."
2. **Search in this order**, and note which source each name came from (it goes in the report's "Came from" column):
   1. **Local lists:** largest employers, fastest growing, best places to work, published by local business journals, newspapers, chambers of commerce and the regional economic development partnership for the user's metro.
   2. **Industry association member lists** for each industry the user wants (for example a state insurance institute, a state technology association, a bankers' association). These are often the richest single source.
   3. **The software and service vendors that sell into the user's industries.** For each industry "in", ask who sells software or services to it (insurance software, HR and payroll technology, health technology, government technology, banking technology). Vendors in a field often hire people from that field.
   4. **Employers that hire the user's kind of role in the user's metro:** search for the role type plus the metro (for example "inside sales desk", "field sales", "account manager", "implementation", "underwriting" with the city name), then confirm each employer's own board.
   5. **Neighbors of good fits:** competitors, partners and customers of employers already on the target list (from their own sites and press releases).
   6. **Remote-friendly employers:** companies in the user's industries whose own careers pages show remote roles open to the user's state.
   7. **Job search engines and job alert emails, read by hand, only to learn company names** that post the user's target titles nearby. Then confirm each on its own board. Never treat them as proof that a job exists.
   8. **Earlier rejects, when the rules change.** If the user widens their rules, look again at the "checked and not added" list from earlier research reports.

3. **Check every candidate** before showing it:
   - Its own careers site exists and opens. Record the link. A redirect to the company's own careers subdomain, or to the job board the company itself links to (Workday, Greenhouse, Lever, Ashby and the like), counts as its own site. If the careers link you tried does not open, find the real one from the company's own home page; never guess, and leave the employer out until you have it.
   - Its industry, in the words of `settings.industryOrder` where it fits.
   - It has a presence the user's place rules allow: an office in the home metro, a territory covering it, or remote roles open to the user's state. Say which, with a link.
   - It is not already on the target list (exact name), not excluded, not the current employer, not on the never-contact list.
   - It plausibly hires the user's target role. Say why in one line.
4. **Know when to stop.** Agree a target with the user first (for example 30 new employers). Track the **yield**: of your last 20 searches or checks, how many produced a new employer that passed step 3. Stop when you reach the target, when yield drops below 2 in 20 (the sources are used up), or at the session budget (about 150 tool calls). Say which one stopped you.
5. **Show the candidates in one table**: company, industry, proposed tier (using the user's tier meanings from `settings`), careers site, why it fits, source. Ask the user to approve, drop or change each one.
6. **Write only the approved ones** to `companies`: `id` (lowercase name with hyphens), `company`, `careersSite`, `tier`, `industry`, `keepAnyway` no, `onHold` (yes only if the user's rules put it on hold), `added` today.
7. Snapshot before and after (see `references/tracker-columns.md`, "Checking by script"), and run `python tools/check_tracker.py check backups/before.json backups/after.json --stage research`.
8. Offer a sweep of the new employers. Do not start one unless the user says yes.

**The research report (part A)** has four lists, so the next session can pick up where this one stopped:

- **Added:** each new employer with its industry, tier, careers site and where the name came from.
- **Borderline, your call:** employers that fit on paper but have a doubt (for example jobs only in a nearby city, or one role that fits among many that do not). One line each on the doubt.
- **Checked and not added:** each with a one-line reason (no board of its own, no roles of the user's kind, excluded industry). This stops the next session from checking them again.
- **Leads for next time:** sources not yet worked, and names found but not yet checked.

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
| `family` | The kind of role, one of `settings.roleFamilies`, written without the `*` (the `*` only marks targets in settings). | Claude |
| `posted` | Date posted, as shown. | Claude |
| `pay` | Posted pay exactly as written, or "not posted". | Claude |
| `why` | One or two sentences on why it fits, and any reach. | Claude |
| `teaches` | What the role would teach you. Starts with "Stated:", "Not stated." or "Not read." | Claude |
| `priority` | `High`, `Medium`, `Low` or `On hold`. Work order for applying. | Both |
| `status` | Where it stands. See the list below. | Both, under the rules |
| `appliedDate` | Date the application went in, `YYYY-MM-DD`. | Claude |
| `postingText` | The full text of the posting, saved so it survives after the posting comes down. | Claude |
| `reviewReason` | Why a listing at Review fit needs your call. | Claude |
| `history` | Dated log of everything sessions did. **Add only, never change or delete.** Entries are separated by ` \| `, and each starts with a `YYYY-MM-DD` date. An entry never contains the `\|` character itself (write `/` instead). | Claude (append only) |
| `yourNotes` | Your own notes. **Claude never writes this.** | You |
| `managerName`, `managerTitle`, `howIdentified`, `confidence`, `profileUrl`, `emailOrFormat`, `connectionNote`, `longMessage` | Outreach research and drafts (stage 04). Drafts only. You send. | Claude |

**Status values:** `To apply`, `Applied`, `Followed up`, `Interview`, `Offer`, `Review fit` (set only by you, for a listing you want to think over; fit review never creates listings at this status), `On hold`, `Rejected` (the employer said no), `Closed` (you passed), `expired` (the posting came down), `filled` (the employer says it is filled).

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
| `industryOrder` | Industries you want, most wanted first. The tracker groups listings in this order. | `Logistics software; Manufacturing; Public utilities` |
| `excludedIndustries` | Industries hidden from the main views and skipped in sweeps. | `Staffing; Retail` |
| `roleFamilies` | Kinds of role. A `*` after a name marks a target family. | `Quality inspector*; Operations analyst*; Shift supervisor` |
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

**Artifact:** list each of the 5 collections (`companies`, `coverage`, `listings`, `answers`, `settings`) with `ArtifactData` (`list`, with `out_dir` set to `backups/before-db`). That saves one file per row. Then combine them:

```
python tools/check_tracker.py snapshot-dir backups/before-db backups/before.json
  (the session runs)
  (list the 5 collections again with out_dir backups/after-db)
python tools/check_tracker.py snapshot-dir backups/after-db backups/after.json
python tools/check_tracker.py check backups/before.json backups/after.json --stage sweep
```

The same `before.json` also serves as the backup rules.md section 7 asks for. Use a fresh `after-db` folder each time, so rows deleted during a session do not linger from an earlier run.

The `--stage` choices are `intake`, `sweep`, `fit`, `apply`, `outreach`, `prep`, `mailbox`, `resume`, `research` and `user` (a change the user asked for directly).

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

<!-- references/board-techniques.md -->

## Board techniques: how to read job boards

How to find and read postings on employers' own job boards, platform by platform. Learned over a few hundred real employer boards. Used by stage 01 (sweeps and rechecks) and stage 08 (company research). The application form itself is in `application-techniques.md`.

Add what a session learns here (with the user's OK): a new platform, a new workaround, a trick that stopped working. Edit the platform's section in place. Never add employer names, the user's details or dates.

### Ground rules

- **Read the employer's own board, never signed in.** Most employer job boards run on an applicant tracking system (ATS) such as Workday, Greenhouse or iCIMS. The employer's careers page links to it.
- **Respect the site.** Read at a human pace. Never bulk-download a site's pages; boards that see many fast requests answer with "too many requests" (HTTP 429), and that is a sign to stop. Never get past a bot check (Cloudflare "Just a moment...", "Verifying you are human", a security checkpoint, a CAPTCHA). Mark the employer **manual** and move on.
- **Record why a board could not be read.** These are different and need different fixes:
  - **Bot check:** the site shows a challenge. A person can usually open it in their own browser.
  - **Browser refusal:** the browser tool refuses to open the site at all. A person's own browser usually works.
  - **Structural absence:** the employer has no postings of its own (it posts only through an aggregator or a staffing firm).
- **Many boards have a public data feed** that the page itself uses. Reading it is faster and more complete than reading the page. Find it with `read_network_requests` while the page loads, or with `performance.getEntriesByType('resource')` in the page when the network list shows nothing. Spend two tries on that before falling back to reading the page text.
- **Some feeds only answer from the board's own page** ("same origin"). Open the board in the tab first, then fetch from that tab. Others answer from any tab.
- **Scripts in the page can time out** after about 45 seconds when they loop over many requests. Keep partial results on `window` and split the work over several calls.
- **Keep tool results small.** A full board can be a very large result. Ask for only the fields you need, and page through.

### Boards that misreport location

Several boards ignore their own location filter, or tag a job "Remote" when it is only remote within some states or near some offices. **Always read each posting's own location text**, not the filter you sent or the headline tag.

- A location search that returns the whole global board is common (several hosted career-site platforms, some front ends built on SmartRecruiters, some iCIMS boards that ignore the country parameter).
- "Remote" often means "remote within these states" or "remote within about 70 miles of an office". The body text or a list of extra locations says which.
- A state-specific remote tag (for example "XX-REMOTE") can mean that state only, or can mean "remote, based anywhere in the country". Read the posting.
- Some city filters match only the posting's **primary** city. Check the full list of locations.
- A job-board tag such as "USA" does not mean remote. Look for "Location: Any" or similar in the body.

### Workday

The most common platform. Board addresses look like `<tenant>.wd<N>.myworkdayjobs.com/<site>` (some use `wd<N>.myworkdaysite.com/recruiting/<tenant>/<site>`).

- **List:** POST `/wday/cxs/<tenant>/<site>/jobs` with `{"appliedFacets":{},"limit":20,"offset":0,"searchText":""}`. It pages 20 at a time. On some boards `total` is returned only on the first page, so do not stop a loop when a later page reports 0.
- **Detail:** GET `/wday/cxs/<tenant>/<site>/job/<externalPath>`. Get `externalPath` from a search by job number. It already starts with `/job/`, so do not add `/job` again. Job paths can change when a title changes, so a 404 on a saved path is not proof the job is gone: search the job number first.
- **Same origin only.** The tab must be on that tenant's board.
- **Filter by location facets, not text.** POST with empty facets first, read the `facets` in the answer, then filter with the facet's own parameter name (often `locations`, sometimes a state or region facet, or `remoteType`). A text search for a state name also returns jobs that merely mention it.
  - A truly nationwide remote job usually carries every state's remote facet, so your state's remote facet catches it.
  - Some boards show only the top 50 or so facet values, so a small state may not appear; filter through the site's own search page instead. Some show no state facet until a country facet is applied first.
  - `searchText` is loose matching on some boards and cannot prove something does not exist.
- **Read `additionalLocations` on every job.** The list view does not show it, and real remote eligibility often lives there.
- **Liveness check without opening the form:** the detail endpoint returns `canApply`, `postedOn` and `endDate`. A 403 "permission denied" on the job endpoint, plus no match when searching the board for the job number, means the job is gone.
- If a job page shows only bare tags, inserting `/en-US/` after the host (`<host>/en-US/<site>/job/...`) often renders the full description.
- Some boards run a career site from another platform (Phenom and others) in front of Workday. The Workday feed underneath often works better.

### Phenom

- A plain fetch returns an empty shell. Use the rendered search page (`/global/en/search-results?keywords=<q>`) and its facet pages.
- **Feed:** POST `<careers host>/widgets` with `ddoKey` `"refineSearch"` (list) or `"jobDetail"` (detail); the payload needs the site's `refNum`. Results come back as an array of `{field, value}` items, not a keyed map.
- State filters differ by board: some want the two-letter code, some the full state name. Some state filters are simply broken; then filter on each row's own city and state.
- When `/widgets` returns 0 for everything, open a search URL and read `window.phApp.ddo.eagerLoadRefineSearch` from the page. Some boards cap that at the first 10 rows; then the board is manual for anything beyond a keyword search.
- On a job page, `document.body.innerText` may show only a chat widget. Read `phApp.ddo.jobDetail.data.job` instead.

### Greenhouse

- `boards-api.greenhouse.io/v1/boards/<token>/jobs?content=true` returns every posting with full text. Load `boards-api.greenhouse.io` in the tab first, then fetch.
- Find the token in the careers page's embed script: `boards.greenhouse.io/embed/job_board/js?for=<token>`. Tokens are often not the company's obvious name.
- The same job number can be shared by copies of a job in several locations; log the job's own id.
- A `job-boards.greenhouse.io` job link that redirects to the employer's general careers page means the job is closed.
- Some boards turn over fast: a job can vanish between two reads minutes apart. Confirm twice before marking it gone.

### Ashby

`api.ashbyhq.com/posting-api/job-board/<slug>?includeCompensation=true` returns the whole board with plain-text descriptions, `isListed` and `publishedAt`. Fetch it from a tab on `api.ashbyhq.com`.

### Lever

`api.lever.co/v0/postings/<company>?mode=json` and `/<id>`. Includes `createdAt`, `salaryRange` and all locations. Load `api.lever.co` in the tab first.

### Workable

`apply.workable.com/api/v1/widget/accounts/<company>` lists jobs with their short codes.

### SmartRecruiters

`api.smartrecruiters.com/v1/companies/<id>/postings` and `/postings/<id>`. Employer front ends built on it may silently ignore their own location and keyword filters, so a filtered result of 0 means nothing there: page the whole board and filter the rows yourself.

### iCIMS

- Fetches fail unless the tab is already on that iCIMS host.
- Open `/jobs/<id>/job?in_iframe=1` and read the frame's `contentDocument`. Some pages set a base address, so use full same-origin addresses.
- The JSON-LD block's `datePosted` gives the posted date.
- Full lists often page with `pr=0..N` (20 per page). When the list sits inside a frame, fetch the frame address with `&in_iframe=1` and page it.
- Some boards ignore the country filter and return the global board: read each row's location.

### Jibe (a front end on iCIMS)

- GET `/api/jobs?page=N&limit=100`. The list already includes descriptions and qualifications, so one call can cover a board. Keep the page size modest: the result can be very large.
- `/api/jobs/<id>` returns HTML, so pull one job with `?keywords=<job number>&limit=5` instead.
- Work type can hide in a tag field. A location search may also return every nationwide posting, and on some boards the location sorts by distance instead of filtering.

### ADP Workforce Now

- The careers page embeds `<recruitment-current-openings cid="...">`.
- The public feed works even when the page never draws its list: `workforcenow.adp.com/mascsr/default/careercenter/public/events/staffing/v1/job-requisitions?cid=<cid>&lang=en_US&locale=en_US&$top=100`. **Each page holds at most 20 rows whatever `$top` says**, so page with `$skip`.
- `/job-requisitions/<itemID>?cid=<cid>` returns the description and pay range.
- When the board sits in a blank frame, find the cid in the careers page's HTML and call the feed directly.
- Try this before marking an ADP-hosted employer manual.

### ADP Career Center (myjobs.adp.com)

- `myjobs.adp.com/public/staffing/v1/career-site/<site name>` returns the site record (`orgoid`, the site `id`, and `settings.externalId`).
- The filter endpoint needs three lowercase headers sent together: `orgoid`, `postingchannelid` (the externalId) and `careersiteid` (the id). With all three it returns the board in one call.
- `job-requisitions?$top=N&$search=<term>` with an `orgoid` header also works; `$search` is the reliable filter because `$skip` stops working past several hundred rows.
- On job pages, `document.body.innerText` often returns only the footer. Read with `read_page` or `find`. A gone job shows a generic "Problem with the service" message: confirm with the board's own search.

### UKG Pro / UltiPro (recruiting.ultipro.com)

- POST `<board path>/JobBoardView/LoadSearchResults` with the search body the page uses.
- Detail: GET `<board path>/OpportunityDetail?opportunityId=<id>`. The HTML embeds `CandidateOpportunityDetail({...});` with description, posted date, locations, travel and pay range. Find the opening brace after the marker and match braces to the end, rather than relying on the closing parenthesis.
- A bare board address can 404 while the board's GUID address works. Take the GUID from the employer's careers-page link.
- A "System is initializing" page on first load is not a bot check: wait about 6 seconds and reload.

### UKG Ready (saashr.com)

Single-page boards with **no link per job**, so log postings by title. Take the tenant number (and any `ein_id`) from the employer's careers-page link. Some tenants expose a public feed at `/ta/rest/ui/recruitment/companies/%7C<tenant>/job-requisitions` and `/<id>` with full text.

### Dayforce

- GET `/api/auth/csrf`, then POST `/api/geo/<namespace>/jobposting/search` with header `x-csrf-token` and a body with `clientNamespace`, `cultureCode`, `jobBoardCode` (often `CANDIDATEPORTAL`), `searchText`, `paginationStart`. `searchText` matches the job number. The answer carries full descriptions, locations and posted time.
- On some boards the feed refuses scripted calls; the rendered page prints every description in full, so read that.

### Eightfold

- `/api/pcsx/search?domain=<domain>&query=...` returns positions. **`num` is silently capped at 10 on some boards** while `count` reports the real total: page with `start=`.
- Details: open `/careers/job/<id>?domain=<domain>` and wait about 2 seconds for it to fill in.
- On some boards a location search returns the nationwide remote board instead of local jobs; read each job's own location.

### Cornerstone (csod.com)

The careers site's own search calls `us.api.csod.com/rec-job-search/external/jobs`. Detail pages read fine as page text.

### Paycom

Next-page arrows can do nothing. Use the page's keyword box: set its value with the native input setter, dispatch an `input` event, then press Enter. A few broad words ("Sales", "Manager", "Associate") surface most titles. Reload between searches if the box stops taking a second query.

### Paylocity

- Board pages expose `window.pageData` with every job and its location.
- Detail at `/recruiting/jobs/Details/<id>`, which carries a JobPosting JSON-LD block. If that says "Job Not Found", the `/recruiting/jobs/Apply/<id>` address may work, and the tab must actually open it.
- No posted date and no pay range are exposed: that is the board's limit, not a gap in the read.
- A remote flag can be set on city jobs; prefer a location that says "Remote".

### Avature

- Location parameters in the address are often ignored.
- Some boards answer `GET /Search/SearchResults?keywords=&location=&jtStartIndex=N&jtPageSize=500` with header `X-Requested-With: XMLHttpRequest`. Values come wrapped in tags: strip them.
- Multi-state jobs can run state codes together in one string; look for your state's code as a separate token, and beware partial matches inside other words.
- Where that does not exist, type in the page's own location box and watch `read_network_requests` for the lookup it makes; reuse the ids it returns in the search address.

### Oracle Recruiting Cloud

- The site's REST feed: `recruitingCEJobRequisitions` with `finder=findReqs;siteNumber=<site>` for the list, and `recruitingCEJobRequisitionDetails` with `finder=ById;Id=<id>,siteNumber=<site>` for detail. The parameter is `Id`, not `jobId`. Find the host and site number with `performance.getEntriesByType('resource')` if the careers page hides them.
- When the feed is dead, click "Show more results" repeatedly on the rendered page and read the list.

### SuccessFactors

- Read the rendered career-site search, with job ids in the addresses.
- On some boards the tile search returns an empty 16-byte page for every query: that is not "no jobs". Try a `facetFilters` search on the site's own domain.
- On some boards the location search is broken while keyword search works.
- A keyword search for a job number may fall back to loose matching: check the exact job number is in the results before calling a job live.
- Some boards tag every job with the same work-type boilerplate; trust the body.
- Some careers hosts do not load in an automated browser while an alternate host for the same board does. Look for it on the employer's careers page.

### Other platforms

- **Radancy / TalentBrew:** `/search-jobs/results` with `RecordsPerPage=100` returns postings and facets. The location filter often returns the global board: use keywords and read each row's city. A keyword search on a bare job number returns exactly that job.
- **LiquidCompass:** the search feed ignores keyword and size parameters except `page_size`; pull the board whole and filter.
- **NLX / jobsyn:** the list caps at 10 rows; use `/sitemap.xml` and the jobs sitemap, where each job address starts with its city.
- **Hirebridge:** `recruit.hirebridge.com/v3/Jobs/list.aspx?cid=<cid>` and `JobDetails.aspx?cid=<cid>&jid=<id>`. Read the `<article>` element, not the whole page text.
- **Jobvite:** `jobs.jobvite.com/<slug>/jobs`. Parse job links from `/search?p=N`; some list classes do not survive a plain fetch.
- **Largely and other script-only boards:** click "Load more" until every card shows, then read the cards.
- **TTC Portals, Frontline and similar small boards:** read the rendered list, then each posting.
- **BambooHR:** `/careers/list` and `/careers/<id>/detail` return JSON. `locationType` "1" means remote.
- **HRMDirect:** skip the frame and open the job-openings list page directly; a plain fetch of a job page works from the board's own origin.
- **isolved Hire:** a fetch returns a shell; open each posting.
- **HiBob:** `<company>.careers.hibob.com`, read through `/api/job-ad`.
- **WordPress job boards:** `/wp-json/wp/v2/jobs` lists postings; each job page's HTML carries the location.
- **Sitemaps:** when a board's filters do nothing, `/sitemap.xml` often lists every job address.
- **Static careers pages and PDFs:** small; read them. A careers address that 404s may have moved: find the link on the employer's home page.

### Signs a posting is gone

Only the employer's own site decides. These are reliable signs, and stage 01 lists what to do with them:

- The page says "no longer available", "this job has been filled", or similar.
- HTTP 410 Gone (confirm once on a retry).
- On Workday: a 403 on the job endpoint plus no match when searching the board for the job number.
- On Greenhouse: the job link redirects to the employer's general careers page.
- The job number is missing from a search of the employer's whole board, and the posting page will not load.

These are **not** proof, and need a second look:

- A 404 on a saved address (job paths change with titles; search the job number).
- An aggregator showing the job as closed.
- The employer rejecting the user (the posting can stay live).
- One of two pages for the same job showing it closed while the other shows it open: trust the page with an explicit closed or filled message, and say so in history.
- A slow first load or an "initializing" page.

### Working with helpers (subagents)

- About **6 employers per helper**, and a cap of about 50 tool calls each. A board with more than about 200 jobs goes alone or with very small boards. Helpers given 11 or more employers silently dropped some.
- Each helper loads its browser tools once, **opens its own tab** (never a shared one), and closes only its own tab.
- Each helper writes its final findings to a file as well as returning them (a hand-back can be lost), and returns at most about 20 KB.
- Every finding carries: job number, title, location as written, the employer's own job address, the board's work-type tag, pay if posted, and the **quoted requirement lines**. If the requirements could not be read, the helper says so.
- Give helpers only confirmed board addresses, or have them find the board from the careers page first.
- Helpers only read: no tracker writes, no applications, no sign-ins, no bot-check workarounds.
- The main session re-checks every finding against the rules, opens at least one posting per helper on the employer's own site, and does every write.

---

<!-- references/application-techniques.md -->

## Application techniques

How application forms behave, platform by platform, and how to fill them correctly. Learned from well over a hundred real applications. Read it before an apply session (stage 03). Reading job boards is in `board-techniques.md`.

Add what a session learns here (with the user's OK): a new platform, a new workaround, a trick that stopped working. Edit the platform's section in place. Never add employer names, the user's details or dates.

### Before you start

- **Read every posting in full before the user creates any account.** Many promising titles turn out, once read, to be senior or out-of-scope roles. Creating accounts for those wastes the user's time.
- **Walls are the user's** (rules 9): accounts, passwords, one-time codes, CAPTCHAs, ID numbers. Fill everything up to the wall, hand the browser over, continue after. **Never read a password field**, and leave password inputs out of every dump of a form's fields.
- **Questions that are always the user's:** assessments and aptitude tests, criminal history and felony questions, whether they would sign a non-solicitation or confidentiality agreement, and any judgement call about their own experience ("years of comparable experience", "describe how you use AI"). Fill everything else, bring the tab forward, and let the user answer. Do not read back or log their answer.
- **One tab per application.** Opening a new address in a tab that holds a half-filled form throws the form away. Open each application in its own new tab, and bring it forward when the user has to act in it.
- **Some saved profiles submit instantly.** On some platforms, once the user is signed in, simply opening another job's apply link submits that application from the saved profile, with no form and no review. Treat opening an apply link on such a platform as submitting: do it only after the user has said yes to that specific application (stage 03, "Review before submit"). Known pattern: some iCIMS boards after sign-in.
- **Do not repeat a failing submit.** Read the error messages, fix the fields, and submit once. Repeated failed submits can trigger an emailed security code or a lockout.
- **Do not click near a code box while the user is typing a code.** After any click that sends a code, stop and hand over; take no more clicks until the user says they are through.

### Getting text into fields

Modern forms ignore some ways of setting a value. In rough order of what to try:

1. **The native value setter plus events.** Set the value with the input's native setter, then dispatch `input` and `change` (and `blur` or `keyup` on some forms). Works on plain forms, AngularJS, many React forms.
2. **Text insertion.** `el.focus(); el.select(); document.execCommand('insertText', false, value)`, then `change` and blur. Works on many React and Ant Design forms where the setter shows the text but the form does not register it. To clear a field: `select()` then `execCommand('delete')`.
3. **Real typing** with the browser tool's type action. Needed for: phone numbers on several platforms, street address line 1, some textareas, some salary boxes, fields whose validation rejects script-set values.

Other rules:

- **A script-set value must change to count.** Setting a dropdown to the value it already shows fires nothing. If a dependent dropdown stays empty, set the parent to another option and back.
- **Read the page a second or two after a click.** Many forms advance late; reading immediately shows the old step, and clicking Next again skips a step. Click Next once per call, wait, and confirm which step is showing before filling.
- **Check which page is showing before a fill script runs.** A script meant for page 2 can overwrite page 1's fields if the Next click silently failed.
- **Screenshots can lag one render.** Before a coordinate click, confirm the state by script or a fresh screenshot.
- **Coordinates:** if screenshots are scaled, multiply page coordinates from `getBoundingClientRect()` by the screenshot width over `innerWidth` before clicking. If the page will not scroll by script, use the browser tool's scroll action and a fresh screenshot.
- **Narrow windows:** if `innerWidth` is very small and the page is unreadable, resize the browser window to a desktop size (for example 1200 x 900), work, then set it back.

### Dropdowns, radios, checkboxes and dates

- **Native `<select>`:** setter plus `change` (plus jQuery `.trigger('change')` where the page uses jQuery).
- **Custom dropdowns (react-select, react-widgets, Ant Design, comboboxes):** one real click on the control, wait about a second for the list to draw, then click the option whose text matches, by script or by its reference. Never click a blind offset: the list may open upward or in a different order than it looks.
- **Searchable lists (school, field of study, city):** after the click, type the text for real, wait 1 to 2 seconds, then click the matching option.
- **Radios and Yes/No buttons:** a script click works on some forms; others need a real click. The first click right after typing can be swallowed: re-read the state and click again if needed.
- **Checkboxes, especially acknowledgements:** usually need a real click. A dispatched change can toggle them back off.
- **Web components (shadow DOM):** click the input inside: `el.shadowRoot.querySelector('input')`.
- **Date fields** vary the most:
  - Native `type=date` inputs: the setter with `YYYY-MM-DD` sometimes works; when the form does not register it, click the field and type the digits.
  - Masked text dates: type the digits (`MMDDYYYY`).
  - Segmented dates (month, day, year boxes): set each segment with the native setter plus an `InputEvent` of type `insertText` and a `change`.
  - Calendar pickers: open the picker and click the day cell. For "today's date" fields, the picker's "today" cell is the most reliable.
- **Address autocompletes:** type the street, then click the suggestion; it fills city, state, ZIP and county. Picking the address can wipe other fields on the same page (such as a start date), so set those after. If the autocomplete fails to load, fill the fields by hand.
- **Phone with a country code:** set the country (or dial code) first, then type the number; typing the number into a box that already holds a prefix can double it.

### Resume upload and resume parsing

Upload methods, in the order stage 03 tries them:

- **Plain file input.** Use the file upload tool on it directly. Never click it: clicking opens the computer's own file picker, which the browser tools cannot see.
- **Button over a hidden input.** The real `input[type=file]` is usually hidden next to the button. Find it with `read_page` (it often shows as a button with type "file"), `find` ("file input for resume"), or a read-only check listing every `input[type=file]` with its id and `accept` value. Upload to that input.
- **Drag-and-drop zone.** There is almost always a hidden file input inside the zone. Upload to it.
- **"Autofill from resume" button.** Find the hidden input behind it and upload there, then check every field it filled.
- **Paste box.** Use the text of `my-files/resume.md` and flag it in the review summary.
- **Built-in browser pane.** It has no file upload tool. Switch the application to Claude in Chrome.
- **When the upload tool is refused** ("not a file input") on a control that is a file input inside a custom widget, a page script can attach the file: build a `File` from the PDF's bytes, put it in a `DataTransfer`, assign it to `input.files`, and dispatch `change`. On a few React dropzones, the change only registers through the input's own React handler.

How to tell an upload worked:

- The page shows the chosen file name (or a preview of the resume) next to the control. A different name, a size of 0, or an error means it failed.
- Some forms read the file only on the next page. Check again after moving on.

**Upload order:**

- On forms that **do not** read the resume, upload **last**: some scripted field changes on those forms wipe an attached file. Check the file name is still there before submitting.
- On forms that **do** read it and fill fields, upload **first**, wait for the reading to finish, then correct the fields.

**Resume readers get things wrong.** After any automatic fill, check every work-history entry against `my-files/resume.md`. Common mistakes:

- employer and job title swapped, or the employer jammed into the title, or the city put in the description;
- dates garbled, or an end date set on the current job;
- bullet points dropped, or the degree set to "Other";
- the phone number copied into the extension field;
- the whole contact line put in the city field;
- parsed rows arriving late and overwriting or duplicating what you typed (wait for the reading to finish first);
- "suggested" skills added that are not on the resume (remove them);
- a re-upload wiping fields such as street address or school.

### Answers forms ask for

Fill from the answer bank. These come up often; the intake collects them (stage 00, step 5):

- **"How did you hear about us":** the employer's own career site ("Company website", "Corporate website", "Careers site"). If there is no such option, use the closest true one and tell the user.
- **Pay:** some boxes take text (use the answer bank's wording), some take digits only (use the single number), some are a range list (pick the band holding the number), some pair a number with a currency picker, some ask hourly or salary first.
- **Start date, relocation, travel, overtime and shifts, work authorization and sponsorship, age 18 or over.**
- **Employer relationships:** previously worked here, relatives working here, current employer is a client or partner, currently bound by a non-compete or other restrictive agreement.
- **References and contact permission:** some forms make supervisor name, title, phone and email required for every past job marked "may we contact". Some ask "ever been fired or asked to resign" or "may we contact past employers".
- **Reason for leaving** each past job.
- **Licenses:** held, and ever denied, revoked or suspended. **Registrations** in regulated fields.
- **Years in specific kinds of work** (customer service, sales, a named tool), and occasionally things like a typical sales cycle.
- **Voluntary self-identification:** gender, Hispanic or Latino, race, veteran status (note the difference between "not a veteran" and "a veteran but not a protected veteran"; pick the one that is true), disability. Option text varies a lot: match by meaning, and read back the chosen value.
- **Optional:** pronouns, SMS consent, phone type, preferred name, middle name, county.
- **LinkedIn:** enter only when required (stage 03). Some forms validate that it is a real LinkedIn profile address.

### Legal text: read it to the user first

Stop and quote it to the user before anyone ticks the box or types a signature (stage 03 step 11). Seen on real forms:

- arbitration agreements, jury or class-action waivers, invention assignment, pay withholding;
- consent to biometric collection (photos, video, facial geometry, fingerprints);
- consent to AI transcription or AI scoring of interviews;
- broad authorization to contact **any** past or current employer, or every business listed on the application. If the user's current employer is listed, point that out: it conflicts with "never contact your current employer".
- background, credit or criminal check releases.

Plain accuracy statements ("the information is true") are routine, but still mention them in the review summary.

### Platform notes

#### Greenhouse

- Usually no account and no CAPTCHA. Form address: `job-boards.greenhouse.io/embed/job_app?for=<board>&token=<job id>`. It works even when the company wraps the board in its own site.
- Read the posting from `boards-api.greenhouse.io/v1/boards/<board>/jobs/<id>` (open it in the tab; a fetch from the form page is blocked).
- Text inputs take the setter; **textareas need real typing**.
- **Phone with a required country:** first click the Country control, type the country, click the option, then type the phone.
- react-select dropdowns: one real click on the control, wait about half a second, then click the `.select__option` with matching text. Read the result from `.select__single-value`. Do not call React internals: that can wipe the attached resume.
- Attach the resume last and check it is still showing before Submit.

#### Lever

No account. Upload the resume first; it fills name, email, phone and current employer. An invisible CAPTCHA usually does not challenge; a visible one is a wall.

#### Ashby

No account. The phone must be typed for real. Yes/No buttons and radios need real clicks; check each took. Location and source are comboboxes: click, type, click the option. Usually ends with an agreement radio: read it.

#### Workday

- **One account per employer** on most boards (the user creates it). Some boards allow applying as a guest.
- Start at `<job address>/apply/autofillWithResume`. After the resume is read, fix every work-history entry.
- Dropdowns are buttons that open a list: click the button, wait about a second, click the `[role=option]` with matching text. Pick questionnaire buttons with `button[id^=primaryQuestionnaire]`, not by position: the page header has a button that matches a looser selector and shifts every answer by one. Read each question beside its answer before continuing.
- Option lists can pile up after several opens; pick text that is unique, one field per call, and press Escape between.
- "How did you hear" is either a plain list or a multi-level prompt: click it, type the option text, press Return, and check the selected item appears.
- Address line 1 and some name fields must be typed for real. Questionnaire textareas (salary, "why this role") must be typed for real.
- The disability self-identification date ("CC-305"): open the calendar and click today's cell.
- **"Use My Last Application"** (`<job address>/apply/useMyLastApplication`) on a second job at the same employer carries the work history forward; the source and questionnaire still need answering.
- Some Next buttons ignore a script click: use a real click at the button's position and confirm the step number after.
- **Never press Discard** on the "Discard application?" dialog; choose Continue. If a field is corrupted, reload the apply address: drafts keep earlier steps.
- Pop-up assessments may not open inside the browser pane. Capture the address the button tries to open, open it in its own tab for the user, then reload the application to check the step registered.
- After submitting, optional follow-up tasks may appear (update personal information, review terms): leave them for the user.

#### iCIMS

- Login, password and CAPTCHA (often hCaptcha at "Submit profile") are the user's.
- The profile form sits in a same-origin frame (`iframe#icims_content_iframe`): work in its `contentDocument`, and attach the resume with that frame's own `File` and `DataTransfer`.
- Uploading the resume reloads the frame and can wipe fields: re-check everything after.
- Lazy dropdowns: dispatch mousedown, mouseup and click on the dropdown anchor, type in its search box if it has one, then click the result item.
- Follow-up forms (disability, veteran, acknowledgements) can load in a cross-origin frame. Complete them **inside the application tab** where possible; on some boards, completing them in a separate tab leaves the application "incomplete".
- Sessions time out after roughly 20 to 30 idle minutes; drafts may keep only some answers.
- **After sign-in, some boards submit an application the moment its apply link opens** (see "Before you start").

#### Paylocity

- No account. "Fill out application with my resume" reads the file; check every field, add missing jobs by hand.
- Dropdowns: real click on the control, wait about 2 seconds, click the list item. The acknowledgement checkbox needs a real click. Month/year dates need text insertion.
- Pick the address from its suggestions, then set the start date (picking the address wipes it).
- Some forms require supervisor contact details for every job marked "may contact".

#### BambooHR

No account. The state list may need real clicks through a button menu (`find` the control, click, `find` the option, click). Dates: click and type, then Escape. Submit is followed by a CAPTCHA checkbox: the user ticks it.

#### Jobvite

No account. Usually several pages: consent, contact and resume, self-identification with a typed name and date, screening questions, then a visible CAPTCHA at send (the user). The file upload tool may refuse the control; attaching by page script works. Next may need a real click.

#### Phenom (apply)

- No account on some boards. Read the posting from `phApp.ddo.jobDetail.data.job`.
- Fill every required field before the first Next: once a field is flagged, picking a value may not clear the error until a related field is retyped.
- An invisible CAPTCHA can reject a scripted submit: the user presses Submit. Reloading the apply address restores the draft and fixes buttons left disabled.

#### UKG Pro Recruiting and UKG Ready

- UKG Pro: an account at "Apply now" (the user). One long page; the resume reader often puts employer and location in the title.
- UKG Ready on a new employer: no password until "Sign & submit", which asks for a password as the signature (the user). Once a profile exists, the board asks the user to sign in.

#### Dayforce

- An account (Dayforce ID) or "apply without an account" on some boards.
- Creating the account: the agree box counts only after both policy links are clicked, and those links can open in the same tab and wipe the form. Have the user open them in a new tab.
- Ant Design form: open selects with a mousedown on `.ant-select-selector`, wait, click the option. Press each section's Update button and read the error messages after each.
- **Next is slow:** click once, wait about 5 seconds, confirm the page number. A double advance can skip a page unanswered.

#### ADP Workforce Now and ADP MyJobs

- Sign-in is by a texted or emailed code (the user). One emailed code may never arrive; the text option is often more reliable.
- Radios are web components; source dropdowns and self-identification need real clicks.
- Text inputs on the questions page often register only when typed for real.
- The last step can be an electronic signature: tick, type the full name, submit. Some flows have no review page: the last Next submits, so stop before it for the user's review.
- Some legacy ADP flows ask for the last four digits of a Social Security number and a birth date (a "rehire check"): a wall. The user decides.

#### Oracle Cloud Candidate Experience

- Often no account; a returning email may get a PIN or emailed code (the user).
- ZIP fields are autocompletes: type the ZIP in two parts so the list filters, then click the matching row.
- Pill-button questions take a script click. Comboboxes: focus, insert the text, wait, click the matching cell.
- The final e-signature can be an employment agreement with arbitration: quote it first.

#### SuccessFactors

- An account (the user). Picklists: click the select button, then the matching option inside the list named by the input's `aria-owns`. Dates are calendar widgets that take typed `MM/DD/YYYY`.
- Some flows require the current supervisor's name and title with no "may we contact" choice: raise it with the user.

#### Hirebridge, ClearCompany, isolved, Cornerstone, Paycom, Paycor and others

- **Hirebridge:** some boards offer a quick apply with no password; others ask for an existing profile's password (the user). The resume upload reloads the page: upload first.
- **ClearCompany:** no account on a first visit; a second visit to the same job emails a sign-in link (the user). Parsed rows arrive late; wait, then fix. Some forms require a birth date and Social Security number: a wall.
- **isolved Hire:** an account is created for the user after step 2 and a password is asked (the user). A returning email gets a secure code.
- **Cornerstone:** the first application creates a profile with a CAPTCHA (the user); later applications submit directly.
- **Paycom:** values set by script on selects, dates and autocompletes are wiped on submit. Use arrow keys on selects, type dates digit by digit, click autocomplete suggestions, real-click the acknowledgement.
- **Paycor:** plain form; setters work.
- **SmartRecruiters:** may show bot-check questions: the user answers.
- **Conversational (chat) apply flows:** answer from the answer bank; anything new goes to the user.

### Bot checks

Some career sites show a bot check that never clears in an automated browser. The user can usually pass it in their own Chrome; after that, Claude in Chrome can continue in that same window. Never try to get past a check yourself.

### Walls at a glance

| Wall | Seen on | Who |
|---|---|---|
| Account per employer | Workday, Dayforce, SuccessFactors, UKG Pro, some iCIMS | User |
| Password typed as the signature | UKG Ready (new employer) | User |
| Emailed or texted code | ADP, Oracle (returning), isolved (returning), Greenhouse after repeated failed submits | User |
| Emailed sign-in link | ClearCompany (second visit) | User |
| CAPTCHA at submit | iCIMS (hCaptcha), Jobvite, BambooHR, Cornerstone (first time), Phenom (invisible) | User |
| Birth date, Social Security number, ID digits | some ClearCompany and ADP flows, some tax-credit surveys | User decides |
| Bot check on the careers site | various | User, in their own browser |

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
[City], [State] | jordan.reyes@example.com | (555) 010-0199

### Summary
Operations coordinator with 5 years in a regional hospital system, moving into software customer success. Runs scheduling and vendor work for 3 clinics, and trained 40 staff on a new scheduling system.

### Experience
#### Operations Coordinator | Example Regional Health | [City], [State] | 2022 to Present
- Run day-to-day scheduling and vendor contracts for 3 outpatient clinics.
- Led staff training when the clinics moved to a new scheduling system; trained 40 staff in 6 weeks.
- Cut appointment no-shows by 20% with a reminder call process.

#### Front Desk Lead | Example Family Clinic | [City], [State] | 2020 to 2022
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
- Standard headings: Summary, Experience, Education (only if the user has any), Licenses and Certifications (if any), Skills. Optional: Volunteer Work, Languages, Military Service, Projects, Portfolio. Their order comes from the "What employers ask for" section of the user's facts file; the default order is Summary, Experience, Education, Licenses and Certifications, Skills.
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

**Words:** no word is off limits. A label like "team player" works best next to a fact that shows it ("trained 6 apprentices"). No em dashes or en dashes.

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
- Licenses and Certifications move up, directly under the summary. Use full names (for example "Registered Nurse, [State]" and "Basic Life Support").
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
- [License name], [State]

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

If the user chose not to show a school year, leave it off: `### Degree, Field | School`. If the user has no degree or diploma to show, leave the Education section out; never invent one.

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
- Years of experience to state on the resume: [number, and what it counts, for example "8, warehouse operations since Mar 2018"]

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

- "Suggest employers that fit my background." (Part A, using your rules)
- "Find [industry] employers in or near [place]." (Part A, narrowed)
- "Find employers like [company A] and [company B]." (Part A, starting from competitors and neighbors of good fits)
- "Find remote-friendly employers in [industry] that hire people in [state]." (Part A, remote only)
- "Tell me about [company]." (Part B, deep dive)
- "Map the [industry] employers around [place]." (Part C)
- "What does a [title] do, and what does it pay around here?" (Part D)
- "Add these employers to my target list: [names]." (Sweep step 1)

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
