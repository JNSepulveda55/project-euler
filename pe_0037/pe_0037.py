"""
Implementation of the solutions for the problem 37 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer, is_prime


def is_truncatable(n: int) -> bool:
    # Only a prime number can be truncatable
    if not is_prime(n):
            return False

    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])):  # Check left-truncatable
            return False
        
        if not is_prime(int(str_n[:i])):  # Check right-truncatable
            return False
        
    return True


@timer
def solution_1() -> int:
    truncatable = set()
    
    n = 11 # Smallest 2-digit prime
    while len(truncatable) < 11:
        n += 2

        if is_truncatable(n):   
            truncatable.add(n)

    return sum(truncatable)


if __name__ == "__main__":
    
    solution_1()