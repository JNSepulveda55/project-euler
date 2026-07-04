"""
Implementation of the solutions for the problem 34 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer, factorial

# Helper function
def sum_factorial_of_digits(n: int):
    total = 0
    for digit in str(n):
        # Add factorial of digit to total
        total += factorial(int(digit))
    
    return total


@timer
def solution_1(limit: int = 2540160) -> int:
    total = 0
    for n in range(3, limit+1):
        if sum_factorial_of_digits(n) == n:
            total += n
    
    return total
if __name__ == "__main__":

    solution_1()
