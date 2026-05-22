"""
Implementation of the solutions for the problem 2 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer


@timer
def solution_1(limit: int) -> int:
    def Fib(n: int) -> int:
        """
        Returns the n-th fibonacci number using recursion
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return Fib(n-1) + Fib(n-2)
    
    total = 0
    n = 0
    last_fib = 0

    while last_fib < limit:
        fib = Fib(n)

        if fib % 2 == 0:
            total += fib

        last_fib = fib
        n += 1

    return total


@timer
def solution_2(limit: int) -> int:
    total = 0
    prev_fib = 1
    curr_fib = 1

    while curr_fib < limit:
        if curr_fib % 2 == 0:
            total += curr_fib

        # Store current value in a temp variable
        temp = curr_fib
        
        # Update Fib number
        curr_fib = curr_fib + prev_fib
        
        # Update the previous Fib
        prev_fib = temp

    return total


if __name__ == "__main__":
    limit = 4_000_000
    solution_1(limit)
    solution_2(limit)
