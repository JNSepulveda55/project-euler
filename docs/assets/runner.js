(function () {
  const payloadElement = document.getElementById("solution-payload");
  const runButton = document.getElementById("run-solution");
  const stdoutElement = document.getElementById("stdout");
  const stderrElement = document.getElementById("stderr");
  const runtimeElement = document.getElementById("runtime");
  const scriptUrl = new URL(document.currentScript.src);
  const workerUrl = new URL("pyodide-worker.js", scriptUrl);

  if (!payloadElement || !runButton || !stdoutElement || !stderrElement || !runtimeElement) {
    return;
  }

  const payload = JSON.parse(payloadElement.textContent);
  const timeoutMs = payload.timeoutMs || 30000;

  function setRunning(isRunning) {
    runButton.disabled = isRunning;
    runButton.textContent = isRunning ? "Running..." : "Run solution";
  }

  function resetOutput(message) {
    stdoutElement.textContent = message || "";
    stderrElement.textContent = "";
    runtimeElement.textContent = "";
  }

  function runSolution() {
    setRunning(true);
    resetOutput("Loading Pyodide. This can take a moment the first time...");

    const worker = new Worker(workerUrl);
    const start = performance.now();
    let finished = false;

    const timeoutId = window.setTimeout(() => {
      if (finished) {
        return;
      }

      finished = true;
      worker.terminate();
      setRunning(false);
      stdoutElement.textContent = "";
      stderrElement.textContent = `Execution stopped after ${Math.round(timeoutMs / 1000)} seconds.`;
      runtimeElement.textContent = `${(performance.now() - start).toFixed(1)} ms`;
    }, timeoutMs);

    worker.onmessage = (event) => {
      const message = event.data || {};

      if (message.type === "status") {
        stdoutElement.textContent = message.message;
        return;
      }

      if (message.type === "result") {
        finished = true;
        window.clearTimeout(timeoutId);
        worker.terminate();
        setRunning(false);

        const result = message.result || {};
        stdoutElement.textContent = result.stdout || "(no stdout)";
        stderrElement.textContent = result.stderr || "";
        runtimeElement.textContent = `${Number(result.elapsedMs || 0).toFixed(1)} ms`;
        return;
      }

      if (message.type === "error") {
        finished = true;
        window.clearTimeout(timeoutId);
        worker.terminate();
        setRunning(false);
        stdoutElement.textContent = "";
        stderrElement.textContent = message.error || "Unknown runner error.";
        runtimeElement.textContent = `${(performance.now() - start).toFixed(1)} ms`;
      }
    };

    worker.onerror = (event) => {
      finished = true;
      window.clearTimeout(timeoutId);
      worker.terminate();
      setRunning(false);
      stdoutElement.textContent = "";
      stderrElement.textContent = event.message || "Worker failed.";
      runtimeElement.textContent = `${(performance.now() - start).toFixed(1)} ms`;
    };

    worker.postMessage({ type: "run", payload });
  }

  runButton.addEventListener("click", runSolution);
})();
