# Working with helpers (subagents)

Rules for any session that hands reading work to research helpers.

- About **6 employers per helper**, and a cap of about 50 tool calls each. A board with more than about 200 jobs goes alone or with very small boards. Helpers given 11 or more employers silently dropped some.
- Each helper loads its browser tools once, **opens its own tab** (never a shared one), and closes only its own tab.
- Each helper writes its final findings to a file in the stage's `output/` folder as well as returning them (a hand-back can be lost), and returns at most about 20 KB.
- Every finding carries: job number, title, location as written, the employer's own job address, the board's work-type tag, pay if posted, and the **quoted requirement lines**. If the requirements could not be read, the helper says so.
- Give helpers only confirmed board addresses, or have them find the board from the careers page first.
- Helpers only read: no tracker writes, no applications, no sign-ins, no bot-check workarounds.
- The main session re-checks every finding against the rules, opens at least one posting per helper on the employer's own site, and does every write.
