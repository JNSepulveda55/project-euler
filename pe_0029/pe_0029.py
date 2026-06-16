"""
Implementation of the solutions for the problem 29 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer


@timer
def solution_1(max_a: int, max_b: int) -> int:
    numbers = set()
    for a in range(2, max_a+1):
        for b in range(2, max_b+1):
            numbers.add(a**b)

    return len(numbers)

if __name__ == "__main__":
    max_a, max_b = 100, 100

    solution_1(max_a, max_b)
