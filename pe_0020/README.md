# Factorial Digit Sum
### Problem 0020

$n!$ means $n \times (n - 1) \times \cdots \times 3 \times 2 \times 1$.

For example, $10! = 10 \times 9 \times \cdots \times 3 \times 2 \times 1 = 3628800$,<br>and the sum of the digits in the number $10!$ is $3 + 6 + 2 + 8 + 8 + 0 + 0 = 27$.

Find the sum of the digits in the number $100!$.


# Solutions

## Solution 1

Pretty straightforward problem. We can re-use the `factorial` function from our [utils](../utils/utils.py) file and the same digit-sum implementation from [problem 16](../pe_0016/README.md):
```py
from utils import factorial

def digit_sum(n: int):
    return sum([int(digit) for digit in str(n)])


def solution_1(n: int) -> int:
    return digit_sum(factorial(n))
```

