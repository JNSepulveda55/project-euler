# Multiples of 3 or 5
### Problem 1

If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3$, $5$, $6$ and $9$. The sum of these multiples is 23.

Find the sum of all the multiples of $3$ or $5$ below $1000$.

# Notes

- Refer first to [Problem 6](../pe_0006/README.md) if you want a similar problem

# Solutions

## Solution 1:

The easiest way to solve this problem is to translate to code what the problem is asking us to do:

***multiples of $3$:*** `if number % 3 == 0`

***or $5$:*** `or number % 5 == 0`

***below $1000$:*** `for number in range(1, n)`

***Find the sum:*** `multiples_sum = 0`, `multiples_sum += number`

With this, we iterate over all (natural) numbers under $1000$ and add them to the sum if they are
either multiples of $3$ (divisible by $3$) or multiples of $5$ (divisible by $5$).

```py
# Solution 1

def solution_1(limit: int) -> int:

    multiples_sum = 0
    for number in range(1, limit):
        if number % 3 == 0 or number % 5 == 0:
            multiples_sum += number

    return multiples_sum
```

## Solution 2:

Let's take a look at the sum of the multiples of $3$ under $1000$:

Let $S_n$ denote the sum of the multiples of $n$ below a thousand. Then, 

$S_3 = 3 + 6 + 9 + 12 + 15 + 18 + ... + 990 + 993 + 996 + 999$

Note that:

$S_3 = 3 \left(1 + 2 + 3 + 4 + 5 + 6 + ... + 330 + 331 + 332 + 333   \right) = 3\sum_{i = 1}^{333}{i}$

And following a similar procedure, 

$S_5 = 5 \left(1 + 2 + 3 + 4 + 5 + 6 + ... + 196 + 197 + 198 + 199   \right) = 5\sum_{i = 1}^{199}{i}$

Where the 333 and 199 are obtained like this:



$\lfloor \frac{1000 - 1}{3}\rfloor = 333$ and $\lfloor \frac{1000 - 1}{5}\rfloor = 199$

Using the formula for the sum of the first n natural numbers we get:

$S_3 = 3\frac{(333)(334)}{2} $ and $S_5 = \sum_{i = 1}^{199}{i} = 3\frac{(199)(200)}{2}$.

If we are not cautious, it is easy to think that since we need the sum of the multiples of three or five,
that the answer is just $S_3 + S_5$. However, this would be a mistake because we would be including some
numbers twice, namely, the multiples of 15.

Its easy to see this if we use set theory:

$\sum{A} + \sum{B} = \sum{A\cup B} + \sum{A\cap B}$

From which we get:

$\sum{A\cup B} = \sum{A} + \sum{B} - \sum{A\cap B}$

So, 

$Solution = S_3 + S_5 - S_{15}$

Which corresponds to the return statement in the function `solution_2`:

 `return S(3) + S(5) - S(15)`.

```py
# Solution 2

def solution_2(limit: int) -> int:

    def sum_first_n(n:int) -> int:
        return n*(n+1)//2
    
    def S(n: int) -> int:
        return n * sum_first_n((limit-1)//n) 

    return S(3) + S(5) - S(15)
```

 # Helpful Links

 - [Sum of the first $n$ numbers](https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_⋯)
