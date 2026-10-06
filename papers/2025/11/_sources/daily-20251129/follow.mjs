import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const dir = path.dirname(fileURLToPath(import.meta.url));
const ids = ['2511.23404','2511.23319','2511.23310','2511.23225','2511.23113','2511.22880','2511.22889','2511.22972','2511.22788','2511.22481','2511.22333','2511.23347','2512.00207','2511.23465','2511.23239','2511.23476','2511.23281','2511.23092','2511.22891','2511.22924','2511.23262','2511.23436','2511.22904','2511.23070','2511.23034','2511.22677','2511.22697','2511.22570'];
const requests = ids.map(id => [`abs-${id}v1.html`, `https://arxiv.org/abs/${id}v1`]);
requests.push(['availability-2025.md', 'https://raw.githubusercontent.com/arXiv/arxiv-docs/95c71658adbaa987dc2ba1105ef9c5201ecde4ce/source/help/availability.md']);
requests.push(['qwen-blog.html', 'https://qwenlm.github.io/blog/']);
requests.push(['google-pubs-web.html', 'https://research.google/pubs/?year=2025']);
requests.push(['google-blog-web.html', 'https://research.google/blog/?year=2025']);
for (const name of ['learning', 'agent', 'multimodal']) {
  const receipt = JSON.parse(await fs.readFile(path.join(dir, `arxiv-${name}.xml.receipt.json`), 'utf8'));
  const url = new URL(receipt.url);
  url.searchParams.set('start', '50');
  url.searchParams.set('max_results', '100');
  requests.push([`arxiv-${name}-tail.xml`, url.toString()]);
}
for (const [name, url] of requests) {
  const receipt = { url, started: new Date().toISOString() };
  try {
    const response = await fetch(url, { signal: AbortSignal.timeout(10000) });
    const body = await response.text();
    Object.assign(receipt, { status: response.status, finalUrl: response.url, bytes: Buffer.byteLength(body) });
    await fs.writeFile(path.join(dir, name), body);
  } catch (error) {
    receipt.error = String(error);
  }
  receipt.ended = new Date().toISOString();
  await fs.writeFile(path.join(dir, `${name}.receipt.json`), JSON.stringify(receipt, null, 2) + '\n');
  process.stdout.write(`${name}: ${receipt.status ?? receipt.error}\n`);
}
