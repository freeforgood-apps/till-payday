# Till Payday: progress

New chat? Read this first. It replaces the old Claude Project instructions. Then read how-to-update.md before editing anything.

## What it is

A free paycheck planner for real budgets: one job or two, any pay schedule. It splits each paycheck into bills, savings and spending money, counts down to payday, and helps people save and pay off debt. README.md lists the main features.

## Where things stand (Nov 9, 2026)

- **Live version:** 1.1.8 (English) at https://freeforgood-apps.github.io/till-payday/
- 1.1.8 (Nov 9, 2026: the Claude copy now says Till Payday has moved to the website; the website is unchanged) and 1.1.7 (Nov 9, 2026: the red Delete button in About no longer gets squashed with its words spilling out, on small phones or with bigger text) passed their self-tests in headless Chrome at three sizes (286 checks each). **Still to do:** on a real iPhone on the live site, look at the Delete button in About and run the self-test, then record it here and in CHANGELOG.md.
- **The Claude copies are retired** (Nov 9, 2026). Both were republished one last time on 1.1.8 and get no more updates. See "Where it lives".
- 1.1.6 (Nov 5, 2026: iPhone date boxes no longer stick out of their card) passed its self-test in headless Chrome at three sizes (286 checks each). Its real-iPhone check (self-test and both date boxes) was never recorded; fold it into the 1.1.7 iPhone check.
- 1.1.5 passed its self-test on the live site on a real iPhone (Safari engine, iOS 18.7, 286 checks, Nov 5, 2026) and the VoiceOver and Reduce Motion check. At zero brightness the gray text is faint; iPhone's Increase Contrast setting brightens it (the app already supports it).
- Every past version is kept in GitHub's history. To roll back, find the version in CHANGELOG.md and restore that upload.

## Where it lives

- **This repo is the latest source.** Claude's workspace is temporary, so anything worth keeping gets saved here.
- `index.html` is the whole app, `selftest.html` the self-test, and `sw.js` handles offline use (its version goes up with each release). Also README.md, manifest.webmanifest and the icons. Files sit flat at the top of the repo (no folders).
- **Version tags** are added automatically. `.github/workflows/tag-new-versions.yml` reads APP_VERSION from `index.html` on every push to main and adds the tag (like `v1.1.4`) if it doesn't exist yet. Claude's sessions can't push tags themselves, which is why it's done this way. Earlier versions (1.1.2 and before) have no tags.
- **Claude copies (retired Nov 9, 2026):** two Claude pages, named "Till Payday" (saves to the Claude account) and "Till Payday Self-Test". Find them by name in the Claude artifacts list. Their links stay out of this repo. Both stay up on 1.1.8, which shows a "Till Payday has moved" note pointing to the website, with steps to bring a plan along by backup code. **Don't republish them on releases.** People's plans live in the app copy, so never delete it without asking. Only touch them again for a safety or data fix, using `artifact.html` and `selftest-artifact.html` from `rebuild.py`.
- **Old address:** freestudycoach.github.io/till-payday holds only a "we've moved" page that forwards people here and helps anyone with a plan saved there bring it along. Never put the app back there. How it works is in how-to-update.md.
- **Shared address:** freeforgood-apps.github.io is shared with Study Coach and more free apps to come. Each app keeps its own storage keys and offline cache names.

## Next up

- Small: on a 320px-wide screen with the biggest text, the amount box under "Spent something?" on Today cuts off its "0.00" hint (it shows "0.0"). Seen Nov 9, 2026, in headless Chrome.

- Restore checks, for the next release (found Nov 5, 2026, comparing with the shared kit in freeforgood-apps/toolkit): `readBackup()` and `sanitize()` already rebuild clean data from known fields only. Still missing: a size cap on pasted codes and backup files, and a friendly "this backup is from a newer version, update the app first" message (right now a newer backup would restore with its new parts quietly dropped).
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
- **Date boxes use `appearance: none`.** Otherwise iPhone draws them wider than their card and centers the date. The self-test checks that every box fits inside its card.
- **Everything directly inside a sheet or the calculator has `flex-shrink: 0`.** They scroll as flex columns, and without it a button with `min-height` gets squashed to 44px and its wrapped words spill out (the Delete button in About, 1.1.7).
- **The Claude copies are retired** (1.1.8), because republishing and checking them on every release cost Claude usage for little gain: the website does more (file backups, offline, Home Screen). `movedCard` shows only when `WEB` is false, so the website never shows it.

## How updates work

Follow how-to-update.md. It has the release steps, how rebuild.py works, and the things that must not break.
