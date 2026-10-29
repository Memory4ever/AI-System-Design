import fs from 'node:fs';
import path from 'node:path';
const dir=path.dirname(new URL(import.meta.url).pathname);
const exact='doi:"10.48550/arxiv.2510.15333"';
const queries={EXACT:exact,CLIENT:exact+' AND client.client-id:arxiv.content',DATE:exact+' AND registered:[2025-10-19T16:00:00Z TO 2025-10-20T15:59:59Z]',TITLE:exact+' AND titles.title:("mixture of experts")',CLIENTID:exact+' AND client.id:arxiv.content'};
for(const [name,query] of Object.entries(queries)){
 const url=new URL('https://api.datacite.org/dois');url.searchParams.set('query',query);
 const r=await fetch(url,{signal:AbortSignal.timeout(45000)});const raw=await r.text();fs.writeFileSync(path.join(dir,`REPAIR_QUERY_DEBUG_${name}_20261029.json`),raw);const d=JSON.parse(raw);console.log(JSON.stringify({name,url:String(url),total:d.meta.total}));
}
