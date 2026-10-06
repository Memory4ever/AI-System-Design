import { spawnSync } from 'node:child_process';
import { writeFileSync } from 'node:fs';
import path from 'node:path';

const [name, url, body, locale] = process.argv.slice(2);
const target = path.join(import.meta.dirname, name);
const args = ['-L', '--max-time', '20', '--retry', '0', '-sS', '-D', `${target}.headers`, '-o', target, '-w', '%{http_code} %{url_effective}'];
if (body) args.push('-H', 'Content-Type: application/json', '--data', body);
if (locale) args.push('-H', `x-tt-locale: ${locale}`);
args.push(url);
const start = new Date().toISOString();
const response = spawnSync('curl', args, { encoding: 'utf8' });
const record = { start, end: new Date().toISOString(), url, body, locale, exit: response.status, http: response.stdout, stderr: response.stderr };
writeFileSync(`${target}.request.json`, `${JSON.stringify(record, null, 2)}\n`);
process.stdout.write(`${JSON.stringify(record)}\n`);
