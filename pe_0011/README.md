# Largest Product in a Grid
### Problem 0011

In the $20 \times 20$ grid below, four numbers along a diagonal line have been marked in red.

`08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08`<br>
`49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00`<br>
`81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65`<br>
`52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91`<br>
`22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80`<br>
`24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50`<br>
`32 98 81 28 64 23 67 10` <span style="color: red"><b>26</b></span> `38 40 67 59 54 70 66 18 38 64 70`<br>
`67 26 20 68 02 62 12 20 95` <span style="color: red"><b>63</b></span> `94 39 63 08 40 91 66 49 94 21`<br>
`24 55 58 05 66 73 99 26 97 17` <span style="color: red"><b>78</b></span> `78 96 83 14 88 34 89 63 72`<br>
`21 36 23 09 75 00 76 44 20 45 35` <span style="color: red"><b>14</b></span> `00 61 33 97 34 31 33 95`<br>
`78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92`<br>
`16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57`<br>
`86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58`<br>
`19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40`<br>
`04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66`<br>
`88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69`<br>
`04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36`<br>
`20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16`<br>
`20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54`<br>
`01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48`<br>

The product of these numbers is $26 \times 63 \times 78 \times 14 = 1788696$.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the $20 \times 20$ grid?

# Notes

- This problem allows for some very nice small optimizations, but I won't cover all of them for the sake of conciseness.

# Solutions

This problem tests our coding skills more than our mathematical knowledge.

We need to scan the grid in four directions:
- Left to right
- Top to bottom
- Top left to bottom right (diagonally)
- Top right to bottom left (diagonally)

However, instead of defining four different functions, we can just do a left to right function and a top left to bottom right function and flip the grid instead, which is easier. See the example below:

Say this is our grid:

$$\begin{bmatrix}
1 & 2 & 3 & 4\\
5 & 6 & 7 & 8\\
9 & 10 & 11 & 12\\
13 & 14 & 15 & 16\\
\end{bmatrix}$$

Assume we only have functions that can process rows. the first row processed would be:

$$\begin{bmatrix}
\textcolor{red}{1} & \textcolor{red}{2} & \textcolor{red}{3} & \textcolor{red}{4}\\
5 & 6 & 7 & 8\\
9 & 10 & 11 & 12\\
13 & 14 & 15 & 16\\
\end{bmatrix}$$

If we want to process the first column, we can just flip the matrix along the diagonal. this is called *transposing* a matrix:

$$\begin{bmatrix}
1 & 5 & 9 & 13\\
2 & 6 & 10 & 14\\
3 & 7 & 11 & 15\\
4 & 8 & 12 & 16\\
\end{bmatrix}$$

Then, processing the first row of this matrix is equivalent to processing the first column of the original matrix:

$$\begin{bmatrix}
\textcolor{red}{1} & \textcolor{red}{5} & \textcolor{red}{9} & \textcolor{red}{13}\\
2 & 6 & 10 & 14\\
3 & 7 & 11 & 15\\
4 & 8 & 12 & 16\\
\end{bmatrix}$$

A similar process can be used with the diagonals if we flip the matrix horizontally.

Even better, we can turn the diagonals into lists similar to rows, which can be also processed in the same way as any other row.

## Solution 1

Note that processing a row is a similar procedure to the sliding window we implemented for [problem 8](../pe_0008/README.md)

Let's define our functions to process a row here:

```py
def process_row(row: list[int], window_size: int) -> int:

    # Edge case
    if len(row) < window_size:
        return 0

    product = 1
    zeros_in_window = 0  # Keep track of zeros in the window

    # Initial window product
    for i in range(window_size):
        number = int(row[i])
        if number == 0:
            zeros_in_window += 1
        product *= number

    max_product = product

    for i in range(1, len(row) - window_size):
        leaves = int(row[i-1])
        comes = int(row[i+window_size-1])

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

With this, we can process rows and columns. Now lets create our helper function to process diagonals:

```py
def get_diagonals(matrix: list[list[int]]):
    m, n = len(matrix), len(matrix[0])  # Get dimensions of matrix
    num_diags = 2 * max(m, n) - 1  # You can doodle on a paper to prove this!
    diags = [[] for _ in range(num_diags)]  # Create `num_diags` empty arrays

    for i in range(m):
        for j in range(n):
            diags[i+j].append(matrix[i][j])

    return diags
```

In this case, we'll extract the bottom left to top right diagonals, then we can flip the matrix and do it again

Now we're ready to implement our solution:

```py
def solution_1(matrix: list[list[int]], window_size: int) -> int:

    def helper(row_list: list):
        """
        Process all rows in a list and return the max product
        """
        max_product = 0

        for row in row_list:
            max_row_product = process_row(row, window_size)
            if max_row_product > max_product:
                max_product = max_row_product

        return max_product

    # Process rows:
    rows_max = helper(matrix)

    # Process columns:
    transpose = zip(*matrix)  # This is a nice trick!
    cols_max = helper(transpose)

    # Process diagonals:
    diags_1_max = helper(get_diagonals(matrix))

    flipped = [row[::-1] for row in matrix]
    diags_2_max = helper(get_diagonals(flipped))

    return max(rows_max, cols_max, diags_1_max, diags_2_max)
```

# Helpful Links

- [Problem 8](../pe_0008/README.md)
