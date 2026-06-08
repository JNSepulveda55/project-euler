"""
Implementation of the solutions for the problem 22 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer


def preprocess_names(filepath: str = "pe_0022/names.txt") -> list[str]:
    with open(filepath, "r") as file:
        names = file.read()
        names = names.replace("\"", "")  # Get rid of quotation marks "
        names = names.split(",")  # Split the names and save in a list

    return names


def name_worth(name: str) -> int:
    return sum([(ord(i)) - 64 for i in name])


@timer
def solution_1(names: list[str]) -> int:
    # Sort the list alphabetically
    names.sort()

    score_sum = 0
    for idx, name in enumerate(names):  # Get index and name
        score_sum += (idx+1) * name_worth(name)

    return score_sum


if __name__ == "__main__":

    names = preprocess_names()
    solution_1(names)