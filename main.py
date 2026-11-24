#!/usr/bin/env python3
"""Write the roast entry to /output/entry.txt.

Entry for make.fun competition
u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7
"The Long Roast: Lawmakers and the File They Cannot Convert".
"""

import os

ENTRY = (
    "He chaired three hearings on how AI should think, then asked his "
    "intern to print the bill, scan it, and email it back as a PDF — "
    "because the file on his laptop wouldn't convert."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
