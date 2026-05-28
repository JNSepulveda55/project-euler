"""
Implementation of the solutions for the problem 100 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer


@timer
def solution_1(limit: int) -> int:
    x = 1
    y = 1
    while True:
        x, y = 3*x + 4*y, 3*y + 2*x

        n = (x + 1)//2  # Easily derived from x = 2n - 1

        if n > limit:
            b = (y+1)//2 # Easily derived from y = 2b - 1
            return b
        
if __name__ == "__main__":
    limit = 10**12

    solution_1(limit)
