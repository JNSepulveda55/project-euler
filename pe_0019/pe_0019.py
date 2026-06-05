"""
Implementation of the solutions for the problem 19 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer


day_offsets = lambda year: [31, 28 + is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year: int) -> bool:

    if year % 4 != 0:
        return False
    
    if year % 100 == 0 and year % 400 != 0:
        return False
    
    return True

# Find what day the first day of a year falls on
def find_first_of_year(year: int) -> int:
    curr_year = 1900  # We know Jan 1 of 1900 is a Monday
    day = 1  # 0 is Sunday, 1 is Monday and so on ...

    # Check if we're searching forwards or backwards
    factor = 1 if year > curr_year else -1

    while curr_year != year:
        curr_year += factor
        day = (day + 1 + is_leap_year(curr_year)) % 7

    return day

@timer
def solution_1(century: int) -> int:
    year = 100*century + 1

    # Find the first day of the year
    day = find_first_of_year(year)
    
    count = 0
    for i in range(year, year + 100):
        for offset in day_offsets(i):
            
            if day % 7 == 0:
                count += 1  # If its a Sunday update count

            day = (day + offset) % 7

    return count
            

if __name__ == "__main__":
    century = 19

    solution_1(19)