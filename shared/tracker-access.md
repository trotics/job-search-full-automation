# Tracker access

How every stage reads, writes, backs up and checks the tracker. Which tracker the user has, and where, is in `my-setup.md`. Every column is described in `tracker-columns.md`.

Run every command from the workspace root (the folder that holds `CLAUDE.md`). Use the Python command saved in `my-setup.md` (`python`, `python3` or `py`).

## Artifact tracker (main)

A Claude artifact page the user published from `tracker/tracker-page.html`, with its own database. The link is in `my-setup.md`.

- **Read** with the `ArtifactData` tool: `list` for a collection, `get` for one row. Collections: `companies`, `coverage`, `listings`, `answers`, `settings`.
- **Write** one row at a time: `update` for an existing row, `set` for a new one.
- **Re-read before writing.** Read the row fresh just before you change it, and write only the fields you changed. Pass the `version` you read as `if_version` on every write to an existing row (a new row needs none). The database refuses the write if the row changed since ("version_mismatch"): read it again and redo the write against what it holds now.

## Spreadsheet tracker (fallback)

`tracker/my-tracker.xlsx`, a copy of `tracker/spreadsheet/job-search-tracker.xlsx`, with tabs of the same names and the same columns.

- Read and write it with `tools/sheet.py`, or with Python and openpyxl.
- Ask the user to close the file in Excel before a session writes to it. If it is open, saving fails with a message saying so.
- If a row changed since you read it, stop and read it again.

## Backups and snapshots

All tracker backups and snapshots go in `tracker/backups/`. Git never shares that folder.

**Before more than five writes in one session**, save a copy of the whole tracker:

- Artifact: list every collection with `ArtifactData` (`out_dir` set to a new folder under `tracker/backups/`), then combine them with `python tools/check_tracker.py snapshot-dir <that folder> tracker/backups/tracker-backup-<YYYY-MM-DD>-<HHMM>.json`.
- Spreadsheet: `python tools/sheet.py backup tracker/my-tracker.xlsx`.

## Checking by script

Every stage that writes ends with a check: `tools/check_tracker.py` compares a snapshot from before the session with one from after, and fails if any rule was broken (`yourNotes` changed, history rewritten, a listing at Applied or later touched by a sweep, a new listing missing a column, and so on). A stage is not done until the check passes.

**Spreadsheet:**

```
python tools/check_tracker.py snapshot tracker/my-tracker.xlsx tracker/backups/before.json
  (the session runs)
python tools/check_tracker.py snapshot tracker/my-tracker.xlsx tracker/backups/after.json
python tools/check_tracker.py check tracker/backups/before.json tracker/backups/after.json --stage sweep
```

**Artifact:** list each of the 5 collections with `ArtifactData` (`list`, with `out_dir` set to `tracker/backups/before-db`). That saves one file per row. Then combine them:

```
python tools/check_tracker.py snapshot-dir tracker/backups/before-db tracker/backups/before.json
  (the session runs)
  (list the 5 collections again with out_dir tracker/backups/after-db)
python tools/check_tracker.py snapshot-dir tracker/backups/after-db tracker/backups/after.json
python tools/check_tracker.py check tracker/backups/before.json tracker/backups/after.json --stage sweep
```

The same `before.json` also serves as the backup for bulk writes. Use a fresh `after-db` folder each time, so rows deleted during a session do not linger from an earlier run.

The `--stage` choices are `intake`, `sweep`, `fit`, `apply`, `outreach`, `prep`, `mailbox`, `resume`, `research` and `user` (a change the user asked for directly).

**When a check fails because of something the user did** (they typed a note, or changed a status on the tracker page during the session), tell the user. Never undo their change, and never write `yourNotes` to make a check pass.
