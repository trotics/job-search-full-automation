# Stage 05: Interview prep

Prepare the user for a named interview. Run when the user asks.

## Tracker access

- **Artifact:** read the listing with `ArtifactData` (`get`). The only write is an optional history line.
- **Spreadsheet:** read the listing's row in `my-files/job-search-tracker.xlsx`.

## Inputs, and which sources count

Use only these sources:

1. **The saved posting:** the listing's `postingText`. Use it even if the live posting is gone. If `postingText` is empty and the posting is gone, say so and ask the user for a copy (an email, a PDF, a screenshot).
2. **The listing row:** title, pay, `why`, `history` (recruiter names, interview format and time) and `yourNotes` (read only).
3. **The employer's own website:** what they sell, to whom, leadership, press releases.
4. **Recent news** from established news outlets and trade publications, found by web search, each linked.
5. **The user's own record:** `my-files/resume.md` and the answer bank's work history entries. The user's stated history is the only source for their stories.

Do not use as fact: anonymous review sites, aggregator job listings, social media posts, or anything you cannot link. You may mention review-site themes only as "people say", and only if the user asks.

## Steps

1. Confirm with the user which interview, the stage (phone screen, hiring manager, panel, onsite), and who they are meeting, if known.
2. **Company brief:** what they sell, to whom, how the team does its work, recent news, and where this role sits. Every fact gets a link.
3. **Likely questions:** from the posting's requirements and the interview stage, including the hard ones the user's record invites (a short stint, a career change, a gap, missing industry experience).
4. **The user's stories:** map each likely question to a true story from the resume or the answer bank's work history. Invent nothing. Mark any gap so the user can fill it.
5. **Questions for the user to ask** the interviewer.
6. **Logistics** from the listing's history: time, format, recording notices, who to contact.

## Outputs

- A prep file saved to `reports/interview-prep-<company-slug>-<YYYY-MM-DD>.md`, in the user's job search folder. Give the user the path.
- No tracker writes, except one history line saying prep was done, if the user wants it. For that line, take a snapshot before and after and run `python tools/check_tracker.py check backups/before.json backups/after.json --stage prep` (snapshots: `references/tracker-columns.md`, "Checking by script").

## Done when

- [ ] Every fact about the company has a link to one of the allowed sources.
- [ ] Every story is one the user has stated or the resume shows.
- [ ] The file is saved in `reports/` and the user has the path.
