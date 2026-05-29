"""
Implementation of the solutions for the problem 12 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer, is_prime


def prime_decomposition(n: int) -> dict:
    """
    Find the prime decomposition of an integer.
    Return format is a dictionary with entries {prime: power}
    """

    if n <= 1:
        return {}  # Edge case
    
    decomposition = {}

    for i in range(n//2 + 1):

        if is_prime(i):
            if n % i == 0:
                decomposition[i] = 0  # Create dictionary entry for prime

            while n % i == 0:
                n //= i
                decomposition[i] += 1  # Update exponent for prime

        if n == 1:
            break

    return decomposition


def number_of_divisors(n: int) -> int:
    """
    Calculate the number of divisors of n using its prime decomposition
    """
    decomposition = prime_decomposition(n)  # Decompose number in prime factors
    powers = decomposition.values()  # Extract the e_i from decomposition

    total = 1
    for e in powers:
        total *= (e + 1)

    return total

@timer
def solution_1(limit: int) -> int:
    n = 1
    triangular = 1

    while number_of_divisors(triangular) <= limit:
        n += 1
        triangular = n*(n+1)//2

    return triangular


if __name__ == "__main__":
    limit = 500

    solution_1(limit)
