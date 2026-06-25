"""
Build a static GitHub Pages site for the Project Euler solutions.

The script scans pe_XXXX problem folders, renders each README, embeds the
matching Python solution, and writes a deployable site into docs/.
"""

from __future__ import annotations

import html
import json
import re
import shutil
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = REPO_ROOT / "docs"
PROBLEMS_DIR = DOCS_DIR / "problems"
ASSETS_DIR = DOCS_DIR / "assets"
ASSET_SOURCE_DIR = REPO_ROOT / "scripts" / "site_assets"
UTILS_DIR = REPO_ROOT / "utils"

PROBLEM_DIR_RE = re.compile(r"^pe_(?P<number>\d+)$")
README_NAMES = ("README.md", "README")
SUPPORT_FILE_SUFFIXES = {".txt", ".csv", ".json", ".dat"}


@dataclass(frozen=True)
class Problem:
    number: int
    folder_name: str
    page_name: str
    title: str
    readme_path: Path
    solution_path: Path
    support_paths: tuple[Path, ...]


def find_readme(problem_dir: Path) -> Path | None:
    for name in README_NAMES:
        path = problem_dir / name
        if path.is_file():
            return path
    return None


def find_solution_file(problem_dir: Path) -> Path | None:
    preferred_names = (
        "solution.py",
        f"{problem_dir.name}.py",
    )

    for name in preferred_names:
        path = problem_dir / name
        if path.is_file():
            return path

    python_files = sorted(path for path in problem_dir.glob("*.py") if path.is_file())
    if len(python_files) == 1:
        return python_files[0]

    return None


def infer_title(readme_text: str, fallback: str) -> str:
    for line in readme_text.splitlines():
        match = re.match(r"^#\s+(.+?)\s*$", line)
        if match:
            return strip_markdown(match.group(1))
    return fallback


def strip_markdown(text: str) -> str:
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\*\*\*(.+?)\*\*\*", r"\1", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", text)
    return html.unescape(text).strip()


def discover_problems() -> list[Problem]:
    problems: list[Problem] = []

    for problem_dir in sorted(path for path in REPO_ROOT.iterdir() if path.is_dir()):
        match = PROBLEM_DIR_RE.match(problem_dir.name)
        if match is None:
            continue

        number = int(match.group("number"))
        if number == 0:
            continue

        readme_path = find_readme(problem_dir)
        solution_path = find_solution_file(problem_dir)
        if readme_path is None or solution_path is None:
            continue

        readme_text = readme_path.read_text(encoding="utf-8")
        support_paths = tuple(
            sorted(
                path
                for path in problem_dir.iterdir()
                if path.is_file()
                and path != readme_path
                and path != solution_path
                and path.suffix.lower() in SUPPORT_FILE_SUFFIXES
            )
        )

        problems.append(
            Problem(
                number=number,
                folder_name=problem_dir.name,
                page_name=f"{number:04d}.html",
                title=infer_title(readme_text, fallback=problem_dir.name),
                readme_path=readme_path,
                solution_path=solution_path,
                support_paths=support_paths,
            )
        )

    return sorted(problems, key=lambda problem: problem.number)


def resolve_readme_link(raw_url: str, readme_path: Path) -> str:
    if raw_url.startswith(("#", "http://", "https://", "mailto:")):
        return raw_url

    target, separator, fragment = raw_url.partition("#")
    resolved = (readme_path.parent / target).resolve()
    parent = resolved.parent

    if resolved.name in README_NAMES:
        match = PROBLEM_DIR_RE.match(parent.name)
        if match is not None:
            page = f"{int(match.group('number')):04d}.html"
            return f"{page}{separator}{fragment}" if separator else page

    return raw_url


def render_inline(text: str, readme_path: Path) -> str:
    text = re.sub(r"<br\s*/?>", " ", text, flags=re.IGNORECASE)
    parts = re.split(r"(`[^`]*`)", text)
    rendered: list[str] = []

    for part in parts:
        if not part:
            continue

        if part.startswith("`") and part.endswith("`"):
            rendered.append(f"<code>{html.escape(part[1:-1])}</code>")
            continue

        rendered.append(render_links_and_emphasis(part, readme_path))

    return "".join(rendered)


def render_links_and_emphasis(text: str, readme_path: Path) -> str:
    link_re = re.compile(
        r"\[([^\]]+)\]\(([^)]+)\)"
        r"|<a\s+href=[\"']([^\"']+)[\"'][^>]*>(.*?)</a>",
        re.IGNORECASE,
    )
    rendered: list[str] = []
    cursor = 0

    for match in link_re.finditer(text):
        rendered.append(render_emphasis(html.escape(text[cursor : match.start()])))

        if match.group(1) is not None:
            label_text = match.group(1)
            href_text = match.group(2)
        else:
            label_text = re.sub(r"<[^>]+>", "", match.group(4))
            href_text = match.group(3)

        label = render_emphasis(html.escape(label_text))
        href = resolve_readme_link(href_text, readme_path)
        rendered.append(f'<a href="{html.escape(href, quote=True)}">{label}</a>')
        cursor = match.end()

    rendered.append(render_emphasis(html.escape(text[cursor:])))
    return "".join(rendered)


def render_emphasis(escaped_text: str) -> str:
    escaped_text = re.sub(r"\*\*\*(.+?)\*\*\*", r"<strong><em>\1</em></strong>", escaped_text)
    escaped_text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped_text)
    escaped_text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", escaped_text)
    return escaped_text


def render_markdown(markdown_text: str, readme_path: Path) -> str:
    lines = markdown_text.replace("\r\n", "\n").split("\n")
    output: list[str] = []
    paragraph: list[str] = []
    list_type: str | None = None
    code_lines: list[str] = []
    code_language = ""
    in_code_block = False

    def close_paragraph() -> None:
        if paragraph:
            text = " ".join(line.strip() for line in paragraph)
            output.append(f"<p>{render_inline(text, readme_path)}</p>")
            paragraph.clear()

    def close_list() -> None:
        nonlocal list_type
        if list_type is not None:
            output.append(f"</{list_type}>")
            list_type = None

    for line in lines:
        fence_match = re.match(r"^```(.*)$", line)
        if fence_match:
            if in_code_block:
                language_class = f' class="language-{html.escape(code_language)}"' if code_language else ""
                output.append(f"<pre><code{language_class}>{html.escape(chr(10).join(code_lines))}</code></pre>")
                code_lines.clear()
                code_language = ""
                in_code_block = False
            else:
                close_paragraph()
                close_list()
                code_language = fence_match.group(1).strip()
                in_code_block = True
            continue

        if in_code_block:
            code_lines.append(line)
            continue

        if not line.strip():
            close_paragraph()
            close_list()
            continue

        heading_match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if heading_match:
            close_paragraph()
            close_list()
            level = len(heading_match.group(1))
            output.append(f"<h{level}>{render_inline(heading_match.group(2), readme_path)}</h{level}>")
            continue

        list_match = re.match(r"^\s*([-*])\s+(.+)$", line)
        ordered_match = re.match(r"^\s*\d+\.\s+(.+)$", line)
        if list_match or ordered_match:
            close_paragraph()
            next_list_type = "ul" if list_match else "ol"
            if list_type != next_list_type:
                close_list()
                output.append(f"<{next_list_type}>")
                list_type = next_list_type

            item = list_match.group(2) if list_match else ordered_match.group(1)
            output.append(f"<li>{render_inline(item, readme_path)}</li>")
            continue

        if re.match(r"^\s*---+\s*$", line):
            close_paragraph()
            close_list()
            output.append("<hr>")
            continue

        close_list()
        paragraph.append(line)

    if in_code_block:
        language_class = f' class="language-{html.escape(code_language)}"' if code_language else ""
        output.append(f"<pre><code{language_class}>{html.escape(chr(10).join(code_lines))}</code></pre>")

    close_paragraph()
    close_list()
    return "\n".join(output)


def html_page(title: str, body: str, css_href: str, script_src: str | None = None) -> str:
    script_tag = f'\n    <script src="{script_src}" defer></script>' if script_src else ""
    mathjax_config = """    <script>
      window.MathJax = {
        tex: {
          inlineMath: [["$", "$"], ["\\\\(", "\\\\)"]],
          displayMath: [["$$", "$$"], ["\\\\[", "\\\\]"]]
        },
        options: {
          skipHtmlTags: ["script", "noscript", "style", "textarea", "pre", "code"]
        }
      };
    </script>
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js" defer></script>"""
    return f"""<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{html.escape(title)}</title>
    <link rel="stylesheet" href="{css_href}">
{mathjax_config}
  </head>
  <body>
{body}{script_tag}
  </body>
</html>
"""


def render_index(problems: list[Problem]) -> str:
    rows = "\n".join(
        f"""              <tr>
                <td><code>{html.escape(problem.folder_name)}</code></td>
                <td>{html.escape(problem.title)}</td>
                <td><a href="problems/{problem.page_name}">Read and run</a></td>
              </tr>"""
        for problem in problems
    )

    body = f"""    <header class="site-header">
      <div class="container">
        <p class="eyebrow">Project Euler</p>
        <h1>Personal problem notes and Python solutions</h1>
        <p class="lead">A simple archive of solved problems, explanations, and runnable Python code. Solutions run locally in your browser through Pyodide, so runtime depends on your machine and browser.</p>
      </div>
    </header>
    <main class="container">
      <section class="panel" aria-labelledby="problem-list-heading">
        <div class="section-heading">
          <h2 id="problem-list-heading">Problems</h2>
          <span>{len(problems)} detected</span>
        </div>
        <div class="table-wrap">
          <table>
            <thead>
              <tr>
                <th scope="col">Problem</th>
                <th scope="col">Title</th>
                <th scope="col">Page</th>
              </tr>
            </thead>
            <tbody>
{rows}
            </tbody>
          </table>
        </div>
      </section>
    </main>
"""

    return html_page(
        title="Project Euler Solutions",
        body=body,
        css_href="assets/site.css",
    )


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def build_runner_payload(problem: Problem) -> str:
    files: dict[str, str] = {
        f"{problem.folder_name}/{problem.solution_path.name}": read_text(problem.solution_path),
    }

    for support_path in problem.support_paths:
        support_text = read_text(support_path)
        files[f"{problem.folder_name}/{support_path.name}"] = support_text
        files[support_path.name] = support_text

    if UTILS_DIR.is_dir():
        for path in sorted(UTILS_DIR.glob("*.py")):
            files[f"utils/{path.name}"] = read_text(path)

    payload = {
        "entrypoint": f"{problem.folder_name}/{problem.solution_path.name}",
        "files": files,
        "problem": problem.folder_name,
        "timeoutMs": 30_000,
    }
    return json.dumps(payload, ensure_ascii=True, sort_keys=True).replace("</", "<\\/")


def render_problem_page(problem: Problem) -> str:
    readme_text = read_text(problem.readme_path)
    readme_html = render_markdown(readme_text, problem.readme_path)
    source_code = html.escape(read_text(problem.solution_path))
    payload_json = build_runner_payload(problem)

    support_files = ""
    if problem.support_paths:
        items = "".join(f"<li><code>{html.escape(path.name)}</code></li>" for path in problem.support_paths)
        support_files = f"""
          <details class="support-files">
            <summary>Included support files</summary>
            <ul>{items}</ul>
          </details>"""

    body = f"""    <header class="page-header">
      <div class="container">
        <a class="back-link" href="../index.html">&larr; All problems</a>
        <p class="eyebrow">{html.escape(problem.folder_name)}</p>
        <h1>{html.escape(problem.title)}</h1>
      </div>
    </header>
    <main class="container problem-page">
      <article class="panel readme-content">
        {readme_html}
      </article>

      <section class="panel runner-panel" aria-labelledby="runner-heading">
        <div class="section-heading">
          <h2 id="runner-heading">Run Solution</h2>
          <button id="run-solution" type="button">Run solution</button>
        </div>
        <p class="muted">Runs the checked-in Python file in your browser with Pyodide. Runtime is browser-dependent and can differ from local CPython. Execution is stopped after 30 seconds.</p>{support_files}
        <div class="output-grid" aria-live="polite">
          <section>
            <h3>stdout</h3>
            <pre id="stdout" class="output-box">Click "Run solution" to execute this problem.</pre>
          </section>
          <section>
            <h3>stderr / errors</h3>
            <pre id="stderr" class="output-box"></pre>
          </section>
          <section>
            <h3>Runtime</h3>
            <pre id="runtime" class="output-box"></pre>
          </section>
        </div>
      </section>

      <section class="panel" aria-labelledby="source-heading">
        <div class="section-heading">
          <h2 id="source-heading">Python Source</h2>
          <span>{html.escape(problem.solution_path.name)}</span>
        </div>
        <pre class="source-code"><code>{source_code}</code></pre>
      </section>

      <script type="application/json" id="solution-payload">{payload_json}</script>
    </main>
"""

    return html_page(
        title=f"{problem.folder_name}: {problem.title}",
        body=body,
        css_href="../assets/site.css",
        script_src="../assets/runner.js",
    )


def copy_assets() -> None:
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    for asset_path in sorted(path for path in ASSET_SOURCE_DIR.iterdir() if path.is_file()):
        shutil.copy2(asset_path, ASSETS_DIR / asset_path.name)


def build_site() -> None:
    problems = discover_problems()
    if not problems:
        raise RuntimeError("No problem folders were found.")

    if DOCS_DIR.exists():
        shutil.rmtree(DOCS_DIR)

    PROBLEMS_DIR.mkdir(parents=True)
    copy_assets()

    (DOCS_DIR / ".nojekyll").write_text("", encoding="utf-8")
    (DOCS_DIR / "index.html").write_text(render_index(problems), encoding="utf-8")

    for problem in problems:
        (PROBLEMS_DIR / problem.page_name).write_text(render_problem_page(problem), encoding="utf-8")

    print(f"Built {len(problems)} problem pages in {DOCS_DIR}")


if __name__ == "__main__":
    build_site()
