import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { hasLesson, lessonMarkup } from './interactive.mjs';
import { mazeMarkup } from './maze.mjs';
import { mechanismNames, mechanismMarkup } from './mechanisms.mjs';
import { frameworkMarkup } from './framework-animation.mjs';

const require = createRequire(import.meta.url);
const { marked } = await import(pathToFileURL(require.resolve('marked')).href);
const root = path.dirname(fileURLToPath(import.meta.url));
const lucide = require('lucide');
const icon = name => `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${lucide[name].map(([tag, attrs]) => `<${tag} ${Object.entries(attrs).map(([k,v]) => `${k}="${v}"`).join(' ')}></${tag}>`).join('')}</svg>`;
const icons = {play:icon('Play'),pause:icon('Pause'),back:icon('StepBack'),next:icon('StepForward'),reset:icon('RotateCcw')};
const interactiveCSS = fs.readFileSync(path.join(root, 'interactive.css'), 'utf8');
const interactiveJS = fs.readFileSync(path.join(root, 'interactive.mjs'), 'utf8').replace(/^export /gm, '');
const mazeCSS = fs.readFileSync(path.join(root, 'maze.css'), 'utf8');
const mazeJS = fs.readFileSync(path.join(root, 'maze.mjs'), 'utf8').replace(/^export /gm, '');
const mechanismCSS = fs.readFileSync(path.join(root, 'mechanisms.css'), 'utf8');
const mechanismJS = fs.readFileSync(path.join(root, 'mechanisms.mjs'), 'utf8').replace(/^import .*\n/gm, '').replace(/^export /gm, '');
const frameworkCSS = fs.readFileSync(path.join(root, 'framework-animation.css'), 'utf8');
const frameworkJS = fs.readFileSync(path.join(root, 'framework-animation.mjs'), 'utf8').replace(/^export /gm, '');
const results = JSON.parse(fs.readFileSync(path.join(root, 'examples/results.json'), 'utf8'));
const text = fs.readFileSync(path.join(root, 'TALK.md'), 'utf8');
const chunks = text.split(/^## /m).slice(1);
const escape = (s) => s.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;');
const slides = chunks.map((chunk, index) => {
  const lines = chunk.split('\n');
  const title = lines[0].replace(/^\d+ /, '');
  const section = (name) => chunk.match(new RegExp(`### ${name}\\n([\\s\\S]*?)(?=\\n### |$)`))?.[1]?.trim() ?? '';
  const content = section('上屏');
  const diagram = section('图示');
  const notes = section('讲稿');
  const pause = section('现场停顿');
  const transition = section('交接').replace(/\n来源：[\s\S]*$/, '').trim();
  const source = chunk.match(/^来源：(.*)$/m)?.[1] ?? '';
  const annotation = section('公式解读');
  const fullFormula = section('完整公式');
  const fallback = `${marked.parse(content)}${diagram ? `<div class="diagram">${marked.parse(diagram)}</div>` : ''}${annotation ? `<div class="formula-notes">${marked.parse(annotation)}</div>` : ''}${fullFormula ? `<details class="formula-details"><summary>完整公式与符号解释</summary><div>${marked.parse(fullFormula)}</div></details>` : ''}`;
  const demo = chunk.match(/^演示：(.*)$/m)?.[1]?.trim();
  const [kind, key, reward = 'exit'] = demo?.split(':') ?? [];
  let body = null;
  if (kind === 'maze' && ['sft','ppo','grpo','dpo'].includes(key) && ['exit','steps'].includes(reward)) body = mazeMarkup(key,icons,reward);
  else if (kind === 'mechanism' && Object.hasOwn(mechanismNames,key)) body = mechanismMarkup(key,icons,[key]);
  else if (kind === 'lesson' && hasLesson(Number(key))) body = lessonMarkup(Number(key),icons);
  else if (kind === 'frameworks' && key === 'comparison') body = frameworkMarkup(icons);
  else if (demo) throw new Error(`Unknown demonstration on slide ${index+1}: ${demo}`);
  return `<section class="slide ${body ? kind === 'frameworks' ? 'has-frameworks' : kind === 'mechanism' ? 'has-mechanism' : kind === 'maze' ? 'has-maze' : 'has-lesson' : ''}" id="s${index + 1}" ${index ? 'hidden' : ''}>
    <div class="eyebrow">大模型强化学习 · ${String(index + 1).padStart(2, '0')}</div>
    <h1${kind==='maze'?` data-maze-heading data-original-title="${escape(title)}"`:''}>${escape(title)}</h1>
    <div class="body">${body ? `${body}<details class="original"><summary>静态图解与公式</summary><div>${fallback}</div></details>` : fallback}</div>
    <footer>${marked.parse(source)}</footer>
    <aside class="notes" hidden><h2>讲稿</h2>${marked.parse(notes)}${pause ? `<h2>现场停顿</h2>${marked.parse(pause)}` : ''}<h2>下一页</h2>${marked.parse(transition)}</aside>
  </section>`;
}).join('\n');
const html = `<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>大模型强化学习 · 技术分享</title>
<style>
:root{color-scheme:light;--ink:#202524;--muted:#59645f;--accent:#167350;--line:#dbe3de;--paper:#fff}
*{box-sizing:border-box} [hidden]{display:none!important}
body{margin:0;background:#f2f5f3;color:var(--ink);font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif;letter-spacing:0}
main{max-width:1400px;margin:0 auto;background:var(--paper);min-height:calc(100vh - 66px)}
.slide{padding:44px 64px 22px;min-height:calc(100vh - 66px);border-top:7px solid var(--accent);display:flex;flex-direction:column}
.eyebrow{font-size:15px;color:var(--accent);font-weight:600;margin-bottom:22px}
h1{font-size:36px;line-height:1.4;margin:0 0 30px;font-weight:650;overflow-wrap:anywhere}
.body{font-size:24px;line-height:1.75;flex:1;min-width:0}.body p{margin:0 0 18px}.body ul{padding-left:1.2em;margin:18px 0}.body li{padding:5px 0}
pre{white-space:pre-wrap;overflow-wrap:anywhere;font-size:21px;line-height:1.8;background:#f3f6f4;border-left:4px solid var(--accent);padding:20px 24px;margin:14px 0 22px}
code{font-family:ui-monospace,SFMono-Regular,Consolas,"PingFang SC",monospace;font-size:.9em}pre code{font-size:inherit}
table{border-collapse:collapse;width:100%;table-layout:fixed;font-size:22px;line-height:1.6;margin:12px 0 22px}th,td{padding:13px 16px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top;overflow-wrap:anywhere}th{color:var(--accent);font-weight:650;background:#f3f6f4}
.diagram pre{font-size:20px;border-color:#c4771a;background:#fcf8ef}
footer{font-size:13px;line-height:1.6;color:var(--muted);margin-top:22px;overflow-wrap:anywhere}footer p{margin:0}a{color:#167350;text-underline-offset:3px}
.notes{font-size:18px;line-height:1.9;border-top:1px solid var(--line);margin-top:22px;padding:20px 0}.notes h2{font-size:18px;margin:10px 0}.notes p{margin:0 0 14px}
nav{height:66px;background:#fff;border-top:1px solid var(--line);display:flex;gap:10px;align-items:center;justify-content:center;position:sticky;bottom:0;padding:8px 16px;z-index:2}
button,select{font:inherit;border:1px solid var(--line);border-radius:5px;background:#fff;color:var(--ink);height:40px;padding:0 14px;cursor:pointer}button:hover{background:#edf5f0}button:disabled{opacity:.35;cursor:default}button:focus-visible,select:focus-visible{outline:3px solid #c4771a;outline-offset:2px}
.arrow{font-size:25px;width:44px;padding:0}select{max-width:110px}#notes[aria-pressed="true"]{background:#e0efe6;color:#126242}
@media(min-width:701px) and (max-height:800px){.slide{padding:24px 48px 16px}.eyebrow{margin-bottom:12px}h1{font-size:32px;margin-bottom:20px}.body{font-size:22px;line-height:1.55}.body li{padding:3px 0}table{font-size:20px;line-height:1.45;margin-bottom:16px}th,td{padding:8px 12px}pre,.diagram pre{font-size:18px;line-height:1.55;padding:12px 18px;margin:10px 0 16px}footer{margin-top:14px}}
@media(max-width:700px){.slide{padding:24px 20px 18px}.eyebrow{font-size:13px;margin-bottom:14px}h1{font-size:26px;margin-bottom:22px}.body{font-size:18px}pre,.diagram pre{font-size:15px;padding:14px 12px}table{font-size:15px}th,td{padding:9px 6px}nav{gap:6px;padding:8px}button,select{font-size:13px;padding:0 10px}.notes{font-size:16px}#print{display:none}}
@media print{@page{size:landscape;margin:10mm}body,main{background:#fff}main{max-width:none}.slide,.slide[hidden]{display:flex!important;min-height:175mm;break-after:page;padding:8mm 10mm;border-width:3px}.slide:last-child{break-after:auto}h1{font-size:25px;margin-bottom:18px}.body{font-size:18px}pre,.diagram pre{font-size:16px;padding:10px 14px}table{font-size:16px}th,td{padding:8px 10px}footer{font-size:10px}.notes,nav{display:none!important}}
${interactiveCSS}
${mazeCSS}
${mechanismCSS}
${frameworkCSS}
</style></head><body><main>${slides}</main>
<nav aria-label="演示控制">
<button class="arrow" id="prev" title="上一页" aria-label="上一页">←</button>
<select id="jump" aria-label="选择页码">${chunks.map((_,i)=>`<option value="${i}">${i+1} / ${chunks.length}</option>`).join('')}</select>
<button class="arrow" id="next" title="下一页" aria-label="下一页">→</button>
<button id="notes" aria-pressed="false">讲者备注</button><button id="fullscreen">全屏</button><button id="print">打印</button>
</nav>
<script>
const slides=[...document.querySelectorAll('.slide')];let current=0;let showNotes=false;
function show(index){document.dispatchEvent(new Event('slidechange'));current=Math.max(0,Math.min(slides.length-1,index));slides.forEach((s,i)=>{s.hidden=i!==current;s.querySelector('.notes').hidden=!showNotes});document.querySelector('#jump').value=current;document.querySelector('#prev').disabled=current===0;document.querySelector('#next').disabled=current===slides.length-1;history.replaceState(null,'','#'+(current+1));window.scrollTo(0,0)}
document.querySelector('#prev').onclick=()=>show(current-1);document.querySelector('#next').onclick=()=>show(current+1);
document.querySelector('#jump').onchange=e=>show(Number(e.target.value));
document.querySelector('#notes').onclick=e=>{showNotes=!showNotes;e.currentTarget.setAttribute('aria-pressed',String(showNotes));slides[current].querySelector('.notes').hidden=!showNotes};
document.querySelector('#fullscreen').onclick=async()=>{if(document.fullscreenElement){await document.exitFullscreen()}else if(document.documentElement.requestFullscreen){await document.documentElement.requestFullscreen()}};
document.querySelector('#print').onclick=()=>window.print();
document.addEventListener('keydown',e=>{if(['SELECT','INPUT','TEXTAREA'].includes(e.target.tagName))return;if(e.key==='ArrowRight'){e.preventDefault();show(current+1)}if(e.key==='ArrowLeft'){e.preventDefault();show(current-1)}});
window.addEventListener('hashchange',()=>show((parseInt(location.hash.slice(1),10)||1)-1));
show((parseInt(location.hash.slice(1),10)||1)-1);
(()=>{${interactiveJS}\nmountLessons(${JSON.stringify(results)});})();
(()=>{${frameworkJS}\nmountFrameworks(${JSON.stringify(icons)});})();
(()=>{${mazeJS}\n${mechanismJS}\nmountMazes(${JSON.stringify(icons)});mountMechanisms(${JSON.stringify(icons)});})();
const printState=[];
const printTitles=[];
window.addEventListener('beforeprint',()=>{document.dispatchEvent(new Event('slidechange'));document.querySelectorAll('.original,.formula-details').forEach(el=>{printState.push([el,el.open]);el.open=true});document.querySelectorAll('[data-maze-heading]').forEach(el=>{printTitles.push([el,el.textContent]);el.textContent=el.dataset.originalTitle})});
window.addEventListener('afterprint',()=>{for(const [el,open] of printState)el.open=open;printState.length=0;for(const [el,title] of printTitles)el.textContent=title;printTitles.length=0});
</script></body></html>`;
fs.writeFileSync(path.join(root, 'slides.html'), html.replace(/[ \t]+$/gm, ''));
const mazeHTML = `<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>同一迷宫，理解强化学习</title><style>
[hidden]{display:none!important}body{margin:0;background:#fff;color:#202524;font-family:-apple-system,BlinkMacSystemFont,"PingFang SC",sans-serif;letter-spacing:0}main{max-width:1100px;padding:12px 24px;margin:auto}h1{font-size:26px;line-height:1.4;margin:0 0 8px}a{color:#167350}.maze-source{font-size:12px;line-height:1.6;margin-top:6px}@media(max-width:700px){main{padding:16px}h1{font-size:23px}}${mazeCSS}\n${mechanismCSS}
</style></head><body><main><h1>同一迷宫，理解强化学习</h1><div class="lab-views" role="tablist" aria-label="实验视图"><button role="tab" data-lab-view="training" aria-selected="true">训练实验</button><button role="tab" data-lab-view="mechanisms" aria-selected="false">机制拆解</button></div><div data-lab-panel="training">${mazeMarkup('ppo',icons)}</div><div data-lab-panel="mechanisms" hidden>${mechanismMarkup('credit',icons)}</div><p class="maze-source">简化与复算说明：<a href="./EXAMPLES.md">实验说明</a> · <a href="./slides.html#11">返回分享</a><br>机制来源：<a href="https://arxiv.org/abs/1707.06347">PPO</a> · <a href="https://arxiv.org/html/2402.03300v3">GRPO</a> · <a href="https://arxiv.org/html/2305.18290v2">DPO</a> · <a href="https://arxiv.org/abs/2203.02155">Reward Model</a></p></main><script>(()=>{${mazeJS}\n${mechanismJS}\nmountMazes(${JSON.stringify(icons)});mountMechanisms(${JSON.stringify(icons)});
function view(name){document.dispatchEvent(new Event('slidechange'));document.querySelectorAll('[data-lab-panel]').forEach(el=>el.hidden=el.dataset.labPanel!==name);document.querySelectorAll('[data-lab-view]').forEach(el=>el.setAttribute('aria-selected',String(el.dataset.labView===name)));}
document.querySelectorAll('[data-lab-view]').forEach(el=>{el.onclick=()=>view(el.dataset.labView);el.onkeydown=e=>{if(['ArrowLeft','ArrowRight'].includes(e.key)){e.preventDefault();const other=el.dataset.labView==='training'?'mechanisms':'training';view(other);document.querySelector('[data-lab-view="'+other+'"]').focus();}}});
if(Object.hasOwn(mechanismNames,location.hash.slice(1))){view('mechanisms');const select=document.querySelector('[data-mechanism-select]');select.value=location.hash.slice(1);select.dispatchEvent(new Event('change'));}
})();</script></body></html>`;
fs.writeFileSync(path.join(root, 'maze.html'), mazeHTML.replace(/[ \t]+$/gm, ''));
console.log(`Rendered ${chunks.length} slides from TALK.md`);
