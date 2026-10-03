# Tracker access

How every stage reads, writes, backs up and checks the tracker. Which tracker the user has, and where, is in `my-setup.md`. Every column is described in `tracker-columns.md`.

Run every command from the workspace root (the folder that holds `CLAUDE.md`). Use the Python command saved in `my-setup.md` (`python`, `python3` or `py`). In a chat with no folder, follow `no-folder.md`, "Scripts", instead.

## Artifact tracker (main)

A Claude artifact page the user published from `tracker/tracker-page.html`, with its own database. The link is in `my-setup.md`.

- **Read** with the `ArtifactData` tool: `list` for a collection, `get` for one row. Collections: `companies`, `coverage`, `listings`, `answers`, `settings`.
- **Write** one row at a time: `update` for an existing row, `set` for a new one.
- **Re-read before writing.** Read the row fresh just before you change it, and write only the fields you changed. Pass the `version` you read as `if_version` on every write to an existing row (a new row needs none). The database refuses the write if the row changed since ("version_mismatch"): read it again and redo the write against what it holds now.

## Spreadsheet tracker (fallback)

`tracker/my-tracker.xlsx`, a copy of `tracker/spreadsheet/job-search-tracker.xlsx`, with tabs of the same names and the same columns.

- Read it with `tools/sheet.py list tracker/my-tracker.xlsx <tab>` (every row) or `show ... <tab> <id>` (one row). Write it with `tools/sheet.py apply`, or with Python and openpyxl.
- Changes files for `sheet.py apply` hold personal data: save them as `tracker/backups/<stamp>-changes.json`.
- Ask the user to close the file in Excel before a session writes to it. If it is open, saving fails with a message saying so.
- If a row changed since you read it, stop and read it again.

## Direct requests

When the person asks for a tracker change outside a stage, take a snapshot first and run the check with `--stage user` afterwards.

- **A status change:** read the row fresh, change `status`, and append a history line: `YYYY-MM-DD status set to <status> at the user's request.` When the new status is Applied, also set `appliedDate` (ask the date). After a fill sheet, use the history line in `stages/03-apply/references/apply-procedure.md`, "No browser Claude can use".
- **A job they applied to on their own:** add the employer first if it is not on the target list (`adding-employers.md`), then add a `listings` row with every column `check_tracker.py` requires: `id` (`<company-slug>-<req id or short title slug>`, unique), `company` (as in `companies`), `title`, `location`, `url`, `industry`, `pay` (or "not posted"), `why` (one line, for example "Applied by the user outside a session"), `teaches` ("Not read." if unknown), `priority`, `status` `Applied`, `appliedDate` (the date they give), `postingText` (the posting if they have it; otherwise "Not saved: applied outside a session"), and `history`: `YYYY-MM-DD added at the user's request; applied on their own on YYYY-MM-DD.` Leave `yourNotes` empty.

## Backups and snapshots

All tracker backups and snapshots go in `tracker/backups/`. Git never shares that folder.

Snapshots get a dated name, so no session overwrites another: `<stamp>` below means the session's start time and stage, for example `2026-10-03-0915-sweep`. Every `before` snapshot is a full copy of the tracker, so it is also the session's backup.

**Before more than five writes in one session** (count rows written, not commands) on the spreadsheet, also save a copy of the file, so it is easy to restore. For the artifact tracker the `before` snapshot is enough. Either kind can also be backed up on its own at any time:

- Artifact: list every collection with `ArtifactData` (`out_dir` set to a new folder under `tracker/backups/`), then combine them with `python tools/check_tracker.py snapshot-dir <that folder> tracker/backups/tracker-backup-<YYYY-MM-DD>-<HHMM>.json`.
- Spreadsheet: `python tools/sheet.py backup tracker/my-tracker.xlsx`.

## Checking by script

Every stage that writes ends with a check: `tools/check_tracker.py` compares a snapshot from before the session with one from after, and fails if any rule was broken (`yourNotes` changed, history rewritten, a listing at Applied or later touched by a sweep, a new listing missing a column, and so on). A stage is not done until the check passes.

**Spreadsheet:**

```
python tools/check_tracker.py snapshot tracker/my-tracker.xlsx tracker/backups/<stamp>-before.json
  (the session runs)
python tools/check_tracker.py snapshot tracker/my-tracker.xlsx tracker/backups/<stamp>-after.json
python tools/check_tracker.py check tracker/backups/<stamp>-before.json tracker/backups/<stamp>-after.json --stage sweep
```

**Artifact:** list each of the 5 collections with `ArtifactData` (`list`, with `out_dir` set to `tracker/backups/<stamp>-before-db`). That saves one file per row. Then combine them:

```
python tools/check_tracker.py snapshot-dir tracker/backups/<stamp>-before-db tracker/backups/<stamp>-before.json
  (the session runs)
  (list the 5 collections again with out_dir tracker/backups/<stamp>-after-db)
python tools/check_tracker.py snapshot-dir tracker/backups/<stamp>-after-db tracker/backups/<stamp>-after.json
python tools/check_tracker.py check tracker/backups/<stamp>-before.json tracker/backups/<stamp>-after.json --stage sweep
```

Use the stage's own name in `--stage`. A fresh `after-db` folder each time keeps rows deleted during a session from lingering from an earlier run.

The `--stage` choices are `intake`, `sweep`, `fit`, `apply`, `outreach`, `prep`, `mailbox`, `resume`, `research` and `user` (a change the user asked for directly).

**When a check fails because of something the user did** (they typed a note, or changed a status on the tracker page during the session), tell the user. Never undo their change, and never write `yourNotes` to make a check pass.
