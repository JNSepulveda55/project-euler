"""
Implementation of the solutions for the problem 28 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer


@timer
def solution_1(n: int) -> int:
    total = 0
    for i in range(1, n+1, 2):
        total += 4*i**2 - 6*i + 6

    return total - 3

if __name__ == "__main__":
    n = 1001

    solution_1(n)