# Intake transcript (test run with a made-up user)

Maya Ortell is a made-up person: a registered nurse with six years in hospitals (three on a medical-surgical floor, three in intensive care), moving into healthcare technology sales. She lives in Larkfield, a made-up metro in the made-up state of Calder. Wrenford is a made-up city 70 miles away.

Claude asked one question at a time and waited for each answer. Shortened here to question and answer.

| # | Question | Maya's answer |
|---|---|---|
| 1 | Artifact or spreadsheet tracker? | Artifact. Not published yet, so Claude offered to publish it together. In this test the publish was simulated with the stand-in database (`tests/stand-in-db.js`). |
| 2 | What kind of job? | Clinical sales specialist, account executive at a health tech company. I would take a sales development job if the pay is right. |
| 3 | What level? | Entry to mid. |
| 4 | Similar titles you do not want? | Implementation or training jobs with no sales. Customer success with no quota. Anything that is really nursing. |
| 5 | What does a good fit look like? | Selling software that makes nurses' work easier, to hospitals, where my bedside years count. |
| 6 | Where do you live? | Larkfield, Calder. |
| 7 | Which places work? | Larkfield metro, a territory based out of Larkfield, fully remote. Not a multi-state territory. |
| 8 | Remote limits? | Remote only if Calder residents can apply. |
| 9 | Nearby cities only above a pay bar? | Wrenford, if the posted pay reaches $100,000. |
| 10 | Would you move? | No. |
| 11 | Lowest pay? | $85,000 a year. |
| 12 | Base only, or base plus commission? | Base plus commission is fine. Total at target counts. |
| 13 | Pay wording on forms? | "$85,000 or more in total pay, open on the split between base and commission." |
| 14 | Single number? | 85000 |
| 15 | Industries you want? | Health tech, digital health, health data, health insurance, medical devices (software side). |
| 16 | Industries out, and why? | Pharma sales: not for me. Staffing agencies: I have seen how they treat nurses. Medical devices where I would be in the operating room. |
| 17 | Hide any of those entirely? | Hide staffing and pharma. |
| 18 | Years in the work you target? | Zero years in sales. Six years of hospital nursing, which some sales jobs count. |
| 19 | How far do you stretch on years? | If they ask for up to two years of sales, I still apply. If they ask for more than that, skip unless clinical experience counts instead. |
| 20 | Licenses? | Registered Nurse, State of Calder. |
| 21 | Degrees? | Bachelor of Science in Nursing. |
| 22 | Automatic noes? | Part-time. Commission only. Travel over half the time. Any license I would need before starting. |
| 23 | Employers to track but not apply to yet? | Northgate Medical Software. I interviewed there last year and want to wait. |
| 24 | Never contact? | Pinecrest Health System, my current employer. |
| 25 | Employers that only post on one job site? | None. |
| 26 | Sweep on your own, or ask first? | Add fitting listings on your own. |
| 27 | Close calls? | Decide by my rules, but list anything about taste in the report. |
| 28 | (Told, not asked) Human review before every submission; auto-submit off by default. | OK. |
| 29 | Outreach drafts? | Yes, when I ask. |
| 30 | Email connector? | Yes, Gmail. |
| 31 | Writing style? | Warm but short. No exclamation marks. Sign off "Maya". |

Claude then showed the full `my-rules.md` (next file). Maya asked for one change: add "medical devices only on the software side" to the "in" list. Claude made the change, showed the full file again, and Maya said approve. Only then was it saved.

Claude showed the `settings` values, Maya said yes, and they were saved. Maya started her answer bank. Each entry was confirmed one at a time (see `tests/sample-data/tracker-before.json`, `answers`).

## Resume (the new end of the intake)

Claude asked: "Do you already have a resume you are happy with?" and offered three answers: use mine as it is, improve mine, or I need a new one. Maya said: "I need a new one. Mine is a nursing resume."

Claude ran stage 07 from the start, one question at a time, for each of her two jobs, then education, licenses, skills, other, gaps, and what must stay off. For every number, Claude asked: "Can you stand behind that number if an interviewer asks? Where does it come from?" Maya gave a source for each one. For example, 30 nurses trained came from the go-live sign-in sheets. Claude showed the full facts file, and Maya approved it (`resume/resume-facts.md`).

Before writing, Claude read 3 postings for her target role that were already in her tracker (Brightline Charting BC-1042, Halyard Patient Monitoring HPM-388, Kestrel Telehealth KT-3315). It noted that all 3 sell software to hospitals, all 3 accept clinical experience in place of sales years, and 1 requires an RN license. From that it summed up what employers ask for: licenses directly under the summary, then in each nursing job the training, software-adoption and vendor bullets first. It listed the posting terms she can use because her facts support them (hospitals, intensive care, remote patient monitoring, training) and the ones she cannot (quota, demos, telehealth, acute care), and asked whether any of those were true for her. She said no. The closest example was "Healthcare technology or medical sales" plus the career-changer notes. Maya confirmed the summary, and it was saved in the "What employers ask for" section of her facts file. Claude drafted the resume one section at a time, Maya approved each one, the checks passed, and she approved the PDF (`resume/maya-ortell-resume.pdf`).

**The opt-out path** ("Yes, use mine as it is") was not run as its own session in this test. What the intake says to do there: ask for the file in `my-files/resume.pdf`, offer a text copy, do not critique or change it, and do not run stage 07 unless the user asks later.

## Employers

Claude asked: "Do you already have a list of employers you want to work for?" Maya named ten (the target list in `tests/sample-data/tracker-before.json`). Claude offered stage 08 part A to find more. She said not yet.

