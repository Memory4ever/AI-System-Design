import { writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = dirname(fileURLToPath(import.meta.url));
const requests = [
  ['openai-research.html', 'https://openai.com/research/'],
  ['openai-rss.xml', 'https://openai.com/news/rss.xml'],
  ['anthropic.html', 'https://www.anthropic.com/research'],
  ['deepmind.html', 'https://deepmind.google/research/'],
  ['deepmind-blog.html', 'https://deepmind.google/discover/blog/?page=1'],
  ['google-pubs.html', 'https://research.google/pubs/'],
  ['google-blog-nov.html', 'https://research.google/blog/?year=2025&month=11'],
  ['meta.html', 'https://ai.meta.com/research/'],
  ['qwen-old.html', 'https://qwenlm.github.io/'],
  ['qwen.html', 'https://qwen.ai/research'],
  ['deepseek.html', 'https://www.deepseek.com/'],
  ['deepseek-updates.html', 'https://api-docs.deepseek.com/updates'],
  ['kimi.html', 'https://platform.kimi.com/blog'],
  ['hunyuan.html', 'https://hunyuan.tencent.com/research'],
  ['hunyuan-p1.json', 'https://api.hunyuan.tencent.com/api/blog/publicList', { pageNum: 1, pageSize: 20, renderType: 0 }],
  ['zai-p1.html', 'https://www.zhipuai.cn/zh/research'],
  ['zai-p2.html', 'https://www.zhipuai.cn/zh/research?page=2'],
  ['zai-releases.html', 'https://docs.z.ai/release-notes/new-released'],
  ['seed-research.html', 'https://seed.bytedance.com/en/research'],
  ['seed-papers.html', 'https://seed.bytedance.com/en/public_papers'],
  ['ernie-p1.html', 'https://ernie.baidu.com/blog/zh/'],
  ['ernie-p2.html', 'https://ernie.baidu.com/blog/zh/page/2/'],
  ['mimo.html', 'https://mimo.xiaomi.com/'],
  ['minimax.html', 'https://www.minimax.io/blog'],
  ['minimax-cn.html', 'https://www.minimaxi.com/blog'],
  ['arxiv-availability.html', 'https://info.arxiv.org/help/availability.html'],
];
requests.push(['arxiv-2025-commit.json', 'https://api.github.com/repos/arXiv/arxiv-docs/commits?path=source/help/availability.md&until=2025-11-09T00:00:00Z&per_page=1']);
for (const type of [1, 2]) {
  for (const token of [0, 20]) {
    requests.push([`seed-t${type}-p${token}.json`, `https://seed.bytedance.com/api/get_article_list_v2?article_type=${type}&publish_year=2025&count=20&page_token=${token}&order_desc=true`]);
  }
}

for (const [name, url, body] of requests.slice(Number(process.argv[2] ?? 0))) {
  const receipt = { url, checked: new Date().toISOString(), method: body ? 'POST' : 'GET', body: body ?? null };
  try {
    const options = { signal: AbortSignal.timeout(15000), headers: { 'User-Agent': 'Mozilla/5.0', 'x-tt-locale': 'US' } };
    if (body) Object.assign(options, { method: 'POST', body: JSON.stringify(body), headers: { ...options.headers, 'Content-Type': 'application/json' } });
    const response = await fetch(url, options);
    const content = await response.text();
    writeFileSync(join(root, name), content);
    Object.assign(receipt, { status: response.status, finalUrl: response.url, bytes: Buffer.byteLength(content) });
  } catch (error) {
    receipt.error = String(error);
  }
  writeFileSync(join(root, `${name}.receipt.json`), JSON.stringify(receipt, null, 2));
  console.log(JSON.stringify({ name, ...receipt }));
}
