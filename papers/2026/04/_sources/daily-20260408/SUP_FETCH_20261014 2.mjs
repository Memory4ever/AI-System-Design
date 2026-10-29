// Raw public-source acquisition for the Apr07 natural-day supplement only.
import { writeFile } from 'node:fs/promises';
const out=new URL('./',import.meta.url);
const ids=process.argv.slice(2);
const staticRoutes={'deepseek-news-bundle':'https://www.deepseek.com/_next/static/chunks/app/%5Blocale%5D/news/page-79e934c891ab4d7a.js'};
const jobs=ids.map(id=>[id,staticRoutes[id]||(id.endsWith('-html')?'https://arxiv.org/html/2604.'+id.replace('-html','')+'v1':id.endsWith('-doi')?'https://api.datacite.org/dois/10.48550/arxiv.2604.'+id.replace('-doi',''):'https://arxiv.org/abs/2604.'+id+'v1')]);
if(!ids.length){
 const routes=[
  ['model','(cat:cs.CL OR cat:cs.LG) AND (all:"language model" OR all:transformer OR all:"mixture of experts" OR all:"foundation model")'],
  ['system','(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF) AND (all:"language model" OR all:LLM OR all:GPU OR all:inference OR all:"model training")'],
  ['multi','(cat:cs.CV OR cat:cs.RO) AND (all:multimodal OR all:"world model" OR all:"vision language action" OR all:"generative model" OR all:diffusion)'],
  ['agent','(cat:cs.AI OR cat:cs.IR OR cat:cs.MA) AND (all:"language model" OR all:LLM OR all:"foundation model" OR all:"retrieval augmented" OR all:"tool calling")']];
 for(const [id,topic] of routes)jobs.push([id,'https://export.arxiv.org/api/query?'+new URLSearchParams({search_query:'(submittedDate:[202604031800 TO 202604061800]) AND ('+topic+')',start:'0',max_results:'300',sortBy:'submittedDate',sortOrder:'ascending'})]);
 for(const c of ['CL','LG','DC','AI','CV','RO','AR','PL','OS','PF','IR','MA'])jobs.push(['list-'+c,'https://arxiv.org/list/cs.'+c+'/2026-04?skip=0&show=2000']);
}
for(let start=0;start<jobs.length;start+=4){
 await Promise.all(jobs.slice(start,start+4).map(async([id,url])=>{
  const at=new Date().toISOString();let receipt;
  try{const r=await fetch(url,{signal:AbortSignal.timeout(25000)});const b=await r.text();await writeFile(new URL('SUP_'+id+'_20261014.raw',out),b);receipt={id,url,at,status:r.status,bytes:Buffer.byteLength(b)};}
  catch(e){receipt={id,url,at,error:String(e)};}
  await writeFile(new URL('SUP_'+id+'_20261014.request.json',out),JSON.stringify(receipt,null,2)+'\n');console.log(JSON.stringify(receipt));
 }));
}
