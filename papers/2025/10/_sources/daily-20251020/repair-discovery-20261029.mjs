import fs from 'node:fs';
import path from 'node:path';
const dir = path.dirname(new URL(import.meta.url).pathname);
const topics = {
  MODEL: 'titles.title:("language model" OR "language models" OR transformer OR transformers OR "mixture of experts" OR "state space")',
  TRAIN: 'titles.title:(pretraining OR "pre-training" OR "post-training" OR GRPO OR "preference optimization" OR "reinforcement learning")',
  AGENT: 'titles.title:("agent memory" OR "tool use" OR "tool calling" OR "retrieval augmented" OR "language agent" OR "language agents")',
  MULTIMODAL: 'titles.title:("vision language" OR "vision-language" OR "world model" OR "world models" OR "diffusion model" OR "diffusion models" OR "vision language action")',
  RUNTIME: 'titles.title:("LLM serving" OR "KV cache" OR "speculative decoding" OR "distributed training" OR "GPU kernel" OR "GPU kernels")',
};
const log = [];
for (const field of ['created', 'registered']) {
  for (const [topic, query] of Object.entries(topics)) {
    let url = new URL('https://api.datacite.org/dois');
    url.searchParams.set('query', `client.id:arxiv.content AND ${field}:[2025-10-18T16:00:00.000Z TO 2025-10-19T15:59:59.999Z] AND ${query}`);
    url.searchParams.set('page[size]', '100');
    let page = 1;
    while (url) {
      const started = new Date().toISOString();
      const res = await fetch(url, {signal: AbortSignal.timeout(45000)});
      const raw = await res.text();
      const name = `REPAIR_DC_VALID_MS_${field.toUpperCase()}_${topic}_P${page}_20261029.json`;
      fs.writeFileSync(path.join(dir, name), raw);
      if (!res.ok) throw new Error(`${res.status}: ${raw.slice(0,300)}`);
      const data = JSON.parse(raw);
      const record = {field, topic, url: String(url), started, status: res.status, file:name, total:data.meta.total, count:data.data.length, next:data.links.next};
      log.push(record);
      fs.writeFileSync(path.join(dir, 'REPAIR_DC_VALID_MS_FETCH_20261029.json'), JSON.stringify(log, null, 2));
      console.log(JSON.stringify(record));
      url = data.links.next ? new URL(data.links.next) : null;
      page++;
      if (page > 20) throw new Error('Unexpected topic expansion; review before more pages');
    }
  }
}
