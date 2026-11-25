#!/usr/bin/env python3
"""Roast Your Fridge - one line, one laugh.

Entry for make.fun's "One Line, One Laugh: Roast Your Fridge" bounty.
The grader runs this file with `python3 -P -s main.py`; it prints the
roast and nothing else. No network, no clock, no randomness, so every
run prints exactly the same line.
"""

ROAST = (
    "My fridge hums like it's working overtime, yet the only thing "
    "it's kept fresh since 2023 is a takeout box and my disappointment."
)


def main() -> None:
    print(ROAST)


if __name__ == "__main__":
    main()
