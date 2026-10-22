// Shared test process ownership; no package installation or remote target option.
import { spawn } from 'node:child_process';
import { once } from 'node:events';
import { fileURLToPath } from 'node:url';

export async function stopProcess(child) {
  if (!child?.pid || child.exitCode !== null || child.signalCode !== null) return;
  const exited = once(child, 'exit');
  child.kill('SIGTERM');
  const hardStop = setTimeout(() => child.kill('SIGKILL'), 1500);
  try { await exited; } finally { clearTimeout(hardStop); }
}

export async function startFixture() {
  const child = spawn(process.env.BP_PYTHON ?? 'python3', [fileURLToPath(new URL('./server.py', import.meta.url))], {
    stdio: ['ignore', 'pipe', 'pipe'],
  });
  let errors = '';
  child.stderr.on('data', (chunk) => { errors = (errors + chunk).slice(-2000); });
  try {
    const origin = await new Promise((resolve, reject) => {
      let output = '';
      const timeout = setTimeout(() => finish(new Error('Fixture startup timed out.')), 5000);
      const onError = (error) => finish(error);
      const onExit = () => finish(new Error(`Fixture exited before startup: ${errors}`));
      const onData = (chunk) => {
        output += chunk;
        if (!output.includes('\n')) return;
        const line = output.split('\n')[0].trim();
        if (!/^http:\/\/127\.0\.0\.1:[0-9]+$/.test(line)) finish(new Error('Unexpected fixture address.'));
        else finish(null, line);
      };
      function finish(error, value) {
        clearTimeout(timeout);
        child.off('error', onError);
        child.off('exit', onExit);
        child.stdout.off('data', onData);
        if (error) reject(error); else resolve(value);
      }
      child.once('error', onError);
      child.once('exit', onExit);
      child.stdout.on('data', onData);
    });
    return { origin, stop: () => stopProcess(child) };
  } catch (error) {
    await stopProcess(child);
    throw error;
  }
}
