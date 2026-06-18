# Digit Fifth Powers
### Problem 0030

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
$$\begin{align*}
1634 &= 1^4 + 6^4 + 3^4 + 4^4\\
8208 &= 8^4 + 2^4 + 0^4 + 8^4\\
9474 &= 9^4 + 4^4 + 7^4 + 4^4
\end{align*}$$

As $1 = 1^4$ is not a sum it is not included.

The sum of these numbers is $1634 + 8208 + 9474 = 19316$.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

# Solutions

Before starting, let's do some quick analysis:

For an $n$-digit number, the maximum sum of the fifth powers of its digits is $n\times 9^5$. Hence, the maximum number that ***could*** be equal to the sum of fifth powers of its digits is $6\times 9^5 = 354,294$, since its the maximum possible sum of fifth powers of digits that has the same or more digits than the number itself.

$7\times 9^5 = 413,343$ is the maximum achievable sum by a 7-digit number but it only has six digits, so from 7 digits onwards it wouldn't work.

## Solution 1

Now that we have an upper limit, we can just check every number up to $354,294$ and record the ones that can be written as the sum of fifth powers of their digits.

First, we define a function to find the sum of fifth powers of the digits of a number:

```py
def fifth_power_digit_sum(n: int) -> int:
    return sum([int(d)**5 for d in str(n)])
```

Now we can implement the main function to solve the problem:

```py
def solution_1(upper_bound: int = 354294) -> int:
    total = 0

    # One-digit numbers don't count, so start at 10
    for i in range(10, upper_bound+1):  
        if fifth_power_digit_sum(i) == i:
            total += i

    return total
```
