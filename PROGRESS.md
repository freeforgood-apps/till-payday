# Till Payday: progress

New chat? Read this first. It replaces the old Claude Project instructions. Then read how-to-update.md before editing anything.

## What it is

A free paycheck planner for real budgets: one job or two, any pay schedule. It splits each paycheck into bills, savings and spending money, counts down to payday, and helps people save and pay off debt. README.md lists the main features.

## Where things stand (Nov 10, 2026)

- **Live version:** 1.1.11 (English) at https://freeforgood-apps.github.io/till-payday/
- 1.1.11 (Nov 10, 2026: on Today, the "Spent something?" amount box gets its own line at the biggest text and on small phones, so its "0.00" hint isn't cut off; the self-test now checks the hint at all three text sizes) passed the toolkit's release check: versions agree, privacy lock up to date, self-test in headless Chrome at three sizes (332 checks each), accessibility checker clean at 4 sizes in light and dark, no security pattern leads. Three planted versions of the old layout were each caught. **Still to do:** the self-test on the live site on a real iPhone.
- 1.1.10 (Nov 10, 2026: the restore checks. A pasted code over 5 MB is turned away, like files already were, and a backup from a newer version asks to update first instead of restoring with its new parts dropped) passed the toolkit's release check: versions agree, privacy lock up to date, self-test in headless Chrome at three sizes (326 checks each), accessibility checker clean at 4 sizes in light and dark, no security pattern leads. Seven planted bugs were each caught. On the live site on a real iPhone (Safari engine, iOS 18.7, Nov 10, 2026), its self-test passed in a Safari tab (326 checks). It said Safari hasn't promised to keep the data, which iPhone often doesn't; backup codes cover that.
- 1.1.9 (Nov 10, 2026: added SECURITY.md and .gitignore from the Baseline kit; the app itself is unchanged) passed the toolkit's release check: versions agree, privacy lock up to date, self-test in headless Chrome at three sizes (286 checks each), accessibility checker clean at 4 sizes in light and dark, no security pattern leads. On the live site on a real iPhone (Safari engine, iOS 18.7, Nov 10, 2026), its self-test passed in a Safari tab (286 checks). It said Safari hasn't promised to keep the data, which iPhone often doesn't; backup codes cover that.
- 1.1.8 (Nov 9, 2026: the Claude copy now says Till Payday has moved to the website; the website is unchanged) and 1.1.7 (Nov 9, 2026: the red Delete button in About no longer gets squashed with its words spilling out, on small phones or with bigger text) passed their self-tests in headless Chrome at three sizes (286 checks each). On the live site on a real iPhone (Safari engine, iOS 18.7, Nov 9, 2026), 1.1.8's self-test passed in a Safari tab and from the Home Screen app (286 checks each), and the red Delete button in About looked right. Both reports said Safari hasn't promised to keep the data, which iPhone often doesn't; backup codes cover that.
- **The Claude copies are retired** (Nov 9, 2026). Both were republished one last time on 1.1.8 and get no more updates. See "Where it lives".
- 1.1.6 (Nov 5, 2026: iPhone date boxes no longer stick out of their card) passed its self-test in headless Chrome at three sizes (286 checks each). Its real-iPhone check is covered by 1.1.8's iPhone self-test (Nov 9, 2026), whose check that every box fits inside its card passed.
- 1.1.5 passed its self-test on the live site on a real iPhone (Safari engine, iOS 18.7, 286 checks, Nov 5, 2026) and the VoiceOver and Reduce Motion check. At zero brightness the gray text is faint; iPhone's Increase Contrast setting brightens it (the app already supports it).
- Every past version is kept in GitHub's history. To roll back, find the version in CHANGELOG.md and restore that upload.

## Where it lives

- **This repo is the latest source.** Claude's workspace is temporary, so anything worth keeping gets saved here.
- `index.html` is the whole app, `selftest.html` the self-test, and `sw.js` handles offline use (its version goes up with each release). Also README.md, manifest.webmanifest, the icons, `SECURITY.md` (how to report a problem privately; update its "Last checked" line after each security check) and `.gitignore` (both from the toolkit's Baseline kit). Files sit flat at the top of the repo (no folders).
- **Version tags** are added automatically. `.github/workflows/tag-new-versions.yml` reads APP_VERSION from `index.html` on every push to main and adds the tag (like `v1.1.4`) if it doesn't exist yet. Claude's sessions can't push tags themselves, which is why it's done this way. Earlier versions (1.1.2 and before) have no tags.
- **Claude copies (retired Nov 9, 2026):** two Claude pages, named "Till Payday" (saves to the Claude account) and "Till Payday Self-Test". Find them by name in the Claude artifacts list. Their links stay out of this repo. Both stay up on 1.1.8, which shows a "Till Payday has moved" note pointing to the website, with steps to bring a plan along by backup code. **Don't republish them on releases.** People's plans live in the app copy, so never delete it without asking. Only touch them again for a safety or data fix, using `artifact.html` and `selftest-artifact.html` from `rebuild.py`.
- **Old address:** freestudycoach.github.io/till-payday holds only a "we've moved" page that forwards people here and helps anyone with a plan saved there bring it along. Never put the app back there. How it works is in how-to-update.md.
- **Shared address:** freeforgood-apps.github.io is shared with Study Coach and more free apps to come. Each app keeps its own storage keys and offline cache names.

## Next up

- Before the plan's data version (`DATA_V`) ever goes past 5: an older copy of the app (a tab left open, or after rolling back a release) still loads newer saved data and automatic copies, and would trim them to its own shape on its next save. Restoring already refuses newer backups (1.1.10). Loading saved data, the other-tab update and bringing back a copy should do the same, keeping the newer data untouched and asking to update. Seen Nov 10, 2026, while adding the restore checks.
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
- **Restore turns away backups from a newer version** (1.1.10) instead of trimming them, because trimming would quietly lose whatever the newer version added. "Newer" means a plan `v` above `DATA_V`, a backup `format` above `BK_FORMAT`, or a password lock `v` above 1. Older backups, including ones from before backups had a wrapper, still restore; the self-test checks one.
- **The 5 MB restore cap** (`BK_MAX`, 1.1.10) matches the shared kit and the file limit Till Payday already had. A plan with every list full and the longest allowed text makes a password backup code of about 860 KB, so no real backup comes close.
- **The "Spent something?" boxes stack at the biggest text and on screens 360px or narrower** (1.1.11), so the amount's "0.00" hint fits (it needs about 68px at normal text and 85px at the biggest; side by side, a 320px screen gives it 58px). The 360px edge matches the app's other small-phone rules. The self-test measures the hint at all three text sizes.
- **The Claude copies are retired** (1.1.8), because republishing and checking them on every release cost Claude usage for little gain: the website does more (file backups, offline, Home Screen). `movedCard` shows only when `WEB` is false, so the website never shows it.

## How updates work

Follow how-to-update.md. It has the release steps, how rebuild.py works, and the things that must not break.
