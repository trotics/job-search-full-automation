# Application techniques

General methods for application forms. No employer names. Add a line when a session finds something new (stage 03, step 17), with the user's OK.

## Upload methods

Try them in the order stage 03 gives (a to e). What each looks like on the page:

- **Plain file input.** A "Choose file" control. Use the file upload tool on it directly. Never click it: clicking opens the computer's own file picker, which the browser tools cannot see.
- **Button over a hidden input.** A styled "Upload resume" or "Attach" button. The real `input[type=file]` is usually hidden next to it or inside the same form section. Find it with `read_page` (it often shows as a button with type "file"), `find` ("file input for resume"), or a read-only page check such as listing every `input[type=file]` with its id and `accept` value. Upload to that input.
- **Drag-and-drop zone.** "Drop your resume here". There is almost always a hidden file input inside the zone. Upload to that input. Dragging a file from the computer is not needed.
- **"Autofill from resume" button.** Opens the computer's file picker, then reads the resume and fills fields. Find the hidden input behind it and upload there. Afterwards, check every field it filled against the answer bank. Auto-fill often gets phone numbers, dates, job titles and school names wrong, and sometimes puts the current employer where a reference should be.
- **Paste box.** "Paste your resume" or "Enter manually". Use the text of `my-files/resume.md`. Flag it in the review summary.
- **Built-in browser pane.** It has no file upload tool. Switch the application to Claude in Chrome.

## How to tell an upload worked

- The page shows the file chosen in stage 03 (`resume.pdf`, or the approved tailored `resume-<listing id>.pdf`), or a preview of its contents, next to the control.
- If the control shows a different file name, a size of 0, or an error, the upload failed. Try the next method.
- Some forms only read the file when the next page loads. Check again after moving on.

## Routes that are always walls

- "Apply with LinkedIn", "Import from LinkedIn", or any LinkedIn sign-in.
- "Import from Google Drive", "Dropbox", "OneDrive" or any other account sign-in.
- Anything asking for a password, a one-time code or a CAPTCHA.

These go to the user.
