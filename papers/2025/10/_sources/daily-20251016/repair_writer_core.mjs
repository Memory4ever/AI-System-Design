import fs from 'node:fs';
import path from 'node:path';
const dir=path.dirname(new URL(import.meta.url).pathname);
const ids='12159 12195 12370 12387 12392 12497 12537 12547 12548 12560 12581 12638 12643 12691 12693 12709 12720 12721 12722 12747 12784 12789 12796 12801 12787 12350 12326 12355 12463 12795 12461 12515 12132 11852 12741 12587 12608 12637 12668 12672 12689 12697 12702 12710 12200 12717 12724 12728 12749 12750 12785'.split(' ');
for(const n of ids){
 const file=path.join(dir,`REPAIR_CORE_${n}.html`);
 if(fs.existsSync(file))continue;
 try{const r=await fetch(`https://arxiv.org/html/2510.${n}v1`,{signal:AbortSignal.timeout(22000)});const body=await r.text();fs.writeFileSync(file,body);fs.writeFileSync(file+'.request.json',JSON.stringify({url:r.url,status:r.status,time:new Date().toISOString()},null,2));console.log(n,r.status,body.length);}catch(e){console.log(n,String(e));}
}
