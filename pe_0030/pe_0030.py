"""
Implementation of the solutions for the problem 30 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer

def fifth_power_digit_sum(n: int) -> int:
    return sum([int(d)**5 for d in str(n)])

@timer
def solution_1(upper_bound: int = 354294) -> int:
    total = 0

    # One-digit numbers don't count, so start at 10
    for i in range(10, upper_bound+1):  
        if fifth_power_digit_sum(i) == i:
            total += i

    return total

if __name__ == "__main__":
    solution_1()
