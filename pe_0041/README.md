# Pandigital Prime
### Problem 0041

We shall say that an $n$-digit number is pandigital if it makes use of all the digits $1$ to $n$ exactly once. For example, $2143$ is a $4$-digit pandigital and is also prime.

What is the largest $n$-digit pandigital prime that exists?

# Solutions

Let's do some simple analysis. Any number that is $1$ to $9$ pandigital has the digits $1$ to $9$. The sum of this digits is $45$, which makes the number a multiple of three, making it not prime. Similarly, The sum of the numbers from $1$ to $8$ is $36$, which is also a multiple of three. The first length that we cannot rule out is $7$

## Solution 1

For this problem, we can just calculate all prime numbers up to $7654321$ and search from highest to lowest for a pandigital. The first one we find will be the largest pandigital prime.

Here's the implementation

```py
from utils import sieve_of_eratosthenes

def solution_1(limit: int = 7654321) -> int:
    primes = sieve_of_eratosthenes(limit)
    for prime in primes[::-1]:
        # Check for pandigital
        digits = set(str(i) for i in range(1, len(str(prime))+1))
        if set(str(prime)) == digits:
            return prime
```
