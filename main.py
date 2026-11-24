#!/usr/bin/env python3
"""Say What Actually Broke — make.fun entry.

Writes one line of software error copy to /output/entry.txt: the brutal
truth about a failed login, funny on a single read, naming the real failure
(the database is down, not the user's password) and what to do next.
"""

import os

ENTRY = (
    "Your password was correct. Our database was not. "
    "It's down, we're rebooting it \u2014 try logging in again "
    "in about five minutes."
)

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    # Fail loudly instead of writing an entry the gate would refuse:
    # 1-200 characters, single line, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one non-blank line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
