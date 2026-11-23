#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? -- make.fun entry.

Writes one number, digits only, to /output/entry.txt: the honest count
of browser tabs open. One number, nothing else.
"""

import os
import sys

# The honest count: 1187 open browser tabs.
# Counted, not rounded: years of research, read-later tabs, docs,
# dashboards and half-finished articles that never got closed. Over a
# thousand, because that is what a real tab hoarder's browser looks
# like; odd and specific, because a real count is never a round number.
TABS_OPEN = 1187


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    text = str(TABS_OPEN)
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 5 characters,
    # digits only, not only white space. "1187" is 4 characters.
    assert text.isdigit() and 1 <= len(text) <= 5, text
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
