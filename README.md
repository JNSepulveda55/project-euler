# Project Euler Solutions

This is my personal Project Euler workspace.

I solve these problems as a hobby, mostly for the fun of thinking through the
math, writing down the reasoning, and keeping a record of different approaches.
The goal is not to build a polished library or the fastest possible solution for
every problem. If a simple solution is clear and runs quickly enough, that is
usually good enough.

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

## GitHub Pages Site

This repo includes a small static site generator for GitHub Pages. It scans the
`pe_XXXX` problem folders, renders the README files, embeds the Python source,
and creates browser-runnable pages using Pyodide.

Build the site locally:

```bash
python3 scripts/build_site.py
```

Preview it locally:

```bash
cd docs
python3 -m http.server 8000
```

Then open `http://localhost:8000`.

To publish it on GitHub Pages, go to the repository settings, open **Pages**,
and set the source to **GitHub Actions**. The included workflow builds and
deploys the `docs/` folder on pushes to `main`.

## Collaboration

If you find a mistake, a clearer explanation, a cleaner implementation, or a
more elegant way to solve one of the existing problems, feel free to open a pull
request.

Contributions do not need to be over-engineered. A useful correction, a simpler
solution, or a better explanation is enough.
