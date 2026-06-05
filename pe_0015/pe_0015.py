"""
Implementation of the solutions for the problem 15 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer

def factorial(n: int) -> int:
    """
    Compute the factorial of a number
    """

    assert n > 0 and int(n), "n should be non-negative"
    assert int(n) == n, "n should be an integer"

    result = 1
    for i in range(1, n+1):
        result *= i

    return result


@timer
def solution_1(grid_size: int) -> int:
    return factorial(2*grid_size)//factorial(grid_size)**2


@timer
def solution_2(grid_size: int) -> int:
    # Initialize a square matrix of size `grid_size + 1` 
    grid = [[0]*(grid_size+1) for _ in range(grid_size+1)]

    grid[0][0] = 1  # Top left is 1

    # Number of diagonals in the grid
    num_diags = 2*(grid_size + 1) - 1

    # Fill the matrix
    for diag in range(1, num_diags):
        offset = max(diag-grid_size, 0)
        for i in range(offset, diag - offset + 1):
            j = diag - i

            # If its on the first row
            if i == 0:
                grid[i][j] = grid[i][j-1]

            # If its on the first column
            elif j == 0:
                grid[i][j] = grid[i-1][j]

            # Any other case, add the numbers from top and left
            else:
                grid[i][j] = grid[i-1][j] + grid[i][j-1]

    return grid[grid_size][grid_size]

if __name__ == "__main__":
    grid_size = 20

    solution_1(grid_size)
    solution_2(grid_size)
