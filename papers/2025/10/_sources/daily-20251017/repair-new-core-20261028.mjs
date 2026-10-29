import fs from 'node:fs/promises';
import path from 'node:path';
const dir=import.meta.dirname;
const ids='13251 13253 13262 13272 13276 13281 13285 13293 13308 13312 13315 13328 13329 13334 13344 13363 13367 13375 13394 13401 13406 13418 13419 13444 13451 13454 13462 13512 13543 13551 13554 13558 13580 13598 13614 13622 13632 13680 13713 13744 13747 13787'.split(' ');
const queue=ids.map(id=>({url:'https://arxiv.org/html/2510.'+id+'v1',name:'REPAIR_NEW_CORE_2510.'+id+'_20261028.html'}));
for(const id of '13255 13320 13343 13358 13371 13660 13760 13794'.split(' '))queue.push({url:'https://arxiv.org/abs/2510.'+id+'v1',name:'REPAIR_ABS_2510.'+id+'_20261028.html'});
queue.push({url:'https://arxiv.org/html/2510.13748v1',name:'REPAIR_RECOVERY_CORE_2510.13748_20261028.html'});
let i=0;
async function worker(){while(i<queue.length){let q=queue[i++],file=path.join(dir,q.name),rec={url:q.url,start:new Date().toISOString()};try{let r=await fetch(q.url,{signal:AbortSignal.timeout(90000)});rec.status=r.status;await fs.writeFile(file,await r.text());}catch(e){rec.error=String(e);}rec.end=new Date().toISOString();await fs.writeFile(file+'.request.json',JSON.stringify(rec,null,2));console.log(q.name,rec.status,rec.error||'');}}
await Promise.all(Array.from({length:4},worker));
