# Arranged Probability
### Problem 0100

If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, $P(\text{BB}) = (15/21) \times (14/20) = 1/2$.

The next such arrangement, for which there is exactly $50\%$ chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over $10^{12} = 1\,000\,000\,000\,000$ discs in total, determine the number of blue discs that the box would contain.

# Notes

- Add examples from the prompt here.
- Add any observations or math shortcuts here.

# Solutions

This is a very interesting problem which involved some searching on the internet (without spoiling the answer!)

The first thing I did was look at the problem tags and noticed the `diophantine-equation` tag, so I tried to reduce the problem to a diophantine equation first:

The probability of getting a blue ball twice is just:

$$\frac{b}{n} \cdot \frac{b-1}{n-1}$$

Where $b$ is the number of blue balls and $n$ is the total number of balls. We then need to equate the this to $\frac{1}{2}$ and do some algebraic manipulation:

$$\begin{align*}
\frac{b}{n} \cdot \frac{b-1}{n-1} &= \frac{1}{2}\\
\\
\frac{b(b-1)}{n(n-1)} &= \frac{1}{2}\\
\\
2b(b-1) &= n(n-1)\\
\\
2b^2-2b &= n^2 - n\\
\\
2b^2-2b - n^2 + n &= 0 
\end{align*}$$

Now this looks more like a diophantine equation.

## Solution 1

My next step was go to google and type diophantine equation to see what pops up. Wikipedia was the first result, where they give this nice table:

| Equation                                                | Description                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| $ax + by = c$                                           | This is a linear Diophantine equation, related to Bézout's identity.                                                                                                                                                                                                                                          |
| $w^3 + x^3 = y^3 + z^3$                                 | The smallest nontrivial solution in positive integers is $12^3 + 1^3 = 9^3 + 10^3 = 1729$. It was famously given as an evident property of 1729, a taxicab number, also called the Hardy–Ramanujan number, by Ramanujan to G. H. Hardy while meeting in 1917. There are infinitely many nontrivial solutions. |
| $x^n + y^n = z^n$                                       | For $n = 2$, there are infinitely many solutions ((x, y, z)): the Pythagorean triples. For larger integer values of $n$, Fermat's Last Theorem, initially claimed by Fermat in 1637 and proved by Andrew Wiles in 1995, states that there are no positive integer solutions $(x, y, z)$.                      |
| $x^2 - ny^2 = \pm 1$                                    | This is Pell's equation, named after the English mathematician John Pell. It was studied by Brahmagupta in the 7th century and by Fermat in the 17th century.                                                                                                                                                 |
| $\frac{4}{n} = \frac{1}{x} + \frac{1}{y} + \frac{1}{z}$ | The Erdős–Straus conjecture states that, for every positive integer (n \ge 2), there exists a solution in positive integers (x, y,) and (z). Although not usually stated in polynomial form, this example is equivalent to the polynomial equation $4xyz = n(yz + xz + xy)$.                                  |
| $x^4 + y^4 + z^4 = w^4$                                 | Euler incorrectly conjectured that this equation has no nontrivial solutions. Elkies proved that it has infinitely many nontrivial solutions, and a computer search by Frye found the smallest nontrivial solution: $95800^4 + 217519^4 + 414560^4 = 422481^4$.|

By mere observation, Pell's equation seemed like the closest to what I have, as in the table it is one of the only two that has squared exponents (and I had a hunch that this problem didn't involve pithagorean triples).

After a couple of hours, of dumb mistakes, I was able to get to this:

I'll take the terms with $b$ and $n$ separately and try to complete the square:

$$\begin{align*}
2b^2-2b &= \frac{1}{2} (4b^2 - 4b)\\
\\
&= \frac{1}{2} (4b^2 - 4b + 1 - 1)\\
\\
 &= \frac{1}{2} (4b^2 - 4b + 1) - \frac{1}{2}\\
\\
&= \frac{1}{2} (2b-1)^2 - \frac{1}{2}\\
\end{align*}$$

And similarly,

$$\begin{align*}
n^2-n &= \frac{1}{4} (4n^2 - 4n)\\
\\
&= \frac{1}{4} (4n^2 - 4n + 1 - 1)\\
\\
 &= \frac{1}{4} (4n^2 - 4n + 1) - \frac{1}{4}\\
\\
&= \frac{1}{4} (2n-1)^2 - \frac{1}{4}\\
\end{align*}$$

Then,

$$\begin{align*}
2b^2-2b - n^2 + n &= \frac{1}{2} (2b-1)^2 - \frac{1}{2} - \frac{1}{4} (2n-1)^2 + \frac{1}{4}\\
\\
&= \frac{1}{2} (2b-1)^2 - \frac{1}{2} - \frac{1}{4} (2n-1)^2 + \frac{1}{4}\\
\\
&= \frac{1}{2} (2b-1)^2 - \frac{1}{4} (2n-1)^2 - \frac{1}{4}
\end{align*}$$

Finally,

$$\begin{align*}
\frac{1}{2} (2b-1)^2 - \frac{1}{4} (2n-1)^2 - \frac{1}{4} &= 0\\
\\
\frac{1}{2} (2b-1)^2 - \frac{1}{4} (2n-1)^2 &= \frac{1}{4}\\
\\
\frac{1}{4} (2n-1)^2 - \frac{1}{2} (2b-1)^2 &= - \frac{1}{4}\\
\\
(2n-1)^2 - 2(2b-1)^2 &= -1\\
\end{align*}$$

Now let $x = 2n-1$ and $y= 2b -1$. We finally get what we want:

$$x^2 - 2y^2 = -1$$

This exact form of Pell's equation is very well described, to the point that they give us both the first solution to the equation and a way of generating all other solutions:

Trivial solution: $x_1 = 1, y_1 = 1$.

Recurrence relation:
$$x_k = x_{k-1}x_1^2 + nx_{k-1}y_1^2 + 2ny_{k-1}y_1x_1$$

$$y_k = y_{k-1}x_1^2 + ny_{k-1}y_1^2 + 2x_{k-1}y_1x_1$$

We can substitute $x_1 = 1, y_1 = 1$ and $n = 2$ to get:

$$x_k = x_{k-1} + 2x_{k-1} + 4y_{k-1}$$

$$y_k = y_{k-1} + 2y_{k-1} + 2x_{k-1}$$

And adding up terms we arrive at:

$$x_k = 3x_{k-1} + 4y_{k-1}$$

$$y_k = 3y_{k-1} + 2x_{k-1}$$

With this recurrence relation we can easily set up a function to find the solution to our problem:

```python
def solution_1(limit: int) -> int:
    x = 1
    y = 1
    while True:
        x, y = 3*x + 4*y, 3*y + 2*x

        n = (x + 1)//2  # Easily derived from x = 2n - 1

        if n > limit:
            b = (y+1)//2 # Easily derived from y = 2b - 1
            return b
```

# Helpful Links

- [Diophantine equation](https://en.wikipedia.org/wiki/Diophantine_equation)
