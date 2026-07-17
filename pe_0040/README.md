# Champernowne's Constant
### Problem 0040

An irrational decimal fraction is created by concatenating the positive integers:
$$0.12345678910{\color{red}\mathbf 1}112131415161718192021\cdots$$

It can be seen that the $12$<sup>th</sup> digit of the fractional part is $1$.

If $d_n$ represents the $n$<sup>th</sup> digit of the fractional part, find the value of the following expression.
$$d_1 \times d_{10} \times d_{100} \times d_{1000} \times d_{10000} \times d_{100000} \times d_{1000000}$$


## Solution 1

For this problem we can just have a string where we append the numbers in order until we hit million digits. Then, its a simple product.

```py
def solution_1(limit: int = 1_000_000) -> int:

    # Build champernowne's constant until a million digits
    champernowne = ""
    i = 1
    while len(champernowne) < limit:
        champernowne += str(i)
        i += 1

    # Find the product of the digits
    prod = 1
    for exp in range(len(str(limit))):
        prod *= int(champernowne[10**exp-1])

    return prod
```

# Helpful Links

- [Champernowne's constant](https://en.wikipedia.org/wiki/Champernowne_constant)
