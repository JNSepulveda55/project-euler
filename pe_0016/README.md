# Power Digit Sum
### Problem 0016

$2^{15} = 32768$ and the sum of its digits is $3 + 2 + 7 + 6 + 8 = 26$.

What is the sum of the digits of the number $2^{1000}$?

# Solutions

## Solution 1
We can just brute-force this problem. We just need to define a function to sum the digits of a number:

```py
def digit_sum(n: int):
    return sum([int(digit) for digit in str(n)])
```

Then our solution would be:

```py
def solution_1(n: int) -> int:
    return digit_sum(n)
```