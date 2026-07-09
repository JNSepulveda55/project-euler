# Double-base Palindromes
### Problem 0036

The decimal number, $585 = 1001001001_2$ (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base $10$ and base $2$.

(Please note that the palindromic number, in either base, may not include leading zeros.)

# Solutions

For this problem, we just need a function to find the base-2 representation of a number and look for numbers that are palindromes in both base $2$ and base $10$.

As a recap, a if a number in base $10$, it means that it can be represented as a sum of powers of $10$, where each digit of the number represents a power of ten. Let's see an example:

$8416_{10} = 8\cdot10^3 + 4\cdot10^2 + 1\cdot10^1 + 6\cdot10^0$.

Similarly, a number in base $2$ represents a sum of powers of $2$, for example:

$110101_2 = 1\cdot2^5 + 1\cdot2^4 + 0\cdot2^3 + 1\cdot2^2 + 0\cdot2^1 + 1\cdot2^0$

Then, to find the base $2$ representation of a number we can iteratively do integer division by two and keep track fo the residues. Let's see and example with the number $53$:

$$
\begin{aligned}
53 &= 2 \cdot 26 + \textcolor{red}{1} \\
26 &= 2 \cdot 13 + \textcolor{red}{0} \\
13 &= 2 \cdot 6  + \textcolor{red}{1} \\
6  &= 2 \cdot 3  + \textcolor{red}{0} \\
3  &= 2 \cdot 1  + \textcolor{red}{1} \\
1  &= 2 \cdot 0  + \textcolor{red}{1}
\end{aligned}
$$

Then, $53$ in base $2$ is $110101$. This algorithm works not only for base $2$ but also for every other base:

```py
def dec2base(n: int, base: int) -> str:
    """
    Return a string representation of a number in a specific base
    """
    new_num = ""
    while n != 0:
        new_num = str(n % base) + new_num
        n //= base

    return new_num
```

We can add this function to our [`utils.py`](../utils/utils.py)

## Solution 1

We can just iterate through all numbers and if a number is a palindrome in both base $10$ and base $2$. But before that, notice that every number in base $2$ has to start with a $1$ (otherwise we'd have leading zeroes), which means that the last number of a palindrome in base $2$ is also $1$. All numbers in base $2$ that end in $1$ are odd numbers, so we only need to check for odd numbers here.

```py
from utils import is_palindrome

def solution_1(limit: int) -> int:
    total = 0

    for n in range(1, limit + 1, 2):
        if is_palindrome(n):
            if is_palindrome(dec2base(n, 2)):
                total += n

    return total
```

# Helpful Links

- [Base $2$](https://en.wikipedia.org/wiki/Binary_number)
