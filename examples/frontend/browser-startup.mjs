import { readFile } from 'node:fs/promises';
import { join } from 'node:path';

// Waiting does not own the child: the caller must stop it on success or failure.
export function waitForBrowserPort(child, profile, {
  timeoutMs = 20000,
  diagnostics = () => '',
} = {}) {
  return new Promise((resolve, reject) => {
    let settled = false;
    let poll;
    const expiresAt = performance.now() + timeoutMs;
    const details = () => diagnostics() || '(no stderr)';
    const timedOut = () => new Error(
      `Chromium did not expose a local debugging port within ${timeoutMs} ms: ${details()}`,
    );
    const deadline = setTimeout(() => finish(timedOut()), timeoutMs);
    const onError = (error) => finish(new Error(`Chromium failed to start: ${error.message}`, { cause: error }));
    const onExit = (code, signal) => finish(new Error(
      `Chromium exited before startup (${signal ? `signal ${signal}` : `code ${code}`}): ${details()}`,
    ));

    function finish(error, value) {
      if (settled) return;
      // A delayed event loop must not accept readiness observed after the deadline.
      if (!error && performance.now() >= expiresAt) error = timedOut();
      settled = true;
      clearTimeout(deadline);
      clearTimeout(poll);
      child.off('error', onError);
      child.off('exit', onExit);
      if (error) reject(error); else resolve(value);
    }

    async function check() {
      if (settled) return;
      if (performance.now() >= expiresAt) { finish(timedOut()); return; }
      if (child.exitCode !== null || child.signalCode !== null) {
        onExit(child.exitCode, child.signalCode);
        return;
      }
      try {
        const portInfo = await readFile(join(profile, 'DevToolsActivePort'), 'utf8');
        const [port, endpoint, extra] = portInfo.trim().split(/\r?\n/);
        // The file can be visible before both lines have been written.
        if (/^[0-9]+$/.test(port) && /^\/devtools\/browser\/[a-zA-Z0-9-]+$/.test(endpoint) &&
            Number(port) > 0 && Number(port) <= 65535 && extra === undefined) {
          finish(null, portInfo);
          return;
        }
      } catch (error) {
        if (error.code !== 'ENOENT') { finish(error); return; }
      }
      if (!settled) poll = setTimeout(check, 50);
    }

    child.once('error', onError);
    child.once('exit', onExit);
    void check();
  });
}
