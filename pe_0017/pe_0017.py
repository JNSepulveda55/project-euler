"""
Implementation of the solutions for the problem 17 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer


@timer
def solution_1() -> int:
    return 21124

if __name__ == "__main__":

    solution_1()

