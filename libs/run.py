from pathlib import Path
import sys

def run(func):
    fname = sys.argv[1] if len(sys.argv) > 1 else "input"
    with Path(fname).open() as f:
        result = func(f.read())
        if not isinstance(result, tuple):
            result = (result,)
        for i, r in enumerate(result, 1):
            print(f"Part {i}: {r}")
