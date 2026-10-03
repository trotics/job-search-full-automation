# Test run with a made-up user: results

**The user:** Maya Ortell, a made-up registered nurse with six years in hospitals, moving into healthcare technology sales. She lives in Larkfield, a made-up metro in the made-up state of Calder. All employers, postings, people and links in this test are made up. Links use the reserved `.example` domain, and the phone numbers use 555.

## 1. Intake

All 31 questions were asked one at a time (`intake-transcript.md`). Her `my-rules.md` was shown in full, changed once at her request, shown again, and approved before saving (`my-rules.md`). Her tracker `settings` and answer bank are in `tests/sample-data/tracker-before.json`.

## 2. Sweep and fit review

Ten employers were on her target list, with fifteen postings on their (made-up) career sites (`tests/sample-data/postings.json`).

| # | Employer | Posting | Call | Deciding check |
|---|---|---|---|---|
| 1 | Brightline Charting | Clinical Solutions Account Executive | **Added, High** | Passes all; clinical years accepted in place of sales |
| 2 | Brightline Charting | Clinical Implementation Specialist | Skipped | 3, target role: no quota, an out role |
| 3 | Halyard Patient Monitoring | Clinical Sales Specialist (Larkfield territory) | **Added, High** | Passes all |
| 4 | Halyard Patient Monitoring | Clinical Sales Specialist (Port Avery) | Skipped | 5, place: must live in Port Avery |
| 5 | CareGrid Scheduling | Sales Development Representative | Skipped | 6, pay: $80,000 is under the $85,000 floor |
| 6 | CareGrid Scheduling | Account Executive, Mid-Market | Skipped | 5, place: remote only for three other states |
| 7 | Meridian Health Plans | Provider Relations Sales Consultant | **Added, Medium** | Pay not posted, judged plausible with reasoning |
| 8 | Northgate Medical Software | Clinical Account Executive | **Added, On hold** | Employer on hold in her rules |
| 9 | Tallow Pharma | Pharmaceutical Sales Representative | Not read | Employer in an excluded industry, not swept |
| 10 | Summit Nurse Staffing | Healthcare Staffing Sales Executive | Not read | Employer in an excluded industry, not swept |
| 11 | Lumen Infusion Systems | Clinical Specialist | Skipped | 5, place: multi-state territory (also 60% travel) |
| 12 | Kestrel Telehealth | Enterprise Account Executive | Skipped | 7, requirements: 7+ years, beyond her stretch |
| 13 | Kestrel Telehealth | Account Executive, Health Systems | **Added, High** | Passes all; 3 years is preferred only |
| 14 | Oakmoor Clinical Analytics | Clinical Data Sales Consultant | Skipped | 5, place: Wrenford below the $100,000 bar |
| 15 | Oakmoor Clinical Analytics | Account Executive (part-time) | Skipped | 7, hard no: part-time |

Result: 5 added, 8 skipped with reasons, 2 not read because the employer's industry is excluded. Every posting is accounted for. The listing already at Applied (Meridian, Member Sales Advisor) was not touched.

**Checked by script, both trackers:**

```
Artifact path (JSON snapshots, as saved from ArtifactData):
  check_tracker.py check tracker-before.json tracker-after-fit.json --stage sweep
  Stage: sweep | listings before 1, after 6 | new 5 | changed 0
  RESULT: PASS (0 problems)

Spreadsheet path (writes made with tools/sheet.py, snapshots from the .xlsx):
  Stage: sweep | listings before 1, after 6 | new 5 | changed 0
  RESULT: PASS (0 problems)
  sheet.py refused a write to yourNotes and a replacement of history, as designed.
```

**Checker self-test** (`tests/run_checker_selftest.py`): 11 broken sessions, each breaking one rule (notes written, history rewritten, a sweep expiring an Applied listing, a missing posting text, a wrong status, a misspelled company, a password in the answer bank, a deleted listing, an undated history entry, settings changed by a sweep). All 11 were caught.

## 3. Tracker page in a browser (stand-in database)

`tests/build_local_test.py` built the page with a stand-in database and opened it in a browser on this computer.

- With Maya's data: all five tabs render. Listings to apply are grouped High, Medium, On hold; the Applied listing shows its history; tiers show her own wording; the two excluded employers sit on the Archive tab; skipped postings show their reasons on the Coverage tab.
- Changing a status saved `status` only. Typing a note saved `yourNotes` only. No other writes.
- With an empty database: every tab shows a plain "nothing yet" message with the next step. No errors.
- Opened with no database at all: a clear message, no errors.
- Final load: browser console clean.

**Not tested:** the page published as a real Claude artifact. That is the first thing to do after setup (README, "Set up your tracker").

## 4. Apply, dry run

Listing: Kestrel Telehealth, Account Executive, Health Systems (High). A made-up application form (`tests/sample-data/apply-form.html`, served only on this computer) was filled following stage 03, as Maya, in two runs.

**Run 1, built-in browser pane.** Everything the answer bank covers was filled. The resume upload was not tried in this run, because the built-in pane has no file upload tool (stage 03 now sends the application to Claude in Chrome at this point: upload option e).

**Run 2, Claude in Chrome.** Maya's made-up resume (`tests/sample-data/maya-ortell-resume.pdf`, built by `tests/make_test_resume_pdf.py`) was uploaded to three different controls. Before touching any of them, a read-only check of the page listed every file input: one visible, two hidden. No upload control was clicked.

| Control | What the user sees | Method that worked | Page showed afterwards |
|---|---|---|---|
| 1. Plain file input | "Choose file" | **a. File upload tool** on the input | "Attached: maya-ortell-resume.pdf (1947 bytes)" |
| 2. Drag-and-drop zone | "Drag and drop your resume here, or browse" | **b. Hidden input** inside the zone | "Attached: maya-ortell-resume.pdf (1947 bytes)" |
| 3. "Autofill from resume" button | A button that opens the computer's file picker | **b. Hidden input** behind the button | "Attached: maya-ortell-resume.pdf (1947 bytes)" |

Methods c (the computer's file picker), d (paste box) and e (switch browsers) were not needed in run 2, because a or b worked first. Run 1 is the case e covers.

**Auto-fill check.** The autofill button read the resume and filled four fields. Each was checked against the answer bank:

| Field | Auto-fill put | Answer bank | Action |
|---|---|---|---|
| Full name | Maya Ortell | Maya Ortell | Kept |
| Email | maya.ortell@example.com | maya.ortell@example.com | Kept |
| Phone | (empty: the parser missed it) | (555) 010-0142 | **Fixed** |
| City and state | "Larkfield, Calder \| maya.ortell@example.com \| (555) 010-0142" | Larkfield, Calder | **Fixed** |

**The rest of the form:**

| Field | Filled with | Source |
|---|---|---|
| Pay expectations | "$85,000 or more in total pay, open on the split between base and commission" | Answer bank, Pay |
| Work authorization | Yes | Answer bank |
| Years of B2B sales | 0 | Resume (flagged: not in the answer bank) |
| Gender, veteran | "I don't wish to answer", "I am not a protected veteran" | Answer bank, Voluntary |
| LinkedIn (optional) | Left blank | Rule: only when required |
| "Apply with LinkedIn" button | **Not clicked** | Rule: LinkedIn import is a wall |
| Why interested (optional) | Left blank | Rule: optional free text |
| Account username and password | **Not touched; handed to the user** | Rule: walls are the user's |
| Arbitration and contact agreement | **Not ticked; quoted to the user** | Rule: legal text |
| Submit | **Not clicked** | Dry run; human review first |

Checked in the page afterwards: all three file inputs hold `maya-ortell-resume.pdf`, agreement unticked, username empty, LinkedIn button not clicked, form not submitted. The browser extension would not let the check script read the password box or the work-authorization box, because it treats them as sensitive. The work-authorization value was confirmed by the fill step itself, and the session never typed in the password box.

The review summary the session gave the user:

> Ready for your review, Kestrel Telehealth, Account Executive, Health Systems (KT-3315). Resume attached as maya-ortell-resume.pdf (the file input behind the autofill button, the main resume input, and the drop zone). The site's autofill got two fields wrong and I fixed them from your answer bank: phone was empty, and city had your whole contact line in it. From your answer bank: name, email, phone, city, pay wording, work authorization, gender and veteran answers. From your resume: years of B2B sales, 0 (want this in your answer bank?). Left blank: LinkedIn and "why are you interested", both optional. I did not use "Apply with LinkedIn". Your steps: create the account (username and password), and read this before ticking the agreement: "binding individual arbitration ... waive the right to join a class action ... authorize Kestrel Telehealth to contact any of my past or current employers." That last part would let them contact your current employer, which your rules say never to contact. I would not agree without asking them to exclude current employers. Nothing has been submitted.

On a real submission, the history entry would end with "upload: hidden file input". `check_tracker.py` now fails any move to Applied whose history does not name the upload method.

## 5. What broke, and the fixes

| # | What broke | Fix |
|---|---|---|
| 1 | The tracker page had the original user's industries, role families, work-order bands and place names written into its code. | All of it now comes from the `settings` record, with plain defaults for an empty database. |
| 2 | The page matched company names by their first letters, the exact mistake in `recurring-mistakes.md` item 7. | Exact name matching only. |
| 3 | The Coverage tab never showed why postings were skipped. | Skipped postings now show under each employer. |
| 4 | Two errors I introduced while editing the page (an unescaped apostrophe, a broken pattern) stopped it loading. | Caught by the browser test and fixed. Final console clean. |
| 5 | The checker missed an undated history entry on a new listing. | Fixed. The self-test now covers it. |
| 6 | The first run did not test the resume upload. The built-in browser pane it used has no upload tool, but uploading itself works (it did in the original system, through Claude in Chrome). | Stage 03 now tries five upload methods in order before handing the upload to the user, checks the page after every upload, and checks every auto-filled field. Retested in Claude in Chrome: three controls, all uploaded (section 4). |
| 7 | Stage 03 had no rule for optional free-text boxes, or for questions answered from the resume. | Rules added: leave optional text blank unless told otherwise; flag resume-sourced answers in the review. |
| 8 | The answer bank had no entry for years of experience, a common form question. | The intake now asks for it. |
| 9 | Nothing told a new user what to do when their tracker link was not set yet. | Setup now creates the tracker before any stage that writes. |
| 10 | The legal-text rule caught a broad "contact your current employer" clause that conflicts with the never-contact list. | Worked as designed. Kept as an example in this report. |
| 11 | The new auto-fill check caught two wrong fields (empty phone, contact line in city) from the form's own resume reader. | Fixed in the form from the answer bank, and listed in the review summary. |

## 6. Resume (stage 07)

Maya chose "I need a new one" in the intake (`intake-transcript.md`, end). Her facts file (`resume/resume-facts.md`) was built one question at a time and approved before writing.

**What employers ask for.** Her "What employers ask for" summary was built from 3 postings for her target role in her tracker (made up, like everything in this test). They led to licenses directly under the summary, and training, software-adoption and vendor bullets first in each nursing job. Posting terms she has no facts for (quota, demos, telehealth, acute care) are listed in the profile as never to be used. She confirmed the profile. The closest example is "Healthcare technology or medical sales" plus the career-changer notes.

```
python tools/build_resume.py resume.md maya-ortell-resume.pdf
  Wrote maya-ortell-resume.pdf: 1 page
python tools/check_resume.py resume.md --facts resume-facts.md --pdf maya-ortell-resume.pdf --years 6
  PDF pages: 1 (limit 1 for 6 years of experience)
  RESULT: PASS (0 problems)
```

The PDF was opened and read back as text in the right order: name, contact line, then each section top to bottom, one column. That is how application systems read it.

**Resume checker self-test** (`tests/run_resume_selftest.py`): the planted resume problems, all caught, plus 9 cases for the "What employers ask for" section. These are 6 that must fail (no profile, only 2 postings with source "postings", no confirmation date, sections out of the profile's order, a posting term not in the facts, a skill that appears only in the postings) and 3 fallbacks that must pass (2 postings plus a example, the user's own description plus a example, and the default). All 22 behaved as expected. They were an invented number, an inflated percent, a spelled-out number not in the facts, an em dash, first person, third person, a birth date, a street address, an employer not in the facts, a skill not in the facts, a bullet too long, and a missing heading. The approved resume passes.

What broke while building it, and the fixes:

| What broke | Fix |
|---|---|
| The first check passed "six years" in the summary, though no number six was in the facts. Spelled-out numbers were not checked. | Number words are now checked. The facts template gained a "years of experience" line with its source. |
| A bullet said "her list". The checker only looked for first person. | All pronouns are now checked; resumes use none. |
| Job headers wrapped badly, with the dates split across lines. | Title on one line in bold; employer, place and dates on the next in grey. |
| The summary ended with a claim not tied to any fact ("Brings the clinical view buyers trust"). | Cut. The summary now states only facts. |
| Once the "What employers ask for" section was added to the facts file, a skill named only in the postings would have passed the facts check. | The checker now leaves the what employers ask for out when checking facts. Posting text is never treated as a fact about the user. |

## 7. Company research (stage 08)

Not run live: it needs real web searches, and every place and employer in this test is made up. What was tested: the tracker checker lets the research stage add an employer, and fails it if it tries to add or change a listing (`tests/run_checker_selftest.py`). The first live run should be a short part A session ("find 5 employers for my target list"), checked by hand against the stage 08 Audit table.

## 8. Live run on real employer sites

Run with a made-up user (a customer success manager looking for remote roles in the United States) against the real, public career sites of three remote-first software employers, and the artifact tracker in a private Claude account. Read only: nothing was typed into an application and nothing was submitted.

- **Artifact tracker:** published `tracker/tracker-page.html` as a private artifact with a database, saved settings and three answer bank entries with `ArtifactData`, then snapshotted it with `out_dir` and `snapshot-dir`. `check_tracker.py --stage intake`: PASS.
- **Adding employers:** each careers site was found from the employer's own home page: one runs on Greenhouse, one on Ashby, one is the employer's own jobs page. `--stage research`: PASS.
- **Sweep:** read 211 postings from the Greenhouse feed, 11 from the Ashby feed, and the five customer success postings on the employer's own page. Added two listings at To apply with their posting text, wrote three coverage rows with skipped lines, and put three close calls in the report for the user. `--stage sweep`: PASS.
- **Location trap seen live:** the Ashby feed gave one remote job the location "HQ"; the posting's own text said "Location: USA & Canada". The board notes now say so.
- **Apply (read only):** the real form had 13 fields, including a plain resume file input (upload option a works there with Claude in Chrome) and a required question confirming the job is open only to people in the United States or Canada. The fill sheet came from the answer bank; contact details, sponsorship and employment-agreement questions went to the user, as the rules say.
- **Not checked:** how the tracker page looks with these rows, because the test browser is not signed in to Claude. The page reads the same data shape as the local test page (`tests/build_local_test.py`).

