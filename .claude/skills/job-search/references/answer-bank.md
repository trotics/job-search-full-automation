# Answer bank

The answer bank lives in the tracker, not in this Skill: the `answers` collection (artifact) or the `answers` tab (spreadsheet). Read it fresh at the start of every application session. It is the source of truth. Nothing in this file overrides it.

## How to use it

- When a form question matches an entry, answer from it without asking.
- When a question is worded unusually, or the entry's `useWhen` says to ask, confirm with the user before using the entry.
- Pay questions use the `Pay` entries: the wording where the form takes text, the single number where it needs one.
- Voluntary diversity questions use the `Voluntary` entries. With no entry, choose "I don't wish to answer" and tell the user.
- References come only from the `References` entries, in the order listed.
- Work history comes from the `Work history` entries and `my-files/resume.md`. They must agree. If they do not, ask the user.
- Add each new application-system account as an `Account` row: the website in `question`, the username in `answer`. **Never a password.**

## What never goes in the answer bank

- Passwords, security answers, one-time codes.
- Social Security numbers or other government ID numbers, driver's license numbers.
- Bank account, routing or card numbers.

## Autonomy

Any extra autonomy the user grants (for example auto-submit) lasts for one session only and is never saved here as a standing permission.
