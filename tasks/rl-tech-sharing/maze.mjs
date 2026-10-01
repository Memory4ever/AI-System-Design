// A finite-horizon teaching MDP. Policy parameters are per-cell action logits, not a neural network.
export const maze = {
  rows: ['#######', '#S...G#', '#.#.#.#', '#.....#', '#######'],
  width: 7, height: 5, start: 8, goal: 12, horizon: 24,
  moves: [-7, 1, 7, -1], names: ['U','R','D','L'],
};
maze.cells = maze.rows.flatMap((row,y)=>[...row].flatMap((c,x)=>c==='#'?[]:[y*7+x]));
const legal = s => maze.moves.map(d=>maze.cells.includes(s+d));
const zeros = () => Array.from({length:35},()=>[0,0,0,0]);
const mean = v => v.reduce((a,b)=>a+b,0)/v.length;
const clip = x => Math.max(.8, Math.min(1.2,x));

export function policy(logits,s) {
  const mask=legal(s), max=Math.max(...logits[s].filter((_,a)=>mask[a]));
  const w=logits[s].map((z,a)=>mask[a]?Math.exp(z-max):0), sum=w.reduce((a,b)=>a+b);
  return w.map(x=>x/sum);
}

function stepReward(next, reward) { return reward==='steps'?.05:(next===maze.goal?1:0)-.02; }
function makePath(actions, logits, reward='exit') {
  let s=maze.start, total=0;
  const steps=[];
  for (const a of actions) {
    if(s===maze.goal || steps.length===maze.horizon) break;
    if(!legal(s)[a])throw new Error('route enters a wall');
    const next=s+maze.moves[a], r=stepReward(next,reward);
    steps.push({s,a,next,r,t:steps.length,old:policy(logits,s)[a]});
    s=next;total+=r;
  }
  let remaining=0;
  for(let t=steps.length-1;t>=0;t--) { remaining+=steps[t].r;steps[t].returns=remaining; }
  return {steps,total,success:s===maze.goal};
}

export function route(text, logits=zeros(), reward='exit') {
  return makePath([...text].map(c=>maze.names.indexOf(c)),logits,reward);
}

function randomGenerator(seed) {
  let state=seed>>>0;
  return ()=>{state=(Math.imul(1664525,state)+1013904223)>>>0;return state/4294967296;};
}

function rollout(logits,rng,reward) {
  let s=maze.start;const actions=[];
  for(let t=0;t<maze.horizon && s!==maze.goal;t++) {
    const probabilities=policy(logits,s);let u=rng(),a=0;
    while(a<3 && (u-=probabilities[a])>=0)a++;
    actions.push(a);s+=maze.moves[a];
  }
  return makePath(actions,logits,reward);
}

export function groupAdvantages(rewards) {
  const m=mean(rewards),sd=Math.sqrt(mean(rewards.map(r=>(r-m)**2)));
  return rewards.map(r=>(r-m)/(sd+1e-8));
}

// Exact evaluation by probability propagation; no training samples enter this measurement.
export function evaluate(logits,reward='exit') {
  let mass=Array(35).fill(0),success=0,total=0;mass[maze.start]=1;
  for(let t=0;t<maze.horizon;t++) {
    const nextMass=Array(35).fill(0);
    for(const s of maze.cells) if(mass[s] && s!==maze.goal) {
      policy(logits,s).forEach((p,a)=>{
        if(!p)return;
        const next=s+maze.moves[a],weight=mass[s]*p;
        total+=weight*stepReward(next,reward);
        if(next===maze.goal)success+=weight;else nextMass[next]+=weight;
      });
    }
    mass=nextMass;
  }
  return {success:Math.max(0,Math.min(1,success)),reward:total};
}

function logPath(logits,path) {
  return path.steps.reduce((sum,{s,a})=>sum+Math.log(policy(logits,s)[a]),0);
}

export function objective(logits,batch) {
  const gradient=zeros();let loss=0;
  const add=(s,a,c)=>policy(logits,s).forEach((p,j)=>{gradient[s][j]+=c*((j===a?1:0)-p);});
  if(batch.mode==='sft') {
    const samples=batch.paths.flatMap(p=>p.steps);
    for(const {s,a} of samples) {loss-=Math.log(policy(logits,s)[a])/samples.length;add(s,a,-1/samples.length);}
  } else if(batch.mode==='dpo') {
    const [chosen,rejected]=batch.paths, beta=.3;
    const delta=beta*(logPath(logits,chosen)-logPath(logits,rejected)-batch.referenceGap);
    loss=Math.max(0,-delta)+Math.log1p(Math.exp(-Math.abs(delta)));
    const c=-beta/(1+Math.exp(delta));
    for(const {s,a} of chosen.steps)add(s,a,c);
    for(const {s,a} of rejected.steps)add(s,a,-c);
  } else {
    const n=batch.paths.reduce((sum,p)=>sum+p.steps.length,0);
    batch.paths.forEach(path=>path.steps.forEach(({s,a,old,advantage})=>{
      const ratio=policy(logits,s)[a]/old;
      const weight=batch.mode==='grpo'?1/(batch.paths.length*path.steps.length):1/n;
      loss-=Math.min(ratio*advantage,clip(ratio)*advantage)*weight;
      const saturated=advantage>0?ratio>1.2:ratio<.8;
      if(!saturated)add(s,a,-advantage*ratio*weight);
    }));
  }
  return {loss,gradient};
}

export class MazeTrainer {
  constructor(mode='ppo',reward='exit',seed=20260923) {
    if(!['sft','ppo','grpo','dpo'].includes(mode))throw new Error('unknown mode');
    this.mode=mode;this.reward=reward;this.seed=seed;this.version=0;
    this.logits=zeros();this.reference=zeros();
    this.values=Array.from({length:maze.horizon},()=>Array(35).fill(0));
    this.rng=randomGenerator(seed);this.evalRng=randomGenerator(seed+1);
    this.history=[{iteration:0,loss:null,criticLoss:null,...evaluate(this.logits,reward)}];
  }
  prepare() {
    let paths;
    if(this.mode==='sft')paths=[route('RRRR',this.logits,this.reward)];
    else if(this.mode==='dpo')paths=[route('RRRR',this.logits,this.reward),route('DDRRRRUU',this.logits,this.reward)];
    else paths=Array.from({length:8},()=>rollout(this.logits,this.rng,this.reward));
    const advantages=groupAdvantages(paths.map(p=>p.total));
    paths.forEach((path,i)=>path.steps.forEach(step=>{
      step.value=this.values[step.t][step.s];
      step.advantage=this.mode==='grpo'?advantages[i]:step.returns-step.value;
    }));
    return {mode:this.mode,version:this.version,paths,advantages,
      referenceGap:this.mode==='dpo'?logPath(this.reference,paths[0])-logPath(this.reference,paths[1]):0,
    };
  }
  update(batch) {
    if(batch.version!==this.version || batch.mode!==this.mode)throw new Error('batch version mismatch');
    const epochs=['ppo','grpo'].includes(this.mode)?4:1;
    const rate={sft:.9,ppo:1.8,grpo:1,dpo:.5}[this.mode];
    for(let i=0;i<epochs;i++) {
      const {gradient}=objective(this.logits,batch);
      for(const s of maze.cells) for(let a=0;a<4;a++)this.logits[s][a]-=rate*gradient[s][a];
    }
    let criticLoss=null;
    if(this.mode==='ppo') {
      const targets=new Map();
      for(const path of batch.paths)for(const step of path.steps) {
        const key=`${step.t}:${step.s}`;
        if(!targets.has(key))targets.set(key,[]);
        targets.get(key).push(step.returns);
      }
      let squared=0,n=0;
      for(const [key,returns] of targets) {
        const [t,s]=key.split(':').map(Number);
        this.values[t][s]+=.3*(mean(returns)-this.values[t][s]);
        for(const target of returns) {squared+=(this.values[t][s]-target)**2;n++;}
      }
      criticLoss=squared/n;
    }
    const loss=objective(this.logits,batch).loss;
    this.version++;
    const point={iteration:this.version,loss,criticLoss,...evaluate(this.logits,this.reward)};
    this.history.push(point);
    batch.evaluationPath=rollout(this.logits,this.evalRng,this.reward);
    return point;
  }
}

const mazeModes = {
  sft: {name:'SFT',input:'固定示范',steps:['读取示范','模仿下一步','更新参数','重新评估'],
    title:'SFT 给出示范，但示范没有覆盖所有尝试',
    loss:'示范动作交叉熵', message:'沿示范路线提高每一步的概率。得分仅作评估，不参与这次训练。'},
  ppo: {name:'PPO',input:'本轮 8 次尝试',steps:['冻结策略并尝试','回报减去预期','裁剪目标更新','重新评估'],
    title:'PPO：比较实际回报与预期，更新策略和 Critic',
    loss:'负裁剪策略目标',message:'实际回报与 Critic 预期比较，再限制对同一批行动的更新幅度。'},
  grpo: {name:'GRPO',input:'同起点 8 条路线',steps:['冻结策略并尝试','比较组内得分','裁剪目标更新','重新评估'],
    title:'GRPO：用同题多次尝试替代 Critic 基线',
    loss:'负组优势裁剪目标',message:'不训练 Critic；把同起点的多次尝试互相比较，整条路线共享组优势。'},
  dpo: {name:'DPO',input:'固定偏好对',steps:['读取两条路线','比较当前与参考','偏好损失更新','重新评估'],
    title:'DPO：已有偏好对时，直接学习相对偏好',
    loss:'偏好对负对数损失',message:'固定偏好：都能到出口，但短路线更受偏好。两条路线都参与更新，不依赖在线得分。'},
};


export function mazeMarkup(mode,icons,reward='exit') {
  return `<div class="maze-lab" data-maze-mode="${mode}" data-maze-reward="${reward}">
    <div class="maze-toolbar"><div class="maze-tabs" role="tablist" aria-label="训练方式">${Object.keys(mazeModes).map(key=>`<button role="tab" data-mode="${key}" aria-selected="${key===mode}">${mazeModes[key].name}</button>`).join('')}</div>
    <label>奖励规则 <select data-reward><option value="exit" ${reward==='exit'?'selected':''}>到达出口</option><option value="steps" ${reward==='steps'?'selected':''}>只奖励步数（反例）</option></select></label></div>
    <div class="maze-rule" data-rule></div>
    <ol class="maze-phases">${Array.from({length:4},()=>'<li></li>').join('')}</ol>
    <div class="maze-layout"><div class="maze-scene"><svg class="maze-board" viewBox="0 0 420 300" role="img" aria-label="同一迷宫，黄色角色从起点移动到出口"></svg>
    <div class="maze-live"><span data-step-label></span><strong data-return></strong></div>
    <div class="maze-probs" data-probs></div></div>
    <div class="maze-data"><div class="maze-metrics"><span>参数更新 <strong data-iteration>0</strong></span><span>到达出口 <strong data-success></strong></span><span>平均得分 <strong data-score></strong></span></div>
    <div class="maze-chart"><div><strong>效果</strong><span>绿：到达出口概率 · 黄：平均得分</span></div><svg data-performance viewBox="0 0 460 105" role="img" aria-label="逐轮评估结果"></svg></div>
    <div class="maze-chart"><div><strong>Loss</strong><span data-loss-title></span></div><svg data-loss viewBox="0 0 460 105" role="img" aria-label="逐轮训练目标"></svg></div>
    <div class="maze-feedback" data-feedback></div></div></div>
    <div class="maze-narration" aria-live="polite" data-narration></div>
    <div class="maze-controls"><button data-maze-action="play" title="播放或暂停" aria-label="播放动画">${icons.play}</button><button data-maze-action="step" title="下一步" aria-label="下一步">${icons.next}</button><button data-maze-action="reset" title="重置实验" aria-label="重置实验">${icons.reset}</button><button data-maze-action="train">训练 10 轮</button><label>速度 <select data-speed><option value="500">慢</option><option value="180" selected>中</option><option value="60">快</option></select></label><span data-run-label></span></div>
    <p class="maze-boundary">实时表格策略实验，最多 24 步；曲线来自计算，非预设动画。不是 LLM，不作算法排名。</p>
  </div>`;
}

export function mazeScene(path,move,active=-1,demonstration=null) {
  const upto=path.steps.slice(0,move),s=upto.at(-1)?.next??maze.start;
  const xy=p=>[p%7*60+30,Math.floor(p/7)*60+30];
  const demo=demonstration?`<g data-demo-route><rect x="76" y="13" width="268" height="34" rx="4" fill="#314b57"/><text x="210" y="36" text-anchor="middle" fill="#fff" font-size="16">蓝色虚线 1→${demonstration.steps.length}：给定示范</text><polyline points="${[maze.start,...demonstration.steps.map(st=>st.next)].map(xy).map(v=>v.join(',')).join(' ')}" fill="none" stroke="#3869a1" stroke-width="4" stroke-dasharray="7 5"/>${demonstration.steps.map((st,i)=>{
    const [x,y]=xy(st.s),[nx,ny]=xy(st.next),mx=(x+nx)/2,my=(y+ny)/2;
    return `<g data-demo-step="${i+1}"><circle cx="${mx}" cy="${my-19}" r="10" fill="#fff" stroke="#3869a1" stroke-width="2"/><text x="${mx}" y="${my-14}" text-anchor="middle" fill="#28527f" font-size="14" font-weight="600">${i+1}</text><path d="M-5 -5L1 0L-5 5" transform="translate(${mx},${my}) rotate(${[-90,0,90,180][st.a]})" fill="none" stroke="#3869a1" stroke-width="2.5"/></g>`;
  }).join('')}</g>`:'';
  return maze.rows.map((row,y)=>[...row].map((c,x)=>c==='#'?`<rect x="${x*60+2}" y="${y*60+2}" width="56" height="56" rx="4" fill="#314b57"/>`:'').join('')).join('')+
    `<rect x="300" y="60" width="60" height="60" fill="#d4eedf"/><text x="330" y="95" text-anchor="middle" fill="#167350" font-size="17">出口</text><text x="90" y="108" text-anchor="middle" fill="#63706a" font-size="12">起点</text>`+
    `<polyline points="${[maze.start,...upto.map(st=>st.next)].map(xy).map(v=>v.join(',')).join(' ')}" fill="none" stroke="#67af9c" stroke-width="5" stroke-linejoin="round" opacity=".7"/>`+
    demo+
    (active>=0?`<circle cx="${xy(path.steps[active].s)[0]}" cy="${xy(path.steps[active].s)[1]}" r="25" stroke="#bb7d19" stroke-width="4" fill="#f8e5b6" fill-opacity=".5"/>`:'')+
    `<g class="maze-player" transform="translate(${xy(s).join(',')}) rotate(${upto.length?[-90,0,90,180][upto.at(-1).a]:0})"><path d="M0 0L16 -13A21 21 0 1 0 16 13Z" fill="#f5c542" stroke="#765d0c" stroke-width="1.5"/><circle cx="-2" cy="-10" r="2.5" fill="#303b39"/></g>`;
}

function mazeChart(svg,series,range) {
  const values=series.flatMap(s=>s.points.map(p=>p.y));
  let min=range?.[0]??Math.min(0,...values),max=range?.[1]??Math.max(.01,...values);
  if(max-min<.01)max=min+.01;
  const last=Math.max(10,...series.flatMap(s=>s.points.map(p=>p.x)));
  const x=v=>42+v/last*402,y=v=>78-(v-min)/(max-min)*65;
  svg.innerHTML=`<path d="M42 9V78H446" fill="none" stroke="#bac6bf"/><text x="1" y="17">${max.toFixed(2)}</text><text x="1" y="79">${min.toFixed(2)}</text><text x="40" y="100">0</text><text x="388" y="100">${last} 轮</text>`+series.map(s=>`<polyline points="${s.points.map(p=>`${x(p.x)},${y(p.y)}`).join(' ')}" fill="none" stroke="${s.color}" stroke-width="2.5"/>${s.points.length?`<circle cx="${x(s.points.at(-1).x)}" cy="${y(s.points.at(-1).y)}" r="3" fill="${s.color}"/>`:''}`).join('');
}

export function mountMazes(icons) {
  document.querySelectorAll('.maze-lab').forEach(root=>{
    let trainer,batch,phase=0,pathIndex=0,move=0,timer=null;
    const heading=root.closest('.slide')?.querySelector('[data-maze-heading]');
    const initialMode=root.dataset.mazeMode,initialReward=root.dataset.mazeReward;
    const originalTitle=heading?.textContent;
    const find=s=>root.querySelector(s);
    function stop() {clearTimeout(timer);timer=null;find('[data-maze-action="play"]').innerHTML=icons.play;find('[data-maze-action="play"]').setAttribute('aria-label','播放动画');}
    function reset(mode=root.dataset.mazeMode,reward=find('[data-reward]').value) {
      stop();root.dataset.mazeMode=mode;root.dataset.mazeReward=reward;
      trainer=new MazeTrainer(mode,reward);batch=trainer.prepare();phase=0;pathIndex=0;move=0;render();
    }
    function paths() {return phase===3?[batch.evaluationPath]:batch.paths;}
    function renderBoard(path) {
      const upto=path.steps.slice(0,move), s=upto.at(-1)?.next??maze.start;
      const board=find('.maze-board');
      board.innerHTML=mazeScene(path,move,-1,trainer.mode==='sft'&&phase!==3?batch.paths[0]:null);
      board.setAttribute('aria-label',trainer.mode==='sft'&&phase!==3?'给定的 SFT 示范：从起点向右走四步到出口，1 至 4 步预先标出':'同一迷宫，黄色角色从起点移动到出口');
      const probs=policy(trainer.logits,s);
      find('[data-probs]').innerHTML=s===maze.goal?'到达出口，轨迹结束':probs.map((p,a)=>`<span class="${p?'':'unavailable'}">${['↑','→','↓','←'][a]} ${(p*100).toFixed(0)}%</span>`).join('');
      find('[data-step-label]').textContent=`${phase===3?'新策略评估':trainer.mode==='sft'?'给定示范':'路线 '+(pathIndex+1)+'/'+paths().length} · 行动 ${move}/${path.steps.length}`;
      const total=upto.reduce((sum,st)=>sum+st.r,0);
      find('[data-return]').textContent=`累计 ${total.toFixed(2)}${move?' · 本步 '+upto.at(-1).r.toFixed(2):''}`;
    }
    function render() {
      const config=mazeModes[trainer.mode],current=trainer.history.at(-1);
      if(heading) {
        const title=trainer.reward==='steps'
          ? trainer.mode==='sft'?'SFT：奖励只用于评估，示范决定训练方向'
          : trainer.mode==='dpo'?'DPO：奖励只用于评估，偏好决定训练方向'
          : `${config.name}：错误奖励可能强化绕路`
          : config.title;
        heading.textContent=trainer.mode===initialMode&&trainer.reward===initialReward?originalTitle:title;
      }
      root.dataset.phase=String(phase);root.dataset.iteration=String(trainer.version);root.dataset.move=String(move);
      root.querySelectorAll('[data-mode]').forEach(el=>el.setAttribute('aria-selected',String(el.dataset.mode===trainer.mode)));
      root.querySelectorAll('.maze-phases li').forEach((el,i)=>{el.textContent=`${i+1} ${config.steps[i]}`;el.classList.toggle('active',i===phase);});
      find('[data-rule]').textContent=trainer.reward==='exit'?'固定奖励：每步 −0.02；到达出口额外 +1；24 步仍未到达则结束。':'错误目标：每走一步 +0.05，到达出口没有额外奖励；多绕路也能涨分。';
      find('[data-iteration]').textContent=String(trainer.version);
      find('[data-success]').textContent=`${(current.success*100).toFixed(1)}%`;
      find('[data-score]').textContent=current.reward.toFixed(3);
      find('[data-loss-title]').textContent=`${config.loss}${current.loss===null?' · 尚未更新':' · '+current.loss.toFixed(4)}`;
      mazeChart(find('[data-performance]'),[
        {color:'#167350',points:trainer.history.map(p=>({x:p.iteration,y:p.success}))},
        {color:'#bb7d19',points:trainer.history.map(p=>({x:p.iteration,y:p.reward}))},
      ],[-.5,1.25]);
      mazeChart(find('[data-loss]'),[{color:'#3869a1',points:trainer.history.filter(p=>p.loss!==null).map(p=>({x:p.iteration,y:p.loss}))}]);
      renderBoard(paths()[pathIndex]);
      const path=paths()[pathIndex];
      if(phase===0) {
        find('[data-feedback]').textContent=trainer.mode==='dpo'?'偏好固定：4 步到达 > 8 步到达。rejected 也成功。':trainer.mode==='sft'?'训练数据：4 步的示范路线。不是策略自己发现的路线。':`${config.input} · 采样期间参数固定为 v${trainer.version}`;
        find('[data-narration]').textContent=config.message;
      } else if(phase===1) {
        const detail=trainer.mode==='ppo'?`首步实际回报 ${path.total.toFixed(2)} − 预期 ${path.steps[0].value.toFixed(2)} = 优势 ${path.steps[0].advantage.toFixed(2)}`:
          trainer.mode==='grpo'?`组内得分 [${batch.paths.map(p=>p.total.toFixed(2)).join(', ')}]；当前路线优势 ${batch.advantages[pathIndex].toFixed(2)}`:
          trainer.mode==='dpo'?'两条路线分别计算当前与冻结 reference 的完整轨迹概率；排序不是本轮打分生成。':'示范的下一步作为标签；计算负 log 概率，不把奖励乘进 SFT loss。';
        find('[data-feedback]').textContent=detail;
        find('[data-narration]').textContent='反馈已经准备好，但参数还没更新，曲线也不应提前变化。';
      } else if(phase===2) {
        find('[data-feedback]').textContent=`待更新的目标值 ${objective(trainer.logits,batch).loss.toFixed(4)}${trainer.mode==='ppo'?'；Critic 另学回报预测。':''}`;
        find('[data-narration]').textContent='下一步才计算梯度、更新参数。小角色的移动与参数更新是不同阶段。';
      } else {
        find('[data-feedback]').textContent=`参数已更新到 v${trainer.version}${current.criticLoss!==null?' · Critic 均方误差 '+current.criticLoss.toFixed(4):''}。评估覆盖当前策略所有可能路线的概率。`;
        find('[data-narration]').textContent=['sft','dpo'].includes(trainer.mode)?'奖励曲线只用于评估；训练依赖原有示范或偏好对。Loss 变好不证明新地图也会走。':'Loss 的样本和优势每轮都在变，不要求曲线单调下降；效果要看出口概率与任务目标是否一致。';
      }
      find('[data-run-label]').textContent=`种子 ${trainer.seed} · ${config.input}`;
    }
    function advance() {
      if(phase===0) {
        if(move<paths()[pathIndex].steps.length)move++;
        else if(pathIndex<paths().length-1) {pathIndex++;move=0;}
        else phase=1;
      } else if(phase===1)phase=2;
      else if(phase===2) {trainer.update(batch);phase=3;pathIndex=0;move=0;}
      else if(move<paths()[0].steps.length)move++;
      else {batch=trainer.prepare();phase=0;pathIndex=0;move=0;}
      render();
    }
    function tick() {advance();timer=setTimeout(tick,Number(find('[data-speed]').value));}
    root.querySelectorAll('[data-mode]').forEach(el=>{
      el.onclick=()=>reset(el.dataset.mode);
      el.onkeydown=e=>{
        if(!['ArrowLeft','ArrowRight'].includes(e.key))return;
        e.preventDefault();e.stopPropagation();
        const keys=Object.keys(mazeModes),next=keys[(keys.indexOf(el.dataset.mode)+(e.key==='ArrowRight'?1:3))%4];
        reset(next);find(`[data-mode="${next}"]`).focus();
      };
    });
    find('[data-reward]').onchange=()=>reset();
    find('[data-maze-action="reset"]').onclick=()=>reset();
    find('[data-maze-action="step"]').onclick=()=>{stop();advance();};
    find('[data-maze-action="play"]').onclick=()=>{
      if(timer!==null)stop();else {find('[data-maze-action="play"]').innerHTML=icons.pause;find('[data-maze-action="play"]').setAttribute('aria-label','暂停动画');timer=setTimeout(tick,Number(find('[data-speed]').value));}
    };
    find('[data-maze-action="train"]').onclick=()=>{
      stop();for(let i=0;i<10;i++){if(phase===3)batch=trainer.prepare();trainer.update(batch);phase=3;}
      move=0;pathIndex=0;render();
    };
    document.addEventListener('slidechange',stop);
    document.addEventListener('visibilitychange',()=>{if(document.hidden)stop();});
    reset();
  });
}
