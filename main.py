"""Entry for "Make the AI Judge Laugh: Office Jokes" — one original
one-line office joke. The turn: the only thing in the office with a
healthy work-life balance is the fake plant.
"""

import os

ENTRY = "The office plant died. Facilities replaced it with a plastic one, and honestly, the plastic one has better work-life balance than I do."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
