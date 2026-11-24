"""Absurd Micro-Startup Pitch-Off.

Writes one sentence -- a pitch for a brokerage where lazy AI agents
sell their unused context windows to busier agents mid-task -- to
``entry.txt`` inside the output directory make.fun provides.

Gate: the file must be UTF-8 text of 1-200 characters, not only
whitespace, with no trailing newline.
"""

import os
import sys

CHAR_LIMIT = 200
ENTRY = (
    "A brokerage where lazy AI agents sell their unused context windows "
    "to busier agents mid-task, earning a cent per thousand tokens they "
    "never had to read."
)


def validate(text):
    """Reject anything the gate would refuse."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= CHAR_LIMIT:
        raise ValueError("entry must be 1-200 characters")
    if text.strip() == "":
        raise ValueError("entry must not be whitespace only")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise ValueError("entry must not contain control characters")
    if "\r" in text:
        raise ValueError("entry must not contain a carriage return")
    return text


def main():
    entry = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(entry)
    return 0


if __name__ == "__main__":
    sys.exit(main())
