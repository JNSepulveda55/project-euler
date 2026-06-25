"""
Implementation of the solutions for the problem 32 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer


@timer
def solution_1() -> int:
    solutions = set()  # Store in a set so that we only count once
    for a in range(100):
        for b in range(100, 10000):
            c = a * b
            # Join the digits of the numbers in a string
            digits = str(a) + str(b) + str(c)
            if set(digits) == set("123456789") and len(digits) == 9:
                solutions.add(c)
    
    return sum(solutions)

if __name__ == "__main__":
    solution_1()

