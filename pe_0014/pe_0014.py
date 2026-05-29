"""
Implementation of the solutions for the problem 14 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer

@timer
def solution_1(limit: int) -> int:
    # Variables to keep track
    best_number = 0
    best_length = 0
    visited = set()

    # Check elements in reverse
    for i in range(limit - 1, 0, -1):
        if i in visited:
            continue

        # Calculate sequence for each number and store visited numbers
        seq_len = 1
        n = i  # Copy the number
        while n != 1:  # Assuming all numbers end in 1
            if n%2 == 0:
                n //= 2
            else:
                n = 3*n + 1

            seq_len += 1
            visited.add(n)

        # Update best number
        if seq_len > best_length:
            best_length = seq_len
            best_number = i
        

    return best_number

if __name__ == "__main__":
    limit = 1_000_000

    solution_1(limit)
