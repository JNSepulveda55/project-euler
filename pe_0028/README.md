# Number Spiral Diagonals
### Problem 0028

Starting with the number $1$ and moving to the right in a clockwise direction a $5$ by $5$ spiral is formed as follows:

```
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
```
It can be verified that the sum of the numbers on the diagonals is $101$.

What is the sum of the numbers on the diagonals in a $1001$ by $1001$ spiral formed in the same way?

# Solutions

## Solution 1

We can solve this problem by simply finding a general solution and applying it to the case of $n = 1001$.

Assume a square spiral of size $n\times n$ where $n$ is odd. Since there are $n^2$ numbers in the grid, and we know that the spiral always ends at the top-right corner, then we know that the number at the top-right corner is just $n^2$.

In general, since layers are added on top of existing ones, then every element in the top-right diagonal (starting at $1$ and ending with $n^2$) has the square of every odd number up to $n$.

The top-left diagonal is always $n-1$ less than the top-right one, so $n^2 - (n-1) = n^2 - n + 1$

For the other diagonals we can do a similar analysis:

- Bottom-left is $n-1$ less than top-left, so its the number $n^2 - n + 1 - (n-1) = n^2 - 2n + 2$
- Bottom-right is $n-1$ less than bottom-left, so its the number $n^2 - 2n + 2 - (n-1) = n^2 - 3n + 3$



In the end, the sum of the diagonals is:

$$\sum_{i = 1,\ i\ \text{is odd}}^n i^2\ \ \ \  + \sum_{i = 1,\ i\ \text{is odd}}^n i^2 - i + 1\ \ \ \  + \sum_{i = 1,\ i\ \text{is odd}}^n i^2 - 2i + 2\ \ \ \  + \sum_{i = 1,\ i\ \text{is odd}}^n i^2 - 3i + 3$$

Which can be reduced to:

$$\sum_{i = 1,\ i\ \text{is odd}}^n i^2 + i^2 - i + 1 + i^2 - 2i + 2 + i^2 - 3i + 3$$


$$= \sum_{i = 1,\ i\ \text{is odd}}^n 4i^2 - 6i + 6$$


With this, we can implement a simple pytho script that will give us the answer.

An important detail is that, since we're adding up the numbers on each of the four diagonals starting from the center, the number $1$ in the middle of the square is being counted four times. This is easily solvable by subtracting $3$ from the final result:

```py
def solution_1(n: int) -> int:
    total = 0
    for i in range(1, n+1, 2):
        total += 4*i**2 - 6*i + 6

    return total - 3
```

## Solution 2

If you're interested in taking the mathematical analysis route all the way, you're welcome to keep reading!

Starting from this:
$$= \sum_{i = 1,\ i\ \text{is odd}}^n 4i^2 - 6i + 6$$

We can reduce it as such:

$$= \sum_{i = 1}^n 4i^2 - 6i + 6\ \ \ \  - \sum_{i = 1,\ i\ \text{is even}}^n 4i^2 - 6i + 6$$

$$= \sum_{i = 1}^n 4i^2 - 6i + 6\ \ \ \  - \ \ \ \ \sum_{j = 1}^{\frac{n-1}{2}} 4(2j)^2 - 6(2j) + 6$$

$$= 4\sum_{i = 1}^n i^2\ - 6\sum_{i = 1}^n i\ \ + 6\sum_{i = 1}^n 1\ - 16\sum_{j = 1}^{\frac{n-1}{2}} j^2\ + 12\sum_{j = 1}^{\frac{n-1}{2}} j\ \ - 6\sum_{j = 1}^{\frac{n-1}{2}} 1\ $$

$$= 4 \frac{n(n+1)(2n+1)}{6} - 6\frac{n(n+1)}{2} + 6n - 16\frac{\frac{n-1}{2}(\frac{n-1}{2} + 1)(2\frac{n-1}{2} + 1)}{6} + 12\frac{\frac{n-1}{2}(\frac{n-1}{2}+1)}{2} - 6\frac{n-1}{2}$$

$$= 2 \frac{n(n+1)(2n+1)}{3} - 3n(n+1) + 6n - 8\frac{\frac{n-1}{2}(\frac{n+1}{2})n}{3} + 6\left(\frac{n-1}{2}\right)\left(\frac{n+1}{2}\right) - 3(n-1)$$

$$= 2 \frac{n(n+1)(2n+1)}{3} - 3n(n+1) + 6n - 2\frac{(n-1)(n+1)n}{3} + 3\frac{(n-1)(n+1)}{2} - 3(n-1)$$

$$= \frac{2}{3}(2n^3+3n^2 + n) - 3(n^2+n) + 6n - \frac{2}{3}(n^3-n) + \frac{3}{2}(n^2-1) - 3n + 3$$

$$= \frac{4}{3}n^3 + 2n^2 + \frac{2}{3}n - 3n^2 - 3n +6n - \frac{2}{3}n^3+\frac{2}{3}n+\frac{3}{2}n^2 - \frac{3}{2}-3n+3$$

$$= \frac{2}{3}n^3 + \frac{1}{2}n^2 + \frac{4}{3}n + \frac{3}{2}$$

$$= \frac{4n^3 + 3n^2 + 8n + 9}{6}$$

Applying the correction to only count the center $1$ once, the final formula is:

$$= \frac{4n^3 + 3n^2 + 8n + 9}{6} - 3$$

$$= \frac{4n^3 + 3n^2 + 8n + 9 - 18}{6}$$

$$= \frac{4n^3 + 3n^2 + 8n -9}{6}$$

To solve our problem, we can just replace $n$ by $1001$ on this formula.

# Helpful Links

- [Sum of $n$ and $n^2$](https://brilliant.org/wiki/sum-of-n-n2-or-n3/)
