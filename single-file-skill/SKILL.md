---
name: job-search
description: Runs a job search with the user. Use for the setup interview, resume building, finding and researching employers, sweeps of employer career sites, fit calls on postings, applications, hiring-manager outreach drafts, interview prep, and mailbox checks that read or write the user's job search tracker.
---

<!-- Built by tools/build_single_file.py from the workspace. Do not edit by hand. -->

# Job search

This Skill is the Job Search Full Automation workspace, packaged for chats outside its folder. It helps one person run their job search: it builds a resume from facts they confirm, finds and researches employers, finds openings on employers' own career sites, decides which ones fit the person's rules, keeps a tracker, fills in applications with them, drafts outreach for them to send, and prepares them for interviews.

The person stays in charge. Never submit an application without their review, never send a message, and never handle passwords, codes, ID numbers or CAPTCHAs.

This one file holds everything: the routing, the rules, the stage contracts and the references. Each file of the workspace is a section below, headed by its path in a comment. Where a section names a file such as `stages/01-sweep/CONTEXT.md` or `shared/rules.md`, read the section of that name below. The tracker page is not in this file: use the spreadsheet tracker, or get `tracker/tracker-page.html` from the full workspace.

## Where to work

- **The working folder holds the full workspace** (`CLAUDE.md` and `stages/` of this system): read that folder's `CLAUDE.md` and follow it. Its files are the same as this Skill's, plus the person's own outputs.
- **Otherwise,** this Skill folder is the workspace. Start at `CONTEXT.md` here. Every path in these files is relative to this folder (for example `shared/rules.md`, `stages/01-sweep/CONTEXT.md`). Save the person's files in their own folder at the same paths when there is one; when there is none, follow `shared/no-folder.md`.

## Every session

0. With no workspace folder, first ask the person to attach `my-setup.md`, `my-rules.md` and their tracker file if they have them (`shared/no-folder.md`).
1. Read `shared/rules.md` and the person's `my-rules.md` (from `stages/00-intake/output/`, or attached). They apply to every stage. Safety rules (rules section 9) apply from the first minute.
2. Find their tracker in `my-setup.md` (made by setup from `shared/my-setup-template.md`). If there is none, it still holds `{{` placeholders, or they did not attach it, ask which tracker they use and where, and run `setup/questionnaire.md` if they have none.
3. If they have no `my-rules.md`, run `stages/00-intake/CONTEXT.md` and nothing else.
4. Route the task with `CONTEXT.md`, then load only that stage's `CONTEXT.md` and the inputs its table names.
5. Do only the task asked. Never start another stage on your own. Nothing runs on a schedule or unattended.
6. A stage is done only when its Audit passes. Say plainly which checks did not.
7. End every session with the next thing to say (`shared/next-steps.md`).

## Scripts

The stages check their work with small Python scripts. They are in this Skill's `tools/` folder too: run them with code execution, from that folder's full path (`shared/no-folder.md`, "Scripts"). If they cannot run, check by hand as that file says, and say plainly that the script did not run.

---

<!-- CONTEXT.md -->

## Job Search Full Automation

A job search system for one person. Set up once, then run any stage when the person asks. The stages share one tracker; files pass between stages through `output/` folders.

### Task Routing

| Task Type | Go To | Description |
|-----------|-------|-------------|
| First-time setup | `setup/questionnaire.md` | Tracker, Python, browser, then the interview |
| Set or change the person's rules | `stages/00-intake/CONTEXT.md` | The interview, one question at a time |
| Check employers for listings, recheck open listings | `stages/01-sweep/CONTEXT.md` | Reads employers' own career sites |
| Decide whether one posting fits | `stages/02-fit-review/CONTEXT.md` | The sweep runs it for every new posting |
| Fill in applications | `stages/03-apply/CONTEXT.md` | The person reviews every form before submit |
| Hiring-manager outreach drafts | `stages/04-outreach/CONTEXT.md` | Only when the person says "run outreach" |
| Prepare for an interview | `stages/05-interview-prep/CONTEXT.md` | For one named interview |
| Check email for employer replies | `stages/06-mailbox-check/CONTEXT.md` | Read only; the person approves each change |
| Build, improve or tailor a resume | `stages/07-resume/CONTEXT.md` | Only from facts the person confirms |
| Find employers, research a company, industry or role | `stages/08-company-research/CONTEXT.md` | Adds employers only after approval |
| Add employers the person names | `shared/adding-employers.md` | Outside a stage, checked with `--stage research` (or `--stage user` when a listing is added too) |
| A returning person with no request | `shared/next-steps.md` | "A returning person with no request": read the tracker, suggest one thing |
| Decide a close call (apply or skip) | `stages/02-fit-review/CONTEXT.md`, then `references/fit-outcomes.md` | "The person decides a close call", checked with `--stage fit` (`--stage user` for dropping an existing listing) |
| A status change, or a job they applied to on their own | `shared/tracker-access.md` | "Direct requests", checked with `--stage user` |

### Shared Resources

| Resource | Location | Contains |
|----------|----------|----------|
| Rules | `shared/rules.md` | Fit rules, who writes what, autonomy limits, safety, writing |
| My setup | `shared/my-setup.md` | Tracker kind and location, Python command, browser, email connector (made by setup from `shared/my-setup-template.md`) |
| Tracker columns | `shared/tracker-columns.md` | Every collection and column, in plain words |
| Tracker access | `shared/tracker-access.md` | Reading, writing, backups, snapshots and the check script |
| Answer bank | `shared/answer-bank.md` | How to use the answers forms ask for |
| Adding employers | `shared/adding-employers.md` | The one way to add an employer |
| Recurring mistakes | `shared/recurring-mistakes.md` | Read before any tracker write |
| Helpers | `shared/helpers.md` | Rules for research helpers (subagents) |
| Prompts | `shared/prompts.md` | What the person can say to start each stage |
| Career direction | `shared/career-direction.md` | The career ladder (L1 to L9), how each posting's level is judged, and advancement |
| Lessons | `shared/lessons.md` | How each session adds what it learned to the notes and the mistakes list |
| Next steps | `shared/next-steps.md` | What to suggest when a session ends, and to a returning person |
| Python setup | `shared/python-setup.md` | Installing and checking Python |
| No folder | `shared/no-folder.md` | Working in a chat with no folder: files to re-attach, scripts, resume PDF |
| Tracker page | `tracker/tracker-page.html` | The page published as the person's tracker |
| Scripts | `tools/` | `check_tracker.py`, `check_resume.py`, `build_resume.py`, `sheet.py` |

### No folder to work in

On Claude on the web, a tablet, or the Skill uploaded in the Claude app, there may be no folder Claude can read and write. Then follow `shared/no-folder.md`: which files the person keeps and re-attaches (including the spreadsheet tracker), how to run or replace the scripts, and what needs the desktop app.

---

<!-- setup/questionnaire.md -->

## Setup questionnaire: Job Search Full Automation

Read this file when the person types `setup`, asks to be set up, or `shared/my-setup.md` does not exist or still holds `{{` placeholders. It configures the system, not the job search itself: the person's goals, rules and resume facts are collected by the stages.

---

### Before the questions

Say hello in two or three sentences: this finds jobs on employers' own career sites, checks each against their rules, keeps a tracker, builds a resume from facts they confirm, and fills in applications with them. Nothing is ever submitted or sent without their review. Setup takes about 15 minutes.

In a chat with no folder, follow `shared/no-folder.md`, "Setup", alongside this file.

Ask once for permission to run the setup commands (a version check, an install of two Python add-ons, and a self-test), rather than asking for each one. Then work out the derived fields below while they answer.

### Ask these all at once

The person should be able to answer both in one message.

#### Q1: Where do you want your tracker?
- Placeholders: `{{TRACKER_KIND}}`, `{{TRACKER_LOCATION}}`
- Files: `shared/my-setup.md` (from `shared/my-setup-template.md`)
- Type: selection
- Options:
  - **A private web page in your Claude account** (default, recommended): publish `tracker/tracker-page.html` as a new artifact with the `db` capability. Give them the link and ask them to open it: they should see an empty tracker that says "No listings recorded yet". Kind `Artifact`, location the link. If you cannot publish an artifact with a database here, say so and use the spreadsheet.
  - **A spreadsheet:** copy `tracker/spreadsheet/job-search-tracker.xlsx` to `tracker/my-tracker.xlsx`. Kind `Spreadsheet`, location `tracker/my-tracker.xlsx`. Tell them to close it in Excel before each session; if it is open, saving fails with a message saying so.

#### Q2: Do you already have a resume you are happy with?
- Placeholder: `{{RESUME_CHOICE}}`
- Files: `shared/my-setup.md` (from `shared/my-setup-template.md`)
- Type: selection
- Options:
  - **Yes, use mine as it is:** ask them to save it as `stages/07-resume/output/resume.pdf` (offer to wait). Write "use mine".
  - **Yes, but I want it improved:** write "improve mine". Ask them to save it in the same place (or paste its text when the resume stage starts), as a source of facts.
  - **No, or I need a new one:** write "build new".
  - Default: "decide later".

### Derived fields (do not ask)

#### `{{PYTHON_COMMAND}}`
In a chat with no folder: write "code execution" if you can run Python there (then use the Skill's `tools/` as `shared/no-folder.md` says), otherwise "none (Skill only)"; skip the install and the self-test. Otherwise follow `shared/python-setup.md`: find the command that works (`python`, `python3` or `py`), install the add-ons, and run the self-test. Write the command, or "none" if the person chose to continue without Python.

#### `{{APPLY_BROWSER}}`
Check whether the Claude in Chrome tools are available to you. Write "Claude in Chrome", "built-in browser only" (no Chrome, but the app's browser pane works), or "none" (no browser tool at all). If not connected, tell them: applying works best with the Claude in Chrome extension, because it can upload their resume (`stages/03-apply/references/claude-in-chrome-setup.md`). Sweeps and everything else work without it. This is not a blocker for today.

#### `{{EMAIL_CONNECTOR}}`
Check whether an email connector (for example Gmail or Outlook) is available to you. Write its name, or "none".

#### `{{SETUP_DATE}}`
Today, `YYYY-MM-DD`.

---

### After setup

1. Copy `shared/my-setup-template.md` to `shared/my-setup.md` and replace every placeholder in the copy with the answers and derived values. Never edit the template.
2. Scan `shared/my-setup.md` for any remaining `{{` patterns. If any remain, ask for the missing information.
3. Only when working in the folder, mention once, for chats outside it: they can also upload `job-search-skill.zip` in the Claude app (Customize, then Skills, then +, then Upload a skill; code execution must be on in Settings). It is not needed when working in this folder.
4. Tell the person:

"You are set up. Here is your setup:

- **Tracker:** [web page link, or tracker/my-tracker.xlsx]
- **Resume:** [use mine / improve mine / build new / decide later]
- **Browser:** [Claude in Chrome / built-in browser only / none]

Next is a short interview about the jobs you want. I ask one question at a time."

5. Start `stages/00-intake/CONTEXT.md`. Do not ask again what setup already answered.

---

<!-- shared/adding-employers.md -->

## Adding employers to the target list

The one way any session adds an employer to `companies`. Only when the user asks, or approves a suggestion.

1. Find the employer's own careers site. A redirect to the company's own careers subdomain, or to the job board the company itself links to (Workday, Greenhouse, Lever, Ashby and the like), counts as its own site. If the link you tried does not open, find the real one from the company's own home page. Never guess: leave the employer out until you have it. A careers link the user gives you counts; open it to confirm when you can.
2. Check that it is not already on the target list (exact name, `recurring-mistakes.md` item 7), not the user's current employer, and not on the never-contact list in the user's rules. Any of those: leave it out and say why.
   - **An industry the user ruled out** (in `settings.excludedIndustries` or "out" in their rules): tell the user and ask. Add it only if they say so in this session, and then set `keepAnyway` to `yes` and say in the report that they asked for it. Otherwise leave it out.
3. Build the row:
   - `id`: the name in lowercase with hyphens, for example `example-health-co`. Check no other row uses it.
   - `company`: the employer's own spelling.
   - `careersSite`: the link from step 1.
   - `tier`: `A`, `B` or `C`, using the user's tier meanings in `settings`.
   - `industry`: in the words of `settings.industryOrder` where it fits.
   - `keepAnyway`: `no`, unless the user asked to keep an excluded-industry employer (step 2).
   - `onHold`: `yes` only if the user's rules put this employer on hold, otherwise `no`.
   - `added`: today, `YYYY-MM-DD`.
4. Show the list to the user before saving. Write only the employers they approve, with a snapshot before and a check after (`tracker-access.md`). Inside a sweep or a fit review, that stage's own check covers it. When a direct request also adds a listing (a job they applied to on their own), the one `--stage user` check covers both. Anywhere else (the intake, company research, or a direct request), run the check with `--stage research`, then suggest a sweep of the new employers ("Say 'Sweep [names]'").

---

<!-- shared/answer-bank.md -->

## Answer bank

The answer bank lives in the tracker, not in these files: the `answers` collection (artifact) or the `answers` tab (spreadsheet). Read it fresh at the start of every application session. It is the source of truth. Nothing in this file overrides it.

### How to use it

- When a form question matches an entry, answer from it without asking.
- When a question is worded unusually, or the entry's `useWhen` says to ask, confirm with the user before using the entry.
- Pay questions use the `Pay` entries: the wording where the form takes text, the single number where it needs one.
- Voluntary diversity questions use the `Voluntary` entries. With no entry, choose "I don't wish to answer" and tell the user.
- References come only from the `References` entries, in the order listed.
- Work history comes from the `Work history` entries and the resume text (`resume.md`). They must agree. If they do not, ask the user.
- Add each new application-system account as an `Account` row: the website in `question`, the username in `answer`. **Never a password.**

### What never goes in the answer bank

- Passwords, security answers, one-time codes.
- Social Security numbers or other government ID numbers, driver's license numbers.
- Bank account, routing or card numbers.

### Autonomy

Any extra autonomy the user grants (for example auto-submit) lasts for one session only and is never saved here as a standing permission.

---

<!-- shared/career-direction.md -->

## Career direction

How the system places a person on the career ladder, judges every posting against where they are and where they want to go, and helps them move up. It works the same for a first job and for an executive search.

### The ladder

Eight levels, plus a top rung for chief roles. Most fields use some version of them; the words differ, the steps do not.

| Level | Name | Typical signs in a person's history or a posting |
|---|---|---|
| L1 | Entry | First job in the field, trainee, "junior", "I"; "coordinator", "assistant" or "associate" asking 0 to 2 years; does assigned tasks under direction |
| L2 | Developing | "II", "specialist", 2 to 4 years required, owns tasks with some guidance |
| L3 | Experienced | No prefix or "III", 4 to 7 years, owns a whole area or a book of work alone |
| L4 | Senior | "Senior", "lead" (individual work), 6+ years, handles the hardest cases, trains others informally |
| L5 | Team lead or supervisor | "Supervisor", "team lead", "manager" of a small team, assigns and checks others' work |
| L6 | Manager | "Manager" with direct reports, owns hiring, a budget or a team's results |
| L7 | Senior manager or director | "Senior manager", "director", "head of", managers report to them (team leads reporting to a manager keep it at L6), sets plans for a function |
| L8 | Executive | "VP", "senior VP", "general manager", owns a business unit or a whole function across the company |
| L9 | Chief | "Chief ... officer", "president", company-wide profit and loss |

Two tracks run side by side above L3: **individual contributor** and **people leader** (L5 to L8). For individual roles above L4, use scope as the guide: several teams or 8+ years is an L5 equivalent, a whole function is an L6 or L7 equivalent. A small team with no hiring or budget ownership is L5; hiring or a budget makes it L6. An individual role matches a next step only on the same track: an IC L5 is not a match for a "first team lead" goal. Principal, staff, expert or individual "director" roles with no reports take the level their scope, required years and pay match (L4 to L7), marked "IC track" in `why`. Moving between tracks at the same scope is a **track switch**, not a step: bring it to the person as a close call. Moving from L4 to a first L5 role is a step up.

**Senior VP and executive VP** stay at L8, a stronger L8 rather than a new level. **L9** chief roles are a step up for an L8, a stretch for L7, and out of reach below that.

Title words mislead across employers ("manager" can mean no reports; "associate" can mean experienced in law or consulting). **Judge a posting by its duties, scope and required years first, the title last.** When duties and title disagree, say so in `why`. When required years and duties point to different levels, go by the required years, unless the duties include supervising people or owning a budget or profit and loss; then go by the duties.

An internship is below L1 for anyone who has finished school: treat it as a step down. For a current student, an internship is the same level (L1).

### Placing the person

The intake interview sets three lines in section 1 of `my-rules.md`:

- **Current level:** worked out from their history, not asked as a label. Use years in the field, the highest title held, whether they led or managed people (how many), and the size of what they owned (accounts, budget, projects). Show the result and the reason in one line, for example "L3 Experienced: 5 years, owns a book of 40 accounts, no direct reports", and let the person correct it.
- **Next step:** the level and role they want next, in their own words, for example "L4 Senior account manager" or "L5 first team lead role". "Same level, new field" is a valid answer.
- **Step down allowed:** yes or no, and when (for example "only to change fields", or "only above my pay floor").

**Career changers** have two levels: their level in the old field and their **starting level in the new field**. The new-field level is usually one to three steps lower, rising with transferable experience (a nurse moving into healthcare sales starts around L2 in sales, not L1, because clinical knowledge transfers). Write both, and judge postings against the new-field level.

### Judging a posting's step

Place each posting on the ladder (duties, scope, years, then title), then compare with the person's current level:

| Step | Rule | What fit review does |
|---|---|---|
| **Step down** (lower than current) | Allowed only if the person's rules say so | Otherwise a no (check 3). If allowed, say why it is worth it in `why`. |
| **Same level** | Always allowed | Normal fit. |
| **Step up** (one level higher) | Always allowed, and preferred when it matches their next step | Raise priority one band only when it matches their next step and pay and place fit (`fit-outcomes.md`). |
| **Stretch** (two levels higher) | The person decides | A close call for the person, never added on its own; lean Skip when most required duties do not match their real experience. |
| **Out of reach** (three or more higher) | Not a target | A no, unless the person asks. |
| **Track switch** (same scope, other track) | Allowed only with the person's yes | A close call for the person. |

Start every `why` with the step, for example "Step up (L3 to L4): ...", so the person can scan the tracker by direction.

**When the level is unclear.** Apply the tie-breaks above first (required years versus duties; title last). If a posting could still sit at two levels and the result would differ (added, close call, or no), do not pick one. Treat it as a close call: in "Flag", name both levels and what points to each (duties, scope, required years, pay), and ask the person which reading fits. If both readings give the same result (for example same level or a step up, both added), write the listing at the lower level's step, add "(level unclear: L4 or L5)" to the `why` prefix, and do not raise priority for a next-step match.

Inside the stretch on required years (rules section 3), years alone never fail a step up.

### Advancement

The system helps the person climb, not just find jobs at their current level:

- **Fit review:** a posting that builds toward the person's next step ranks above one that does not, at the same pay. Record in `teaches` what the role would add toward that next step (for example "Stated: leads a team of 4, which builds toward the L5 goal").
- **Resume:** for a step-up resume, read postings at the next level, and lead each job with the facts that show next-level scope (leading, training, owning results, cross-team work). Only facts the person confirmed.
- **Interview prep:** for a step up, prepare the likely question "Why are you ready for this level?", answered with true stories of work already done at that level.
- **Career path research:** "What's my next career step?" (company research part E) maps the person's current role to the next one or two levels, from real postings: what those roles require, what the person already has, the gaps, and how to close each gap (a skill, a certification, a project at work).
- **Review the direction** when the person lands a job, gets promoted, or every six months: offer to update the three lines in `my-rules.md`. After a new job, also offer to add the new employer to the never-contact list as their current employer (section 7), put it on hold in the target list, and close or keep their other open listings, one at a time with their yes.

### Examples

- **Entry level:** a graduate with internships is L1. Postings at L1 and L2 fit; L2 is a step up. "Senior" postings are out of reach.
- **Experienced, aiming to lead:** an L4 senior analyst whose next step is "L5 team lead". L5 postings are step ups and rank high; L6 manager roles are stretches brought as close calls; L4 roles are same level and still fit.
- **Executive:** an L7 director whose next step is "L8 VP". Most L7 roles are same level; L8 roles are step ups; L6 roles are step downs and are a no unless they allow it.

---

<!-- shared/helpers.md -->

## Working with helpers (subagents)

Rules for any session that hands reading work to research helpers.

- About **6 employers per helper**, and a cap of about 50 tool calls each. A board with more than about 200 jobs goes alone or with very small boards. Helpers given 11 or more employers silently dropped some.
- Each helper loads its browser tools once, **opens its own tab** (never a shared one), and closes only its own tab.
- Each helper writes its final findings to a file in the stage's `output/` folder as well as returning them (a hand-back can be lost), and returns at most about 20 KB.
- Every finding carries: job number, title, location as written, the employer's own job address, the board's work-type tag, pay if posted, and the **quoted requirement lines**. If the requirements could not be read, the helper says so.
- Give helpers only confirmed board addresses, or have them find the board from the careers page first.
- Helpers only read: no tracker writes, no applications, no sign-ins, no bot-check workarounds.
- The main session re-checks every finding against the rules, opens at least one posting per helper on the employer's own site, and does every write.

---

<!-- shared/lessons.md -->

## Lessons

How the system learns from use. Every stage does this once, at the end of the session, before suggesting the next step.

### Ask once

Ask: "Did anything surprise you or go wrong this session?" Add anything you noticed yourself: a site that behaved differently from the notes, a rule that led to a wrong call, a check that caught a mistake, a step that was unclear. If there is nothing new, say nothing more and move on.

### Where each lesson goes

Show the person the exact line you would add and where. Add it only after they say yes.

| The lesson is about | Add it to |
|---|---|
| How a job board behaves | `stages/01-sweep/references/board-platforms.md` (that platform's section), or `board-techniques.md` for something true of every board |
| How an application form behaves | `stages/03-apply/references/application-platforms.md` (that platform's section), or `application-techniques.md` for something general |
| A mistake that could happen again | `recurring-mistakes.md`: a new numbered item at the end, saying what happened and the rule that prevents it |
| The person's own preferences changed | Their `my-rules.md`, through the intake stage, with a dated line in section 10 |

### Rules for every lesson

- One or two lines. Edit the existing section in place; never repeat what is already there.
- General methods only: never employer names, the person's details or dates in the shared or reference files.
- A lesson never weakens a safety rule (`rules.md` section 9) or the rule that the person reviews every application. If a lesson seems to call for that, tell the person instead of writing it.
- With no folder, give the changed file as a download (`no-folder.md`).

### Share it

After adding a general lesson about a job board or an application form, offer once: "Want to share this with everyone who uses this system? Open an issue at https://github.com/trotics/job-search-full-automation/issues with just the general method (no employer names or personal details)."

---

<!-- shared/my-setup-template.md -->

## My setup

<!-- Setup copies this template to shared/my-setup.md (which git never shares) and fills in every placeholder. -->

System settings for this job search, filled in once by setup. Every stage reads this file to find the tracker and the tools.

- **Tracker kind:** {{TRACKER_KIND}}
- **Tracker location:** {{TRACKER_LOCATION}}
- **Python command:** {{PYTHON_COMMAND}}
- **Browser:** {{APPLY_BROWSER}}
- **Email connector:** {{EMAIL_CONNECTOR}}
- **Resume choice:** {{RESUME_CHOICE}}
- **Set up on:** {{SETUP_DATE}}

---

<!-- shared/next-steps.md -->

## Next steps

What to suggest when a session ends, so the person always knows what to say next. "Check my email" is short for "Check my email for employer replies". Wherever a line says "Check my email" and `my-setup.md` shows no email connector, say instead: "In a few days, paste any employer replies here and say 'Check these emails' (or connect your email in Claude's settings)." If the person has no browser Claude can control (`my-setup.md` says browser "none", or there is no desktop app, see `no-folder.md`), never suggest "Run a sweep" as something to do now. "Let's apply" still works with a fill sheet (Claude prepares every answer; the person fills in the form and submits it in their own browser), so say that plainly. Also suggest "Build my resume" (if there is no resume yet) or "Is this a fit? [paste a posting and its link]". Suggest only; never start the next stage yourself. Keep it to one or two lines, with the exact words to say in quotes, and pick the line that fits what just happened.

### After the interview

- They chose "build new" or "improve mine" for the resume: "Say 'Build my resume'." Then, if they have no employers yet, add "After that, 'Suggest employers that fit my background'"; if they just added some, "After that, 'Run a sweep'".
- They have a resume and no employers yet: "Say 'Suggest employers that fit my background', then 'Run a sweep'."
- They have a resume and just added employers: "Say 'Run a sweep'."

### After the resume

- No employers on the target list yet: "Say 'Suggest employers that fit my background'."
- Listings at To apply: "Say 'Let's apply'. Your new resume will be used."
- Otherwise: "Say 'Run a sweep'."

### After company research

- Employers were added: offer a sweep of them ("Say 'Sweep [names]'").
- A company deep dive before applying or an interview: "Say 'Apply to the [company] [title] listing'" or "Say 'Prep me for my interview with [company]'".
- An industry map: "Say 'Add these employers to my target list: [names]'" for any they liked.
- Role research: if the role fits, "Say 'I want to change my rules: add [title]'".

### After a sweep or a fit call

- No resume yet (no `resume.pdf`): "Say 'Build my resume' first, then 'Let's apply'."
- New listings at To apply: give the count, then "Say 'Let's apply' when you have time to sit with it."
- Manual employers: list them, and ask the person to open those sites in their own browser when they can.
- Close calls in the report: ask the person to decide each one.
- Nothing new: "Nothing fit this time. Say 'Suggest employers that fit my background' for more employers, or run another sweep in about a week."

### After applying

- A dry run: "Say 'Apply to the [company] [title] listing' when you want to do it for real."
- A fill sheet was given (no browser): "Fill it in and submit in your browser, then tell me 'I submitted it' with the confirmation, and I will mark it Applied."
- Listings still at To apply: "Say 'Let's apply' to keep going."
- Applications went in: "In a few days, say 'Check my email' to catch replies."
- Their rules ask for outreach drafts: "Say 'Run outreach on the [company] listing' if you want a note to the hiring manager."

### After outreach

- The listing is still at To apply: "Apply first: say 'Apply to the [company] [title] listing'. Then send the drafts yourself."
- Otherwise: "Send the drafts yourself when you are ready. In a few days, say 'Check my email'."

- No listings qualified: say why in one line (for example "outreach is for listings at To apply or Applied recently"), then the next most useful thing from "A returning person with no request".

### After a close-call decision

- They chose to apply: "Say 'Apply to the [company] [title] listing'."
- They chose to skip: confirm in one line, then the next most useful thing from "A returning person with no request".

### After a direct change

- A job accepted or a promotion: congratulate them, then "Say 'Update my career direction' so I aim at your next step." After a new job, also offer the updates in `career-direction.md`, "Advancement" (new employer as current employer, other open listings).
- A rejection or a closed listing: one kind line, then the next most useful thing from "A returning person with no request".
- Anything else: confirm what changed in one line, then the same.

### After interview prep

"Good luck. After the interview, say 'Check my email' to log the next step."

### After the mailbox check

- An interview was found: "Say 'Prep me for my interview with [company] on [day]'."
- Deadlines (assessments, scheduling): list them first, with dates.
- A rejection: one kind line, then the next most useful thing below.
- Listings still at To apply: "Say 'Let's apply'."
- Nothing new and no sweep in the last week: "Say 'Run a sweep' to look for new listings."

### A returning person with no request

Find the tracker in `my-setup.md` and read `listings` and `coverage` as `tracker-access.md` says (no snapshot needed: this only reads). An employer with no `coverage` row has never been swept, unless its industry is excluded (those are skipped on purpose and do not count). Then suggest the one most useful thing:

1. A deadline or an interview coming up (a listing at Interview whose newest history line gives a future date, or a deadline in the latest mailbox report): name it with its date first. If no prep file for it exists in `stages/05-interview-prep/output/`, add "Say 'Prep me for my interview with [company] on [day]'"; if one exists, just wish them luck. For an assessment or a reply to send, say what to do and by when.
2. Things waiting on the person: close calls in the latest sweep or fit report that are not decided yet (not in `listings` or `coverage.skipped` and not marked decided in their report; recording a decision: `stages/02-fit-review/references/fit-outcomes.md`), and employers whose `coverage` says `manual` or `LEAD`. Name them in one line each and ask them to decide or open the site.
3. Listings at To apply: "Say 'Let's apply'."
4. Applications in and no mailbox check in the last week: "Say 'Check my email'."
5. No sweep in the last week: "Say 'Run a sweep'."
6. Otherwise: "Say 'Suggest employers that fit my background'."

---

<!-- shared/no-folder.md -->

## Working without a folder

For a chat with no folder Claude can read and write (Claude on the web, a tablet, or the Skill uploaded in the Claude app). Every other file still applies; this one says what changes.

### The person's files travel with them

There is nowhere to keep files between chats, so the person keeps them:

- `my-setup.md`, `my-rules.md`, and `my-tracker.xlsx` (if their tracker is the spreadsheet).
- For the resume: `resume-facts.md`, `resume.md` and `resume.pdf`.

At the start of each chat, before anything else, ask them to attach `my-setup.md`, `my-rules.md` and their tracker file plus the ones the task needs, or to keep them in the files of a Claude Project so every chat sees them. **Every session that creates or changes one of these files ends by giving the complete new file as a download**, with one line: "Save this over your old copy, and attach it next time." Never start a new tracker, setup or interview when the person may simply have forgotten to attach their files: ask first. Reports (fit, research, prep) are shown in the chat and given as downloads if the person wants to keep them.

In `my-setup.md`, the spreadsheet tracker's location is "my-tracker.xlsx (kept by you; attach it each chat)".

### Scripts

The scripts are in this Skill's `tools/` folder. If code execution is on, run them from there with the full path, on the files the person attached (for example `python <skill folder>/tools/check_tracker.py snapshot my-tracker.xlsx <stamp>-before.json`), and give back the changed files.

If code execution is off or a script cannot run: edit the spreadsheet only if you can, otherwise give the person the exact rows to type in. Check the work by hand against `recurring-mistakes.md` and the stage's Audit table, and say "checked by hand; the script did not run". Never call that a passed check. Backups and snapshots made in code execution are lost when the chat ends: the downloaded tracker is the person's only backup, so remind them to keep the previous copy until the new one is saved.

**The one-file Skill** (`single-file-skill/SKILL.md`) has no `tools/` and no tracker files. With code execution, build the spreadsheet with openpyxl from the tabs and columns in `tracker-columns.md` (settings has one row, id `main`), and check by hand. Without it, get the tracker from the full workspace at the link at the end of this file.

### Setup

- Skip the permission request for the install and the self-test: they are not run without a folder. If code execution is on, ask once before running scripts.
- Tracker: publish the tracker page if you can (the page is in this Skill's `tracker/` folder). Otherwise give `tracker/spreadsheet/job-search-tracker.xlsx` as a download named `my-tracker.xlsx`, and tell them to keep it.
- Resume they want to use: ask them to attach it, rather than save it in a folder.
- Do not suggest uploading the Skill; they already have it.

### The resume PDF

Build it with `tools/build_resume.py` in code execution and give it as a download. If that cannot run, give `resume.md` as a download and tell them to paste it into a word processor and save it as a PDF; then run the resume checks by hand (no dashes or pronouns, every fact in the facts file, page count).

### What needs the desktop app

Sweeps of most career sites need a browser Claude can control. Applying works without one through a fill sheet (`stages/03-apply/references/apply-procedure.md`, "No browser Claude can use"): Claude prepares every answer and the person submits it in their own browser. Until the person is at a computer with the desktop app, also suggest fit calls on postings they paste ("Is this a fit? [paste the posting and its link]"), resume work, company research and interview prep.

The full workspace folder, with everything set up for the desktop app, is at https://github.com/trotics/job-search-full-automation.

---

<!-- shared/prompts.md -->

## Prompts: what to say to Claude

Copy any of these into a session. Words in [brackets] are yours to fill in. Each one starts the stage named after it, and only that stage.

### Getting set up

- "Hey, look at this folder and set me up." (Setup, then stage 00: the intake interview)
- "I want to change my rules: [what changed]." (Stage 00, only the parts you name)
- "Publish tracker/tracker-page.html as a new artifact with the db capability, and give me the link." (Tracker setup, if setup could not do it)

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
- "What's my next career step?" (Part E: the next levels up, what they need, and how to close the gaps)
- "Update my career direction." (Stage 00: your current level and next step)
- "Add these employers to my target list: [names]." (Adds them to your target list)

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
- "Check these emails: [paste the employer replies]." (No email connector needed)

---

<!-- shared/python-setup.md -->

## Python setup

**What it is:** Python is a free program that runs the small scripts in `tools/`. They check Claude's work on the tracker and the resume, and build the resume PDF. Every stage that writes uses them.

### Check whether it is installed

Run `python --version`. On a Mac try `python3 --version`; on some Windows computers `py --version`. Use whichever works for every later command, and save it in `my-setup.md`.

### Install it (only if none of those work)

Tell the user in plain words:

- **Windows:** download Python 3 from python.org. In the installer, tick "Add python.exe to PATH" before clicking Install.
- **Mac:** download Python 3 from python.org and run the installer.

Then check again. The user may also continue without Python for now. Without it, stages cannot finish their checks, and you must say so whenever that happens.

### Install the two add-ons

```
python -m pip install -r requirements.txt
```

This installs openpyxl (reads the spreadsheet) and reportlab (builds the resume PDF).

### Verify it works

```
python tests/run_checker_selftest.py
```

Only the last line matters: it should say `SELF-TEST: ALL CAUGHT`. The lines above it that say FAIL are the test catching mistakes it planted on purpose; tell the user that so they are not alarmed. If the last line says anything else, tell them, and do not go further until it is understood.

### When a script cannot run

If Python or an add-on is missing, say so plainly and offer to install it. Never skip a check silently: a stage whose check could not run is not done.

---

<!-- shared/recurring-mistakes.md -->

## Recurring mistakes to avoid

Each of these happened during real use of this system. Read this list before any tracker write. When a session finds a new mistake that could happen again, add it at the end as `lessons.md` says, with the person's OK.

1. **Aggregator pages treated as proof.** An unattended run marked a batch of listings expired because a job aggregator showed them gone. Most were still live on the employers' own sites, and some were already Applied. Only the employer's own site decides.
2. **Changing listings at Applied or later.** The same run did it. Sweeps never touch them.
3. **Starting work nobody asked for.** A session asked to do one small task ran a whole other stage and wrote to many listings. Do only the task asked.
4. **Two sessions writing the same file.** The last write silently won and the earlier work was lost. One session owns the tracker at a time. For the spreadsheet, the user's own Excel window counts as a second writer: ask them to close it.
5. **Overloaded research helpers.** Helpers given 11 or more employers silently dropped some. Keep it to about six each.
6. **Stale reads.** Values copied from an earlier read were wrong by the time of the write. Read each row fresh right before writing it, and check by script after.
7. **Loose company matching.** A first-word match filed one company's listings under a different company whose name started the same way. Match the full company name, exactly as in `companies`.
8. **A background the user wants to leave, used as a selling point.** If the user says they are moving away from a kind of work, it is never a plus in a fit call or a message.
9. **Rules left in old prompts.** Saved prompts and notes carried outdated rules that later sessions followed. The rules live only in `shared/rules.md` and the user's `my-rules.md`.
10. **Shared browser tabs.** Two helpers working in one browser tab overwrote each other's pages. Each helper opens its own tab.
11. **Unattended runs that could not do the work.** A scheduled run in the cloud had no browser access to employer sites and no access to the user's folder, so it wrote bad data. Every stage is started by the user, in a session that can reach the sites and files it needs.

---

<!-- shared/rules.md -->

## Rules

Stable rules for every stage. They work together with the user's own rules, `my-rules.md` (saved by the intake interview), which holds everything personal: target roles, place, pay, industries, experience stretch, hard noes, employers on hold, autonomy and writing style. Where this file says "the user's rules", it means `my-rules.md`.

If the tracker and a file disagree on status, the tracker wins. If anything disagrees with this file or `my-rules.md`, those win. If this file and `my-rules.md` disagree, `my-rules.md` wins for the user's own preferences (roles, place, pay, industries) and this file wins for safety. Safety rules never bend. For tools and connections (tracker, Python, browser, email connector), `my-setup.md` wins: it records what setup actually found.

When two rules conflict and nothing here settles it, the newest dated rule in `my-rules.md` wins, and you tell the user about the conflict. Safety rules (section 9) always win.

### 1. What counts as a target role

- A role is a target only if it matches the **target roles** in the user's rules and its **level** is allowed by `career-direction.md` (same level, a step up, or a stretch brought to the user; a step down only if their rules allow it).
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

### 8. Autonomy

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

### 9. Safety

- Never create an account, set or enter a password, or read a password field.
- Never enter a Social Security number or other government ID, driver's license, bank account or card number.
- Never solve or try to get past a CAPTCHA, bot check or one-time code.
- Never send an email, message or form on the user's behalf. The only exception is submitting an application after the user's review, or under auto-submit the user turned on for this session.
- Assessments, aptitude tests, criminal-history questions, and whether they would sign a future non-compete or non-solicitation agreement are the user's to answer. Whether they are bound by one now comes from the answer bank.
- Never contact the user's current employer. Never use the user's work email, work phone or work accounts.
- **Site terms.** LinkedIn and some job boards forbid automated access in their terms of use. This system never automates LinkedIn in any way: no scraping, no automated profile visits, no messages, and no opening linkedin.com pages. The user is responsible for following each site's terms.

### 10. Writing

- Follow the writing style in the user's rules.
- Plain language. No em dashes or en dashes.
- Anything sent under the user's name must read like a person wrote it.
- The resume is submitted as-is and never rewritten unless the user asks in that session. When the user asks, stage 07 builds it only from facts they approved.

### 11. Files

- Each stage saves its reports in its own `output/` folder, named as its Outputs table says. Git never shares those folders.
- Tracker backups and snapshots go to `tracker/backups/`.
- When a file changes, give the complete new version, never a list of edits.

---

<!-- shared/tracker-access.md -->

## Tracker access

How every stage reads, writes, backs up and checks the tracker. Which tracker the user has, and where, is in `my-setup.md`. Every column is described in `tracker-columns.md`.

Run every command from the workspace root (the folder that holds `CLAUDE.md`). Use the Python command saved in `my-setup.md` (`python`, `python3` or `py`). In a chat with no folder, follow `no-folder.md`, "Scripts", instead.

### Artifact tracker (main)

A Claude artifact page the user published from `tracker/tracker-page.html`, with its own database. The link is in `my-setup.md`.

- **Read** with the `ArtifactData` tool: `list` for a collection, `get` for one row. Collections: `companies`, `coverage`, `listings`, `answers`, `settings`.
- **Write** one row at a time: `update` for an existing row, `set` for a new one.
- **Re-read before writing.** Read the row fresh just before you change it, and write only the fields you changed. Pass the `version` you read as `if_version` on every write to an existing row (a new row needs none). The database refuses the write if the row changed since ("version_mismatch"): read it again and redo the write against what it holds now.

### Spreadsheet tracker (fallback)

`tracker/my-tracker.xlsx`, a copy of `tracker/spreadsheet/job-search-tracker.xlsx`, with tabs of the same names and the same columns.

- Read it with `tools/sheet.py list tracker/my-tracker.xlsx <tab>` (every row) or `show ... <tab> <id>` (one row). Write it with `tools/sheet.py apply`, or with Python and openpyxl.
- Changes files for `sheet.py apply` hold personal data: save them as `tracker/backups/<stamp>-changes.json`.
- Ask the user to close the file in Excel before a session writes to it. If it is open, saving fails with a message saying so.
- If a row changed since you read it, stop and read it again.

### Direct requests

When the person asks for a tracker change outside a stage, take a snapshot first and run the check with `--stage user` afterwards.

- **A status change:** read the row fresh, change `status`, and append a history line: `YYYY-MM-DD status set to <status> at the user's request.` When the new status is Applied, also set `appliedDate` (ask the date); record a confirmation number only by its last 4 digits. After a fill sheet, use the history line in `stages/03-apply/references/apply-procedure.md`, "No browser Claude can use".
- **A job they applied to on their own:** add the employer first if it is not on the target list (`adding-employers.md`), then add a `listings` row with every column `check_tracker.py` requires: `id` (`<company-slug>-<req id or short title slug>`, unique), `company` (as in `companies`), `title`, `location`, `url`, `industry`, `pay` (or "not posted"), `why` (one line, for example "Applied by the user outside a session"), `teaches` ("Not read." if unknown), `priority`, `status` `Applied`, `appliedDate` (the date they give), `postingText` (the posting if they have it; otherwise "Not saved: applied outside a session"), and `history`: `YYYY-MM-DD added at the user's request; applied on their own on YYYY-MM-DD.` Leave `yourNotes` empty.

### Backups and snapshots

All tracker backups and snapshots go in `tracker/backups/`. Git never shares that folder.

Snapshots get a dated name, so no session overwrites another: `<stamp>` below means the session's start time and stage, for example `2026-10-03-0915-sweep`. Every `before` snapshot is a full copy of the tracker, so it is also the session's backup.

**Before more than five writes in one session** (count rows written, not commands) on the spreadsheet, also save a copy of the file, so it is easy to restore. For the artifact tracker the `before` snapshot is enough. Either kind can also be backed up on its own at any time:

- Artifact: list every collection with `ArtifactData` (`out_dir` set to a new folder under `tracker/backups/`), then combine them with `python tools/check_tracker.py snapshot-dir <that folder> tracker/backups/tracker-backup-<YYYY-MM-DD>-<HHMM>.json`.
- Spreadsheet: `python tools/sheet.py backup tracker/my-tracker.xlsx`.

### Checking by script

Every stage that writes ends with a check: `tools/check_tracker.py` compares a snapshot from before the session with one from after, and fails if any rule was broken (`yourNotes` changed, history rewritten, a listing at Applied or later touched by a sweep, a new listing missing a column, and so on). A stage is not done until the check passes.

**Spreadsheet:**

```
python tools/check_tracker.py snapshot tracker/my-tracker.xlsx tracker/backups/<stamp>-before.json
  (the session runs)
python tools/check_tracker.py snapshot tracker/my-tracker.xlsx tracker/backups/<stamp>-after.json
python tools/check_tracker.py check tracker/backups/<stamp>-before.json tracker/backups/<stamp>-after.json --stage sweep
```

**Artifact:** list each of the 5 collections with `ArtifactData` (`list`, with `out_dir` set to `tracker/backups/<stamp>-before-db`). That saves one file per row. Then combine them:

```
python tools/check_tracker.py snapshot-dir tracker/backups/<stamp>-before-db tracker/backups/<stamp>-before.json
  (the session runs)
  (list the 5 collections again with out_dir tracker/backups/<stamp>-after-db)
python tools/check_tracker.py snapshot-dir tracker/backups/<stamp>-after-db tracker/backups/<stamp>-after.json
python tools/check_tracker.py check tracker/backups/<stamp>-before.json tracker/backups/<stamp>-after.json --stage sweep
```

Use the stage's own name in `--stage`. A fresh `after-db` folder each time keeps rows deleted during a session from lingering from an earlier run.

The `--stage` choices are `intake`, `sweep`, `fit`, `apply`, `outreach`, `prep`, `mailbox`, `resume`, `research` and `user` (a change the user asked for directly).

**When a check fails because of something the user did** (they typed a note, or changed a status on the tracker page during the session), tell the user. Never undo their change, and never write `yourNotes` to make a check pass.

---

<!-- shared/tracker-columns.md -->

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
| `keepAnyway` | `yes` keeps this employer in sweeps even if its industry is excluded. Otherwise `no`. | You (Claude sets `yes` only when you ask for it) |
| `onHold` | `yes` means sweep it, but do not apply without your go-ahead. Otherwise `no`. | You (Claude sets it from your rules when adding an employer) |
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
| `result` | `HIT` (listing added), `NONE` (nothing fit), `LEAD` (something needs you, including a site you must open yourself), `PENDING` (not finished). | Claude |
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
| `reviewReason` | Why a listing at Review fit needs your call. | You (Claude only at your request) |
| `history` | Dated log of everything sessions did. **Add only, never change or delete.** Entries are separated by ` \| `, and each starts with a `YYYY-MM-DD` date. An entry never contains the `\|` character itself (write `/` instead). | Claude (append only) |
| `yourNotes` | Your own notes. **Claude never writes this.** | You |
| `managerName`, `managerTitle`, `howIdentified`, `confidence`, `profileUrl`, `emailOrFormat`, `connectionNote`, `longMessage` | Outreach research and drafts (stage 04). Drafts only. You send. | Claude |

**Status values:** `To apply`, `Applied`, `Followed up`, `Interview`, `Offer`, `Review fit` (set only by you, for a listing you want to think over; fit review never creates listings at this status), `On hold`, `Rejected` (the employer said no), `Closed` (you passed), `expired` (the posting came down), `filled` (the employer says it is filled).

An accepted offer stays at `Offer`, with "accepted" and the date in `history`.

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

How sessions read, write and check the tracker is in `tracker-access.md`.

---

<!-- stages/00-intake/CONTEXT.md -->

## Stage 00: Intake interview

Set up a new user's rules, or change an existing user's rules. Ends with `my-rules.md` saved, the tracker's `settings` record filled, and, if the user wants it, a starter answer bank.

### Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Shared | `../../shared/rules.md` | Full file | The general rules, to explain them when asked |
| Shared | `../../shared/career-direction.md` | "The ladder", "Placing the person" | Working out current level and next step |
| Shared | `../../shared/my-setup.md` | Full file | Tracker kind and location, Python command, browser, email connector |
| Shared | `../../shared/tracker-access.md` | Full file | Reading, writing and the check around the tracker writes |
| Shared | `../../shared/recurring-mistakes.md` | Full file | Read before any tracker write |
| Shared | `../../shared/adding-employers.md` | Full file | If the user already has a list of employers |
| Shared | `../../shared/prompts.md` | Full file | What to say in later sessions |
| Shared | `../../shared/next-steps.md` | "After the interview" | What to suggest when the session ends |
| Shared | `../../shared/lessons.md` | Full file | Learning from this session |
| Reference | `references/interview-questions.md` | Full file | The questions, in order, and how to ask them |
| Reference | `references/my-rules-template.md` | Full file | The shape of the finished file |
| Reference | `references/settings-and-answers.md` | Full file | The settings record and the starter answer bank |
| Previous run | `output/my-rules.md` | Full file, if it exists | Change only the parts the user names |

### Process

1. If `output/my-rules.md` exists, read it first. Ask only about the parts the user wants to change, then add a dated line to section 10.
2. Ask every question in `references/interview-questions.md`, one at a time, skipping any that setup already answered.
3. Write the full `my-rules.md` from the template and the answers, in the user's own words where you can.
4. **[Checkpoint]** Show the whole file. Ask: "Is this right? Tell me anything to change, or say approve." Repeat until they approve.
5. Save it to `output/my-rules.md`.
6. Take a dated tracker snapshot. On the spreadsheet, if settings and answers will add up to more than five writes, also back up the file (`tracker-access.md`, "Backups and snapshots"). Show the `settings` values (`references/settings-and-answers.md`) and save them after the user says yes.
7. Offer the starter answer bank. If yes, ask one item at a time, and save the confirmed items as `settings-and-answers.md` says.
8. Take an after snapshot and run the check with `--stage intake`.
9. **Resume.** If `my-setup.md` says "use mine", confirm the file is saved as `stages/07-resume/output/resume.pdf`, and offer to make the text copy `stages/07-resume/output/resume.md` from it for filling forms: read the PDF yourself (or, if you cannot read it, ask the user to paste its text), keep their wording, show the copy before saving, and do not rewrite or critique the resume. Otherwise tell the user to say "Build my resume" when they are ready.
10. **Employers.** Ask: "Do you already have a list of employers you want to work for?" If yes, add them as `adding-employers.md` says. If no, or they want more, tell them they can say "Suggest employers that fit my background".
11. Ask once what this session taught (`lessons.md`) and add any lesson the person approves. Then end by suggesting the next step in one or two lines (`next-steps.md`, "After the interview"). Suggest only; do not start it. Point them to `shared/prompts.md` for everything else they can say.

### Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 3 | The complete `my-rules.md` | Approve, or what to change |
| 6 | The `settings` values | Save, or what to change |
| 7 | Each answer bank item | Save, change or skip |

### Audit

| Check | Pass Condition |
|-------|---------------|
| Questions | Every question was asked, one at a time, or the user skipped it |
| Approval | The user saw the complete `my-rules.md` and said approve before it was saved |
| Settings | `settings` was saved after the user said yes, and `check_tracker.py --stage intake` passes |
| Safety | No password, ID number or bank detail was asked for or stored |
| Lessons | The person was asked once what the session taught; only approved lessons were added |
| Next step | The session ended with the next thing to say, in quotes |

### Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| The user's rules | `output/my-rules.md` | Markdown, in the template's shape, approved by the user |
| Settings record | Tracker, `settings` | One row, id `main` |
| Starter answer bank | Tracker, `answers` | One row per confirmed answer, if the user wanted them |

---

<!-- stages/00-intake/references/interview-questions.md -->

## Interview questions

The intake interview, in order. The number in brackets is the section of `my-rules.md` the answer fills.

### How to ask

- Ask **one question at a time**. Wait for the answer before asking the next one.
- Keep each question short. Give one or two examples so the user knows what kind of answer fits. Examples should not lead the user toward any industry.
- **If an answer is already known** (for example from setup), do not ask it again. Say in one line what you have and move on.
- If an answer is vague, ask one follow-up. If it is still vague, write down what they said and move on.
- Never guess an answer. If the user skips a question, write "None" or "Not decided" in that line.

### Target roles

1. "What kind of job are you looking for? Name a few titles if you can." [1]
2. "What is the highest job title you have held, and did you lead or manage anyone? How many, and what did you own (accounts, budget, projects)?" Ask question 17 (years of experience) now too. From both, work out their current level as `shared/career-direction.md` says, show it with the reason, and let them correct it. [1]
2a. "Where do you want to go next: the next level up, the same level somewhere better, or a new field? Name the role if you can." Career changers: also work out their starting level in the new field. [1]
2b. "Would you take a step down in level? If so, when (for example only to change fields, or only above your pay floor)?" For someone looking for their first job, skip this and write "no (entry level)". [1]
3. "Are there roles with similar titles that you do not want? For example, a title that sounds right but is really support or admin work." [1]
4. "In a sentence or two, what does a good fit look like to you?" [1]

### Place

5. "Where do you live? A city or metro area is enough." [2]
6. "Which of these work for you: jobs in your home metro, a territory based out of your home metro, a territory covering several states, fully remote?" [2]
7. "For remote jobs, are there limits? For example, some remote jobs only hire in certain states." [2]
8. "Are any nearby cities OK only if the pay is high enough? If so, which cities and what pay?" [2]
9. "Would you move for the right job? If yes, where?" [2]

### Pay

10. "What is the lowest pay you will accept? Say whether that is per year or per hour." [3]
11. "Does that floor count base salary only, or base plus commission or bonus?" [3]
12. "When a form lets you type your pay expectation, how do you want it worded?" [3]
13. "When a form needs a single number, what number?" [3]

### Industries and products

14. "Which industries or kinds of products are you most interested in?" [4]
15. "Which industries or products are out for you, and why?" [4]
16. "Of the ones that are out, which should be hidden in your tracker entirely?" These become `excludedIndustries`. [4]

### Experience

17. "How many years of experience do you have in the kind of work you are targeting? What counts?" [5]
18. "If a posting asks for more years than you have, how far would you still apply? For example, up to two more years." [5]
19. "What licenses or certifications do you hold?" [5]
20. "What degrees do you hold, and in what field?" [5]

### Hard noes

21. "Anything that is an automatic no? For example: part-time, contract, commission only, night shifts, heavy travel, a license you would need before starting." [6]

### Employers

22. "Are there employers you want tracked but not applied to yet?" These go on hold. [7]
23. "Who must never be contacted? Your current employer goes here if you have one." [7]
24. "Any employer that only posts jobs on one job site (like Indeed) and has no job board of its own?" [7]

### Autonomy

25. "When I sweep employer sites, should I add fitting listings on my own, or ask you before writing anything?" [8]
26. "When a posting is a close call, should I decide by your rules, or bring every close call to you?" [8]
27. Tell the user, do not ask: "For applications, I fill in the form and you review it before anything is submitted. You can turn on auto-submit for one session by writing it out, but it is off by default." [8]
28. "Do you want hiring-manager outreach drafts? I only draft. You send everything yourself." [8]
29. Do not ask about email: setup already checked for a connector. If `my-setup.md` names one, write "Mailbox check: on, with [connector]". If it says "none", write "Mailbox check: pasted emails only, until a connector is added" and tell the user that in one line. [8]

### Writing style

30. "How should anything written for you sound? For example: short and direct, warm, formal. Any words or habits to avoid?" [9]

---

<!-- stages/00-intake/references/my-rules-template.md -->

## My rules

<!-- The intake interview fills this in and saves it as stages/00-intake/output/my-rules.md.
     Every line in [brackets] is replaced with the user's answer. Lines that do not apply say "None". -->

Last updated: [YYYY-MM-DD]

### 1. Target roles

- Roles I want: [titles or kinds of role]
- Current level: [L1 to L9 from shared/career-direction.md, with the reason; career changers: old-field level and new-field level]
- Next step: [the level and role they want next, in their words]
- Step down allowed: [no / yes, and when]
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
- Fit calls: [autonomous / bring me every close call]
- Apply: Human review before every submission. Auto-submit is off unless I turn it on for one session in writing.
- Outreach: [off / drafts when I start it by name]
- Mailbox check: [pasted emails only / on, using my email connector]

### 9. Writing style

- [for example "short and direct, no exclamation marks, sign off with my first name only"]

### 10. Dated changes

<!-- Newest first. Each line: YYYY-MM-DD what changed. -->
- [YYYY-MM-DD] Rules created by the intake interview.

---

<!-- stages/00-intake/references/settings-and-answers.md -->

## Settings record and starter answer bank

What the intake writes to the tracker after `my-rules.md` is approved. Column meanings are in `shared/tracker-columns.md`.

### The settings record

The record's id is `main`. In the spreadsheet it already exists (the template has it), so **update** that row (`tools/sheet.py` op `update`, id `main`). In a new artifact tracker it does not exist yet, so create it with `set`. Show the values first and save after the user says yes.

- `tierA`, `tierB`, `tierC`: what each employer tier means for this user. Work them out from section 2 (Place) of `my-rules.md`; the user approves them with the other settings. Default when the place rules give nothing more: A "Employer based in my home metro", B "Employer elsewhere with jobs open to my area", C "Other allowed place" (for example a nearby city allowed only above a pay bar). For someone who works only remotely: A "Remote roles open to my state, employer nearby or in my state", B "Remote roles open to my state, employer elsewhere", C "Remote roles with limits I need to check".
- `industryOrder`: the "in" industries, most wanted first.
- `excludedIndustries`: from interview question 16.
- `roleFamilies`: the kinds of role from questions 1 to 3, with a `*` after the ones that are targets.
- `tracks`: leave as `Main` unless the user is searching for two quite different kinds of role.
- `priorities`: leave as `High; Medium; Low; On hold` unless the user asks.

If the tracker does not exist yet, keep these values in the chat, tell the user, and write them the first time the tracker exists.

### Starter answer bank

Ask: "Do you want to start your answer bank now? It holds the answers application forms ask for again and again, so you are not asked each time. You can also fill it later." If yes, ask one item at a time, in this order. The user may skip any item. Save the confirmed items together in one write after the last one (spreadsheet: one `tools/sheet.py apply` changes file), or save what is confirmed so far if the session has to stop early.

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

---

<!-- stages/01-sweep/CONTEXT.md -->

## Stage 01: Sweep

Check employers for new listings, and confirm that listings already in the tracker are still open. The user starts every sweep. Nothing here runs on a schedule.

### Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| User | The session's scope | Employers, count, or listings to recheck | What this sweep covers |
| Stage 00 | `../00-intake/output/my-rules.md` | Full file | The user's rules |
| Shared | `../../shared/rules.md` | Full file | Rules for every stage |
| Shared | `../../shared/my-setup.md` | Full file | Tracker kind and location, Python command, browser, email connector |
| Shared | `../../shared/tracker-access.md` | Full file | Reading, writing, backups and the check |
| Shared | `../../shared/recurring-mistakes.md` | Full file | Read before any tracker write |
| Shared | `../../shared/adding-employers.md` | Full file | Only when the user asks to add employers |
| Shared | `../../shared/helpers.md` | Full file | Only if you use research helpers |
| Shared | `../../shared/next-steps.md` | "After a sweep or a fit call" | What to suggest when the session ends |
| Shared | `../../shared/lessons.md` | Full file | Learning from this session |
| Tracker | `companies`, `coverage`, `listings`, `settings` | All rows in scope | The target list and what is known |
| Stage 02 | `../02-fit-review/CONTEXT.md` | Full file | Run for every new posting |
| Reference | `references/sweep-procedure.md` | Full file | Scope, reading, coverage rows, rechecks, budget |
| Reference | `references/board-techniques.md` | Full file | Ground rules, location traps, signs a posting is gone |
| Reference | `references/board-platforms.md` | The section for each board | Read before reading that board |

### Process

1. Take a tracker snapshot before writing anything. If this run may write more than five rows on the spreadsheet, take a backup too (for the artifact tracker the before snapshot counts).
2. If the user asked to add employers, add them as `adding-employers.md` says.
3. Agree the scope with the user (`sweep-procedure.md`, "Scope").
4. For each employer in scope, read its own board (`sweep-procedure.md`, "Reading one employer").
5. Run stage 02 on every new posting.
6. Update the employer's `coverage` row.
7. Recheck each listing in scope at To apply (`sweep-procedure.md`, "Rechecking listings").
8. Take an after snapshot and run the check with `--stage sweep`. Fix anything it reports.
9. Run the audit below, then save the report.
10. Ask once what this session taught (`lessons.md`) and add any lesson the person approves. Then end by suggesting the next step in one or two lines (`next-steps.md`, "After a sweep or a fit call"). Suggest only; do not start it.

### Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 2 | Employers to add, with their careers sites | Which to add |
| 3 | The proposed scope | Go, or a different scope |

Stage 02 follows the user's autonomy lines and asks before writing when they say so. Paths in stage 02's file are relative to `stages/02-fit-review/`.

### Audit

| Check | Pass Condition |
|-------|---------------|
| Coverage | Every employer in scope has a dated coverage entry, or is listed in the report as not reached |
| Manual employers | Every one says which kind of failure it was (bot check, browser refusal or structural absence) |
| New listings | Every one passed stage 02 and has all its required columns |
| Protected listings | No listing at Applied, Followed up, Interview or Offer was changed (`check_tracker.py`) |
| Evidence | No status change rests on aggregator evidence |
| User's notes | `yourNotes` untouched on every row (`check_tracker.py`) |
| Backup | On the spreadsheet, taken if more than five rows were written |
| Lessons | The person was asked once what the session taught; only approved lessons were added |
| Next step | The session ended with the next thing to say, in quotes |

### Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| New listings | Tracker, `listings` | Rows at To apply, from stage 02 |
| Coverage | Tracker, `coverage` | One updated row per employer touched |
| Expired or filled listings | Tracker, `listings` | Status changed, with a history entry |
| Sweep report | `output/[YYYY-MM-DD]-sweep-report.md` | Markdown, as `sweep-procedure.md` "The report" lists |

---

<!-- stages/01-sweep/references/board-platforms.md -->

## Board platforms: platform by platform

How to read each kind of employer job board. The ground rules, location traps and signs a posting is gone are in `board-techniques.md`. Add what a session learns here (with the user's OK). Edit the platform's section in place. Never add employer names, the user's details or dates.

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
- Find the token in the careers page's embed script: `boards.greenhouse.io/embed/job_board/js?for=<token>`, in the page's job links (`job-boards.greenhouse.io/<token>/jobs/<id>`), or in its network requests to `boards-api.greenhouse.io/v1/boards/<token>/`. Tokens are often not the company's obvious name.
- The same job number can be shared by copies of a job in several locations; log the job's own id.
- A `job-boards.greenhouse.io` job link that redirects to the employer's general careers page means the job is closed.
- Some boards turn over fast: a job can vanish between two reads minutes apart. Confirm twice before marking it gone.

### Ashby

`api.ashbyhq.com/posting-api/job-board/<slug>?includeCompensation=true` returns the whole board with plain-text descriptions, `isListed` and `publishedAt`. Fetch it from a tab on `api.ashbyhq.com`.

- The feed's `location` can be an office label such as "HQ" on a remote job. Read the posting's own "Location:" line in the description, and `secondaryLocations`, before judging place.

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

---

<!-- stages/01-sweep/references/board-techniques.md -->

## Board techniques: how to read job boards

How to find and read postings on employers' own job boards, Learned over a few hundred real employer boards. Platform-by-platform notes are in `board-platforms.md`.

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

### Signs a posting is gone

Only the employer's own site decides. These are reliable signs:

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

---

<!-- stages/01-sweep/references/sweep-procedure.md -->

## Sweep procedure

The detail behind each step of the sweep. Board-by-board reading is in `board-techniques.md` and `board-platforms.md`.

> **Site terms.** LinkedIn and some job boards forbid automated access in their terms. A sweep reads employers' own career sites only. It never opens LinkedIn and never uses an aggregator as a source of truth. The user is responsible for following each site's terms.

### Scope

- From the user: which employers, how many, or which listings to recheck. If the user gives no scope, offer: "the 10 employers swept longest ago, plus a recheck of every listing at To apply".
- Skip employers whose `industry` is in `settings.excludedIndustries` unless `keepAnyway` is yes.
- Work only inside the target list. Employers you happen to find along the way go on a "candidates" list in the report, not into the sweep.
- `coverage` is the checkpoint: a sweep that stopped part way resumes at the first employer whose `sweepState` is `not swept` or `partial`.

### Reading one employer

1. Open its own careers site or applicant tracking system. Never sign in, never create an account. Use the board's section in `board-platforms.md`.
2. **Search by department, not only by title.** Open the board's categories that hold the user's target roles (for example Sales, Customer Service, Operations, Finance) and read every entry to mid level posting in them; titles vary too much between employers for a title search alone. Then read every posting that could match the user's target roles, with its requirements in full, and its **own** location text (many boards misreport location).
3. Large boards: read them in parts and record how far you got in `sweepProgress`, with `sweepState` `partial`.
4. A posting is new if no row in `listings` has its job number, or its title and location at that employer.
5. **If the site will not load,** first try the known workarounds (the board's public feed, an alternate host, the sitemap). If they fail, do not try to get past anything. Set `sweepState` to `manual`, `result` to `LEAD`, and start `detail` with today's date and "MANUAL:" plus the link and which kind of failure it was: a **bot check** (the user can usually open it in their own browser), a **browser refusal** (the browser tool will not open the site), or a **structural absence** (the employer has no postings of its own). Never remove an employer from the target list because its site was hard to reach.

### The coverage row

Update the employer's `coverage` row, or create it if the employer has none yet (same `id`, `company` and `industry` as in `companies`):

- `sweepDate`: today.
- `sweepState`: `done`, `partial`, or `manual` (see "Reading one employer" step 5).
- `result`: `HIT` if a listing was added, `NONE` if nothing fit, `LEAD` if something needs the user.
- `detail`: a dated line at the start (`YYYY-MM-DD ...`, or `YYYY-MM-DD MANUAL: ...` for a manual employer), with older text kept after "Earlier:".
- `skipped`: one line per skipped posting: title, req id, reason.

### Rechecking listings (status To apply only)

1. Open the posting on the employer's own site.
2. **Gone:** a "no longer available" or filled message; HTTP 410; on Workday a 403 on the job plus no match for the job number on the board; a Greenhouse job link that redirects to the general careers page; the job number missing from a search of the whole board while the page will not load. Set `status` to `expired` (or `filled` when the employer says filled) and append a `history` entry naming exactly what showed it.
3. **Not proof on its own:** a 404 on a saved address (job addresses change with titles: search the job number first); a slow or "initializing" page (wait and reload); one of two pages for the same job showing it closed (trust the page with an explicit closed or filled message); an aggregator showing it closed; the employer rejecting the user (the posting can stay live). Look again before changing anything.
4. **Fast-turnover boards:** a job can vanish between two reads minutes apart. Confirm twice.
5. If the employer's site cannot be read, leave the status alone and report the listing as unconfirmed.
6. Never touch a listing at Applied, Followed up, Interview or Offer, even if its posting is gone.

### Budget

Stop starting new employers at about 150 tool calls in the main session, so there is room to check, write and report. Record where you stopped in `coverage`; the next sweep resumes there.

### The report

Employers checked, new listings, listings expired or filled, manual employers, anything unconfirmed, candidates found along the way, and calls for the user.

---

<!-- stages/02-fit-review/CONTEXT.md -->

## Stage 02: Fit review

Decide whether one posting goes in the tracker. A sweep runs this for every new posting. The user can also hand you a posting link and ask for a fit call.

### Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| User or sweep | The posting, read on the employer's own site, or pasted by the user | Title, location detail, pay, requirements, work type | What is being judged |
| Stage 00 | `../00-intake/output/my-rules.md` | Full file | The user's rules |
| Shared | `../../shared/rules.md` | Sections 1 to 6 | The checks |
| Shared | `../../shared/career-direction.md` | Full file | Placing postings on the ladder, the step, `why` prefix, priority |
| Shared | `../../shared/my-setup.md` | Full file | Tracker kind and location, Python command, browser, email connector |
| Shared | `../../shared/tracker-access.md` | Full file | Reading, writing and the check |
| Shared | `../../shared/recurring-mistakes.md` | Full file | Read before any tracker write |
| Shared | `../../shared/adding-employers.md` | Full file | When the employer is not on the target list |
| Shared | `../../shared/next-steps.md` | "After a sweep or a fit call", "After a close-call decision" | What to suggest when the session ends |
| Shared | `../../shared/lessons.md` | Full file | Learning from this session |
| Tracker | `listings`, `companies`, `settings`, `coverage` | That employer's rows | Duplicates, spelling, settings lists |
| Previous runs | `../01-sweep/output/`, `output/` | The latest report | Close calls waiting for a decision |
| Reference | `references/fit-outcomes.md` | Full file | What to write for each result |

### Process

1. Take a tracker snapshot, unless a sweep already took one this session.
2. **Employer not on the target list** (for example the user pasted a link): ask whether to add it. If yes, add it as `adding-employers.md` says, then go on. If no, give the fit call in chat only and write nothing.
3. Check in this order. The first failure decides:
   1. **Duplicate?** Same req id, or same title and location at the same employer, already in `listings`: stop, nothing to add.
   2. **Live on the employer's own site?** If the site shows it gone: no. If you cannot open the site (no browser, or the person pasted the text), judge it on the pasted text, say "not confirmed live", and ask for the employer's link before writing a listing.
   3. **Target role and level?** Not one of the user's target roles, one of their "out" roles, a step down they do not allow, or out of reach: no. A stretch, a track switch, or a level that is unclear between two steps is a close call (rules 1, `career-direction.md`).
   4. **Industry and product?** An "out" industry, or an excluded industry without `keepAnyway`: no (rules 1).
   5. **Place?** Fails the user's place rules: no (rules 4).
   6. **Pay?** Under the floor: no. No posted pay: decide plausibility and write the reasoning (rules 2).
   7. **Hard requirements?** License before hire, a specific degree the user lacks, any hard no in the user's rules: no. Required years inside the user's stretch never fail it on their own (rules 3).
   8. **On-hold employer?** Add the listing, set `priority` to `On hold`, and say so in `why`.
4. Follow the user's autonomy lines in `my-rules.md`: if they want to be asked before listings are written, show each result and wait for their yes before writing. "Bring me every close call" applies only to close calls; clear fits are written as usual.
5. Write the result as `references/fit-outcomes.md` says: a new listing, a skipped line, or a report item for the user.
6. If no sweep is running, take an after snapshot and run the check with `--stage fit`.
7. If no sweep is running: ask once what this session taught (`lessons.md`) and add any lesson the person approves, then end by suggesting the next step (`next-steps.md`, "After a sweep or a fit call"). Inside a sweep, the sweep does this.

### Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 2 | Whether to add an employer not on the target list | Add it, or a chat-only fit call |
| 3 | Each result, when the user's autonomy lines say to ask | Write it, or not |
| 5 | Close calls that depend on taste, in the report | Apply or skip |

### Audit

| Check | Pass Condition |
|-------|---------------|
| Every posting | Ends as a new listing, a skipped line, or a report item for the user |
| No Review fit | No listing was created at Review fit; close calls are in the report instead |
| Columns | Every new listing has every column in `fit-outcomes.md`, including `postingText`, and a unique `id` |
| Check | `check_tracker.py` passes (`--stage fit`, or the sweep's own check) |
| Lessons | The person was asked once what the session taught; only approved lessons were added |
| Next step | The session ended with the next thing to say, in quotes |

### Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| New listing | Tracker, `listings` | One row at To apply |
| Skipped line | Tracker, `coverage.skipped` | Title, req id, reason |
| Fit report | Inside a sweep: the sweep report. Run alone: `output/[YYYY-MM-DD]-fit-report.md`, always | Each posting and its result; close calls in the seven-part shape in `fit-outcomes.md` |

---

<!-- stages/02-fit-review/references/fit-outcomes.md -->

## Fit outcomes

What to write for each result of a fit review. Column meanings are in `shared/tracker-columns.md`.

### Pass: a new listings row

- `id`: `<company-slug>-<req id or short title slug>`, lowercase, letters, numbers and hyphens only. Check no other row uses it.
- `company`: spelled exactly as in `companies`.
- `title`, `location` (the posting's own location detail), `url` (employer's own site), `reqId`, `industry`, `posted` (date as shown, or blank).
- `pay`: the posted pay as written, or "not posted".
- `why`: starts with the career step (for example "Step up (L3 to L4):", "Same level (L3):", "Stretch (L4 to L6):" or "Track switch (L6 to IC L6):", `shared/career-direction.md`), then one or two sentences on the fit, any reach (years, industry), and anything the user should know.
- `teaches`: what the role would teach the user, starting "Stated:" (the posting says so), "Not stated." or "Not read." When it builds toward their next step, say how.
- `family`: one of `settings.roleFamilies`, written without the `*`. `track`: one of `settings.tracks`.
- `priority`: `High` (clear fit, pay at or above the floor), `Medium` (fits with a reach), `Low` (fits on paper, weaker on taste or pay), or `On hold`. A step up that matches the user's next step moves up one band (Low to Medium, Medium to High), but never to High when `why` names a years reach. A stretch the person chose to apply to is Medium.
- `postingText`: the posting's full text, copied from the employer's own page (title, location, pay, duties, requirements). This lets later stages work after the posting is taken down. If the page is too long, keep at least the duties, requirements and pay.
- `status`: `To apply`.
- `history`: `YYYY-MM-DD added from the employer's own site by fit review.` If it was judged on pasted text: `YYYY-MM-DD added from pasted posting text by fit review; not confirmed live on the employer's site.`, and `why` ends with "Not confirmed live."
- `yourNotes`: leave empty.

### Fail

One line in the employer's `coverage.skipped`: title, req id, reason. Run alone, for an employer with no `coverage` row: record the skip only in the fit report, and never create a coverage row outside a sweep (a coverage row means the employer was swept).

### A matter of taste, not a rule

For example a commission-only role when the user's rules say nothing about commission. Do not add it. List it in the session report for the user, in this shape, so they can decide from it alone:

1. **Flag:** what made it a close call. For an unclear level, name both levels and what points to each.
2. **Posting says:** the exact requirement or fact, quoted short, marked required or preferred.
3. **You have:** how the user's background compares, from the resume, the answer bank and the experience section of `my-rules.md` only.
4. **Teaches:** what the role would build.
5. **Pay and next step:** posted pay or "not posted", and any named next role.
6. **Lean:** Apply or Skip, with one sentence of reasoning.
7. **Decide:** the one question the user needs to answer.

### The person decides a close call

When the person answers a close call (in the session or a later one), record it, so it is never asked again. Take a snapshot first and check with `--stage fit` after.

- **Apply:** first re-open the posting on the employer's own site to confirm it is live and copy `postingText` (if it cannot be opened, ask for the employer's link first, as in the CONTEXT step on pasted postings, and record "not confirmed live"). Then write the listing as in "Pass", with history `YYYY-MM-DD added after the user's close-call decision` plus `; not confirmed live on the employer's site` when it was judged on pasted text, ending with a period. If the employer has a `coverage` row, set its `result` to `HIT`, unless another close call there is still waiting (then leave `LEAD`).
- **Skip:** if the employer has a `coverage` row, add `title, req id: skipped by the user's decision YYYY-MM-DD` to its `skipped` and set `result` to `NONE` unless something else there is still waiting. Keep every earlier line of `skipped` when you add one (read the cell fresh and write it back with the new line at the end), and add a dated line to the start of `detail` saying the close call was decided, keeping older text after "Earlier:" (`shared/tracker-columns.md`). If it has no coverage row, do not create one: add `YYYY-MM-DD decided: skip` under that close call in its report instead (with no folder, give the updated report as a download so the mark is kept).

A close call that is already a listing and that the person now drops is a status change to `Closed`: do it as a direct request with its own snapshot and a `--stage user` check (`shared/tracker-access.md`, "Direct requests"), not inside the `--stage fit` check.

For an unclear level, use the level the person chose in the `why` prefix.

A close call counts as decided when its req id (or, with none, its title and location) is in `listings` or `coverage.skipped`, or its report marks it decided.

### A closed listing that is live again

Do not reopen it. List it in the report. The user decides.

---

<!-- stages/03-apply/CONTEXT.md -->

## Stage 03: Apply

Fill in applications for listings at To apply, live with the user. **The user reviews every application before it is submitted.**

### Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Stage 00 | `../00-intake/output/my-rules.md` | Full file | The user's rules and writing style |
| Stage 07 | `../07-resume/output/resume.pdf` | The file | The resume to upload (or the user's own file saved there at setup) |
| Stage 07 | `../07-resume/output/resume.md` | Full file | Resume text for form fields |
| Stage 07 | `../07-resume/output/resume-[listing-id].pdf` | Only if the listing's history names it | An approved tailored resume |
| Shared | `../../shared/rules.md` | Sections 5 to 10 | On-hold employers, evidence, status rules, autonomy, safety, writing |
| Shared | `../../shared/my-setup.md` | Full file | Tracker kind and location, Python command, browser, email connector |
| Shared | `../../shared/tracker-access.md` | Full file | Reading, writing and the check |
| Shared | `../../shared/recurring-mistakes.md` | Full file | Read before any tracker write |
| Shared | `../../shared/answer-bank.md` | Full file | How to use the answer bank |
| Shared | `../../shared/next-steps.md` | "After applying" | What to suggest when the session ends |
| Shared | `../../shared/lessons.md` | Full file | Learning from this session |
| Tracker | `listings`, `answers`, `companies` | Listings at To apply; all answers; `onHold` | What to apply to, the answers, and employers on hold |
| Reference | `references/apply-procedure.md` | Full file | Auto-submit, upload order, filling, review, recording |
| Reference | `references/application-techniques.md` | Full file | How forms behave, upload methods, legal text, walls |
| Reference | `references/application-platforms.md` | The platform's section | Read before each form |
| Reference | `references/claude-in-chrome-setup.md` | Full file | Only if Claude in Chrome is not connected |

Apply in **Claude in Chrome** when it is connected. It can upload files; the built-in browser pane cannot.

### Process

1. Take a tracker snapshot, once for the whole session. Then pick the next listing (`apply-procedure.md`, "Order of work").
2. **Still live?** Open the posting on the employer's own site. If it is gone, set `expired` or `filled` with a history entry and move on. With no browser at all, follow `apply-procedure.md`, "No browser Claude can use", for steps 2 to 8.
3. Save the posting text and re-check the fit (`apply-procedure.md`, "Before the form").
4. Upload the resume, trying the methods in order, and check the upload on the page.
5. Fill the form from the answer bank and the resume. Quote legal text to the user. Hand every wall to the user.
6. **[Checkpoint]** Show the review summary and stop.
7. Submit only on the user's "submit" (or under auto-submit turned on in writing this session).
8. Record the result: `Applied`, `appliedDate`, and the history entry with `upload: <method>`. Add any new account username to `answers`.
9. Pick the next listing and repeat from step 2, as long as the user wants. Do not take a new snapshot.
10. Take an after snapshot and run the check with `--stage apply`.
11. Run the audit below, then save the report.
12. Ask once what this session taught (`lessons.md`) and add any lesson the person approves. Then end by suggesting the next step in one or two lines (`next-steps.md`, "After applying"). Suggest only; do not start it.

For a **dry run**, stop at step 6 and follow `apply-procedure.md`, "Dry run", then do steps 10 to 12.

### Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 3 | A posting that no longer fits | Apply anyway or skip |
| 5 | Legal text, walls, any question the answer bank does not cover, any cover letter | Their answer, their wall step, their sign-off |
| 6 | The review summary of every answer and the upload | "Submit", changes, or skip |

### Audit

| Check | Pass Condition |
|-------|---------------|
| Review | Every submitted application was reviewed by the user (or under auto-submit turned on in writing this session), with a confirmation and a history entry |
| Posting text | Every listing worked has `postingText` saved |
| Upload | Every upload was checked on the page (right file name), and every auto-filled field was checked against the answer bank |
| Safety | No password, code or ID number was typed by the session or written anywhere. No LinkedIn or cloud-account import was used |
| Cover letters | None went out without the user's sign-off |
| Check | `check_tracker.py --stage apply` passes, and `yourNotes` is untouched |
| Lessons | The person was asked once what the session taught; only approved lessons were added |
| Next step | The session ended with the next thing to say, in quotes |

### Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Applied listings | Tracker, `listings` | Status Applied, `postingText`, `appliedDate`, history with the upload method |
| Blocked listings | Tracker, `listings` | Left at To apply, with a history entry naming the block |
| Apply report | `output/[YYYY-MM-DD]-apply-report.md` (a dry run saves `output/[YYYY-MM-DD]-apply-dry-run.md` instead) | What went through, what is blocked and why, what needs the user |

---

<!-- stages/03-apply/references/application-platforms.md -->

## Application platforms: form by form

How each platform's application form behaves. General methods are in `application-techniques.md`. Add what a session learns here (with the user's OK). Edit the platform's section in place. Never add employer names, the user's details or dates.

### Greenhouse

- Usually no account and no CAPTCHA. Form address: `job-boards.greenhouse.io/embed/job_app?for=<board>&token=<job id>`. It works even when the company wraps the board in its own site.
- Read the posting from `boards-api.greenhouse.io/v1/boards/<board>/jobs/<id>` (open it in the tab; a fetch from the form page is blocked).
- Text inputs take the setter; **textareas need real typing**.
- **Phone with a required country:** first click the Country control, type the country, click the option, then type the phone.
- react-select dropdowns: one real click on the control, wait about half a second, then click the `.select__option` with matching text. Read the result from `.select__single-value`. Do not call React internals: that can wipe the attached resume.
- Attach the resume last and check it is still showing before Submit.

### Lever

No account. Upload the resume first; it fills name, email, phone and current employer. An invisible CAPTCHA usually does not challenge; a visible one is a wall.

### Ashby

No account. The phone must be typed for real. Yes/No buttons and radios need real clicks; check each took. Location and source are comboboxes: click, type, click the option. Usually ends with an agreement radio: read it.

### Workday

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

### iCIMS

- Login, password and CAPTCHA (often hCaptcha at "Submit profile") are the user's.
- The profile form sits in a same-origin frame (`iframe#icims_content_iframe`): work in its `contentDocument`, and attach the resume with that frame's own `File` and `DataTransfer`.
- Uploading the resume reloads the frame and can wipe fields: re-check everything after.
- Lazy dropdowns: dispatch mousedown, mouseup and click on the dropdown anchor, type in its search box if it has one, then click the result item.
- Follow-up forms (disability, veteran, acknowledgements) can load in a cross-origin frame. Complete them **inside the application tab** where possible; on some boards, completing them in a separate tab leaves the application "incomplete".
- Sessions time out after roughly 20 to 30 idle minutes; drafts may keep only some answers.
- **After sign-in, some boards submit an application the moment its apply link opens** (see "Before you start").

### Paylocity

- No account. "Fill out application with my resume" reads the file; check every field, add missing jobs by hand.
- Dropdowns: real click on the control, wait about 2 seconds, click the list item. The acknowledgement checkbox needs a real click. Month/year dates need text insertion.
- Pick the address from its suggestions, then set the start date (picking the address wipes it).
- Some forms require supervisor contact details for every job marked "may contact".

### BambooHR

No account. The state list may need real clicks through a button menu (`find` the control, click, `find` the option, click). Dates: click and type, then Escape. Submit is followed by a CAPTCHA checkbox: the user ticks it.

### Jobvite

No account. Usually several pages: consent, contact and resume, self-identification with a typed name and date, screening questions, then a visible CAPTCHA at send (the user). The file upload tool may refuse the control; attaching by page script works. Next may need a real click.

### Phenom (apply)

- No account on some boards. Read the posting from `phApp.ddo.jobDetail.data.job`.
- Fill every required field before the first Next: once a field is flagged, picking a value may not clear the error until a related field is retyped.
- An invisible CAPTCHA can reject a scripted submit: the user presses Submit. Reloading the apply address restores the draft and fixes buttons left disabled.

### UKG Pro Recruiting and UKG Ready

- UKG Pro: an account at "Apply now" (the user). One long page; the resume reader often puts employer and location in the title.
- UKG Ready on a new employer: no password until "Sign & submit", which asks for a password as the signature (the user). Once a profile exists, the board asks the user to sign in.

### Dayforce

- An account (Dayforce ID) or "apply without an account" on some boards.
- Creating the account: the agree box counts only after both policy links are clicked, and those links can open in the same tab and wipe the form. Have the user open them in a new tab.
- Ant Design form: open selects with a mousedown on `.ant-select-selector`, wait, click the option. Press each section's Update button and read the error messages after each.
- **Next is slow:** click once, wait about 5 seconds, confirm the page number. A double advance can skip a page unanswered.

### ADP Workforce Now and ADP MyJobs

- Sign-in is by a texted or emailed code (the user). One emailed code may never arrive; the text option is often more reliable.
- Radios are web components; source dropdowns and self-identification need real clicks.
- Text inputs on the questions page often register only when typed for real.
- The last step can be an electronic signature: stop there. The user ticks the box, types their name and submits. Some flows have no review page: the last Next submits, so stop before it for the user's review.
- Some legacy ADP flows ask for the last four digits of a Social Security number and a birth date (a "rehire check"): a wall. The user decides.

### Oracle Cloud Candidate Experience

- Often no account; a returning email may get a PIN or emailed code (the user).
- ZIP fields are autocompletes: type the ZIP in two parts so the list filters, then click the matching row.
- Pill-button questions take a script click. Comboboxes: focus, insert the text, wait, click the matching cell.
- The final e-signature can be an employment agreement with arbitration: quote it first.

### SuccessFactors

- An account (the user). Picklists: click the select button, then the matching option inside the list named by the input's `aria-owns`. Dates are calendar widgets that take typed `MM/DD/YYYY`.
- Some flows require the current supervisor's name and title with no "may we contact" choice: raise it with the user.

### Hirebridge, ClearCompany, isolved, Cornerstone, Paycom, Paycor and others

- **Hirebridge:** some boards offer a quick apply with no password; others ask for an existing profile's password (the user). The resume upload reloads the page: upload first.
- **ClearCompany:** no account on a first visit; a second visit to the same job emails a sign-in link (the user). Parsed rows arrive late; wait, then fix. Some forms require a birth date and Social Security number: a wall.
- **isolved Hire:** an account is created for the user after step 2 and a password is asked (the user). A returning email gets a secure code.
- **Cornerstone:** the first application creates a profile with a CAPTCHA (the user); later applications submit directly.
- **Paycom:** values set by script on selects, dates and autocompletes are wiped on submit. Use arrow keys on selects, type dates digit by digit, click autocomplete suggestions, real-click the acknowledgement.
- **Paycor:** plain form; setters work.
- **SmartRecruiters:** may show bot-check questions: the user answers.
- **Conversational (chat) apply flows:** answer from the answer bank; anything new goes to the user.

---

<!-- stages/03-apply/references/application-techniques.md -->

## Application techniques

How application forms behave, platform by platform, and how to fill them correctly. Learned from well over a hundred real applications. Read it before an apply session. Platform-specific notes are in `application-platforms.md`.

Add what a session learns here (with the user's OK): a new platform, a new workaround, a trick that stopped working. Edit the platform's section in place. Never add employer names, the user's details or dates.

### Before you start

- **Read every posting in full before the user creates any account.** Many promising titles turn out, once read, to be senior or out-of-scope roles. Creating accounts for those wastes the user's time.
- **Walls are the user's** (rules 9): accounts, passwords, one-time codes, CAPTCHAs, ID numbers. Fill everything up to the wall, hand the browser over, continue after. **Never read a password field**, and leave password inputs out of every dump of a form's fields.
- **Questions that are always the user's:** assessments and aptitude tests, criminal history and felony questions, whether they would sign a future non-compete, non-solicitation or confidentiality agreement, and any judgement call about their own experience that the answer bank does not cover ("years of comparable experience" with no matching entry, "describe how you use AI"). Fill everything else, bring the tab forward, and let the user answer. Do not read back or log their answer.
- **One tab per application.** Opening a new address in a tab that holds a half-filled form throws the form away. Open each application in its own new tab, and bring it forward when the user has to act in it.
- **Some saved profiles submit instantly.** On some platforms, once the user is signed in, simply opening another job's apply link submits that application from the saved profile, with no form and no review. Treat opening an apply link on such a platform as submitting: do it only after the user has said yes to that specific application ("Review before submit"). Known pattern: some iCIMS boards after sign-in.
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

Upload methods, in the order to try them:

- **Plain file input.** Use the file upload tool on it directly. Never click it: clicking opens the computer's own file picker, which the browser tools cannot see.
- **Button over a hidden input.** The real `input[type=file]` is usually hidden next to the button. Find it with `read_page` (it often shows as a button with type "file"), `find` ("file input for resume"), or a read-only check listing every `input[type=file]` with its id and `accept` value. Upload to that input.
- **Drag-and-drop zone.** There is almost always a hidden file input inside the zone. Upload to it.
- **"Autofill from resume" button.** Find the hidden input behind it and upload there, then check every field it filled.
- **Paste box.** Use the resume text (`resume.md`) and flag it in the review summary.
- **Built-in browser pane.** It has no file upload tool. Switch the application to Claude in Chrome.
- **When the upload tool is refused** ("not a file input") on a control that is a file input inside a custom widget, a page script can attach the file: build a `File` from the PDF's bytes, put it in a `DataTransfer`, assign it to `input.files`, and dispatch `change`. On a few React dropzones, the change only registers through the input's own React handler.

How to tell an upload worked:

- The page shows the chosen file name (or a preview of the resume) next to the control. A different name, a size of 0, or an error means it failed.
- Some forms read the file only on the next page. Check again after moving on.

**Upload order:**

- On forms that **do not** read the resume, upload **last**: some scripted field changes on those forms wipe an attached file. Check the file name is still there before submitting.
- On forms that **do** read it and fill fields, upload **first**, wait for the reading to finish, then correct the fields.

**Resume readers get things wrong.** After any automatic fill, check every work-history entry against the resume text (`resume.md`). Common mistakes:

- employer and job title swapped, or the employer jammed into the title, or the city put in the description;
- dates garbled, or an end date set on the current job;
- bullet points dropped, or the degree set to "Other";
- the phone number copied into the extension field;
- the whole contact line put in the city field;
- parsed rows arriving late and overwriting or duplicating what you typed (wait for the reading to finish first);
- "suggested" skills added that are not on the resume (remove them);
- a re-upload wiping fields such as street address or school.

### Answers forms ask for

Fill from the answer bank. These come up often; the intake collects them:

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
- **LinkedIn:** enter only when required. Some forms validate that it is a real LinkedIn profile address.

### Legal text: read it to the user first

Stop and quote it to the user before anyone ticks the box or types a signature. Seen on real forms:

- arbitration agreements, jury or class-action waivers, invention assignment, pay withholding;
- consent to biometric collection (photos, video, facial geometry, fingerprints);
- consent to AI transcription or AI scoring of interviews;
- broad authorization to contact **any** past or current employer, or every business listed on the application. If the user's current employer is listed, point that out: it conflicts with "never contact your current employer".
- background, credit or criminal check releases.

Plain accuracy statements ("the information is true") are routine, but still mention them in the review summary.

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

<!-- stages/03-apply/references/apply-procedure.md -->

## Apply procedure

The detail behind each step of an application. How each platform's form behaves is in `application-techniques.md` and `application-platforms.md`.

### Auto-submit (off by default)

Auto-submit is off. The user can turn it on for **this session only** by writing a sentence like: "I turn on auto-submit for this session." It turns off when the session ends and never carries over. Even with auto-submit on:

- Every wall (account, password, code, CAPTCHA, ID number) is still the user's to do.
- No cover letter goes out without the user's sign-off on that letter.
- Legal text is still quoted to the user, and **Claude never ticks a legal agreement box itself**. A form with a legal agreement is never auto-submitted: the user ticks the box and submits.
- Anything not covered by the answer bank still goes to the user.
- The review summary is still posted in the chat as you submit.

### Order of work

Listings at To apply, High then Medium then Low, oldest `posted` first within each. Skip `On hold` listings unless the user says go.

### Before the form

- **Save the posting.** Copy the full posting text into `postingText`, even if fit review saved it already, and append: `YYYY-MM-DD posting text saved before applying.` The later copy wins, because postings change. Interview prep depends on this.
- **Re-check the fit** before the user does anything on the site, so they never create an account for a job that does not fit. If it now fails, tell the user and let them decide.
- **One tab per application.** Opening another address in a tab with a half-filled form throws the form away.
- **Apply links that submit on their own.** On some platforms, once the user is signed in, opening another job's apply link submits at once from the saved profile. On such a platform, opening the link **is** submitting: do it only after the user has said yes to that application.

### Uploading the resume

**Which file:** a tailored `resume-<listing id>.pdf` if the listing's history shows one was approved, otherwise `resume.pdf`. Ask once per session for access to the resume folder if you do not have it, then upload the file yourself.

Try these in order. Move to the next only if the one before it failed.

- **a. File upload tool.** Use Claude in Chrome's file upload tool on the form's file input, with the full path to the file. Do not click the input first: clicking opens the computer's own file picker.
- **b. Hidden input.** If the visible control is a button or a drag-and-drop zone, find the hidden `input[type=file]` behind it (with `read_page`, `find`, or a read-only check of the page) and use the file upload tool on it.
- **c. The computer's file picker.** If a click opened it, close it (Escape) and go back to b. Only if b finds no input: if the desktop control tool can work that dialog on this computer, use it to type the full path and confirm. If the tool's access level blocks it, stop this option.
- **d. Paste or type.** If the form offers "paste your resume" or "enter manually", use the text of `resume.md`, and flag it in the review summary.
- **e. Switch browsers.** If the active browser cannot upload at all (for example the built-in browser pane), move this application to Claude in Chrome, if it is connected, and start again at a.
- **Never:** "Apply with LinkedIn" or any LinkedIn import; signing in to Google Drive, Dropbox or any other account to import a file; any step that needs a password, a code or a CAPTCHA. Those are walls.
- **Check after every upload.** The page must show the file name (or a preview), and it must be the file chosen above. If the site filled fields from the resume, check every one against the answer bank and fix any that are wrong.
- **Hand it to the user only when a to e all failed or hit a wall.** Say which options you tried and why each failed.
- **Claude in Chrome not connected** (`my-setup.md`): options a to e cannot run. At the point where the file goes in (last, on forms that do not read the resume; first, on forms that do), tell the user the full path of the file to attach, wait until they say it is attached, check the file name on the page, and record `upload: attached by the user`.

### Filling the form

- Fill from the answer bank and the resume. Invent nothing. For a question the answer bank does not cover, answer only if the answer is plainly safe and true from the resume. Otherwise ask the user. Questions about years of experience always go to the user unless the answer bank has the number.
- **Optional free-text boxes** ("Why are you interested?"): leave blank unless the user's rules say to fill them. If you fill one, draft it in the user's writing style and flag it.
- **Required free-text boxes:** draft them in the user's writing style from the resume and the posting, and get the user's OK on that text before it goes in.
- **Questions answered from the resume** rather than the answer bank: flag each one, and offer to add it to the answer bank. Also offer to save any new answer the user gives during the form (for example a years-of-experience number).
- **Pay:** the answer bank's wording where text is allowed, the single number where one is required.
- **Voluntary questions** (gender, race, veteran, disability): from the answer bank. With no entry, choose "I don't wish to answer" or the closest option, and tell the user.
- **Links** (LinkedIn, portfolio): only when required, from the answer bank. Never open LinkedIn.
- **References:** from the answer bank, in its order. Never the user's current employer, or anyone the user's rules say never to contact.
- **Cover letter:** only if required. Draft it from the resume and the posting, in the user's style. Attach it only after the user signs off on that letter.
- **Legal text** (arbitration, waivers, non-compete, non-solicitation, broad permission to contact past employers): quote it to the user. **Never tick a legal agreement box yourself**, in any mode.
- **Walls** (create account, password, code, CAPTCHA, ID number): fill up to the wall, then hand the browser to the user. Never do the wall step, and never read what they typed. After any click that sends a code, take no more clicks until the user says they are through.

### Review, submit and record

- **Review summary:** every answer on the form, the upload (file name and method), and any auto-filled fields you corrected. Then stop. Submit only when the user says "submit" for this application, or clicks submit themselves.
- **A failed submit:** read the errors, fix the fields, submit **once** more. Repeated failed submits can trigger a code or a lockout.
- **After submitting:** capture the confirmation. Set `status` to `Applied` and `appliedDate` to today. Append a history entry: date, req id, title, company, location, pay if posted, the application system, the username if an account was used (never a password), the confirmation ("confirmation shown", or only the last 4 digits of a long number: the check rejects runs of 13 or more digits), the upload method written exactly as `upload: <method>` (for example `upload: hidden file input`; the check looks for `upload:`), and anything unusual.
- **Blocked while the user is away:** leave the status at To apply and append a history entry naming the exact step that blocked. Never work around it.
- **New accounts:** add to `answers` (topic `Account`, question = the site, answer = the username). Never a password.
- **Something new:** if an upload control behaved in a way `application-techniques.md` does not cover, tell the user and suggest a line to add there. General methods only, never employer names.

### No browser Claude can use

If no browser tool works in this session (for example a chat with no desktop app), Claude cannot open or fill the form. Then:

1. Still save the posting text and re-check the fit, from the posting the person pastes.
2. Give the review summary as a **fill sheet**: every answer for the form, in order, the file to attach, the legal text to read, and the walls that are theirs.
3. The person fills it in and submits in their own browser. Claude never claims to have submitted anything.
4. When they say they submitted, ask for the confirmation (record only "confirmation shown" or the last 4 digits of a long number, as in "After submitting"), then record `Applied` and `appliedDate`, with a history entry that says "submitted by the user from a fill sheet" and `upload: attached by the user`. Until then the listing stays at To apply.

### Dry run

If the user asks for a dry run, go up to the review summary and stop. Write nothing to the tracker except `postingText` and its history line. Close the browser tab without submitting. If the posting could not be checked as still live, say "not confirmed live" in the summary. Then still run the check (`--stage apply`), save the review summary as `output/[YYYY-MM-DD]-apply-dry-run.md`, and suggest the next step.

### The report

What went through, what is blocked and why, and what needs the user.

---

<!-- stages/03-apply/references/claude-in-chrome-setup.md -->

## Claude in Chrome setup

**What it is:** a browser extension for Google Chrome that lets Claude work in the user's own Chrome, connected to the Claude desktop app. Applying needs it because it can upload the resume file. The app's built-in browser pane cannot upload files.

### Install

1. Install Google Chrome if the user does not have it.
2. Install the Claude in Chrome extension from the Chrome Web Store, and sign in to it with the same Claude account as the desktop app.
3. Connect it to the Claude desktop app when the extension asks.

### Verify it works

Check whether tools named `mcp__claude-in-chrome__*` are available in the session. If they are, open a new tab with them and read its address. If they are not, tell the user what is missing in plain words.

### How this workspace uses it

Only the apply stage needs it. Sweeps, research and everything else work in the built-in browser. If it is not connected, applying can still fill forms in the built-in browser, but the user attaches the resume by hand. With no browser at all, applying uses a fill sheet (`apply-procedure.md`, "No browser Claude can use").

Claude in Chrome acts only on sites the user allows. Their own sign-ins stay theirs: never sign out, change settings, or act beyond the application in front of you.

---

<!-- stages/04-outreach/CONTEXT.md -->

## Stage 04: Hiring-manager outreach

**Off unless the user starts it by name in the session** ("run outreach"). Never as a side task of another stage. **Drafts only. The user sends every message.**

### Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| User | "Run outreach", in this session | The request | Nothing runs without it |
| Stage 00 | `../00-intake/output/my-rules.md` | Pay, place, employers (never-contact list), autonomy, writing style | Which listings qualify, who never to contact, and how drafts sound |
| Stage 07 | `../07-resume/output/resume.md` | Full file | Facts used in messages |
| Shared | `../../shared/rules.md` | Sections 7 to 10 | Status rules, autonomy, safety, writing |
| Shared | `../../shared/my-setup.md` | Full file | Tracker kind and location, Python command, browser, email connector |
| Shared | `../../shared/tracker-access.md` | Full file | Reading, writing and the check |
| Shared | `../../shared/recurring-mistakes.md` | Full file | Read before any tracker write |
| Shared | `../../shared/next-steps.md` | "After outreach" | What to suggest when the session ends |
| Shared | `../../shared/lessons.md` | Full file | Learning from this session |
| Tracker | `listings`, `companies` | Qualifying listings | What to research |
| Reference | `references/outreach-rules.md` | Full file | Qualifying listings, sources, confidence, drafts |

### Process

1. Take a tracker snapshot.
2. Count the qualifying listings (`outreach-rules.md`) and tell the user the number before any research.
3. Work them in order: highest pay first, home metro before remote, 10 per session unless the user says otherwise.
4. Find the likely hiring manager from web search and the employer's own pages only. Rate the confidence.
5. Draft the connection note and the longer message in the user's writing style.
6. Save the outreach columns and one history line per listing worked.
7. Take an after snapshot and run the check with `--stage outreach`.
8. Run the audit below, then save the report.
9. Ask once what this session taught (`lessons.md`) and add any lesson the person approves. Then end by suggesting the next step in one or two lines (`next-steps.md`, "After outreach"). Suggest only; do not start it.

### Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 2 | How many listings qualify | Go, a smaller set, or stop |
| 5 | The drafts, in the report | Whether and how to send each one (the user sends) |

### Audit

| Check | Pass Condition |
|-------|---------------|
| Started by name | The user started this stage by name in this session |
| No LinkedIn, no sending | No LinkedIn page was opened and nothing was sent |
| Length | Every connection note is under 300 characters and every message under 90 words |
| Style | No em dashes or en dashes in any draft |
| Columns | Only the outreach columns and history were written (`check_tracker.py --stage outreach`) |
| Lessons | The person was asked once what the session taught; only approved lessons were added |
| Next step | The session ended with the next thing to say, in quotes |

### Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Outreach drafts | Tracker, `listings` outreach columns | Contact, confidence, two drafts per listing |
| Outreach report | `output/[YYYY-MM-DD]-outreach-report.md` | Each contact, confidence, and anything the user should know (wrong place, posting closed) |

---

<!-- stages/04-outreach/references/outreach-rules.md -->

## Outreach rules

A short, specific note to the person who runs the team can get an application read by someone who decides. This stage finds that person from public sources and drafts the note. The user decides whether and how to send it.

> **Site terms.** LinkedIn and some job boards forbid automated access in their terms. Outreach never automates LinkedIn in any way: no scraping, no automated profile visits, no messages, no opening linkedin.com pages. It uses web search and the employer's own pages only. The user is responsible for following each site's terms.

### Which listings qualify

- Status To apply (any date); Applied within the last 30 days (by `appliedDate`); Rejected within the last 30 days, only if the posting is still open on the employer's own site.
- The level the user's rules name for outreach. If they name none, use mid level and up.
- Pay at or above the user's floor. Listings with no posted pay are included, marked "pay unverified", and worked after posted-pay listings.
- Skip excluded industries unless the employer's `keepAnyway` is yes.
- *Example for sales roles (change it to fit the user):* mid level means account executive, account manager, territory manager, business development manager, sales consultant, or anything titled senior, strategic or enterprise. Not mid level: sales development, business development representative, associate, trainee, coordinator, support.

### Order

Highest pay first, employers in the user's home metro before remote ones, 10 listings per session unless the user says otherwise.

### Finding the hiring manager

- The manager or director over that team, not HR or recruiting. **Web search and the employer's own pages only.**
- Never open a linkedin.com page. Store a public profile link only if it appeared in search results. The user opens it themselves.
- **Confidence:** **high** when a public source names them over that team or region; **medium** when the title fits but the team or region is inferred; **low** when they are only a plausible senior leader at the company, or when no one was found.
- **No one found:** leave `managerName` and `managerTitle` blank, write in `howIdentified` what was searched, set `confidence` to `low`, still draft both messages with a general greeting (for example "Hello [team] hiring team"), and say so in the report.
- **Email:** record a work email only if it is publicly published. Otherwise note the company's email format if a public source documents it, marked "unverified". No paid lookup tools and no guessing beyond that.

### The drafts

Two versions per contact, in the user's writing style:

- A connection note under 300 characters.
- A longer message under 90 words, for email or after connecting.
- Specific to the role and company. The ask is a 15-minute call about the team and what they look for. Not a referral request, and not "please look at my application". Say the user applied only if the listing's status is Applied or later. For a listing at To apply, write "I plan to apply" (or suggest they apply first).

### What to write in the tracker

Only the outreach columns: `managerName`, `managerTitle`, `howIdentified`, `confidence`, `profileUrl`, `emailOrFormat`, `connectionNote`, `longMessage`. Never `status` or `yourNotes`. One dated history line per listing worked, saying outreach was drafted.

---

<!-- stages/05-interview-prep/CONTEXT.md -->

## Stage 05: Interview prep

Prepare the user for a named interview. Run when the user asks.

### Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| User | Which interview, its stage, who they meet | The request | What to prepare for |
| Stage 00 | `../00-intake/output/my-rules.md` | Writing style | How the file reads |
| Stage 07 | `../07-resume/output/resume.md` | Full file | The user's stories come only from their own record |
| Shared | `../../shared/my-setup.md` | Full file | Tracker kind and location, Python command, browser, email connector |
| Shared | `../../shared/tracker-access.md` | Full file | The step 1 direct request, and the optional history line |
| Shared | `../../shared/recurring-mistakes.md` | Full file | Read before any tracker write |
| Shared | `../../shared/next-steps.md` | "After interview prep" | What to suggest when the session ends |
| Shared | `../../shared/lessons.md` | Full file | Learning from this session |
| Tracker | `listings` (that listing), `answers` (Work history) | One row; work history entries | The saved posting, the history, the user's record |
| Reference | `references/prep-sources-and-format.md` | Full file | Which sources count, and what the file holds |

### Process

1. Confirm with the user which interview, the stage (phone screen, hiring manager, panel, onsite), the date, and who they are meeting, if known. If the listing is not at Interview yet, offer to set it, and ask when they applied so `appliedDate` is filled too (a direct request, `shared/tracker-access.md`, with its own snapshot and `--stage user` check before step 2).
2. Read the listing (artifact: `get`; spreadsheet: `sheet.py show`). Read its `postingText`.
3. Build the company brief from allowed sources only, every fact linked.
4. List the likely questions, including the hard ones the user's record invites.
5. Map each question to a true story from the resume or the answer bank. Mark every gap.
6. Add questions for the user to ask, and the logistics from the listing's history.
7. Run the audit below, then save the file and give the user its path.
8. If the user wants it, add one history line saying prep was done, with a snapshot before and after and the check with `--stage prep`.
9. Ask once what this session taught (`lessons.md`) and add any lesson the person approves. Then end by suggesting the next step in one or two lines (`next-steps.md`, "After interview prep"). Suggest only; do not start it.

### Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 1 | Which interview and stage | Confirm or correct |
| 5 | Gaps where no true story fits | Fill the gap, or leave it marked |

### Audit

| Check | Pass Condition |
|-------|---------------|
| Company facts | Every fact about the company has a link to an allowed source |
| Stories | Every story is one the user has stated or the resume shows |
| Saved | The file is saved in `output/` and the user has the path |
| Lessons | The person was asked once what the session taught; only approved lessons were added |
| Next step | The session ended with the next thing to say, in quotes |

### Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Prep file | `output/[company-slug]-[interview date YYYY-MM-DD]-interview-prep.md` | Markdown, in the five parts of `prep-sources-and-format.md` |
| History line (optional) | Tracker, `listings` | One line saying prep was done |

---

<!-- stages/05-interview-prep/references/prep-sources-and-format.md -->

## Prep sources and file format

### Sources that count

Use only these:

1. **The saved posting:** the listing's `postingText`. Use it even if the live posting is gone. If `postingText` is empty and the posting is gone, say so and ask the user for a copy (an email, a PDF, a screenshot).
2. **The listing row:** title, pay, `why`, `history` (recruiter names, interview format and time) and `yourNotes` (read only).
3. **The employer's own website:** what they sell, to whom, leadership, press releases.
4. **Recent news** from established news outlets and trade publications, found by web search, each linked.
5. **The user's own record:** the resume text and the answer bank's work history entries. The user's stated history is the only source for their stories.

If web search is not available, build the brief from the saved posting and the listing only, and say plainly in the file what could not be researched.

Do not use as fact: anonymous review sites, aggregator job listings, social media posts, or anything you cannot link. You may mention review-site themes only as "people say", and only if the user asks.

### The prep file

1. **Company brief:** what they sell, to whom, how the team does its work, recent news, and where this role sits. Every fact gets a link.
2. **Likely questions:** from the posting's requirements and the interview stage, including the hard ones the user's record invites (a short stint, a career change, a gap, missing industry experience). For a step up (the listing's `why` says so), include "Why are you ready for this level?", answered with true stories that already show next-level scope (people led, results owned, decisions made).
3. **The user's stories:** each likely question mapped to a true story from the resume or the answer bank's work history. Invent nothing. Mark any gap so the user can fill it.
4. **Questions for the user to ask** the interviewer.
5. **Logistics** from the listing's history: time, format, recording notices, who to contact.

---

<!-- stages/06-mailbox-check/CONTEXT.md -->

## Stage 06: Mailbox check

Read the user's email for replies from employers and suggest status updates. Run only when the user asks ("check my email", "update the tracker from my email"). **Read only:** never reply, send, forward, delete, archive, label, mark as read, or move any email.

### Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| User | The user's email, through a connector, their webmail, or pasted mail | The window to check | Where the replies are |
| Stage 00 | `../00-intake/output/my-rules.md` | Employers, autonomy | Never-contact list and what may be written |
| Previous run | `output/` | The newest mailbox report | Where the last check stopped |
| Shared | `../../shared/rules.md` | Section 7 | Which status changes this stage may make |
| Shared | `../../shared/my-setup.md` | Full file | Tracker kind and location, Python command, browser, email connector |
| Shared | `../../shared/tracker-access.md` | Full file | Reading, writing and the check |
| Shared | `../../shared/recurring-mistakes.md` | Full file | Read before any tracker write |
| Shared | `../../shared/next-steps.md` | "After the mailbox check" | What to suggest when the session ends |
| Shared | `../../shared/lessons.md` | Full file | Learning from this session |
| Tracker | `listings`, `companies` | Listings at Applied, Followed up, Interview; To apply only to notice a reply | What a message can match |
| Reference | `references/reading-and-sorting-mail.md` | Full file | Ways in, the window, matching, sorting, what gets written |

### Process

1. Take a tracker snapshot.
2. Set the window: from where the last check stopped to now.
3. Search every folder in the window, by employer name and by application-system sender.
4. Match each message to one listing. Ask the user when a message could match more than one.
5. Sort each match (`reading-and-sorting-mail.md`, "Sorting each match").
6. **[Checkpoint]** Show every proposed change in one list. Wait for yes, no or a change on each.
7. Write only what the user approved: `status` and one history line per listing.
8. Take an after snapshot and run the check with `--stage mailbox`.
9. Run the audit below, then save the report.
10. Ask once what this session taught (`lessons.md`) and add any lesson the person approves. Then end by suggesting the next step in one or two lines (`next-steps.md`, "After the mailbox check"). Suggest only; do not start it.

### Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 4 | A message that could match more than one listing | Which listing |
| 6 | Every proposed status change and history line | Yes, no, or a change, for each |

### Audit

| Check | Pass Condition |
|-------|---------------|
| Read only | No email was sent, replied to, deleted, moved, labeled or marked as read |
| Approval | Every status change was approved by the user in this session |
| No Applied | No listing was set to Applied from an email |
| Secrets | No code, sign-in link or password was copied anywhere |
| Window | The window covered is written in the report |
| Check | `check_tracker.py --stage mailbox` passes, and `yourNotes` is untouched |
| Lessons | The person was asked once what the session taught; only approved lessons were added |
| Next step | The session ended with the next thing to say, in quotes |

### Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Approved changes | Tracker, `listings` | Status and history lines, as approved |
| Mailbox report | `output/[YYYY-MM-DD]-mailbox-report.md` | Window covered (from and to), deadlines first, what was found, what changed, what was left alone, what needs the user |

---

<!-- stages/06-mailbox-check/references/reading-and-sorting-mail.md -->

## Reading and sorting mail

### Three ways in, best first

- **An email connector** (for example Gmail or Outlook) connected in Claude.
- **The user's webmail open in the browser**, with the user signed in themselves. Claude never signs in to email.
- **The user pastes or forwards** the emails.

**Read only.** Never reply, send, forward, delete, archive, label, mark as read, or move any email.

**Codes and passwords in email.** Verification codes, sign-in links and temporary passwords often show in message previews. Never copy them into the tracker, a report or the chat.

### Covering the window

For pasted or forwarded mail, the window is simply the dates of the messages the user gave; write those in the report.

- Start where the last mailbox check stopped (its history lines and report say "covered <from> to <to>"), and end now. With no earlier check, use the period the user gives, or the last 14 days. Write the window in this session's report, so the next check starts there and nothing is read twice or missed.
- **Search every folder, not just the inbox.** Many people have rules that file job email into folders, and some mail apps split the inbox (for example Focused and Other). Search all folders by date range. Date-bounded searches one day at a time are the most reliable on a busy mailbox (for example `received:` searches in Outlook, `after:` and `before:` in Gmail).
- Look for each employer that has a listing at Applied or later, by company name and by the application system's sender (messages often come from the platform, not the employer).
- **Webmail in the browser:** message lists load as you scroll ("virtualized"), so collect rows by scrolling the list by script until no new rows appear, then open each relevant message by a snippet of its preview text. If the list stops loading new rows, the browser window may be covered or hidden: ask the user to bring it to the front.

### Matching

Match each message to one listing: same company and, where the message names it, the same title or req id. If a message could match more than one listing, do not guess. Ask the user.

### Sorting each match

- **Confirmation** of an application ("we received your application"): no status change. Ask once whether the user wants these logged as history lines; many people do not.
- **Interview request or scheduling:** propose `Interview`, with the date, time, format and names in the history line.
- **Rejection,** including "we filled the position with another candidate": propose `Rejected`.
- **The role was cancelled or is "no longer available"** (not a rejection of the user): propose `expired`.
- **Offer:** propose `Offer`.
- **A follow-up the user sent** (found in their sent mail, to an employer with a listing at Applied): propose `Followed up`.
- **Assessment or next step that is not an interview** (online test, video interview, game-based assessment): no status change. Offer a history line, and put any **deadline** at the top of the report. Assessments are the user's to take.
- **Scheduling back-and-forth** (a recruiter offering times): replies are the user's to send. List it with any deadline.
- **Invitations from employers not on the target list** (for example a job site's "apply to this job" message): never act on them. List them for the user's call.
- **A reply about a listing still at To apply** (for example the user applied outside a session): no status change from this stage. Tell the user, and offer a history line. The user can then set the status directly (checked with `--stage user`).

### The proposed-changes list

One list, before writing anything, for example: "Example Health Co, Clinical Account Executive: Applied to Interview. Email from 2026-03-14 asks for a call on 3/18 at 10am with the regional manager." The user says yes, no, or change it for each one.

### What gets written

Only what the user approved: `status` (if changed) and one history line per listing, ending "from email dated YYYY-MM-DD, approved by the user". When several approved emails concern one listing (for example a confirmation and an interview request), combine them into that one line, naming each email's date. Never set Applied from an email: Applied comes only from the apply stage or the user.

---

<!-- stages/07-resume/CONTEXT.md -->

## Stage 07: Resume

Build the user's resume from facts they state, shaped by what real postings for their target role ask for, and checked by script before anyone sees it as final. Also makes tailored versions for single listings. Run when the user asks ("Build my resume").

**Nothing on the resume may be something the user did not say.** Every fact comes from `output/resume-facts.md`, which the user confirms line by line.

### Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Stage 00 | `../00-intake/output/my-rules.md` | Target roles, industries, place, writing style | What the resume is for |
| Shared | `../../shared/my-setup.md` | Full file | Tracker kind and location, Python command, browser, email connector |
| Shared | `../../shared/rules.md` | Section 10 | Writing rules |
| Shared | `../../shared/career-direction.md` | Full file | Judge posting levels and aim the resume at the next step |
| Shared | `../../shared/tracker-access.md` | Full file | Only for a tailored version's history line |
| Shared | `../../shared/recurring-mistakes.md` | Full file | Read before any tracker write |
| Shared | `../../shared/next-steps.md` | "After the resume" | What to suggest when the session ends |
| Shared | `../../shared/lessons.md` | Full file | Learning from this session |
| User | Their current resume, if any (`output/resume.pdf` or pasted) | Full content | A source of facts only |
| Tracker | `listings` | `postingText` of listings for the target role | Real postings, and the listing for a tailored version |
| Reference | `references/fact-questions.md` | Full file | Collecting the facts |
| Reference | `references/resume-facts-template.md` | Full file | The shape of the facts file |
| Reference | `references/employer-asks.md` | Full file | What employers ask for, and the fallbacks |
| Reference | `references/resume-guide.md` | Full file | General rules, examples by field, the default, the file format |
| Reference | `references/sample-resume.md` | Full file | A finished example of the format |
| Reference | `references/writing-and-tailoring.md` | The part for this request | Writing, checking, building, tailoring, opting out |

### Process

1. If the user keeps their own resume, follow `writing-and-tailoring.md`, "The user keeps their own resume", and stop there.
2. Collect the facts one question at a time (`fact-questions.md`) into `output/resume-facts.md`.
3. **[Checkpoint]** The user approves the whole facts file.
4. Learn what employers ask for from 3 to 5 real postings, or a named fallback (`employer-asks.md`).
5. **[Checkpoint]** The user confirms the summary. Save it in the facts file.
6. Write `output/resume.md` one section at a time, each one approved.
7. Run `check_resume.py` and fix everything it reports.
8. Back up any earlier PDF, build `output/resume.pdf`, check the page count, and run the check again.
9. **[Checkpoint]** The user opens and approves the PDF.
10. For a tailored version, follow `writing-and-tailoring.md`, "A tailored version for one listing".
11. Ask once what this session taught (`lessons.md`) and add any lesson the person approves. Then end by suggesting the next step in one or two lines (`next-steps.md`, "After the resume"). Suggest only; do not start it.

### Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 2 | The complete facts file | Approve, or what to change |
| 4 | What employers ask for, with the postings it came from | Confirm, or what to change |
| 6 | Each resume section | Yes, or changes |
| 8 | The finished PDF | Approve, or what to change |
| 10 | What a tailored version changed | Approve, or what to change |

### Audit

| Check | Pass Condition |
|-------|---------------|
| Facts first | The user approved the facts file before any resume was written |
| Employer asks | A confirmed "What employers ask for" section is saved, from 3 to 5 real postings or a named fallback |
| Terms | No term from the postings was used unless it is in the facts file |
| Facts only | Every number, title, date, tool and skill on the resume is in the facts file (`check_resume.py`), and every scope claim (people led, budget, profit and loss, reporting line) matches a confirmed fact; the script cannot catch these, so read them by hand |
| Style | `check_resume.py` passes: no dashes, no pronouns, no personal data that does not belong, sensible bullets, standard headings |
| Length | The page count is within the limit |
| Approval | The user approved the final PDF, and any earlier `resume.pdf` was backed up first |
| Lessons | The person was asked once what the session taught; only approved lessons were added |
| Next step | The session ended with the next thing to say, in quotes |

### Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Facts file | `output/resume-facts.md` | The template's shape, approved, with "What employers ask for" |
| Resume text | `output/resume.md` | The format in `resume-guide.md` |
| Resume PDF | `output/resume.pdf` | One-column PDF, approved by the user |
| Tailored versions | `output/resume-[listing-id].md` and `.pdf` | Same format, each approved |
| Earlier PDF | `output/resume-before-[YYYY-MM-DD].pdf` | The user's previous file, unchanged |

---

<!-- stages/07-resume/references/employer-asks.md -->

## What employers ask for

Before writing, look at what employers actually ask for in real postings for the user's target role, so the resume puts first what matters for that job. This works the same for any job in any field. `resume-guide.md` has examples by field showing what a finished summary looks like.

**Every user gets a resume, in any field.** If a step cannot be done, go to the next fallback. Never stop the resume because postings are hard to find.

### Steps

1. **Pick the target.** Take the main target role from the user's rules, at the level of their next step when it is a step up (`shared/career-direction.md`), so the resume reads at the level they are aiming for. If the user has two quite different targets, ask which one this resume is for. One resume per target. A resume for a second target is saved as `resume-<target>.md` and `.pdf` (for example `resume-quality-inspector.md`), never over `resume.md`.
2. **Gather 3 to 5 real postings for that role**, newest first, in this order of preference:
   1. Listings already in the tracker for this role that have `postingText` saved.
   2. Postings on employers' own career sites, found by web search, for this role and level in or near the user's allowed places (or remote roles open to them). Posted in the last six months where possible.
   3. Postings the user pastes or attaches.
   Use only postings for the target role and level. If one is for a different kind of job (for example a role the user's rules list as out), say so and leave it out, or ask for another.
   Never open LinkedIn. Job aggregators may be used to find which employers post the role; read the posting itself on the employer's own site when you can.
3. **Read each posting and note**, with the posting it came from:
   - Must-have credentials: licenses, degrees, certifications, clearances.
   - Tools, systems and hard skills named.
   - The results the employer cares about (for example revenue, patient outcomes, uptime, students served, safety record).
   - The words the employer uses for the work (for example "territory", "pipeline", "caseload", "care plan").
   - Seniority signals and anything that sets length (years required, scope).
   - Tone (plain, formal, technical).
   - Anything asked for beyond the resume (portfolio, writing sample, references up front).
4. **Sum it up.** What appears in at least two postings counts; what appears in one is noted but given less weight.
   - **Section order:** which sections come first. Credentials that most postings require and the user holds go directly under the summary.
   - **What leads each job:** the kind of proof that goes first in each role's bullets, matched to the results employers asked for.
   - **Terms to mirror:** the employers' own words for the work. Mark each one "in your facts" or "not in your facts". Terms not in the facts are **never** used. List them for the user as possible gaps: if the user says one is true, add it to the facts file first (with their confirmation), then it may be used.
   - **Length and tone.**
   - **Closest example(s)** from `resume-guide.md`, and the career-changer notes if the user is moving fields.
5. **Show this summary to the user** in plain words, with the postings it came from (company, title, link). Ask: "Does this match the jobs you want? Anything to change?" Make their changes.
6. **Save it** in the "What employers ask for" section of the facts file, with the date and the user's confirmation.

### Fallbacks, in order

- **Fewer than 3 postings found** (rare role, small market, no web access on this device): use the ones found, plus the closest example. Write that down ("Based on: 2 postings plus example").
- **No postings at all:** ask the user to describe two or three jobs they want in their own words, or to paste any job description they have seen. Build the summary from that plus the closest example ("Based on: user description plus example").
- **Still nothing:** use the "Default (any job)" in `resume-guide.md`. It works for every job ("Based on: default").
- In every case the user confirms the summary before writing, and the source is written down.

### Refresh

If the user's target role changes, or the summary is more than six months old, offer to redo these steps before making a new resume.

---

<!-- stages/07-resume/references/fact-questions.md -->

## Collecting the facts

Fill in `resume-facts.md` from `resume-facts-template.md`. Ask **one question at a time** and wait for each answer. Nothing on the resume may be something the user did not say.

1. If the user has a resume, read it first and fill in what it already says. Then show each job's facts and ask: "Is all of this true and current? Anything to add or remove?"
2. For each job, newest first:
   1. "What was your job title, the employer, the city, and the start and end month and year?"
   2. "In a few sentences, what did you do day to day? Who did you serve or sell to?"
   3. "What are you proudest of in this job? Results, numbers, awards, promotions, things you built or fixed."
   4. For every number the user gives: "Can you stand behind that number if an interviewer asks? Where does it come from?" Keep only numbers they confirm. Write the source next to each one.
   5. "Did you lead, train or manage anyone? How many?"
   6. "What tools, systems or software did you use?"
3. After all jobs: work out the years of experience from the dates and compare with what the user says. If they differ, ask which number to use and what it counts. Write it on the "Years of experience" line.
4. Education: school, degree, field, year (or "in progress"). Ask whether to show the year.
5. Licenses and certifications: name, issuer, state if any, year. **Never the license number.**
6. Skills the user can show in an interview.
7. Anything else worth showing: volunteer work, languages, military service, publications.
8. Gaps: "Is there any gap of six months or more you want to explain, or leave as is?" Never hide or change dates to cover a gap.
9. "Is there anything that must stay off your resume?" (for example a current employer's client names, or a job they do not want listed).
10. Show the full facts file. The user approves it before any resume is written. Every later change to a fact goes into this file first.

---

<!-- stages/07-resume/references/resume-facts-template.md -->

## Resume facts

<!-- The resume stage fills this in with the user, one question at a time, and saves it as stages/07-resume/output/resume-facts.md.
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

<!-- Built from 3 to 5 real postings for the target role, then confirmed by the user. -->

- Based on: [exactly one of: postings / N postings plus example / user description plus example / default. Postings the user pasted count as postings. A note in brackets after it is fine, for example "postings (3 pasted by the user)"]
- Built and confirmed by the user: [YYYY-MM-DD]
- Postings used:
  - Posting: [company] | [title] | [link] | [date posted or read]
- Section order: [for example Summary, Licenses and Certifications, Experience, Education, Skills]
- What leads each job: [the kind of proof that goes first]
- Must-have credentials the postings ask for: [list, and whether the user holds each]
- Terms to mirror (in your facts): [list]
- Terms the postings use that are not in your facts (never used unless added to the facts first): [list]
- Length and tone: [one page, plain / two pages, formal]
- Closest example: [name from resume-guide.md, plus "career changer" if it applies]

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

<!-- stages/07-resume/references/resume-guide.md -->

## Resume guide

Rules for every resume this system writes, for any job in any field. "General rules" always apply. What goes first on a resume comes from real postings for the user's target job ("What employers ask for" in the facts file). The examples by field below show finished results for common jobs; they are not a list the user must fit into. When nothing else is available, use the default, so every user gets a resume.

### General rules

**Honesty**
- Every fact comes from the approved facts file, `resume-facts.md`. Nothing invented, nothing rounded up, no title the user did not hold, no tool they did not use.
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

What usually goes first on a resume for some common jobs. For a real user, this always comes from postings for their own target job. These examples help spot anything missed. A job not listed here is handled exactly the same way.

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

### File format (for `resume.md`)

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

<!-- stages/07-resume/references/sample-resume.md -->

## Sample resume (made up)

This is a made-up person, to show the exact format `resume.md` must follow. It is the same format as "File format" in `resume-guide.md`, and the one `tools/build_resume.py` and `tools/check_resume.py` read. Everything below the line is the resume.

If the user keeps their own resume (they opted out of resume building), `resume.md` is a plain copy of their PDF's text for filling forms, and does not need to follow this format.

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

<!-- stages/07-resume/references/writing-and-tailoring.md -->

## Writing the resume, and tailored versions

Run every command from the workspace root. `<out>` below means `stages/07-resume/output`.

### The user keeps their own resume

If the user opted out (setup's resume choice "use mine"), do not rewrite or critique it. Their file is `<out>/resume.pdf`. Offer to make the text copy `<out>/resume.md` from it for filling forms, and show the copy before saving. You may offer one short list of suggestions from `resume-guide.md`, once, and only if they want it.

### Writing the main resume

1. Write `<out>/resume.md` in the exact format in `resume-guide.md` ("File format"). `sample-resume.md` shows a finished one.
2. Follow every rule in "General rules" and the "What employers ask for" section saved in the facts file. The resume's sections come in that section order. For a step-up resume, lead each job with the confirmed facts that show next-level scope: leading or training people, owning results, cross-team work (`shared/career-direction.md`, "Advancement").
3. Draft **one section at a time**, in that order (contact line and summary always first). Show each one and get a yes or changes before the next.
4. Show the whole resume, and check the text:
   `python tools/check_resume.py <out>/resume.md --facts <out>/resume-facts.md`
   Fix everything it reports. Do not show the resume as final until it passes.
5. If the user already had a `resume.pdf`, first copy it to `<out>/resume-before-<YYYY-MM-DD>.pdf`. Then build the PDF: `python tools/build_resume.py <out>/resume.md <out>/resume.pdf`, and check again with the PDF and the page limit:
   `python tools/check_resume.py <out>/resume.md --facts <out>/resume-facts.md --pdf <out>/resume.pdf --years <years from the facts file>`
6. Check the page count the build reports: one page for under ten years of experience, two at most otherwise. If it is over, cut the oldest or weakest bullets (ask the user which), never the font size below the minimum.
7. Ask the user to open the PDF and approve it. Only an approved PDF is used to apply.

### A tailored version for one listing (only when the user asks)

1. Read the listing's `postingText`. List the posting's top requirements in plain words.
2. Build a tailored copy from the same facts file:
   - **Allowed:** reorder bullets, choose which facts to show, shorten bullets, rewrite the summary for this role, use the posting's own words for a skill **only where the facts show that skill**.
   - **Not allowed:** any fact, number, tool, title or skill not in the facts file. Changed dates or titles. Copying sentences from the posting.
3. Show what changed compared with the main resume, in a short list.
4. Write it to `<out>/resume-<listing id>.md`, check the text, build `<out>/resume-<listing id>.pdf`, then check again with `--pdf` and `--years`, as in steps 4 and 5 above. Never overwrite `resume.md`.
5. After the user approves it, take a tracker snapshot, add a history line to the listing: `YYYY-MM-DD tailored resume approved: resume-<listing id>.pdf`, then run the check with `--stage resume`.

---

<!-- stages/08-company-research/CONTEXT.md -->

## Stage 08: Company research

Research sessions the user starts by asking: (A) find employers, (B) a company deep dive, (C) an industry map, (D) role research, or (E) a career path. Only part A writes to the tracker, and only after the user approves each employer.

### Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| User | The request | Which kind, and its subject | What to research |
| Stage 00 | `../00-intake/output/my-rules.md` | Target roles, place, pay, industries, employers | What fits, and who never to suggest |
| Stage 07 | `../07-resume/output/resume.md` | Full file, if it exists | The user's stated facts, for fit notes |
| Shared | `../../shared/my-setup.md` | Full file | Tracker kind and location, Python command, browser, email connector |
| Shared | `../../shared/tracker-access.md` | Full file | Part A only: reading, writing and the check |
| Shared | `../../shared/recurring-mistakes.md` | Full file | Read before any tracker write |
| Shared | `../../shared/adding-employers.md` | Full file | Part A: checking and writing each employer |
| Shared | `../../shared/helpers.md` | Full file | Only if you use research helpers |
| Shared | `../../shared/prompts.md` | "Finding employers and researching them" | Wording the user can use |
| Shared | `../../shared/next-steps.md` | "After company research" | What to suggest when the session ends |
| Shared | `../../shared/lessons.md` | Full file | Learning from this session |
| Tracker | `companies`, `settings`, `listings` | All rows; `postingText` for part E | The target list, tiers, industry words, postings by level |
| Previous runs | `output/` | "Checked and not added" and "Leads" lists | So earlier work is not repeated |
| Reference | `references/research-rules.md` | Full file | Sources, links, names, size, the five kinds |
| Reference | `references/find-employers.md` | Full file | Part A |
| Reference | `references/other-research.md` | The part asked for | Parts B, C, D and E |
| Shared | `../../shared/career-direction.md` | Full file | Part E, and judging levels in part A |

### Process

1. Name the kind (A, B, C, D or E) and say in one line what you will look for.
2. For part A, agree a target number with the user and take a tracker snapshot.
3. Research from allowed sources only, every fact linked (`research-rules.md`).
4. Part A: check every candidate, and stop at the target, at low yield, or at the budget (`find-employers.md`).
5. **[Checkpoint]** Part A: show the candidates in one table for the user to approve, drop or change.
6. Part A: write only the approved employers, take an after snapshot, and run the check with `--stage research`.
7. Run the audit below, then save the report.
8. Ask once what this session taught (`lessons.md`) and add any lesson the person approves. Then end by suggesting the next step in one or two lines (`next-steps.md`, "After company research"). Suggest only; do not start it.

### Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 1 | What you will look for | Go, or a different focus |
| 4 | Candidate employers, with careers site, tier, fit and source | Approve, drop or change each one |

### Audit

| Check | Pass Condition |
|-------|---------------|
| Links | Every fact in the report has a link to an allowed source |
| Access | No LinkedIn page was opened, no site required a sign-in, nothing was scraped |
| Part A approval | Every new employer was approved by the user and has its own careers site link |
| Part A names | No new employer matches an existing name or a never-contact entry, and none is in an excluded industry unless the user asked to keep it (`keepAnyway` yes) |
| Check | Part A: `check_tracker.py --stage research` passes |
| Lessons | The person was asked once what the session taught; only approved lessons were added |
| Next step | The session ended with the next thing to say, in quotes |

### Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| New employers (A) | Tracker, `companies` | One approved row each |
| Find-employers report (A) | `output/[YYYY-MM-DD]-find-employers.md` | Added, borderline, checked and not added, leads |
| Company report (B) | `output/[company-slug]-company-research.md` | The six parts of B, every source linked |
| Industry map (C) | `output/[industry-slug]-industry-map.md` | Employers by type, every source linked |
| Role report (D) | `output/[title-slug]-role-research.md` | Duties, requirements, posted pay, next roles, every source linked |
| Career path (E) | `output/[YYYY-MM-DD]-career-path.md` | Next levels on each track, requirements, gaps and how to close them, posted pay, every source linked |

---

<!-- stages/08-company-research/references/find-employers.md -->

## A. Find employers (target list building)

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
3. **Check every candidate** before showing it, as `shared/adding-employers.md` steps 1 and 2 say, and also:
   - It has a presence the user's place rules allow: an office in the home metro, a territory covering it, or remote roles open to the user's state. Say which, with a link.
   - It plausibly hires the user's target role. Say why in one line.
4. **Know when to stop.** Agree a target with the user first (for example 30 new employers). Track the **yield**: of your last 20 searches or checks, how many produced a new employer that passed step 3. Stop when you reach the target, when yield drops below 2 in 20 (the sources are used up), or at the session budget (about 150 tool calls). Say which one stopped you.
5. **Show the candidates in one table**: company, industry, proposed tier (using the user's tier meanings from `settings`), careers site, why it fits, source. Ask the user to approve, drop or change each one.
6. **Write only the approved ones**, as `shared/adding-employers.md` step 3 says.
7. Offer a sweep of the new employers ("Say 'Sweep [names]'"). Do not start one unless the user says yes.

### The report

Four lists, so the next session can pick up where this one stopped:

- **Added:** each new employer with its industry, tier, careers site and where the name came from.
- **Borderline, your call:** employers that fit on paper but have a doubt (for example jobs only in a nearby city, or one role that fits among many that do not). One line each on the doubt.
- **Checked and not added:** each with a one-line reason (no board of its own, no roles of the user's kind, excluded industry). This stops the next session from checking them again.
- **Leads for next time:** sources not yet worked, and names found but not yet checked.

---

<!-- stages/08-company-research/references/other-research.md -->

## B, C, D and E: reports only

### B. Company deep dive

For one employer the user names (often before applying or before an interview).

1. What they sell, to whom, and how (their own site).
2. Size, locations, and where the user's target role sits (their own site, press releases, government filings for public companies).
3. Recent news from the last 12 months (established news outlets and trade publications).
4. Open roles that match the user's targets, from their own careers site, with links.
5. How the user's background fits, in two or three plain sentences, using only the user's stated facts.
6. Questions worth asking them.

### C. Industry map

For one industry in or near the user's place.

1. List the main employers in that industry that the user's place rules allow, grouped by type (for example software vendors, insurers, service firms), each with a link and one line on what they do.
2. Mark which are already on the target list.
3. Note which roles in that industry match the user's targets, and where they usually sit (sales team, clinical team, operations).
4. To add any to the target list, run part A for those names.

### D. Role research

For one job title the user asks about.

1. What the role does day to day, from three or more employers' own postings, each linked.
2. What those postings require and prefer, and how that compares with the user's stated experience (facts only).
3. Pay: only pay **posted by employers** for this role in the user's area or remote roles open to them. Give the range and the number of postings it comes from. If fewer than three postings show pay, say so. Never estimate a number without a posting behind it.
4. Typical next roles, if postings or employers' own career pages say so.

### E. Career path

For "What's my next career step?" Uses `shared/career-direction.md` and the user's current level and next step in `my-rules.md`.

1. The next one or two levels up from the user's current role, on both tracks where both exist (senior individual contributor, and team lead or manager), with real titles employers use, from three or more of their own postings each, linked.
2. For each: what those postings require, what the user already has (facts only), and the gaps.
3. How to close each gap: a skill to build, a certification, a project to take on at work, or a bridge role. Name the source for every requirement.
4. Posted pay at each level, as in part D.
5. Ask whether to update "Next step" in their rules. A change goes through the intake stage.

Without web search: use the `postingText` of tracker listings at those levels, plus the ladder in `shared/career-direction.md`. Write "Based on: N tracker postings, no web search" at the top, say that pay at each level is unknown unless those postings show it, and state nothing unsourced as fact.

---

<!-- stages/08-company-research/references/research-rules.md -->

## Research rules

Rules for every research session.

> **Site terms.** LinkedIn and some job boards forbid automated access in their terms. Research uses web search, employers' own websites, and public lists. It never opens LinkedIn, never scrapes a site, and never signs in anywhere. Job aggregators are used only to learn company names, never as proof that a job exists. The user is responsible for following each site's terms.

- **Sources:** web search results, employers' own sites (including careers and locations pages), and public lists: business journal and newspaper lists, chamber of commerce directories, economic development agency lists, industry association member lists, conference exhibitor lists, government data, company press releases. **No paid tools, no sign-ins, no LinkedIn.**
- **Every fact gets a link.** If you cannot link it, do not state it as fact.
- **Exact names.** Use the company's own spelling. Check the target list for an exact match before calling anyone new (`shared/recurring-mistakes.md` item 7).
- **Never suggest** the user's current employer, anyone on their never-contact list, or employers in an excluded industry unless the user asks.
- **Helpers:** if you use research helpers, follow `shared/helpers.md`. The main session checks every result and does every write.
- **Size:** about 25 candidates per session at most, so each one gets checked properly.

### The five kinds

| Kind | The user says something like | Writes to the tracker |
|---|---|---|
| A. Find employers | "Suggest employers that fit my background" | New `companies` rows, after the user approves each one |
| B. Company deep dive | "Tell me about [company]" | Nothing (a report only) |
| C. Industry map | "Map the [industry] employers around [place]" | Nothing, unless the user then asks to add some (run A for those) |
| D. Role research | "What does a [title] do, and what does it pay around here?" | Nothing (a report only) |
| E. Career path | "What's my next career step?" | Nothing (a report only) |
