"""
Implementation of the solutions for the problem 31 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer


@timer
def solution_1(target: int, coins: list) -> int:
    values = [1] + [0] * target  # Initialize initial value list
    
    # Loop over every coin
    for v in coins:
        # Loop over the list starting at v
        for i in range(v, target+1):
            values[i] = values[i] + values[i-v]

    return values[-1]  # Return last element


if __name__ == "__main__":
    target = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]

    solution_1(target, coins)
