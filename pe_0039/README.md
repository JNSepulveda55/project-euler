# Integer Right Triangles
### Problem 0039

If $p$ is the perimeter of a right angle triangle with integral length sides, $\{a, b, c\}$, there are exactly three solutions for $p = 120$.

$\{20,48,52\}$, $\{24,45,51\}$, $\{30,40,50\}$

For which value of $p \le 1000$, is the number of solutions maximised?

# Notes

- A pythagorean triplet is a 3-tuple ${a, b, c}$ such that $a^2 + b^2 = c^2$

# Solutions

With just a little algebraic manipulation of the contraints given in the problem, we can find a formula to check if a solution exists given $p$ and $a$.


## Solution 1

We know that $a^2 + b^2 = c^2\ \ \ (1)$. Additionally, we have the constraint $a + b + c = p\ \ \ (2)$. From this second equation we can get that $c = p - (a + b)$. Replacing in $(1)$, we get the following:

$$\begin{align*}
c^2 &= a^2 + b^2  \\
(p-(a+b))^2 &= a^2 + b^2\\
p^2 - 2p(a+b) + a^2 + 2ab + b^2 &= a^2 + b^2\\
p^2 - 2p(a+b) + 2ab &= 0\\
2ab - 2pb &= 2pa - p^2\\
2b(a-p) &= p(2a - p)\\
\end{align*}$$

Then, $b = \frac{p(p-2a)}{2(p-a)}$, and since this equation comes from $(1)$ and $(2)$, then as long as b is an integer, we know that ${a, b, p-(a+b)}$ is a pythagorean triplet.


The code for our solution is just:


```py
def solution_1(limit: int) -> int:
    # Initialize variables
    max_num_sols = 0
    best_p = 0
    
    for p in range(1, limit):
        num_sols = 0

        # Assuming a <= b < c, we only need to check up to p/3
        for a in range(1, p//3+1):    
            # Simple check derived from formula    
            if p*(p-2*a) % (2*(p-a)) == 0:
                num_sols += 1

        # Update best solution
        if num_sols > max_num_sols:
            max_num_sols = num_sols
            best_p = p

    return best_p
```


# Helpful Links

- [Pythagorean theorem](https://en.wikipedia.org/wiki/Pythagorean_theorem)
