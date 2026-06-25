"""
Implementation of the solutions for the problem 23 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer, divisors


@timer
def solution_1(limit: int = 28123) -> int:
    
    # Find abundant numbers:
    abundant = []
    for i in range(1, limit):
        if sum(divisors(i, proper=True)) > i:
            abundant.append(i)

    # Calculate all sums of abundant numbers
    abundant_sums = set()
    for i in range(len(abundant)):
        for j in range(i+1):
            abundant_sums.add(abundant[i]+abundant[j])

    # Calculate the difference of sets
    non_abundant_sums = set(range(1, limit+1)) - abundant_sums

    return sum(non_abundant_sums)


if __name__ == "__main__":
    solution_1()
