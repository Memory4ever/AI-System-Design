import fs from 'node:fs/promises';
import { execFileSync } from 'node:child_process';
import path from 'node:path';
const dir = import.meta.dirname;
const text = await fs.readFile(path.join(dir, 'SUP_DATE_20261014.md'), 'utf8');
const ids = [...text.matchAll(/(?:旧113|新44)资格未定（均2510前缀）：([^。]+)。/g)].flatMap(m => m[1].trim().split(',').map(s => '2510.' + s.trim()));
let cursor = 0;
const results = [];
async function worker() {
  while (cursor < ids.length) {
    const id = ids[cursor++];
    const url = 'https://api.datacite.org/dois/10.48550/arXiv.' + id;
    const filename = path.join(dir, 'REPAIR_DC_' + id + '_20261028.json');
    try {
      const response = await fetch(url, { signal: AbortSignal.timeout(45000) });
      const raw = await response.text();
      await fs.writeFile(filename, raw);
      await fs.writeFile(filename + '.request.json', JSON.stringify({url,status:response.status,checked:new Date().toISOString()}, null, 2));
      const result = JSON.parse(execFileSync('python3', ['scripts/arxiv_publication_date.py', filename, '--arxiv-id', id], {cwd:path.resolve(dir,'../../../../../'),encoding:'utf8'}));
      results.push(result);
    } catch (e) {
      if (e.stdout) { try {results.push(JSON.parse(e.stdout));continue;} catch {} }
      results.push({arxiv_id:id,status:'request_error',error:String(e)});
    }
  }
}
await Promise.all(Array.from({length:6}, worker));
results.sort((a,b)=>a.arxiv_id.localeCompare(b.arxiv_id));
await fs.writeFile(path.join(dir, 'REPAIR_DATES_20261028.json'), JSON.stringify(results,null,2));
const counts = {};
for (const r of results) { const key = r.bounded_bjt_date || r.reasons?.join(',') || r.status; counts[key]=(counts[key]||0)+1; }
console.log(JSON.stringify({count:ids.length,counts},null,2));
