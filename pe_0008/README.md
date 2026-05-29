# Largest Product in a Series
### Problem 0008

The four adjacent digits in the $1000$-digit number that have the greatest product are $9 \times 9 \times 8 \times 9 = 5832$.

731671765313306249192251196744265747423553491949349698352031277450632623957831801698480186947885184385861560789112949495459501737958331952853208805511125406987471585238630507156932909632952274430435576689664895044524452316173185640309871112172238311362229893423380308135336276614282806444486645238749303589072962904915604407723907138105158593079608667017242712188399879790879227492190169972088809377665727333001053367881220235421809751254540594752243525849077116705560136048395864467063244157221553975369781797784617406495514929086256932197846862248283972241375657056057490261407972968652414535100474821663704844031<span style="color: red">9989</span>000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the $1000$-digit number that have the greatest product. What is the value of this product?

# Solutions

## Solution 1

We can easily solve this problem with a sliding window. Imagine we have the following string of numbers: `6247195`. 

We can imagine that we have a window which we manually move one space at a time and we claculate the product of the numbers only inside this window. For this example the window size will be $4$.

`[6247]195` $\longrightarrow 6 \times 2 \times 4 \times 7 = 336$

For the nex steps there is a trick. We could calculate the product like usual:

`6[2471]95` $\longrightarrow 2 \times 4 \times 7 \times 1 = 56$

But we would be doing a lot of repeated calculations, since we'll be multiplying together $2, 4$ and $7$ again. To avoid this, we can just keep track of the last result, divide by the number that 'leaves' and multiply by the number that 'comes' like this:

`6[2471]95` $\longrightarrow \frac{336 \times 1}{6} = 56$

And we can carry on doing this until we hit the end:

`62[4719]5` $\longrightarrow \frac{56 \times 9}{2} = 252$

`624[7195]` $\longrightarrow \frac{252 \times 5}{4} = 315$

In our case, the $4$-digit string with the maximum product is `6247`

Finally, you may have noticed that we might have problems if we get a $0$ in our string. We can just add a rule that whenever there's a zero in the window we skip this step since the product will be $0$ anyways, we just need to make sure to still keep track of the product of the other numbers.

We can translate this method to a python function like this:

```py
def solution_1(digit_string: str, window_size: int) -> int:
    product = 1
    zeros_in_window = 0  # Keep track of zeros in the window

    # Initial window product
    for i in range(window_size):
        digit = int(digit_string[i])
        if digit == 0:
            zeros_in_window += 1
        product *= digit

    max_product = product

    for i in range(1, len(digit_string) - window_size):
        leaves = int(digit_string[i-1])
        comes = int(digit_string[i+window_size-1])

        if leaves != 0:
            product //= leaves
        else:
            zeros_in_window -= 1

        if comes != 0:
            product *= comes
        else:
            zeros_in_window += 1
            continue  # If there's a 0 incoming just skip the iteration
        
        if product > max_product and zeros_in_window == 0:
            max_product = product

    return max_product
```

# Helpful Links

- [Sliding window technique](https://www.geeksforgeeks.org/dsa/window-sliding-technique/)
