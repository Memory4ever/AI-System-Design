import { writeFileSync, existsSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = dirname(fileURLToPath(import.meta.url));
const [name, url, body] = process.argv.slice(2);
const path = join(root, name);
if (existsSync(path) || existsSync(`${path}.receipt.json`)) throw new Error('Refusing to overwrite evidence');
const started = new Date().toISOString();
const options = { signal: AbortSignal.timeout(25000), headers: { 'x-tt-locale': 'US', 'User-Agent': 'HistoricalDailyResearch/1.0' } };
if (body) Object.assign(options, { method: 'POST', body, headers: { ...options.headers, 'Content-Type': 'application/json' } });
try {
  const response = await fetch(url, options);
  const content = await response.text();
  writeFileSync(path, content, { flag: 'wx' });
  const receipt = { author: 'Darwin/Codex Sep02 supplement', url, method: options.method || 'GET', body: body || null, started, checked: new Date().toISOString(), status: response.status, finalUrl: response.url, bytes: Buffer.byteLength(content) };
  writeFileSync(`${path}.receipt.json`, JSON.stringify(receipt, null, 2), { flag: 'wx' });
  console.log(JSON.stringify(receipt));
} catch (error) {
  const receipt = { url, started, checked: new Date().toISOString(), error: String(error) };
  writeFileSync(`${path}.receipt.json`, JSON.stringify(receipt, null, 2), { flag: 'wx' });
  console.log(JSON.stringify(receipt));
}
