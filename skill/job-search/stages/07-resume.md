# Stage 07: Resume

Build the user's resume from facts they state, shaped by what real postings for their target role ask for, and checked by script before anyone sees it as final. Also makes tailored versions for single listings. Run when the user asks, or from the intake when the user wants a new or improved resume.

**Nothing on the resume may be something the user did not say.** Every fact comes from `my-files/resume-facts.md`, which the user confirms line by line.

## When to run, and when not to

- The user said in the intake (or later) that they want a new resume, or want theirs improved: run it.
- The user has a resume they are happy with and opted out: do not run it. Never rewrite their resume unless they ask in that session. You may offer one short list of suggestions from `references/resume-guide.md`, once, and only if they want it.

## Inputs

- `rules.md` and `my-files/my-rules.md` (target roles, industries, writing style).
- `references/resume-guide.md`: the general rules, examples by field, and the default.
- `references/resume-facts-template.md`: the shape of the facts file.
- The user's current resume, if they have one (`my-files/resume.pdf` or `my-files/resume.md`), as a source of facts only.
- 3 to 5 real postings for the target role (Part B).
- For a tailored version: the listing's `postingText`.

## Part A. Collect the facts

Write to `my-files/resume-facts.md`, using the template. Ask **one question at a time** and wait for each answer.

1. If the user has a resume, read it first and fill in what it already says. Then show each job's facts and ask: "Is all of this true and current? Anything to add or remove?"
2. For each job, newest first (after all jobs: work out the years of experience from the dates, compare with what the user says, and if they differ ask which number to use and what it counts; write it on the "Years of experience" line):
   1. "What was your job title, the employer, the city, and the start and end month and year?"
   2. "In a few sentences, what did you do day to day? Who did you serve or sell to?"
   3. "What are you proudest of in this job? Results, numbers, awards, promotions, things you built or fixed."
   4. For every number the user gives: "Can you stand behind that number if an interviewer asks? Where does it come from?" Keep only numbers they confirm. Write the source next to each one.
   5. "Did you lead, train or manage anyone? How many?"
   6. "What tools, systems or software did you use?"
3. Education: school, degree, field, year (or "in progress"). Ask whether to show the year.
4. Licenses and certifications: name, issuer, state if any, year. **Never the license number.**
5. Skills the user can show in an interview.
6. Anything else worth showing: volunteer work, languages, military service, publications.
7. Gaps: "Is there any gap of six months or more you want to explain, or leave as is?" Never hide or change dates to cover a gap.
8. "Is there anything that must stay off your resume?" (for example a current employer's client names, or a job they do not want listed).
9. Show the full facts file. The user approves it before any resume is written. Every later change to a fact goes into this file first.

## Part B. Learn what employers ask for

Before writing, look at what employers actually ask for in real postings for the user's target role, so the resume puts first what matters for that job. This works the same for any job in any field. `references/resume-guide.md` has examples by field showing what a finished summary looks like.

**Every user gets a resume, in any field.** If a step below cannot be done, go to the next fallback. Never stop the resume because postings are hard to find.

1. **Pick the target.** Take the main target role and level from `my-rules.md`. If the user has two quite different targets, ask which one this resume is for. One resume per target. A resume for a second target goes to `my-files/resumes/resume-<target>.md` and `.pdf` (for example `resume-quality-inspector.md`), never over `my-files/resume.md`.
2. **Gather 3 to 5 real postings for that role**, newest first, in this order of preference:
   1. Listings already in the tracker for this role that have `postingText` saved.
   2. Postings on employers' own career sites, found by web search, for this role and level in or near the user's allowed places (or remote roles open to them). Posted in the last six months where possible.
   3. Postings the user pastes or attaches.
   Never open LinkedIn. Job aggregators may be used to find which employers post the role; read the posting itself on the employer's own site when you can.
3. **Read each posting and note**, with the posting it came from:
   - Must-have credentials: licenses, degrees, certifications, clearances.
   - Tools, systems and hard skills named.
   - The results the employer cares about (for example revenue, patient outcomes, uptime, students served, safety record).
   - The words the employer uses for the work (for example "territory", "pipeline", "caseload", "care plan").
   - Seniority signals and anything that sets length (years required, scope).
   - Tone (plain, formal, technical).
   - Anything asked for beyond the resume (portfolio, writing sample, references up front).
4. **Sum up what employers ask for.** What appears in at least two postings counts; what appears in one is noted but given less weight.
   - **Section order:** which sections come first. Credentials that most postings require and the user holds go directly under the summary.
   - **What leads each job:** the kind of proof that goes first in each role's bullets, matched to the results employers asked for.
   - **Terms to mirror:** the employers' own words for the work. Mark each one "in your facts" or "not in your facts". Terms not in the facts are **never** used. List them for the user as possible gaps: if the user says one is true, add it to the facts file first (with their confirmation), then it may be used.
   - **Length and tone.**
   - **Closest example(s)** from `references/resume-guide.md`, and the career-changer notes if the user is moving fields.
5. **Show this summary to the user** in plain words, with the postings it came from (company, title, link). Ask: "Does this match the jobs you want? Anything to change?" Make their changes.
6. **Save it** in the "What employers ask for" section of `my-files/resume-facts.md`, with the date and the user's confirmation. Part C follows it.

**Fallbacks, in order, so every user gets a resume:**

- **Fewer than 3 postings found** (rare role, small market, no web access on this device): use the ones found, plus the closest example. Write that down ("Based on: 2 postings plus example").
- **No postings at all:** ask the user to describe two or three jobs they want in their own words, or to paste any job description they have seen. Build the summary from that plus the closest example ("Based on: user description plus example").
- **Still nothing:** use the "Default (any job)" in `references/resume-guide.md`. It works for every job ("Based on: default").
- In every case the user confirms the summary before Part C, and the source is written down.

**Refresh:** if the user's target role changes, or the summary is more than six months old, offer to redo Part B before making a new resume.

## Part C. Write it

1. Write `my-files/resume.md` in the exact format in `references/resume-guide.md` ("File format").
2. Follow every rule in "General rules" and the "What employers ask for" section saved in the facts file. The resume's sections must come in the section order in "What employers ask for".
3. Draft **one section at a time**, in the section order in "What employers ask for" (contact line and summary always first). Show each one and get a yes or changes before the next.
4. Then show the whole resume, and run the checks:
   - `python tools/check_resume.py my-files/resume.md --facts my-files/resume-facts.md --pdf my-files/resume.pdf --years <years from the facts file>` (run it again after step 5 builds the PDF; `--years` sets the page limit)
   - Fix everything it reports. Do not show the resume as final until it passes.
5. Build the PDF: `python tools/build_resume.py my-files/resume.md my-files/resume.pdf`. If the user already had a `resume.pdf`, first copy it to `backups/resume-before-<YYYY-MM-DD>.pdf`.
6. Check the page count the build reports: one page for under ten years of experience, two at most otherwise. If it is over, cut the oldest or weakest bullets (ask the user which), never the font size below the minimum.
7. Ask the user to open the PDF and approve it. Only an approved PDF is used to apply.

## Part D. Tailored version for one listing (only when the user asks)

1. Read the listing's `postingText`. List the posting's top requirements in plain words.
2. Build a tailored copy from the same facts file:
   - **Allowed:** reorder bullets, choose which facts to show, shorten bullets, rewrite the summary for this role, use the posting's own words for a skill **only where the facts show that skill**.
   - **Not allowed:** any fact, number, tool, title or skill not in the facts file. Changed dates or titles. Copying sentences from the posting.
3. Show what changed compared with the main resume, in a short list.
4. Write the tailored text to `my-files/resumes/resume-<listing id>.md`, run the same checks on it, then build `my-files/resumes/resume-<listing id>.pdf`. Never overwrite `my-files/resume.md`.
5. After the user approves it, take a snapshot, add a history line to the listing: `YYYY-MM-DD tailored resume approved: resume-<listing id>.pdf`, then run `python tools/check_tracker.py check backups/before.json backups/after.json --stage resume`. Stage 03 uploads that file for that listing instead of `resume.pdf`.

## Outputs

- `my-files/resume-facts.md`, approved by the user, with a confirmed "What employers ask for" section.
- `my-files/resume.md` and `my-files/resume.pdf`, approved by the user.
- Optional: tailored PDFs in `my-files/resumes/`, each approved.
- No tracker writes, except the one history line for an approved tailored version.

## Done when

- [ ] The user approved the facts file before any resume was written.
- [ ] A "What employers ask for" section is saved in the facts file, built from 3 to 5 real postings or from a named fallback, and the user confirmed it.
- [ ] No term from the postings was used unless it is in the facts file.
- [ ] Every number, title, date, tool and skill on the resume is in the facts file (`check_resume.py`).
- [ ] `check_resume.py` passes: no dashes, no pronouns, no personal data that does not belong on a resume, bullets a sensible length, standard headings.
- [ ] The page count is within the limit.
- [ ] The user approved the final PDF.
- [ ] Any earlier `resume.pdf` was backed up first.
