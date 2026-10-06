import { spawnSync } from 'node:child_process';
import path from 'node:path';

const themes = {
  model: '(cat:cs.CL OR cat:cs.LG) AND (all:"mixture of experts" OR all:attention OR all:"language model training" OR all:"reinforcement learning" OR all:"language model alignment")',
  agent: '(cat:cs.AI OR cat:cs.IR OR cat:cs.MA) AND (all:"retrieval augmented" OR all:"LLM agent" OR all:"tool calling" OR all:"agent memory" OR all:"language model reasoning")',
  multimodal: '(cat:cs.CV OR cat:cs.RO) AND (all:"vision language" OR all:"world model" OR all:"diffusion model" OR all:"vision language action")',
  runtime: '(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF) AND (all:LLM OR all:"language model" OR all:GPU OR all:"model serving")',
};
for (const [name, theme] of Object.entries(themes)) {
  const url = new URL('https://export.arxiv.org/api/query');
  url.searchParams.set('search_query', `${theme} AND submittedDate:[202510151400 TO 202510161400]`);
  url.searchParams.set('start', '0');
  url.searchParams.set('max_results', '60');
  url.searchParams.set('sortBy', 'submittedDate');
  url.searchParams.set('sortOrder', 'ascending');
  const result = spawnSync(process.execPath, [path.join(import.meta.dirname, 'fetch.mjs'), `arxiv-${name}.xml`, url.href], { encoding: 'utf8' });
  process.stdout.write(result.stdout);
  process.stderr.write(result.stderr);
}
