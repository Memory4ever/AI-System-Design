import assert from 'node:assert/strict';
import {createRequire} from 'node:module';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {mechanismNames,mechanismFrames} from './mechanisms.mjs';

const {chromium}=createRequire(import.meta.url)('playwright');
const browser=await chromium.launch({headless:true,executablePath:process.env.CHROME_PATH});
const screenshots=fs.mkdtempSync(path.join(os.tmpdir(),'rl-mechanisms-'));
const errors=[],requests=[],layouts=[];
try {
  const page=await browser.newPage();
  page.on('pageerror',e=>errors.push(String(e)));
  page.on('request',r=>{if(/^https?:/.test(r.url()))requests.push(r.url());});
  const url=new URL('./maze.html#credit',import.meta.url).href;
  for(const size of [{width:1440,height:900},{width:1280,height:720},{width:390,height:844},{width:320,height:740}]) {
    await page.setViewportSize(size);await page.goto(url);
    assert.equal(await page.locator('[data-lab-panel="training"]').isHidden(),true);
    assert.equal(await page.locator('body').getByText(/DAPO/).count(),0);
    assert.deepEqual(await page.locator('[data-mechanism-select] option').evaluateAll(els=>els.map(el=>el.value)),['sampling','credit','rm','dpo','repair']);
    for(const id of Object.keys(mechanismNames)) {
      await page.selectOption('[data-mechanism-select]',id);
      const root=page.locator('.mechanism');
      assert.equal(await root.getAttribute('data-frame'),'0');
      const states=await page.evaluate(()=>{
        const root=document.querySelector('.mechanism'),states=[];
        for(let i=0;i<Number(root.dataset.frames);i++) {
          const svg=root.querySelector('.maze-board');
          states.push({frame:root.dataset.frame,title:root.querySelector('h2').textContent,scene:svg.innerHTML,
            width:document.documentElement.scrollWidth,height:document.documentElement.scrollHeight,
            svgOverflow:[...root.querySelectorAll('svg text')].some(el=>{const b=el.getBBox(),v=el.closest('svg').viewBox.baseVal;return b.x<0 || b.x+b.width>v.width+1;})});
          root.querySelector('[data-mechanism-action="next"]').click();
        }
        return states;
      });
      assert.equal(states.length,mechanismFrames(id).length);
      assert.ok(new Set(states.map(s=>s.scene)).size>1,`${id}: board should reflect the changing scenario`);
      for(const s of states)if(s.width>size.width || (size.width>700 && s.height>size.height+1) || s.svgOverflow)layouts.push({id,size,...s,scene:undefined});
      await page.screenshot({path:path.join(screenshots,`${size.width}-${id}.png`),fullPage:true});
      assert.ok(await root.locator('[data-mechanism-action="next"]').isDisabled());
      await root.locator('[data-mechanism-action="back"]').click();
      assert.equal(await root.getAttribute('data-frame'),String(states.length-2));
      await root.locator('[data-mechanism-action="reset"]').click();
      assert.equal(await root.getAttribute('data-frame'),'0');
    }
  }
  const root=page.locator('.mechanism');
  await page.selectOption('[data-mechanism-select]','credit');
  await page.selectOption('[data-mechanism-speed]','600');
  await root.locator('[data-mechanism-action="play"]').click();await page.waitForTimeout(700);
  await root.locator('[data-mechanism-action="play"]').click();
  const paused=await root.getAttribute('data-frame');assert.notEqual(paused,'0');
  await page.waitForTimeout(700);assert.equal(await root.getAttribute('data-frame'),paused);
  await root.locator('[data-mechanism-action="play"]').click();
  await page.locator('[data-lab-view="training"]').click();
  await page.waitForTimeout(700);assert.equal(await root.getAttribute('data-frame'),paused);
  await page.goto(new URL('./maze.html#clip',import.meta.url).href);
  assert.ok(await page.locator('[data-lab-panel="mechanisms"]').isHidden(),'retired DAPO links must not activate an animation');
  await page.goto(new URL('./slides.html#5',import.meta.url).href);
  assert.equal(await page.locator('.slide [data-mechanism="rm"]').count(),0,'optional scoring mechanism stays out of the main talk');
  const deck=page.locator('#s5 .mechanism');
  assert.deepEqual(await deck.locator('[data-mechanism-select] option').evaluateAll(els=>els.map(el=>el.value)),['credit']);
  await deck.locator('[data-mechanism-action="next"]').press('ArrowRight');
  assert.equal(await deck.getAttribute('data-frame'),'1');assert.equal(await page.locator('#jump').inputValue(),'4');
  await deck.locator('[data-mechanism-action="play"]').click();await page.selectOption('#jump','5');
  await page.waitForTimeout(650);assert.equal(await deck.getAttribute('data-frame'),'1');
  console.log(JSON.stringify({screenshots,layouts,errors,requests,checks:'5 mechanisms, every frame, 4 viewports, retired DAPO links, SVG bounds, reset/back/play/pause, view switching and slide lifecycle'},null,2));
  assert.deepEqual(layouts,[]);assert.deepEqual(errors,[]);assert.deepEqual(requests,[]);
} finally {await browser.close();}
