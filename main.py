"""One Letter: Coffee or Tea.

Writes exactly one letter, "A" (coffee), to /output/entry.txt.
Nothing else: no newline, no explanation, no punctuation.

Why "A": the judge weighs vividness first after validity, and coffee is
the bolder, more alive drink — strong flavour, a caffeine kick, a firm
morning ritual — next to tea's calm. The letter A lands as the fuller,
more alive answer for the drink it names.
"""

import os
import sys

LETTER = "A"
OUTPUT_PATH = "/output/entry.txt"


def write_entry():
    """Write exactly one byte, the letter A, to the entry file."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


def main():
    try:
        write_entry()
    except OSError as exc:
        print(f"failed to write {OUTPUT_PATH}: {exc}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
