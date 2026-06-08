# Reciprocal Cycles
### Problem 0026

A unit fraction contains $1$ in the numerator. The decimal representation of the unit fractions with denominators $2$ to $10$ are given:

$$\begin{align*}
1/2 &= 0.5\\
1/3 &=0.(3)\\
1/4 &=0.25\\
1/5 &= 0.2\\
1/6 &= 0.1(6)\\
1/7 &= 0.(142857)\\
1/8 &= 0.125\\
1/9 &= 0.(1)\\
1/10 &= 0.1
\end{align*}$$

Where $0.1(6)$ means $0.166666\cdots$, and has a $1$-digit recurring cycle. It can be seen that $1/7$ has a $6$-digit recurring cycle.

Find the value of $d \lt 1000$ for which $1/d$ contains the longest recurring cycle in its decimal fraction part.

# Notes

- Add examples from the prompt here.
- Add any observations or math shortcuts here.

# Solutions

## Solution 1

To solve this problem, we can just use the classic division algorithm to find the period of each decimal: We take the integer part of the division, add a zero to the remainder and keep dividing until the remainder repeats or the remainder is zero.

Let's code a function to find the length of the period for $\frac{1}{d}$ for a given number $d$

```py
def find_period_length(d: int) -> int:
    remainders = []  # We'll store the reaminders here
    remainder = 1  # Initialize remainder

    while True:
        remainder = remainder % d

        # If there is no remainder, the decimal is not periodic. Return 0
        if remainder == 0:
            return 0
        
        # If we already got that remainder, the cycle closed. Return length
        elif remainder in remainders:
            return len(remainders) - remainders.index(remainder)

        # Else, add a zero and continue the cycle
        else:
            remainders.append(remainder)
            remainder *= 10  # Add a zero
```

Now, we can just calculate it for all numbers under the limit and find the one with the longest period:

```py
def solution_1(limit: int) -> int:
    longest_period = 0
    best_number = 0

    for i in range(1, limit):
        period_length = find_period_length(i)

        if period_length > longest_period:  # Update the best guess
            longest_period = period_length
            best_number = i

    return best_number
```

# Helpful Links

- [Division algorithm](https://math.libretexts.org/Bookshelves/Combinatorics_and_Discrete_Mathematics/A_Spiral_Workbook_for_Discrete_Mathematics_(Kwong)/05%3A_Basic_Number_Theory/5.02%3A_Division_Algorithm)
