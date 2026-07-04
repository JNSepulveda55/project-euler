# Circular Primes
### Problem 0035

The number, $197$, is called a circular prime because all rotations of the digits: $197$, $971$, and $719$, are themselves prime.

There are thirteen such primes below $100$: $2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79$, and $97$.

How many circular primes are there below one million?


# Solutions

For this problem we can just find all primes up to one million and check each one individually and see if they're circular.

We can define a function to check is a prime is circular:

```py
def check_circular(n: int, primes: list[int]):
    str_n = str(n)
    # Cycle through the digits
    for i in range(len(str_n)):
        p = str_n[i:] + str_n[i:]
        # It at some point its not a prime, return False
        if p not in primes:
            return False
    
    return True
```

However, just naively checking every prime will take a long time. We can rule out many primes by noticing the following:

Say we want to check if the number $5939$ is prime. then, we will have to check every rotaion of the digits of the number:

```
5939 -> 9593 -> 3959 -> 9395
```

Notice that at some point, every digit in the number will occupy the ones position. Since any number ending in $2, 4, 5, 6, 8$ or $0$ is not prime, the only digits that a circular prime can have are $1, 3, 7$ and $9$.

So, we can discard any number that has a $2, 4, 5, 6, 8$ or $0$ in its digits. The updated `check_circular()` function then is:

```py
def check_circular(n: int, primes: list[int]):
    str_n = str(n)

    # Rule out before checking
    if (n > 10 and (
        "2" in str_n or
        "4" in str_n or
        "5" in str_n or
        "6" in str_n or
        "8" in str_n or
        "0" in str_n)):

        return False

    # Cycle through the digits
    for i in range(len(str_n)):
        p = int(str_n[i:] + str_n[:i])
        # It at some point its not a prime, return False
        if p not in primes:
            return False
    
    return True
```

## Solution 1

Our solution looks like this:

```py
def solution_1(limit: int) -> int:
    primes = sieve(limit+1)

    total = 0
    for p in primes:
        if check_circular(p, primes):
            total += 1

    return total
```

# Helpful Links

- [Circular primes](https://en.wikipedia.org/wiki/Circular_prime)
