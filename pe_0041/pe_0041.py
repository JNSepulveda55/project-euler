"""
Implementation of the solutions for the problem 41 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer, sieve_of_eratosthenes, is_prime


@timer
def solution_1(limit: int = 7654321) -> int:
    primes = sieve_of_eratosthenes(limit)
    for prime in primes[::-1]:
        # Check for pandigital
        digits = set(str(i) for i in range(1, len(str(prime))+1))
        if set(str(prime)) == digits:
            return prime

if __name__ == "__main__":

    solution_1()
