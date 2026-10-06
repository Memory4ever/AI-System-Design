import { readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = dirname(fileURLToPath(import.meta.url));
for (const name of ['ohm-anthropic.html', 'ohm-zai.html', 'ohm-zai-p2.html']) {
  const html = readFileSync(join(root, name), 'utf8');
  const chunks = [...html.matchAll(/self\.__next_f\.push\((\[[\s\S]*?\])\)<\/script>/g)]
    .map(match => JSON.parse(match[1])).filter(chunk => chunk[0] === 1 && typeof chunk[1] === 'string');
  const records = chunks.flatMap(chunk => chunk[1].split('\n'));
  const found = [];
  const lists = [];
  const roots = [];
  function visit(value) {
    if (!value || typeof value !== 'object') return;
    if (value._type === 'publicationList') lists.push(value);
    if (value.publishedOn || (value.title && (value.date || value.publishDate || value.publishedAt))) found.push(value);
    for (const child of Object.values(value)) visit(child);
  }
  for (const record of records) {
    const separator = record.indexOf(':');
    if (separator < 0) continue;
    try {
      const value = JSON.parse(record.slice(separator + 1));
      roots.push(value);
      visit(value);
    } catch { /* Non-JSON Flight records are module or text references. */ }
  }
  const result = { source: name, flightChunks: chunks.length, jsonRecords: roots.length, lists, found, roots };
  writeFileSync(join(root, `${name}.extracted.json`), JSON.stringify(result, null, 2));
  console.log(JSON.stringify({ source: name, flightChunks: chunks.length, jsonRecords: roots.length, lists: lists.map(list => ({ keys: Object.keys(list), count: Array.isArray(list.posts) ? list.posts.length : null, reference: typeof list.posts === 'string' ? list.posts : null, target: Array.isArray(list.posts) ? list.posts.filter(post => post.publishedOn?.startsWith('2025-11')).map(post => ({ title: post.title, date: post.publishedOn, slug: post.slug, directories: post.directories })) : null })), found: found.length, rootKeys: roots.map(value => value && typeof value === 'object' && !Array.isArray(value) ? Object.keys(value) : null).filter(Boolean) }));
}
