#!/usr/bin/env python3
"""Make the Judge Laugh in One Line — entry generator.

Writes one funny line (<=200 chars, single line) to
$MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output).
Stdlib only.
"""

import os
import sys

LINE = "I said 'just one episode' at 9 p.m. At 3 a.m. Netflix asked 'are you still watching?' like a worried parent who'd already called the police."
# NOTE: 140 chars, single line — relatable late-night binge moment, sharp
# worried-parent metaphor, twist at the end; no question-format setup.


def main() -> int:
    line = LINE
    if not line or not line.strip():
        print("error: line is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: line must be a single line", file=sys.stderr)
        return 1
    if len(line) > 200:
        print(f"error: line is {len(line)} chars, max 200", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)

    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != line:
        print("error: written entry does not match LINE", file=sys.stderr)
        return 1

    print(f"wrote {len(line)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
