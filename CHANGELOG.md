# Till Payday: changelog

## 1.1.2 (Nov 3, 2026)
- Bringing back an automatic copy no longer counts as a backup. The copy is still only on this device, so it keeps its own "last backed up" date and the backup reminders keep counting. Restoring a real backup (file or code) still counts, as before. This matches Study Coach 2.5.
- The self-test now checks automatic copies: they show in the backup sheet, bringing one back takes two taps, it restores the right plan, it doesn't count as a backup, and a real backup still does. It caught both bugs planted on purpose.
- Tested: the self-test passed in headless Chrome at phone size, small phone size in dark mode and desktop size (279 checks each). Both Claude copies were republished. On the live site, the self-test passed on a real iPhone (Safari engine, iOS 18.7, 279 checks), including the privacy lock and offline use.

## 1.1.1 (Nov 3, 2026)
- Moved to its new home at freeforgood-apps.github.io/till-payday, with the new GitHub link.
- New feedback address: freeforgood-apps+payday@proton.me.
- Self-test fix: on the 4th of any month, the "15th and last day" check used to fail falsely. The test now sets the second payday first. The app itself was fine.
- Tested: the self-test passed on 94 dates across 7 time zones (every day of Nov and Dec 2026 and Feb 2027, plus daylight-saving changeovers), and at 320px and 390px widths. The About screen was checked at 320px in dark mode. The two Claude copies were republished; their self-test passes everything except the privacy-lock check, which can only pass inside Claude. On the live site, the self-test passed on a real iPhone (Safari engine, iOS 18.7, 265 checks), including the privacy lock and offline use.

## 1.1 (Nov 2, 2026)
New:
- Where it went: spending by label over your last 1, 3 or 6 paychecks.
- Debt payoff: each debt pays its own amount; a what-if extra goes to the highest rate first.
- Calendar reminders: repeating events; the 29th and 30th fall back to the last day of the month, like the app does.
- Prices in hours of work, count my cash, no-spend days, and goal quick picks.
- A one-time "What's new" card for people who already had a plan.
- An Android install button.

Saving: every save is read back to check it; there's a daily copy from each of the last 3 days; damaged data is set aside instead of saved over; tabs stay in sync; and the app asks the browser to keep its data.

Privacy and security:
- The privacy lock: the page blocks itself from sending anything over the internet.
- Built-in fonts, so nothing loads from other sites.
- Delete everything.
- Password backups (PBKDF2-SHA256, 250,000 rounds, AES-256-GCM).
- PIN lock (a privacy screen with a salted hash; it doesn't encrypt the numbers).

Tested: 465 automated checks. The self-test (265 checks) passed across 10 time zones and dates, plus once on a real iPhone (Safari engine, iOS 18.7). It caught 10 bugs planted on purpose. Those test suites lived in a temporary workspace and weren't kept; the self-test is the lasting check.

## 1.0 (Nov 2, 2026)
- First public version.
