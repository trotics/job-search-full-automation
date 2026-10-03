# Setup questionnaire: Job Search Full Automation

Read this file when the person types `setup`, asks to be set up, or `shared/my-setup.md` does not exist or still holds `{{` placeholders. It configures the system, not the job search itself: the person's goals, rules and resume facts are collected by the stages.

---

## Before the questions

Say hello in two or three sentences: this finds jobs on employers' own career sites, checks each against their rules, keeps a tracker, builds a resume from facts they confirm, and fills in applications with them. Nothing is ever submitted or sent without their review. Setup takes about 15 minutes.

In a chat with no folder, follow `shared/no-folder.md`, "Setup", alongside this file.

Ask once for permission to run the setup commands (a version check, an install of two Python add-ons, and a self-test), rather than asking for each one. Then work out the derived fields below while they answer.

## Ask these all at once

The person should be able to answer both in one message.

### Q1: Where do you want your tracker?
- Placeholders: `{{TRACKER_KIND}}`, `{{TRACKER_LOCATION}}`
- Files: `shared/my-setup.md` (from `shared/my-setup-template.md`)
- Type: selection
- Options:
  - **A private web page in your Claude account** (default, recommended): publish `tracker/tracker-page.html` as a new artifact with the `db` capability. Give them the link and ask them to open it: they should see an empty tracker that says "No listings recorded yet". Kind `Artifact`, location the link. If you cannot publish an artifact with a database here, say so and use the spreadsheet.
  - **A spreadsheet:** copy `tracker/spreadsheet/job-search-tracker.xlsx` to `tracker/my-tracker.xlsx`. Kind `Spreadsheet`, location `tracker/my-tracker.xlsx`. Tell them to close it in Excel before each session; if it is open, saving fails with a message saying so.

### Q2: Do you already have a resume you are happy with?
- Placeholder: `{{RESUME_CHOICE}}`
- Files: `shared/my-setup.md` (from `shared/my-setup-template.md`)
- Type: selection
- Options:
  - **Yes, use mine as it is:** ask them to save it as `stages/07-resume/output/resume.pdf` (offer to wait). Write "use mine".
  - **Yes, but I want it improved:** write "improve mine". Ask them to save it in the same place (or paste its text when the resume stage starts), as a source of facts.
  - **No, or I need a new one:** write "build new".
  - Default: "decide later".

## Derived fields (do not ask)

### `{{PYTHON_COMMAND}}`
In a chat with no folder: write "code execution" if you can run Python there (then use the Skill's `tools/` as `shared/no-folder.md` says), otherwise "none (Skill only)"; skip the install and the self-test. Otherwise follow `shared/python-setup.md`: find the command that works (`python`, `python3` or `py`), install the add-ons, and run the self-test. Write the command, or "none" if the person chose to continue without Python.

### `{{APPLY_BROWSER}}`
Check whether the Claude in Chrome tools are available to you. Write "Claude in Chrome" or "not connected yet". If not connected, tell them: applying works best with the Claude in Chrome extension, because it can upload their resume (`stages/03-apply/references/claude-in-chrome-setup.md`). Sweeps and everything else work without it. This is not a blocker for today.

### `{{EMAIL_CONNECTOR}}`
Check whether an email connector (for example Gmail or Outlook) is available to you. Write its name, or "none".

### `{{SETUP_DATE}}`
Today, `YYYY-MM-DD`.

---

## After setup

1. Copy `shared/my-setup-template.md` to `shared/my-setup.md` and replace every placeholder in the copy with the answers and derived values. Never edit the template.
2. Scan `shared/my-setup.md` for any remaining `{{` patterns. If any remain, ask for the missing information.
3. Only when working in the folder, mention once, for chats outside it: they can also upload `job-search-skill.zip` in the Claude app (Customize, then Skills, then +, then Upload a skill; code execution must be on in Settings). It is not needed when working in this folder.
4. Tell the person:

"You are set up. Here is your setup:

- **Tracker:** [web page link, or tracker/my-tracker.xlsx]
- **Resume:** [use mine / improve mine / build new / decide later]
- **Applying browser:** [Claude in Chrome / not connected yet]

Next is a short interview about the jobs you want. I ask one question at a time."

5. Start `stages/00-intake/CONTEXT.md`. Do not ask again what setup already answered.
