# Recurring mistakes to avoid

Each of these happened during real use of this system. Read this list before any tracker write.

1. **Aggregator pages treated as proof.** An unattended run marked a batch of listings expired because a job aggregator showed them gone. Most were still live on the employers' own sites, and some were already Applied. Only the employer's own site decides.
2. **Changing listings at Applied or later.** The same run did it. Sweeps never touch them.
3. **Starting work nobody asked for.** A session asked to do one small task ran a whole other stage and wrote to many listings. Do only the task asked.
4. **Two sessions writing the same file.** The last write silently won and the earlier work was lost. One session owns the tracker at a time. For the spreadsheet, the user's own Excel window counts as a second writer: ask them to close it.
5. **Overloaded research helpers.** Helpers given 11 or more employers silently dropped some. Keep it to about six each.
6. **Stale reads.** Values copied from an earlier read were wrong by the time of the write. Read each row fresh right before writing it, and check by script after.
7. **Loose company matching.** A first-word match filed one company's listings under a different company whose name started the same way. Match the full company name, exactly as in `companies`.
8. **A background the user wants to leave, used as a selling point.** If the user says they are moving away from a kind of work, it is never a plus in a fit call or a message.
9. **Rules left in old prompts.** Saved prompts and notes carried outdated rules that later sessions followed. The rules live only in `rules.md` and `my-files/my-rules.md`.
10. **Shared browser tabs.** Two helpers working in one browser tab overwrote each other's pages. Each helper opens its own tab.
11. **Unattended runs that could not do the work.** A scheduled run in the cloud had no browser access to employer sites and no access to the user's folder, so it wrote bad data. Every stage is started by the user, in a session that can reach the sites and files it needs.
