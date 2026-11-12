#!/usr/bin/env python3
"""English/Chinese documentation sync tool.

The Chinese documentation at the repository root is the authoritative source.
Every English page under ``en/`` is a translation of the Chinese page with the
same relative path.  This tool records the FNV-1a 64-bit hash of each Chinese
source file in ``en/_sync.json`` at translation time.  The English site reads
that manifest at page load, re-hashes the live Chinese page and shows an
"outdated translation" banner whenever the two differ.

Commands
--------
    python tools/en_sync.py status [-v]
        Report translated / stale / missing / orphan pages.

    python tools/en_sync.py check
        Same as status, but exits with code 1 when anything is stale, missing
        or orphaned (suitable for CI).

    python tools/en_sync.py verify
        Structural parity checks between every English page and its Chinese
        source (headings, code fences, table rows, link targets).

    python tools/en_sync.py update [PATH ...]
        Refresh hashes in en/_sync.json after (re)translating pages.  PATHs are
        repository-relative (``system/foo.md`` or ``en/system/foo.md``).  With
        no arguments every English page is refreshed.

The hash algorithm must stay in sync with en/index.html (fnv1a64 over UTF-8
bytes of the page text after newline normalisation).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path

# Landing pages are written by hand and intentionally deviate from the Chinese
# structure (bilingual notices), so only content pages are checked.
SITE_CHROME = {"README.md", "_404.md", "doc-template.md"}

ROOT = Path(__file__).resolve().parent.parent
EN_ROOT = ROOT / "en"
MANIFEST = EN_ROOT / "_sync.json"
SIDEBAR = "_sidebar.md"
ALGORITHM = "fnv1a64"

PRIME = 0x100000001B3
OFFSET = 0xCBF29CE484222325
MASK = 0xFFFFFFFFFFFFFFFF

HEADING_RE = re.compile(r"^(#{1,6})\s+", re.MULTILINE)
TABLE_RULE_RE = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$")
LINK_RE = re.compile(r"\]\(([^)\s]+)\)")


def read_source(path: Path) -> str:
    """Read a page as UTF-8, dropping a BOM if present."""
    return path.read_text(encoding="utf-8-sig")


def normalise(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def fnv1a64(text: str) -> str:
    value = OFFSET
    for byte in normalise(text).encode("utf-8"):
        value ^= byte
        value = (value * PRIME) & MASK
    return f"{value:016x}"


def relative_pages() -> list[str]:
    """All Chinese documentation pages (root-relative POSIX paths)."""
    pages = []
    for path in sorted(ROOT.rglob("*.md")):
        rel = path.relative_to(ROOT)
        if rel.parts[0] in {"en", ".git"} or rel.as_posix() == SIDEBAR:
            continue
        pages.append(rel.as_posix())
    return pages


def english_pages() -> list[str]:
    """All translated pages (paths relative to the repository root)."""
    pages = []
    for path in sorted(EN_ROOT.rglob("*.md")):
        rel = path.relative_to(EN_ROOT).as_posix()
        if rel == SIDEBAR:
            continue
        pages.append(rel)
    return pages


def load_manifest() -> dict:
    if not MANIFEST.exists():
        return {"algorithm": ALGORITHM, "files": {}}
    try:
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        sys.exit(f"error: cannot parse {MANIFEST}: {exc}")
    data.setdefault("files", {})
    return data


def save_manifest(data: dict) -> None:
    data["algorithm"] = ALGORITHM
    data["generated"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    MANIFEST.write_text(
        json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def to_repo_relative(raw: str) -> str:
    rel = Path(raw).as_posix().lstrip("./")
    if rel.startswith("en/"):
        rel = rel[3:]
    return rel


def command_update(args) -> int:
    data = load_manifest()
    files = dict(data.get("files", {}))
    targets = [to_repo_relative(p) for p in args.paths] or english_pages()
    today = date.today().isoformat()
    changed = 0
    for rel in targets:
        zh = ROOT / rel
        en = EN_ROOT / rel
        if not en.exists():
            print(f"skip (no English page): {rel}")
            continue
        if not zh.exists():
            print(f"skip (no Chinese source): {rel}")
            continue
        digest = fnv1a64(read_source(zh))
        previous = files.get(rel, {})
        if previous.get("hash") != digest:
            changed += 1
            synced = today
            status = "updated"
        else:
            synced = previous.get("synced", today)
            status = "unchanged"
        files[rel] = {"hash": digest, "synced": synced}
        print(f"{status}: {rel} ({digest})")
    data["files"] = files
    save_manifest(data)
    print(f"\n{len(targets)} page(s) processed, {changed} hash(es) changed.")
    return 0


def collect_state(verbose: bool) -> dict:
    data = load_manifest()
    recorded = data.get("files", {})
    zh_pages = set(relative_pages())
    en_pages = set(english_pages())

    stale, untracked, orphan, missing = [], [], [], []
    for rel in sorted(en_pages):
        zh = ROOT / rel
        entry = recorded.get(rel)
        if not zh.exists():
            orphan.append(rel)
        elif not entry:
            untracked.append(rel)
        elif fnv1a64(read_source(zh)) != entry.get("hash"):
            stale.append(rel)
    missing = sorted(zh_pages - en_pages)

    print(f"Chinese pages: {len(zh_pages)}")
    print(f"English pages: {len(en_pages)}")
    print(f"Up to date   : {len(en_pages) - len(stale) - len(untracked) - len(orphan)}")
    print(f"Stale        : {len(stale)}")
    print(f"Untracked    : {len(untracked)}")
    print(f"Orphaned     : {len(orphan)}")
    print(f"Untranslated : {len(missing)}")
    if verbose or stale:
        for rel in stale:
            entry = recorded.get(rel, {})
            print(f"  stale      {rel}  (last synced {entry.get('synced', '?')})")
    if verbose:
        for rel in untracked:
            print(f"  untracked  {rel}")
        for rel in orphan:
            print(f"  orphan     {rel}")
        for rel in missing:
            print(f"  missing    {rel}")
    return {"stale": stale, "untracked": untracked, "orphan": orphan, "missing": missing}


def structural_signature(text: str) -> dict:
    lines = normalise(text).split("\n")
    return {
        "headings": [len(m.group(1)) for m in HEADING_RE.finditer(normalise(text))],
        "fences": sum(1 for line in lines if line.lstrip().startswith("```")),
        "table_rows": sum(1 for line in lines if TABLE_RULE_RE.match(line)),
        "links": sorted(LINK_RE.findall(normalise(text))),
    }


def command_verify() -> int:
    problems = 0
    for rel in english_pages():
        if rel in SITE_CHROME:
            continue
        zh_path = ROOT / rel
        en_path = EN_ROOT / rel
        if not zh_path.exists():
            print(f"orphan: {rel}")
            problems += 1
            continue
        zh = structural_signature(read_source(zh_path))
        en = structural_signature(read_source(en_path))
        diffs = [key for key in zh if zh[key] != en[key]]
        if diffs:
            problems += 1
            print(f"mismatch: {rel} -> {', '.join(diffs)}")
            for key in diffs:
                if key in {"headings", "links"}:
                    print(f"  zh {key}: {zh[key]}")
                    print(f"  en {key}: {en[key]}")
                else:
                    print(f"  zh {key}: {zh[key]}, en {key}: {en[key]}")
    if problems:
        print(f"\n{problems} page(s) differ structurally.")
        return 1
    print(f"All {len(english_pages())} English page(s) match their Chinese source structure.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    status = sub.add_parser("status", help="show translation state")
    status.add_argument("-v", "--verbose", action="store_true")
    sub.add_parser("check", help="exit non-zero when translations lag behind Chinese")
    sub.add_parser("verify", help="check structural parity with the Chinese source")
    update = sub.add_parser("update", help="record current Chinese hashes")
    update.add_argument("paths", nargs="*")
    args = parser.parse_args()

    if args.command == "update":
        return command_update(args)
    if args.command == "verify":
        return command_verify()
    state = collect_state(verbose=getattr(args, "verbose", False) or args.command == "check")
    if args.command == "check" and (state["stale"] or state["untracked"] or state["orphan"] or state["missing"]):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
