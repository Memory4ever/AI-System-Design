import { writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
const root = dirname(fileURLToPath(import.meta.url));
const requests = [
  ['openai-rss.xml', 'https://openai.com/news/rss.xml'],
  ['anthropic.html', 'https://www.anthropic.com/research'],
  ['deepmind.html', 'https://deepmind.google/blog/page/5/'],
  ['google-pubs.html', 'https://research.google/pubs/'],
  ['meta.html', 'https://ai.meta.com/research/'],
  ['qwen.html', 'https://qwen.ai/research'],
  ['deepseek.html', 'https://www.deepseek.com/'],
  ['kimi.html', 'https://platform.kimi.com/blog'],
  ['hunyuan.html', 'https://hunyuan.tencent.com/research'],
  ['hunyuan-p1.json', 'https://api.hunyuan.tencent.com/api/blog/publicList', {pageNum:1,pageSize:20,renderType:0}],
  ['zai-p1.html', 'https://www.zhipuai.cn/zh/research'],
  ['zai-p2.html', 'https://www.zhipuai.cn/zh/research?page=2'],
  ['ernie-p1.html', 'https://ernie.baidu.com/blog/zh/'],
  ['ernie-p2.html', 'https://ernie.baidu.com/blog/zh/page/2/'],
  ['mimo.html', 'https://mimo.xiaomi.com/'],
  ['minimax.html', 'https://www.minimax.io/blog'],
  ['minimax-cn.html', 'https://www.minimaxi.com/blog'],
  ['arxiv-availability.html', 'https://info.arxiv.org/help/availability.html'],
];
for (const type of [1,2]) for (const token of [0,20]) requests.push([`seed-t${type}-p${token}.json`, `https://seed.bytedance.com/api/get_article_list_v2?article_type=${type}&publish_year=2025&count=20&page_token=${token}&order_desc=true`]);
const selected = process.argv[2] ? [[process.argv[2],process.argv[3]]] : requests;
for (const [name,url,body] of selected) {
  const receipt = {url, checked:new Date().toISOString(), method:body?'POST':'GET', body:body||null};
  try {
    const options={signal:AbortSignal.timeout(30000),headers:{'x-tt-locale':'US'}};
    if(body) Object.assign(options,{method:'POST',body:JSON.stringify(body),headers:{...options.headers,'Content-Type':'application/json'}});
    const response=await fetch(url,options);
    const content=await response.text();
    writeFileSync(join(root,name),content);
    Object.assign(receipt,{status:response.status,finalUrl:response.url,bytes:Buffer.byteLength(content)});
  } catch(error) {receipt.error=String(error);}
  writeFileSync(join(root,`${name}.receipt.json`),JSON.stringify(receipt,null,2));
  console.log(JSON.stringify({name,...receipt}));
}
