# Lattice Paths
### Problem 0015

Starting in the top left corner of a $2 \times 2$ grid, and only being able to move to the right and down, there are exactly $6$ routes to the bottom right corner.

<div>
<img src="https://projecteuler.net/resources/images/0015.png?1678992052" alt=""></div>

How many such routes are there through a $20 \times 20$ grid?


# Solutions

## Solution 1

This is a nice combinatorics problem. We can view the grid as a tree of choices like this:

```
        o
       / \
      o   o
     / \ / \
    o   o   o
     \ / \ /
      o   o 
       \ /
        o
```

This looks very similar to Pascal's triangle. In fact, Pascal's triangle tells us in how many ways we can reach a node in the triangle.

```
        1        
       / \       
      1   1      
     / \ / \     
    1   2   1    
   / \ / \ / \   
  1   3   3   1  
 / \ / \ / \ / \ 
1   4   6   4   1
```

In this case, there are six ways of reaching the node with the number `6`.


Also, each entry in Pascal's triangle can be found using combinatorics.

If we label the rows from the top down starting at zero and label each node in each row from left to right starting at zero like this:

```
                    (0, 0)        
                     /  \       
               (1, 0)    (1, 1)      
                /  \      /  \     
          (2, 0)    (2, 1)    (2, 2)    
           /  \      /  \      /  \   
     (3, 0)    (3, 1)    (3, 2)    (3, 3)  
      /  \      /  \      /  \      /  \ 
(4, 0)    (4, 1)    (4, 2)    (4, 3)    (4, 4)
```
If we take an arbitrary node $(n, r)$ in the tree, then the number in that node will be $\begin{pmatrix}n\\r\end{pmatrix} = \frac{n!}{r!(n-r)!}$

With this, we can easily calculate in how many ways we can reach the bottom-right corner of the grid. If we take the top-left corner of the grid as $(0, 0)$ and we say the grid size is $g$, then the bottom right corner will be at position $(2g, g)$. The number in that position would be $\begin{pmatrix}2g\\g\end{pmatrix} = \frac{(2g)!}{g!(2g-g)!} = \frac{(2g)!}{g!g!} = \frac{(2g)!}{(g!)^2}$

We can code this pretty easily. First lets define a function to find the factorial of a number:

```py
def factorial(n: int) -> int:
    """
    Compute the factorial of a number
    """

    assert n > 0 and int(n), "n should be non-negative"
    assert int(n) == n, "n should be an integer"

    result = 1
    for i in range(1, n+1):
        result *= i

    return result
```
We can add this function to our [`utils.py`](../utils/utils.py) file.

Then our solution just becomes:

```py
def solution_1(grid_size: int) -> int:
    return factorial(2*grid_size)//factorial(grid_size)**2
```

## Solution 2

If you want a more algorithmic approach, we can implement something similar to pascal's triangle, but with the grid.

At step i, we update all intersections/nodes that are at distance i from the top left corner by adding the numbers of the adjacent squares in the previous step.

Let's see this with an example. We start with an empty grid:

```
   +---+---+
   |   |   |
   +---+---+
   |   |   |
   +---+---+
```

There's only one way to start at the top-left, so we put a `1` in that square.

```
   1---+---+
   |   |   |
   +---+---+
   |   |   |
   +---+---+
```

Next, we update the adjacent empty squares with a `1`, as there is only one way to get to each of them:

```
   1---1---+
   |   |   |
   1---+---+
   |   |   |
   +---+---+
```

Now, for the numbers in the border of the grid there is still only one way to get to them, but for the center sqaure there are two ways, which also happens to be the sum of the squares next to it:

```
   1---1---1
   |   |   |
   1---2---+
   |   |   |
   1---+---+
```

We continue doing this until we fill the grid:

```
   1---1---1
   |   |   |
   1---2---3
   |   |   |
   1---3---+
```

And finally:

```
   1---1---1
   |   |   |
   1---2---3
   |   |   |
   1---3---6
```

Note that even though the grid from the problem is $2 \times 2$, the matrix we need to store the values is of size $3 \times 3$. In general, we'll need a matrix of size `grid_size + 1` $\times$ `grid_size + 1`

We can easily implement it like this

```py
def solution_2(grid_size: int) -> int:
    # Initialize a square matrix of size `grid_size + 1` 
    grid = [[0]*(grid_size+1) for _ in range(grid_size+1)]

    grid[0][0] = 1  # Top left is 1

    # Number of diagonals in the grid
    num_diags = 2*(grid_size + 1) - 1

    # Fill the matrix
    for diag in range(1, num_diags):
        offset = max(diag-grid_size, 0)
        for i in range(offset, diag - offset + 1):
            j = diag - i

            # If its on the first row
            if i == 0:
                grid[i][j] = grid[i][j-1]

            # If its on the first column
            elif j == 0:
                grid[i][j] = grid[i-1][j]

            # Any other case, add the numbers from top and left
            else:
                grid[i][j] = grid[i-1][j] + grid[i][j-1]

    return grid[grid_size][grid_size]
```

# Helpful Links

- [Pascal's Triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle)
