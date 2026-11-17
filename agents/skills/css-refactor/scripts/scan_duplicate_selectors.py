#!/usr/bin/env python3
"""Read-only CSS audit: detect repeated selector blocks under matching at-rule scopes.

Usage: python scan_duplicate_selectors.py path/to/file.css [another.css ...]
False positives are possible (intentional fallbacks, legacy overrides); investigate
before changing code. This does not rewrite or lint CSS.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
from pathlib import Path
import re
import sys


def iter_blocks(css: str):
    """Yield (selector, parent-scope, line) without needing third-party CSS parsers."""
    stack = []  # (kind, name)
    start, i, n = 0, 0, len(css)
    while i < n:
        c = css[i]
        if c == '/' and i+1 < n and css[i+1] == '*':
            close = css.find('*/', i+2)
            i = close+2 if close != -1 else n
            continue
        if c in "'\"":
            q = c
            i += 1
            while i < n:
                if css[i] == '\\':
                    i += 2
                elif css[i] == q:
                    i += 1
                    break
                else:
                    i += 1
            continue
        if c == '{':
            raw = css[start:i]
            prelude = re.sub(r'/\*.*?\*/', '', raw, flags=re.DOTALL)
            prelude = ' '.join(prelude.split())
            if prelude.startswith('@'):
                stack.append(('at', prelude))
            else:
                parents = tuple(name for _, name in stack)
                # Ignore rules within keyframes; they're animation steps, not components.
                if prelude and not any('@keyframes' in name or '@-webkit-keyframes' in name for name in parents):
                    line = css.count('\n', 0, start + len(raw) - len(raw.lstrip())) + 1
                    yield prelude, parents, line
                stack.append(('selector', prelude))
            start = i+1
        elif c == '}':
            if stack:
                stack.pop()
            start = i+1
        elif c == ';':
            start = i+1
        i += 1


def duplicates(path: Path):
    css = path.read_text(encoding='utf-8-sig')
    seen = defaultdict(list)
    for selector, scope, line in iter_blocks(css):
        seen[(selector, scope)].append(line)
    return [(selector, scope, lines) for (selector, scope), lines in seen.items() if len(lines) > 1]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('files', nargs='+', type=Path)
    args = p.parse_args()
    errors = 0
    reports = 0
    for path in args.files:
        try:
            matches = duplicates(path)
        except OSError as ex:
            print(f'{path}: could not read: {ex}', file=sys.stderr)
            errors += 1
            continue
        for selector, scope, lines in matches:
            chain = ' > '.join(scope) if scope else 'root'
            print(f'{path}:{",".join(map(str, lines))}  {selector}  [scope: {chain}]')
            reports += 1
    if not errors and not reports:
        print('No identical selector blocks repeated in the same scope.')
    elif reports:
        print(f'{reports} repeat(s) need review; intentional repeats may be valid.')
    return 2 if errors else (1 if reports else 0)

if __name__ == '__main__':
    raise SystemExit(main())
