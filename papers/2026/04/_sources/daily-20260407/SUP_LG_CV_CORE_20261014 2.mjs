// Exact raw capture for 15 potential leads; fetching is not admission or Source completion.
import {writeFile} from 'node:fs/promises';
const out=new URL('./',import.meta.url);
const ids=['02338','02355','02371','02492','02556','02570','02689','02751','02817','02870','02956','02979','03072','03114','03231'];
const req=ids.flatMap(id=>[[id+'-v1',`https://arxiv.org/html/2604.${id}v1`],[id+'-doi',`https://api.datacite.org/dois/10.48550/arxiv.2604.${id}`]]);
await Promise.all(req.map(async([name,url])=>{const at=new Date().toISOString();let rec;
 try{const r=await fetch(url,{signal:AbortSignal.timeout(25000)}),b=await r.text();await writeFile(new URL(`SUP_${name}_20261014.raw`,out),b);rec={url,at,status:r.status,bytes:Buffer.byteLength(b)};}
 catch(e){rec={url,at,error:String(e)};}
 await writeFile(new URL(`SUP_${name}_20261014.request.json`,out),JSON.stringify(rec,null,2)+'\n');console.log(JSON.stringify(rec));
}));
