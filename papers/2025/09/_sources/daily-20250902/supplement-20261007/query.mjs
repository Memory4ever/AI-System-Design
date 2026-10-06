import { execFileSync } from 'node:child_process';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = dirname(fileURLToPath(import.meta.url));
const groups = {
  model: ['mixture of experts', 'state space model', 'reward model', 'preference optimization', 'test-time scaling', 'model merging'],
  system: ['speculative decoding', 'prefill', 'disaggregated', 'distributed training', 'inference serving', 'LLM compiler'],
  multimodal: ['video generation', 'vision language model', 'flow matching', 'embodied', 'world model'],
  agent: ['retrieval augmented generation', 'agent memory', 'prompt injection', 'computer use', 'multi-agent language'],
};
const name = process.argv[2];
if (!groups[name]) throw new Error('Unknown theme');
const url = new URL('https://arxiv.org/search/advanced');
const parameters = { advanced: '', 'classification-include_cross_list': 'include', 'date-filter_by': 'date_range', 'date-from_date': '2025-09-01', 'date-to_date': '2025-10-01', 'date-date_type': 'announced_date_first', abstracts: 'show', size: '50', order: 'announced_date_first', start: '0' };
for (const [i, term] of groups[name].entries()) Object.assign(parameters, { [`terms-${i}-operator`]: i ? 'OR' : 'AND', [`terms-${i}-term`]: `"${term}"`, [`terms-${i}-field`]: 'title' });
for (const [key, value] of Object.entries(parameters)) url.searchParams.set(key, value);
execFileSync(process.execPath, [join(root, 'fetch.mjs'), `arxiv-${name}.html`, url.toString()], { stdio: 'inherit' });
