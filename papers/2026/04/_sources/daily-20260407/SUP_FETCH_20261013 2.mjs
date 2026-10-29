// Bounded title/abstract discovery leads; submittedDate is not a public-date filter.
import { writeFile } from 'node:fs/promises';
const out=new URL('./',import.meta.url);
const routes=[
 ['model','(cat:cs.CL OR cat:cs.LG) AND (all:"language model" OR all:transformer OR all:"mixture of experts" OR all:"foundation model")'],
 ['system','(cat:cs.DC OR cat:cs.AR OR cat:cs.PL OR cat:cs.OS OR cat:cs.PF) AND (all:"language model" OR all:LLM OR all:GPU OR all:inference OR all:"model training")'],
 ['multi','(cat:cs.CV OR cat:cs.RO) AND (all:multimodal OR all:"world model" OR all:"vision language action" OR all:"generative model" OR all:diffusion)'],
 ['agent','(cat:cs.AI OR cat:cs.IR OR cat:cs.MA) AND (all:"language model" OR all:LLM OR all:"foundation model" OR all:"retrieval augmented" OR all:"tool calling")'],
];
const requests=routes.map(([id,topic])=>[id,'https://export.arxiv.org/api/query?'+new URLSearchParams({search_query:'(submittedDate:[202604021800 TO 202604031800]) AND ('+topic+')',start:'0',max_results:'300',sortBy:'submittedDate',sortOrder:'ascending'})]);
requests.push(['dc-april','https://arxiv.org/list/cs.DC/2026-04?skip=0&show=500']);
requests.push(['cl-tail','https://arxiv.org/list/cs.CL/2026-04?skip=2000&show=1000']);
for(const [id,url] of requests){
 if(id!=='cl-tail')continue; // only recover the missing bounded official-list tail, preserve earlier attempts
 const at=new Date().toISOString();let receipt;
 try{const r=await fetch(url,{signal:AbortSignal.timeout(25000)});const b=await r.text();await writeFile(new URL('SUP_'+id+'_20261013.raw',out),b);receipt={id,url,at,status:r.status,bytes:Buffer.byteLength(b)};}
 catch(e){receipt={id,url,at,error:String(e)};}
 await writeFile(new URL('SUP_'+id+'_20261013.request.json',out),JSON.stringify(receipt,null,2)+'\n');console.log(JSON.stringify(receipt));
}
