# Settings record and starter answer bank

What the intake writes to the tracker after `my-rules.md` is approved. Column meanings are in `shared/tracker-columns.md`.

## The settings record

The record's id is `main`. In the spreadsheet it already exists (the template has it), so **update** that row (`tools/sheet.py` op `update`, id `main`). In a new artifact tracker it does not exist yet, so create it with `set`. Show the values first and save after the user says yes.

- `tierA`, `tierB`, `tierC`: what each employer tier means for this user. Work them out from section 2 (Place) of `my-rules.md`; the user approves them with the other settings. Default when the place rules give nothing more: A "Employer based in my home metro", B "Employer elsewhere with jobs open to my area", C "Other allowed place" (for example a nearby city allowed only above a pay bar). For someone who works only remotely: A "Remote roles open to my state, employer nearby or in my state", B "Remote roles open to my state, employer elsewhere", C "Remote roles with limits I need to check".
- `industryOrder`: the "in" industries, most wanted first.
- `excludedIndustries`: from interview question 16.
- `roleFamilies`: the kinds of role from questions 1 to 3, with a `*` after the ones that are targets.
- `tracks`: leave as `Main` unless the user is searching for two quite different kinds of role.
- `priorities`: leave as `High; Medium; Low; On hold` unless the user asks.

If the tracker does not exist yet, keep these values in the chat, tell the user, and write them the first time the tracker exists.

## Starter answer bank

Ask: "Do you want to start your answer bank now? It holds the answers application forms ask for again and again, so you are not asked each time. You can also fill it later." If yes, ask one item at a time, in this order. The user may skip any item. Save the confirmed items together in one write after the last one (spreadsheet: one `tools/sheet.py apply` changes file), or save what is confirmed so far if the session has to stop early.

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
