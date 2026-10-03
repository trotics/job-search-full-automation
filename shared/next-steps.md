# Next steps

What to suggest when a session ends, so the person always knows what to say next. "Check my email" is short for "Check my email for employer replies". Wherever a line says "Check my email" and `my-setup.md` shows no email connector, say instead: "In a few days, paste any employer replies here and say 'Check these emails' (or connect your email in Claude's settings)." If the person has no browser Claude can control (no desktop app, see `no-folder.md`), never suggest "Let's apply" or "Run a sweep" as something to do now: say "When you are at the desktop app, say 'Let's apply'", and meanwhile suggest "Build my resume" (if there is no resume yet) or "Is this a fit? [paste a posting and its link]". Suggest only; never start the next stage yourself. Keep it to one or two lines, with the exact words to say in quotes, and pick the line that fits what just happened.

## After the interview

- They chose "build new" or "improve mine" for the resume: "Say 'Build my resume'. After that, 'Suggest employers that fit my background'."
- They have a resume and no employers yet: "Say 'Suggest employers that fit my background', then 'Run a sweep'."
- They have a resume and just added employers: "Say 'Run a sweep'."

## After the resume

- No employers on the target list yet: "Say 'Suggest employers that fit my background'."
- Listings at To apply: "Say 'Let's apply'. Your new resume will be used."
- Otherwise: "Say 'Run a sweep'."

## After company research

- Employers were added: offer a sweep of them ("Say 'Sweep [names]'").
- A company deep dive before applying or an interview: "Say 'Apply to the [company] [title] listing'" or "Say 'Prep me for my interview with [company]'".
- An industry map: "Say 'Add these employers to my target list: [names]'" for any they liked.
- Role research: if the role fits, "Say 'I want to change my rules: add [title]'".

## After a sweep or a fit call

- No resume yet (no `resume.pdf`): "Say 'Build my resume' first, then 'Let's apply'."
- New listings at To apply: give the count, then "Say 'Let's apply' when you have time to sit with it."
- Manual employers: list them, and ask the person to open those sites in their own browser when they can.
- Close calls in the report: ask the person to decide each one.
- Nothing new: "Nothing fit this time. Say 'Suggest employers that fit my background' for more employers, or run another sweep in about a week."

## After applying

- A dry run: "Say 'Apply to the [company] [title] listing' when you want to do it for real."
- A fill sheet was given (no browser): "Fill it in and submit in your browser, then tell me 'I submitted it' with the confirmation, and I will mark it Applied."
- Listings still at To apply: "Say 'Let's apply' to keep going."
- Applications went in: "In a few days, say 'Check my email' to catch replies."
- Their rules ask for outreach drafts: "Say 'Run outreach on the [company] listing' if you want a note to the hiring manager."

## After outreach

- The listing is still at To apply: "Apply first: say 'Apply to the [company] [title] listing'. Then send the drafts yourself."
- Otherwise: "Send the drafts yourself when you are ready. In a few days, say 'Check my email'."

## After interview prep

"Good luck. After the interview, say 'Check my email' to log the next step."

## After the mailbox check

- An interview was found: "Say 'Prep me for my interview with [company] on [day]'."
- Deadlines (assessments, scheduling): list them first, with dates.
- A rejection: one kind line, then the next most useful thing below.
- Listings still at To apply: "Say 'Let's apply'."
- Nothing new and no sweep in the last week: "Say 'Run a sweep' to look for new listings."

## A returning person with no request

Find the tracker in `my-setup.md` and read `listings` and `coverage` as `tracker-access.md` says (no snapshot needed: this only reads). An employer with no `coverage` row has never been swept, unless its industry is excluded (those are skipped on purpose and do not count). Then suggest the one most useful thing:

1. A deadline or an interview coming up (a listing at Interview whose newest history line gives a future date, or a deadline in the latest mailbox report): name it with its date first. If no prep file for it exists in `stages/05-interview-prep/output/`, add "Say 'Prep me for my interview with [company] on [day]'"; if one exists, just wish them luck. For an assessment or a reply to send, say what to do and by when.
2. Things waiting on the person: close calls in the latest sweep or fit report that they have not decided, and employers whose `coverage` says `manual` or `LEAD`. Name them in one line each and ask them to decide or open the site.
3. Listings at To apply: "Say 'Let's apply'."
4. Applications in and no mailbox check in the last week: "Say 'Check my email'."
5. No sweep in the last week: "Say 'Run a sweep'."
6. Otherwise: "Say 'Suggest employers that fit my background'."
