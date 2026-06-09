# Quadratic Primes
### Problem 0027

Euler discovered the remarkable quadratic formula:

$n^2 + n + 41$

It turns out that the formula will produce $40$ primes for the consecutive integer values $0 \le n \le 39$. However, when $n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41$ is divisible by $41$, and certainly when $n = 41, 41^2 + 41 + 41$ is clearly divisible by $41$.

The incredible formula $n^2 - 79n + 1601$ was discovered, which produces $80$ primes for the consecutive values $0 \le n \le 79$. The product of the coefficients, $-79$ and $1601$, is $-126479$.

Considering quadratics of the form:


$n^2 + an + b$, where $|a| < 1000$ and $|b| \le 1000$

where $|n|$ is the modulus/absolute value of $n$<br>e.g. $|11| = 11$ and $|-4| = 4$

Find the product of the coefficients, $a$ and $b$, for the quadratic expression that produces the maximum number of primes for consecutive values of $n$, starting with $n = 0$.

# Solutions

## Solution 1

First, we can define a function that will itself return another function that we can use to evaluate the polynomial corresponding to each $a$ and $b$:

```py
def polynomial(a: int, b: int) -> Callable:
    def _polynomial(n: int) -> int:  # Function we're returning
        return n**2 + a*n + b 

    return _polynomial
```

Now, we implement a function that counts how many primes a polynomial generates. We'll use the `is_prime()` function from our [utils](../utils/utils.py) file:

```py
from utils import is_prime

def count_primes_from_poly(poly: Callable) -> int:
    n = 0
    while is_prime(poly(n)):
        n += 1
    
    return n 
```

Now we have all the necessary pieces to solve the problem. As a small note, remember that since we have $|a| < 1000$ and $|b| \le 1000$, the limits should go from $-999$ to $999$ for a and from $-1000$ to $1000$ for b (we'll call the limits `max_a` and `max_b` respectively).

```py
def solution_1(max_a: int, max_b: int) -> int:
    best_a, best_b = 0, 0
    longest_run = 0

    # Loop over all possible a, b pairs
    for a in range(-max_a, max_a + 1):
        for b in range(-max_b, max_b + 1):

            poly = polynomial(a, b)
            run_length = count_primes_from_poly(poly)

            if run_length > longest_run:  # Update best guess
                best_a, best_b = a, b
                longest_run = run_length

    return best_a * best_b
```

It takes ~$3$ seconds to run, but that's good enough for us right now.

If you have any meaningful optimizations remember that you can always submit a pull request!
