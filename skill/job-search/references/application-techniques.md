# Application techniques

How application forms behave, platform by platform, and how to fill them correctly. Learned from well over a hundred real applications. Read it before an apply session (stage 03). Reading job boards is in `board-techniques.md`.

Add what a session learns here (with the user's OK): a new platform, a new workaround, a trick that stopped working. Edit the platform's section in place. Never add employer names, the user's details or dates.

## Before you start

- **Read every posting in full before the user creates any account.** Many promising titles turn out, once read, to be senior or out-of-scope roles. Creating accounts for those wastes the user's time.
- **Walls are the user's** (rules 9): accounts, passwords, one-time codes, CAPTCHAs, ID numbers. Fill everything up to the wall, hand the browser over, continue after. **Never read a password field**, and leave password inputs out of every dump of a form's fields.
- **Questions that are always the user's:** assessments and aptitude tests, criminal history and felony questions, whether they would sign a non-solicitation or confidentiality agreement, and any judgement call about their own experience ("years of comparable experience", "describe how you use AI"). Fill everything else, bring the tab forward, and let the user answer. Do not read back or log their answer.
- **One tab per application.** Opening a new address in a tab that holds a half-filled form throws the form away. Open each application in its own new tab, and bring it forward when the user has to act in it.
- **Some saved profiles submit instantly.** On some platforms, once the user is signed in, simply opening another job's apply link submits that application from the saved profile, with no form and no review. Treat opening an apply link on such a platform as submitting: do it only after the user has said yes to that specific application (stage 03, "Review before submit"). Known pattern: some iCIMS boards after sign-in.
- **Do not repeat a failing submit.** Read the error messages, fix the fields, and submit once. Repeated failed submits can trigger an emailed security code or a lockout.
- **Do not click near a code box while the user is typing a code.** After any click that sends a code, stop and hand over; take no more clicks until the user says they are through.

## Getting text into fields

Modern forms ignore some ways of setting a value. In rough order of what to try:

1. **The native value setter plus events.** Set the value with the input's native setter, then dispatch `input` and `change` (and `blur` or `keyup` on some forms). Works on plain forms, AngularJS, many React forms.
2. **Text insertion.** `el.focus(); el.select(); document.execCommand('insertText', false, value)`, then `change` and blur. Works on many React and Ant Design forms where the setter shows the text but the form does not register it. To clear a field: `select()` then `execCommand('delete')`.
3. **Real typing** with the browser tool's type action. Needed for: phone numbers on several platforms, street address line 1, some textareas, some salary boxes, fields whose validation rejects script-set values.

Other rules:

- **A script-set value must change to count.** Setting a dropdown to the value it already shows fires nothing. If a dependent dropdown stays empty, set the parent to another option and back.
- **Read the page a second or two after a click.** Many forms advance late; reading immediately shows the old step, and clicking Next again skips a step. Click Next once per call, wait, and confirm which step is showing before filling.
- **Check which page is showing before a fill script runs.** A script meant for page 2 can overwrite page 1's fields if the Next click silently failed.
- **Screenshots can lag one render.** Before a coordinate click, confirm the state by script or a fresh screenshot.
- **Coordinates:** if screenshots are scaled, multiply page coordinates from `getBoundingClientRect()` by the screenshot width over `innerWidth` before clicking. If the page will not scroll by script, use the browser tool's scroll action and a fresh screenshot.
- **Narrow windows:** if `innerWidth` is very small and the page is unreadable, resize the browser window to a desktop size (for example 1200 x 900), work, then set it back.

## Dropdowns, radios, checkboxes and dates

- **Native `<select>`:** setter plus `change` (plus jQuery `.trigger('change')` where the page uses jQuery).
- **Custom dropdowns (react-select, react-widgets, Ant Design, comboboxes):** one real click on the control, wait about a second for the list to draw, then click the option whose text matches, by script or by its reference. Never click a blind offset: the list may open upward or in a different order than it looks.
- **Searchable lists (school, field of study, city):** after the click, type the text for real, wait 1 to 2 seconds, then click the matching option.
- **Radios and Yes/No buttons:** a script click works on some forms; others need a real click. The first click right after typing can be swallowed: re-read the state and click again if needed.
- **Checkboxes, especially acknowledgements:** usually need a real click. A dispatched change can toggle them back off.
- **Web components (shadow DOM):** click the input inside: `el.shadowRoot.querySelector('input')`.
- **Date fields** vary the most:
  - Native `type=date` inputs: the setter with `YYYY-MM-DD` sometimes works; when the form does not register it, click the field and type the digits.
  - Masked text dates: type the digits (`MMDDYYYY`).
  - Segmented dates (month, day, year boxes): set each segment with the native setter plus an `InputEvent` of type `insertText` and a `change`.
  - Calendar pickers: open the picker and click the day cell. For "today's date" fields, the picker's "today" cell is the most reliable.
- **Address autocompletes:** type the street, then click the suggestion; it fills city, state, ZIP and county. Picking the address can wipe other fields on the same page (such as a start date), so set those after. If the autocomplete fails to load, fill the fields by hand.
- **Phone with a country code:** set the country (or dial code) first, then type the number; typing the number into a box that already holds a prefix can double it.

## Resume upload and resume parsing

Upload methods, in the order stage 03 tries them:

- **Plain file input.** Use the file upload tool on it directly. Never click it: clicking opens the computer's own file picker, which the browser tools cannot see.
- **Button over a hidden input.** The real `input[type=file]` is usually hidden next to the button. Find it with `read_page` (it often shows as a button with type "file"), `find` ("file input for resume"), or a read-only check listing every `input[type=file]` with its id and `accept` value. Upload to that input.
- **Drag-and-drop zone.** There is almost always a hidden file input inside the zone. Upload to it.
- **"Autofill from resume" button.** Find the hidden input behind it and upload there, then check every field it filled.
- **Paste box.** Use the text of `my-files/resume.md` and flag it in the review summary.
- **Built-in browser pane.** It has no file upload tool. Switch the application to Claude in Chrome.
- **When the upload tool is refused** ("not a file input") on a control that is a file input inside a custom widget, a page script can attach the file: build a `File` from the PDF's bytes, put it in a `DataTransfer`, assign it to `input.files`, and dispatch `change`. On a few React dropzones, the change only registers through the input's own React handler.

How to tell an upload worked:

- The page shows the chosen file name (or a preview of the resume) next to the control. A different name, a size of 0, or an error means it failed.
- Some forms read the file only on the next page. Check again after moving on.

**Upload order:**

- On forms that **do not** read the resume, upload **last**: some scripted field changes on those forms wipe an attached file. Check the file name is still there before submitting.
- On forms that **do** read it and fill fields, upload **first**, wait for the reading to finish, then correct the fields.

**Resume readers get things wrong.** After any automatic fill, check every work-history entry against `my-files/resume.md`. Common mistakes:

- employer and job title swapped, or the employer jammed into the title, or the city put in the description;
- dates garbled, or an end date set on the current job;
- bullet points dropped, or the degree set to "Other";
- the phone number copied into the extension field;
- the whole contact line put in the city field;
- parsed rows arriving late and overwriting or duplicating what you typed (wait for the reading to finish first);
- "suggested" skills added that are not on the resume (remove them);
- a re-upload wiping fields such as street address or school.

## Answers forms ask for

Fill from the answer bank. These come up often; the intake collects them (stage 00, step 5):

- **"How did you hear about us":** the employer's own career site ("Company website", "Corporate website", "Careers site"). If there is no such option, use the closest true one and tell the user.
- **Pay:** some boxes take text (use the answer bank's wording), some take digits only (use the single number), some are a range list (pick the band holding the number), some pair a number with a currency picker, some ask hourly or salary first.
- **Start date, relocation, travel, overtime and shifts, work authorization and sponsorship, age 18 or over.**
- **Employer relationships:** previously worked here, relatives working here, current employer is a client or partner, currently bound by a non-compete or other restrictive agreement.
- **References and contact permission:** some forms make supervisor name, title, phone and email required for every past job marked "may we contact". Some ask "ever been fired or asked to resign" or "may we contact past employers".
- **Reason for leaving** each past job.
- **Licenses:** held, and ever denied, revoked or suspended. **Registrations** in regulated fields.
- **Years in specific kinds of work** (customer service, sales, a named tool), and occasionally things like a typical sales cycle.
- **Voluntary self-identification:** gender, Hispanic or Latino, race, veteran status (note the difference between "not a veteran" and "a veteran but not a protected veteran"; pick the one that is true), disability. Option text varies a lot: match by meaning, and read back the chosen value.
- **Optional:** pronouns, SMS consent, phone type, preferred name, middle name, county.
- **LinkedIn:** enter only when required (stage 03). Some forms validate that it is a real LinkedIn profile address.

## Legal text: read it to the user first

Stop and quote it to the user before anyone ticks the box or types a signature (stage 03 step 11). Seen on real forms:

- arbitration agreements, jury or class-action waivers, invention assignment, pay withholding;
- consent to biometric collection (photos, video, facial geometry, fingerprints);
- consent to AI transcription or AI scoring of interviews;
- broad authorization to contact **any** past or current employer, or every business listed on the application. If the user's current employer is listed, point that out: it conflicts with "never contact your current employer".
- background, credit or criminal check releases.

Plain accuracy statements ("the information is true") are routine, but still mention them in the review summary.

## Platform notes

### Greenhouse

- Usually no account and no CAPTCHA. Form address: `job-boards.greenhouse.io/embed/job_app?for=<board>&token=<job id>`. It works even when the company wraps the board in its own site.
- Read the posting from `boards-api.greenhouse.io/v1/boards/<board>/jobs/<id>` (open it in the tab; a fetch from the form page is blocked).
- Text inputs take the setter; **textareas need real typing**.
- **Phone with a required country:** first click the Country control, type the country, click the option, then type the phone.
- react-select dropdowns: one real click on the control, wait about half a second, then click the `.select__option` with matching text. Read the result from `.select__single-value`. Do not call React internals: that can wipe the attached resume.
- Attach the resume last and check it is still showing before Submit.

### Lever

No account. Upload the resume first; it fills name, email, phone and current employer. An invisible CAPTCHA usually does not challenge; a visible one is a wall.

### Ashby

No account. The phone must be typed for real. Yes/No buttons and radios need real clicks; check each took. Location and source are comboboxes: click, type, click the option. Usually ends with an agreement radio: read it.

### Workday

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

### iCIMS

- Login, password and CAPTCHA (often hCaptcha at "Submit profile") are the user's.
- The profile form sits in a same-origin frame (`iframe#icims_content_iframe`): work in its `contentDocument`, and attach the resume with that frame's own `File` and `DataTransfer`.
- Uploading the resume reloads the frame and can wipe fields: re-check everything after.
- Lazy dropdowns: dispatch mousedown, mouseup and click on the dropdown anchor, type in its search box if it has one, then click the result item.
- Follow-up forms (disability, veteran, acknowledgements) can load in a cross-origin frame. Complete them **inside the application tab** where possible; on some boards, completing them in a separate tab leaves the application "incomplete".
- Sessions time out after roughly 20 to 30 idle minutes; drafts may keep only some answers.
- **After sign-in, some boards submit an application the moment its apply link opens** (see "Before you start").

### Paylocity

- No account. "Fill out application with my resume" reads the file; check every field, add missing jobs by hand.
- Dropdowns: real click on the control, wait about 2 seconds, click the list item. The acknowledgement checkbox needs a real click. Month/year dates need text insertion.
- Pick the address from its suggestions, then set the start date (picking the address wipes it).
- Some forms require supervisor contact details for every job marked "may contact".

### BambooHR

No account. The state list may need real clicks through a button menu (`find` the control, click, `find` the option, click). Dates: click and type, then Escape. Submit is followed by a CAPTCHA checkbox: the user ticks it.

### Jobvite

No account. Usually several pages: consent, contact and resume, self-identification with a typed name and date, screening questions, then a visible CAPTCHA at send (the user). The file upload tool may refuse the control; attaching by page script works. Next may need a real click.

### Phenom (apply)

- No account on some boards. Read the posting from `phApp.ddo.jobDetail.data.job`.
- Fill every required field before the first Next: once a field is flagged, picking a value may not clear the error until a related field is retyped.
- An invisible CAPTCHA can reject a scripted submit: the user presses Submit. Reloading the apply address restores the draft and fixes buttons left disabled.

### UKG Pro Recruiting and UKG Ready

- UKG Pro: an account at "Apply now" (the user). One long page; the resume reader often puts employer and location in the title.
- UKG Ready on a new employer: no password until "Sign & submit", which asks for a password as the signature (the user). Once a profile exists, the board asks the user to sign in.

### Dayforce

- An account (Dayforce ID) or "apply without an account" on some boards.
- Creating the account: the agree box counts only after both policy links are clicked, and those links can open in the same tab and wipe the form. Have the user open them in a new tab.
- Ant Design form: open selects with a mousedown on `.ant-select-selector`, wait, click the option. Press each section's Update button and read the error messages after each.
- **Next is slow:** click once, wait about 5 seconds, confirm the page number. A double advance can skip a page unanswered.

### ADP Workforce Now and ADP MyJobs

- Sign-in is by a texted or emailed code (the user). One emailed code may never arrive; the text option is often more reliable.
- Radios are web components; source dropdowns and self-identification need real clicks.
- Text inputs on the questions page often register only when typed for real.
- The last step can be an electronic signature: tick, type the full name, submit. Some flows have no review page: the last Next submits, so stop before it for the user's review.
- Some legacy ADP flows ask for the last four digits of a Social Security number and a birth date (a "rehire check"): a wall. The user decides.

### Oracle Cloud Candidate Experience

- Often no account; a returning email may get a PIN or emailed code (the user).
- ZIP fields are autocompletes: type the ZIP in two parts so the list filters, then click the matching row.
- Pill-button questions take a script click. Comboboxes: focus, insert the text, wait, click the matching cell.
- The final e-signature can be an employment agreement with arbitration: quote it first.

### SuccessFactors

- An account (the user). Picklists: click the select button, then the matching option inside the list named by the input's `aria-owns`. Dates are calendar widgets that take typed `MM/DD/YYYY`.
- Some flows require the current supervisor's name and title with no "may we contact" choice: raise it with the user.

### Hirebridge, ClearCompany, isolved, Cornerstone, Paycom, Paycor and others

- **Hirebridge:** some boards offer a quick apply with no password; others ask for an existing profile's password (the user). The resume upload reloads the page: upload first.
- **ClearCompany:** no account on a first visit; a second visit to the same job emails a sign-in link (the user). Parsed rows arrive late; wait, then fix. Some forms require a birth date and Social Security number: a wall.
- **isolved Hire:** an account is created for the user after step 2 and a password is asked (the user). A returning email gets a secure code.
- **Cornerstone:** the first application creates a profile with a CAPTCHA (the user); later applications submit directly.
- **Paycom:** values set by script on selects, dates and autocompletes are wiped on submit. Use arrow keys on selects, type dates digit by digit, click autocomplete suggestions, real-click the acknowledgement.
- **Paycor:** plain form; setters work.
- **SmartRecruiters:** may show bot-check questions: the user answers.
- **Conversational (chat) apply flows:** answer from the answer bank; anything new goes to the user.

## Bot checks

Some career sites show a bot check that never clears in an automated browser. The user can usually pass it in their own Chrome; after that, Claude in Chrome can continue in that same window. Never try to get past a check yourself.

## Walls at a glance

| Wall | Seen on | Who |
|---|---|---|
| Account per employer | Workday, Dayforce, SuccessFactors, UKG Pro, some iCIMS | User |
| Password typed as the signature | UKG Ready (new employer) | User |
| Emailed or texted code | ADP, Oracle (returning), isolved (returning), Greenhouse after repeated failed submits | User |
| Emailed sign-in link | ClearCompany (second visit) | User |
| CAPTCHA at submit | iCIMS (hCaptcha), Jobvite, BambooHR, Cornerstone (first time), Phenom (invisible) | User |
| Birth date, Social Security number, ID digits | some ClearCompany and ADP flows, some tax-credit surveys | User decides |
| Bot check on the careers site | various | User, in their own browser |
