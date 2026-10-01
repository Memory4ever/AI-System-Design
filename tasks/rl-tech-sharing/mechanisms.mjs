import { maze, route, policy, MazeTrainer, mazeScene } from './maze.mjs';

export const mechanismNames={sampling:'采样与更新',credit:'奖励怎样传回动作',rm:'先学评分，再学策略',dpo:'偏好改善不等于成功率提高',repair:'奖励修正与参数恢复'};
const fmt=n=>n.toFixed(3),pct=n=>`${(100*n).toFixed(1)}%`;
export function scorerTrace() {
  let w=0;const result=[];
  for(let i=0;i<=8;i++) {
    const short=w*.5,long=w,delta=short-long,preferredProbability=1/(1+Math.exp(-delta));
    result.push({w,short,long,preferredProbability,loss:Math.log1p(Math.exp(-delta))});
    w-=.8*(preferredProbability-1)*(-.5);
  }
  return result;
}

// Frames carry computed quantities separately from explanatory text and synthetic counterexamples.
export function mechanismFrames(id) {
  const short=route('RRRR'),long=route('DDRRRRUU');
  const base={path:short,move:0,headers:['对象','当前值','含义'],rows:[],bars:[],boundary:'按实际表格计算结果分步回放；不与实时训练实验拼接曲线。'};
  const frame=data=>({...base,...data});
  if(id==='sampling') {
    const trainer=new MazeTrainer('ppo'),batch=trainer.prepare(),path=batch.paths[0];
    const probabilities=()=>path.steps.slice(0,4).map(s=>policy(trainer.logits,s.s)[s.a]);
    const before=probabilities(),rows=p=>p.map((n,i)=>[`第 ${i+1} 步 ${maze.names[path.steps[i].a]}`,pct(n),'同一已采样动作的条件概率']);
    const frames=[0,1,2,3].map(move=>frame({path,move,title:move?'冻结策略，继续采样':'先收集一条路线',rows:rows(before),version:0,probabilities:before,
      caption:'角色按 v0 策略逐步行动；走过的状态、动作和 old 概率被保存。参数尚未变化。'}));
    frames.push(frame({path,move:path.steps.length,title:'固定这批路线，重新计算概率',rows:rows(before),version:0,probabilities:before,
      caption:'更新阶段读取已经走过的路线，不重新抽下一步。SFT 同样读取已知前缀，但标签来自示范。'}));
    trainer.update(batch);const after=probabilities();
    frames.push(frame({path,move:path.steps.length,title:'参数变为 v1，动作记录不变',rows:rows(after),version:1,probabilities:after,
      bars:[['第 1 步更新前',before[0]],['第 1 步更新后',after[0]]],caption:'同一动作的概率发生变化；下一批 rollout 才使用新策略。此处执行了真实表格 PPO 更新。'}));
    return frames;
  }
  if(id==='credit') {
    const returns=short.steps.map(s=>s.returns),values=[.5,.6,.7,.8];
    return Array.from({length:9},(_,i)=>{
      const reverse=i>=5,active=reverse?8-i:-1;
      return frame({move:Math.min(i,4),active,returns,title:reverse?`从终点向前累计：第 ${active+1} 步`:(i===4?'出口奖励出现了':'先走，再得到每步反馈'),
        headers:['行动 / 即时奖励','未来回报','减去预期'],rows:short.steps.map((s,t)=>{
          const known=i>t,back=reverse&&t>=active;
          return [`${t+1} →  ${known?s.r.toFixed(2):'待发生'}`,back?s.returns.toFixed(2):'待累计',back?`${s.returns.toFixed(2)} − ${values[t].toFixed(2)} = ${(s.returns-values[t]).toFixed(2)}`:'待比较'];
        }),bars:reverse?[['本步 Return',returns[active],returns[active].toFixed(2)],['示例 Value',values[active],values[active].toFixed(2)]]:[],
        caption:reverse?'回报只累计本步及之后的奖励，再减去预期。这里只计算反馈，尚未反向传播；数值更大不等于因果贡献更大。':'每步 −0.02，到达额外 +1。走动与回报计算是不同阶段，参数没有自动更新。',
        boundary:'Return 由路线精确计算，γ=1；Value 为示意值，不是此次训练所得。'});
    });
  }
  if(id==='rm') {
    const trace=scorerTrace();
    return [0,1,4,8,8,8].map((n,i)=>{
      const s=trace[n];return frame({path:i>=4?route('RLRRRR'):i===1?long:short,move:i===0?0:i>=4?6:i===1?8:4,
        title:['人给两条路线排序','把排序变成评分器训练数据','只更新评分器','评分器更符合这组偏好','冻结评分器，评价新路线','接下来才更新行动策略'][i],
        rows:[['短路线分数',fmt(s.short),'4 步到达，人工偏好'],['长路线分数',fmt(s.long),'8 步到达，不是失败'],['偏好损失',fmt(s.loss),`评分器更新 ${n} 次`],...(i>=4?[['6 步新路线分数',fmt(s.w*.75),'冻结评分器计算；未证明泛化']]:[])],
        bars:[['评分器认为短路更优',s.preferredProbability]],
        caption:i<4?'人工排序只训练评分器。这里学一个路线长度权重，行动策略完全不变。':i===4?'用已经固定的评分器给新尝试打分。偏好分数没有天然零点，也不是成功概率。':'将分数交给 PPO / GRPO 才能更新策略；Critic 另预测未来回报，DPO 则绕过独立评分器。',
        boundary:'实际计算一维线性评分器的偏好损失；不是神经 Reward Model，也未执行评分器驱动的策略训练。'});
    });
  }
  if(id==='dpo') {
    return [0,1/3,2/3,1].map((t,i)=>{
      const chosen=.4-.1*t,rejected=.2-.15*t,ratio=chosen/rejected,loss=Math.log1p(Math.exp(-.3*Math.log(ratio/2)));
      return frame({move:i+1,title:i?'偏好比变好，成功质量却流失':'两条路线都能到达出口',loss,success:chosen+rejected,
        rows:[['短路 chosen',pct(chosen),'绝对概率下降'],['长路 rejected',pct(rejected),'下降得更快'],['偏好比',`${ratio.toFixed(2)} 倍`,'固定 reference 比值为 2'],['DPO loss',fmt(loss),'β=0.3；相对目标改善']],
        bars:[['两条成功路线合计',chosen+rejected],['其他失败路线',1-chosen-rejected]],
        caption:'提高 chosen / rejected 的比值，不要求 chosen 的绝对概率增加。必须另测任务成功率。',
        boundary:'人为构造的合法分布反例；不是迷宫 DPO 优化器的训练记录。'});
    });
  }
  if(id==='repair') {
    let trainer=new MazeTrainer('ppo','steps');const batch=trainer.prepare(),path=batch.paths[0];
    const snapshot=()=>JSON.stringify([trainer.version,trainer.logits,trainer.values]);
    const initial=snapshot(),before=policy(trainer.logits,maze.start)[1];
    trainer.update(batch);const changed=snapshot(),after=policy(trainer.logits,maze.start)[1];
    const corrected=route(path.steps.map(s=>maze.names[s.a]).join(''),trainer.logits,'exit');
    const afterRescore=snapshot();
    trainer=new MazeTrainer('ppo','steps');
    return [0,1,2,3].map(i=>frame({path,move:i?path.steps.length:0,fingerprint:i===0?initial:i===3?snapshot():i===2?afterRescore:changed,
      title:['先保存一致的训练状态','错误奖励已经进入一次更新','改对数据里的分数，参数不会自动回退','回到旧状态，再决定如何继续训练'][i],
      rows:[['策略参数',i===0||i===3?'v0':'v1',i===2?'仍是错误奖励训练后的参数':'与训练进度一致'],['起点向右概率',pct(i===0||i===3?before:after),'由真实表格策略计算'],['本条路线重评分',i>=2?`${fmt(path.total)} → ${fmt(corrected.total)}`:'尚未修正','重新计算奖励不写策略参数']],
      bars:[['起点向右概率',i===0||i===3?before:after]],
      caption:i===3?'这里按原种子重建，恢复玩具实验初始状态。实际训练还需一致的 optimizer、数据进度等，或用纠正后的数据继续训练并回归验证。':'打分错误与参数错误发生在不同阶段。更新前可重算反馈；更新后，修改标签不是撤销训练。',
      boundary:'执行一次错误奖励的表格 PPO 更新；随后展示分数修正不改参数与确定性重建，不模拟大模型 checkpoint 恢复。'}));
  }
  throw new Error(`Unknown mechanism: ${id}`);
}

export function mechanismMarkup(id,icons,scope=Object.keys(mechanismNames)) {
  return `<div class="mechanism" data-mechanism="${id}">
    <div class="mechanism-toolbar"><label>机制 <select data-mechanism-select aria-label="选择机制">${scope.map(key=>`<option value="${key}" ${id===key?'selected':''}>${mechanismNames[key]}</option>`).join('')}</select></label><span data-mechanism-progress></span></div>
    <h2 data-mechanism-title></h2>
    <div class="mechanism-layout"><div class="mechanism-scene"><svg class="maze-board" viewBox="0 0 420 300" role="img" aria-label="同一迷宫中的行动与反馈"></svg><div class="mechanism-route" data-mechanism-route></div><div class="mechanism-actions" data-mechanism-actions></div></div>
    <div class="mechanism-data"><table><thead></thead><tbody></tbody></table><svg class="mechanism-chart" viewBox="0 0 500 130" role="img" aria-label="当前机制的数值对照"></svg></div></div>
    <p class="mechanism-caption" data-mechanism-caption aria-live="polite"></p>
    <div class="mechanism-controls"><button data-mechanism-action="back" title="上一步" aria-label="上一步">${icons.back}</button><button data-mechanism-action="play" title="播放或暂停" aria-label="播放机制动画">${icons.play}</button><button data-mechanism-action="next" title="下一步" aria-label="下一步">${icons.next}</button><button data-mechanism-action="reset" title="重置机制" aria-label="重置机制">${icons.reset}</button><label>速度 <select data-mechanism-speed><option value="3000" selected>慢</option><option value="1500">中</option><option value="600">快</option></select></label></div>
    <p class="mechanism-boundary" data-mechanism-boundary></p>
  </div>`;
}

function mechanismChart(frame) {
  const colors=['#167350','#3869a1'];
  return frame.bars.map(([label,value,display],i)=>`<text x="4" y="${22+i*56}">${label}</text><rect x="200" y="${7+i*56}" width="230" height="24" fill="#edf1ee"/><rect x="200" y="${7+i*56}" width="${Math.max(0,Math.min(1,value))*230}" height="24" fill="${colors[i%2]}"/><text x="438" y="${25+i*56}">${display??pct(value)}</text>`).join('');
}

export function mountMechanisms(icons) {
  document.querySelectorAll('.mechanism').forEach(root=>{
    let frames,index=0,timer=null;
    const find=s=>root.querySelector(s);
    function stop() {clearTimeout(timer);timer=null;find('[data-mechanism-action="play"]').innerHTML=icons.play;find('[data-mechanism-action="play"]').setAttribute('aria-label','播放机制动画');}
    function render() {
      const f=frames[index];root.dataset.frame=String(index);root.dataset.frames=String(frames.length);
      find('[data-mechanism-progress]').textContent=`${index+1} / ${frames.length}`;
      find('[data-mechanism-title]').textContent=f.title;
      find('.maze-board').innerHTML=mazeScene(f.path,f.move,f.active);
      find('[data-mechanism-route]').textContent=`已走 ${f.move} / ${f.path.steps.length} 步${f.path.steps.length>8?' · 下列仅显示前 8 步':f.active>=0?' · 黄圈标出回报计算位置':''}`;
      const steps=f.path.steps.slice(0,8);
      find('[data-mechanism-actions]').innerHTML=steps.map((s,i)=>`<span class="${i===f.active?'credit':i<f.move?'visited':''}">${i+1} ${['↑','→','↓','←'][s.a]}</span>`).join('');
      find('thead').innerHTML=`<tr>${f.headers.map(h=>`<th>${h}</th>`).join('')}</tr>`;
      find('tbody').innerHTML=f.rows.map((row,i)=>`<tr class="${i===f.active?'credit':''}">${row.map(cell=>`<td>${cell}</td>`).join('')}</tr>`).join('');
      find('.mechanism-chart').innerHTML=mechanismChart(f);
      find('[data-mechanism-caption]').textContent=f.caption;
      find('[data-mechanism-boundary]').textContent=f.boundary;
      find('[data-mechanism-action="back"]').disabled=index===0;
      find('[data-mechanism-action="next"]').disabled=index===frames.length-1;
    }
    function reset(id=find('[data-mechanism-select]').value) {
      stop();root.dataset.mechanism=id;find('[data-mechanism-select]').value=id;index=0;frames=mechanismFrames(id);render();
    }
    function tick() {index++;render();if(index===frames.length-1)stop();else timer=setTimeout(tick,Number(find('[data-mechanism-speed]').value));}
    find('[data-mechanism-select]').onchange=()=>reset();
    root.querySelectorAll('[data-mechanism-action]').forEach(button=>button.onclick=()=>{
      const action=button.dataset.mechanismAction;
      if(action==='play') {
        if(timer!==null){stop();return;}
        if(index===frames.length-1){index=0;render();}
        button.innerHTML=icons.pause;button.setAttribute('aria-label','暂停机制动画');
        timer=setTimeout(tick,Number(find('[data-mechanism-speed]').value));return;
      }
      stop();if(action==='reset')reset();else {index=Math.max(0,Math.min(frames.length-1,index+(action==='next'?1:-1)));render();}
    });
    root.addEventListener('keydown',e=>{
      if(e.target.tagName==='SELECT'||!['ArrowLeft','ArrowRight'].includes(e.key))return;
      e.preventDefault();e.stopPropagation();stop();index=Math.max(0,Math.min(frames.length-1,index+(e.key==='ArrowRight'?1:-1)));render();
    });
    document.addEventListener('slidechange',stop);
    document.addEventListener('visibilitychange',()=>{if(document.hidden)stop();});
    reset(root.dataset.mechanism);
  });
}
