import { writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
const root = dirname(fileURLToPath(import.meta.url));
const [name, url, body] = process.argv.slice(2);
const options = { signal: AbortSignal.timeout(45000), headers: { 'x-tt-locale': 'US' } };
if (body) Object.assign(options, { method: 'POST', body, headers: { ...options.headers, 'Content-Type': 'application/json' } });
try {
  const response = await fetch(url, options);
  const content = await response.text();
  writeFileSync(join(root, name), content);
  const receipt = { url, method: options.method || 'GET', body: body || null, checked: new Date().toISOString(), status: response.status, finalUrl: response.url, bytes: Buffer.byteLength(content) };
  writeFileSync(join(root, `${name}.receipt.json`), JSON.stringify(receipt, null, 2));
  console.log(JSON.stringify(receipt));
} catch (error) {
  const receipt = { url, checked: new Date().toISOString(), error: String(error) };
  writeFileSync(join(root, `${name}.receipt.json`), JSON.stringify(receipt, null, 2));
  console.log(JSON.stringify(receipt));
}
