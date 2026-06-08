# Non-Abundant Sums
### Problem 0023

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of $28$ would be $1 + 2 + 4 + 7 + 14 = 28$, which means that $28$ is a perfect number.

A number $n$ is called deficient if the sum of its proper divisors is less than $n$ and it is called abundant if this sum exceeds $n$.

As $12$ is the smallest abundant number, $1 + 2 + 3 + 4 + 6 = 16$, the smallest number that can be written as the sum of two abundant numbers is $24$. By mathematical analysis, it can be shown that all integers greater than $28123$ can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

# Solutions

## Solution 1

We will make use of the `divisors()` function from [`utils`] to solve this problem.

The first step is to find every abundant number under $28123$. After that, we can calculate all possible sums from two abundant numbers.

Finally, we compare and return the sum of all the numbers not in the set of abundant sums (sum of two abundant numbers)

```py
from utils import divisors

def solution_1(limit: int = 28123) -> int:
    
    # Find abundant numbers:
    abundant = []
    for i in range(1, limit):
        if sum(divisors(i, proper=True)) > i:
            abundant.append(i)

    # Calculate all sums of abundant numbers
    abundant_sums = set()
    for i in range(len(abundant)):
        for j in range(i+1):
            abundant_sums.add(abundant[i]+abundant[j])

    # Calculate the difference of sets
    non_abundant_sums = set(range(1, limit+1)) - abundant_sums

    return sum(non_abundant_sums)
```

# Helpful Links

- [Abundant Number](https://en.wikipedia.org/wiki/Abundant_number)
