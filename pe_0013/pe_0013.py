"""
Implementation of the solutions for the problem 13 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer


@timer
def solution_1(numbers: int) -> int:
    return str(sum(numbers))[:10]


if __name__ == "__main__":
    with open("pe_0013/numbers.txt") as file:
        text = file.read()
        numbers = text.split("\n")
        numbers = [int(x) for x in numbers]

    solution_1(numbers)
