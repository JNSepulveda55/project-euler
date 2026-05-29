"""
Implementation of the solutions for the problem 10 of Project Euler

See the README file for the explanation of the solutions
"""

import sys
from pathlib import Path

# Allow running this file directly while still importing from the repo root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer, is_prime

@timer(print_result=False)
def sieve_of_eratosthenes(n: int) -> list:
    """
    Find all primes under a limit n and returns them as a list.
    From PE_0010
    """
    if n <= 1:  # Edge case
        return []

    # [0, 1, 2] + [odd, even] (n//2 - 1) times + [odd] if n is odd
    sieve = [False, False, True] + [True, False] * (n//2 - 1) + ([False] if n%2 else [])
    p = 2
    while p * p <= n:
        # Find next non-crossed number
        p += 1
        while p * p < n and not sieve[p]:
            p += 1

        # Cross out non-primes
        sieve[p*p::p] = [False] * ((n - p**2)//p + 1) 
        
    return [i for i in range(n) if sieve[i]]

@timer
def solution_1(limit: int) -> int:
    total = 2  # We know 2 is prime
    for i in range(3, limit, 2):  # Only check odd numbers
        if is_prime(i):
            total += i

    return total


@timer
def solution_2(limit: int) -> int:
    primes = [2] # We know 2 is prime
    for i in range(3, limit, 2):  # Only check odd numbers
        for p in primes:
            # If divisible by a prime then not a prime. Skip
            if i % p == 0:  
                break
            # Only check until root of i
            if p > i**0.5:
                primes.append(i)
                break

    return sum(primes)

@timer
def solution_3(limit: int) -> int:
    return sum(sieve_of_eratosthenes(limit)) 

if __name__ == "__main__":
    limit = 2_000_000

    solution_1(limit)
    solution_2(limit)
    solution_3(limit)
