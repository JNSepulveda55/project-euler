# Digit Factorials
### Problem 0034

$145$ is a curious number, as $1! + 4! + 5! = 1 + 24 + 120 = 145$.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As $1! = 1$ and $2! = 2$ are not sums they are not included.


# Solutions

Here, we can do an analysis similar to [Problem 30](../pe_0030/README.md):

The highest value for the factorial of a digit is $9! = 362,880$. Then, the highest number which *could* be equal to the sum of the factorial of its digits is $7\times9! = 2,540,160$, as if we add more digits, the sum of factorials of the digits will always be less than the number.

We define a helper function to find the sum of the factorial of the digits of a number:

```py
def sum_factorial_of_digits(n: int):
    total = 0
    for digit in str(n):
        # Add factorial of digit to total
        total += factorial(int(digit))
    
    return total
```

## Solution 1

Having found an upper bound, the code for the solution looks like this:

```py
from utils import factorial

@timer
def solution_1(limit: int = 2540160) -> int:
    total = 0
    for n in range(limit+1):
        if sum_factorial_of_digits(n) == n:
            total += n
    
    return n
    
```