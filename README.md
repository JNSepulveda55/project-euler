# Project Euler Solutions

This is my pesonal Project Euler Repo.

Most of the problem I've solved I did during undergrad, and since I would just sit at a random computer and write code,
I only have a few of my original solutions for the problems, and even if I have the original code, I have no idea of what my thought process was when
writing that specific piece of code.

This motivated me to redo evey problem but including a thorough explanation of my thought process for each problem. This repo is effectively an archive for my solutions.
However, I also thought it would be fun to share my solutions through github. If you're stuck on a problem I would recommend trying your best to solve it by yourself first!
Seeing someone else's solution is only like $1%$ as actually solving the problem. Once you've solved it come back and check if our answers match!

If you want to collaborate with your own solutions to the already posted problems, you can submit a pull request and I'll gladly accept your contribution!
Also if you find any error you can also submit a PR or just hit me up at `jn.sepulveda55@gmail.com`

I'm glad you found this repo and I hope you enjoy it!

Try the webpage version [here](https://jnsepulveda55.github.io/project-euler).


## Repository Structure

Each problem has its own folder:

```text
pe_0001/
  README.md
  pe_0001.py

pe_0002/
  README.md
  pe_0002.py

utils/
  utils.py
```

The usual layout is:

- `pe_XXXX/README.md`: problem statement, notes, and solution explanation.
- `pe_XXXX/pe_XXXX.py`: Python implementation for that problem.
- `utils/`: small shared helpers used across multiple solutions.
- `old_solutions/`: older scripts and notebooks from before this repo had a
  consistent structure.

Most solution files can be run directly:

```bash
python3 pe_0001/pe_0001.py
```

## Creating A New Problem

Use `create_problem.py` to create a new folder from the `pe_0000` template.

For example, to create Problem 42:

```bash
python3 create_problem.py 42
```

This creates:

```text
pe_0042/
  README.md
  pe_0042.py
```

The helper script also fetches the problem title and statement from Project
Euler and inserts them into the new README.

You can also choose a different destination root:

```bash
python3 create_problem.py 42 --destination-root /path/to/output
```

The script needs network access because it reads the problem page from
`projecteuler.net`.

## Collaboration

If you find a mistake, a clearer explanation, a cleaner implementation, or a
more elegant way to solve one of the existing problems, feel free to open a pull
request.

Contributions do not need to be over-engineered. A useful correction, a simpler
solution, or a better explanation is enough.
