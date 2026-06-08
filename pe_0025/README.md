# $1000$-digit Fibonacci Number
### Problem 0025

The Fibonacci sequence is defined by the recurrence relation:

$F_n = F_{n - 1} + F_{n - 2}$, where $F_1 = 1$ and $F_2 = 1$.

Hence the first $12$ terms will be:

$$\begin{align*}
F_1 &= 1\\
F_2 &= 1\\
F_3 &= 2\\
F_4 &= 3\\
F_5 &= 5\\
F_6 &= 8\\
F_7 &= 13\\
F_8 &= 21\\
F_9 &= 34\\
F_{10} &= 55\\
F_{11} &= 89\\
F_{12} &= 144
\end{align*}$$

The $12$-th term, $F_{12}$, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain $1000$ digits?

# Solutions

## Solution 1

This is another easy problem to solve by brute force. We'll reuse code from [problem 2](../pe_0002/README.md).

```py
def solution_1(digits: int) -> int:
    total = 0
    prev_fib = 1
    curr_fib = 1
    idx = 2

    # 10**(digits-1) is the first number with that amount of digits
    while curr_fib < 10**(digits-1):
        if curr_fib % 2 == 0:
            total += curr_fib

        # Store current value in a temp variable
        temp = curr_fib
        
        # Update Fib number
        curr_fib = curr_fib + prev_fib
        
        # Update the previous Fib
        prev_fib = temp
        idx += 1

    return idx
```

And that's it!

# Helpful Links

- [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence)
