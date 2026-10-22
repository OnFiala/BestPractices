# Independent browser-startup control

Date: 2026-10-22. Manual read-only delta review of commit
`4ecd1c23e4693d6a739397e879580db92ab7d0b4`, following
`ad545de7d86e2177d86353ac021663b354a70ad0`. No unresolved blocking defect was
identified within this bounded browser-readiness change. This is not a formal
security scan, production assurance or human release approval.

## Observed failure and bounded change

Independent inspection of GitHub check `119793580699` confirmed that
[run 39769618962](https://github.com/OnFiala/BestPractices/actions/runs/39769618962)
failed at `browser-smoke.mjs:106`: Chromium had not exposed its debugging port
within the former approximately five-second polling budget; captured stderr was
empty. This establishes the failed readiness condition. It does not establish
whether Chromium would later become ready, why it was delayed, or whether runner
OS variability caused it. Earlier CI failures and successes remain historical
observations; they are not erased by this change.

The commit changes exactly four files: `examples/frontend/browser-startup.mjs`,
`examples/frontend/browser-smoke.mjs`, `examples/frontend/README.md`, and
`tests/frontend.test.cjs`. The helper permits one startup attempt for at most
20 seconds. The existing 45-second overall abort deadline is unchanged. Browser
selection order, explicit sandbox opt-in, fixed target, permissions and all 20
browser journey checks are unchanged. No retry, fallback browser, skip or relaxed
acceptance rule was added.

The reviewed helper checks monotonic expiry at every poll and again before
accepting readiness after an asynchronous file read. It requires exactly two valid
marker lines, a port from 1 through 65535 and the expected browser endpoint form;
partial markers continue waiting within the same deadline. Both helper and driver
handle LF/CRLF consistently. Spawn errors and exited/signalled children fail;
settlement clears timers/listeners and prevents late completion from changing an
outcome. Non-ENOENT read failures remain failures. Existing stderr consumption and
bounded diagnostics remain in place; startup errors now identify executable and
Node version. The caller retains process/profile ownership and cleanup.

## Independent checks

- `node --test tests/frontend.test.cjs`: 12 passed, zero skipped. New real-child
  cases cover readiness after the former limit (observed about 5.56 seconds),
  early exit, spawn failure, a partial marker and valid readiness after timeout.
- `BP_BROWSER_NO_SANDBOX=1 node examples/frontend/browser-smoke.mjs`: all 20 actual
  browser checks passed on Chrome/154.0.8037.57 and Node v24.19.0. This explicit
  reduced-isolation condition applies only to the owned local fixture.
- An independent run of the actual driver used a synthetic browser that never
  became ready. It exited 1 after 20.091 seconds with the expected timeout and
  executable/Node diagnostics. Both owned browser and HTTP-fixture processes had
  stopped, and the temporary browser profile was gone. The four reviewed files
  were unchanged before/after this check; their SHA-256 hashes and output hashes
  are recorded in the accompanying `bp-browser-startup-control.json` metadata.
  This exercises failure cleanup, not the performance of a real Chromium launch.

During review, the implementation was tightened to check elapsed time before
acceptance and to wait for a complete marker; the driver's CRLF parsing was aligned
with the helper. The control role made no repository edits or commits.

## Current observations and limits

The coordinator's `reports/reference-checks-browser-startup.json` records passed
suites with counts 19 delivery, 12 durable service, 22 agent workflow, 12 frontend
unit/fixture and 20 browser checks. I independently verified its unchanged-input
flag, successful outcomes and current-image match at
`662f3feb9a2a5d6149e5b4a9e5944bead4834cecfd9b8b4e6c9344cdc0043e90`.
This full fixed-runner execution is coordinator evidence, distinct from the
independent checks above.

Independent GitHub job metadata inspection confirmed
[run 39770522601](https://github.com/OnFiala/BestPractices/actions/runs/39770522601)
at `4ecd1c23e4693d6a739397e879580db92ab7d0b4` passed every quality step, including
fixed references, coverage, site build and generated-site checks. The workflow
contains no sandbox opt-out. Its exact browser version and per-case runtime receipt
were not independently read from hosted logs.

These observations support the longer bounded wait and its failure handling.
They do not diagnose the original host delay, guarantee repeated-run reliability,
or authorize production release. A future failure remains a failure requiring
its own diagnostic evidence; local fixture and authenticity limits remain intact.
