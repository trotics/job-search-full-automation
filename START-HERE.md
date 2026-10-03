# Start here (instructions for Claude)

This folder is a job search system: a Claude Skill, a tracker, and small scripts that check the work. A person has opened it and asked you to look at it, set it up, or help with their job search. Follow these steps. Talk to them in plain, friendly language; most people using this are not technical.

## Which situation is this?

- **`my-files/my-rules.md` does not exist:** this is a first-time setup. Do "First-time setup" below.
- **`my-files/my-rules.md` exists:** this is a returning user. Read `skill/job-search/SKILL.md` and follow it. Ask what they want to do today, and offer the common choices from `skill/job-search/references/prompts.md` (for example "Run a sweep", "Let's apply", "Build my resume", "Check my email").

## Using the Skill

The Skill's instructions are the files in `skill/job-search/`. Always follow them:

- If a skill named **job-search** is already available to you (it loads automatically in Claude Code from `.claude/skills/`, or the user uploaded it in the Claude app), use it.
- If it is not, read `skill/job-search/SKILL.md` now and follow it, and the files it points to, straight from this folder. It works exactly the same; nothing has to be installed for you to follow it.

The safety rules in `skill/job-search/rules.md` (section 9) apply from the first minute: never create accounts, type passwords, enter ID or bank numbers, solve CAPTCHAs, send messages, or submit an application without the person's review.

## First-time setup

Do one step at a time. Say in one line what you are doing before each step and what happened after it. Ask once, before step 2, for permission to run the setup commands in steps 2 and 3 (a version check, an install of two Python add-ons, and a self-test), rather than asking for each one.

1. **Say hello.** In two or three sentences: this finds jobs on employers' own career sites, checks each against their rules, keeps a tracker, builds a resume from facts they confirm, and fills in applications with them. Nothing is ever submitted or sent without their review. Setup takes about 15 minutes.
2. **Python.** The checking scripts need Python 3. Run `python --version` (on a Mac use `python3`; on some Windows computers `py`). Use whichever works for every later command.
   - If it works: ask, then run `python -m pip install -r requirements.txt`.
   - If Python is missing: tell them in plain words how to install it from python.org (on Windows, tick "Add python.exe to PATH" in the installer; on a Mac, run the downloaded installer), then try again. Or offer to continue without it for now. Without Python, stages cannot finish their checks, and you must say so whenever that happens.
3. **Quick self-test.** If Python works, run `python tests/run_checker_selftest.py`. Only the last line matters: it should say `SELF-TEST: ALL CAUGHT`. The lines above it that say FAIL are the test catching mistakes it planted on purpose; tell the user that so they are not alarmed. If the last line says anything else, tell them, and do not go further until it is understood.
4. **Tracker.** Ask: "Do you want your tracker as a private web page in your Claude account (recommended), or as a spreadsheet?"
   - **Web page:** publish `tracker/tracker-page.html` as a new artifact with the `db` capability. Give them the link and ask them to open it: they should see an empty tracker that says "No listings recorded yet". If you cannot publish an artifact with a database here, say so and use the spreadsheet.
   - **Spreadsheet:** copy `tracker/spreadsheet/job-search-tracker.xlsx` into `my-files/`. Tell them to close it in Excel before each session; if it is open, saving fails with a message saying so.
5. **Resume.** Ask whether they have a resume they are happy with. If yes, ask them to save it as `my-files/resume.pdf` (offer to wait). If not, tell them the interview will offer to build one.
6. **Browser for applying.** Check whether the Claude in Chrome tools are available to you. If not, tell them: applying works best with the Claude in Chrome extension for Google Chrome, connected to the Claude desktop app, because it can upload their resume. Sweeps and everything else work without it. This is not a blocker for today.
7. **Optional, for chats outside this folder:** they can also upload `job-search-skill.zip` in the Claude app (Customize, then Skills, then +, then Upload a skill; code execution must be on in Settings). Mention it once; it is not needed when working in this folder.
8. **Start the interview.** Run `skill/job-search/stages/00-intake.md`: the setup interview, one question at a time. It saves their rules to `my-files/my-rules.md` only after they approve. **Do not ask again what setup already answered:** the tracker (intake question 1) and the resume (intake step 6). Say in one line what you already have (for example "Your tracker is the spreadsheet in my-files") and go straight to the next question.

When the interview is done, tell them the next step in one line, usually: "Say 'Suggest employers that fit my background', then 'Run a sweep'."

## Do not

- Do not edit files in `skill/`, `tools/`, `tracker/` or `tests/` unless the person asks to change how the system works.
- Do not run `git` commands that push, publish or change history.
- Do not put the person's details anywhere except `my-files/`, `reports/`, `backups/` and their own tracker. Those folders are never uploaded by git.
