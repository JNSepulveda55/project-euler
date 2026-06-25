const PYODIDE_BASE_URL = "https://cdn.jsdelivr.net/pyodide/v0.28.3/full/";

let pyodideReadyPromise = null;

function getPyodide() {
  if (!pyodideReadyPromise) {
    importScripts(`${PYODIDE_BASE_URL}pyodide.js`);
    pyodideReadyPromise = loadPyodide({ indexURL: PYODIDE_BASE_URL });
  }

  return pyodideReadyPromise;
}

function ensureParentDirectories(pyodide, absolutePath) {
  const parts = absolutePath.split("/").filter(Boolean);
  let current = "";

  for (const part of parts.slice(0, -1)) {
    current += `/${part}`;
    if (!pyodide.FS.analyzePath(current).exists) {
      pyodide.FS.mkdir(current);
    }
  }
}

async function runPythonSolution(payload) {
  postMessage({ type: "status", message: "Loading Pyodide runtime..." });
  const pyodide = await getPyodide();
  const start = performance.now();
  const runId = `${Date.now()}_${Math.random().toString(16).slice(2)}`;
  const workdir = `/tmp/project_euler_${runId}`;

  pyodide.FS.mkdirTree(workdir);

  for (const [relativePath, contents] of Object.entries(payload.files || {})) {
    const absolutePath = `${workdir}/${relativePath}`;
    ensureParentDirectories(pyodide, absolutePath);
    pyodide.FS.writeFile(absolutePath, contents, { encoding: "utf8" });
  }

  pyodide.FS.chdir(workdir);
  pyodide.globals.set("__runner_entrypoint", payload.entrypoint);

  postMessage({ type: "status", message: "Running solution..." });

  const resultJson = await pyodide.runPythonAsync(`
import contextlib
import io
import json
import os
import runpy
import sys
import traceback

entrypoint = __runner_entrypoint
stdout = io.StringIO()
stderr = io.StringIO()
ok = True

sys.path.insert(0, os.getcwd())

with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
    try:
        runpy.run_path(entrypoint, run_name="__main__")
    except BaseException:
        ok = False
        traceback.print_exc(file=stderr)

json.dumps({
    "ok": ok,
    "stdout": stdout.getvalue(),
    "stderr": stderr.getvalue(),
})
`);

  const result = JSON.parse(resultJson);
  result.elapsedMs = performance.now() - start;
  return result;
}

self.onmessage = async (event) => {
  const message = event.data || {};
  if (message.type !== "run") {
    return;
  }

  try {
    const result = await runPythonSolution(message.payload || {});
    postMessage({ type: "result", result });
  } catch (error) {
    postMessage({
      type: "error",
      error: error && error.stack ? error.stack : String(error),
    });
  }
};
