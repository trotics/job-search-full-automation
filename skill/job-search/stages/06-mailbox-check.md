# Stage 06: Mailbox check

Read the user's email for replies from employers and suggest status updates. Run only when the user asks ("check my email", "update the tracker from my email"). Optional: it needs an email connector (for example Gmail or Outlook) connected in Claude. Without one, the user can paste or forward the emails instead.

**Read only.** Never reply, send, forward, delete, archive, label, mark as read, or move any email.

## Tracker access

- **Artifact:** read `listings` and `companies` with `ArtifactData`. After the user says yes, write `status` and `history` with `update`, after reading the row fresh.
- **Spreadsheet:** the same tabs and columns in `my-files/job-search-tracker.xlsx`.

## Inputs

- `rules.md` and `my-files/my-rules.md`.
- The user's email, through their connector. The period to check is from the user, or since the last mailbox check in the history, or the last 14 days.
- Listings at Applied, Followed up and Interview. Listings at To apply only to notice a reply about them (see step 4).

## Steps

1. Take a snapshot of the tracker.
2. Search the mailbox for each employer that has a listing at Applied or later, by company name and by the application system's sender (for example messages from the employer's careers site). Read only messages in the period.
3. Match each message to one listing: same company and, where the message names it, the same title or req id. If a message could match more than one listing, do not guess. Ask the user.
4. Sort each match:
   - **Confirmation** of an application ("we received your application"): no status change. Offer a history line.
   - **Interview request or scheduling:** propose `Interview`, with the date, time, format and names in the history line.
   - **Rejection:** propose `Rejected`.
   - **Offer:** propose `Offer`.
   - **Assessment or next step that is not an interview:** no status change. Offer a history line and tell the user.
   - **A reply about a listing still at To apply** (for example the user applied outside a session): no status change from this stage. Tell the user, and offer a history line. The user can then set the status directly (`python tools/check_tracker.py check backups/before.json backups/after.json --stage user`).
5. **Show the user every proposed change in one list** before writing anything, for example: "Example Health Co, Clinical Account Executive: Applied to Interview. Email from 2026-03-14 asks for a call on 3/18 at 10am with the regional manager." Wait for the user to say yes, no, or change it for each one.
6. Write only what the user approved: `status` (if changed) and one history line per listing, ending "from email dated YYYY-MM-DD, approved by the user".
7. Never change a listing based on an email the user did not approve. Never set Applied from an email. Applied comes only from stage 03 or the user.
8. Take an after snapshot and run `python tools/check_tracker.py check backups/before.json backups/after.json --stage mailbox` (snapshots: `references/tracker-columns.md`, "Checking by script").

## Outputs

- Approved status changes and history lines.
- A report saved to `reports/mailbox-<YYYY-MM-DD>.md`: what was found, what changed, what was left alone, and anything that needs the user (interviews to confirm, assessments to take).

## Done when

- [ ] No email was sent, replied to, deleted, moved, labeled or marked as read.
- [ ] Every status change was approved by the user in this session.
- [ ] `yourNotes` untouched (`check_tracker.py`).
- [ ] Report saved.
