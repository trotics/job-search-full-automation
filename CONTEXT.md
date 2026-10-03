# Job Search Full Automation

A job search system for one person. Set up once, then run any stage when the person asks. The stages share one tracker; files pass between stages through `output/` folders.

## Task Routing

| Task Type | Go To | Description |
|-----------|-------|-------------|
| First-time setup | `setup/questionnaire.md` | Tracker, Python, browser, then the interview |
| Set or change the person's rules | `stages/00-intake/CONTEXT.md` | The interview, one question at a time |
| Check employers for listings, recheck open listings | `stages/01-sweep/CONTEXT.md` | Reads employers' own career sites |
| Decide whether one posting fits | `stages/02-fit-review/CONTEXT.md` | The sweep runs it for every new posting |
| Fill in applications | `stages/03-apply/CONTEXT.md` | The person reviews every form before submit |
| Hiring-manager outreach drafts | `stages/04-outreach/CONTEXT.md` | Only when the person says "run outreach" |
| Prepare for an interview | `stages/05-interview-prep/CONTEXT.md` | For one named interview |
| Check email for employer replies | `stages/06-mailbox-check/CONTEXT.md` | Read only; the person approves each change |
| Build, improve or tailor a resume | `stages/07-resume/CONTEXT.md` | Only from facts the person confirms |
| Find employers, research a company, industry or role | `stages/08-company-research/CONTEXT.md` | Adds employers only after approval |
| Add employers the person names | `shared/adding-employers.md` | Outside a stage, checked with `--stage research` |
| A status change the person asks for directly | `shared/tracker-access.md` | Checked with `--stage user` |

## Shared Resources

| Resource | Location | Contains |
|----------|----------|----------|
| Rules | `shared/rules.md` | Fit rules, who writes what, autonomy limits, safety, writing |
| My setup | `shared/my-setup.md` | Tracker kind and location, Python command, browser, email connector (made by setup from `shared/my-setup-template.md`) |
| Tracker columns | `shared/tracker-columns.md` | Every collection and column, in plain words |
| Tracker access | `shared/tracker-access.md` | Reading, writing, backups, snapshots and the check script |
| Answer bank | `shared/answer-bank.md` | How to use the answers forms ask for |
| Adding employers | `shared/adding-employers.md` | The one way to add an employer |
| Recurring mistakes | `shared/recurring-mistakes.md` | Read before any tracker write |
| Helpers | `shared/helpers.md` | Rules for research helpers (subagents) |
| Prompts | `shared/prompts.md` | What the person can say to start each stage |
| Python setup | `shared/python-setup.md` | Installing and checking Python |
| Tracker page | `tracker/tracker-page.html` | The page published as the person's tracker |
| Scripts | `tools/` | `check_tracker.py`, `check_resume.py`, `build_resume.py`, `sheet.py` |

## No folder to work in

On Claude on the web or a tablet there may be no folder Claude can read and write. Then ask the person to attach `my-rules.md` and `my-setup.md` (and `resume-facts.md` for the resume stage) at the start of each chat, or keep them in a Claude Project. Give every file you create or change as a download, and tell them to save it and attach it next time. Sweeps of most career sites, and applying, need the desktop app.
