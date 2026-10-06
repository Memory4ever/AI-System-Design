import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';

const [name, url, body, locale] = process.argv.slice(2);
const target = path.join(import.meta.dirname, name);
const start = new Date().toISOString();
const args = ['-sS', '-L', '--max-time', '20', '--retry', '0', '-A', 'AI-System-Design historical research', '-D', target + '.headers', '-o', target, '-w', '%{http_code} %{url_effective}'];
if (body) args.push('-H', 'Content-Type: application/json', '--data', body);
if (locale) args.push('-H', 'x-tt-locale: ' + locale);
args.push(url);
const r = spawnSync('curl', args, { encoding: 'utf8' });
const request = { start, end: new Date().toISOString(), url, body, locale, exit: r.status, http: r.stdout, stderr: r.stderr };
fs.writeFileSync(target + '.request.json', JSON.stringify(request, null, 2) + '\n');
console.log(JSON.stringify(request));
