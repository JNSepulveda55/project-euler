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

Notes for self

- Only show alternative solutions if its worth it. Most problems from 1 to 100 can be solved with brute force algorithms anyway (18/05/2026)

- If a solution runs in less than a second, I probably won't bother in optimizing it, specially for easier problems

# Contributions

Want to contribute with a problem I havent solved yet? Have a different approach to an already solved problem? Feel free to issue a pull request! I'll review the changes and merge if I feel it matches the style of the repo and could be valuable to add.