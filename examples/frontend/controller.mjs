import { decodeResources, initialRemoteState, normalizeQuery, transition } from './state.mjs';

// One owner for requests/results. The injected transport makes race behavior testable.
export function createResourceController({ fetcher = fetch, onChange = () => {} } = {}) {
  let state = initialRemoteState();
  let active;
  let sequence = 0;
  let query = normalizeQuery();
  let attempt = 1;
  const publish = (event) => {
    const next = transition(state, event);
    if (next !== state) {
      state = next;
      onChange(state);
    }
  };

  async function run(nextQuery, retry = false) {
    active?.abort();
    query = normalizeQuery(nextQuery);
    attempt = retry ? 2 : 1;
    const controller = new AbortController();
    active = controller;
    const requestId = ++sequence;
    publish({ type: 'start', requestId });
    const params = new URLSearchParams({ ...query, attempt: String(attempt) });
    try {
      // Relative path, no credentials, no configurable target host or automatic retries.
      const response = await fetcher(`/api/resources?${params}`, {
        signal: controller.signal, credentials: 'omit', cache: 'no-store', redirect: 'error',
      });
      if (!response.ok) throw new Error('Resources are unavailable. Please retry.');
      const items = decodeResources(await response.json());
      publish({ type: 'resolve', requestId, items });
    } catch (error) {
      if (error.name === 'AbortError') publish({ type: 'cancel', requestId });
      else publish({ type: 'reject', requestId, message: 'Resources are unavailable. Please retry.' });
    } finally {
      if (requestId === sequence) active = undefined;
    }
  }

  return {
    search: (nextQuery) => run(nextQuery),
    retry: () => ['error', 'cancelled'].includes(state.phase) ? run(query, true) : Promise.resolve(),
    cancel() {
      publish({ type: 'cancel', requestId: sequence });
      active?.abort();
      active = undefined;
    },
    getState: () => state,
  };
}
