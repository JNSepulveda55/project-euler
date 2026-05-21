# from utils import timer, divisors_alter, fast_divisors, factors, divisors
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from utils import timer
from sympy import divisors as divisors_sympy

@timer
def solve(amount):

    alexandrian = set()

    n = 1
    while len(alexandrian) < amount:
        n += 1

        # if n % 3 == 1:
        #     continue
        divs = fast_divisors(n*(n+1))
        # print(n)
        for d in divs:
            # print("=================================")
            p = (-d + (d**2 + 4*n)**0.5)/2
            # print("n", n)
            # print("d", d)
            # print("p:", p)
            if p % 1 == 0 and (p**2 + 1) % d == 0:
                alexandrian.add(n*(n+1)//d)


@timer
def alexandrian(amount):
    
    alexandrian = set()

    p = 0
    while len(alexandrian) < amount:
        p += 1

        # print("===================================0")
        
        for d, d_prime in divisors_alter(p**2+1):
            A = p*(p+d)*(p+d_prime)
            alexandrian.add(A)
            # print("p: ", p)
            # print("q: ", -p-d)
            # print("r: ", -p-d_prime)
            # print("A: ", A)

    alexandrian = list(alexandrian)
    alexandrian.sort()
    return alexandrian[-1]

@timer
def alexandrian_sympy(amount):
    
    alexandrian = set()

    p = 0
    while len(alexandrian) < amount:
        p += 1

        # print("===================================0")
        divs = divisors_sympy(p**2+1)
        for d in divs[:len(divs)//2+1]:
            A = p*(p+d)*(p + (p**2+1)//d)
            alexandrian.add(A)
            # print("p: ", p)
            # print("q: ", -p-d)
            # print("r: ", -p-d_prime)
            # print("A: ", A)

    alexandrian = list(alexandrian)
    alexandrian.sort()
    return alexandrian[149999]

print(alexandrian_sympy(550000))
