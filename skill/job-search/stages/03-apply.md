# Stage 03: Apply

Fill in applications for listings at To apply, live with the user. **The user reviews every application before it is submitted.**

## Auto-submit (off by default)

Auto-submit is off. The user can turn it on for **this session only** by writing a sentence like: "I turn on auto-submit for this session." It turns off when the session ends and never carries over. Even with auto-submit on:

- Every wall (account, password, code, CAPTCHA, ID number) is still the user's to do.
- No cover letter goes out without the user's sign-off on that letter.
- Legal text is still quoted to the user, and **Claude never ticks a legal agreement box itself**. A form with a legal agreement is never auto-submitted: the user ticks the box and submits.
- Anything not covered by the answer bank still goes to the user.

## Browser

Apply in **Claude in Chrome** when it is connected. It can upload files. The app's built-in browser pane cannot upload files, so if you start there and reach an upload, switch to Claude in Chrome (upload step 4e).

## Tracker access

- **Artifact:** read `listings` and `answers` with `ArtifactData`. Write the listing's `status`, `postingText`, `appliedDate` and `history` with `update`, after reading the row fresh. Add new accounts to `answers` with `set`.
- **Spreadsheet:** the same tabs and columns in `my-files/job-search-tracker.xlsx`.

## Inputs

- `rules.md` and `my-files/my-rules.md`.
- Listings at To apply, worked in priority order (High, then Medium, then Low), oldest `posted` first within each. Skip `On hold` listings unless the user says go.
- The answer bank: `answers` in the tracker (see `references/answer-bank.md`).
- `my-files/resume.md` for text fields, and `my-files/resume.pdf` to upload. Ask once per session for access to `my-files/` if you do not have it, then upload the resume yourself.
- `references/application-techniques.md`: how upload controls and auto-fill behave.

## Steps

1. **Still live?** Open the posting on the employer's own site. If it is gone, set `expired` or `filled` with a history entry and move on.
2. **Save the posting.** Copy the full posting text into `postingText` now, even if fit review saved it already, and append a history line: `YYYY-MM-DD posting text saved before applying.` The later copy wins, because postings change. Interview prep depends on this.
3. **Re-check the fit.** Read the posting in full before the user does anything on the site. Re-check it against the rules. If it now fails, tell the user and let them decide.
4. **Upload the resume.** Try these in order. Move to the next only if the one before it failed.
   - **Which file:** `my-files/resumes/resume-<listing id>.pdf` if the listing's history shows a tailored resume was approved (stage 07 part D), otherwise `my-files/resume.pdf`.
   - **a. File upload tool.** Use Claude in Chrome's file upload tool on the form's file input, with the full path to that file. Do not click the input first: clicking opens the computer's own file picker.
   - **b. Hidden input.** If the visible control is a button or a drag-and-drop zone, find the hidden `input[type=file]` behind it (with `read_page`, `find`, or a read-only check of the page) and use the file upload tool on that input directly.
   - **c. The computer's file picker.** If clicking a button opened the computer's own file picker, do not get stuck in it. Close it (Escape) and go back to b. Only if b finds no input: if the desktop control tool can work that dialog on this computer, use it to type the full path to `resume.pdf` and confirm. If the tool's access level blocks it, stop this option.
   - **d. Paste or type.** If the form offers "paste your resume" or "enter manually", use the text of `my-files/resume.md`, and flag this in the review summary.
   - **e. Switch browsers.** If the active browser cannot upload at all (for example the built-in browser pane), move this application to Claude in Chrome and start again at a.
   - **Never take these routes:** "Apply with LinkedIn" or any LinkedIn import; signing in to Google Drive, Dropbox or any other account to import a file; any step that needs a password, a code or a CAPTCHA. Those are walls, and walls stay the user's.
   - **Check after every upload.** The page must show the file name (or a preview of the resume it read), and it must be the file chosen above (`resume.pdf`, or the approved tailored file), not another file. If the site filled in form fields from the resume, check every one against the answer bank and fix any that are wrong. A wrong auto-fill is a common way applications go bad.
   - **Hand it to the user only when a to e all failed or hit a wall.** Say which options you tried and why each one failed, then pick up the form after the user attaches the file.
5. **Fill the form** from the answer bank and the resume. Invent nothing. For a question the answer bank does not cover, answer only if the answer is plainly safe and true from the resume. Otherwise ask the user.
   - **Optional free-text boxes** (for example "Why are you interested?"): leave them blank unless the user's rules say to fill them. If you fill one, draft it in the user's writing style and flag it in the review summary.
   - **Questions answered from the resume** rather than the answer bank (for example "years of B2B sales"): flag each one in the review summary, and offer to add it to the answer bank.
6. **Pay questions:** use the answer bank's Pay entries: the wording where text is allowed, the single number where one is required.
7. **Diversity and voluntary questions** (gender, race, veteran, disability): answer from the answer bank. If it has no entry, choose "I don't wish to answer" or the closest option, and tell the user.
8. **Links** (LinkedIn profile, portfolio): enter only when the field is required, from the answer bank. Never open LinkedIn.
9. **References:** from the answer bank, in the order it lists them. Never list the user's current employer, or anyone the user's rules say never to contact.
10. **Cover letter:** if the form requires one, draft it from the resume and the posting, in the user's writing style. Show it to the user. It is attached only after the user signs off on that letter.
11. **Legal text** (arbitration, waivers, non-compete, non-solicitation, broad permission to contact past employers): quote it to the user. **Never tick a legal agreement box yourself**, in any mode. The user reads it and ticks it, or decides not to apply.
12. **Walls** (create account, password, verification code, CAPTCHA, Social Security number or other ID): fill everything up to the wall, then hand the browser to the user. Continue after they are through. Never do the wall step yourself, and never read what they typed.
13. **Review before submit.** Show the user a summary of every answer on the form, including the upload (file name and method) and any auto-filled fields you corrected, and stop. Submit only when the user says "submit" for this application, or clicks submit themselves. Under auto-submit, still post the summary in the chat as you submit.
14. **After submitting:** capture the confirmation (confirmation page text or number). Set `status` to `Applied` and `appliedDate` to today. Append a history entry: date, req id, title, company, location, pay if posted, the application system used, the username if an account was used (never a password), the confirmation, the upload method (for example "upload: hidden file input"), and anything unusual.
15. **If blocked and the user has stepped away** (for example they left the session at a wall): leave the status at To apply and append a history entry naming the exact step that blocked. Never work around the block.
16. Add any new account to `answers` (topic `Account`, question = the site, answer = the username). Never a password.
17. If an upload control behaved in a way `references/application-techniques.md` does not cover, tell the user and suggest a line to add there. General methods only, never employer names.
18. Take an after snapshot and run `python tools/check_tracker.py check backups/before.json backups/after.json --stage apply` (snapshots: `references/tracker-columns.md`, "Checking by script").

## Dry run

If the user asks for a dry run, do steps 1 to 13 and stop at the review summary. Write nothing to the tracker except `postingText` and its history line (step 2). Close the browser tab without submitting.

## Outputs

- Listings set to Applied, each with `postingText`, `appliedDate` and a history entry that names the upload method.
- Blocked listings left at To apply, each with a history entry.
- A report saved to `reports/apply-<YYYY-MM-DD>.md`: what went through, what is blocked and why, what needs the user.

## Done when

- [ ] Every submitted application was reviewed by the user (or was under auto-submit turned on in writing this session) and has a confirmation and a history entry.
- [ ] Every listing worked has `postingText` saved.
- [ ] Every upload was checked on the page (right file name) and every auto-filled field was checked against the answer bank.
- [ ] No password, code or ID number was typed by the session or written anywhere. No LinkedIn import and no cloud-account import was used.
- [ ] No cover letter went out without the user's sign-off.
- [ ] `yourNotes` untouched (`check_tracker.py`).
- [ ] Report saved.
