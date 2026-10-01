import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import { sampledStep } from './interactive.mjs';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');
const executablePath = process.env.CHROME_PATH;
const browser = await chromium.launch({headless:true, ...(executablePath ? {executablePath} : {})});
const screenshots = fs.mkdtempSync(path.join(os.tmpdir(), 'rl-slides-'));
console.log(`Screenshots: ${screenshots}`);
try {
  const page = await browser.newPage();
  await page.clock.install();
  const errors = [], requests = [], layouts = [];
  page.on('pageerror', e => errors.push(String(e)));
  page.on('request', request => {if (/^https?:/.test(request.url())) requests.push(request.url());});
  const url = new URL('./slides.html', import.meta.url).href;
  await page.goto(url+'#2');
  await page.locator('#s2 [data-mode="ppo"]').click();
  assert.ok((await page.locator('#s2 h1').textContent()).startsWith('PPO：'),'maze tab must update the slide heading');
  for (const size of [{width:1440,height:900},{width:1280,height:720},{width:390,height:844},{width:320,height:740}]) {
    await page.setViewportSize(size); await page.goto(url);
    const slideCount = await page.locator('.slide').count();
    assert.equal(slideCount,16,'main talk should contain 16 slides');
    assert.equal(await page.locator('#s2 .maze-lab').count(),1,'SFT demonstration follows the opening');
    assert.equal(await page.locator('#s4 [data-lesson="6"]').count(),1,'reward-to-update animation must follow the narrative, not its old page number');
    assert.equal(await page.locator('#s5 [data-mechanism="credit"]').count(),1);
    assert.equal(await page.locator('#s8 .maze-lab').count(),1);
    assert.equal(await page.locator('#s10 .maze-lab').count(),1);
    assert.equal(await page.locator('#s14 [data-lesson="23"]').count(),1);
    assert.equal(await page.locator('#s15 .framework-demo').count(),1);
    assert.equal(slideCount, await page.locator('#jump option').count());
    for (let i=0;i<slideCount;i++) {
      await page.selectOption('#jump', String(i));
      const lesson=page.locator(`#s${i+1} .lesson`);
      const count=await lesson.count() ? Math.max(1, await lesson.locator('.lesson-steps li').count()) : 1;
      for (let step=0;step<count;step++) {
        const box=await page.evaluate(()=>({width:document.documentElement.scrollWidth,height:document.documentElement.scrollHeight}));
        if(box.width>size.width || (size.width>700 && box.height>size.height+1))layouts.push({slide:i+1,step,size,...box});
        const next=lesson.locator('[data-action="next"]');
        if(await next.count() && await next.isEnabled())await next.click();
      }
      if(await page.locator(`#s${i+1} .maze-lab`).count()) {
        const mazeLayouts=await page.evaluate(({slide,size})=>{
          const root=document.querySelector(`#s${slide} .maze-lab`),failures=[];
          for(let frame=0;frame<250;frame++) {
            const width=document.documentElement.scrollWidth,height=document.documentElement.scrollHeight;
            if(width>size.width || (size.width>700 && height>size.height+1))failures.push({slide,phase:root.dataset.phase,frame,size,width,height});
            if(root.dataset.phase==='3')break;
            root.querySelector('[data-maze-action="step"]').click();
          }
          return failures;
        },{slide:i+1,size});
        layouts.push(...mazeLayouts);
        const maze=page.locator(`#s${i+1} .maze-lab`);
        const heading=page.locator(`#s${i+1} h1`);
        const defaultMode=await maze.getAttribute('data-maze-mode');
        const defaultReward=await maze.locator('[data-reward]').inputValue();
        const defaultTitle=await heading.textContent();
        for(const mode of ['sft','ppo','grpo','dpo'])for(const reward of ['exit','steps']) {
          await maze.locator(`[data-mode="${mode}"]`).click();
          await maze.locator('[data-reward]').selectOption(reward);
          const title=await heading.textContent();
          if(mode===defaultMode&&reward===defaultReward)assert.equal(title,defaultTitle);
          else assert.ok(title.startsWith(mode.toUpperCase()),`slide ${i+1}: ${mode}/${reward} heading mismatch`);
          if(reward==='steps'&&['sft','dpo'].includes(mode))assert.ok(title.includes('只用于评估'));
          await maze.locator('[data-maze-action="reset"]').click();
          assert.equal(await heading.textContent(),title,'reset must preserve current mode heading');
          const box=await page.evaluate(()=>({width:document.documentElement.scrollWidth,height:document.documentElement.scrollHeight}));
          if(box.width>size.width||(size.width>700&&box.height>size.height+1))layouts.push({slide:i+1,mode,reward,size,...box});
          if(i===1&&reward==='exit')await page.screenshot({path:path.join(screenshots,`${size.width}-tab-${mode}.png`),fullPage:true});
        }
        await maze.locator(`[data-mode="${defaultMode}"]`).click();
        await maze.locator('[data-reward]').selectOption(defaultReward);
        assert.equal(await heading.textContent(),defaultTitle,'switching back restores the authored title');
      }
      const mechanism=page.locator(`#s${i+1} .mechanism`);
      if(await mechanism.count()) {
        const options=await mechanism.locator('[data-mechanism-select] option').evaluateAll(els=>els.map(el=>el.value));
        for(const option of options) {
          await mechanism.locator('[data-mechanism-select]').selectOption(option);
          const failures=await mechanism.evaluate((root,size)=>{
            const failures=[];
            for(let frame=0;frame<Number(root.dataset.frames);frame++) {
              const width=document.documentElement.scrollWidth,height=document.documentElement.scrollHeight;
              if(width>size.width || (size.width>700 && height>size.height+1))failures.push({mechanism:root.dataset.mechanism,frame,size,width,height});
              root.querySelector('[data-mechanism-action="next"]').click();
            }
            return failures;
          },size);
          layouts.push(...failures);
        }
      }
      const framework=page.locator(`#s${i+1} .framework-demo`);
      if(await framework.count()) {
        for(const scene of ['shared','handoff','async']) {
          await framework.locator(`[data-framework-tab="${scene}"]`).click();
          const frames=Number(await framework.getAttribute('data-frames'));
          for(const outcome of scene==='async'?['accept','retry']:['accept']) {
          await framework.locator('[data-framework-action="reset"]').click();
          if(scene==='async') await framework.locator('[data-framework-outcome]').selectOption(outcome);
          for(let frame=0;frame<frames;frame++) {
            assert.equal(await framework.getAttribute('data-frame'),String(frame));
            assert.equal(await framework.locator('[aria-current="step"]').count(),scene==='async'?4:2);
            assert.equal(await framework.locator('.framework-track').count(),scene==='async'?4:0);
            if(scene==='async'&&frame===1) {
              assert.match(await framework.locator('.lane-0 .framework-track').first().locator('[aria-current="step"]').textContent(),/空闲/);
              assert.match(await framework.locator('.lane-1 .framework-track').first().locator('[aria-current="step"]').textContent(),/第2批 v7/);
              assert.match(await framework.locator('.lane-1 .framework-track').last().locator('[aria-current="step"]').textContent(),/训第1批/);
            }
            if(scene==='async'&&frame===4) {
              assert.match(await framework.locator('[data-batch-second]').textContent(),outcome==='accept'?/v8.*v9/:/v8.*重.*中/);
              assert.match(await framework.locator('.lane-1 .framework-track').last().locator('[aria-current="step"]').textContent(),outcome==='accept'?/更新到 v9/:/等待新数据/);
            }
            const box=await page.evaluate(()=>({width:document.documentElement.scrollWidth,height:document.documentElement.scrollHeight}));
            if(box.width>size.width||(size.width>700&&box.height>size.height+1))layouts.push({slide:i+1,scene,frame,size,...box});
            const clipped=await framework.locator('li>span,button,[data-answer]').evaluateAll(els=>els.filter(el=>el.scrollWidth>el.clientWidth+1||el.scrollHeight>el.clientHeight+1).map(el=>el.textContent));
            assert.deepEqual(clipped,[],`framework ${scene} frame ${frame} has clipped text at ${size.width}`);
            if(frame>=1)await page.screenshot({path:path.join(screenshots,`${size.width}-framework-${scene}-${outcome}-${frame}.png`),fullPage:true});
            if(frame<frames-1)await framework.locator('[data-framework-action="next"]').click();
          }
          }
          if(scene==='async') await framework.locator('[data-framework-outcome]').selectOption('accept');
        }
        await framework.locator('[data-framework-tab="shared"]').click();
      }
    }
    for(let slide=1;slide<=slideCount;slide++) {
      await page.selectOption('#jump',String(slide-1));
      await page.screenshot({path:path.join(screenshots,`${size.width}-${slide}.png`),fullPage:true});
    }
  }
  console.log(JSON.stringify({layouts}));
  await page.setViewportSize({width:1440,height:900});await page.goto(url+'#4');await page.reload();
  const sample=page.locator('#s4 .lesson');
  await sample.locator('[data-action="play"]').click();
  await page.clock.runFor(2800);assert.equal(await sample.getAttribute('data-step'),'1');
  await sample.locator('[data-action="play"]').click();
  await page.clock.runFor(2800);assert.equal(await sample.getAttribute('data-step'),'1');
  await sample.locator('[data-action="play"]').click();
  await page.selectOption('#jump','4');await page.clock.runFor(2800);
  assert.equal(await sample.getAttribute('data-step'),'1','leaving a slide must stop its animation');
  await page.selectOption('#jump','3');
  await sample.locator('[data-action="reset"]').click();assert.equal(await sample.getAttribute('data-step'),'0');
  for(let i=0;i<5;i++)await sample.locator('[data-action="next"]').click();
  const sampleProbability=(sampledStep([0,0,0,0],0,1,0.2).after[0]*100).toFixed(2)+'%';
  assert.ok((await sample.locator('.calculation').textContent()).includes(sampleProbability));
  await page.selectOption('#jump','7');
  const group=page.locator('#s8 .maze-lab');
  await group.locator('[data-maze-action="train"]').click();
  assert.equal(await group.getAttribute('data-iteration'),'10');
  await group.locator('select').first().focus();await page.keyboard.press('ArrowRight');
  assert.equal(await page.locator('#jump').inputValue(),'7','select key must not turn slide');
  await page.locator('h1:visible').click();await page.keyboard.press('ArrowRight');
  assert.equal(await page.locator('#jump').inputValue(),'8');
  await page.locator('#notes').click();assert.ok(await page.locator('#s9 .notes').isVisible());await page.locator('#notes').click();
  for (const slide of [4,5,10,16]) {
    await page.selectOption('#jump', String(slide-1));
    assert.ok(await page.locator(`#s${slide} .notes`).isHidden());
    await page.locator('#notes').click();
    const notes=page.locator(`#s${slide} .notes`);
    assert.ok(await notes.isVisible());
    assert.ok((await notes.locator('h2').allTextContents()).includes('现场停顿'));
    assert.equal(await page.locator(`#s${slide} .body`).getByText('现场停顿', {exact:true}).count(),0);
    await page.locator('#notes').click();
  }
  assert.ok((await page.locator('#s16 .body').textContent()).includes('说出一轮 GRPO'));
  assert.ok((await page.locator('#s6 .body').textContent()).includes('Critic'));
  assert.ok((await page.locator('#s9 .body').textContent()).includes('更新共享参数'));
  assert.equal(await page.locator('#s7 .lesson').count(),0,'static constraints must not inherit an old animation');
  assert.equal(await page.locator('#s15 .maze-lab').count(),0,'framework summary must remain a comparison');
  await page.selectOption('#jump','14');
  const framework=page.locator('#s15 .framework-demo');
  await framework.locator('[data-framework-tab="shared"]').press('ArrowRight');
  assert.equal(await framework.getAttribute('data-framework-scene'),'handoff');
  assert.equal(await page.locator('#jump').inputValue(),'14','framework tabs must not navigate slides');
  await framework.locator('[data-framework-speed]').selectOption('4000');
  await framework.locator('[data-framework-action="play"]').click();
  await page.clock.runFor(4250);
  assert.equal(await framework.getAttribute('data-frame'),'1');
  await framework.locator('[data-framework-action="play"]').click();
  await page.clock.runFor(4250);
  assert.equal(await framework.getAttribute('data-frame'),'1','pause freezes framework animation');
  await framework.locator('[data-framework-action="play"]').click();
  await framework.locator('[data-framework-tab="async"]').click();
  await page.clock.runFor(4250);
  assert.equal(await framework.getAttribute('data-frame'),'0','tab switch resets and pauses');
  await framework.locator('[data-framework-action="next"]').click();
  assert.match(await framework.locator('[data-batch-second]').textContent(),/v8.*尚未训练完/);
  await framework.locator('[data-framework-action="back"]').click();
  assert.equal(await framework.getAttribute('data-frame'),'0');
  await framework.locator('[data-framework-action="next"]').click();
  await framework.locator('[data-framework-action="reset"]').click();
  assert.equal(await framework.getAttribute('data-frame'),'0');
  await framework.locator('[data-framework-action="play"]').click();
  await page.selectOption('#jump','15');await page.clock.runFor(4250);
  assert.equal(await framework.getAttribute('data-frame'),'0','leaving framework slide stops playback');
  await page.emulateMedia({reducedMotion:'reduce'});
  assert.equal(await framework.locator('li').first().evaluate(el=>getComputedStyle(el).transitionDuration),'0s');
  await page.selectOption('#jump','14');
  for(let step=0;step<4;step++)await framework.locator('[data-framework-action="next"]').click();
  assert.ok(await framework.locator('[data-framework-action="next"]').isDisabled());
  await framework.locator('[data-framework-outcome]').selectOption('retry');
  assert.equal(await framework.getAttribute('data-frame'),'4','scenario change keeps the current stage');
  assert.match(await framework.locator('[data-framework-title]').textContent(),/仍要等/);
  await framework.locator('[data-framework-action="play"]').click();
  await framework.locator('[data-framework-outcome]').selectOption('accept');
  await page.clock.runFor(4250);
  assert.equal(await framework.getAttribute('data-frame'),'0','changing the outcome stops playback');
  await framework.locator('[data-framework-action="play"]').click();
  assert.equal(await framework.getAttribute('data-frame'),'0','play at the end restarts');
  await page.evaluate(()=>window.dispatchEvent(new Event('beforeprint')));
  assert.equal(await framework.locator('[data-framework-action="play"]').getAttribute('aria-label'),'播放');
  await page.emulateMedia({media:'print'});
  assert.ok(await framework.isHidden(),'print uses authored static comparison');
  await page.emulateMedia({media:'screen'});
  await page.evaluate(()=>window.dispatchEvent(new Event('afterprint')));
  await page.selectOption('#jump','13');
  await page.emulateMedia({reducedMotion:'reduce'});
  assert.equal(await page.locator('#s14 .trace-node').first().evaluate(el=>getComputedStyle(el).animationName),'none');
  await page.selectOption('#jump','1');
  await page.locator('#s2 [data-mode="sft"]').press('ArrowRight');
  assert.equal(await page.locator('#s2 .maze-lab').getAttribute('data-maze-mode'),'ppo');
  const switchedTitle=await page.locator('#s2 h1').textContent();
  assert.ok(switchedTitle.startsWith('PPO：'),'keyboard tab switching updates heading');
  await page.evaluate(()=>window.dispatchEvent(new Event('beforeprint')));
  assert.equal(await page.locator('#s2 h1').textContent(),await page.locator('#s2 h1').getAttribute('data-original-title'),'print matches original static content');
  assert.equal(await page.locator('details.original:not([open])').count(),0);
  await page.evaluate(()=>window.dispatchEvent(new Event('afterprint')));
  assert.equal(await page.locator('#s2 h1').textContent(),switchedTitle,'after print restores selected mode heading');
  assert.equal(await page.locator('details.original[open]').count(),0);
  assert.deepEqual(errors,[]);assert.deepEqual(requests,[]);
  console.log(JSON.stringify({layouts,errors,externalRequests:requests,screenshots,checks:'16-slide content bindings, all retained animation states, 3 framework scenes with both async outcomes x 4 viewports, play/pause, reset, scenario switch, slide lifecycle, real group training, keyboard, notes, reduced motion, print fallback'},null,2));
  assert.deepEqual(layouts,[],'unexpected viewport overflow');
} finally {await browser.close();}
