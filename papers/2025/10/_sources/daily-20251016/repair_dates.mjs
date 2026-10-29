import fs from 'node:fs';
import path from 'node:path';
const dir = path.dirname(new URL(import.meta.url).pathname);
const note = fs.readFileSync(path.join(dir,'SUP_DATE_20261014.md'),'utf8');
const line = note.split('\n').find(x=>x.startsWith('- 必要公开日未定178'));
const discovery = process.argv[2] === 'discovery';
const discoveryRecords = new Map();
const discoveryOrigins = new Map();
if(discovery){
  const old=note+fs.readFileSync(path.join(dir,'SCREENING.md'),'utf8');
  for(const topic of ['model','agent','multimodal','system']){
    for(const record of JSON.parse(fs.readFileSync(path.join(dir,`REPAIR_DISCOVERY_${topic}.json`),'utf8')).data){
      const id=record.id.split('arxiv.')[1];
      if(id&&!old.includes(id)){
        discoveryRecords.set(id,record);
        discoveryOrigins.set(id,`REPAIR_DISCOVERY_${topic}.json`);
      }
    }
  }
}
const ids = discovery ? [...discoveryRecords.keys()] : [...line.matchAll(/`(\d{4}\.\d{5})`/g)].map(x=>x[1]);
const rows=[];
for (const id of ids) {
  const file=path.join(dir,`REPAIR_DC_${id.replace('.','_')}.json`);
  try {
    if (!discovery && !fs.existsSync(file)) {
      const r=await fetch(`https://api.datacite.org/dois/10.48550/arXiv.${id}`,{signal:AbortSignal.timeout(16000)});
      const body=await r.text(); fs.writeFileSync(file,body);
      fs.writeFileSync(file+'.headers',JSON.stringify({url:r.url,status:r.status,headers:Object.fromEntries(r.headers),time:new Date().toISOString()},null,2));
    }
    const j=discovery ? {data:discoveryRecords.get(id)} : JSON.parse(fs.readFileSync(file,'utf8')); const a=j.data.attributes;
    const v1=a.dates.filter(x=>x.dateType==='Submitted'&&x.dateInformation==='v1');
    let earliest=null;
    if(v1.length===1){
      const t=new Date(v1[0].date);const ny=new Intl.DateTimeFormat('en-CA',{timeZone:'America/New_York',year:'numeric',month:'2-digit',day:'2-digit',hour:'2-digit',hourCycle:'h23'}).formatToParts(t);
      const p=Object.fromEntries(ny.map(x=>[x.type,x.value]));
      const cut=new Date(`${p.year}-${p.month}-${p.day}T18:00:00Z`);
      if(Number(p.hour)>=14)cut.setUTCDate(cut.getUTCDate()+1);
      while([0,6].includes(cut.getUTCDay()))cut.setUTCDate(cut.getUTCDate()+1);
      if(cut.getUTCDay()===5)cut.setUTCDate(cut.getUTCDate()+2);
      earliest=new Date(+cut+6*3600000).toISOString();
    }
    const registered=a.registered; const bjt=x=>new Intl.DateTimeFormat('en-CA',{timeZone:'Asia/Shanghai',year:'numeric',month:'2-digit',day:'2-digit'}).format(new Date(x));
    const valid=j.data.id===`10.48550/arxiv.${id}`&&j.data.relationships.client.data.id==='arxiv.content'&&a.state==='findable'&&v1.length===1&&earliest&&+new Date(earliest)<=+new Date(registered);
    rows.push({id,title:a.titles,v1,earliest,registered,created:a.created,client:j.data.relationships.client.data.id,state:a.state,day:valid&&bjt(earliest)===bjt(registered)?bjt(earliest):null,description:a.descriptions,version:a.version,file:discovery?discoveryOrigins.get(id):path.basename(file)});
  }catch(e){rows.push({id,error:String(e)});}
  fs.writeFileSync(path.join(dir,discovery?'REPAIR_NEW_DATES.json':'REPAIR_DATES.json'),JSON.stringify(rows,null,2));
  console.log(`${rows.length}/${ids.length} ${id} ${rows.at(-1).day??rows.at(-1).error??'unresolved'}`);
}
