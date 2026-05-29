# Summation of Primes
### Problem 0010

The sum of the primes below $10$ is $2 + 3 + 5 + 7 = 17$.

Find the sum of all the primes below two million.

# Notes

- This is our first problem with three solutions! (28-05-26)

# Solutions

## Solution 1

Once again, we can just use the `is_prime` function we defined in [utils.py](../utils/utils.py) to brute-force our way into solving this problem

```py
from utils import is_prime

def solution_1(limit: int) -> int:
    total = 2. # We know 2 is prime
    for i in range(3, limit, 2):  # Only check odd numbers
        if is_prime(i):
            total += i

    return total
```

This one actually takes some time to run! (Still just a few seconds)

## Solution 2

We can optimize our first solution by storing the primes we find and only using those to check for divisibility. It would look something like this:

```python
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
```
It runs in about half the time which is a nice improvement


## Solution 3

There is actually an even faster way to solve this problem! We can use what's called a **Sieve of Eratosthenes**, which lets us build a list of primes under certain number in a really efficient way.

Let's see how it works:

Imagine we were to put al the integers from 2 onwards in a grid or list like this, here $n = 25$:

$2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25$

We then will start crossing out the numbers that are multiple of the smallest number in the list starting from the square of the number, so in the first step we only need to cross out the multiples of two:

$2, 3, \textcolor{red}{4}, 5, \textcolor{red}{6}, 7, \textcolor{red}{8}, 9, \textcolor{red}{10}, 11, \textcolor{red}{12}, 13, \textcolor{red}{14}, 15, \textcolor{red}{16}, 17, \textcolor{red}{18}, 19, \textcolor{red}{20}, 21, \textcolor{red}{22}, 23, \textcolor{red}{24}, 25$

Next we do multiples of three:

$2, 3, \textcolor{red}{4}, 5, \textcolor{red}{6}, 7, \textcolor{red}{8}, \textcolor{red}{9}, \textcolor{red}{10}, 11, \textcolor{red}{12}, 13, \textcolor{red}{14}, \textcolor{red}{15}, \textcolor{red}{16}, 17, \textcolor{red}{18}, 19, \textcolor{red}{20}, \textcolor{red}{21}, \textcolor{red}{22}, 23, \textcolor{red}{24}, 25$

And since we only need to check until $\sqrt{n}$, it suffices to check until 5:

$2, 3, \textcolor{red}{4}, 5, \textcolor{red}{6}, 7, \textcolor{red}{8}, \textcolor{red}{9}, \textcolor{red}{10}, 11, \textcolor{red}{12}, 13, \textcolor{red}{14}, \textcolor{red}{15}, \textcolor{red}{16}, 17, \textcolor{red}{18}, 19, \textcolor{red}{20}, \textcolor{red}{21}, \textcolor{red}{22}, 23, \textcolor{red}{24}, \textcolor{red}{25}$

We can implement the sieve in code like this:

```python
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
```

We'll also add this function to our [`utils.py`](../utils/utils.py) file

Then the solution just becomes:

```python
def solution_3(limit: int) -> int:
    return sum(sieve_of_eratosthenes(limit)) 
```

And it runs incredibly fast!

# Helpful Links

- [Problem 7](../pe_0007/README.md)
- [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)

