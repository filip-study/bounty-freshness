#!/usr/bin/env python3
"""bounty-freshness — check whether listed bounty URLs still point at OPEN issues.

Usage:
  python3 bounty_freshness.py urls.txt
  echo 'https://github.com/owner/repo/issues/1' | python3 bounty_freshness.py -

Needs: gh auth (or public API, rate-limited).
Exit 0 always; prints TSV: status\\turl\\ttitle
"""
from __future__ import annotations
import json, re, subprocess, sys

ISSUE_RE = re.compile(r"https?://github\.com/([^/]+)/([^/]+)/issues/(\d+)")

def check(url: str) -> tuple[str, str, str]:
    m = ISSUE_RE.search(url.strip())
    if not m:
        return ("skip", url.strip(), "not a github issue url")
    owner, repo, num = m.group(1), m.group(2), m.group(3)
    r = subprocess.run(
        ["gh", "api", f"repos/{owner}/{repo}/issues/{num}", "--jq", "{state:.state,title:.title}"],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        return ("error", url.strip(), (r.stderr or r.stdout).strip()[:120])
    data = json.loads(r.stdout)
    return (data.get("state") or "?", url.strip(), data.get("title") or "")

def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__, file=sys.stderr); sys.exit(2)
    src = sys.argv[1]
    lines = sys.stdin.read().splitlines() if src == "-" else open(src).read().splitlines()
    urls = [ln.strip() for ln in lines if ln.strip() and not ln.strip().startswith("#")]
    print("status\turl\ttitle")
    for u in urls:
        st, url, title = check(u)
        print(f"{st}\t{url}\t{title}")

if __name__ == "__main__":
    main()
