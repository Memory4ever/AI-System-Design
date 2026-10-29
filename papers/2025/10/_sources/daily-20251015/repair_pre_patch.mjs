import fs from 'node:fs';
const root='papers/2025/10/_sources/daily-20251015/';
const pre=fs.readFileSync(root+(process.argv[2]||'REPAIR_PRE_01.md'),'utf8');
const specs=process.argv[3]?JSON.parse(process.argv[3]):[
 ['books/part-03-multimodal-world-models/23-multimodal-representation.md','SF-2026-ARXIV-2605-30307'],
 ['books/part-07-agent/76-rag.md','SF-2025-ARXIV-2509-18091'],
];
const sections=pre.split(/^## I\d\d /m).slice(1);
let patch='*** Begin Patch\n';
const notes=new Map();
const hunks=new Map();
for(let i=0;i<specs.length;i++){
 const [file,anchor]=specs[i];
 const text=fs.readFileSync(file,'utf8');
 const lines=text.trimEnd().split('\n');
 const context=lines.find(l=>l.includes(anchor));
 const body=sections[i].split('拟正文全文：\n\n')[1].split('\n\n拟本人Review note')[0];
 const note=sections[i].split('\n').find(l=>l.startsWith('- `SF-2025-'));
 if(!context||!body||!note)throw Error('Missing exact PRE fields');
 if(!hunks.has(file))hunks.set(file,[]);
 hunks.get(file).push({line:lines.indexOf(context),text:`@@\n ${context}\n+\n${body.split('\n').map(l=>'+'+l).join('\n')}\n`});
 if(!notes.has(file))notes.set(file,{last:lines.at(-1),rows:[]});
 notes.get(file).rows.push(note);
}
for(const [file,n] of notes){
 patch+=`*** Update File: ${file}\n${hunks.get(file).sort((a,b)=>a.line-b.line).map(h=>h.text).join('')}@@\n ${n.last}\n${n.rows.map(x=>'+\n+'+x).join('\n')}\n`;
}
console.log(JSON.stringify({patch:patch+'*** End Patch'}));
