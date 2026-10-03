# Stage 00: Intake interview

Set up a new user's rules, or change an existing user's rules. Ends with `my-rules.md` saved, the tracker's `settings` record filled, and, if the user wants it, a starter answer bank.

## Inputs

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

## Process

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

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 3 | The complete `my-rules.md` | Approve, or what to change |
| 6 | The `settings` values | Save, or what to change |
| 7 | Each answer bank item | Save, change or skip |

## Audit

| Check | Pass Condition |
|-------|---------------|
| Questions | Every question was asked, one at a time, or the user skipped it |
| Approval | The user saw the complete `my-rules.md` and said approve before it was saved |
| Settings | `settings` was saved after the user said yes, and `check_tracker.py --stage intake` passes |
| Safety | No password, ID number or bank detail was asked for or stored |
| Lessons | The person was asked once what the session taught; only approved lessons were added |
| Next step | The session ended with the next thing to say, in quotes |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| The user's rules | `output/my-rules.md` | Markdown, in the template's shape, approved by the user |
| Settings record | Tracker, `settings` | One row, id `main` |
| Starter answer bank | Tracker, `answers` | One row per confirmed answer, if the user wanted them |
