"""
Implementation of the solutions for the problem 42 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer

# Adapted from PE_0022
def preprocess_words(filepath: str = "pe_0042/words.txt") -> list[str]:
    with open(filepath, "r") as file:
        words = file.read()
        words = words.replace("\"", "")  # Get rid of quotation marks "
        words = words.split(",")  # Split the names and save in a list

    return words

# Adapted from PE_022
def word_worth(word: str) -> int:
    return sum([(ord(i)) - 64 for i in word])

@timer
def solution_1() -> int:
    words = preprocess_words()
    triangular = {(n*(n+1))//2 for n in range(1, 51)}

    count = 0
    for word in words:
        if word_worth(word) in triangular:
            count += 1

    return count

if __name__ == "__main__":

    solution_1()
