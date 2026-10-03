# Stage 04: Hiring-manager outreach

**Off unless the user starts it by name in the session** ("run outreach"). Never as a side task of another stage. **Drafts only. The user sends every message.**

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| User | "Run outreach", in this session | The request | Nothing runs without it |
| Stage 00 | `../00-intake/output/my-rules.md` | Pay, place, autonomy, writing style | Which listings qualify, and how drafts sound |
| Stage 07 | `../07-resume/output/resume.md` | Full file | Facts used in messages |
| Shared | `../../shared/rules.md` | Sections 7 to 10 | Status rules, autonomy, safety, writing |
| Shared | `../../shared/my-setup.md` | Full file | Tracker kind and location, Python command, browser, email connector |
| Shared | `../../shared/tracker-access.md` | Full file | Reading, writing and the check |
| Shared | `../../shared/recurring-mistakes.md` | Full file | Read before any tracker write |
| Shared | `../../shared/next-steps.md` | "After outreach" | What to suggest when the session ends |
| Tracker | `listings`, `companies` | Qualifying listings | What to research |
| Reference | `references/outreach-rules.md` | Full file | Qualifying listings, sources, confidence, drafts |

## Process

1. Take a tracker snapshot.
2. Count the qualifying listings (`outreach-rules.md`) and tell the user the number before any research.
3. Work them in order: highest pay first, home metro before remote, 10 per session unless the user says otherwise.
4. Find the likely hiring manager from web search and the employer's own pages only. Rate the confidence.
5. Draft the connection note and the longer message in the user's writing style.
6. Save the outreach columns and one history line per listing worked.
7. Take an after snapshot and run the check with `--stage outreach`.
8. Run the audit below, then save the report.
9. End by suggesting the next step in one or two lines (`next-steps.md`, "After outreach"). Suggest only; do not start it.

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 2 | How many listings qualify | Go, a smaller set, or stop |
| 5 | The drafts, in the report | Whether and how to send each one (the user sends) |

## Audit

| Check | Pass Condition |
|-------|---------------|
| Started by name | The user started this stage by name in this session |
| No LinkedIn, no sending | No LinkedIn page was opened and nothing was sent |
| Length | Every connection note is under 300 characters and every message under 90 words |
| Style | No em dashes or en dashes in any draft |
| Columns | Only the outreach columns and history were written (`check_tracker.py --stage outreach`) |
| Next step | The session ended with the next thing to say, in quotes |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Outreach drafts | Tracker, `listings` outreach columns | Contact, confidence, two drafts per listing |
| Outreach report | `output/[YYYY-MM-DD]-outreach-report.md` | Each contact, confidence, and anything the user should know (wrong place, posting closed) |
