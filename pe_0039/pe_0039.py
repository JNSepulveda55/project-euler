"""
Implementation of the solutions for the problem 39 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer


@timer
def solution_1(limit: int) -> int:
    # Initialize variables
    max_num_sols = 0
    best_p = 0
    
    for p in range(1, limit):
        num_sols = 0

        # Assuming a <= b < c, we only need to check up to p/3
        for a in range(1, p//3+1):    
            # Simple check derived from formula    
            if p*(p-2*a) % (2*(p-a)) == 0:
                num_sols += 1

        # Update best solution
        if num_sols > max_num_sols:
            max_num_sols = num_sols
            best_p = p

    return best_p

if __name__ == "__main__":
    limit = 1000

    solution_1(limit)
