# Sum Square Difference
### Problem 0006

The sum of the squares of the first ten natural numbers is,

$$1^2 + 2^2 + ... + 10^2 = 385.$$

The square of the sum of the first ten natural numbers is,

$$(1 + 2 + ... + 10)^2 = 55^2 = 3025.$$

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# Notes

- Refer first to [Problem 1](../pe_0001/README.md) if you want a similar problem

- There's a heated debate on whether $0$ is a natural number, but for the sake of consistency we'll assume $0$ is in fact not a natural number.

# Solutions

## Solution 1

We'll make use of *well-known* mathematical formulas to solve this problem in a very straightforward way. Feel free to implement the brute-force solution for some practice. 

We know from **Problem 1** that the sum of the first $n$  numbers is given by the following formula: $\sum_{i=1}^n i = \frac{n(n+1)}{2}$. 

Then, the square of the sum of the first $n$ numbers is $\left(\sum_{i=1}^n i\right)^2 = \left(\frac{n(n+1)}{2}\right)^2 = \frac{n^2(n+1)^2}{4}$

Now, we can also use the fact that the formula for the sum of the first $n$ square numbers, which is as follows: $\sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6}$

Finally, we can combine these two formulas to find the solution for our problem:

$$\left(\sum_{i=1}^n i\right)^2 - \sum_{i=1}^n i^2 = \frac{n^2(n+1)^2}{4} - \frac{n(n+1)(2n+1)}{6}$$



```py
def solution_1(n: int) -> int:
    return (n**2 * (n+1)**2)//4 - (n*(n+1)*(2*n+1))//6
```


# Helpful Links

 - [Sum of the first $n$ numbers](https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_⋯)

 - [Sum of $n$, $n^2$ and $n^3$](https://brilliant.org/wiki/sum-of-n-n2-or-n3/)
