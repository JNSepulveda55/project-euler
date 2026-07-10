# Pandigital Multiples
### Problem 0038

Take the number $192$ and multiply it by each of $1$, $2$, and $3$:

$$\begin{align*}
192 \times 1 &= 192\\
192 \times 2 &= 384\\
192 \times 3 &= 576
\end{align*}$$

By concatenating each product we get the $1$ to $9$ pandigital, $192384576$. We will call $192384576$ the concatenated product of $192$ and $(1,2,3)$.

The same can be achieved by starting with $9$ and multiplying by $1$, $2$, $3$, $4$, and $5$, giving the pandigital, $918273645$, which is the concatenated product of $9$ and $(1,2,3,4,5)$.

What is the largest $1$ to $9$ pandigital $9$-digit number that can be formed as the concatenated product of an integer with $(1,2, \dots, n)$ where $n \gt 1$?


# Solutions

## Solution 1

The restriction $n>1$ is the same as saying $n\ge2$, which means we'll be using at least two numbers, and since we only have a budget of nine digits one of them will have to be $4$ digits long and the other $5$ digits long.

So we only need to check numbers up to 4 digits long. We can just store their digits and generate multiples until we have 9 total digits or more. Then check if the number is pandigital. Do that for all numbers and keep track of the largest pandigital found this way.

Our solution looks like this:

```py
def solution_1() -> int:
    largest = 0

    for i in range(10**4):  # Check numbers up to 4 digits long
        mult = 2
        digits = str(i)  # Store digits
        while len(digits) < 9:
            digits += str(mult * i)  # Find next multiple and concatenate it
            mult += 1

        if len(digits) == 9 and set(digits) == set("123456789"):  # If its pandigital
            if int(digits) > largest:  # If its the largest, update
                largest = int(digits)
            
    return largest
```
