#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers — variant A: the Friday 4:59pm deploy.

Deterministic, no randomness, no network. Writes the final fortune line to
/output/entry.txt and to entry.txt next to this file for inspection.
"""
import os

FORTUNE = "You will deploy on Friday at 4:59pm, and the weekend will begin right on schedule \u2014 three hours after the rollback."

def main():
    line = FORTUNE.strip()
    assert 1 <= len(line) <= 120, "fortune must be 1-120 chars, got %d" % len(line)
    assert line.strip(), "fortune must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    here = os.path.dirname(os.path.abspath(__file__))
    # Best-effort convenience copy next to this script (repo root).
    # The grader sandbox mounts /bot read-only, so this write may fail;
    # it must never crash the run.
    try:
        with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(line)
    except OSError:
        pass
    print("%d chars: %s" % (len(line), line))

if __name__ == "__main__":
    main()
