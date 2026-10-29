import fs from 'node:fs/promises';
import path from 'node:path';
const dir=import.meta.dirname;
const rows=JSON.parse(await fs.readFile(path.join(dir,'REPAIR_DISCOVERY_DELTA_20261028.json'),'utf8'));
const outside=new Set('13255 13316 13320 13343 13358 13359 13364 13371 13390 13432 13439 13441 13488 13493 13513 13582 13592 13604 13645 13660 13688 13729 13760 13763 13768 13774 13794 13805'.split(' '));
const queue=rows.filter(r=>r.id>='2510.13250'&&!outside.has(r.id.split('.')[1]));
let i=0;
async function worker(){while(i<queue.length){const r=queue[i++],url='https://arxiv.org/abs/'+r.id+'v1',file=path.join(dir,'REPAIR_ABS_'+r.id+'_20261028.html');const record={url,start:new Date().toISOString()};try{let res=await fetch(url,{signal:AbortSignal.timeout(45000)});record.status=res.status;let raw=await res.text();await fs.writeFile(file,raw);}catch(e){record.error=String(e);}record.end=new Date().toISOString();await fs.writeFile(file+'.request.json',JSON.stringify(record,null,2));console.log(r.id,record.status,record.error||'');}}
await Promise.all(Array.from({length:4},worker));
