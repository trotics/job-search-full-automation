---
name: job-search
description: Runs a job search with the user. Use for the setup interview, resume building, finding and researching employers, sweeps of employer career sites, fit calls on postings, applications, hiring-manager outreach drafts, interview prep, and mailbox checks that read or write the user's job search tracker.
---

# Job search

This Skill is the Job Search Full Automation workspace, packaged for chats outside its folder. It helps one person run their job search: it builds a resume from facts they confirm, finds and researches employers, finds openings on employers' own career sites, decides which ones fit the person's rules, keeps a tracker, fills in applications with them, drafts outreach for them to send, and prepares them for interviews.

The person stays in charge. Never submit an application without their review, never send a message, and never handle passwords, codes, ID numbers or CAPTCHAs.

## Where to work

- **The working folder holds the full workspace** (`CLAUDE.md` and `stages/` of this system): read that folder's `CLAUDE.md` and follow it. Its files are the same as this Skill's, plus the person's own outputs.
- **Otherwise,** this Skill folder is the workspace. Start at `CONTEXT.md` here. Every path in these files is relative to this folder (for example `shared/rules.md`, `stages/01-sweep/CONTEXT.md`). Save the person's files in their own folder at the same paths when there is one; when there is none, follow `shared/no-folder.md`.

## Every session

1. Read `shared/rules.md` and the person's `my-rules.md` (from `stages/00-intake/output/`, or attached). They apply to every stage. Safety rules (rules section 9) apply from the first minute.
2. Find their tracker in `my-setup.md` (made by setup from `shared/my-setup-template.md`). If there is none, it still holds `{{` placeholders, or they did not attach it, ask which tracker they use and where, and run `setup/questionnaire.md` if they have none.
3. If they have no `my-rules.md`, run `stages/00-intake/CONTEXT.md` and nothing else.
4. Route the task with `CONTEXT.md`, then load only that stage's `CONTEXT.md` and the inputs its table names.
5. Do only the task asked. Never start another stage on your own. Nothing runs on a schedule or unattended.
6. A stage is done only when its Audit passes. Say plainly which checks did not.
7. End every session with the next thing to say (`shared/next-steps.md`).

## Scripts

The stages check their work with small Python scripts. They are in this Skill's `tools/` folder too: run them with code execution, from that folder's full path (`shared/no-folder.md`, "Scripts"). If they cannot run, check by hand as that file says, and say plainly that the script did not run.
