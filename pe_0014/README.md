# Longest Collatz Sequence
### Problem 0014

The following iterative sequence is defined for the set of positive integers:

- $n \to \frac{n}{2}$ ($n$ is even)

- $n \to 3n + 1$ ($n$ is odd)

Using the rule above and starting with $13$, we generate the following sequence:
$$13 \to 40 \to 20 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1.$$

It can be seen that this sequence (starting at $13$ and finishing at $1$) contains $10$ terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at $1$.

Which starting number, under one million, produces the longest chain?

<b>NOTE:</b> Once the chain starts the terms are allowed to go above one million.

# Solutions

## Solution 1

We can brute force this problem. We can just check the sequence of every number starting with the largest numbers and going in reverse.

We can skip any number in the chain of the biggest number since we know that its chain will be shorter.

```py
def solution_1(limit: int) -> int:
    # Variables to keep track
    best_number = 0
    best_length = 0
    visited = set()

    # Check elements in reverse
    for i in range(limit - 1, 0, -1):
        if i in visited:
            continue

        # Calculate sequence for each number and store visited numbers
        seq_len = 1
        n = i  # Copy the number
        while n != 1:  # Assuming all numbers end in 1
            if n%2 == 0:
                n //= 2
            else:
                n = 3*n + 1

            seq_len += 1
            visited.add(n)

        # Update best number
        if seq_len > best_length:
            best_length = seq_len
            best_number = i
        

    return best_number
```


# Helpful Links

- [Collatz sequence](https://en.wikipedia.org/wiki/Collatz_conjecture)
