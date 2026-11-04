"""Till Payday rebuild tool. Run after editing the app.

The repo's index.html is the source. This makes the other three files from it, and refreshes the privacy lock:
  index.html            the website (privacy lock refreshed to match the edited code)
  selftest.html         the website self-test (the app on its own storage + the test runner taken from the current selftest.html)
  artifact.html         the Claude page (publish to the Till Payday artifact)
  selftest-artifact.html  the Claude self-test (publish to the Self-Test artifact)

Usage:  python3 rebuild.py <folder with index.html and selftest.html> [new version like 1.2]
Writes into <folder>/out/. With a version, it also sets APP_VERSION in the app, the self-test, and sw.js.
Why: the privacy lock (Content-Security-Policy) only lets scripts run whose exact fingerprint (sha256) is listed.
Any edit to a script changes its fingerprint, so the lock must be refreshed, or the edited app won't start.
"""
import sys, re, base64, hashlib, pathlib

src = pathlib.Path(sys.argv[1])
ver = sys.argv[2] if len(sys.argv) > 2 else None
out = src / "out"
out.mkdir(exist_ok=True)
index = (src / "index.html").read_text(encoding="utf-8")
selftest_web = (src / "selftest.html").read_text(encoding="utf-8")

SCRIPT = re.compile(r"<script>(.*?)</script>", re.S)
def lock(html):
    hashes = " ".join("'sha256-" + base64.b64encode(hashlib.sha256(m.group(1).encode("utf-8")).digest()).decode() + "'" for m in SCRIPT.finditer(html))
    new, n = re.subn(r"(script-src )[^;]*(;)", lambda m: m.group(1) + hashes + m.group(2), html, count=1)
    assert n == 1, "privacy lock not found"
    return new

def one(text, old, new):
    assert text.count(old) == 1, ("expected once", old[:60], text.count(old))
    return text.replace(old, new)

if ver:
    index = re.sub(r'const APP_VERSION = "[^"]+";', 'const APP_VERSION = "%s";' % ver, index, count=1)
    sw = (src / "sw.js").read_text(encoding="utf-8")
    sw = re.sub(r"\(version [^)]+\)", "(version %s)" % ver, sw, count=1)
    sw = re.sub(r'const CACHE = "till-payday-[^"]+";', 'const CACHE = "till-payday-%s";' % ver, sw, count=1)
    (out / "sw.js").write_text(sw, encoding="utf-8")

# The test runner is the last script in the current selftest.html
runner = SCRIPT.findall(selftest_web)[-1]
if ver: runner = re.sub(r'const VERSION = "[^"]+";', 'const VERSION = "%s";' % ver, runner, count=1)

KEY_WEB = 'const LOCAL_KEY = "till-payday-v1";'
ACCOUNT = 'if (window.claude && typeof window.claude.use === "function") {'
def selftest_from(app_html, web):
    t = one(app_html, KEY_WEB if web else 'const LOCAL_KEY = "shareable-payday-planner-v1";', 'const LOCAL_KEY = "till-payday-selftest-v1";')
    t = one(t, ACCOUNT, "if (false) {   // the self-test never uses account storage")
    t = one(t, "<title>Till Payday</title>", "<title>Till Payday Self-Test</title>")
    r = runner if web else re.sub(r"const WEBSITE = true;", "const WEBSITE = false;", runner, count=1)
    end = t.rindex("</script>") + len("</script>")
    return t[:end] + "\n<script>" + r + "</script>" + ("" if web else "\n") + t[end:]

# Website pages
index = lock(index)
(out / "index.html").write_text(index, encoding="utf-8")
(out / "selftest.html").write_text(lock(selftest_from(index, True)), encoding="utf-8")

# Claude pages: the same app without the website's head, on the Claude storage key, with website-only parts off
head_end = index.index("<title>Till Payday</title>")
body = index[head_end:]
body = one(body, "</head>\n<body>\n", "")
body = body[: body.rindex("\n</body>")] + "\n"
art = one(body, KEY_WEB, 'const LOCAL_KEY = "shareable-payday-planner-v1";')
art = one(art, "const WEB = true;", "const WEB = false;")
(out / "artifact.html").write_text(art, encoding="utf-8")
(out / "selftest-artifact.html").write_text(selftest_from(art, False), encoding="utf-8")
print("wrote", sorted(p.name for p in out.iterdir()))
