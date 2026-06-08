"""
Implementation of the solutions for the problem 21 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer

def divisors(n: int, proper: bool = False) -> list[int]:
    """
    Find the divisors of a number.
    Returns a list of unordered divisors.
    """
    if proper:
        divisors = [1]
    else:
        divisors = [1, n]

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            
            if n//i != i:
                divisors.append(n//i)

    return divisors

@timer
def solution_1(limit: int) -> int:
    amicable = set()

    for i in range(limit):
        # Skip if already amicable
        if i in amicable:
            continue

        div_sum_i = sum(divisors(i, proper=True))  # Find sum of divisors

        # If sum of divisors is the same number skip
        if div_sum_i == i:  
            continue

        if sum(divisors(div_sum_i, proper=True)) == i:  # If amicable
            amicable.add(i)

            if div_sum_i < limit:
                amicable.add(div_sum_i)

    return sum(amicable)


if __name__ == "__main__":
    limit = 10000

    solution_1(limit)
