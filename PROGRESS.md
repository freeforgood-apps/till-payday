# Till Payday: progress

New chat? Read this first. It replaces the old Claude Project instructions. Then read how-to-update.md before editing anything.

## What it is

A free paycheck planner for real budgets: one job or two, any pay schedule. It splits each paycheck into bills, savings and spending money, counts down to payday, and helps people save and pay off debt. README.md lists the main features.

## Where things stand (Nov 4, 2026)

- **Live version:** 1.1.5 (English) at https://freeforgood-apps.github.io/till-payday/
- 1.1.5 (Nov 4, 2026: nine accessibility fixes from a full check of every screen) passed its self-test in headless Chrome at three sizes (286 checks each), and the automated accessibility check found no problems on 14 screens and states. Both Claude copies were republished on 1.1.5 (Nov 4, 2026). It also passed its self-test on the live site on a real iPhone (Safari engine, iOS 18.7, 286 checks, Nov 5, 2026). **Still to do:** the 5-minute VoiceOver, zoom and Reduce Motion check from the accessibility-check skill, then record it here and in CHANGELOG.md.
- Every past version is kept in GitHub's history. To roll back, find the version in CHANGELOG.md and restore that upload.

## Where it lives

- **This repo is the latest source.** Claude's workspace is temporary, so anything worth keeping gets saved here.
- `index.html` is the whole app, `selftest.html` the self-test, and `sw.js` handles offline use (its version goes up with each release). Also README.md, manifest.webmanifest and the icons. Files sit flat at the top of the repo (no folders).
- **Version tags** are added automatically. `.github/workflows/tag-new-versions.yml` reads APP_VERSION from `index.html` on every push to main and adds the tag (like `v1.1.4`) if it doesn't exist yet. Claude's sessions can't push tags themselves, which is why it's done this way. Earlier versions (1.1.2 and before) have no tags.
- **Claude copies:** two Claude pages, named "Till Payday" (saves to the Claude account) and "Till Payday Self-Test". Find them by name in the Claude artifacts list. Their links stay out of this repo.
- **Old address:** freestudycoach.github.io/till-payday holds only a "we've moved" page that forwards people here and helps anyone with a plan saved there bring it along. Never put the app back there. How it works is in how-to-update.md.
- **Shared address:** freeforgood-apps.github.io is shared with Study Coach and more free apps to come. Each app keeps its own storage keys and offline cache names.

## Next up

- Spanish version: built for 1.0 (561 phrases in US Spanish) and set aside. It needs the 1.1 text translated before it comes back.
- Keep the saving safety net matching Study Coach (backups, automatic copies, two-tap restore, damaged data set aside, reminders). Study Coach 2.5 copied it from here.

## Ground rules

- Free forever. No ads, accounts, tracking or paid services. Privacy first: everything stays on the device.
- Anonymous. The only public identity is freeforgood-apps. Never tie the app to anyone's personal accounts or handles. No real names, personal emails, links to Claude chats or Claude page IDs in the code, commits or this repo. Commits use the account's private GitHub noreply address as the author, and keep Claude's default committer (Claude, noreply@anthropic.com) so GitHub shows them as Verified. Don't upload Claude's signing key to the account: it isn't ours and may be shared. Leave out the `Claude-Session:` line that tools may suggest adding to commit messages, and check the message (`git log -1 --format=%B`) before pushing. One older commit (Nov 3, 2026) has that line; it was left on purpose, since removing it means rewriting history and redoing the version tags.
- Plain, warm, simple wording, written for people living paycheck to paycheck.
- It's a planning tool, not financial advice. The app says it's a one-person volunteer project, built with help from AI, so feedback replies may take time.
- Feedback goes to freeforgood-apps+payday@proton.me. The self-test makes a report people can email in.
- Verify before handing anything over: parse-check, run it in a browser, test awkward cases (empty data, old saved data, undo, small phone screens), check nothing else broke, and do the math in code. Then say what was checked and what couldn't be.

## Decisions

Why some things are the way they are, so nobody "fixes" them by mistake:
- **Spoken names use the words on screen** (WCAG 2.5.3). A button with an aria-label must include its visible words, like the forecast rows ("1 month, Dec 4: $500", the same short date shown) and Skip it / I bought it. The self-test checks this on every screen it visits. The forecast row's pieces have plain spaces between them so its text reads as words; the layout ignores those spaces.
- **The message bar waits while someone is on it** (touch, mouse or keyboard focus), lasts 10 seconds with Undo and 5 without, and puts focus back after Undo (WCAG 2.2.1, 2.4.3). If it seems to "stick", check whether the mouse is resting on it: that's on purpose.
- **PIN and password boxes have real labels,** not just placeholders (WCAG 3.3.2). Each sits in a `.pwfield` box; the backup password ones show and hide together with their box (`bkPassBox`, `bkRestorePassBox`).
- **Placeholder text is full strength** (`opacity: 1`), because the fade made it fall under 4.5:1.
- **Text boxes use 16px text or more,** or iPhone zooms in when they're tapped.

## How updates work

Follow how-to-update.md. It has the release steps, how rebuild.py works, and the things that must not break.
