"""
Implementation of the solutions for the problem 33 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer


def find_digit_cancelling_fractions() -> tuple[list[int], list[int]]:
    numerators = []
    denominators = []

    for d in range(10, 100):  # Denominator
        str_d = str(d)
        for n in range(10, d):  # Numerator can't be larger than `d`
            str_n = str(n)

            # Check if they share a digit
            if str_d[0] in str_n:
                shared = str_d[0]

            elif str_d[1] in str_n:
                shared = str_d[1]

            else:
                continue  # Check next number

            # Skip trivial cases
            if shared == "0":
                continue

            # Cancel shared digit
            leftover_d = int(str_d.replace(shared, "", 1))
            leftover_n = int(str_n.replace(shared, "", 1))

            # Save result
            if n * leftover_d == d * leftover_n:
                numerators.append(n)
                denominators.append(d)
    
    return numerators, denominators


def gcd(a: int, b: int) -> int:
    """
    Find the greatest common divisor (gcd) between two integers
    """
    while True:
        if b == 0:
            return a
        
        a, b = b, a%b

@timer
def solution_1() -> int:
    numerators, denominators = find_digit_cancelling_fractions()

    # Multiply all numerators and denominators to find the product of the fractions
    num = 1
    den = 1
    for i in range(len(numerators)):
        num *= numerators[i]
        den *= denominators[i]

    return den // gcd(num, den)

if __name__ == "__main__":
    solution_1()