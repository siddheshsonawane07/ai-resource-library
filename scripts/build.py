#!/usr/bin/env python3
"""Validate library.csv and generate README.md from it.

    python3 scripts/build.py           validate, then write README.md
    python3 scripts/build.py --check   validate, and fail if README.md is out of date
    python3 scripts/build.py --links   request every URL and report the ones that fail
"""
import csv
import re
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIBRARY = ROOT / "skills" / "resource-library" / "library.csv"
README = ROOT / "README.md"
REPO = "siddheshsonawane07/ai-resource-library"

COLUMNS = ["name", "url", "category", "use", "stack", "good_for",
           "description", "pricing", "status", "notes", "added"]
REQUIRED = ["name", "url", "category", "use", "description", "pricing", "status", "added"]

# README section order; also the allowed values.
CATEGORIES = [
    "UI Components",
    "Design Inspiration",
    "3D, Animation & Shaders",
    "Agent Skills",
    "AI & Dev Tools",
    "GitHub Repos",
    "Learning & Articles",
    "Showcases & Portfolios",
]
USES = {
    "copy-code": "copy components or templates into the project",
    "library": "add as a dependency",
    "reference": "look at it; nothing to install",
    "install-skill": "an agent skill to install",
    "asset": "download and drop in",
    "tool": "a product you use yourself",
}
PRICING = ["open-source", "free", "freemium", "paid", "unverified"]
STATUSES = ["not-started", "exploring", "using", "bookmarked", "not-useful"]


def url_key(url):
    return re.sub(r"^https?://(www\.)?", "", url.strip().lower()).rstrip("/")


def load():
    with LIBRARY.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != COLUMNS:
            sys.exit(f"library.csv header is {reader.fieldnames}, expected {COLUMNS}")
        return list(reader)


def validate(rows):
    errors, urls, names = [], {}, {}
    for line, r in enumerate(rows, start=2):
        where = f"line {line} ({r['name'] or '?'})"
        for col in REQUIRED:
            if not r[col].strip():
                errors.append(f"{where}: {col} is empty")
        for col, allowed in (("category", CATEGORIES), ("use", USES),
                             ("pricing", PRICING), ("status", STATUSES)):
            if r[col] and r[col] not in allowed:
                errors.append(f"{where}: {col} '{r[col]}' is not one of {', '.join(allowed)}")
        if r["url"] and not re.match(r"https?://", r["url"]):
            errors.append(f"{where}: url must start with http:// or https://")
        if r["added"] and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", r["added"]):
            errors.append(f"{where}: added must be YYYY-MM-DD")
        for seen, key, label in ((urls, url_key(r["url"]), "url"),
                                 (names, r["name"].strip().lower(), "name")):
            if key in seen:
                errors.append(f"{where}: duplicate {label}, first on line {seen[key]}")
            seen.setdefault(key, line)
    return errors


def cell(text):
    return text.replace("|", "\\|").strip()


def render(rows):
    out = [
        "# AI Resource Library",
        "",
        f"{len(rows)} links for building and designing with AI coding agents: component "
        "registries, design galleries, animation and 3D libraries, agent skills and tools. "
        "Each one is tagged by what you do with it, so an agent can pick from the list "
        "instead of guessing.",
        "",
        "This file is generated from "
        "[`library.csv`](skills/resource-library/library.csv). Edit the CSV, not this page.",
        "",
        "## Use it as a Claude Code skill",
        "",
        "```bash",
        f"git clone https://github.com/{REPO}.git",
        f'ln -s "$PWD/{REPO.split("/")[1]}/skills/resource-library" ~/.claude/skills/resource-library',
        "```",
        "",
        "Then ask Claude Code to improve a site's design, or give it a link to add. "
        "[`SKILL.md`](skills/resource-library/SKILL.md) is the procedure it follows.",
        "",
        "## Reading the tables",
        "",
        "| Use | Meaning |",
        "|---|---|",
        *[f"| `{use}` | {meaning} |" for use, meaning in USES.items()],
        "",
        "Pricing is what the site said on the day the link was added; check before you rely "
        "on it. A ★ marks something the maintainer is actually using.",
        "",
        "## Contents",
        "",
    ]
    by_category = {c: [r for r in rows if r["category"] == c] for c in CATEGORIES}
    for c in CATEGORIES:
        anchor = re.sub(r"[^a-z0-9 -]", "", c.lower()).replace(" ", "-")
        out.append(f"- [{c}](#{anchor}) ({len(by_category[c])})")
    for c in CATEGORIES:
        out += ["", f"## {c}", "",
                "| Resource | What it is | Use | Pricing | Notes |",
                "|---|---|---|---|---|"]
        for r in sorted(by_category[c], key=lambda r: r["name"].lower()):
            star = "★ " if r["status"] == "using" else ""
            out.append(f"| {star}[{cell(r['name'])}]({r['url']}) | {cell(r['description'])} "
                       f"| `{r['use']}` | {r['pricing']} | {cell(r['notes'])} |")
    out += [
        "",
        "## Maintaining",
        "",
        "Add or change a row in `library.csv`, then run `python3 scripts/build.py`. It checks "
        "the row and rewrites this page. `--check` fails if this page is stale, and `--links` "
        "reports URLs that no longer respond.",
        "",
    ]
    return "\n".join(out)


def fetch(row):
    req = urllib.request.Request(row["url"], headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return None if resp.status < 400 else f"HTTP {resp.status}"
    except Exception as e:
        return str(e)


def check_links(rows):
    with ThreadPoolExecutor(16) as pool:
        failed = [(r, err) for r, err in zip(rows, pool.map(fetch, rows)) if err]
    for r, err in failed:
        print(f"{r['name']}: {r['url']}: {err}")
    print(f"{len(rows) - len(failed)} of {len(rows)} responded. "
          "A 403 usually means the site blocks scripts, not that it is gone.")


def main():
    rows = load()
    errors = validate(rows)
    if errors:
        sys.exit("\n".join(errors))
    if "--links" in sys.argv:
        check_links(rows)
        return
    readme = render(rows)
    if "--check" in sys.argv:
        if not README.exists() or README.read_text(encoding="utf-8") != readme:
            sys.exit("README.md is out of date. Run: python3 scripts/build.py")
        print(f"{len(rows)} rows valid, README.md is current")
        return
    README.write_text(readme, encoding="utf-8")
    print(f"{len(rows)} rows valid, wrote README.md")


if __name__ == "__main__":
    main()
