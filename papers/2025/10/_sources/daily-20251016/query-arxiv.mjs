import { spawnSync } from 'node:child_process';
import path from 'node:path';

const groups = {
  model: '(cat:cs.CL OR cat:cs.LG) AND (all:"language model" OR all:transformer OR all:"mixture of experts" OR all:"foundation model")',
  agent: '(cat:cs.AI OR cat:cs.IR OR cat:cs.MA) AND (all:"language model" OR all:"LLM agent" OR all:"retrieval augmented" OR all:"tool calling")',
  multimodal: '(cat:cs.CV OR cat:cs.RO) AND (all:"vision language" OR all:"world model" OR all:"foundation model" OR all:"diffusion model" OR all:"vision language action")',
  runtime: '(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF) AND (all:LLM OR all:"language model" OR all:GPU OR all:"model serving")',
};
for (const [name, theme] of Object.entries(groups)) {
  const url = new URL('https://export.arxiv.org/api/query');
  url.searchParams.set('search_query', `${theme} AND submittedDate:[202510141400 TO 202510151400]`);
  url.searchParams.set('start', '0');
  url.searchParams.set('max_results', '60');
  url.searchParams.set('sortBy', 'submittedDate');
  url.searchParams.set('sortOrder', 'ascending');
  const r = spawnSync(process.execPath, [path.join(import.meta.dirname, 'fetch.mjs'), `arxiv-${name}.xml`, url.href], { encoding: 'utf8' });
  process.stdout.write(r.stdout);
  process.stderr.write(r.stderr);
}
