# Project Euler



My solutions to all of the project euler problems I've solved, with explained solutions. (In progress)

I will soon update this README! (Typed on May 11th 2026 to keep me accountable)

## Problem Scaffolding Tool

Use `create_problem.py` to generate a new problem folder from the `pe_0000` template and fill its `README.md` with the problem title and statement from Project Euler.

Example:

```bash
python3 create_problem.py 42
```

This creates a new folder named `pe_0042` with:

- `pe_0042.py`, copied from the template and renamed
- `README.md`, updated with the scraped Project Euler problem

Optional example with a custom destination root:

```bash
python3 create_problem.py 42 --destination-root /path/to/output
```

The script needs network access when it fetches the problem statement from `projecteuler.net`.

Notes for self (18/05/2026)

- Only show alternative solutions if its worth it. Most problems from 1 to 100 can be solved with brute force algorithms anyway

