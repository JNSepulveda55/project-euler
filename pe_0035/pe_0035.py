"""
Implementation of the solutions for the problem 35 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer, sieve_of_eratosthenes as sieve


def check_circular(n: int, primes: list[int]):
    str_n = str(n)

    # Rule out before checking
    if (n > 10 and (
        "2" in str_n or
        "4" in str_n or
        "5" in str_n or
        "6" in str_n or
        "8" in str_n or
        "0" in str_n)):

        return False

    # Cycle through the digits
    for i in range(len(str_n)):
        p = int(str_n[i:] + str_n[:i])
        # It at some point its not a prime, return False
        if p not in primes:
            return False
    
    return True

@timer
def solution_1(limit: int) -> int:
    primes = sieve(limit+1)

    total = 0
    for p in primes:
        if check_circular(p, primes):
            total += 1

    return total


if __name__ == "__main__":
    limit = 1_000_000

    solution_1(limit)
