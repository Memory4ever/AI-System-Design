import fs from 'node:fs/promises';
import path from 'node:path';
const dir = import.meta.dirname;
for (const id of process.argv.slice(2)) {
  const file = path.join(dir, `REPAIR_NEW_CORE_2510.${id}_20261028.html`);
  const rec = {url: `https://arxiv.org/html/2510.${id}v1`, start: new Date().toISOString()};
  try {
    const response = await fetch(rec.url, {signal: AbortSignal.timeout(90000)});
    rec.status = response.status;
    await fs.writeFile(file, await response.text());
  } catch (error) { rec.error = String(error); }
  rec.end = new Date().toISOString();
  await fs.writeFile(file + '.request.json', JSON.stringify(rec, null, 2));
  console.log(id, rec.status, rec.error || '');
}
