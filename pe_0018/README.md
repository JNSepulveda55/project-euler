# Maximum Path Sum I
### Problem 0018

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is $23$.

```
   3
  7 4
 2 4 6
8 5 9 3
```

That is, $3 + 7 + 4 + 9 = 23$.

Find the maximum total from top to bottom of the triangle below:

```
                            75
                          95  64
                        17  47  82
                      18  35  87  10
                    20  04  82  47  65
                  19  01  23  75  03  34
                88  02  77  73  07  63  67
              99  65  04  28  06  16  70  92
            41  41  26  56  83  40  80  70  33
          41  48  72  33  47  32  37  16  94  29
        53  71  44  65  25  43  91  52  97  51  14
      70  11  33  28  77  73  17  78  39  68  17  57
    91  71  52  38  17  14  91  43  58  50  27  29  48
  63  66  04  68  89  53  67  30  73  16  69  87  40  31
04  62  98  27  23  09  70  98  73  93  38  53  60  04  23
```

<b>NOTE:</b> As there are only $16384$ routes, it is possible to solve this problem by trying every route. However, <a href="https://projecteuler.net/problem=67">Problem 67</a>, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! (c;

# Notes

We'll store the triangle as a list of lists:

```
   3
  7 4
 2 4 6   ---->  [[3],[7, 4],[2, 4, 6],[8, 5, 9, 3]] 
8 5 9 3
```

We can then just parse the triangle with this function:

```py
def parse_triangle(triangle: str) -> list[list[int]]:
    lines = triangle.split("\n")
    return [[int(x) for x in line.split()] for line in lines]
```

# Solutions

## Solution 1

Since they tell us that the efficient solution should be used for <a href="https://projecteuler.net/problem=67">Problem 67</a>, we're going to brute-force our way into the solution. We can just define a recursive function that checks every path and keeps track of the maximum sum at every node.

```py
def solution_1(triangle: int) -> int:
    
    def find_max_sum(root: tuple[int, int] = (0, 0), sum: int = 0) -> int:

        i, j = root
        root_number = triangle[i][j]

        if i == len(triangle) - 1:
            return sum + root_number

        return root_number + max(
            find_max_sum(triangle[i+1][j]),
            find_max_sum(triangle[i+1][j+1])
        )

    return find_max_sum()
```