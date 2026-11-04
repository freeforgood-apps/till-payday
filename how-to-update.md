# How to update Till Payday

This repo (freeforgood-apps/till-payday) is the source. `index.html` is the whole app. Everything else is made from it with `rebuild.py` (in this repo).

## Release steps
1. Get the current files from this repo.
2. Edit `index.html`. Keep the app in one file.
3. Run `python3 rebuild.py <folder> <new version>` on a copy of the files, outside the repo. It writes `out/` with:
   - `index.html`: the edited app with the privacy lock refreshed
   - `selftest.html`: the self-test, rebuilt from the edited app
   - `sw.js`: the offline cache, renamed to the new version so phones update
   - `artifact.html`: publish to the Claude page named "Till Payday"
   - `selftest-artifact.html`: publish to the Claude page named "Till Payday Self-Test"
4. Test: parse-check, run it in a browser, run the self-test, check old saved data and small screens.
5. Save `index.html`, `selftest.html` and `sw.js` to this repo, plus README.md if it changed, a new CHANGELOG.md entry, and an update to PROGRESS.md. All files sit flat at the top of the repo. They can also be uploaded by hand from a phone.
6. Run the self-test on the live site afterwards, on a real iPhone.

## Things that must not break
- **The privacy lock.** `index.html` and `selftest.html` carry a Content-Security-Policy that only lets scripts run whose exact sha256 fingerprint is listed. Any edit to a script changes its fingerprint. Always run `rebuild.py` after editing, or the app won't start.
- **Storage keys. Never rename them, or people lose their plans.** The website uses `till-payday-v1`, the Claude page `shareable-payday-planner-v1`, and the self-test `till-payday-selftest-v1`. Other keys add a suffix (`-copies`, `-pin`, `-new`, etc.).
- **The offline cache name** must start with `till-payday-`. The site shares freeforgood-apps.github.io with Study Coach and other apps, and sw.js only clears its own caches.
- **No outside requests.** Fonts are built in (Atkinson Hyperlegible, Bricolage Grotesque, DM Mono, all SIL Open Font License). Don't add Google Fonts or any CDN back. The lock would block them anyway.
- **APP_VERSION** in the app and the version in sw.js must match. rebuild.py sets both.
- **Website-only parts** (file downloads, calendar file, install card, offline) are switched by `const WEB`. The Claude page has `WEB = false` and saves to the Claude account instead.
- **Calendar event IDs** still end in `@freestudycoach.github.io` on purpose. Changing them would make re-added reminders show up twice in people's calendars.
- **Anonymous.** No real names, personal emails, links to Claude chats or Claude page IDs in this repo or its commits.

## The old address
freestudycoach.github.io/till-payday (repo freestudycoach/till-payday) holds only a "we've moved" page, `index.html` and `selftest.html`. If nothing real is saved there, it forwards straight to the new address (the old `selftest.html` forwards to the new self-test). If a plan is saved there, it asks for the PIN when one is set, then gives a backup code in the app's own `TILLPAY1:` format to restore at the new address, plus a button to delete the old copy. On both old pages the address and the "Open the new Till Payday" button point at the new app, never the self-test, because the self-test keeps its own storage and wipes it on every run (fixed Nov 3, 2026, matching the same fix on Study Coach's old page). It has its own privacy lock and loads nothing from other sites.

What changed in each version, and how it was tested, is in CHANGELOG.md.
