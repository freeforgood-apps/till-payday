# Till Payday: changelog

## 1.1.4 (Nov 4, 2026)
- Fixed: after opening the self-test (for example from About in the Home Screen app), Till Payday could show the self-test instead of your plan when opened without internet. Now only the app itself is saved for offline use, and updating to 1.1.4 clears out the wrong copy. Your numbers were never affected.
- iPhone and iPad: the Home Screen tips now explain that the Home Screen app doesn't see what you saved in Safari, and how to bring your plan along with a backup code. This is on the "Make it an app" card, the backup reminder and in About.
- Accessibility: VoiceOver now reads the savings goal button by the words on it (goal name, percent and progress) instead of a different label (WCAG 2.5.3).
- Tidied up: removed leftover offline code for Google Fonts, which the app hasn't loaded since its fonts were built in.
- The self-test checks that the saved offline copy is the app and not the self-test. It caught the old behavior when that was put back on purpose.
- Version tags (like v1.1.4) are now added on GitHub automatically when a new version goes live. 1.1.3 was the first.
- Tested: the self-test passed in headless Chrome at phone size, small phone size in dark mode and desktop size (280 checks each), including the privacy lock. Offline in headless Chrome: after opening the self-test, the app still opened offline, and a phone that already had the wrong copy from 1.1.3 got the right one after updating. An automated accessibility check (axe-core 4.14 at four sizes in light and dark mode, plus About open) found no problems, and the goal button's spoken name now matches its words. The security release check found nothing new. Both Claude copies were republished. Still to do: run the self-test on the live site on a real iPhone.

## 1.1.3 (Nov 4, 2026)
- Accessibility: easier-to-read text on the teal payday strip. In dark mode, the smaller text ("Next payday", "in 9 days", the day count) is a touch darker. The pace chip ("On track", "Doing great") has a lighter tint in both themes, so its words stand out more. Everything on the strip now meets the WCAG AA contrast minimum of 4.5:1: dark-mode small text went from 4.50 to 4.63, and the chip went from 4.14 to 4.69 in light mode and from 5.54 to 6.18 in dark mode.
- Tested: the self-test passed in headless Chrome at phone size, small phone size in dark mode and desktop size (279 checks each), including the privacy lock. An automated accessibility check (axe-core 4.14 at four sizes in light and dark mode) found no contrast problems left, and side-by-side screenshots show the same look. Both Claude copies were republished. On the live site, the self-test passed on a real iPhone (Safari engine, iOS 18.7, 279 checks), including the privacy lock and offline use.

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
