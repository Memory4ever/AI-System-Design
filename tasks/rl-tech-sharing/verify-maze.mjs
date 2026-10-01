import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';

const {chromium}=createRequire(import.meta.url)('playwright');
const browser=await chromium.launch({headless:true,executablePath:process.env.CHROME_PATH});
const screenshots=fs.mkdtempSync(path.join(os.tmpdir(),'rl-maze-'));
const errors=[],network=[],layouts=[];
try {
  const page=await browser.newPage();
  page.on('pageerror',e=>errors.push(String(e)));
  page.on('request',r=>{if(/^https?:/.test(r.url()))network.push(r.url());});
  const url=new URL('./maze.html',import.meta.url).href;
  for(const size of [{width:1440,height:900},{width:1280,height:720},{width:390,height:844},{width:320,height:740}]) {
    await page.setViewportSize(size);await page.goto(url);
    for(const mode of ['sft','ppo','grpo','dpo']) for(const reward of ['exit','steps']) {
      await page.locator(`[data-mode="${mode}"]`).click();
      await page.selectOption('[data-reward]',reward);
      assert.equal(await page.locator('.maze-lab [data-demo-step]').count(),mode==='sft'?4:0);
      if(mode==='sft'&&reward==='exit') {
        assert.equal(await page.locator('.maze-lab').getAttribute('data-move'),'0');
        assert.deepEqual(await page.locator('.maze-lab [data-demo-step]').evaluateAll(els=>els.map(el=>el.dataset.demoStep)),['1','2','3','4']);
        await page.screenshot({path:path.join(screenshots,`${size.width}-sft-demonstration.png`),fullPage:true});
      }
      const initial=await page.locator('[data-success]').textContent();
      const oldTransform=await page.locator('.maze-lab .maze-player').getAttribute('transform');
      await page.locator('[data-maze-action="step"]').click();
      assert.notEqual(await page.locator('.maze-lab .maze-player').getAttribute('transform'),oldTransform,'the character must move');
      assert.equal(await page.locator('.maze-lab').getAttribute('data-iteration'),'0');
      // Walk every frame of a real batch, then verify that only the update changes the curves.
      const visited=await page.evaluate(()=>{
        const root=document.querySelector('.maze-lab'),seen=new Set();
        for(let i=0;i<240 && root.dataset.phase!=='3';i++) {
          seen.add(root.dataset.phase);root.querySelector('[data-maze-action="step"]').click();
        }
        return [...seen];
      });
      assert.deepEqual(visited,['0','1','2']);
      assert.equal(await page.locator('.maze-lab').getAttribute('data-iteration'),'1');
      assert.equal(await page.locator('.maze-lab [data-demo-route]').count(),0,'autonomous evaluation must not be presented as a demonstration');
      assert.equal(await page.locator('[data-loss] polyline').count(),1);
      assert.notEqual(await page.locator('[data-success]').textContent(),initial);
      await page.locator('[data-maze-action="train"]').click();
      assert.equal(await page.locator('.maze-lab').getAttribute('data-iteration'),'11');
      const box=await page.evaluate(()=>({width:document.documentElement.scrollWidth,height:document.documentElement.scrollHeight}));
      if(box.width>size.width || (size.width>700 && box.height>size.height+1))layouts.push({mode,reward,size,...box});
      if(reward==='exit' || mode==='grpo')await page.screenshot({path:path.join(screenshots,`${size.width}-${mode}-${reward}.png`),fullPage:true});
      await page.locator('[data-maze-action="reset"]').click();
      assert.equal(await page.locator('[data-success]').textContent(),initial);
      assert.equal(await page.locator('.maze-lab').getAttribute('data-iteration'),'0');
      assert.equal(await page.locator('.maze-lab [data-demo-step]').count(),mode==='sft'?4:0);
    }
  }
  await page.locator('[data-mode="sft"]').click();
  await page.selectOption('[data-speed]','60');
  await page.locator('[data-maze-action="play"]').click();
  await page.waitForTimeout(160);
  await page.locator('[data-maze-action="play"]').click();
  const paused=await page.locator('.maze-lab').getAttribute('data-move');
  assert.notEqual(paused,'0');await page.waitForTimeout(150);
  assert.equal(await page.locator('.maze-lab').getAttribute('data-move'),paused);
  await page.goto(new URL('./slides.html#2',import.meta.url).href);
  const root=page.locator('#s2 .maze-lab');
  await root.locator('[data-mode="sft"]').click();await root.locator('[data-mode="sft"]').press('ArrowRight');
  assert.equal(await root.getAttribute('data-maze-mode'),'ppo');
  assert.equal(await page.locator('#jump').inputValue(),'1');
  await root.locator('[data-maze-action="play"]').click();
  await page.selectOption('#jump','2');
  const move=await root.getAttribute('data-move');await page.waitForTimeout(250);
  assert.equal(await root.getAttribute('data-move'),move);
  assert.deepEqual(layouts,[]);assert.deepEqual(errors,[]);assert.deepEqual(network,[]);
  console.log(JSON.stringify({screenshots,layouts,errors,network,checks:'4 algorithms x 2 rewards x 4 viewports; all batch phases; real movement; update, reset, pause, keyboard and slide lifecycle'},null,2));
} finally {await browser.close();}
