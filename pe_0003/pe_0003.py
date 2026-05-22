"""
Implementation of the solutions for the problem 0 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer


def is_prime(n: int) -> bool:
    sqrtn = n ** 0.5
    for i in range(2, int(sqrtn) + 1):

        # If it has a divisor return false
        if n % i == 0:
            return False

    # It finished the loop so it has no divisors. Return True
    return True


@timer
def solution(n: int) -> int:
    sqrtn = n ** 0.5
    largest = 0
    for i in range(1, int(sqrtn) + 1):
        if n % i == 0 and is_prime(i):
            largest = i

    return largest


if __name__ == "__main__":
    n = 600851475143
    
    solution(n)
