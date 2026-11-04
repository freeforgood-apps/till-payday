# Till Payday: progress

New chat? Read this first. It replaces the old Claude Project instructions. Then read how-to-update.md before editing anything.

## What it is

A free paycheck planner for real budgets: one job or two, any pay schedule. It splits each paycheck into bills, savings and spending money, counts down to payday, and helps people save and pay off debt. README.md lists the main features.

## Where things stand (Nov 3, 2026)

- **Live version:** 1.1.2 (English) at https://freeforgood-apps.github.io/till-payday/
- 1.1.1 passed its self-test on a real iPhone (Nov 3, 2026). 1.1.2 (Nov 3, 2026: restoring an automatic copy no longer counts as a backup, matching Study Coach 2.5) passed in headless Chrome at three sizes, and both Claude copies were republished on 1.1.2 (Nov 3, 2026). **Still to do:** run the 1.1.2 self-test on the live site on a real iPhone.
- Every past version is kept in GitHub's history. To roll back, find the version in CHANGELOG.md and restore that upload.

## Where it lives

- **This repo is the latest source.** Claude's workspace is temporary, so anything worth keeping gets saved here.
- `index.html` is the whole app, `selftest.html` the self-test, and `sw.js` handles offline use (its version goes up with each release). Also README.md, manifest.webmanifest and the icons. Files sit flat at the top of the repo (no folders).
- **Claude copies:** two Claude pages, named "Till Payday" (saves to the Claude account) and "Till Payday Self-Test". Find them by name in the Claude artifacts list. Their links stay out of this repo.
- **Old address:** freestudycoach.github.io/till-payday holds only a "we've moved" page that forwards people here and helps anyone with a plan saved there bring it along. Never put the app back there. How it works is in how-to-update.md.
- **Shared address:** freeforgood-apps.github.io is shared with Study Coach and more free apps to come. Each app keeps its own storage keys and offline cache names.

## Next up

- Spanish version: built for 1.0 (561 phrases in US Spanish) and set aside. It needs the 1.1 text translated before it comes back.
- Nothing else planned yet.
- Keep the saving safety net matching Study Coach (backups, automatic copies, two-tap restore, damaged data set aside, reminders). Study Coach 2.5 copied it from here.

## Ground rules

- Free forever. No ads, accounts, tracking or paid services. Privacy first: everything stays on the device.
- Anonymous. The only public identity is freeforgood-apps. Never tie the app to anyone's personal accounts or handles. No real names, personal emails, links to Claude chats or Claude page IDs in the code, commits or this repo. Commits use the account's private GitHub noreply address.
- Plain, warm, simple wording, written for people living paycheck to paycheck.
- It's a planning tool, not financial advice. The app says it's a one-person volunteer project, built with help from AI, so feedback replies may take time.
- Feedback goes to freeforgood-apps+payday@proton.me. The self-test makes a report people can email in.
- Verify before handing anything over: parse-check, run it in a browser, test awkward cases (empty data, old saved data, undo, small phone screens), check nothing else broke, and do the math in code. Then say what was checked and what couldn't be.

## How updates work

Follow how-to-update.md. It has the release steps, how rebuild.py works, and the things that must not break.
