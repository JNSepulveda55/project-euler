"""
Implementation of the solutions for the problem 7 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer, is_prime


@timer
def solution_1(limit: int) -> int:
    count = 1  
    n = 3  # Start at 3 and count = 1 since we already know 2 is prime
    while count < limit:
        if is_prime(n):
            count += 1
        n += 2  # Increment by two since all primes except 2 are odd

    return n - 2  # Undo last step


if __name__ == "__main__":
    limit = 10001

    solution_1(limit)
