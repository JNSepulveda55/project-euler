# Smallest Multiple
### Problem 0005

$2520$ is the smallest number that can be divided by each of the numbers from $1$ to $10$ without any remainder.

What is the smallest positive number that is <strong>evenly divisible</strong> by all of the numbers from $1$ to $20$?

# Notes

- **Evenly divisible:** divisible with no remainder

# Solutions

In other words, we're being asked what's the minumum common multiple of all numbers $1$ through $20$.

A naïve first approach would be to just multiply all numbers 1 to 20 together, but this won't be the right answer, which we can easily illustrate with an example:

$1 \cdot 2 \cdot 3 \cdot 4 = 24$, but the smallest number evenly divisible by the numbers $1, 2, 3$ and $4$. This is because 4 is already a multiple of 2, so we do not need to multiply by 2 and 4, just by 4.

## Solution 1

In order to detect this systematically, we can keep track of the highest exponent in the prime factorization of the numbers in order. So in the case of $n = 10$, it would look like this:

Call $S$ the solution. We initialize $S = 1$.

$1 = \textcolor{red}{1} \to S = \textcolor{red}{1}$

$2 = \textcolor{red}{2} \to S = \textcolor{red}{2}$

$3 = \textcolor{red}{3} \to S = 2 \cdot \textcolor{red}{3}$

$4 = \textcolor{red}{2^2} \to S = \textcolor{red}{2^2} \cdot 3$

$5 = \textcolor{red}{5} \to S = 2^2 \cdot 3 \cdot \textcolor{red}{5}$

$6 = 2 \cdot 3 \to S = 2^2 \cdot 3 \cdot 5$

$7 = \textcolor{red}{7} \to S = 2^2 \cdot 3 \cdot 5 \cdot \textcolor{red}{7}$

$8 = \textcolor{red}{2^3} \to S = \textcolor{red}{2^3} \cdot 3 \cdot 5 \cdot 7$

$9 = \textcolor{red}{3^2} \to S = 2^3 \cdot \textcolor{red}{3^2} \cdot 5 \cdot 7$

$10 = 2 \cdot 5 \to S = 2^3 \cdot 3^2 \cdot 5 \cdot 7$

Then, $S = 2^3 \cdot 3^2 \cdot 5 \cdot 7 = 2520$, like stated in the example. We can keep doing this with the numbers 11 - 20 like this:

$11 = \textcolor{red}{11} \to S = 2^3 \cdot 3^2 \cdot 5 \cdot 7 \cdot \textcolor{red}{11}$

$12 = 2^2 \cdot 3 \to S = 2^3 \cdot 3^2 \cdot 5 \cdot 7 \cdot 11$

$13 = \textcolor{red}{13} \to S = 2^3 \cdot 3^2 \cdot 5 \cdot 7 \cdot 11 \cdot \textcolor{red}{13}$

$14 = 2 \cdot 7 \to S = 2^3 \cdot 3^2 \cdot 5 \cdot 7 \cdot 11 \cdot 13$

$15 = 3 \cdot 5 \to S = 2^3 \cdot 3^2 \cdot 5 \cdot 7 \cdot 11 \cdot 13$

$16 = \textcolor{red}{2^4} \to S = \textcolor{red}{2^4} \cdot 3^2 \cdot 5 \cdot 7 \cdot 11 \cdot 13$

$17 = \textcolor{red}{17} \to S = 2^4 \cdot 3^2 \cdot 5 \cdot 7 \cdot 11 \cdot 13 \cdot \textcolor{red}{17}$

$18 = 2 \cdot 3^2 \to S = 2^4 \cdot 3^2 \cdot 5 \cdot 7 \cdot 11 \cdot 13 \cdot 17$

$19 = \textcolor{red}{19} \to S = 2^4 \cdot 3^2 \cdot 5 \cdot 7 \cdot 11 \cdot 13 \cdot 17 \cdot \textcolor{red}{19}$

$20 = 2^2 \cdot 5 \to S = 2^4 \cdot 3^2 \cdot 5 \cdot 7 \cdot 11 \cdot 13 \cdot 17 \cdot 19$

Finally, our solution is $S = 2^4 \cdot 3^2 \cdot 5 \cdot 7 \cdot 11 \cdot 13 \cdot 17 \cdot 19 = 232792560$

## Solution 2

The last solution gave us an interesting insight: The solution is just the product of every prime lower than $n$ to its highest power that is also smaller than $n$. See the breakdown:

$2^4 = 16 \leq 20$ but $2^5 = 32 > 20$

$3^2 = 9 \leq 20$ but $3^3 = 27 > 20$

$5 \leq 20$ but $5^2 = 25 > 20$

Ans so on ...

We can easily translate this to code by finding all prime numbers smaller than $n$ and keep track of their highest power lower than $n$.

```py
def solution_2(limit: int) -> int:
    prime_powers = []
    result = 1

    # Iterate over all numbers less than limit
    for i in range(1, limit+1):

        # If prime, find greatest power under limit
        if is_prime(i):
            max_pow = 1
            curr_num = i

            while curr_num * i <= limit:
                curr_num *= i
                max_pow += 1
            
            result *= curr_num

    return result
```

# Helpful Links

- [Fundamental theorem of arithmetic](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic)

