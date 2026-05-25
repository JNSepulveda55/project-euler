# Largest Palindrome Product
### Problem 0004

A palindromic number reads the same both ways. The largest palindrome made from the product of two $2$-digit numbers is $9009 = 91 \times 99$.

Find the largest palindrome made from the product of two $3$-digit numbers.

# Solutions

This is a very straightforward problem. 

The first thing we need to know is what a palindrome is.

> A palindrome number is a number that when written down in a valid form, its digits read the same left-to-right (l2r) and right-to-left (r2l).

E.g $123321$ is a palindrome, but $123421$ is not since the it doesn't read the same *l2r* and *r2l*. $09877890$ is not a palindrome either since its not written in a valid form. 

We want to find the two three-digit numbers whose product is the biggest palindrome. Since there are only 900 3-digit numbers, the maximum number of iterations we'll need to do is $900^2 = 810000$ iterations which is very manageable for a computer.

We can design a very simple `is_palindrome()` function in python like this:


```py
def is_palindrome(n: int) -> bool:
    """Returns True if the number reads the same l2r and r2l"""
    return str(n) == str(n)[::-1] 
```

## Solution 1

With this, we can implement a simple function that checks for the the biggest palindromic product of two three-digit numbers:

```py
def solution_1(digits: int) -> int:
    largest = 0
    for a in range(10**(digits-1), 10**digits):
        for b in range(10**(digits-1), 10**digits):
            product = a*b
            if is_palindrome(product) and product > largest:
                largest = product

    return largest
```
Its left as an excercise for the reader to think about why we use `10**(digits-1)` and `10**digits` 

# Helpful Links

- [Palindromic Number](https://en.wikipedia.org/wiki/Palindromic_number)
