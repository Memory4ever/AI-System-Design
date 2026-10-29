// Exact v1 abstract probes after bounded title discovery and candidate membership checks.
import {writeFile} from 'node:fs/promises';
const out=new URL('./',import.meta.url);
const ids=['02338','02355','02371','02492','02556','02570','02689','02751','02817','02870','02956','02979','03072','03114','03231'];
await Promise.all(ids.map(async id=>{
 const url=`https://arxiv.org/abs/2604.${id}v1`,at=new Date().toISOString();let rec;
 try{const r=await fetch(url,{signal:AbortSignal.timeout(25000)}),b=await r.text();await writeFile(new URL(`SUP_${id}-ab_20261014.raw`,out),b);rec={url,at,status:r.status,bytes:Buffer.byteLength(b)};}
 catch(e){rec={url,at,error:String(e)};}
 await writeFile(new URL(`SUP_${id}-ab_20261014.request.json`,out),JSON.stringify(rec,null,2)+'\n');console.log(JSON.stringify(rec));
}));
