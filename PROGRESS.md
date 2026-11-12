# Till Payday: progress

New chat? Read this first, then how-to-update.md before editing anything. It replaces the old Claude Project instructions. The steady brief comes first; the changing status is at the bottom, and every version's full test notes are in CHANGELOG.md.

## What it is

A free paycheck planner for real budgets: one job or two, any pay schedule. It splits each paycheck into bills, savings and spending money, counts down to payday, and helps people save and pay off debt. README.md lists the main features.

## Ground rules

- Free forever. No ads, accounts, tracking or paid services. Privacy first: everything stays on the device.
- Anonymous. The only public identity is freeforgood-apps. Never tie the app to anyone's personal accounts or handles. No real names, personal emails, links to Claude chats or Claude page IDs in the code, commits or this repo. Commits use the account's private GitHub noreply address as the author, and keep Claude's default committer (Claude, noreply@anthropic.com) so GitHub shows them as Verified. Don't upload Claude's signing key to the account: it isn't ours and may be shared. Leave out the `Claude-Session:` line that tools may suggest adding to commit messages, and check the message (`git log -1 --format=%B`) before pushing. One older commit (Nov 3, 2026) has that line; it was left on purpose, since removing it means rewriting history and redoing the version tags.
- Plain, warm, simple wording, written for people living paycheck to paycheck.
- It's a planning tool, not financial advice. The app says it's a one-person volunteer project, built with help from AI, so feedback replies may take time.
- Feedback goes to freeforgood-apps+payday@proton.me. The self-test makes a report people can email in.
- Verify before handing anything over: parse-check, run it in a browser, test awkward cases (empty data, old saved data, undo, small phone screens), check nothing else broke, and do the math in code. Then say what was checked and what couldn't be.

## Where it lives

- **This repo is the latest source.** Claude's workspace is temporary, so anything worth keeping gets saved here.
- `index.html` is the whole app, `selftest.html` the self-test, and `sw.js` handles offline use (its version goes up with each release). Also README.md, manifest.webmanifest, the icons, `SECURITY.md` (how to report a problem privately; update its "Last checked" line after each security check) and `.gitignore` (both from the toolkit's Baseline kit). Files sit flat at the top of the repo (no folders).
- **Version tags** are added automatically. `.github/workflows/tag-new-versions.yml` reads APP_VERSION from `index.html` on every push to main and adds the tag (like `v1.1.4`) if it doesn't exist yet. Claude's sessions can't push tags themselves, which is why it's done this way. Earlier versions (1.1.2 and before) have no tags.
- **Claude copies (retired Nov 9, 2026):** two Claude pages, named "Till Payday" (saves to the Claude account) and "Till Payday Self-Test". Find them by name in the Claude artifacts list. Their links stay out of this repo. Both stay up on 1.1.8, which shows a "Till Payday has moved" note pointing to the website, with steps to bring a plan along by backup code. **Don't republish them on releases.** People's plans live in the app copy, so never delete it without asking. Only touch them again for a safety or data fix, using `artifact.html` and `selftest-artifact.html` from `rebuild.py`.
- **Old address:** freestudycoach.github.io/till-payday holds only a "we've moved" page that forwards people here and helps anyone with a plan saved there bring it along. Never put the app back there. How it works is in how-to-update.md.
- **Shared address:** freeforgood-apps.github.io is shared with Study Coach and more free apps to come. Each app keeps its own storage keys and offline cache names.
- **Rolling back:** every past version is kept in GitHub's history. To roll back, find the version in CHANGELOG.md and restore that upload.

## How updates work

Follow how-to-update.md. It has the release steps, how rebuild.py works, and the things that must not break.

## Decisions

Why some things are the way they are, so nobody "fixes" them by mistake:
- **Spoken names use the words on screen** (WCAG 2.5.3). A button with an aria-label must include its visible words, like the forecast rows ("1 month, Dec 4: $500", the same short date shown) and Skip it / I bought it. The self-test checks this on every screen it visits. The forecast row's pieces have plain spaces between them so its text reads as words; the layout ignores those spaces.
- **The message bar waits while someone is on it** (touch, mouse or keyboard focus), lasts 10 seconds with Undo and 5 without, and puts focus back after Undo (WCAG 2.2.1, 2.4.3). If it seems to "stick", check whether the mouse is resting on it: that's on purpose.
- **PIN, password and backup code boxes have real labels,** not just placeholders (WCAG 3.3.2). Each sits in a `.pwfield` box; the backup password ones show and hide together with their box (`bkPassBox`, `bkRestorePassBox`). The backup code box (`bkPaste`, 1.1.13) has no placeholder or aria-label, so VoiceOver reads its label, "Or paste a backup code". The self-test checks it after a code is pasted.
- **Damaged saved numbers open on Today, with their card at the top** (1.1.13). The example numbers show too (nothing readable was loaded), so `damagedCard` sits above `setupCard` in the page, or it lands just below the bottom of the screen. The app opens on Today whenever `newer` or `damaged` is set, and goes back to the last tab used once that's sorted.
- **Placeholder text is full strength** (`opacity: 1`), because the fade made it fall under 4.5:1.
- **Text boxes use 16px text or more,** or iPhone zooms in when they're tapped.
- **Date boxes use `appearance: none`.** Otherwise iPhone draws them wider than their card and centers the date. The self-test checks that every box fits inside its card.
- **Everything directly inside a sheet or the calculator has `flex-shrink: 0`.** They scroll as flex columns, and without it a button with `min-height` gets squashed to 44px and its wrapped words spill out (the Delete button in About, 1.1.7).
- **Restore turns away backups from a newer version** (1.1.10) instead of trimming them, because trimming would quietly lose whatever the newer version added. "Newer" means a plan `v` above `DATA_V`, a backup `format` above `BK_FORMAT`, or a password lock `v` above 1. Older backups, including ones from before backups had a wrapper, still restore; the self-test checks one.
- **The 5 MB restore cap** (`BK_MAX`, 1.1.10) matches the shared kit and the file limit Till Payday already had. A plan with every list full and the longest allowed text makes a password backup code of about 860 KB, so no real backup comes close.
- **The "Spent something?" boxes always stack** (1.1.12): the amount on its own line, then "What for?" with a real label ("Optional" under it, like "What is it?" on the Afford it? tab), then the quick labels. 1.1.11 stacked them only at the biggest text and 360px or narrower, so the amount's "0.00" hint fits (it needs about 68px at normal text and 85px at the biggest); 1.1.12 stacks them everywhere so "What for?" can keep a label you can see (WCAG 3.3.2). The self-test measures the hint at all three text sizes and checks the label.
- **A plan saved by a newer version is shown but never saved over** (1.1.12), the same idea as restore turning away newer backups (1.1.10). "Newer" means a plan `v` above `DATA_V`. It applies when the app opens, when another tab saves, and when bringing back an automatic copy (which is turned away on the first tap). While held, the header shows "Not saving until Till Payday updates" on every tab instead of the backup line, the app opens on Today where the update card is, and Update now reloads the page (the offline helper asks the network first). Restoring a backup over a held plan is allowed (two taps), and its Undo writes the newer plan back exactly as it was saved. A backup made while held holds only what this version understands. The retired Claude copies' account saving isn't covered; they stay on 1.1.8.
- **The Claude copies are retired** (1.1.8), because republishing and checking them on every release cost Claude usage for little gain: the website does more (file backups, offline, Home Screen). `movedCard` shows only when `WEB` is false, so the website never shows it.
- **README.md follows the toolkit's README outline** (`templates/README-outline.md`, Nov 12, 2026), so it has the same sections in the same order as Study Coach's. Every line in it comes from the app's own words or CHANGELOG.md, so when the app's wording changes, change the README to match. **Tested on** lists 1.1.8 and later; older results stay in CHANGELOG.md, where they were first written down.

## Where things stand (Nov 10, 2026)

- **Live version:** 1.1.13 (English) at https://freeforgood-apps.github.io/till-payday/
- **Tested:** 1.1.13 passed the toolkit's release check and the separate headless load-path check (80 checks), and its self-test passed on the live site on a real iPhone in a Safari tab (Safari engine, iOS 18.7, 355 checks, Nov 10, 2026). CHANGELOG.md has the full "Tested:" notes for this and every earlier version.
- **Last VoiceOver and Reduce Motion check on a real iPhone:** 1.1.5 (Nov 5, 2026). At zero brightness the gray text is faint; iPhone's Increase Contrast setting brightens it (the app already supports it).
- **Known:** the iPhone self-test says Safari hasn't promised to keep the data, which iPhone often doesn't; backup codes cover that.

## Next up

- The self-test can't reload itself, so the load path (opening the app with a newer plan or damaged data saved, and which tab it opens on) is checked by a separate headless run at release time, not on the phone. The other-tab and copy paths share the same code and are in the self-test.
- Spanish version: built for 1.0 (561 phrases in US Spanish) and set aside. It needs the 1.1 text translated before it comes back.
- Keep the saving safety net matching Study Coach (backups, automatic copies, two-tap restore, damaged data set aside, reminders). Study Coach 2.5 copied it from here.
