"""
Implementation of the solutions for the problem 26 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer


def find_period_length(d: int) -> int:
    remainders = []  # We'll store the reaminders here
    remainder = 1  # Initialize remainder

    while True:
        remainder = remainder % d

        # If there is no remainder, the decimal is not periodic. Return 0
        if remainder == 0:
            return 0
        
        # If we already got that remainder, the cycle closed. Return length
        elif remainder in remainders:
            return len(remainders) - remainders.index(remainder)

        # Else, add a zero and continue the cycle
        else:
            remainders.append(remainder)
            remainder *= 10  # Add a zero
            

@timer
def solution_1(limit: int) -> int:
    longest_period = 0
    best_number = 0

    for i in range(1, limit):
        period_length = find_period_length(i)

        if period_length > longest_period:  # Update the best guess
            longest_period = period_length
            best_number = i

    return best_number


if __name__ == "__main__":
    limit = 1000

    solution_1(limit)
