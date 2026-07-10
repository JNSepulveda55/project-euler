"""
Implementation of the solutions for the problem 38 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer


@timer
def solution_1() -> int:
    largest = 0

    for i in range(10**4):  # Check numbers up to 4 digits long
        mult = 2
        digits = str(i)  # Store digits
        while len(digits) < 9:
            digits += str(mult * i)  # Find next multiple and concatenate it
            mult += 1

        if len(digits) == 9 and set(digits) == set("123456789"):  # If its pandigital
            if int(digits) > largest:  # If its the largest, update
                largest = int(digits)
            
    return largest

if __name__ == "__main__":

    solution_1()
