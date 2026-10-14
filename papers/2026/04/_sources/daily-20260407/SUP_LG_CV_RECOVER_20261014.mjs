// Official monthly listings used only as bounded title leads for batch 02333–03231.
import {writeFile} from 'node:fs/promises';
const out=new URL('./',import.meta.url);
await Promise.all(['LG','CV'].map(async cat=>{
 const url=`https://arxiv.org/list/cs.${cat}/2026-04?skip=0&show=2000`,at=new Date().toISOString();
 let rec;
 try {const r=await fetch(url,{signal:AbortSignal.timeout(25000)}),b=await r.text();await writeFile(new URL(`SUP_${cat.toLowerCase()}-april_20261014.raw`,out),b);rec={url,at,status:r.status,bytes:Buffer.byteLength(b)};}
 catch(e){rec={url,at,error:String(e)};}
 await writeFile(new URL(`SUP_${cat.toLowerCase()}-april_20261014.request.json`,out),JSON.stringify(rec,null,2)+'\n');console.log(JSON.stringify(rec));
}));
