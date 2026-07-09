# Truncatable Primes
### Problem 0037

The number $3797$ has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: $3797$, $797$, $97$, and $7$. Similarly we can work from right to left: $3797$, $379$, $37$, and $3$.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: $2$, $3$, $5$, and $7$ are not considered to be truncatable primes.

# Solutions

Similar to [problem 35](../pe_0035/README.md), for a prime to be truncatable it can only consist of the digits $1, 3, 7$ and $9$ except for the first digit, which can be a $2, 3, 5$ or $7$ (1-digit prime numbers).

Then, we only need to check numbers that follow these restrictions, and stop once we find $11$ truncatable primes.

## Solution 1

Here's a small function to tell if a number is truncatable:

```py
def is_truncatable(n: int) -> bool:
    # Only a prime number can be truncatable
    if not is_prime(n):
            return False

    str_n = str(n)
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])):  # Check left-truncatable
            return False
        
        if not is_prime(int(str_n[:i])):  # Check right-truncatable
            return False
        
    return True
```

The implementation for our solution is then:

```py
def solution_1() -> int:
    truncatable = set()
    
    n = 11 # Smallest 2-digit prime
    while len(truncatable) < 11:
        n += 2

        if is_truncatable(n):   
            truncatable.add(n)

    return sum(truncatable)
```
