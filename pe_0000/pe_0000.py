"""
Implementation of the solutions for the problem 0 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer


@timer
def solution_1(limit: int) -> int:
    """
    Replace this with a straightforward solution.
    """
    raise NotImplementedError("Implement solution_1 for this problem.")


@timer
def solution_2(limit: int) -> int:
    """
    Replace this with a faster or cleaner solution.
    """
    raise NotImplementedError("Implement solution_2 for this problem.")


if __name__ == "__main__":
    limit = 1000

    solution_1(limit)
    solution_2(limit)
