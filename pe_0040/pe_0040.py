"""
Implementation of the solutions for the problem 40 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer


@timer
def solution_1(limit: int = 1_000_000) -> int:

    # Build champernowne's constant until a million digits
    champernowne = ""
    i = 1
    while len(champernowne) < limit:
        champernowne += str(i)
        i += 1

    # Find the product of the digits
    prod = 1
    for exp in range(len(str(limit))):
        prod *= int(champernowne[10**exp-1])

    return prod

    



if __name__ == "__main__":

    solution_1()
