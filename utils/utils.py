"""
This file contains useful functions that may be used
to get to the solution for a problem or just implement
nice functionalities like timing a code
"""

from time import time
from functools import wraps


def timer(function):
    """
    Time the function and print result
    """
    @wraps(function)
    def timer(*args, **kwargs):
        start = time()
        result = function(*args, **kwargs)
        end = time()
        print(f"Function {function.__name__} ran in {end-start:.5f} seconds.")
        print(f"The function's output is: {result}")

    return timer

def is_prime(n: int) -> bool:
    """
    Check if a positive integer is a prime number.
    From PE_0003.
    """
    if n < 2:           # Edge case
        return False

    sqrtn = n ** 0.5
    for i in range(2, int(sqrtn) + 1):

        # If it has a divisor return false
        if n % i == 0:
            return False

    # It finished the loop so it has no divisors. Return True
    return True

def is_palindrome(n: int) -> bool:
    """
    Returns True if the number reads the same l2r and r2l
    From PE_0004
    """
    return str(n) == str(n)[::-1] 
