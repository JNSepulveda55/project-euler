"""
Implementation of the solutions for the problem 5 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer, is_prime


@timer
def solution_2(limit: int) -> int:
    prime_powers = []
    result = 1

    # Iterate over all numbers less than limit
    for i in range(1, limit+1):

        # If prime, find greatest power under limit
        if is_prime(i):
            max_pow = 1
            curr_num = i

            while curr_num * i <= limit:
                curr_num *= i
                max_pow += 1
            
            # Keep track of the product of the results
            result *= curr_num

    return result

if __name__ == "__main__":
    limit = 20

    # No code for solution 1
    solution_2(limit)
