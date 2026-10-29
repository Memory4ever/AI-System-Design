// This day's bounded official index snapshots, not a paper-review queue.
import { writeFile } from 'node:fs/promises';
const out = new URL('./', import.meta.url);
const requests = [
 ['openai-research','https://openai.com/research/'],
 ['openai-rss','https://openai.com/news/rss.xml'],
 ['anthropic','https://www.anthropic.com/research'],
 ['google-blog','https://research.google/blog/2026/04/'],
 ['google-pubs','https://research.google/pubs/'],
 ['deepmind','https://deepmind.google/research/publications/'],
 ['meta','https://ai.meta.com/research/'],
 ['qwen','https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US'],
 ['deepseek','https://www.deepseek.com/news/'],
 ['deepseek-home','https://www.deepseek.com/'],
 ['moonshot','https://platform.kimi.com/blog'],
 ['hunyuan','https://api.hunyuan.tencent.com/api/blog/publicList',{method:'POST',body:JSON.stringify({pageNum:1,pageSize:100,renderType:0}),headers:{'Content-Type':'application/json'}}],
 ['zai','https://www.zhipuai.cn/zh/research'],
 ['zai-releases','https://docs.z.ai/release-notes/new-released'],
 ['seed-papers','https://seed.bytedance.com/api/get_article_list_v2?article_type=1&count=20&order_desc=true&page_token=40',{headers:{'x-tt-locale':'US'}}],
 ['seed-blog','https://seed.bytedance.com/api/get_article_list_v2?article_type=2&count=20&order_desc=true&page_token=0',{headers:{'x-tt-locale':'US'}}],
 ['ernie','https://ernie.baidu.com/blog/zh/'],
 ['mimo','https://mimo.xiaomi.com/'],
 ['minimax','https://www.minimax.io/blog'],
 ['minimax-zh','https://www.minimaxi.com/blog'],
 ['minimax-agent','https://agent.minimax.io/docs/llms.txt'],
 ['minimax-techblog','https://agent.minimaxi.com/docs/techblog.md'],
 ['arxiv-rules','https://info.arxiv.org/help/availability.html'],
 ['arxiv-cl-april','https://arxiv.org/list/cs.CL/2026-04?skip=0&show=2000'],
];
await Promise.all(requests.map(async ([id,url,options={}]) => {
 const at=new Date().toISOString();
 try {
  const response=await fetch(url,{...options,signal:AbortSignal.timeout(25000)});
  const body=await response.text();
  await writeFile(new URL('SUP_'+id+'_20261013.raw',out),body);
  const receipt={id,url,at,status:response.status,bytes:Buffer.byteLength(body),request:options};
  await writeFile(new URL('SUP_'+id+'_20261013.request.json',out),JSON.stringify(receipt,null,2)+'\n');
  console.log(JSON.stringify(receipt));
 } catch(error) {
  const receipt={id,url,at,error:String(error),request:options};
  await writeFile(new URL('SUP_'+id+'_20261013.request.json',out),JSON.stringify(receipt,null,2)+'\n');
  console.log(JSON.stringify(receipt));
 }
}));
