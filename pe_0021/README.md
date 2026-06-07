# Amicable Numbers
### Problem 0021

Let $d(n)$ be defined as the sum of proper divisors of $n$ (numbers less than $n$ which divide evenly into $n$).<br>
If $d(a) = b$ and $d(b) = a$, where $a \ne b$, then $a$ and $b$ are an amicable pair and each of $a$ and $b$ are called amicable numbers.

For example, the proper divisors of $220$ are $1, 2, 4, 5, 10, 11, 20, 22, 44, 55$ and $110$; therefore $d(220) = 284$. The proper divisors of $284$ are $1, 2, 4, 71$ and $142$; so $d(284) = 220$.

Evaluate the sum of all the amicable numbers under $10000$.

# Solutions

The first thing we need to solve this problem is a function to find the divisors of a number $n$. We can do this by checking all numbers up to $\sqrt{n}$ and any time we find a divisor $d$, we know that $\frac{n}{d}$ is also a divisor since $d \cdot \frac{n}{d} = n$.

Here's our function:

```py
def divisors(n: int, proper: bool = False) -> list[int]:
    """
    Find the divisors of a number.
    Returns a list of unordered divisors.
    """
    if proper:
        divisors = [1]
    else:
        divisors = [1, n]

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n//i)

    return divisors
```

We can add this function to our [utils](../utils/utils.py) file.

## Solution 1

Now, we can simply check each number from $1$ to the limit ($10000$ in this case) and see if they are part of an amicable pair. Additionally, we can keep track of the numbers we already checked so that we don't check numbers twice.

Here's the code for that:

```py
def solution_1(limit: int) -> int:
    amicable = set()

    for i in range(limit):
        # Skip if already amicable
        if i in amicable:
            continue

        div_sum_i = sum(divisors(i, proper=True))  # Find sum of divisors

        # If sum of divisors is the same number skip
        if div_sum_i == i:  
            continue

        if sum(divisors(div_sum_i, proper=True)) == i:  # If amicable
            amicable.add(i)

            if div_sum_i < limit:
                amicable.add(div_sum_i)

    return sum(amicable)
```

# Helpful Links

- [Find divisors of a number](https://read.learnyard.com/dsa/divisors-of-a-number/)

- [Amicable numbers](https://en.wikipedia.org/wiki/Amicable_numbers)
