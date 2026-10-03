# Stage 03: Apply

Fill in applications for listings at To apply, live with the user. **The user reviews every application before it is submitted.**

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Stage 00 | `../00-intake/output/my-rules.md` | Full file | The user's rules and writing style |
| Stage 07 | `../07-resume/output/resume.pdf` | The file | The resume to upload (or the user's own file saved there at setup) |
| Stage 07 | `../07-resume/output/resume.md` | Full file | Resume text for form fields |
| Stage 07 | `../07-resume/output/resume-[listing-id].pdf` | Only if the listing's history names it | An approved tailored resume |
| Shared | `../../shared/rules.md` | Sections 7 to 10 | Status rules, autonomy, safety, writing |
| Shared | `../../shared/my-setup.md` | Full file | Tracker kind and location, Python command, browser, email connector |
| Shared | `../../shared/tracker-access.md` | Full file | Reading, writing and the check |
| Shared | `../../shared/recurring-mistakes.md` | Full file | Read before any tracker write |
| Shared | `../../shared/answer-bank.md` | Full file | How to use the answer bank |
| Shared | `../../shared/next-steps.md` | "After applying" | What to suggest when the session ends |
| Tracker | `listings`, `answers` | Listings at To apply; all answers | What to apply to, and the answers |
| Reference | `references/apply-procedure.md` | Full file | Auto-submit, upload order, filling, review, recording |
| Reference | `references/application-techniques.md` | Full file | How forms behave, upload methods, legal text, walls |
| Reference | `references/application-platforms.md` | The platform's section | Read before each form |
| Reference | `references/claude-in-chrome-setup.md` | Full file | Only if Claude in Chrome is not connected |

Apply in **Claude in Chrome** when it is connected. It can upload files; the built-in browser pane cannot.

## Process

1. Take a tracker snapshot, once for the whole session. Then pick the next listing (`apply-procedure.md`, "Order of work").
2. **Still live?** Open the posting on the employer's own site. If it is gone, set `expired` or `filled` with a history entry and move on.
3. Save the posting text and re-check the fit (`apply-procedure.md`, "Before the form").
4. Upload the resume, trying the methods in order, and check the upload on the page.
5. Fill the form from the answer bank and the resume. Quote legal text to the user. Hand every wall to the user.
6. **[Checkpoint]** Show the review summary and stop.
7. Submit only on the user's "submit" (or under auto-submit turned on in writing this session).
8. Record the result: `Applied`, `appliedDate`, and the history entry with `upload: <method>`. Add any new account username to `answers`.
9. Pick the next listing and repeat from step 2, as long as the user wants. Do not take a new snapshot.
10. Take an after snapshot and run the check with `--stage apply`.
11. Run the audit below, then save the report.
12. End by suggesting the next step in one or two lines (`next-steps.md`, "After applying"). Suggest only; do not start it.

For a **dry run**, stop at step 6 and follow `apply-procedure.md`, "Dry run".

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 3 | A posting that no longer fits | Apply anyway or skip |
| 5 | Legal text, walls, any question the answer bank does not cover, any cover letter | Their answer, their wall step, their sign-off |
| 6 | The review summary of every answer and the upload | "Submit", changes, or skip |

## Audit

| Check | Pass Condition |
|-------|---------------|
| Review | Every submitted application was reviewed by the user (or under auto-submit turned on in writing this session), with a confirmation and a history entry |
| Posting text | Every listing worked has `postingText` saved |
| Upload | Every upload was checked on the page (right file name), and every auto-filled field was checked against the answer bank |
| Safety | No password, code or ID number was typed by the session or written anywhere. No LinkedIn or cloud-account import was used |
| Cover letters | None went out without the user's sign-off |
| Check | `check_tracker.py --stage apply` passes, and `yourNotes` is untouched |
| Next step | The session ended with the next thing to say, in quotes |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Applied listings | Tracker, `listings` | Status Applied, `postingText`, `appliedDate`, history with the upload method |
| Blocked listings | Tracker, `listings` | Left at To apply, with a history entry naming the block |
| Apply report | `output/[YYYY-MM-DD]-apply-report.md` | What went through, what is blocked and why, what needs the user |
