"""
Implementation of the solutions for the problem 36 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer, is_palindrome


def dec2base(n: int, base: int) -> str:
    """
    Convert a number from base 10 to base n
    """
    new_num = ""
    while n != 0:
        new_num = str(n % base) + new_num
        n //= base

    return new_num


@timer
def solution_1(limit: int) -> int:
    total = 0

    for n in range(1, limit + 1, 2):
        if is_palindrome(n):
            if is_palindrome(dec2base(n, 2)):
                total += n

    return total

if __name__ == "__main__":
    limit = 1_000_000

    solution_1(limit)
