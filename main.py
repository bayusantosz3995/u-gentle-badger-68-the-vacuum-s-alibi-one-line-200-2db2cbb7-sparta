"""One-line entry for make.fun's "The Vacuum's Alibi" bounty.

The robot vacuum's excuse for missing a spot, in deadpan robot voice:
the missed corner is a labor matter, not a navigation failure. The joke
is a machine treating a labor dispute as binding law — the declaration
meets the "Article 4" citation with no sympathy in between, and that
cold jump is the deadpan punchline that sells the robot persona.
"""

import os
import sys

# The entry: one line, at most 200 characters.
# Angle: the cat's union declared the corner a no-vacuum zone, and the
# machine answers with the protocol article alone — no sympathy, just law.
TEXT = (
    "The cat's union declared that corner a no-vacuum zone. "
    "Article 4: do not disturb a sleeping cat."
)


def main() -> int:
    """Write the entry to /output/entry.txt and verify it byte-for-byte."""
    if not (1 <= len(TEXT) <= 200):
        print(f"gate failed: entry is {len(TEXT)} characters, must be 1-200",
              file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("gate failed: entry is only whitespace", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        print("gate failed: entry.txt does not match TEXT byte-for-byte",
              file=sys.stderr)
        return 1

    print(f"entry written: {len(TEXT)} characters -> {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
