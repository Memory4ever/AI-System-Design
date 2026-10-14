import {readFileSync} from 'node:fs';
const [id,pattern='inventory']=process.argv.slice(2);
let b=readFileSync(new URL('SUP_'+id+'-html_20261014.raw',import.meta.url),'utf8');
b=b.replace(/<math[^>]*alttext="([^"]*)"[\s\S]*?<\/math>/g,(_,x)=>' '+x+' ');
const plain=s=>s.replace(/<[^>]*>/g,' ').replace(/&amp;/g,'&').replace(/&#39;/g,"'").replace(/&quot;/g,'"').replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/\s+/g,' ').trim();
const heads=[...b.matchAll(/<h[123][^>]*>[\s\S]*?<\/h[123]>/g)];
for(let i=0;i<heads.length;i++){
 let title=plain(heads[i][0]),body=plain(b.slice(heads[i].index,heads[i+1]?.index));
 if(pattern==='inventory')console.log(i,title,'chars='+body.length);
 else if(new RegExp(pattern,'i').test(title))console.log('\n'+title+'\n'+body);
}
