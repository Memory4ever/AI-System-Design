import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
const root='papers/2025/10/_sources/daily-20251015/';
const file='papers/2025/10/15/README.md';
const text=fs.readFileSync(file,'utf8');
const baseline=fs.readFileSync('/tmp/daily-20251015-baseline-20261028.md','utf8');
const assert=(test,msg)=>{if(!test)throw Error(msg);};
const oldRow=baseline.split('\n').find(l=>l.startsWith('| [Part II: ROLL Flash'));
const old4=baseline.split('## 4. 证据与知识整合\n\n')[1].split('\n## 5. 缺口与下一步')[0].trimEnd();
assert(text.includes(oldRow),'Old row changed');
assert(text.includes(old4),'Continuous old section4 changed');
assert(text.split('\n').find(l=>l.startsWith('**窗口：**'))===baseline.split('\n').find(l=>l.startsWith('**窗口：**')),'Hour window changed');
assert((text.match(/^## /gm)||[]).length===6,'Not six H2');
const table=text.split('## 3. 候选与判断')[1].split('## 4. 证据与知识整合')[0];
const ids=[...table.matchAll(/^\| \[.*?\]\(https:\/\/arxiv.org\/abs\/2510\.(\d{5})v1\)/gm)].map(m=>m[1]);
const evidence=text.split('## 4. 证据与知识整合')[1].split('## 5. 缺口与下一步')[0];
const evidenceIds=[...evidence.matchAll(/^### \[.*?\]\(https:\/\/arxiv.org\/abs\/2510\.(\d{5})v1\)/gm)].map(m=>m[1]);
assert(ids.length===29&&new Set(ids).size===29,'Candidate family count');
assert(JSON.stringify([...ids].sort())===JSON.stringify([...evidenceIds].sort()),'Candidate/evidence identity mismatch');
assert(new Set([...text.matchAll(/^\| (SRC-[A-Z-]+) \|/gm)].map(m=>m[1])).size===14,'Daily source count');
const books=new Set();
const roadmapPaths=[...fs.readFileSync('ROADMAP.md','utf8').matchAll(/`(books\/[^`]+\.md)`/g)].map(m=>m[1]);
let integrations=0;
for(let n=1;n<=8;n++){
 const pre=fs.readFileSync(root+`REPAIR_PRE_${String(n).padStart(2,'0')}.md`,'utf8');
 let book;
 for(const section of pre.split(/^## I\d\d /m).slice(1)){
  const explicit=section.match(/文件 `([^`]+\.md)`/);
  if(explicit)book=explicit[1];
  const short=section.match(/精确插入：`([^`]+\.md)`/);
  if(short)book=roadmapPaths.find(p=>p.endsWith('/'+short[1]));
  assert(book,'Missing inherited book');
  const body=section.split('拟正文全文：\n\n')[1].split('\n\n拟本人Review note')[0];
  const note=section.split('\n').find(l=>l.startsWith('- `SF-2025-'));
  const actual=fs.readFileSync(book,'utf8');
  assert(actual.includes(body),'Full approved body missing '+book);
  assert(actual.split(note).length===2,'Own note missing/duplicated '+book);
  const marker=body.match(/^<!-- source-family:SF-2025-ARXIV-2510-\d{5} -->$/m)?.[0];
  assert(marker&&actual.split(marker).length===2,'Standalone marker missing/duplicated');
  books.add(book);integrations++;
 }
}
assert(integrations===25,'Expected actual saved integrations');
const missing=[];
let refs=0;
const targets=new Set();
for(const m of text.matchAll(/\[[^\]]*\]\(([^)]+)\)/g)){
 let target=m[1].trim().replace(/^<|>$/g,'');
 if(/^(?:https?:|mailto:|#)/.test(target))continue;
 target=decodeURIComponent(target.split('#')[0]);
 const resolved=path.resolve(path.dirname(file),target);
 refs++;targets.add(resolved);
 if(!fs.existsSync(resolved))missing.push(target);
}
assert(missing.length===0,'Missing local refs '+missing.join(', '));
console.log(JSON.stringify({report:file,sha256:crypto.createHash('sha256').update(text).digest('hex'),candidateFamilies:ids.length,evidenceItems:evidenceIds.length,savedFullApprovedBodies:integrations,bookFiles:books.size,localReferences:refs,uniqueLocalTargets:targets.size,missing,oldRow:true,oldHourWindow:true,continuousOldSection4:true,sixH2:true,dailySources:14},null,2));
