import fs from 'node:fs/promises';
import path from 'node:path';
const dir=import.meta.dirname;
for(const theme of ['MODEL','TRAIN','AGENT','MULTIMODAL','RUNTIME']){
  const request=JSON.parse(await fs.readFile(path.join(dir,'REPAIR_DISCOVERY_'+theme+'_20261028.json.request.json'),'utf8'));
  const u=new URL(request.url);
  u.searchParams.set('query',u.searchParams.get('query').replace('created:[','registered:['));
  const file=path.join(dir,'REPAIR_REGISTERED_'+theme+'_20261028.json');
  const record={url:u.href,start:new Date().toISOString()};
  try{const r=await fetch(u,{signal:AbortSignal.timeout(45000)});record.status=r.status;await fs.writeFile(file,await r.text());}catch(e){record.error=String(e);}
  record.end=new Date().toISOString();await fs.writeFile(file+'.request.json',JSON.stringify(record,null,2));console.log(theme,record.status,record.error||'');
}
