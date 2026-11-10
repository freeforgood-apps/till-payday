# Till Payday: changelog

## 1.1.12 (Nov 10, 2026)
- Accessibility: on Today, the "What for?" box under "Spent something?" now has its own label you can see, "What for?" (marked Optional), so it doesn't disappear once you start typing, and VoiceOver reads it with the same words. The box now sits on its own line under the amount, with the quick labels (Food, Gas or bus…) right below it.
- Safer saving: if your plan was saved by a newer version of Till Payday (for example a tab left open while the app updated), an older copy no longer trims it to its own shape. It shows your numbers with a card saying to update, stops saving until you do, and has an Update now button. The note at the top says "Not saving until Till Payday updates" on every tab. This works the same when the app opens, when another tab saves, and when you bring back an automatic copy, which now says to update first, like restoring a newer backup already did. If you restore a backup over that newer plan, Undo puts it back exactly as it was. Your plan isn't affected.
- The self-test now checks the "What for?" label, a newer version saving in another tab, restoring over it and Undo, and a newer automatic copy.
- Tested: the toolkit's release check passed every line: versions agree, the privacy lock is up to date on both pages, the self-test passed in headless Chrome at three sizes (354 checks each, up from 332), the accessibility checker found nothing at 4 sizes in light and dark mode, and the security patterns found nothing since 1.1.11. The accessibility checker also passed at the same sizes on a test copy that opens with a newer plan saved, so the update card was showing. A separate headless Chrome check (21 checks) opened the app with a plan from a newer version, this version, an older version and damaged data: the newer one showed the card, never saved over it after an edit or a reload, kept today's automatic copy exactly as saved, turned that copy away, reloaded on Update now, and cleared on Delete everything; the others loaded and saved as before. Seven bugs planted on purpose (another tab, the copy check, Undo, the label, saving, loading and the note at the top) were each caught. Code put into the What for? box and into a newer plan's names showed as plain text and never ran. Screenshots at 320px dark, 390px light, 390px at the biggest text and 768px were checked before and after. On the live site on a real iPhone (Safari engine, iOS 18.7, Nov 10, 2026), the self-test passed in a Safari tab (354 checks).

## 1.1.11 (Nov 10, 2026)
- Fixed: on Today, the amount box under "Spent something?" cut off its "0.00" hint on small phones at every text size, and on some phones at the biggest text size. Now, at the biggest text size and on small phones, the amount gets its own full-width line with "What for?" below it, like other boxes already do there. Your plan isn't affected.
- The self-test now checks that the whole "0.00" hint fits at all three text sizes.
- Tested: the toolkit's release check passed every line: versions agree, the privacy lock is up to date on both pages, the self-test passed in headless Chrome at three sizes (332 checks each, up from 326), the accessibility checker found nothing at 4 sizes in light and dark mode, and the security patterns found nothing since 1.1.10. The hint was measured at four screen widths and all three text sizes: before the fix it was cut off in 4 of 12, after it in none, and it also fits right at the small-phone edge (360 to 362px wide). Three versions of the old layout, planted on purpose, were each caught by the self-test at the screen sizes where they cut the hint off. Screenshots at small phone size in both themes looked right, and the amount box still comes before "What for?" for VoiceOver and the keyboard. On the live site on a real iPhone (Safari engine, iOS 18.7, Nov 10, 2026), the self-test passed in a Safari tab (332 checks).

## 1.1.10 (Nov 10, 2026)
- Safer restoring: if a backup was made by a newer version of Till Payday, it now says so and asks you to update first (close the app and open it again while online). Before, it would have restored without the parts this version doesn't know about. Nothing changes until you restore again.
- Safer restoring: a pasted backup code over 5 MB is turned away, the same limit backup files already had. The biggest real plan makes a code under 1 MB.
- Older backups restore the same as before. Your plan isn't affected.
- The self-test now checks all of this: codes and files that are too big, backups (plain and with a password) from a newer version, a normal backup file, and a backup from before 1.1.
- Tested: the toolkit's release check passed every line: versions agree, the privacy lock is up to date on both pages, the self-test passed in headless Chrome at three sizes (326 checks each, up from 286), the accessibility checker found nothing at 4 sizes in light and dark mode, and the security patterns found nothing since 1.1.9. Seven bugs planted on purpose in the new checks were each caught by the self-test. A plan with every list full and the longest allowed text makes a password backup code of 860 KB, and it still restores. The update message fits a 320px screen at the biggest text size in light and dark mode, and it's read aloud like the other messages. The old address's moving page makes the same kind of backup code that the self-test restores. On the live site on a real iPhone (Safari engine, iOS 18.7, Nov 10, 2026), the self-test passed in a Safari tab (326 checks).

## 1.1.9 (Nov 10, 2026)
- Security: added a SECURITY.md (how to report a problem privately) and a .gitignore, from the shared Baseline kit.
- Nothing else changed. Your plan isn't affected.
- Tested: the toolkit's release check passed every line: versions agree, the privacy lock is up to date on both pages, the self-test passed in headless Chrome at three sizes (286 checks each), the accessibility checker found nothing at 4 sizes in light and dark mode, and the security patterns found nothing since 1.1.8. On the live site on a real iPhone (Safari engine, iOS 18.7), the self-test passed in a Safari tab (286 checks).

## 1.1.8 (Nov 9, 2026)
- Claude copy only: the Till Payday page inside Claude now says Till Payday has moved to the website. It explains how to bring your plan along with a backup code, with a button that opens the backup code. This is the last update to the Claude copies, so the website is the one to use from now on. Plans saved in the Claude copy stay there and keep working.
- The website looks and works the same as 1.1.7.
- Tested: the website self-test passed in headless Chrome at phone size, small phone size in dark mode and desktop size (286 checks each), including the privacy lock. The Claude self-test passed 279 of 280 checks at the same sizes, run outside Claude: the one miss is the privacy lock that only Claude's own page adds, the same as the 1.1.6 Claude copy run the same way. In the Claude copy, a browser check (8 of 8) showed the moving note on Today, its link to the website, and its button opening the backup code. A plan made there (with a made-up amount) restored exactly on the website, which doesn't show the note. The note fits a small phone at the biggest text size. An automated accessibility check (axe-core 4.14 at four sizes in light and dark mode) found no problems on the website or the Claude copy. The security scan found only the new link to the website, which is fine. Both Claude copies were republished for the last time and match the tested build exactly. On the live site, the self-test passed on a real iPhone (Safari engine, iOS 18.7, 286 checks, Nov 9, 2026), both in Safari and from the Home Screen, and the red Delete button in About looked right.

## 1.1.7 (Nov 9, 2026)
- Fixed: in About, the red "Delete everything from this device" button could get squashed, so its words spilled out past the bottom of the button. This happened on small phones and with bigger text. The button now grows to fit its words. The same fix stops the Back up buttons getting squashed at the biggest text size. Your numbers aren't affected.
- Tested: the self-test passed in headless Chrome at phone size, small phone size in dark mode and desktop size (286 checks each), including the privacy lock. A browser check opened every sheet and the calculator at three screen sizes, three text sizes and both themes (18 runs): before the fix, the Delete button's words spilled out in 8 runs; after it, in none. Comparing the height of every item in every sheet before and after, only the squashed buttons changed. An automated accessibility check (axe-core 4.14 at four sizes in light and dark mode) found no new problems on the main screen or with the About and Back up sheets open, and the security scan of the changes found nothing. Both Claude copies were republished. The real iPhone check was done on 1.1.8, which has the same website (see above).

## 1.1.6 (Nov 5, 2026)
- Fixed: on iPhone, the "Your last payday" and "Last payday" date boxes stuck out past their card and showed the date centered. They now match the other boxes, with the same width and the date on the left. Tapping still opens the date picker.
- The self-test now checks, on every screen it visits, that every box fits inside its card. It caught this date-box problem when it was planted on purpose.
- Tested: the self-test passed in headless Chrome at phone size, small phone size in dark mode and desktop size (286 checks each). With the date-box problem planted on purpose, the new check failed on both date boxes. An automated accessibility check (axe-core 4.14 at four sizes in light and dark mode) found no problems, and the security scan of the changes found nothing. Both Claude copies were republished. The fix is for iPhone, which headless Chrome can't show. On a real iPhone, the 1.1.8 self-test passed (Nov 9, 2026), including its check that every box fits inside its card.

## 1.1.5 (Nov 4, 2026)
Fixes from a full accessibility check of every screen (WCAG 2.2 AA). Your numbers aren't affected.
- Accessibility: the green "Ready", "Doable" and "Easy one" chips on Afford it?, and the extra-paycheck chip on Plan, are a touch darker green in light mode, so their words are easier to read. Contrast went from 4.38 to 4.61 (WCAG 1.4.3). They look the same.
- Accessibility: the forecast rows on Savings and the Skip it / I bought it buttons on Afford it? are now read aloud with the words on screen, so Voice Control and VoiceOver match what you see (WCAG 2.5.3). A forecast row that reaches your goal now reads "hits goal" clearly.
- Accessibility: the PIN boxes and the backup password boxes have labels above them, so you can still tell which box is which once you start typing (WCAG 3.3.2).
- Accessibility: the hint text inside boxes (like "0" and "Shoes") is easier to read. Contrast went from 3.6 to 5.48 in light mode and from 4.24 to 5.77 in dark mode (WCAG 1.4.3).
- Accessibility: the message bar at the bottom waits while you're on it (touching it, hovering over it, or with keyboard focus on Undo), and stays a bit longer: 10 seconds with Undo (was 6.5) and 5 without (was 3). After Undo, focus stays in the app instead of jumping to the top of the page (WCAG 2.2.1, 2.4.3).
- Accessibility: iPhone no longer zooms in when you tap the box to paste a backup code. Its text is now 16px.
- Accessibility: the Undo button is a full 44 points wide, so it's easier to tap.
- Accessibility: with a keyboard, "Choose a backup file" now shows a focus ring (WCAG 2.4.7).
- Accessibility: with Reduce Motion on, tapping a forecast row jumps there instead of scrolling smoothly.
- The self-test now checks, on every screen it visits, that buttons are read by the words on them. It also checks that the PIN and password boxes have labels you can see, and that focus stays in the app after Undo. It caught all five bugs planted on purpose.
- Tested: the self-test passed in headless Chrome at phone size, small phone size in dark mode and desktop size (286 checks each), including the privacy lock and the offline copy check. An automated accessibility check (axe-core 4.14 at four sizes in light and dark mode) found no problems on 14 screens and states: every tab, the calculator, the Backup, About and PIN sheets, the lock screen and extra-large text. Browser checks of each fix passed (22 of 22), including the message bar's timing and focus, contrast measured from the real colors, and opening offline. Backups made in 1.1.4, plain and with a password, restored exactly in 1.1.5. The security release check found nothing new. Both Claude copies were republished. On the live site, the self-test passed on a real iPhone (Safari engine, iOS 18.7, 286 checks, Nov 5, 2026), including the privacy lock, offline use, password backups and the PIN lock. On a real iPhone (Nov 5, 2026), VoiceOver outlined and read each item and Reduce Motion worked. Two things came up: gray text is faint at zero brightness (iPhone's Increase Contrast setting brightens it), and the date boxes stuck out of their card (fixed in 1.1.6).

## 1.1.4 (Nov 4, 2026)
- Fixed: after opening the self-test (for example from About in the Home Screen app), Till Payday could show the self-test instead of your plan when opened without internet. Now only the app itself is saved for offline use, and updating to 1.1.4 clears out the wrong copy. Your numbers were never affected.
- iPhone and iPad: the Home Screen tips now explain that the Home Screen app doesn't see what you saved in Safari, and how to bring your plan along with a backup code. This is on the "Make it an app" card, the backup reminder and in About.
- Accessibility: VoiceOver now reads the savings goal button by the words on it (goal name, percent and progress) instead of a different label (WCAG 2.5.3).
- Tidied up: removed leftover offline code for Google Fonts, which the app hasn't loaded since its fonts were built in.
- The self-test checks that the saved offline copy is the app and not the self-test. It caught the old behavior when that was put back on purpose.
- Version tags (like v1.1.4) are now added on GitHub automatically when a new version goes live. 1.1.3 was the first.
- Tested: the self-test passed in headless Chrome at phone size, small phone size in dark mode and desktop size (280 checks each), including the privacy lock. Offline in headless Chrome: after opening the self-test, the app still opened offline, and a phone that already had the wrong copy from 1.1.3 got the right one after updating. An automated accessibility check (axe-core 4.14 at four sizes in light and dark mode, plus About open) found no problems, and the goal button's spoken name now matches its words. The security release check found nothing new. Both Claude copies were republished. On the live site, the self-test passed on a real iPhone (Safari engine, iOS 18.7, 280 checks), including the privacy lock, offline use and the new offline copy check.

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
