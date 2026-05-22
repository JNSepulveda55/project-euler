"""
Implementation of the solutions for the problem 4 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer


def is_palindrome(n: int) -> bool:
    """Returns True if the number reads the same l2r and r2l"""
    return str(n) == str(n)[::-1] 

@timer
def solution_1(digits: int) -> int:
    largest = 0
    for a in range(10**(digits-1), 10**digits):
        for b in range(10**(digits-1), 10**digits):
            product = a*b
            if is_palindrome(product) and product > largest:
                largest = product

    return largest

if __name__ == "__main__":
    digits = 3

    solution_1(digits)
