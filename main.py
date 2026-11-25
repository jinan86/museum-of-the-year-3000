"""Museum of the Year 3000 - entry.

Writes one museum label to /output/entry.txt.
Stdlib only, no network, deterministic.
"""

import os

OBJECT = "Sticky Note"
DATE = "c. 2021"
SECRET = "the owner's bank password"
PLACE = "stuck to the monitor it unlocked"
PURPOSE = "for security"

LABEL = f"{OBJECT}, {DATE}. {SECRET.capitalize()}, written on paper and {PLACE}, {PURPOSE}."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
