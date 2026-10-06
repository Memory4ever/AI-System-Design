import { readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = dirname(fileURLToPath(import.meta.url));
for (const name of ['anthropic.html', 'zai-p1.html', 'zai-p2.html', 'deepseek-news.html']) {
  const html = readFileSync(join(root, name), 'utf8');
  const chunks = [...html.matchAll(/self\.__next_f\.push\((\[[\s\S]*?\])\)<\/script>/g)]
    .map(match => JSON.parse(match[1])).filter(chunk => chunk[0] === 1 && typeof chunk[1] === 'string');
  const lists = [];
  function visit(value) {
    if (!value || typeof value !== 'object') return;
    if (value._type === 'publicationList' && Array.isArray(value.posts)) lists.push({ kind: 'publicationList', directory: value.directory, posts: value.posts.map(post => ({ title: post.title, publishedOn: post.publishedOn, slug: post.slug, directories: post.directories })) });
    if (Array.isArray(value.blogsItems)) lists.push({ kind: 'blogsItems', nextPage: value.nextPage, hasMore: value.hasMore, initialTag: value.initialTag, posts: value.blogsItems.map(post => ({ id: post.id, title: post.title_zh, createAt: post.createAt, createdAt: post.createdAt })) });
    if (name === 'deepseek-news.html' && Array.isArray(value.posts) && value.posts.some(post => post.slug)) lists.push({ kind: 'newsPosts', posts: value.posts.map(post => ({ title: post.title, date: post.date, slug: post.slug })) });
    for (const child of Object.values(value)) visit(child);
  }
  for (const record of chunks.flatMap(chunk => chunk[1].split('\n'))) {
    const separator = record.indexOf(':');
    if (separator < 0) continue;
    try { visit(JSON.parse(record.slice(separator + 1))); } catch { /* Flight text and module references are not JSON records. */ }
  }
  writeFileSync(join(root, `${name}.extracted.json`), JSON.stringify({ source: name, lists }, null, 2));
  console.log(JSON.stringify({ source: name, lists: lists.map(list => ({ kind: list.kind, count: list.posts.length, nextPage: list.nextPage, hasMore: list.hasMore, near: list.posts.filter(post => (post.publishedOn ?? post.createAt) >= '2025-11-01' && (post.publishedOn ?? post.createAt) < '2025-11-15') })) }));
}
