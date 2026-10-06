import { writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = dirname(fileURLToPath(import.meta.url));
const requests = [
  ['ohm-agent-tech.html', 'https://agent.minimax.io/docs/techblog'],
  ['ohm-agent-tech.md', 'https://agent.minimax.io/docs/techblog.md'],
  ['ohm-agent-index.txt', 'https://agent.minimax.io/docs/llms.txt'],
  ['ohm-anthropic.html', 'https://www.anthropic.com/research'],
  ['ohm-zai.html', 'https://www.zhipuai.cn/zh/research'],
  ['ohm-zai-research.js', 'https://www.zhipuai.cn/_next/static/chunks/app/(frontend)/%5Blocale%5D/(routes)/research/page-dbb507db4bffb18e.js'],
  ['ohm-zai-research-support.js', 'https://www.zhipuai.cn/_next/static/chunks/8423-f2a102673951d80b.js'],
  ['ohm-zai-p2.html', 'https://www.zhipuai.cn/zh/research?page=2'],
];
for (const [name, url] of requests.slice(Number(process.argv[2] ?? 0))) {
  const receipt = { url, checked: new Date().toISOString(), method: 'GET' };
  try {
    const response = await fetch(url, { signal: AbortSignal.timeout(20000), headers: { 'User-Agent': 'Mozilla/5.0' } });
    const content = await response.text();
    writeFileSync(join(root, name), content);
    Object.assign(receipt, { status: response.status, finalUrl: response.url, bytes: Buffer.byteLength(content) });
  } catch (error) {
    receipt.error = String(error);
  }
  writeFileSync(join(root, `${name}.receipt.json`), JSON.stringify(receipt, null, 2));
  console.log(JSON.stringify({ name, ...receipt }));
}
