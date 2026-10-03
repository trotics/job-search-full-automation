# Claude in Chrome setup

**What it is:** a browser extension for Google Chrome that lets Claude work in the user's own Chrome, connected to the Claude desktop app. Applying needs it because it can upload the resume file. The app's built-in browser pane cannot upload files.

## Install

1. Install Google Chrome if the user does not have it.
2. Install the Claude in Chrome extension from the Chrome Web Store, and sign in to it with the same Claude account as the desktop app.
3. Connect it to the Claude desktop app when the extension asks.

## Verify it works

Check whether tools named `mcp__claude-in-chrome__*` are available in the session. If they are, open a new tab with them and read its address. If they are not, tell the user what is missing in plain words.

## How this workspace uses it

Only the apply stage needs it. Sweeps, research and everything else work in the built-in browser. If it is not connected, applying can still fill forms in the built-in browser, but the user attaches the resume by hand. With no browser at all, applying uses a fill sheet (`apply-procedure.md`, "No browser Claude can use").

Claude in Chrome acts only on sites the user allows. Their own sign-ins stay theirs: never sign out, change settings, or act beyond the application in front of you.
