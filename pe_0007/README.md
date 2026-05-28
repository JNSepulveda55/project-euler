# 10 001st Prime
### Problem 0007

By listing the first six prime numbers: $2, 3, 5, 7, 11$, and $13$, we can see that the $6$th prime is $13$.

What is the $10\,001$st prime number?

# Solutions

## Solution 1

This problem is very straightforward, and we can use one of the functions that we have defined previously for this:

```py
from utils import is_prime

def solution_1(limit: int) -> int:
    count = 1  
    n = 3  # Start at 3 and count = 1 since we already know 2 is prime
    while count < limit:
        if is_prime(n):
            count += 1
        n += 2  # Increment by two since all primes except 2 are odd

    return n - 2  # Undo last step
```

# Helpful Links

- [Problem 0003](../pe_0003/README.md)
