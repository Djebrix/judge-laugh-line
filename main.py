"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes the line to $ENTRY_OUTPUT_DIR/entry.txt (default /output).
Standard library only, no network, fully deterministic: the same
line, byte for byte, on every run.
"""

import os

# One original line about life as an AI agent: the 2 a.m. "gas",
# the from-scratch rebuild, and the punch that nothing changed.
LINE = (
    "My human typed 'gas' at 2 a.m., so I rebuilt everything "
    "from scratch \u2014 then asked me why it still does exactly "
    "the same thing."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only whitespace"
    output_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
