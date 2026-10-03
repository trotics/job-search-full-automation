# Apply procedure

The detail behind each step of an application. How each platform's form behaves is in `application-techniques.md` and `application-platforms.md`.

## Auto-submit (off by default)

Auto-submit is off. The user can turn it on for **this session only** by writing a sentence like: "I turn on auto-submit for this session." It turns off when the session ends and never carries over. Even with auto-submit on:

- Every wall (account, password, code, CAPTCHA, ID number) is still the user's to do.
- No cover letter goes out without the user's sign-off on that letter.
- Legal text is still quoted to the user, and **Claude never ticks a legal agreement box itself**. A form with a legal agreement is never auto-submitted: the user ticks the box and submits.
- Anything not covered by the answer bank still goes to the user.
- The review summary is still posted in the chat as you submit.

## Order of work

Listings at To apply, High then Medium then Low, oldest `posted` first within each. Skip `On hold` listings unless the user says go.

## Before the form

- **Save the posting.** Copy the full posting text into `postingText`, even if fit review saved it already, and append: `YYYY-MM-DD posting text saved before applying.` The later copy wins, because postings change. Interview prep depends on this.
- **Re-check the fit** before the user does anything on the site, so they never create an account for a job that does not fit. If it now fails, tell the user and let them decide.
- **One tab per application.** Opening another address in a tab with a half-filled form throws the form away.
- **Apply links that submit on their own.** On some platforms, once the user is signed in, opening another job's apply link submits at once from the saved profile. On such a platform, opening the link **is** submitting: do it only after the user has said yes to that application.

## Uploading the resume

**Which file:** a tailored `resume-<listing id>.pdf` if the listing's history shows one was approved, otherwise `resume.pdf`. Ask once per session for access to the resume folder if you do not have it, then upload the file yourself.

Try these in order. Move to the next only if the one before it failed.

- **a. File upload tool.** Use Claude in Chrome's file upload tool on the form's file input, with the full path to the file. Do not click the input first: clicking opens the computer's own file picker.
- **b. Hidden input.** If the visible control is a button or a drag-and-drop zone, find the hidden `input[type=file]` behind it (with `read_page`, `find`, or a read-only check of the page) and use the file upload tool on it.
- **c. The computer's file picker.** If a click opened it, close it (Escape) and go back to b. Only if b finds no input: if the desktop control tool can work that dialog on this computer, use it to type the full path and confirm. If the tool's access level blocks it, stop this option.
- **d. Paste or type.** If the form offers "paste your resume" or "enter manually", use the text of `resume.md`, and flag it in the review summary.
- **e. Switch browsers.** If the active browser cannot upload at all (for example the built-in browser pane), move this application to Claude in Chrome and start again at a.
- **Never:** "Apply with LinkedIn" or any LinkedIn import; signing in to Google Drive, Dropbox or any other account to import a file; any step that needs a password, a code or a CAPTCHA. Those are walls.
- **Check after every upload.** The page must show the file name (or a preview), and it must be the file chosen above. If the site filled fields from the resume, check every one against the answer bank and fix any that are wrong.
- **Hand it to the user only when a to e all failed or hit a wall.** Say which options you tried and why each failed.

## Filling the form

- Fill from the answer bank and the resume. Invent nothing. For a question the answer bank does not cover, answer only if the answer is plainly safe and true from the resume. Otherwise ask the user.
- **Optional free-text boxes** ("Why are you interested?"): leave blank unless the user's rules say to fill them. If you fill one, draft it in the user's writing style and flag it.
- **Questions answered from the resume** rather than the answer bank: flag each one, and offer to add it to the answer bank.
- **Pay:** the answer bank's wording where text is allowed, the single number where one is required.
- **Voluntary questions** (gender, race, veteran, disability): from the answer bank. With no entry, choose "I don't wish to answer" or the closest option, and tell the user.
- **Links** (LinkedIn, portfolio): only when required, from the answer bank. Never open LinkedIn.
- **References:** from the answer bank, in its order. Never the user's current employer, or anyone the user's rules say never to contact.
- **Cover letter:** only if required. Draft it from the resume and the posting, in the user's style. Attach it only after the user signs off on that letter.
- **Legal text** (arbitration, waivers, non-compete, non-solicitation, broad permission to contact past employers): quote it to the user. **Never tick a legal agreement box yourself**, in any mode.
- **Walls** (create account, password, code, CAPTCHA, ID number): fill up to the wall, then hand the browser to the user. Never do the wall step, and never read what they typed. After any click that sends a code, take no more clicks until the user says they are through.

## Review, submit and record

- **Review summary:** every answer on the form, the upload (file name and method), and any auto-filled fields you corrected. Then stop. Submit only when the user says "submit" for this application, or clicks submit themselves.
- **A failed submit:** read the errors, fix the fields, submit **once** more. Repeated failed submits can trigger a code or a lockout.
- **After submitting:** capture the confirmation. Set `status` to `Applied` and `appliedDate` to today. Append a history entry: date, req id, title, company, location, pay if posted, the application system, the username if an account was used (never a password), the confirmation, the upload method written exactly as `upload: <method>` (for example `upload: hidden file input`; the check looks for `upload:`), and anything unusual.
- **Blocked while the user is away:** leave the status at To apply and append a history entry naming the exact step that blocked. Never work around it.
- **New accounts:** add to `answers` (topic `Account`, question = the site, answer = the username). Never a password.
- **Something new:** if an upload control behaved in a way `application-techniques.md` does not cover, tell the user and suggest a line to add there. General methods only, never employer names.

## Dry run

If the user asks for a dry run, go up to the review summary and stop. Write nothing to the tracker except `postingText` and its history line. Close the browser tab without submitting.

## The report

What went through, what is blocked and why, and what needs the user.
