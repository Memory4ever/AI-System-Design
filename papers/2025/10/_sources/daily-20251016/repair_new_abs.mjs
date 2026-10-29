import fs from 'node:fs';
import path from 'node:path';
const dir=path.dirname(new URL(import.meta.url).pathname);
const ids='12044 12041 11839 11944 12229 12071 12744 11974 12787 11938 12476 12117 12184 12225 11892 12264 12462 12064 12402 12121 12026 12078 11822 12085 11963 12793 12175 12089 12660 12740 12276 12252 12167 12350 12217 12210 12777 12742 12474 12389 12343 12323 12218 12460 12434 11956 12119 11967 11897 11838 12088 12312 12369 12681 12326 12095 12014 11996 11978 11842 11835 11738 12355 12463 12399 12364 12795 12403 12461 12409 12302 12515 12132 12650 12128 12395 12316 11852 12741'.split(' ');
for(const n of ids){
 const file=path.join(dir,`REPAIR_ABS_${n}.html`);
 if(fs.existsSync(file))continue;
 try{const r=await fetch(`https://arxiv.org/abs/2510.${n}v1`,{signal:AbortSignal.timeout(18000)});const body=await r.text();fs.writeFileSync(file,body);fs.writeFileSync(file+'.request.json',JSON.stringify({url:r.url,status:r.status,time:new Date().toISOString()},null,2));console.log(n,r.status,body.length);}catch(e){console.log(n,String(e));}
}
