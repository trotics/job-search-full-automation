# Adding employers to the target list

The one way any session adds an employer to `companies`. Only when the user asks, or approves a suggestion.

1. Find the employer's own careers site. A redirect to the company's own careers subdomain, or to the job board the company itself links to (Workday, Greenhouse, Lever, Ashby and the like), counts as its own site. If the link you tried does not open, find the real one from the company's own home page. Never guess: leave the employer out until you have it.
2. Check that it is not already on the target list (exact name, `recurring-mistakes.md` item 7), not in an excluded industry, not the user's current employer, and not on the never-contact list in the user's rules.
3. Build the row:
   - `id`: the name in lowercase with hyphens, for example `example-health-co`. Check no other row uses it.
   - `company`: the employer's own spelling.
   - `careersSite`: the link from step 1.
   - `tier`: `A`, `B` or `C`, using the user's tier meanings in `settings`.
   - `industry`: in the words of `settings.industryOrder` where it fits.
   - `keepAnyway`: `no`.
   - `onHold`: `yes` only if the user's rules put this employer on hold, otherwise `no`.
   - `added`: today, `YYYY-MM-DD`.
4. Show the list to the user before saving. Write only the employers they approve, with a snapshot before and a check after (`tracker-access.md`). Inside a sweep or a fit review, that stage's own check covers it. Anywhere else (the intake, company research, or a direct request), run the check with `--stage research`.
