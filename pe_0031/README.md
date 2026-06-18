# Coin Sums
### Problem 0031

In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

<blockquote>1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).</blockquote>

It is possible to make £2 in the following way:

<blockquote>1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p</blockquote>

How many different ways can £2 be made using any number of coins?


# Solutions

## Solution 1

We can't solve this problem by directly attempting to compute all the different ways of making £2 with the coins given. Instead, let's try to be clever about it. 

We can try to solve a similar but much smaller problem: In how many ways can we make 10p with 1p, 2p and 5p coins?

For this, we can store in a list the number of ways of making each of the values from 0p to 10p with the available coins. The initial state of the list would be this:

```text

 0p  1p  2p  3p  4p  5p  6p  7p  8p  9p  10p
+---+---+---+---+---+---+---+---+---+---+---+
| 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
+---+---+---+---+---+---+---+---+---+---+---+
```

Number `0` isn't important for this problem but adding it will help making indexing easier. We add a $1$ in the zeroth spot since there is exactly one way of making zero with any number of coins, which is using no coins.

We can start with the 1p coin: There is only one way of getting each number using only 1p coins, so we fill the table with ones (except for `0p`):

```text

 0p  1p  2p  3p  4p  5p  6p  7p  8p  9p  10p
+---+---+---+---+---+---+---+---+---+---+---+
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
+---+---+---+---+---+---+---+---+---+---+---+
```

Next is the `2p` coin. Numbers will be updated by adding to the current square the number $v$ positions before in the table, where $v$ is the value of the coin (in this case $2$).

This is because a number $n$ can be expressed in $f(n-v) + f(n)$ ways using coins of value $v$, with $f(\cdot)$ represents the number of ways a quantity can be represented. It is important to note that this only works if $f(n-v)$ already counts using the $v$-valued coin.

In other words, a quantity can be represented in as many ways as it could be represented without the new coin **plus** the amount of ways we can represent a number that is exactly the value of the coin away from our current value.

Example: The quantity `3p` can be represented using either three `1p` coins or one `1p` and one `2p` coin. The quantity `5p` can b represented by using only `1p` coins **plus** however many ways we can represent the quantity `3p` (since we can just add a `2p` to each of them and get `5p`).

Let's see the steps in order. We add $1$ to the `2p` square:

```text

 0p  1p  2p  3p  4p  5p  6p  7p  8p  9p  10p
+---+---+---+---+---+---+---+---+---+---+---+
| 1 | 1 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
+---+---+---+---+---+---+---+---+---+---+---+
```

Then, we add $1$ to the `3p` square since its the value in the `1p` square.

```text

 0p  1p  2p  3p  4p  5p  6p  7p  8p  9p  10p
+---+---+---+---+---+---+---+---+---+---+---+
| 1 | 1 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
+---+---+---+---+---+---+---+---+---+---+---+
```

We now add $2$ to the `4p` square:

```text

 0p  1p  2p  3p  4p  5p  6p  7p  8p  9p  10p
+---+---+---+---+---+---+---+---+---+---+---+
| 1 | 1 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 |
+---+---+---+---+---+---+---+---+---+---+---+
```

We also add $2$ to the `5p` square:

```text

 0p  1p  2p  3p  4p  5p  6p  7p  8p  9p  10p
+---+---+---+---+---+---+---+---+---+---+---+
| 1 | 1 | 2 | 2 | 3 | 3 | 1 | 1 | 1 | 1 | 1 |
+---+---+---+---+---+---+---+---+---+---+---+
```

If we keep doing this, the end result is:

```text

 0p  1p  2p  3p  4p  5p  6p  7p  8p  9p  10p
+---+---+---+---+---+---+---+---+---+---+---+
| 1 | 1 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 5 | 6 |
+---+---+---+---+---+---+---+---+---+---+---+
```

We can now do the same with the `5p` coins, for which we get:

```text

 0p  1p  2p  3p  4p  5p  6p  7p  8p  9p  10p
+---+---+---+---+---+---+---+---+---+---+---+
| 1 | 1 | 2 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 10 |
+---+---+---+---+---+---+---+---+---+---+---+
```

Now, we can implement this in code in te following way:


```py
def solution_1(target: int, coins: list) -> int:
    values = [1] + [0] * target  # Initialize initial value list
    
    # Loop over every coin
    for v in coins:
        # Loop over the list starting at v
        for i in range(v, target+1):
            values[i] = values[i] + values[i-v]

    return values[-1]  # Return last element
```


# Helpful Links

- [Dynamic Programming coin change problem](https://www.geeksforgeeks.org/dsa/understanding-the-coin-change-problem-with-dynamic-programming/)
