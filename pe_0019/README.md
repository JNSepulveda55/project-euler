# Counting Sundays
### Problem 0019

You are given the following information, but you may prefer to do some research for yourself.

<ul><li>1 Jan 1900 was a Monday.</li>
<li>Thirty days has September,<br>
April, June and November.<br>
All the rest have thirty-one,<br>
Saving February alone,<br>
Which has twenty-eight, rain or shine.<br>
And on leap years, twenty-nine.</li>
<li>A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.</li>
</ul>

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?


# Solutions

## Solution 1

We'll divide the problem into two phases. First, we're going to calculate which day the first day of the century falls on. 

We're going to make a series of observations which will give us the necessary insights to solve the problem.


First, any non-leap year has $365$ days. Since $365 \ \text{mod}\ 7 = 1$, this means that a year starts and ends on the same day. So, the next year starts on the next day as the previous year.

On a leap year, $366 \ \text{mod}\ 7 = 2$, so the next year will start two days ahead as the previous year.

We can use this to build a function to find us the day of the week on which any year starts.

First, we need a function to check whether a year is a leap year or not:

```py
def is_leap_year(year: int) -> bool:

    if year % 4 != 0:
        return False
    
    if year % 100 == 0 and year % 400 != 0:
        return False
    
    return True
```

Now, we implement the function to find what day the first day of a year falls on:

```py
# Find what day the first day of a year falls on
def find_first_of_year(year: int) -> int:
    curr_year = 1900  # We know Jan 1 of 1900 is a Monday
    day = 1  # 0 is Sunday, 1 is Monday and so on ...

    # Check if we're searching forwards or backwards
    factor = 1 if year > curr_year else -1

    while curr_year != year:
        curr_year += factor
        day = (day + 1 + is_leap_year(curr_year)) % 7

    return day
```

Now, that we know which day the first of the year is, we can start adding the amount of days in each month $\text{mod}\ 7$ and keep track of how many times `day == 0`, which means the first of the month is a monday.

```py
# Helper function that returns the days in each month of the year
def day_offsets = lambda year: [31, 28 + is_leap_year(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def solution_1(century: int) -> int:
    year = 100*century + 1

    # Find the first day of the year
    day = find_first_of_year(year)
    
    count = 0
    for i in range(year, year + 100):
        for offset in day_offsets(i):
            
            if day % 7 == 0:
                count += 1  # If its a Sunday update count

            day = (day + offset) % 7

    return count
```

# References

- [Leap year](https://en.wikipedia.org/wiki/Leap_year)
