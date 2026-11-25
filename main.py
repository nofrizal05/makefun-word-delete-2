#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary — make.fun entry.

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt: the single word this
entry would delete from the dictionary, and why.
"""

import os

LINE = (
    "Delete 'irregardless' \u2014 a typo that showed up so often "
    "the dictionary gave up and adopted it, and now it corrects me."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
