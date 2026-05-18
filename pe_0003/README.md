# Problem Title
### Problem 0003

The prime factors of $13195$ are $5, 7, 13$ and $29$.

What is the largest prime factor of the number $600851475143$?

# Notes

- We'll be dealing with positive numbers only for this problem. Divisors can be extended to negative numbers as well but that is out of scope for this problem.

### A note on finding the divisors of a number

First, I want to point out a simple fact that will make this problem computationally feasible.

For any integer $n$, an integer $a$ is said to be a divisor of $n$ iif there exists another integer $b$ such that $n = a \cdot b$.

From this, we can see that divisors come in pairs, since if $a$ is a divisor of $n$ then $b$ is also a divisor of $n$. $(a, b)$ is called a *divisor pair* of $n$. (Note that a and b are not necessarily different). The trivial divisor pair is $(1, n)$.

**Lemma:** let $(a, b)$ be a divisor pair such that $a \leq b$. It follows that $a \leq \sqrt{n} \leq b$.

***proof.*** Let (a, b) be a divisor pair of $n$.
- If $a = b$ then $a = b = \sqrt{n}$

Assume $a \neq b$

- If $a < \sqrt{n}$ and $b < \sqrt{n}$ then $a \cdot b < \sqrt{n} \cdot \sqrt{n} = n$ $(\to \gets)$
- If $a > \sqrt{n}$ and $b > \sqrt{n}$ then $a \cdot b > \sqrt{n} \cdot \sqrt{n} = n$ $(\to \gets)$

The only option left is that $a < \sqrt{n} < b$

Finally, we get that $a \leq \sqrt{n} \leq b$. $\hspace{5cm} \square$

This result is telling us that to find all of the divisors of an integer $n$, we only need to check up to $\sqrt{n}$, which saves up a lot of compute time. 

# Solution

For the sake of convenience, we assume `n = 600851475143`. The code will work for any $n$

## Solution 1

The brute force approach would be to check every number up to $\sqrt{n}$ to see if its both prime and a divisor of $n$.

We first code a function to check whether a number is prime:

```py
def is_prime(n: int) -> bool:
    sqrtn = n ** 0.5
    for i in range(2, int(sqrtn) + 1):

        # If it has a divisor return false
        if n % i == 0:
            return False

    # It finished the loop so it has no divisors. Return True
    return True
```

Now we code the solution:

```py
def solution_1(n: int) -> int:
    sqrtn = n ** 0.5
    largest = 0
    for i in range(1, int(sqrtn) + 1):
        if n % i == 0 and is_prime(i):
            largest = i

    return largest
```

# Helpful Links

- [Divisor of a number](https://en.wikipedia.org/wiki/Divisor)
- [Prime number](https://en.wikipedia.org/wiki/Prime_number)


