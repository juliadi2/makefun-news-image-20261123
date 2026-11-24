#!/usr/bin/env python3
"""Entry program for news-image-20261123.

Copies the pre-rendered front page (entry.png) to the grader's output
directory. Standard library only: the grader runs with no network and
installs nothing, so the image is rendered at build time by render.py
and shipped in this repository. A plain copy is deterministic, so both
grader runs write identical bytes.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "entry.png", OUT / "entry.png")


if __name__ == "__main__":
    main()
