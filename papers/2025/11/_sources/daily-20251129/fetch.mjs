import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const dir = path.dirname(fileURLToPath(import.meta.url));
const requests = [
  ['openai-rss.xml', 'https://openai.com/news/rss.xml'],
  ['anthropic.html', 'https://www.anthropic.com/research'],
  ['google-pubs.html', 'https://research.google/pubs/?year=2025'],
  ['google-blog.html', 'https://research.google/blog/2025/'],
  ['deepmind.html', 'https://deepmind.google/blog/page/4/'],
  ['meta.html', 'https://ai.meta.com/research/'],
  ['qwen.html', 'https://qwen.ai/research'],
  ['deepseek.html', 'https://api-docs.deepseek.com/updates'],
  ['kimi.html', 'https://platform.kimi.com/blog'],
  ['hunyuan.html', 'https://hunyuan.tencent.com/research'],
  ['zai-p1.html', 'https://www.zhipuai.cn/zh/research'],
  ['zai-p2.html', 'https://www.zhipuai.cn/zh/research?page=2'],
  ['ernie-p1.html', 'https://ernie.baidu.com/blog/zh/'],
  ['ernie-p2.html', 'https://ernie.baidu.com/blog/zh/page/2/'],
  ['mimo.html', 'https://mimo.xiaomi.com/'],
  ['minimax.html', 'https://www.minimax.io/blog'],
  ['minimax-cn.html', 'https://www.minimaxi.com/blog'],
  ['minimax-agent.md', 'https://agent.minimax.io/docs/techblog.md'],
  ['minimax-index.txt', 'https://agent.minimax.io/docs/llms.txt'],
];
for (const type of [1, 2]) {
  for (const page of [0, 20]) {
    requests.push([`seed-t${type}-p${page}.json`, `https://seed.bytedance.com/api/get_article_list_v2?article_type=${type}&publish_year=2025&count=20&order_desc=true&page_token=${page}`, { headers: { 'x-tt-locale': 'US' } }]);
  }
}
requests.push(['hunyuan-p1.json', 'https://api.hunyuan.tencent.com/api/blog/publicList', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ pageNum: 1, pageSize: 20, renderType: 0 }) }]);
const topics = [
  ['learning', '(cat:cs.CL OR cat:cs.LG OR cat:cs.AI) AND (all:"language model" OR all:transformer OR all:"foundation model") AND (all:"pre-training" OR all:"reinforcement learning" OR all:gradient OR all:optimization OR all:architecture OR all:attention OR all:distillation)'],
  ['runtime', '(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF OR cat:cs.CL) AND (all:LLM OR all:"language model") AND (all:inference OR all:training OR all:GPU OR all:communication OR all:memory OR all:parallel OR all:kernel)'],
  ['agent', '(cat:cs.AI OR cat:cs.CL OR cat:cs.IR OR cat:cs.MA) AND (all:"language model" OR all:LLM) AND (all:agent OR all:"tool use" OR all:retrieval OR all:planning)'],
  ['multimodal', '(cat:cs.CV OR cat:cs.RO OR cat:cs.LG) AND (all:"vision language" OR all:"vision-language" OR all:"world model" OR all:"diffusion model" OR all:"flow matching") AND (all:training OR all:architecture OR all:representation)'],
];
for (const [name, query] of topics) {
  const params = new URLSearchParams({ search_query: `${query} AND submittedDate:[202511270000 TO 202511282359]`, start: '0', max_results: '50', sortBy: 'submittedDate', sortOrder: 'descending' });
  requests.push([`arxiv-${name}.xml`, `https://export.arxiv.org/api/query?${params}`]);
}
for (const [name, url, options = {}] of requests) {
  const receipt = { url, options, started: new Date().toISOString() };
  try {
    const response = await fetch(url, { ...options, signal: AbortSignal.timeout(12000) });
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
