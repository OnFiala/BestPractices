// Original example: URL state and remote-result transitions have no DOM dependency.
export const scenarios = Object.freeze(['normal', 'empty', 'error', 'retry', 'slow', 'injection']);

export function normalizeQuery({ q = '', scenario = 'normal' } = {}) {
  return {
    q: String(q).trim().slice(0, 80),
    scenario: scenarios.includes(scenario) ? scenario : 'normal',
  };
}

export function readQuery(search) {
  const params = new URLSearchParams(search);
  return normalizeQuery({ q: params.get('q') ?? '', scenario: params.get('scenario') });
}

export function queryString(query) {
  const { q, scenario } = normalizeQuery(query);
  const params = new URLSearchParams();
  if (q) params.set('q', q);
  if (scenario !== 'normal') params.set('scenario', scenario);
  return params.size ? `?${params}` : '';
}

export function initialRemoteState() {
  return { phase: 'idle', requestId: 0, items: [], message: '' };
}

export function transition(state, event) {
  if (event.type === 'start') {
    return { phase: 'loading', requestId: event.requestId, items: [], message: '' };
  }
  // Aborting transport is an optimization; this gate is the correctness boundary.
  if (state.phase !== 'loading' || event.requestId !== state.requestId) return state;
  if (event.type === 'resolve') {
    return { ...state, phase: event.items.length ? 'success' : 'empty', items: event.items };
  }
  if (event.type === 'reject') return { ...state, phase: 'error', message: event.message };
  if (event.type === 'cancel') return { ...state, phase: 'cancelled' };
  return state;
}

export function decodeResources(payload) {
  if (!payload || !Array.isArray(payload.items) || payload.items.length > 20) {
    throw new Error('Unexpected response. Please try again.');
  }
  return payload.items.map((item) => {
    if (!item || typeof item.id !== 'string' || item.id.length > 80 ||
        typeof item.title !== 'string' || item.title.length > 200 ||
        typeof item.summary !== 'string' || item.summary.length > 500) {
      throw new Error('Unexpected response. Please try again.');
    }
    return { id: item.id, title: item.title, summary: item.summary };
  });
}

export function statusText(state) {
  switch (state.phase) {
    case 'loading': return 'Loading resources…';
    case 'success': return `${state.items.length} ${state.items.length === 1 ? 'resource' : 'resources'} found.`;
    case 'empty': return 'No resources found. Try another search.';
    case 'error': return state.message;
    case 'cancelled': return 'Search cancelled. You can retry or change your search.';
    default: return 'Ready to search.';
  }
}
