import { spawnSync } from 'node:child_process';
import { readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = dirname(fileURLToPath(import.meta.url));
const requests = [
  ['openai-research', 'https://openai.com/research/'],
  ['openai-rss', 'https://openai.com/news/rss.xml'],
  ['anthropic', 'https://www.anthropic.com/research'],
  ['deepmind', 'https://deepmind.google/research/'],
  ['google-pubs', 'https://research.google/pubs/'],
  ['google-blog-month', 'https://research.google/blog/2025/11/'],
  ['meta', 'https://ai.meta.com/research/'],
  ['qwen', 'https://qwenlm.github.io/'],
  ['deepseek', 'https://www.deepseek.com/'],
  ['deepseek-news', 'https://www.deepseek.com/news'],
  ['kimi', 'https://platform.kimi.com/blog'],
  ['hunyuan', 'https://hunyuan.tencent.com/research'],
  ['zai', 'https://www.zhipuai.cn/zh/research'],
  ['seed', 'https://seed.bytedance.com/en/research'],
  ['ernie', 'https://ernie.baidu.com/blog/zh/'],
  ['mimo', 'https://mimo.xiaomi.com/'],
  ['minimax-en', 'https://www.minimax.io/blog'],
  ['minimax-cn', 'https://www.minimaxi.com/blog'],
  ['minimax-tech', 'https://agent.minimax.io/docs/techblog.md'],
];

const follow = [
  ['qwen-research', 'https://qwen.ai/research'],
  ['deepseek-news-js', 'https://www.deepseek.com/_next/static/chunks/app/%5Blocale%5D/news/page-79e934c891ab4d7a.js'],
  ['zai-p2', 'https://www.zhipuai.cn/zh/research?page=2'],
  ['ernie-p2', 'https://ernie.baidu.com/blog/zh/page/2/'],
  ['seed-1-0', 'https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2025&count=20&page_token=0&order_desc=true', ['x-tt-locale:US']],
  ['seed-1-20', 'https://seed.bytedance.com/api/get_article_list_v2?article_type=1&publish_year=2025&count=20&page_token=20&order_desc=true', ['x-tt-locale:US']],
  ['seed-2-0', 'https://seed.bytedance.com/api/get_article_list_v2?article_type=2&publish_year=2025&count=20&page_token=0&order_desc=true', ['x-tt-locale:US']],
  ['seed-2-20', 'https://seed.bytedance.com/api/get_article_list_v2?article_type=2&publish_year=2025&count=20&page_token=20&order_desc=true', ['x-tt-locale:US']],
  ['hunyuan-api', 'https://api.hunyuan.tencent.com/api/blog/publicList', ['Content-Type: application/json'], '{"pageNum":1,"pageSize":20,"renderType":0}'],
  ['minimax-index', 'https://agent.minimaxi.com/docs/llms.txt'],
  ['mimo-index', 'https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/index.c5195ace.js'],
  ['qwen-home-js', 'https://g.alicdn.com/qwenweb/qwen-ai-fe/0.0.85/js/p_home-index.js'],
  ['qwen-layout-js', 'https://g.alicdn.com/qwenweb/qwen-ai-fe/0.0.85/js/p_layout.js'],
  ['qwen-shared-js', 'https://g.alicdn.com/qwenweb/qwen-ai-fe/0.0.85/js/9e22d361.js'],
  ['mimo-blog-js', 'https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/8557.2d420be2.js'],
  ['mimo-list-js', 'https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/6159.4efb0769.js'],
  ['mimo-blog-async-js', 'https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/async/8557.2d420be2.js'],
  ['mimo-list-async-js', 'https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/async/6159.4efb0769.js'],
];
const arxiv = [['model', 'language model'], ['gpu', 'GPU'], ['agent', 'agent'], ['vision', 'vision-language'], ['world', 'world model']].map(([name, term]) => {
  const params = new URLSearchParams({ advanced: '1', 'terms-0-operator': 'AND', 'terms-0-term': term, 'terms-0-field': 'title', 'classification-computer_science': 'y', 'classification-include_cross_list': 'include', 'date-filter_by': 'date_range', 'date-from_date': '2025-11-17', 'date-to_date': '2025-11-18', 'date-date_type': 'submitted_date_first', abstracts: 'show', size: '50', order: '-announced_date_first' });
  return [`arxiv-${name}`, `https://arxiv.org/search/advanced?${params}`];
});
const current = ['2511.17599', '2511.17593', '2511.14813', '2511.14086', '2511.13892', '2511.13717', '2511.13647', '2511.13548', '2511.13494', '2511.13478', '2511.13420', '2511.13371', '2511.13240', '2511.13225', '2511.13189', '2511.13095', '2511.13052', '2511.13036', '2511.13029', '2511.13023', '2511.13940', '2512.00047', '2511.14136', '2511.13998', '2511.13860', '2511.13614', '2511.13593', '2511.13305', '2511.13297', '2511.13288', '2511.13248', '2511.13193', '2511.13137', '2511.13118', '2511.13087', '2511.12998', '2511.14131', '2511.13021', '2512.00045', '2511.14101', '2511.13410', '2511.13293', '2511.13103', '2511.21707', '2511.13646', '2511.12997'].map(id => [`current-${id}`, `https://arxiv.org/abs/${id}`]);
const qwen = [
  ['qwen-retrieval', 'https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US'],
  ['qwen-config-zh', 'https://qwen.ai/api/page_config?code=research.research-list&language=zh-cn'],
];
const selected = process.argv[4] === 'qwen' ? qwen : process.argv[4] === 'current' ? current : process.argv[4] === 'arxiv' ? arxiv : process.argv[4] === 'follow' ? follow : requests;
for (const [name, url, headers = [], data] of selected.slice(Number(process.argv[2] ?? 0), Number(process.argv[3] ?? selected.length))) {
  if (/arxiv\.org\/(?:api|rss|oai)/i.test(url)) throw new Error('Legacy arXiv requires a root lease');
  const stem = join(root, `SUP_${name}_20261015`);
  const checked = new Date().toISOString();
  const args = ['-L', '--connect-timeout', '8', '--max-time', '20', '--retry', '0', '-sS', '-A', 'Mozilla/5.0', '-D', `${stem}.headers`, '-o', `${stem}.raw`, '-w', '%{http_code}\n%{url_effective}'];
  for (const header of headers) args.push('-H', header);
  if (data !== undefined) args.push('--data', data);
  args.push(url);
  const result = spawnSync('curl', args, { encoding: 'utf8', timeout: 25000 });
  let bytes = 0;
  try { bytes = readFileSync(`${stem}.raw`).length; } catch {}
  const receipt = { name, url, checked, method: data === undefined ? 'GET' : 'POST', headers, data, exitCode: result.status, transport: result.stdout?.trim(), bytes, error: result.stderr?.trim() || String(result.error ?? '') };
  writeFileSync(`${stem}.request.json`, `${JSON.stringify(receipt, null, 2)}\n`);
  console.log(JSON.stringify(receipt));
}
