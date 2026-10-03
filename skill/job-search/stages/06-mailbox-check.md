# Stage 06: Mailbox check

Read the user's email for replies from employers and suggest status updates. Run only when the user asks ("check my email", "update the tracker from my email"). It works three ways, best first:

- **An email connector** (for example Gmail or Outlook) connected in Claude.
- **The user's webmail open in the browser**, with the user signed in themselves. Claude never signs in to email.
- **The user pastes or forwards** the emails.

**Read only.** Never reply, send, forward, delete, archive, label, mark as read, or move any email.

**Codes and passwords in email.** Verification codes, sign-in links and temporary passwords often show in message previews. Never copy them into the tracker, a report or the chat.

## Tracker access

- **Artifact:** read `listings` and `companies` with `ArtifactData`. After the user says yes, write `status` and `history` with `update`, after reading the row fresh and passing its `version` as `if_version`.
- **Spreadsheet:** the same tabs and columns in `my-files/job-search-tracker.xlsx`.

## Inputs

- `rules.md` and `my-files/my-rules.md`.
- The user's email, through their connector. The period to check is from the user, or since the last mailbox check in the history, or the last 14 days.
- Listings at Applied, Followed up and Interview. Listings at To apply only to notice a reply about them (see step 4).

## Steps

1. Take a snapshot of the tracker.
2. **Cover a clear window.** Start where the last mailbox check stopped (its history lines and report say "covered <from> to <to>"), and end now. Write the window in this session's report, so the next check starts there and nothing is read twice or missed.
3. **Search every folder, not just the inbox.** Many people have rules that file job email into folders, and some mail apps split the inbox (for example Focused and Other). Search all folders by date range. Date-bounded searches one day at a time are the most reliable on a busy mailbox (for example `received:` searches in Outlook, `after:` and `before:` in Gmail).
4. Within the window, look for each employer that has a listing at Applied or later, by company name and by the application system's sender (messages often come from the platform, not the employer).
5. **Webmail in the browser:** message lists load as you scroll ("virtualized"), so collect rows by scrolling the list by script until no new rows appear, then open each relevant message by a snippet of its preview text. If the list stops loading new rows, the browser window may be covered or hidden: ask the user to bring it to the front.
6. Match each message to one listing: same company and, where the message names it, the same title or req id. If a message could match more than one listing, do not guess. Ask the user.
7. Sort each match:
   - **Confirmation** of an application ("we received your application"): no status change. Offer a history line.
   - **Interview request or scheduling:** propose `Interview`, with the date, time, format and names in the history line.
   - **Rejection,** including "we filled the position with another candidate": propose `Rejected`.
   - **The role was cancelled or is "no longer available"** (not a rejection of the user): propose `expired`.
   - **Offer:** propose `Offer`.
   - **A follow-up the user sent** (found in their sent mail, to an employer with a listing at Applied): propose `Followed up`.
   - **Assessment or next step that is not an interview** (online test, video interview, game-based assessment): no status change. Offer a history line, and put any **deadline** at the top of the report. Assessments are the user's to take.
   - **Scheduling back-and-forth** (a recruiter offering times): replies are the user's to send. List it with any deadline.
   - **Confirmations of applications:** no status change. Ask once whether the user wants these logged; many people do not.
   - **Invitations from employers not on the target list** (for example a job site's "apply to this job" message): never act on them. List them for the user's call.
   - **A reply about a listing still at To apply** (for example the user applied outside a session): no status change from this stage. Tell the user, and offer a history line. The user can then set the status directly (`python tools/check_tracker.py check backups/before.json backups/after.json --stage user`).
8. **Show the user every proposed change in one list** before writing anything, for example: "Example Health Co, Clinical Account Executive: Applied to Interview. Email from 2026-03-14 asks for a call on 3/18 at 10am with the regional manager." Wait for the user to say yes, no, or change it for each one.
9. Write only what the user approved: `status` (if changed) and one history line per listing, ending "from email dated YYYY-MM-DD, approved by the user".
10. Never change a listing based on an email the user did not approve. Never set Applied from an email. Applied comes only from stage 03 or the user.
11. Take an after snapshot and run `python tools/check_tracker.py check backups/before.json backups/after.json --stage mailbox` (snapshots: `references/tracker-columns.md`, "Checking by script").

## Outputs

- Approved status changes and history lines.
- A report saved to `reports/mailbox-<YYYY-MM-DD>.md`: the window covered (from and to), deadlines first, what was found, what changed, what was left alone, and anything that needs the user (interviews to confirm, assessments to take, replies to send).

## Done when

- [ ] No email was sent, replied to, deleted, moved, labeled or marked as read.
- [ ] Every status change was approved by the user in this session.
- [ ] `yourNotes` untouched (`check_tracker.py`).
- [ ] The window covered is written in the report, and no code, sign-in link or password was copied anywhere.
- [ ] Report saved.
