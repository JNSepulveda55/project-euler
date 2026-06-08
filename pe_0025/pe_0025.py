"""
Implementation of the solutions for the problem 25 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer


@timer
def solution_1(digits: int) -> int:
    total = 0
    prev_fib = 1
    curr_fib = 1
    idx = 2

    # 10**(digits-1) is the first number with that amount of digits
    while curr_fib < 10**(digits-1):
        if curr_fib % 2 == 0:
            total += curr_fib

        # Store current value in a temp variable
        temp = curr_fib
        
        # Update Fib number
        curr_fib = curr_fib + prev_fib
        
        # Update the previous Fib
        prev_fib = temp
        idx += 1

    return idx


if __name__ == "__main__":
    limit = 1000

    solution_1(limit)
    # solution_2(limit)
