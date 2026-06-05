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
    Find all primes under a limit n and returns them as a list.
    From PE_0010
    """
    if n <= 1:  # Edge case
        return []
    
    if n == 2:
        return [2]

    # [0, 1, 2] + [odd, even] (n//2 - 1) times + [odd] if n is odd
    sieve = [False, False, True] + [True, False] * (n//2 - 1) + ([False] if n%2 else [])
    p = 1
    while p * p <= n:
        # Find next non-crossed number
        p += 2
        while p * p < n and not sieve[p]:
            p += 2

        # Cross out non-primes
        sieve[p*p::p] = [False] * ((n - p**2)//p + 1) 
        
    return [i for i in range(n) if sieve[i]]


def prime_decomposition(n: int) -> dict:
    """
    Find the prime decomposition of an integer.
    Return format is a dictionary with entries {prime: power}.
    From PE_0012
    """

    if n <= 1:
        return {}  # Edge case
    
    decomposition = {}

    for i in range(n//2 + 1):

        if is_prime(i):
            if n % i == 0:
                decomposition[i] = 0  # Create dictionary entry for prime

            while n % i == 0:
                n //= i
                decomposition[i] += 1  # Update exponent for prime

        if n == 1:
            break

    return decomposition


def factorial(n: int) -> int:
    """
    Compute the factorial of a number.
    From PE_0015
    """

    assert n > 0 and int(n), "n should be non-negative"
    assert int(n) == n, "n should be an integer"

    result = 1
    for i in range(1, n+1):
        result *= i

    return result

if __name__ == "__main__":
    
    for n in range(100):
        print(f"n: {n} ->", sieve_of_eratosthenes(n))
    
    # print(sieve_of_eratosthenes(12))