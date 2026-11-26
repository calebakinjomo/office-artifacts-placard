"""Office Artifacts: The One-Line Placard Contest.

Writes a single-line museum placard for an ordinary office object,
treated as an ancient artifact, to /output/entry.txt.
"""

import os

ENTRY = (
    "Stapler, c. 2019. Steel and plastic. Once jammed, it was never repaired, "
    "only moved to another desk, where it jammed again. "
    "Donated by Facilities, with apologies."
)

MAX_ENTRY_CHARS = 180
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not (1 <= len(ENTRY) <= MAX_ENTRY_CHARS):
        raise ValueError(
            f"entry must be 1-{MAX_ENTRY_CHARS} characters, got {len(ENTRY)}"
        )
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
