# Stage 06: Mailbox check

Read the user's email for replies from employers and suggest status updates. Run only when the user asks ("check my email", "update the tracker from my email"). **Read only:** never reply, send, forward, delete, archive, label, mark as read, or move any email.

## Inputs

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

## Process

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

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 4 | A message that could match more than one listing | Which listing |
| 6 | Every proposed status change and history line | Yes, no, or a change, for each |

## Audit

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

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Approved changes | Tracker, `listings` | Status and history lines, as approved |
| Mailbox report | `output/[YYYY-MM-DD]-mailbox-report.md` | Window covered (from and to), deadlines first, what was found, what changed, what was left alone, what needs the user |
