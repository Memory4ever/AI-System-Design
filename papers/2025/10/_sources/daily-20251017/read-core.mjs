import { spawnSync } from 'node:child_process';
import path from 'node:path';

for (const id of process.argv.slice(2)) {
  const response = spawnSync(process.execPath, [path.join(import.meta.dirname, 'fetch.mjs'), `${id}v1-core.html`, `https://arxiv.org/html/${id}v1`], { encoding: 'utf8' });
  process.stdout.write(response.stdout);
}
