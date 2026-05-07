"""
This file contains useful functions that may be used
to get to the solution for a problem or just implement
nice functionalities like timing a code
"""

from time import time
from functools import wraps


def timer(function):
    @wraps(function)
    def timer(*args, **kwargs):
        start = time()
        result = function(*args, **kwargs)
        end = time()
        print(f"Function {function.__name__} ran in {end-start:.5f} seconds")
        return result

    return timer
