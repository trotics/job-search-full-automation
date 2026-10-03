# Python setup

**What it is:** Python is a free program that runs the small scripts in `tools/`. They check Claude's work on the tracker and the resume, and build the resume PDF. Every stage that writes uses them.

## Check whether it is installed

Run `python --version`. On a Mac try `python3 --version`; on some Windows computers `py --version`. Use whichever works for every later command, and save it in `my-setup.md`.

## Install it (only if none of those work)

Tell the user in plain words:

- **Windows:** download Python 3 from python.org. In the installer, tick "Add python.exe to PATH" before clicking Install.
- **Mac:** download Python 3 from python.org and run the installer.

Then check again. The user may also continue without Python for now. Without it, stages cannot finish their checks, and you must say so whenever that happens.

## Install the two add-ons

```
python -m pip install -r requirements.txt
```

This installs openpyxl (reads the spreadsheet) and reportlab (builds the resume PDF).

## Verify it works

```
python tests/run_checker_selftest.py
```

Only the last line matters: it should say `SELF-TEST: ALL CAUGHT`. The lines above it that say FAIL are the test catching mistakes it planted on purpose; tell the user that so they are not alarmed. If the last line says anything else, tell them, and do not go further until it is understood.

## When a script cannot run

If Python or an add-on is missing, say so plainly and offer to install it. Never skip a check silently: a stage whose check could not run is not done.
