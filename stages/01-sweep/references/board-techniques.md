# Board techniques: how to read job boards

How to find and read postings on employers' own job boards, Learned over a few hundred real employer boards. Platform-by-platform notes are in `board-platforms.md`.

Add what a session learns here (with the user's OK): a new platform, a new workaround, a trick that stopped working. Edit the platform's section in place. Never add employer names, the user's details or dates.

## Ground rules

- **Read the employer's own board, never signed in.** Most employer job boards run on an applicant tracking system (ATS) such as Workday, Greenhouse or iCIMS. The employer's careers page links to it.
- **Respect the site.** Read at a human pace. Never bulk-download a site's pages; boards that see many fast requests answer with "too many requests" (HTTP 429), and that is a sign to stop. Never get past a bot check (Cloudflare "Just a moment...", "Verifying you are human", a security checkpoint, a CAPTCHA). Mark the employer **manual** and move on.
- **Record why a board could not be read.** These are different and need different fixes:
  - **Bot check:** the site shows a challenge. A person can usually open it in their own browser.
  - **Browser refusal:** the browser tool refuses to open the site at all. A person's own browser usually works.
  - **Structural absence:** the employer has no postings of its own (it posts only through an aggregator or a staffing firm).
- **Many boards have a public data feed** that the page itself uses. Reading it is faster and more complete than reading the page. Find it with `read_network_requests` while the page loads, or with `performance.getEntriesByType('resource')` in the page when the network list shows nothing. Spend two tries on that before falling back to reading the page text.
- **Some feeds only answer from the board's own page** ("same origin"). Open the board in the tab first, then fetch from that tab. Others answer from any tab.
- **Scripts in the page can time out** after about 45 seconds when they loop over many requests. Keep partial results on `window` and split the work over several calls.
- **Keep tool results small.** A full board can be a very large result. Ask for only the fields you need, and page through.

## Boards that misreport location

Several boards ignore their own location filter, or tag a job "Remote" when it is only remote within some states or near some offices. **Always read each posting's own location text**, not the filter you sent or the headline tag.

- A location search that returns the whole global board is common (several hosted career-site platforms, some front ends built on SmartRecruiters, some iCIMS boards that ignore the country parameter).
- "Remote" often means "remote within these states" or "remote within about 70 miles of an office". The body text or a list of extra locations says which.
- A state-specific remote tag (for example "XX-REMOTE") can mean that state only, or can mean "remote, based anywhere in the country". Read the posting.
- Some city filters match only the posting's **primary** city. Check the full list of locations.
- A job-board tag such as "USA" does not mean remote. Look for "Location: Any" or similar in the body.

## Signs a posting is gone

Only the employer's own site decides. These are reliable signs:

- The page says "no longer available", "this job has been filled", or similar.
- HTTP 410 Gone (confirm once on a retry).
- On Workday: a 403 on the job endpoint plus no match when searching the board for the job number.
- On Greenhouse: the job link redirects to the employer's general careers page.
- The job number is missing from a search of the employer's whole board, and the posting page will not load.

These are **not** proof, and need a second look:

- A 404 on a saved address (job paths change with titles; search the job number).
- An aggregator showing the job as closed.
- The employer rejecting the user (the posting can stay live).
- One of two pages for the same job showing it closed while the other shows it open: trust the page with an explicit closed or filled message, and say so in history.
- A slow first load or an "initializing" page.
