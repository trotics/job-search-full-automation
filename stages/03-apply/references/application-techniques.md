# Application techniques

How application forms behave, platform by platform, and how to fill them correctly. Learned from well over a hundred real applications. Read it before an apply session. Platform-specific notes are in `application-platforms.md`.

Add what a session learns here (with the user's OK): a new platform, a new workaround, a trick that stopped working. Edit the platform's section in place. Never add employer names, the user's details or dates.

## Before you start

- **Read every posting in full before the user creates any account.** Many promising titles turn out, once read, to be senior or out-of-scope roles. Creating accounts for those wastes the user's time.
- **Walls are the user's** (rules 9): accounts, passwords, one-time codes, CAPTCHAs, ID numbers. Fill everything up to the wall, hand the browser over, continue after. **Never read a password field**, and leave password inputs out of every dump of a form's fields.
- **Questions that are always the user's:** assessments and aptitude tests, criminal history and felony questions, whether they would sign a non-solicitation or confidentiality agreement, and any judgement call about their own experience ("years of comparable experience", "describe how you use AI"). Fill everything else, bring the tab forward, and let the user answer. Do not read back or log their answer.
- **One tab per application.** Opening a new address in a tab that holds a half-filled form throws the form away. Open each application in its own new tab, and bring it forward when the user has to act in it.
- **Some saved profiles submit instantly.** On some platforms, once the user is signed in, simply opening another job's apply link submits that application from the saved profile, with no form and no review. Treat opening an apply link on such a platform as submitting: do it only after the user has said yes to that specific application ("Review before submit"). Known pattern: some iCIMS boards after sign-in.
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

Upload methods, in the order to try them:

- **Plain file input.** Use the file upload tool on it directly. Never click it: clicking opens the computer's own file picker, which the browser tools cannot see.
- **Button over a hidden input.** The real `input[type=file]` is usually hidden next to the button. Find it with `read_page` (it often shows as a button with type "file"), `find` ("file input for resume"), or a read-only check listing every `input[type=file]` with its id and `accept` value. Upload to that input.
- **Drag-and-drop zone.** There is almost always a hidden file input inside the zone. Upload to it.
- **"Autofill from resume" button.** Find the hidden input behind it and upload there, then check every field it filled.
- **Paste box.** Use the resume text (`resume.md`) and flag it in the review summary.
- **Built-in browser pane.** It has no file upload tool. Switch the application to Claude in Chrome.
- **When the upload tool is refused** ("not a file input") on a control that is a file input inside a custom widget, a page script can attach the file: build a `File` from the PDF's bytes, put it in a `DataTransfer`, assign it to `input.files`, and dispatch `change`. On a few React dropzones, the change only registers through the input's own React handler.

How to tell an upload worked:

- The page shows the chosen file name (or a preview of the resume) next to the control. A different name, a size of 0, or an error means it failed.
- Some forms read the file only on the next page. Check again after moving on.

**Upload order:**

- On forms that **do not** read the resume, upload **last**: some scripted field changes on those forms wipe an attached file. Check the file name is still there before submitting.
- On forms that **do** read it and fill fields, upload **first**, wait for the reading to finish, then correct the fields.

**Resume readers get things wrong.** After any automatic fill, check every work-history entry against the resume text (`resume.md`). Common mistakes:

- employer and job title swapped, or the employer jammed into the title, or the city put in the description;
- dates garbled, or an end date set on the current job;
- bullet points dropped, or the degree set to "Other";
- the phone number copied into the extension field;
- the whole contact line put in the city field;
- parsed rows arriving late and overwriting or duplicating what you typed (wait for the reading to finish first);
- "suggested" skills added that are not on the resume (remove them);
- a re-upload wiping fields such as street address or school.

## Answers forms ask for

Fill from the answer bank. These come up often; the intake collects them:

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
- **LinkedIn:** enter only when required. Some forms validate that it is a real LinkedIn profile address.

## Legal text: read it to the user first

Stop and quote it to the user before anyone ticks the box or types a signature . Seen on real forms:

- arbitration agreements, jury or class-action waivers, invention assignment, pay withholding;
- consent to biometric collection (photos, video, facial geometry, fingerprints);
- consent to AI transcription or AI scoring of interviews;
- broad authorization to contact **any** past or current employer, or every business listed on the application. If the user's current employer is listed, point that out: it conflicts with "never contact your current employer".
- background, credit or criminal check releases.

Plain accuracy statements ("the information is true") are routine, but still mention them in the review summary.

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
