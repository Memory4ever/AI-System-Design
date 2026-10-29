import fs from 'node:fs/promises';
import path from 'node:path';
const dir=import.meta.dirname;
const dates=JSON.parse(await fs.readFile(path.join(dir,'REPAIR_DATES_20261028.json'),'utf8'));
const queue=[];
for(const row of dates.filter(r=>r.bounded_bjt_date==='2025-10-16'&&r.arxiv_id>='2510.13700')){
  try{await fs.access(path.join(dir,row.arxiv_id+'v1-core.html'));}
  catch{queue.push({name:'REPAIR_CORE_'+row.arxiv_id+'_20261028.html',url:'https://arxiv.org/html/'+row.arxiv_id+'v1'});}
}
const themes={MODEL:'"language model" OR transformer OR "mixture of experts"',TRAIN:'"language model training" OR "reinforcement learning" OR alignment',AGENT:'"LLM agent" OR "retrieval augmented" OR "tool calling" OR "agent memory"',MULTIMODAL:'"vision language" OR "world model" OR "diffusion model" OR "vision language action"',RUNTIME:'"LLM inference" OR "GPU kernel" OR "model serving" OR "distributed training"'};
for(const [name,terms] of Object.entries(themes)){
  const u=new URL('https://api.datacite.org/dois');
  u.searchParams.set('client-id','arxiv.content');
  u.searchParams.set('query','created:[2025-10-15T16:00:00Z TO 2025-10-16T15:59:59Z] AND (titles.title:('+terms+') OR descriptions.description:('+terms+'))');
  u.searchParams.set('page[size]','100');
  queue.push({name:'REPAIR_DISCOVERY_'+name+'_20261028.json',url:u.href});
}
let cursor=0;
async function worker(){while(cursor<queue.length){const q=queue[cursor++];let record={url:q.url,start:new Date().toISOString()};try{let r=await fetch(q.url,{signal:AbortSignal.timeout(45000)});record.status=r.status;await fs.writeFile(path.join(dir,q.name),await r.text());}catch(e){record.error=String(e);}record.end=new Date().toISOString();await fs.writeFile(path.join(dir,q.name+'.request.json'),JSON.stringify(record,null,2));console.log(q.name,record.status||record.error);}}
await Promise.all(Array.from({length:4},worker));
