# Till Payday: progress

New chat? Read this first. It replaces the old Claude Project instructions.

## Where things stand (Nov 3, 2026)

- **Live version:** 1.1.1 at https://freeforgood-apps.github.io/till-payday/
- Passed its self-test on a real iPhone (Nov 3, 2026).
- Every working version is tagged (v1.0, v1.1, v1.1.1), so any of them can be rolled back to.

## Next up

- Spanish version: on hold until the English version is settled.
- Nothing else planned yet.

## Ground rules

- Free forever. No ads, accounts, tracking or paid services.
- Privacy first. Numbers stay only in the person's own browser (saved under `till-payday-v1`). The page blocks itself from sending anything over the internet.
- Anonymous. No real names, personal emails or personal info in the code, commits or this repo.
- Plain, warm wording for people living paycheck to paycheck.
- It's a planning tool, not financial advice. It's a one-person volunteer project, built with help from AI.
- Feedback goes to freeforgood-apps+payday@proton.me.

## How updates work

1. Claude edits the files, runs the self-test in a headless browser, and saves the changes straight to GitHub. GitHub Pages updates the live site within a few minutes.
2. Every new version gets a number in `index.html` (APP_VERSION) and in `sw.js` (CACHE), a CHANGELOG.md entry, an update to this file, and a version tag.
3. Afterward, open selftest.html on the iPhone to confirm it passes there too.

## Things to know before editing

- The page has a security rule with a fingerprint (hash) of its script. Any change to the script means that hash has to be updated, or the app won't run.
- selftest.html carries its own copy of the app, so it has to be rebuilt after every change to index.html.
- Files sit flat at the top of the repo (no folders).
