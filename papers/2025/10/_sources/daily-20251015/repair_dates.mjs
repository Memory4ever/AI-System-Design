import fs from 'node:fs';
import path from 'node:path';
const root=path.dirname(new URL(import.meta.url).pathname);
const source=fs.readFileSync(path.join(root,'SUP_DATE_20261014.md'),'utf8');
const block=source.match(/```text\n([\s\S]*?)```/)[1];
const ids=block.match(/\d{5}/g).filter(x=>!['11683','11690','11602'].includes(x));
const rows=[];
for(const id of ids){
 const url=`https://api.datacite.org/dois/10.48550/arXiv.2510.${id}`;
 const start=new Date().toISOString();
 try{
  const r=await fetch(url,{signal:AbortSignal.timeout(20000)});
  const body=await r.text();
  fs.writeFileSync(path.join(root,`REPAIR_DC_${id}.json`),body);
  const a=JSON.parse(body).data?.attributes;
  rows.push({id,url,start,status:r.status,end:new Date().toISOString(),doi:a?.doi,client:a?.clientId,state:a?.state,registered:a?.registered,created:a?.created,title:a?.titles});
 }catch(e){rows.push({id,url,start,error:String(e)});}
 console.log(JSON.stringify(rows.at(-1)));
}
fs.writeFileSync(path.join(root,'REPAIR_DC_SUMMARY.json'),JSON.stringify(rows,null,2)+'\n');
