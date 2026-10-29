import fs from 'node:fs';
import path from 'node:path';
const dir = path.dirname(new URL(import.meta.url).pathname);
for (const field of ['created','registered']) {
  const query = `client.id:arxiv.content AND ${field}:[2025-10-19T16:00:00Z TO 2025-10-20T15:59:59Z] AND titles.title:("mixture of experts") AND doi:"10.48550/arxiv.2510.15333"`;
  const url = new URL('https://api.datacite.org/dois');
  url.searchParams.set('query',query);
  url.searchParams.set('page[size]','100');
  const res = await fetch(url,{signal:AbortSignal.timeout(45000)});
  const raw = await res.text();
  fs.writeFileSync(path.join(dir, `REPAIR_DC_VALID_POSITIVE_${field.toUpperCase()}_20261029.json`),raw);
  const d=JSON.parse(raw);
  console.log(JSON.stringify({url:String(url),status:res.status,total:d.meta.total,ids:d.data.map(x=>x.id)}));
}
