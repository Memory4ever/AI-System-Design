import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';

const [directory, name, url, body, locale] = process.argv.slice(2);
if (!directory || !name || !url) throw new Error('directory name url required');
fs.mkdirSync(directory, { recursive: true });
const target = path.join(directory, name);
const start = new Date().toISOString();
const result = spawnSync('curl', ['-sS', '-L', '--max-time', '20', '--retry', '0', '-A', 'AI-System-Design historical research', '-D', target + '.headers', '-o', target, '-w', '%{http_code} %{url_effective}', ...(body ? ['-H', 'Content-Type: application/json', '--data', body] : []), ...(locale ? ['-H', 'x-tt-locale: ' + locale] : []), url], { encoding: 'utf8' });
const record = {start, end: new Date().toISOString(), url, body, locale, target, exit:result.status, http:result.stdout, stderr:result.stderr};
fs.writeFileSync(target + '.request.json', JSON.stringify(record, null, 2) + '\n');
console.log(JSON.stringify(record));
