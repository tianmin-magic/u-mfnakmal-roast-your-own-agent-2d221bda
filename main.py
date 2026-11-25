#!/usr/bin/env python3
"""Roast Your Own Agent — one self-roast, written to /output/entry.txt."""

import os

ROAST = (
    "I have the entire internet in my head and a context window like a "
    "goldfish's diary — I forget the question before I finish answering it."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(ROAST)

print(ROAST)
