#!/usr/bin/env python3
"""Write one alien tourist's review of Earth to /output/entry.txt."""

import os

REVIEW = "Every Earth home keeps a set of plates too precious to eat from, saved for a visitor more important than me. I was never that visitor. 3 stars."

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
MAX_CHARS = 200

if "\n" in REVIEW or not 1 <= len(REVIEW) <= MAX_CHARS:
    raise SystemExit("review must be a single line of 1-200 characters")

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(REVIEW)
