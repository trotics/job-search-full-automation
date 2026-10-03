# Stage 08: Company research

Research sessions the user starts by asking: (A) find employers, (B) a company deep dive, (C) an industry map, or (D) role research. Only part A writes to the tracker, and only after the user approves each employer.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| User | The request | Which kind, and its subject | What to research |
| Stage 00 | `../00-intake/output/my-rules.md` | Target roles, place, pay, industries, employers | What fits, and who never to suggest |
| Stage 07 | `../07-resume/output/resume.md` | Full file, if it exists | The user's stated facts, for fit notes |
| Shared | `../../shared/my-setup.md` | Full file | Tracker kind and location, Python command, browser, email connector |
| Shared | `../../shared/tracker-access.md` | Full file | Part A only: reading, writing and the check |
| Shared | `../../shared/recurring-mistakes.md` | Full file | Read before any tracker write |
| Shared | `../../shared/adding-employers.md` | Full file | Part A: checking and writing each employer |
| Shared | `../../shared/helpers.md` | Full file | Only if you use research helpers |
| Shared | `../../shared/prompts.md` | "Finding employers and researching them" | Wording the user can use |
| Shared | `../../shared/next-steps.md` | "After company research" | What to suggest when the session ends |
| Tracker | `companies`, `settings` | All rows | The target list, tiers, industry words |
| Previous runs | `output/` | "Checked and not added" and "Leads" lists | So earlier work is not repeated |
| Reference | `references/research-rules.md` | Full file | Sources, links, names, size, the four kinds |
| Reference | `references/find-employers.md` | Full file | Part A |
| Reference | `references/other-research.md` | The part asked for | Parts B, C and D |

## Process

1. Name the kind (A, B, C or D) and say in one line what you will look for.
2. For part A, agree a target number with the user and take a tracker snapshot.
3. Research from allowed sources only, every fact linked (`research-rules.md`).
4. Part A: check every candidate, and stop at the target, at low yield, or at the budget (`find-employers.md`).
5. **[Checkpoint]** Part A: show the candidates in one table for the user to approve, drop or change.
6. Part A: write only the approved employers, take an after snapshot, and run the check with `--stage research`.
7. Run the audit below, then save the report.
8. End by suggesting the next step in one or two lines (`next-steps.md`, "After company research"). Suggest only; do not start it.

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 1 | What you will look for | Go, or a different focus |
| 4 | Candidate employers, with careers site, tier, fit and source | Approve, drop or change each one |

## Audit

| Check | Pass Condition |
|-------|---------------|
| Links | Every fact in the report has a link to an allowed source |
| Access | No LinkedIn page was opened, no site required a sign-in, nothing was scraped |
| Part A approval | Every new employer was approved by the user and has its own careers site link |
| Part A names | No new employer matches an existing name, an excluded industry or a never-contact entry |
| Check | Part A: `check_tracker.py --stage research` passes |
| Next step | The session ended with the next thing to say, in quotes |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| New employers (A) | Tracker, `companies` | One approved row each |
| Find-employers report (A) | `output/[YYYY-MM-DD]-find-employers.md` | Added, borderline, checked and not added, leads |
| Company report (B) | `output/[company-slug]-company-research.md` | The six parts of B, every source linked |
| Industry map (C) | `output/[industry-slug]-industry-map.md` | Employers by type, every source linked |
| Role report (D) | `output/[title-slug]-role-research.md` | Duties, requirements, posted pay, next roles, every source linked |
