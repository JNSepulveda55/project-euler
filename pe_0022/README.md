# Names Scores
### Problem 0022

Using <a href="https://projecteuler.net/resources/documents/0022_names.txt">names.txt</a> (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth $3 + 15 + 12 + 9 + 14 = 53$, is the $938$-th name in the list. So, COLIN would obtain a score of $938 \times 53 = 49714$.

What is the total of all the name scores in the file?

# Notes

- Here, we simpify the use of ASCII. I acknowledge that more modern standards like Unicode are used, but they are compatible with ASCII, which is easier to explain.

# Solutions

This is a nice problem that evaluates our coding skills more than our math skills.

The first thing we need is a way to parse the file. Here's the code:

```py
def preprocess_names(filepath: str = "pe_0022/names.txt") -> list[str]:
    with open(filepath, "r") as file:
        names = file.read()
        names = names.replace("\"", "")  # Get rid of quotation marks "
        names = names.split(",")  # Split the names and save in a list

    return names
```

## Solution 1

We would like to have a function to calculate the worth of each name. To do this, we can make use of the ASCII values of the letters. ASCII is a unique identifier that is given to any possible character (symbol) that can be typed. 

In the ASCII table, the character `'A'` has the code `65`, Letter `'B'` has the code `66` and so on until `'Z'` which has the code `90`. 

In python, there is a built'in function to get the ASCII code of a charater: `ord()`, so `ord('A') = 65`, and `ord('A') - 64 = 1`. If we do this for every letter, we can get their value.

We now can implement the worth function:

```py
def name_worth(name: str) -> int:
    return sum([(ord(i)) - 64 for i in name])
```

Finally, the solution would look like this:

```py
def solution_1(names: list[str]) -> int:
    # Sort the list alphabetically
    names.sort()

    score_sum = 0
    for idx, name in enumerate(names):  # Get index and name
        score_sum += (idx+1) * name_worth(name)

    return score_sum
```

# Helpful Links

- [ASCII codes](https://en.wikipedia.org/wiki/ASCII)
