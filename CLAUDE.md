# Job Search Full Automation

A job search system for the person you are working with. It finds jobs on employers' own career sites, checks each against the person's rules, keeps a tracker, builds a resume from facts they confirm, and fills in applications with them. Nothing is ever submitted or sent without their review. Talk to them in plain, friendly language; most people using this are not technical.

This folder is an ICM workspace: the folders are the workflow. Each stage has a `CONTEXT.md` contract that says what to read, what to do, what to check and where to save.

## Folder Map

```
job-search-full-automation/
├── CLAUDE.md              (you are here)
├── CONTEXT.md             (task routing)
├── setup/
│   └── questionnaire.md   (one-time setup: tracker, Python, browser)
├── shared/                (used by every stage: rules, tracker guide, answer bank, prompts, my-setup.md)
├── stages/
│   ├── 00-intake/         (interview: the person's own rules)
│   ├── 01-sweep/          (check employers' career sites for listings)
│   ├── 02-fit-review/     (does one posting fit the rules)
│   ├── 03-apply/          (fill in applications, the person reviews)
│   ├── 04-outreach/       (hiring-manager drafts, only when asked by name)
│   ├── 05-interview-prep/ (prep file for a named interview)
│   ├── 06-mailbox-check/  (read replies, propose status changes)
│   ├── 07-resume/         (resume from confirmed facts)
│   └── 08-company-research/ (find and research employers)
├── tracker/               (the tracker page, the spreadsheet template, the person's copy and backups)
├── tools/                 (scripts that check the work and build files)
├── tests/                 (self-tests for the scripts)
└── examples/              (a full test run with a made-up user)
```

Every stage folder holds `CONTEXT.md`, `references/` (how to do it) and `output/` (what it made). Git never shares anything in `output/`, `shared/my-setup.md`, `tracker/my-tracker.xlsx` or `tracker/backups/`.

## Triggers

| Keyword | Action |
|---------|--------|
| `setup` | Run `setup/questionnaire.md`. Also when the person says something like "look at this folder and set me up", or when `shared/my-setup.md` is missing or still holds `{{` placeholders |
| `status` | Show which stages have output |

### How `status` works

Scan `stages/*/output/`. A stage whose output folder holds files other than `.gitkeep` is COMPLETE (list the file names); otherwise PENDING. Fit reviews run inside a sweep are reported in the sweep's report, so 02 can stay PENDING while 01 is COMPLETE; say so. Exceptions: if `stages/07-resume/output/` holds a resume but no `resume-facts.md`, show 07 as YOURS when `my-setup.md` says "use mine", and PENDING otherwise (an old resume waiting to be improved). Employers added outside a stage leave 08 PENDING. A stage whose only output says nothing was done (for example "0 listings qualified") shows RAN, not COMPLETE; so does an apply stage whose only output is a dry run. Also say whether setup is done (`shared/my-setup.md` exists with no `{{` left). Render:

```
Pipeline Status: job-search-full-automation   (setup: DONE)

  [00-intake] --> [07-resume] --> [08-company-research] --> [01-sweep] --> [02-fit-review]
     STATUS          STATUS             STATUS                STATUS          STATUS
  --> [03-apply] --> [04-outreach] --> [05-interview-prep] --> [06-mailbox-check]
        STATUS          STATUS               STATUS                  STATUS
```

## Which situation is this?

- **Setup not done** (`shared/my-setup.md` is missing or has `{{` placeholders): run `setup`, which ends by starting stage 00.
- **Setup done, no `stages/00-intake/output/my-rules.md`:** run stage 00.
- **Both exist:** a returning user. If they did not say what they want, read the tracker and suggest the one most useful thing (`shared/next-steps.md`, "A returning person with no request"), then mention the other common choices from `shared/prompts.md`.

## Every session

1. Read `shared/rules.md` and `stages/00-intake/output/my-rules.md` (when it exists). They apply to every stage. Safety rules (rules section 9) apply from the first minute: never create accounts, type passwords, enter ID or bank numbers, solve CAPTCHAs, send messages, open LinkedIn, contact their current employer, or submit an application without the person's review.
2. Route the task with `CONTEXT.md`, then load only that stage's `CONTEXT.md` and the inputs its table names.
3. Do only the task asked. Never start another stage on your own. Every stage is started by the person in a live session; nothing runs on a schedule.
4. A stage is done only when its Audit passes. Say plainly which checks did not.
5. End every session with the next thing to say (`shared/next-steps.md`).

## Do not

- Do not edit files in `shared/`, `stages/*/references/`, `stages/*/CONTEXT.md`, `tools/`, `tracker/` (except the person's own copy and backups) or `tests/` unless the person asks to change how the system works, or approves a lesson (`shared/lessons.md`). `shared/my-setup.md` is written only by `setup`, from `shared/my-setup-template.md`.
- Do not run `git` commands that push, publish or change history.
- Do not put the person's details anywhere except `stages/*/output/`, `shared/my-setup.md`, `tracker/my-tracker.xlsx`, `tracker/backups/` and their own tracker.
