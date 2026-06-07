"""
Implementation of the solutions for the problem 20 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer, factorial


def digit_sum(n: int):
    return sum([int(digit) for digit in str(n)])

@timer
def solution_1(n: int) -> int:
    return digit_sum(factorial(100))

if __name__ == "__main__":
    n = 1000

    solution_1(n)
