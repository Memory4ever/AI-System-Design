import {writeFile} from 'node:fs/promises';
const out=new URL('./',import.meta.url);
const req=[];
for(const id of ['02990']){req.push([id+'-v1','https://arxiv.org/html/2604.'+id+'v1']);req.push([id+'-doi','https://api.datacite.org/dois/10.48550/arxiv.2604.'+id]);}
await Promise.all(req.map(async([id,url])=>{const at=new Date().toISOString();let rec;try{const r=await fetch(url,{signal:AbortSignal.timeout(25000)}),b=await r.text();await writeFile(new URL('SUP_'+id+'_20261013.raw',out),b);rec={url,at,status:r.status,bytes:Buffer.byteLength(b)};}catch(e){rec={url,at,error:String(e)};}await writeFile(new URL('SUP_'+id+'_20261013.request.json',out),JSON.stringify(rec,null,2)+'\n');console.log(JSON.stringify(rec));}));
