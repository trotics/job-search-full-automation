# Resume guide

Rules for every resume stage 07 writes, for any job in any field. "General rules" always apply. What goes first on a resume comes from real postings for the user's target job (stage 07 Part B). The examples by field below show finished results for common jobs; they are not a list the user must fit into. When nothing else is available, use the default, so every user gets a resume.

## General rules

**Honesty**
- Every fact comes from `my-files/resume-facts.md`. Nothing invented, nothing rounded up, no title the user did not hold, no tool they did not use.
- Numbers appear exactly as the facts file states them.
- Strong verbs only where the facts support them. "Led" needs a fact that says they led. "Managed" needs people or a budget they managed.
- Dates are real. Gaps are not hidden by changing dates.

**Format (so application systems can read it)**
- One column. No tables, text boxes, graphics, icons, photos, charts or skill-level bars.
- Standard headings: Summary, Experience, Education (only if the user has any), Licenses and Certifications (if any), Skills. Optional: Volunteer Work, Languages, Military Service, Projects, Portfolio. Their order comes from the "What employers ask for" section of the user's facts file; the default order is Summary, Experience, Education, Licenses and Certifications, Skills.
- Plain fonts. The build script uses Helvetica, 10 to 11 point for body text, never below 9.5.
- Length: one page for under ten years of experience, two pages at most.
- Dates in one style throughout: "Mar 2021 to Present" or "2021 to Present". Words, not dashes.
- Saved as PDF with the user's name in the file name only if the user wants that. Default: `resume.pdf`.

**Contact line**
- Name, city and state, email, phone. Optional: LinkedIn or portfolio link, if the user gives it.
- Never: street address, date of birth, age, photo, marital status, nationality, Social Security or other ID numbers, license numbers, salary history.

**Summary**
- Two or three lines. Who they are in this field, their strongest proof, and what they are moving toward.
- No pronouns at all ("I", "my", "she", "her"). No buzzwords.

**Bullets**
- Start with a verb: past tense for past jobs, present tense for the current one.
- One idea per bullet. At most two lines (about 200 characters).
- Lead with the result when there is one: what changed, by how much, for whom.
- Three to six bullets for recent roles, one to three for older ones. Roles over 15 years old may be grouped under "Earlier experience" with titles only.
- Numbers as digits ("12 nurses", "$1.2 million"). Spell out an acronym once unless everyone in the field knows it.

**Words:** no word is off limits. A label like "team player" works best next to a fact that shows it ("trained 6 apprentices"). No em dashes or en dashes.

## Default (any job)

Used when no postings can be found and the user cannot describe the jobs they want. It suits every field.

- Section order: Summary, Experience, Education, Licenses and Certifications (if any), Skills.
- Summary: the role they want, their years doing the closest work, and their strongest fact.
- Each job leads with the bullet that shows the biggest result or the most responsibility, then the work most like the target role.
- Skills: the tools and skills from the facts file that the target role most likely uses. Ask the user which those are.
- Plain tone. One page under ten years of experience.

## Examples by field

What usually goes first on a resume for some common jobs. For a real user, this always comes from postings for their own target job (stage 07 Part B). These examples help spot anything missed. A job not listed here is handled exactly the same way.

**Sales and business development**
- Summary names the kind of sale (new business or existing accounts, deal size, buyer) and the best number.
- Every role leads with quota attainment, revenue, rank or deals closed, if the facts have them, with the period ("in 2024", "first quarter").
- Show the sales cycle and buyer: who they sold to, how long deals took, what they sold.
- Skills: CRM and prospecting tools the user actually used.

**Healthcare (clinical)**
- Licenses and Certifications move up, directly under the summary. Use full names (for example "Registered Nurse, [State]" and "Basic Life Support").
- Each role names the setting (intensive care, outpatient clinic), unit size or patient load if known, and specialties.
- Results are about safety, quality, training and process: audits passed, protocols adopted, staff trained.

**Healthcare technology or medical sales (and other industries that sell to clinicians)**
- Clinical credentials near the top, because buyers trust clinicians.
- Bullets that show persuading, training, adopting new systems, working with vendors, or leading change come first in each clinical role.
- A short "Systems" line in Skills: charting and other software used.

**Software, IT and technical roles**
- Skills section near the top, grouped (languages, tools, platforms). Only what the user can discuss in an interview.
- Bullets show what was built or fixed, scale (users, data, uptime) and the result.
- A link to a portfolio or code samples if the user has one.

**Finance, insurance and banking**
- Licenses and designations near the top (with state and status, never numbers).
- Bullets show accuracy, compliance, portfolio or book size, and client retention.
- Conservative tone. No casual phrasing.

**Education and training**
- Certifications and subjects near the top.
- Bullets show learners served, outcomes, programs built.

**Skilled trades, logistics and operations**
- Certifications, licenses and equipment near the top.
- Bullets show safety record, volume, on-time rates, cost or time saved.

**Government and nonprofit**
- Fuller detail is expected: two pages are fine with enough experience.
- Name programs, funding sources, communities served and outcomes.
- Match the posting's required qualifications in plain words where the facts support them.

**Creative, marketing and communications**
- Portfolio link in the contact line.
- Bullets show campaigns, audiences, reach and results.
- Still one column and plain fonts: the portfolio carries the visual style, the resume stays readable by systems.

## Career changers

- The summary bridges the two fields in one sentence: what they did, what carries over, what they are moving into.
- Keep the experience in time order. Do not hide the old field.
- In each past role, put first the bullets that match the new field (persuading, training, numbers, customers, systems).
- A "Relevant Skills" line can come before Experience if the user has very little direct experience. Every skill on it must appear somewhere in the facts.
- Never use a title from the new field for a job in the old field.

## File format (for `my-files/resume.md`)

The build script reads exactly this shape:

```
# Full Name
City, State | email@example.com | (555) 010-0000 | optional link

## Summary
Two or three lines of plain text.

## Licenses and Certifications
- [License name], [State]

## Experience
### Job Title | Employer | City, State | 2023 to Present
- Bullet.
- Bullet.

## Education
### Degree, Field | School | Year

## Skills
- Group: item, item, item
```

Headings use `##`. Jobs and schools use `###` with ` | ` between title, employer, place and dates. Bullets start with `- `.

If the user chose not to show a school year, leave it off: `### Degree, Field | School`. If the user has no degree or diploma to show, leave the Education section out; never invent one.
