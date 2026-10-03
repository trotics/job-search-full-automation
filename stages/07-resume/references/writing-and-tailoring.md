# Writing the resume, and tailored versions

Run every command from the workspace root. `<out>` below means `stages/07-resume/output`.

## The user keeps their own resume

If the user opted out (setup's resume choice "use mine"), do not rewrite or critique it. Their file is `<out>/resume.pdf`. Offer to make the text copy `<out>/resume.md` from it for filling forms, and show the copy before saving. You may offer one short list of suggestions from `resume-guide.md`, once, and only if they want it.

## Writing the main resume

1. Write `<out>/resume.md` in the exact format in `resume-guide.md` ("File format"). `sample-resume.md` shows a finished one.
2. Follow every rule in "General rules" and the "What employers ask for" section saved in the facts file. The resume's sections come in that section order. For a step-up resume, lead each job with the confirmed facts that show next-level scope: leading or training people, owning results, cross-team work (`shared/career-direction.md`, "Advancement").
3. Draft **one section at a time**, in that order (contact line and summary always first). Show each one and get a yes or changes before the next.
4. Show the whole resume, and check the text:
   `python tools/check_resume.py <out>/resume.md --facts <out>/resume-facts.md`
   Fix everything it reports. Do not show the resume as final until it passes.
5. If the user already had a `resume.pdf`, first copy it to `<out>/resume-before-<YYYY-MM-DD>.pdf`. Then build the PDF: `python tools/build_resume.py <out>/resume.md <out>/resume.pdf`, and check again with the PDF and the page limit:
   `python tools/check_resume.py <out>/resume.md --facts <out>/resume-facts.md --pdf <out>/resume.pdf --years <years from the facts file>`
6. Check the page count the build reports: one page for under ten years of experience, two at most otherwise. If it is over, cut the oldest or weakest bullets (ask the user which), never the font size below the minimum.
7. Ask the user to open the PDF and approve it. Only an approved PDF is used to apply.

## A tailored version for one listing (only when the user asks)

1. Read the listing's `postingText`. List the posting's top requirements in plain words.
2. Build a tailored copy from the same facts file:
   - **Allowed:** reorder bullets, choose which facts to show, shorten bullets, rewrite the summary for this role, use the posting's own words for a skill **only where the facts show that skill**.
   - **Not allowed:** any fact, number, tool, title or skill not in the facts file. Changed dates or titles. Copying sentences from the posting.
3. Show what changed compared with the main resume, in a short list.
4. Write it to `<out>/resume-<listing id>.md`, check the text, build `<out>/resume-<listing id>.pdf`, then check again with `--pdf` and `--years`, as in steps 4 and 5 above. Never overwrite `resume.md`.
5. After the user approves it, take a tracker snapshot, add a history line to the listing: `YYYY-MM-DD tailored resume approved: resume-<listing id>.pdf`, then run the check with `--stage resume`.
