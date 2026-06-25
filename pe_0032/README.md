# Pandigital Products
### Problem 0032

We shall say that an $n$-digit number is pandigital if it makes use of all the digits $1$ to $n$ exactly once; for example, the $5$-digit number, $15234$, is $1$ through $5$ pandigital.

The product $7254$ is unusual, as the identity, $39 \times 186 = 7254$, containing multiplicand, multiplier, and product is $1$ through $9$ pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a $1$ through $9$ pandigital.

<div>HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.</div>

# Solutions

We'll solve this by brute-force. However, we can make our like easier by noting the following:

1. We need to use all digits $1$ through $9$. This means we have a max of 10 digits.
2. If $a$ is a number with $d_a$ digits and $b$ is a number with $d_b$ digits, then $a \times b$ has at least $d_a + d_b - 1$ digits and at most $d_a + d_b$ digits.

Let's call $a \times b = c$, with $d_c$ being the number of digits of $c$. For this problem we also have that $d_a + d_b + d_c = 9$

Assuming that $d_a \le d_b$, then the only triplets $(d_a, d_b, d_c)$ that follow all constraints are $(1, 4, 4)$ and $(2, 3, 4)$.

We can find them by hand, or just use this small scrip to print them:

```python
for da in range(1, 10):
    for db in range(da, 10):
        dc = 9 - da - db
        if da + db - 1 <= dc <= da + db:
            print(f"({da}, {db}, {dc})")
```

Then we know that a is $a$ one-digit or two-digit number, and $b$ is a three-digit or four-digit number.

## Solution 1

We can solve the problem using brute-force like this:

```py
def solution_1() -> int:
    solutions = set()  # Store in a set so that we only count once
    for a in range(100):
        for b in range(100, 10000):
            c = a * b
            # Join the digits of the numbers in a string
            digits = str(a) + str(b) + str(c)
            if set(digits) == set("123456789") and len(digits) == 9:
                solutions.add(c)
    
    return sum(solutions)
```