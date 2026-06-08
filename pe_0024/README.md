# Lexicographic Permutations
### Problem 0024

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# Solutions

Let's do some analysis:

For any $n$ distinct objects, there are $n!$ possible permutations of those objects. This means that there are $10! = 3,628,800$ possible permutations of the ten digits. This means that for every digit, $\frac{10!}{10} = 9! = 362,880$ start with that digit.

So, in lexicographic order, the first permutation starting with a 1 is number $362,881$, as all others before that start with a zero.

Similarly, the first one starting with a two is number $725,761$, and the first one starting with a three is number $1,088,641$, which is more than $1,000,000$.

So, we know that the first digit of the millionth lexicographic permutation is a $2$.

If we continue doing this analysis of trial and error calculating the position's lower and upper bounds we will eventually get to the solution, but why not code it? :)

We'll use the `factorial()` function from our [`utils`](../utils/utils.py) file.

## Solution 1

```py
from utils import factorial

def solution_1(position: int) -> int:
    permutation = ""  # This will be our final permutation
    
    # To keep track of remaining digits
    remaining_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # We'll subtract from this as we find digits
    remaining_positions = position - 1  # We start counting at 0

    while len(remaining_digits) > 0:
        # How many permutations start with each of the remaining digits?
        perms_per_digit = factorial(len(remaining_digits) - 1)

        # Get the index of the next digit
        digit_idx = remaining_positions // perms_per_digit

        digit = remaining_digits[digit_idx]  # Next digit in the permutation
        permutation += digit  # Add digit to the permutation
        remaining_digits.remove(digit)       # Remove digit from remaining digits list

        remaining_positions -= perms_per_digit * digit_idx  # Update remaining positions

    return int(permutation)
    
```

# Helpful Links

- [Permutations without repetition](https://www.mathsisfun.com/combinatorics/combinations-permutations.html)
