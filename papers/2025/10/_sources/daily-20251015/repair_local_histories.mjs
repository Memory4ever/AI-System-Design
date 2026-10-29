import fs from 'node:fs';
import path from 'node:path';
const root=path.dirname(new URL(import.meta.url).pathname);
const ids=fs.readFileSync(path.join(root,'SUP_DATE_20261014.md'),'utf8').match(/```text\n([\s\S]*?)```/)[1].match(/\d{5}/g);
const results=Object.fromEntries(ids.map(id=>[id,[]]));
for(const file of fs.readdirSync(root).filter(x=>/\.(raw|html|json)$/.test(x)&&!x.includes(' 2')&&!x.startsWith('REPAIR'))){
 let t=fs.readFileSync(path.join(root,file),'utf8');
 try{const j=JSON.parse(t);if(typeof j==='string')t=j;}catch{}
 const matches=[...t.matchAll(/\[2510\.(\d{5})v1\]/g)];
 const chunks=matches.length?matches.map((m,i)=>({id:m[1],text:t.slice(m.index,matches[i+1]?.index)})):[{id:(file.match(/(?:abs-|AB_|ABS_)(\d{5})v1/i)||[])[1],text:t}];
 for(const c of chunks){
  if(!results[c.id])continue;
  const text=c.text.replace(/<[^>]*>/g,' ').replace(/\s+/g,' ');
  const history=text.slice(text.indexOf('Submission history'));
  const h=history.match(/\[v1\]\s*(?:[A-Z][a-z]{2}, )?(\d{1,2} [A-Z][a-z]{2} 2025 \d\d:\d\d:\d\d UTC)/);
  if(h)results[c.id].push({file,history:h[1],utc:new Date(h[1]).toISOString(),v1count:[...history.matchAll(/\[v1\]/g)].length});
 }
}
fs.writeFileSync(path.join(root,'REPAIR_LOCAL_HISTORIES.json'),JSON.stringify(results,null,2)+'\n');
console.log(JSON.stringify(Object.fromEntries(Object.entries(results).map(([id,x])=>[id,x.length?x[0]:null])),null,2));
