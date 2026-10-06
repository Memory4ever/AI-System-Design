import { writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = dirname(fileURLToPath(import.meta.url));
const ids = ['01824', '01805', '01758', '01386', '01059', '02770', '02776', '02919', '01554'];
for (const id of ids) {
  const url = `https://api.datacite.org/dois/10.48550/arXiv.2511.${id}`;
  const receipt = { url, checked: new Date().toISOString(), method: 'GET' };
  try {
    const response = await fetch(url, { signal: AbortSignal.timeout(20000) });
    const raw = await response.text();
    writeFileSync(join(root, `datacite-${id}.json`), raw);
    Object.assign(receipt, { status: response.status, bytes: Buffer.byteLength(raw) });
    if (response.ok) {
      const a = JSON.parse(raw).data.attributes;
      console.log(JSON.stringify({ id, created: a.created, registered: a.registered, dates: a.dates }));
    }
  } catch (error) {
    receipt.error = String(error);
  }
  writeFileSync(join(root, `datacite-${id}.receipt.json`), JSON.stringify(receipt, null, 2));
}
