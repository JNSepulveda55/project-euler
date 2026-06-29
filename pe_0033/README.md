# Digit Cancelling Fractions
### Problem 0033

The fraction $49/98$ is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that $49/98 = 4/8$, which is correct, is obtained by cancelling the $9\text{s}$.

We shall consider fractions like, $30/50 = 3/5$, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.


# Solutions
The first thing we have to notice is that we're dealing with numbers that only have two digits, and we know that the numerator and denominator must share exactly one digit. 

If they shared both digits, the fraction would equal $1$, and if they share no digits then we couldn't cancel the digits.

The other thing we have to notice is that two fractions $\frac{a}{b}$ and $\frac{c}{d}$ are the same if and only if $ad = bc$.

Finally, we need a way to return the fraction in its lowest common terms.

## Solution 1

We can start by finding all digit-cancelling fractions. The code would look like this:

```py
def find_digit_cancelling_fractions() -> tuple[list[int], list[int]]:
    numerators = []
    denominators = []

    for d in range(10, 100):  # Denominator
        str_d = str(d)
        for n in range(10, d):  # Numerator can't be larger than `d`
            str_n = str(n)

            # Check if they share a digit
            if str_d[0] in str_n:
                shared = str_d[0]

            elif str_d[1] in str_n:
                shared = str_d[1]

            else:
                continue  # Check next number

            # Skip trivial cases
            if shared == "0":
                continue

            # Cancel shared digit
            leftover_d = int(str_d.replace(shared, "", 1))
            leftover_n = int(str_n.replace(shared, "", 1))

            # Save result
            if n * leftover_d == d * leftover_n:
                numerators.append(n)
                denominators.append(d)
    
    return numerators, denominators
```

Now, we need a way to find the reduced form of a fraction given the numerator and denominator. For this, we can just divide the numberator and denominator by the greatest common divisor of both.

To get the greatest common divisor of two numbers, we can use the euclidean algorithm, which says that $\text{gcd}(a, b) = \text{gcd}(b, a \mod b)$, with the base case $\text{gcd}(a, 0) = a$

We can easily write this in code like this:

```py
def gcd(a: int, b: int) -> int:
    """
    Find the greatest common divisor (gcd) between two integers
    """
    while True:
        if b == 0:
            return a
        
        a, b = b, a%b
```
We will add this function to 

We now have all the necessary components to implement the function:

```py
def solution_1() -> int:
    numerators, denominators = find_digit_cancelling_fractions()

    # Multiply all numerators and denominators to find the product of the fractions
    num = 1
    den = 1
    for i in range(len(numerators)):
        num *= numerators[i]
        den *= denominators[i]

    return den // gcd(num, den)
```

# Helpful Links

- [Euclidean Algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm)
