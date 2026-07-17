# Coded Triangle Numbers
### Problem 0042

The $n$<sup>th</sup> term of the sequence of triangle numbers is given by, $t_n = \frac12n(n+1)$; so the first ten triangle numbers are:
$$1, 3, 6, 10, 15, 21, 28, 36, 45, 55, \dots$$

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is $19 + 11 + 25 = 55 = t_{10}$. If the word value is a triangle number then we shall call the word a triangle word.

Using <a href="https://projecteuler.net/resources/documents/0042_words.txt">words.txt</a> (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?


# Solutions

To solve this problem we can just pre-compute a list of the first $50$ triangular numbers (We could go further just to be safe but $50$ is more than enough).

Then, we'll just use a similar approach to [problem 22](../pe_0022/README.md) to calculate the score for each word and just check if its a triangular number.

## Solution 1

The code for the solution looks like this:

```py
# Adapted from PE_0022
def preprocess_words(filepath: str = "pe_0042/words.txt") -> list[str]:
    with open(filepath, "r") as file:
        words = file.read()
        words = words.replace("\"", "")  # Get rid of quotation marks "
        words = words.split(",")  # Split the names and save in a list

    return words

# Adapted from PE_022
def word_worth(word: str) -> int:
    return sum([(ord(i)) - 64 for i in word])


def solution_1() -> int:
    words = preprocess_words()
    triangular = {(n*(n+1))//2 for n in range(1, 51)}

    count = 0
    for word in words:
        if word_worth(word) in triangular:
            count += 1

    return count
```
