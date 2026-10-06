import { writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = dirname(fileURLToPath(import.meta.url));
const requests = [
  ['arxiv-2025-availability.md', 'https://raw.githubusercontent.com/arXiv/arxiv-docs/95c71658adbaa987dc2ba1105ef9c5201ecde4ce/source/help/availability.md'],
  ['minimax-agent.md', 'https://agent.minimax.io/docs/techblog.md'],
  ['minimax-agent-index.txt', 'https://agent.minimax.io/docs/llms.txt'],
  ['qwen-blog.html', 'https://qwen.ai/blog'],
  ['google-pubs-tail.html', 'https://research.google/pubs/'],
  ['google-blog-tail.html', 'https://research.google/blog/'],
  ['arxiv-2025-content.json', 'https://api.github.com/repos/arXiv/arxiv-docs/contents/source/help/availability.md?ref=95c71658adbaa987dc2ba1105ef9c5201ecde4ce'],
  ['iana-2025b-northamerica.txt', 'https://data.iana.org/time-zones/tzdb-2025b/northamerica'],
  ['qwen-home-index.js', 'https://g.alicdn.com/qwenweb/qwen-ai-fe/0.0.85/js/p_home-index.js'],
  ['qwen-layout.js', 'https://g.alicdn.com/qwenweb/qwen-ai-fe/0.0.85/js/p_layout.js'],
  ['mimo-index.js', 'https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/index.c5195ace.js'],
  ['hunyuan-index.js', 'https://hunyuan-blog-web-prod-1258344703.cos.ap-guangzhou.myqcloud.com/assets/js/index-I3I3bCf9.js'],
  ['deepmind-publications.html', 'https://deepmind.google/research/publications/'],
  ['hunyuan-blog.js', 'https://hunyuan-blog-web-prod-1258344703.cos.ap-guangzhou.myqcloud.com/assets/js/index-CUQAWQeM.js'],
  ['qwen-main.js', 'https://g.alicdn.com/qwenweb/qwen-ai-fe/0.0.85/js/main.js'],
  ['hunyuan-service.js', 'https://hunyuan-blog-web-prod-1258344703.cos.ap-guangzhou.myqcloud.com/assets/js/index-cEoitnb7.js'],
  ['qwen-article.js', 'https://g.alicdn.com/qwenweb/qwen-ai-fe/0.0.85/js/4467.js'],
  ['qwen-research.js', 'https://g.alicdn.com/qwenweb/qwen-ai-fe/0.0.85/js/p_research-index.js'],
  ['hunyuan-zh.json', 'https://api.hunyuan.tencent.com/api/blog/publicList', { method: 'POST', headers: { 'accept-language': 'zh', 'Content-Type': 'application/json' }, body: JSON.stringify({ pageNum: 1, pageSize: 20, renderType: 0 }) }],
  ['kimi-changelog.html', 'https://platform.kimi.com/blog/posts/changelog'],
  ['deepseek-news.html', 'https://www.deepseek.com/news/'],
  ['qwen-shared.js', 'https://g.alicdn.com/qwenweb/qwen-ai-fe/0.0.85/js/eee9d9dd.js'],
];
for (const [name, url, extra] of requests.slice(Number(process.argv[2] ?? 0))) {
  const receipt = { url, checked: new Date().toISOString(), method: extra?.method ?? 'GET', body: extra?.body ?? null, headers: extra?.headers ?? null };
  try {
    const response = await fetch(url, { signal: AbortSignal.timeout(15000), ...extra, headers: { 'User-Agent': 'Mozilla/5.0', ...extra?.headers } });
    const content = await response.text();
    writeFileSync(join(root, name), content);
    if (name === 'arxiv-2025-content.json' && response.ok) {
      const record = JSON.parse(content);
      if (record.encoding !== 'base64' || record.path !== 'source/help/availability.md') throw new Error('Unexpected content identity');
      writeFileSync(join(root, 'arxiv-2025-availability-api.md'), Buffer.from(record.content, 'base64'));
    }
    Object.assign(receipt, { status: response.status, finalUrl: response.url, bytes: Buffer.byteLength(content) });
  } catch (error) { receipt.error = String(error); }
  writeFileSync(join(root, `${name}.receipt.json`), JSON.stringify(receipt, null, 2));
  console.log(JSON.stringify({ name, ...receipt }));
}
