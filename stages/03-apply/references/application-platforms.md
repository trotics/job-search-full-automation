# Application platforms: form by form

How each platform's application form behaves. General methods are in `application-techniques.md`. Add what a session learns here (with the user's OK). Edit the platform's section in place. Never add employer names, the user's details or dates.

## Greenhouse

- Usually no account and no CAPTCHA. Form address: `job-boards.greenhouse.io/embed/job_app?for=<board>&token=<job id>`. It works even when the company wraps the board in its own site.
- Read the posting from `boards-api.greenhouse.io/v1/boards/<board>/jobs/<id>` (open it in the tab; a fetch from the form page is blocked).
- Text inputs take the setter; **textareas need real typing**.
- **Phone with a required country:** first click the Country control, type the country, click the option, then type the phone.
- react-select dropdowns: one real click on the control, wait about half a second, then click the `.select__option` with matching text. Read the result from `.select__single-value`. Do not call React internals: that can wipe the attached resume.
- Attach the resume last and check it is still showing before Submit.

## Lever

No account. Upload the resume first; it fills name, email, phone and current employer. An invisible CAPTCHA usually does not challenge; a visible one is a wall.

## Ashby

No account. The phone must be typed for real. Yes/No buttons and radios need real clicks; check each took. Location and source are comboboxes: click, type, click the option. Usually ends with an agreement radio: read it.

## Workday

- **One account per employer** on most boards (the user creates it). Some boards allow applying as a guest.
- Start at `<job address>/apply/autofillWithResume`. After the resume is read, fix every work-history entry.
- Dropdowns are buttons that open a list: click the button, wait about a second, click the `[role=option]` with matching text. Pick questionnaire buttons with `button[id^=primaryQuestionnaire]`, not by position: the page header has a button that matches a looser selector and shifts every answer by one. Read each question beside its answer before continuing.
- Option lists can pile up after several opens; pick text that is unique, one field per call, and press Escape between.
- "How did you hear" is either a plain list or a multi-level prompt: click it, type the option text, press Return, and check the selected item appears.
- Address line 1 and some name fields must be typed for real. Questionnaire textareas (salary, "why this role") must be typed for real.
- The disability self-identification date ("CC-305"): open the calendar and click today's cell.
- **"Use My Last Application"** (`<job address>/apply/useMyLastApplication`) on a second job at the same employer carries the work history forward; the source and questionnaire still need answering.
- Some Next buttons ignore a script click: use a real click at the button's position and confirm the step number after.
- **Never press Discard** on the "Discard application?" dialog; choose Continue. If a field is corrupted, reload the apply address: drafts keep earlier steps.
- Pop-up assessments may not open inside the browser pane. Capture the address the button tries to open, open it in its own tab for the user, then reload the application to check the step registered.
- After submitting, optional follow-up tasks may appear (update personal information, review terms): leave them for the user.

## iCIMS

- Login, password and CAPTCHA (often hCaptcha at "Submit profile") are the user's.
- The profile form sits in a same-origin frame (`iframe#icims_content_iframe`): work in its `contentDocument`, and attach the resume with that frame's own `File` and `DataTransfer`.
- Uploading the resume reloads the frame and can wipe fields: re-check everything after.
- Lazy dropdowns: dispatch mousedown, mouseup and click on the dropdown anchor, type in its search box if it has one, then click the result item.
- Follow-up forms (disability, veteran, acknowledgements) can load in a cross-origin frame. Complete them **inside the application tab** where possible; on some boards, completing them in a separate tab leaves the application "incomplete".
- Sessions time out after roughly 20 to 30 idle minutes; drafts may keep only some answers.
- **After sign-in, some boards submit an application the moment its apply link opens** (see "Before you start").

## Paylocity

- No account. "Fill out application with my resume" reads the file; check every field, add missing jobs by hand.
- Dropdowns: real click on the control, wait about 2 seconds, click the list item. The acknowledgement checkbox needs a real click. Month/year dates need text insertion.
- Pick the address from its suggestions, then set the start date (picking the address wipes it).
- Some forms require supervisor contact details for every job marked "may contact".

## BambooHR

No account. The state list may need real clicks through a button menu (`find` the control, click, `find` the option, click). Dates: click and type, then Escape. Submit is followed by a CAPTCHA checkbox: the user ticks it.

## Jobvite

No account. Usually several pages: consent, contact and resume, self-identification with a typed name and date, screening questions, then a visible CAPTCHA at send (the user). The file upload tool may refuse the control; attaching by page script works. Next may need a real click.

## Phenom (apply)

- No account on some boards. Read the posting from `phApp.ddo.jobDetail.data.job`.
- Fill every required field before the first Next: once a field is flagged, picking a value may not clear the error until a related field is retyped.
- An invisible CAPTCHA can reject a scripted submit: the user presses Submit. Reloading the apply address restores the draft and fixes buttons left disabled.

## UKG Pro Recruiting and UKG Ready

- UKG Pro: an account at "Apply now" (the user). One long page; the resume reader often puts employer and location in the title.
- UKG Ready on a new employer: no password until "Sign & submit", which asks for a password as the signature (the user). Once a profile exists, the board asks the user to sign in.

## Dayforce

- An account (Dayforce ID) or "apply without an account" on some boards.
- Creating the account: the agree box counts only after both policy links are clicked, and those links can open in the same tab and wipe the form. Have the user open them in a new tab.
- Ant Design form: open selects with a mousedown on `.ant-select-selector`, wait, click the option. Press each section's Update button and read the error messages after each.
- **Next is slow:** click once, wait about 5 seconds, confirm the page number. A double advance can skip a page unanswered.

## ADP Workforce Now and ADP MyJobs

- Sign-in is by a texted or emailed code (the user). One emailed code may never arrive; the text option is often more reliable.
- Radios are web components; source dropdowns and self-identification need real clicks.
- Text inputs on the questions page often register only when typed for real.
- The last step can be an electronic signature: stop there. The user ticks the box, types their name and submits. Some flows have no review page: the last Next submits, so stop before it for the user's review.
- Some legacy ADP flows ask for the last four digits of a Social Security number and a birth date (a "rehire check"): a wall. The user decides.

## Oracle Cloud Candidate Experience

- Often no account; a returning email may get a PIN or emailed code (the user).
- ZIP fields are autocompletes: type the ZIP in two parts so the list filters, then click the matching row.
- Pill-button questions take a script click. Comboboxes: focus, insert the text, wait, click the matching cell.
- The final e-signature can be an employment agreement with arbitration: quote it first.

## SuccessFactors

- An account (the user). Picklists: click the select button, then the matching option inside the list named by the input's `aria-owns`. Dates are calendar widgets that take typed `MM/DD/YYYY`.
- Some flows require the current supervisor's name and title with no "may we contact" choice: raise it with the user.

## Hirebridge, ClearCompany, isolved, Cornerstone, Paycom, Paycor and others

- **Hirebridge:** some boards offer a quick apply with no password; others ask for an existing profile's password (the user). The resume upload reloads the page: upload first.
- **ClearCompany:** no account on a first visit; a second visit to the same job emails a sign-in link (the user). Parsed rows arrive late; wait, then fix. Some forms require a birth date and Social Security number: a wall.
- **isolved Hire:** an account is created for the user after step 2 and a password is asked (the user). A returning email gets a secure code.
- **Cornerstone:** the first application creates a profile with a CAPTCHA (the user); later applications submit directly.
- **Paycom:** values set by script on selects, dates and autocompletes are wiped on submit. Use arrow keys on selects, type dates digit by digit, click autocomplete suggestions, real-click the acknowledgement.
- **Paycor:** plain form; setters work.
- **SmartRecruiters:** may show bot-check questions: the user answers.
- **Conversational (chat) apply flows:** answer from the answer bank; anything new goes to the user.
