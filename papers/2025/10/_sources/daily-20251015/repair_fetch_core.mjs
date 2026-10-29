import fs from 'node:fs';
import path from 'node:path';
import {spawnSync} from 'node:child_process';
const root=path.dirname(new URL(import.meta.url).pathname);
const ids='11012 11031 11062 11210 11302 11307 11370 11414 11509 11512 11529 11538 11558 11588 11598 11631 11677 11682 11686 11693 11696 11715'.split(' ');
for(const id of ids){
 const url=`https://arxiv.org/html/2510.${id}v1`;
 const start=new Date().toISOString();
 const r=spawnSync('curl',['-L','--max-time','25','-sS','-D',path.join(root,`REPAIR_CORE_${id}.headers`),url,'-o',path.join(root,`REPAIR_CORE_${id}.html`),'-w','%{http_code} %{size_download}'],{encoding:'utf8'});
 console.log(JSON.stringify({id,url,start,end:new Date().toISOString(),exit:r.status,result:r.stdout,error:r.stderr}));
 await new Promise(r=>setTimeout(r,3100));
}
