"""
Implementation of the solutions for the problem 24 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer, factorial


@timer
def solution_1(position: int) -> int:
    permutation = ""  # This will be our final permutation
    
    # To keep track of remaining digits
    remaining_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # We'll subtract from this as we find digits
    remaining_positions = position - 1  # We start counting at 0

    while len(remaining_digits) > 0:
        # How many permutations start with each of the remaining digits?
        perms_per_digit = factorial(len(remaining_digits) - 1)

        # Get the index of the next digit
        digit_idx = remaining_positions // perms_per_digit

        digit = remaining_digits[digit_idx]  # Next digit in the permutation
        permutation += digit  # Add digit to the permutation
        remaining_digits.remove(digit)       # Remove digit from remaining digits list

        remaining_positions -= perms_per_digit * digit_idx  # Update remaining positions

    return int(permutation)


if __name__ == "__main__":
    position = 1_000_000

    solution_1(position)
