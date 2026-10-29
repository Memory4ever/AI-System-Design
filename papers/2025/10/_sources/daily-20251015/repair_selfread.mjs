import fs from 'node:fs';
const specs=JSON.parse(process.argv[2]);
for(const [file,id] of specs){
 const text=fs.readFileSync(file,'utf8');
 const blocks=text.split(/\n\s*\n/);
 const marker=`<!-- source-family:SF-2025-ARXIV-2510-${id} -->`;
 const i=blocks.findIndex(x=>x.trim()===marker);
 if(i<1)throw Error('Missing standalone marker '+id);
 const isMeta=x=>!x||x.trim().startsWith('<!--')||x.trim().startsWith('#');
 let before=i-2,after=i+1;
 while(before>=0&&isMeta(blocks[before]))before--;
 while(after<blocks.length&&isMeta(blocks[after]))after++;
 const note=text.split('\n').find(x=>x.startsWith(`- \`SF-2025-ARXIV-2510-${id}\``));
 console.log(JSON.stringify({file,id,before:blocks[before],body:blocks[i-1],marker,after:blocks[after],note},null,2));
}
