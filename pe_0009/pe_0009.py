"""
Implementation of the solutions for the problem 9 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer


@timer
def solution_1(n: int) -> int:

    for a in range(n//4, (3*n)//4):
        for b in range(n//2 - a, a):
            c = (a**2 + b**2)**0.5
            # Check if c is an integer and a + b + c = n
            if c % 1 == 0 and a + b + int(c) == n:
                return int(a * b * c)

if __name__ == "__main__":
    n = 1000

    solution_1(n)
