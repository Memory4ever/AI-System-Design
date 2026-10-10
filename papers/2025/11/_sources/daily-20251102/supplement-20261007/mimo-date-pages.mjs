import { execFileSync } from 'node:child_process';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = dirname(fileURLToPath(import.meta.url));
const paths = [
  '/mimo-v2-5-asr/index.html', '/mimo-v2-5-tts/index.html',
  '/mimo-v2-5-pro/index.html', '/mimo-v2-5/index.html',
  '/mimo-v2-pro/index.html', '/mimo-v2-omni/index.html',
  '/mimo-v2-tts/index.html', '/mimo-v2-flash/index.html',
];
for (const [index, path] of paths.entries()) {
  execFileSync(process.execPath, [join(root, 'fetch.mjs'), `mimo-date-${index + 7}.html`, new URL(path, 'https://mimo.xiaomi.com').href], { stdio: 'inherit' });
}
