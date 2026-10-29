import fs from 'node:fs';
import path from 'node:path';
const dir=path.dirname(new URL(import.meta.url).pathname);
const topics={model:'"language model" OR "language models" OR transformer OR transformers OR "mixture of experts"',agent:'"LLM agent" OR "LLM agents" OR "tool calling" OR "retrieval augmented"',multimodal:'"vision language" OR "world model" OR "world models" OR "foundation model" OR "foundation models"',system:'"GPU" AND ("inference" OR "training" OR "kernel" OR "serving")'};
for(const [name,topic]of Object.entries(topics)){
 const query=`registered:[2025-10-14T16:00:00Z TO 2025-10-15T15:59:59Z] AND (${topic})`;
 const u=new URL('https://api.datacite.org/dois');u.searchParams.set('client-id','arxiv.content');u.searchParams.set('query',query);u.searchParams.set('page[size]','100');
 const r=await fetch(u,{signal:AbortSignal.timeout(25000)});const body=await r.text();fs.writeFileSync(path.join(dir,`REPAIR_DISCOVERY_${name}.json`),body);fs.writeFileSync(path.join(dir,`REPAIR_DISCOVERY_${name}.request.json`),JSON.stringify({url:String(u),query,status:r.status,time:new Date().toISOString(),stop:'first page, at most 100; thematic discovery only'},null,2));
 console.log(name,r.status,JSON.parse(body).meta);
}
