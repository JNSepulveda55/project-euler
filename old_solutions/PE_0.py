solve = lambda n: (n * (n + 1) * (2*n+1))//6 - 4 * (n//2 * (n//2 + 1) * (2*(n//2)+1))//6

print(solve(830_000))