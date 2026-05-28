# Special Pythagorean Triplet
### Problem 0009

A Pythagorean triplet is a set of three natural numbers, $a \lt b \lt c$, for which,
$$a^2 + b^2 = c^2.$$

For example, $3^2 + 4^2 = 9 + 16 = 25 = 5^2$.

There exists exactly one Pythagorean triplet for which $a + b + c = 1000$.<br>Find the product $abc$.

# Solutions

## Solution 1

We can brute-force this problem by checking every possible $(a, b, c)$ combination.

However, there are some small optimizations that can go a long way.

First, we know that pitagorean triples are related to the sides of a triangle, and in a triangle no side can be longer than the sum of the other two sides. Then:

Since $a + b + c = 1000$, then $c = 1000 - (a + b)$

$$a + b \geq c = 1000 - (a + b)$$
$$2 (a + b) \geq 1000$$
$$ (a + b) \geq 500$$
$$ b \geq 500 - a$$

And without loss of generality, we can assume $b \leq a$. 

Then, 

$$ 500 - a \leq b \leq a$$
$$ 500 - a \leq a$$
$$ 500 \leq 2a$$
$$ 250 \leq a$$

Finally, since $c > a \geq 250$, $c$ is at least 251, which means $a$ is at most $1000 - 251 = 749$

If we say $n = 1000$, we can write our bounds like this:

For a:
$$\frac{n}{4} \leq a \leq n - \frac{n}{4} - 1$$
$$\frac{n}{4} \leq a \leq \frac{3}{4}n - 1$$

For b:

$$\frac{n}{2} - a \leq b \leq a$$

Now we're ready for an *educated* brufe force approach

```py
def solution_1(n: int) -> int:

    for a in range(n//4, (3*n)//4):
        for b in range(n//2 - a, a):
            c = (a**2 + b**2)**0.5
            # Check if c is an integer and a + b + c = n
            if c % 1 == 0 and a + b + int(c) == n:
                return int(a * b * c)
```

# Helpful Links

- [Pythagorean triple](https://en.wikipedia.org/wiki/Pythagorean_triple)
