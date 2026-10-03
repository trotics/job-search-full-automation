# Lessons

How the system learns from use. Every stage does this once, at the end of the session, before suggesting the next step.

## Ask once

Ask: "Did anything surprise you or go wrong this session?" Add anything you noticed yourself: a site that behaved differently from the notes, a rule that led to a wrong call, a check that caught a mistake, a step that was unclear. If there is nothing new, say nothing more and move on.

## Where each lesson goes

Show the person the exact line you would add and where. Add it only after they say yes.

| The lesson is about | Add it to |
|---|---|
| How a job board behaves | `stages/01-sweep/references/board-platforms.md` (that platform's section), or `board-techniques.md` for something true of every board |
| How an application form behaves | `stages/03-apply/references/application-platforms.md` (that platform's section), or `application-techniques.md` for something general |
| A mistake that could happen again | `recurring-mistakes.md`: a new numbered item at the end, saying what happened and the rule that prevents it |
| The person's own preferences changed | Their `my-rules.md`, through the intake stage, with a dated line in section 10 |

## Rules for every lesson

- One or two lines. Edit the existing section in place; never repeat what is already there.
- General methods only: never employer names, the person's details or dates in the shared or reference files.
- A lesson never weakens a safety rule (`rules.md` section 9) or the rule that the person reviews every application. If a lesson seems to call for that, tell the person instead of writing it.
- With no folder, give the changed file as a download (`no-folder.md`).

## Share it

After adding a general lesson about a job board or an application form, offer once: "Want to share this with everyone who uses this system? Open an issue at https://github.com/trotics/job-search-full-automation/issues with just the general method (no employer names or personal details)."
