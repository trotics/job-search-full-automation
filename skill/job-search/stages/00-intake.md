# Stage 00: Intake interview

Set up a new user, or change an existing user's rules. Ends with `my-files/my-rules.md` saved, the tracker's `settings` record filled, and, if the user wants them, a starter answer bank, a resume (stage 07) and a first list of employers (stage 08).

## How to run it

- Ask **one question at a time**. Wait for the answer before asking the next one.
- Keep each question short. Give one or two examples so the user knows what kind of answer fits. Examples should not lead the user toward any industry.
- If an answer is vague, ask one follow-up. If it is still vague, write down what they said and move on.
- Never guess an answer. If the user skips a question, write "None" or "Not decided" in that line.
- If `my-files/my-rules.md` already exists, read it first. Only ask about the parts the user wants to change, then add a dated line to section 10.

## Inputs

- `references/my-rules-template.md`: the shape of the finished file.
- `rules.md`: the general rules, so you can explain them when asked.
- `stages/07-resume.md` and `stages/08-company-research.md`, which the intake can hand off to at the end.

## Questions

Ask them in this order. The number in brackets is the section of `my-rules.md` it fills.

**Tracker**
1. "Will you keep your tracker as a Claude artifact (a web page in your Claude account) or as a spreadsheet file?" [Tracker]
   - **Artifact, already published:** "Paste the link." Save it.
   - **Artifact, not published yet:** offer to publish it now, together: publish `tracker/tracker-page.html` as a new artifact with the `db` capability (README, "Set up your tracker"), show the user the empty tracker, and save the link. If publishing is not possible here (for example on a device without that feature), offer the spreadsheet for now.
   - **Spreadsheet:** copy `tracker/spreadsheet/job-search-tracker.xlsx` to `my-files/` and save that path.
   - The tracker must exist before step 4 below writes `settings` and `answers` to it. If it still does not exist by then, keep those values in the chat, tell the user, and write them the first time the tracker exists.

**Target roles**
2. "What kind of job are you looking for? Name a few titles if you can." [1]
3. "What level: entry, mid, senior, or a range?" [1]
4. "Are there roles with similar titles that you do not want? For example, a title that sounds right but is really support or admin work." [1]
5. "In a sentence or two, what does a good fit look like to you?" [1]

**Place**
6. "Where do you live? A city or metro area is enough." [2]
7. "Which of these work for you: jobs in your home metro, a territory based out of your home metro, a territory covering several states, fully remote?" [2]
8. "For remote jobs, are there limits? For example, some remote jobs only hire in certain states." [2]
9. "Are any nearby cities OK only if the pay is high enough? If so, which cities and what pay?" [2]
10. "Would you move for the right job? If yes, where?" [2]

**Pay**
11. "What is the lowest pay you will accept? Say whether that is per year or per hour." [3]
12. "Does that floor count base salary only, or base plus commission or bonus?" [3]
13. "When a form lets you type your pay expectation, how do you want it worded?" [3]
14. "When a form needs a single number, what number?" [3]

**Industries and products**
15. "Which industries or kinds of products are you most interested in?" [4]
16. "Which industries or products are out for you, and why?" [4]
17. "Of the ones that are out, which should be hidden in your tracker entirely?" These become `excludedIndustries`. [4]

**Experience**
18. "How many years of experience do you have in the kind of work you are targeting? What counts?" [5]
19. "If a posting asks for more years than you have, how far would you still apply? For example, up to two more years." [5]
20. "What licenses or certifications do you hold?" [5]
21. "What degrees do you hold, and in what field?" [5]

**Hard noes**
22. "Anything that is an automatic no? For example: part-time, contract, commission only, night shifts, heavy travel, a license you would need before starting." [6]

**Employers**
23. "Are there employers you want tracked but not applied to yet?" These go on hold. [7]
24. "Who must never be contacted? Your current employer goes here if you have one." [7]
25. "Any employer that only posts jobs on one job site (like Indeed) and has no job board of its own?" [7]

**Autonomy**
26. "When I sweep employer sites, should I add fitting listings on my own, or ask you before writing anything?" [8]
27. "When a posting is a close call, should I decide by your rules, or bring every close call to you?" [8]
28. Tell the user, do not ask: "For applications, I fill in the form and you review it before anything is submitted. You can turn on auto-submit for one session by writing it out, but it is off by default." [8]
29. "Do you want hiring-manager outreach drafts? I only draft. You send everything yourself." [8]
30. "Do you have an email connector set up in Claude (for example Gmail or Outlook)? If yes, I can check for employer replies when you ask and suggest status updates." [8]

**Writing style**
31. "How should anything written for you sound? For example: short and direct, warm, formal. Any words or habits to avoid?" [9]

## After the last question

1. Write the full `my-rules.md` from the template and the answers. Use the user's own words where you can.
2. **Show the whole file** to the user and ask: "Is this right? Tell me anything to change, or say approve." Make changes and show the whole file again until they approve.
3. Only after approval, save it to `my-files/my-rules.md`.
4. Write the tracker's `settings` record (see `references/tracker-columns.md`). Take a snapshot first (`references/tracker-columns.md`, "Checking by script"). Show the values first and save after the user says yes. The record's id is `main`. In the spreadsheet it already exists (the template has it), so **update** that row (`tools/sheet.py` op `update`, id `main`). In a new artifact tracker it does not exist yet, so create it with `set`. Afterwards, and again after any answer bank entries in step 5, take an after snapshot and run `python tools/check_tracker.py check backups/before.json backups/after.json --stage intake`. The fields:
   - `tierA`, `tierB`, `tierC`: what each employer tier means for this user. Default: A "Employer based in my home metro", B "Employer elsewhere with jobs open to my area", C "Other allowed place".
   - `industryOrder`: the "in" industries, most wanted first.
   - `excludedIndustries`: from question 17.
   - `roleFamilies`: the kinds of role from questions 2 to 4, with a `*` after the ones that are targets.
   - `tracks`: leave as `Main` unless the user is searching for two quite different kinds of role.
   - `priorities`: leave as `High; Medium; Low; On hold` unless the user asks.
5. Ask: "Do you want to start your answer bank now? It holds the answers application forms ask for again and again, so you are not asked each time. You can also fill it later." If yes, ask one item at a time, in this order, and save each to `answers` after the user confirms it. The user may skip any item.
   - **Contact:** full name, preferred name, email, phone and phone type, city and state, county (some forms require it), street address only if they want forms filled with it.
   - **Work history:** each job (title, employer, city, start and end month and year), the **reason for leaving** each one, and whether each past employer **may be contacted**; if yes, that supervisor's name, title and contact details (some forms require them).
   - **Years of experience** in the work they are targeting, and in common form categories (customer service, sales, a key tool).
   - **Education:** school, degree, field, year.
   - **Licenses and registrations:** held, and whether any was ever denied, revoked or suspended. Never the license number.
   - **Work authorization:** authorized to work in the country, needs sponsorship now or later, age 18 or over.
   - **Pay:** the text wording, the single number, and hourly or salary.
   - **Logistics:** earliest start date, willing to relocate, willing to travel (how much), overtime and shift work.
   - **Employer relationships:** currently bound by a non-compete or other restrictive agreement; ever worked for a given employer is asked per form, so note only whether they want to be asked each time.
   - **"Ever been fired or asked to resign":** the user's own answer, or "ask me each time".
   - **References:** names, relationship and contact details, in the order to use them. Never the user's current employer.
   - **Links:** LinkedIn or portfolio (used only when a form requires it).
   - **Voluntary self-identification:** gender, Hispanic or Latino, race, veteran status (and whether "protected veteran" applies), disability. "I don't wish to answer" is a full answer for each.
   - **Optional:** pronouns, consent to text messages.
   - **Always the user's, never stored as an answer:** criminal history, assessments, whether they would sign a future non-solicitation agreement. Tell the user these will always come to them on the form.
   Never ask for or store passwords, ID numbers or bank details.
6. **Resume.** Ask: "Do you already have a resume you are happy with?" Offer three answers, and respect the choice:
   - **"Yes, use mine as it is"** (opt out): ask them to put it in `my-files/resume.pdf`. Offer to make the text copy `my-files/resume.md` from it, and show the copy before saving. Do not rewrite or critique it. Stage 07 never runs unless they ask later.
   - **"Yes, but I want it improved"**: run `stages/07-resume.md`, starting from their file. Their resume is a source of facts, and nothing changes without their yes.
   - **"No" or "I need a new one"**: run `stages/07-resume.md` from the start.
   Tell them they can skip this for now and say "build my resume" any time.
7. **Employers.** Ask: "Do you already have a list of employers you want to work for?" If yes, add them with sweep step 1. If no, or they want more, offer stage 08 part A ("suggest employers that fit my background"). Do not start it unless they say yes.
8. Point them to `references/prompts.md` for what to say in later sessions.

## Outputs

- `my-files/my-rules.md`, approved by the user.
- The tracker's `settings` record.
- Answer bank entries, if the user wanted them.
- A resume from stage 07, or the user's own resume in `my-files/`, or a note that they skipped it for now.

## Done when

- [ ] Every question was asked, one at a time, or the user skipped it.
- [ ] The user saw the complete `my-rules.md` and said approve before it was saved.
- [ ] `settings` was saved after the user said yes.
- [ ] No password, ID number or bank detail was asked for or stored.
- [ ] The user chose one of the three resume answers, or chose to skip for now, and that choice was respected.
- [ ] The user knows the next step (usually: add or find employers, then run a sweep) and where the prompts list is.
