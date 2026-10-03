# Working without a folder

For a chat with no folder Claude can read and write (Claude on the web, a tablet, or the Skill uploaded in the Claude app). Every other file still applies; this one says what changes.

## The person's files travel with them

There is nowhere to keep files between chats, so the person keeps them:

- `my-setup.md`, `my-rules.md`, and `my-tracker.xlsx` (if their tracker is the spreadsheet).
- For the resume: `resume-facts.md`, `resume.md` and `resume.pdf`.

At the start of each chat, before anything else, ask them to attach `my-setup.md`, `my-rules.md` and their tracker file plus the ones the task needs, or to keep them in the files of a Claude Project so every chat sees them. **Every session that creates or changes one of these files ends by giving the complete new file as a download**, with one line: "Save this over your old copy, and attach it next time." Never start a new tracker, setup or interview when the person may simply have forgotten to attach their files: ask first. Reports (fit, research, prep) are shown in the chat and given as downloads if the person wants to keep them.

In `my-setup.md`, the spreadsheet tracker's location is "my-tracker.xlsx (kept by you; attach it each chat)".

## Scripts

The scripts are in this Skill's `tools/` folder. If code execution is on, run them from there with the full path, on the files the person attached (for example `python <skill folder>/tools/check_tracker.py snapshot my-tracker.xlsx before.json`), and give back the changed files.

If code execution is off or a script cannot run: edit the spreadsheet only if you can, otherwise give the person the exact rows to type in. Check the work by hand against `recurring-mistakes.md` and the stage's Audit table, and say "checked by hand; the script did not run". Never call that a passed check. Backups and snapshots made in code execution are lost when the chat ends: the downloaded tracker is the person's only backup, so remind them to keep the previous copy until the new one is saved.

## Setup

- Skip the permission request for the install and the self-test: they are not run without a folder. If code execution is on, ask once before running scripts.
- Tracker: publish the tracker page if you can (the page is in this Skill's `tracker/` folder). Otherwise give `tracker/spreadsheet/job-search-tracker.xlsx` as a download named `my-tracker.xlsx`, and tell them to keep it.
- Resume they want to use: ask them to attach it, rather than save it in a folder.
- Do not suggest uploading the Skill; they already have it.

## The resume PDF

Build it with `tools/build_resume.py` in code execution and give it as a download. If that cannot run, give `resume.md` as a download and tell them to paste it into a word processor and save it as a PDF; then run the resume checks by hand (no dashes or pronouns, every fact in the facts file, page count).

## What needs the desktop app

Sweeps of most career sites, and applying, need a browser Claude can control. Until the person is at a computer with the desktop app, suggest fit calls on postings they paste ("Is this a fit? [paste the posting and its link]"), resume work, company research and interview prep.

The full workspace folder, with everything set up for the desktop app, is at https://github.com/trotics/job-search-full-automation.
