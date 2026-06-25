"""
Implementation of the solutions for the problem 27 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path
from collections.abc import Callable

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer, is_prime


def polynomial(a: int, b: int) -> Callable:
    def _polynomial(n: int) -> int:  # Function we're returning
        return n**2 + a*n + b 

    return _polynomial


def count_primes_from_poly(poly: Callable) -> int:
    n = 0
    while is_prime(poly(n)):
        n += 1
    
    return n 

@timer
def solution_1(max_a: int, max_b: int) -> int:
    best_a, best_b = 0, 0
    longest_run = 0

    for a in range(-max_a, max_a + 1):
        for b in range(-max_b, max_b + 1):
            poly = polynomial(a, b)
            run_length = count_primes_from_poly(poly)

            if run_length > longest_run:
                best_a, best_b = a, b
                longest_run = run_length

    return best_a * best_b


if __name__ == "__main__":
    max_a, max_b = 999, 1000

    solution_1(max_a, max_b)

