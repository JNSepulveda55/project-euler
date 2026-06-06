# Number Letter Counts
### Problem 0017

If the numbers $1$ to $5$ are written out in words: one, two, three, four, five, then there are $3 + 3 + 5 + 4 + 4 = 19$ letters used in total.

If all the numbers from $1$ to $1000$ (one thousand) inclusive were written out in words, how many letters would be used?

<br>

<b>NOTE:</b> Do not count spaces or hyphens. For example, $342$ (three hundred and forty-two) contains $23$ letters and $115$ (one hundred and fifteen) contains $20$ letters. The use of "and" when writing out numbers is in compliance with British usage.

# Notes

When I first attempted this problem, I wrote $40$ as *fo****u****rty* instead of *forty*. Don't be like me :)

# Solutions

## Solution 1

This will be a nice problem to solve by hand :)

Let's start with the numbers from $1$ to $9$:

- `one` -> $3$
- `two` -> $3$
- `three` -> $5$
- `four` -> $4$
- `five` -> $4$
- `six` -> $3$
- `seven` -> $5$
- `eight` -> $5$
- `nine` -> $4$

Total: $36$

Now, the *teens* are special, so we'll count them separately as well:

- `ten` -> $3$
- `eleven` -> $6$
- `twelve` -> $6$
- `thirteen` -> $8$
- `fourteen` -> $8$
- `fifteen` -> $7$
- `sixteen` -> $7$
- `seventeen` -> $9$
- `eighteen` -> $8$
- `nineteen` -> $8$

Total: $70$

Now let's do the tenths from $20$ to $90$

- `twenty` -> $6$
- `thirty` -> $6$
- `forty` -> $5$
- `fifty` -> $5$
- `sixty` -> $5$
- `seventy` -> $7$
- `eighty` -> $6$
- `ninety` -> $6$

Total: $46$

With this, we can calculate the number of letters needed from $1$ to $99$, which would be:

```
Number of letters from 1 to 9
            +
Number of letters from 10 to 19
            +
10 * tenths, because each tenth is counted 10 times
            +
8 * (1 to 9), because each number appears once for each tenth
```
Total $=$ `1-9` + `10-19` + $10 \times \text{tenths}$  + $8 \times$ `1-9` = $36 + 70 + 10 \times 46 + 8 \times 36 = 854$

Finally, note that the word `hundred` has $7$ letters, the word `and` has $3$ letters and the number `one thousand` is spelled with $11$ letters.

Following a similar logic as the last step,  our final result would be as follows:

```
Numbers from 1 to 99
            +
100 * 9 * Letters in 'hundred'
            +
100 * Numbers from 1 to 9
            +
99 * 9 * Letters in 'and'
            +
9 * Numbers from 1 to 99
            +
Letters in 'one thousand'
```

Total $= 854\ +\ 100 \times 9 \times 7\ +\ 100 \times 36\ +\ 99 \times 9 \times 3\ +\ 9 \times 854\ +\ 11 = 21124$

Just for the sake of consistency, here's what the solution in code would look like:

```py
@timer
def solution_1() -> int:
    return 21124
```

# Helpful Links

- [How to spell the number $40$](https://www.merriam-webster.com/grammar/is-it-forty-or-fourty)
