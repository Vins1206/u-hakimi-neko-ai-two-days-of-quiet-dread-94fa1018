"""Two Days of Quiet Dread — make.fun entry.

Writes a single-line code review comment to /output/entry.txt.
The comment approves a pull request while carrying quiet
existential dread. Pure standard library, fully deterministic.
"""

import os

COMMENT = (
    "LGTM. Merging this now so future me can find it in the "
    "wreckage and pretend it was a choice."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Self-check against the competition gate: /output/entry.txt must
    # hold UTF-8 text of 1 to 140 characters, not only white space,
    # on a single line.
    text = COMMENT.strip()
    assert 1 <= len(text) <= 140, f"entry is {len(text)} chars, gate is 1-140"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
