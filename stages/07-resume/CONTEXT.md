# Stage 07: Resume

Build the user's resume from facts they state, shaped by what real postings for their target role ask for, and checked by script before anyone sees it as final. Also makes tailored versions for single listings. Run when the user asks ("Build my resume").

**Nothing on the resume may be something the user did not say.** Every fact comes from `output/resume-facts.md`, which the user confirms line by line.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Stage 00 | `../00-intake/output/my-rules.md` | Target roles, industries, place, writing style | What the resume is for |
| Shared | `../../shared/my-setup.md` | Full file | Tracker kind and location, Python command, browser, email connector |
| Shared | `../../shared/rules.md` | Section 10 | Writing rules |
| Shared | `../../shared/tracker-access.md` | Full file | Only for a tailored version's history line |
| Shared | `../../shared/recurring-mistakes.md` | Full file | Read before any tracker write |
| Shared | `../../shared/next-steps.md` | "After the resume" | What to suggest when the session ends |
| User | Their current resume, if any (`output/resume.pdf` or pasted) | Full content | A source of facts only |
| Tracker | `listings` | `postingText` of listings for the target role | Real postings, and the listing for a tailored version |
| Reference | `references/fact-questions.md` | Full file | Collecting the facts |
| Reference | `references/resume-facts-template.md` | Full file | The shape of the facts file |
| Reference | `references/employer-asks.md` | Full file | What employers ask for, and the fallbacks |
| Reference | `references/resume-guide.md` | Full file | General rules, examples by field, the default, the file format |
| Reference | `references/sample-resume.md` | Full file | A finished example of the format |
| Reference | `references/writing-and-tailoring.md` | The part for this request | Writing, checking, building, tailoring, opting out |

## Process

1. If the user keeps their own resume, follow `writing-and-tailoring.md`, "The user keeps their own resume", and stop there.
2. Collect the facts one question at a time (`fact-questions.md`) into `output/resume-facts.md`.
3. **[Checkpoint]** The user approves the whole facts file.
4. Learn what employers ask for from 3 to 5 real postings, or a named fallback (`employer-asks.md`).
5. **[Checkpoint]** The user confirms the summary. Save it in the facts file.
6. Write `output/resume.md` one section at a time, each one approved.
7. Run `check_resume.py` and fix everything it reports.
8. Back up any earlier PDF, build `output/resume.pdf`, check the page count, and run the check again.
9. **[Checkpoint]** The user opens and approves the PDF.
10. For a tailored version, follow `writing-and-tailoring.md`, "A tailored version for one listing".
11. End by suggesting the next step in one or two lines (`next-steps.md`, "After the resume"). Suggest only; do not start it.

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 2 | The complete facts file | Approve, or what to change |
| 4 | What employers ask for, with the postings it came from | Confirm, or what to change |
| 6 | Each resume section | Yes, or changes |
| 8 | The finished PDF | Approve, or what to change |
| 10 | What a tailored version changed | Approve, or what to change |

## Audit

| Check | Pass Condition |
|-------|---------------|
| Facts first | The user approved the facts file before any resume was written |
| Employer asks | A confirmed "What employers ask for" section is saved, from 3 to 5 real postings or a named fallback |
| Terms | No term from the postings was used unless it is in the facts file |
| Facts only | Every number, title, date, tool and skill on the resume is in the facts file (`check_resume.py`) |
| Style | `check_resume.py` passes: no dashes, no pronouns, no personal data that does not belong, sensible bullets, standard headings |
| Length | The page count is within the limit |
| Approval | The user approved the final PDF, and any earlier `resume.pdf` was backed up first |
| Next step | The session ended with the next thing to say, in quotes |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Facts file | `output/resume-facts.md` | The template's shape, approved, with "What employers ask for" |
| Resume text | `output/resume.md` | The format in `resume-guide.md` |
| Resume PDF | `output/resume.pdf` | One-column PDF, approved by the user |
| Tailored versions | `output/resume-[listing-id].md` and `.pdf` | Same format, each approved |
| Earlier PDF | `output/resume-before-[YYYY-MM-DD].pdf` | The user's previous file, unchanged |
