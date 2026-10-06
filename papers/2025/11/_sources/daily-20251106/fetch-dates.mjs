import { writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = dirname(fileURLToPath(import.meta.url));
const requests = [
  ['datacite-01884.json', 'https://api.datacite.org/dois/10.48550/arXiv.2511.01884'],
  ['datacite-02833.json', 'https://api.datacite.org/dois/10.48550/arXiv.2511.02833'],
  ['datacite-03675.json', 'https://api.datacite.org/dois/10.48550/arXiv.2511.03675'],
  ['openreview-graces.json', 'https://api2.openreview.net/notes?id=XP6IvkhPt4'],
  ['graces-repo.json', 'https://api.github.com/repos/abhishekpanigrahi1996/GRACE'],
  ['cudaforge-repo.json', 'https://api.github.com/repos/OptimAI-Lab/CudaForge'],
  ['kimi-thinking-model.json', 'https://huggingface.co/api/models/moonshotai/Kimi-K2-Thinking'],
  ['kimi-repo.json', 'https://api.github.com/repos/MoonshotAI/Kimi-K2'],
  ['arxiv-cl-month.html', 'https://arxiv.org/list/cs.CL/2025-11?skip=25&show=25'],
  ['arxiv-dc-month.html', 'https://arxiv.org/list/cs.DC/2025-11?skip=0&show=25'],
];
for (const [name, url] of requests) {
  const receipt = { url, checked: new Date().toISOString(), method: 'GET' };
  try {
    const response = await fetch(url, { signal: AbortSignal.timeout(30000) });
    const content = await response.text();
    writeFileSync(join(root, name), content);
    Object.assign(receipt, { status: response.status, finalUrl: response.url, bytes: Buffer.byteLength(content) });
  } catch (error) {
    receipt.error = String(error);
  }
  writeFileSync(join(root, `${name}.receipt.json`), JSON.stringify(receipt, null, 2));
  console.log(JSON.stringify({ name, ...receipt }));
}
