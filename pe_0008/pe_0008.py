"""
Implementation of the solutions for the problem 8 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer


@timer
def solution_1(digit_string: str, window_size) -> int:
    product = 1
    zeros_in_window = 0  # Keep track of zeros in the window

    # Initial window product
    for i in range(window_size):
        digit = int(digit_string[i])
        if digit == 0:
            zeros_in_window += 1
        product *= digit

    max_product = product

    for i in range(1, len(digit_string) - window_size):
        leaves = int(digit_string[i-1])
        comes = int(digit_string[i+window_size-1])

        if leaves != 0:
            product //= leaves
        else:
            zeros_in_window -= 1

        if comes != 0:
            product *= comes
        else:
            zeros_in_window += 1
            continue  # If there's a 0 incoming just skip the iteration
        
        if product > max_product and zeros_in_window == 0:
            max_product = product
            print(digit_string[i:i+window_size])

    return max_product


@timer
def solution_2(limit: int) -> int:
    """
    Replace this with a faster or cleaner solution.
    """
    raise NotImplementedError("Implement solution_2 for this problem.")


if __name__ == "__main__":
    digit_string = "73167176531330624919225119674426574742" \
    "35534919493496983520312774506326239578318016984801869" \
    "47885184385861560789112949495459501737958331952853208" \
    "80551112540698747158523863050715693290963295227443043" \
    "55766896648950445244523161731856403098711121722383113" \
    "62229893423380308135336276614282806444486645238749303" \
    "58907296290491560440772390713810515859307960866701724" \
    "27121883998797908792274921901699720888093776657273330" \
    "01053367881220235421809751254540594752243525849077116" \
    "70556013604839586446706324415722155397536978179778461" \
    "74064955149290862569321978468622482839722413756570560" \
    "57490261407972968652414535100474821663704844031998900" \
    "08895243450658541227588666881164271714799244429282308" \
    "63465674813919123162824586178664583591245665294765456" \
    "82848912883142607690042242190226710556263211111093705" \
    "44217506941658960408071984038509624554443629812309878" \
    "79927244284909188845801561660979191338754992005240636" \
    "89912560717606058861164671094050775410022569831552000" \
    "55935729725716362695618826704282524836008232575304207" \
    "52963450"

    window_size = 13

    solution_1(digit_string, window_size)
