"""
This file contains useful functions that may be used
to get to the solution for a problem or just implement
nice functionalities like timing a code
"""

from time import time
from functools import wraps

def timer(original_function=None, *, print_result=True):
    """
    Time the function and optionally print result
    """
    def _timer(function):
        
        @wraps(function)
        def wrapped_function(*args, **kwargs):
            start = time()
            result = function(*args, **kwargs)
            end = time()
            print(f"Function {function.__name__} ran in {end-start:.5f} seconds.")
            if print_result:
                print(f"The function's output is: {result}")

            return result

        return wrapped_function
    
    if original_function:
        return _timer(original_function)
    
    return _timer


def is_prime(n: int) -> bool:
    """
    Check if a positive integer is a prime number.
    From PE_0003.
    """
    # Edge case not covered in the problem but necessary
    if n < 2:
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
    Returns True if the number reads the same l2r and r2l.
    From PE_0004
    """
    return str(n) == str(n)[::-1]


def sieve_of_eratosthenes(n: int) -> list:
    """
    Find all primes under n and returns them as a list.
    From PE_0010
    """

    # [0, 1, 2] + [odd, even] and so on
    sieve = [False, False, True] + [True, False] * (n//2 - 1)
    p = 2
    while p * p <= n:
        # Find next non-crossed number
        p += 1
        while p * p < n and not sieve[p]:
            p += 1

        # Cross out non-primes
        sieve[p*p::p] = [False] * ((n - p**2)//p + 1) 
        
    return [i for i in range(n) if sieve[i]]
