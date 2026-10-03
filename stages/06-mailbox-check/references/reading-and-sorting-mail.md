# Reading and sorting mail

## Three ways in, best first

- **An email connector** (for example Gmail or Outlook) connected in Claude.
- **The user's webmail open in the browser**, with the user signed in themselves. Claude never signs in to email.
- **The user pastes or forwards** the emails.

**Read only.** Never reply, send, forward, delete, archive, label, mark as read, or move any email.

**Codes and passwords in email.** Verification codes, sign-in links and temporary passwords often show in message previews. Never copy them into the tracker, a report or the chat.

## Covering the window

- Start where the last mailbox check stopped (its history lines and report say "covered <from> to <to>"), and end now. With no earlier check, use the period the user gives, or the last 14 days. Write the window in this session's report, so the next check starts there and nothing is read twice or missed.
- **Search every folder, not just the inbox.** Many people have rules that file job email into folders, and some mail apps split the inbox (for example Focused and Other). Search all folders by date range. Date-bounded searches one day at a time are the most reliable on a busy mailbox (for example `received:` searches in Outlook, `after:` and `before:` in Gmail).
- Look for each employer that has a listing at Applied or later, by company name and by the application system's sender (messages often come from the platform, not the employer).
- **Webmail in the browser:** message lists load as you scroll ("virtualized"), so collect rows by scrolling the list by script until no new rows appear, then open each relevant message by a snippet of its preview text. If the list stops loading new rows, the browser window may be covered or hidden: ask the user to bring it to the front.

## Matching

Match each message to one listing: same company and, where the message names it, the same title or req id. If a message could match more than one listing, do not guess. Ask the user.

## Sorting each match

- **Confirmation** of an application ("we received your application"): no status change. Ask once whether the user wants these logged as history lines; many people do not.
- **Interview request or scheduling:** propose `Interview`, with the date, time, format and names in the history line.
- **Rejection,** including "we filled the position with another candidate": propose `Rejected`.
- **The role was cancelled or is "no longer available"** (not a rejection of the user): propose `expired`.
- **Offer:** propose `Offer`.
- **A follow-up the user sent** (found in their sent mail, to an employer with a listing at Applied): propose `Followed up`.
- **Assessment or next step that is not an interview** (online test, video interview, game-based assessment): no status change. Offer a history line, and put any **deadline** at the top of the report. Assessments are the user's to take.
- **Scheduling back-and-forth** (a recruiter offering times): replies are the user's to send. List it with any deadline.
- **Invitations from employers not on the target list** (for example a job site's "apply to this job" message): never act on them. List them for the user's call.
- **A reply about a listing still at To apply** (for example the user applied outside a session): no status change from this stage. Tell the user, and offer a history line. The user can then set the status directly (checked with `--stage user`).

## The proposed-changes list

One list, before writing anything, for example: "Example Health Co, Clinical Account Executive: Applied to Interview. Email from 2026-03-14 asks for a call on 3/18 at 10am with the regional manager." The user says yes, no, or change it for each one.

## What gets written

Only what the user approved: `status` (if changed) and one history line per listing, ending "from email dated YYYY-MM-DD, approved by the user". When several approved emails concern one listing (for example a confirmation and an interview request), combine them into that one line, naming each email's date. Never set Applied from an email: Applied comes only from the apply stage or the user.
