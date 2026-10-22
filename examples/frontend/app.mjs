import { createResourceController } from './controller.mjs';
import { normalizeQuery, queryString, readQuery, statusText } from './state.mjs';

const form = document.querySelector('#search-form');
const input = document.querySelector('#query');
const scenario = document.querySelector('#scenario');
const search = document.querySelector('#search');
const cancel = document.querySelector('#cancel');
const retry = document.querySelector('#retry');
const list = document.querySelector('#resource-list');
const content = document.querySelector('#result-content');
const status = document.querySelector('#status');

function render(state) {
  const focused = document.activeElement;
  cancel.hidden = state.phase !== 'loading';
  retry.hidden = !['error', 'cancelled'].includes(state.phase);
  content.setAttribute('aria-busy', String(state.phase === 'loading'));
  content.dataset.phase = state.phase;
  status.textContent = statusText(state);
  const cards = state.items.map((item) => {
    const li = document.createElement('li');
    const article = document.createElement('article');
    const heading = document.createElement('h3');
    const summary = document.createElement('p');
    // Server strings remain text, even when they contain HTML-shaped payloads.
    heading.textContent = item.title;
    summary.textContent = item.summary;
    article.append(heading, summary);
    li.append(article);
    return li;
  });
  list.replaceChildren(...cards);
  // A disappearing action must not strand focus on the document body.
  if ((focused === cancel && cancel.hidden) || (focused === retry && retry.hidden)) {
    (state.phase === 'cancelled' ? retry : search).focus();
  }
}

const controller = createResourceController({ onChange: render });
function loadFromURL() {
  const query = readQuery(location.search);
  input.value = query.q;
  scenario.value = query.scenario;
  void controller.search(query);
}

form.addEventListener('submit', (event) => {
  event.preventDefault();
  const query = normalizeQuery({ q: input.value, scenario: scenario.value });
  input.value = query.q;
  const nextURL = `${location.pathname}${queryString(query)}`;
  if (nextURL !== `${location.pathname}${location.search}`) history.pushState(null, '', nextURL);
  void controller.search(query);
});
cancel.addEventListener('click', () => controller.cancel());
retry.addEventListener('click', () => { void controller.retry(); });
document.querySelector('#compact').addEventListener('change', (event) => {
  // Local display state has no server effect and no durable storage.
  list.classList.toggle('compact', event.target.checked);
});
window.addEventListener('popstate', loadFromURL);
window.addEventListener('pagehide', () => controller.cancel());
// A page restored from the back-forward cache needs to restart cancelled work.
window.addEventListener('pageshow', (event) => { if (event.persisted) loadFromURL(); });
loadFromURL();
