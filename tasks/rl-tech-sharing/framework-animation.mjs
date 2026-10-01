const lane = (name, active, nodes, detail) => ({ name, active, nodes, detail });
const frame = (title, ready, updated, lanes, takeaway) => ({ title, ready, updated, lanes, takeaway });
const trainCycle = ['等待数据', '接收轨迹', '更新 v8', '准备权重', '确认交接'];
const rolloutCycle = ['生成 v7', '交付轨迹', '仍用 v7', '暂停与加载', '启用 v8'];
const engineFrame = (title, step, ready, updated, trainDetail, rolloutDetail, takeaway) => frame(title, ready, updated,
  [lane('训练端 · 更新策略', step, trainCycle, trainDetail), lane('vLLM · 生成回答', step, rolloutCycle, rolloutDetail)], takeaway);

// These are authored teaching states, not timings or traces from framework runs.
export const frameworkScenes = {
  shared: {
    label: '采样与权重',
    boundary: '以 vLLM 为例解释框架内的训练/生成交接；具体同步路径依配置而定。两题八回答为教学设定，不是实测。',
    frames: [
      engineFrame('先把反复尝试，变成高效的生成任务', 0, 0, false,
        '同步基线等待 Q1、Q2 各四条回答；这里还没有本批可用的训练数据。',
        '连续批处理让完成的槽位接入新请求；PagedAttention 按块管理不断增长的 KV。',
        'vLLM 加速生成，不负责定义奖励或替代 PPO / GRPO 的梯度更新。'),
      engineFrame('回答完成，还要变成对齐的训练数据', 1, 8, false,
        '接收评分与轨迹；Q1、Q2 分别比较，八条进入同一次更新。',
        '交付真实 token、行为 logprob 与版本 v7；不只交付回答的文字。',
        '生成、评分、概率重算各有成本；不能把它们全算作自回归解码。'),
      engineFrame('训练端已经 v8，生成端仍然是 v7', 2, 8, true,
        '对八条回答做前向、反向与梯度累积，再执行一次 optimizer step，得到 v8。',
        '尚未收到新权重，仍持有 v7；异步时可用它生成下一批，但必须记录版本。',
        '训练完成不等于生成端已更新。Actor 学策略，Critic 学价值，不能当成自动同步的副本。'),
      engineFrame('先建立交接窗口，再传输并加载参数', 3, 8, true,
        '按需转换训练/推理分片；交付策略参数，例如跨 GPU 用 NCCL，同卡进程可用 IPC。',
        '暂停并处理在途请求 → 接收/加载 v8 → 确认各 worker 完成；不在半套参数上生成。',
        '同卡可以减少部分搬运，但不等于 Actor、Critic、推理引擎共享参数或同步零成本。'),
      engineFrame('新权重生效，旧轨迹却不会自动变新', 4, 8, true,
        '交接确认后标记 v8 可用；队列中的 v7 轨迹仍按原版本和真实行为概率处理。',
        '处理旧 KV / prefix cache 后恢复生成；保留 token 续跑时，要重建适配新权重的 KV。',
        '权重同步解决“以后用什么生成”；数据校验解决“此前生成的样本还能不能用”。'),
    ],
  },
  handoff: {
    label: '数据交接',
    boundary: '两类机制互补，并非独占功能。概率与 token ID 是假设值；路由重放仅适用于支持的 MoE 配置。',
    frames: [
      frame('同一条 b1，交到训练端时还是原来的尝试吗？', 8, false, [
        lane('verl · 概率校验', 0, ['采样概率', '重算概率', '检查差异', '校正 / 过滤', '观察指标'],
          '固定权重 v7 与同一前缀：某 token 的采样概率记录为 0.20。'),
        lane('miles · 轨迹保真', 0, ['采样轨迹', '保留 token', '记录路由', '重放路由', '检查残差'],
          'b1 的原始 token：[31,42,9]；其中某 token 的 expert 为 {2,7}。'),
      ], '痛点：奖励没有变，但训练端可能在对“另一条轨迹”或另一种分布做更新。'),
      frame('看似相同的文本，未必是相同的训练输入', 8, false, [
        lane('verl · 概率校验', 1, ['采样 0.20', '重算 0.12', '检查差异', '校正 / 过滤', '观察指标'],
          '同权重重算得到 0.12：先查 token、精度与后端，而非直接断言策略学坏了。'),
        lane('miles · 轨迹保真', 1, ['[31,42,9]', '[31,42,9]', '记录路由', '重放路由', '检查残差'],
          'TITO 保留真实 token；避免解析、模板重渲染后变成假设的 [31,8,9]。'),
      ], '先保证行动序列一致，再讨论概率差异；重要性加权不能修复错位的 token。'),
      frame('输入一致，执行路径仍可能不同', 8, false, [
        lane('verl · 概率校验', 2, ['采样 0.20', '重算 0.12', '比值 0.60', '校正 / 过滤', '观察指标'],
          '教学比值 0.12 / 0.20 = 0.60。真实校正还取决于策略定义与 token / 序列配置。'),
        lane('miles · 轨迹保真', 2, ['原始 token', '原样传递', '记录 {2,7}', '重放路由', '检查残差'],
          'MoE 数值误差可能把训练路由改成 {2,8}；记录采样时的选择 {2,7}。'),
      ], '这里不是保留基座行为的 reference KL，而是检查生成与训练是否对上。'),
      frame('一个调整更新贡献，一个保留实际执行路径', 8, false, [
        lane('verl · 概率校验', 3, ['采样概率', '重算概率', '检查差异', '加权 / 拒绝', '观察指标'],
          'Rollout Correction：按所选模式重加权，或过滤偏差过大的样本。'),
        lane('miles · 轨迹保真', 3, ['原始 token', '原样传递', '记录 {2,7}', '重放 {2,7}', '检查残差'],
          'R3 在支持的训练路径重放 expert 选择；不让路由静默换成 {2,8}。'),
      ], '差异在干预位置：分布校正与轨迹保真可以共存，不是二选一。'),
      frame('降低一种错误，不等于消除所有误差', 8, false, [
        lane('verl · 概率校验', 4, ['采样概率', '重算概率', '检查差异', '校正 / 过滤', '偏差与拒绝率'],
          '代价：加权有方差，截断或过滤改变估计与数据；仍需检查有效样本。'),
        lane('miles · 轨迹保真', 4, ['原始 token', '原样传递', '记录路由', '重放路由', '剩余概率差'],
          '代价：记录、传输与适配成本；相同 token / expert 不保证数值完全一致。'),
      ], '两者都不能自动修好错误奖励，也不能凭空提供没有探索到的成功经验。'),
    ],
  },
  async: {
    label: '异步与等待',
    boundary: '教学情景：每批两题、每题四答。异步需资源余量；版本号不是质量分。时间不按比例，verl 也支持异步。',
    batchStates: [
      ['用 v7 生成中', '尚未开始'],
      ['八条已评分，训练中', '用 v7 生成中；v8 尚未训练完'],
      ['更新已完成：v7 → v8', '八条已生成并评分；仍标记 v7'],
      ['已用于第一次更新', '本例允许使用：保留 v7 行为记录'],
      ['已用于第一次更新', '用于第二次更新：v8 → v9'],
    ],
    timelines: [
      [
        {name: '生成', cells: [['第1批 v7','rollout'], ['空闲','wait'], ['接收 v8','sync'], ['第2批 v8','rollout'], ['第2批完成','rollout']]},
        {name: '训练', cells: [['等第1批','wait'], ['训第1批','train'], ['得到 v8','sync'], ['等第2批','wait'], ['后续再训练','check']]},
      ],
      [
        {name: '生成', cells: [['第1批 v7','rollout'], ['第2批 v7','rollout'], ['接收 v8','sync'], ['可继续采样','rollout'], ['后续尝试','rollout']]},
        {name: '训练', cells: [['等第1批','wait'], ['训第1批','train'], ['得到 v8','sync'], ['接受第2批','check'], ['更新到 v9','train']]},
      ],
    ],
    frames: [
      frame('两批数据，不是三个模型', 0, false, [
        lane('同步基线', 0, ['第1批','训练','同步','第2批','再训练'],
          '第1批：Q1、Q2 各四条路线。凑齐八条、评分并按题分组，才能训练。'),
        lane('异步示例 · miles', 0, ['第1批','重叠','同步','检查','再训练'],
          '第2批：Q3、Q4 各四条新路线，供下一次更新；不是第1批的续写。'),
      ], 'v7、v8、v9 才是同一策略的参数版本；两批数据分别提供两次学习经历。'),
      frame('训练第1批时，v8 还没完成：先用 v7 生成第2批', 8, false, [
        lane('同步基线', 1, ['第1批','训练','同步','第2批','再训练'],
          '第1批已完整并评分。训练端正在更新，生成端空闲，等待新参数。'),
        lane('异步示例 · miles', 1, ['第1批','重叠','同步','检查','再训练'],
          '独立生成资源用现有 v7 采第2批，同时训练第1批；并不是有 v8 却故意不用。'),
      ], '减少的就是这段空等。不能提前训练尚未生成的数据，也不能免费重叠两个满载任务。'),
      frame('第1次更新完成；提前生成的第2批仍属于 v7', 8, true, [
        lane('同步基线', 2, ['第1批','训练','同步','第2批','再训练'],
          '训练得到 v8 并完成权重交接，现在才能用 v8 开始第2批。'),
        lane('异步示例 · miles', 2, ['第1批','重叠','同步','检查','再训练'],
          '本例第2批八条已用 v7 生成并评分，随后才交接 v8；已有数据不会自动变成 v8。'),
      ], '旧的是“这些经历由谁产生”，不是“这些经历必然没价值”。v8 不一定已经学会 Q3、Q4。'),
      frame('检查通过：旧经历可以进入下一次训练', 8, true, [
        lane('同步基线', 3, ['第1批','训练','同步','第2批','再训练'],
          '正在用 v8 收集第2批，训练端等它完成；数据更新鲜，但起步较晚。'),
        lane('异步示例 · miles', 3, ['第1批','重叠','同步','检查','再训练'],
          '本例允许这次滞后：保留 v7 的 token、奖励与行为概率，v8 重算训练所需概率。'),
      ], '按所选算法校正分布差异；不是把旧梯度直接加到新模型，也不是落后一版就一定能用。'),
      frame('第2批派上用场：用旧经历，把当前策略 v8 更新到 v9', 8, true, [
        lane('同步基线', 4, ['第1批','训练','同步','第2批','再训练'],
          '本例此时第2批才收齐；评分、整理后也会训练。时间线仅表达先后，不是速度测量。'),
        lane('异步示例 · miles', 4, ['第1批','重叠','同步','检查','再训练'],
          '八条完整且获准使用，按 Q3 / Q4 分组计算目标，更新的是当前 v8，而非重新训练 v7。'),
      ], '收益：少等一段采样时间。代价：允许旧策略数据；校正有局限，仍需任务验证。'),
    ],
    retry: {
      batchStates: {3: ['已用于第一次更新', '本例不允许使用：原 v7 八条被拒绝'], 4: ['已用于第一次更新', '原八条已弃；用 v8 重新采样中']},
      trainerCells: [['等第1批','wait'], ['训第1批','train'], ['得到 v8','sync'], ['拒绝旧数据','check'], ['等待新数据','wait']],
      generationCells: [['第1批 v7','rollout'], ['第2批 v7','rollout'], ['接收 v8','sync'], ['安排重采','check'], ['第2批 v8','rollout']],
      frames: {
        3: {
          title: '检查未通过：这批旧经历不能直接拿来训练',
          detail: '本例的接受规则不允许这批滞后数据；拒绝两组旧回答，把 Q3、Q4 送回采样端。',
          takeaway: '这是一种对照情景，不是“v7 天生不能用”。版本、概率差异和算法约束共同影响接受规则。',
        },
        4: {
          title: '用 v8 重新采样；新数据未齐，训练仍要等',
          detail: '原 v7 回答不参与第二次更新。用 v8 重采 Q3、Q4 各四条；完成、评分并验收后才继续更新。',
          takeaway: '这次提前生成没有被用于学习，采样成本确实浪费了。异步必须看有效进展，而不是只看 GPU 忙不忙。',
        },
      },
    },
  },
};

export function frameworkFrame(scene, index, outcome = 'accept') {
  if (!Object.hasOwn(frameworkScenes, scene)) throw new Error(`Unknown framework scene: ${scene}`);
  const frames = frameworkScenes[scene].frames;
  const position = Math.max(0, Math.min(frames.length - 1, index));
  const current = frames[position];
  const variant = scene === 'async' && outcome === 'retry' ? frameworkScenes.async.retry.frames[position] : null;
  if (!variant) return current;
  return {...current, title: variant.title, takeaway: variant.takeaway,
    lanes: current.lanes.map((row, i) => i === 1 ? {...row, detail: variant.detail} : row)};
}

export function frameworkMarkup(icons) {
  const controls = [['back','上一步'],['play','播放'],['next','下一步'],['reset','重置']];
  return `<div class="framework-demo" data-framework-scene="shared" data-frame="0">
    <div class="framework-tabs" role="tablist" aria-label="框架对比场景">${Object.entries(frameworkScenes).map(([key,scene],index) => `<button type="button" role="tab" id="framework-tab-${key}" aria-controls="framework-panel" aria-selected="${index === 0}" tabindex="${index === 0 ? 0 : -1}" data-framework-tab="${key}">${scene.label}</button>`).join('')}</div>
    <div id="framework-panel" role="tabpanel" aria-labelledby="framework-tab-shared">
      <h2 data-framework-title></h2>
      <div class="framework-batch" aria-label="本批回答进度"><strong>本批</strong>${['a','b'].map((group,index) => `<div class="framework-group"><span>Q${index+1}</span>${[1,2,3,4].map(n => `<span class="framework-answer" data-answer="${group}${n}">${group}${n}</span>`).join('')}</div>`).join('')}<span data-framework-status></span></div>
      <div class="framework-async-info" hidden><div><strong>第1批 · Q1/Q2，各4答</strong><span data-batch-first></span></div><div><strong>异步第2批 · Q3/Q4，各4答</strong><span data-batch-second></span></div></div>
      <div class="framework-lanes"></div>
      <p class="framework-takeaway" data-framework-takeaway></p>
    </div>
    <div class="framework-controls">${controls.map(([action,label]) => `<button type="button" data-framework-action="${action}" aria-label="${label}" title="${label}">${icons[action] ?? ''}</button>`).join('')}<span data-framework-progress aria-live="polite"></span><label class="framework-outcome" hidden>旧数据情景 <select data-framework-outcome aria-label="旧数据接受情景"><option value="accept">本例允许使用</option><option value="retry">本例拒绝，重采</option></select></label><label>间隔 <select data-framework-speed aria-label="播放间隔"><option value="4000">4 秒</option><option value="7000" selected>7 秒</option><option value="10000">10 秒</option></select></label></div>
    <p class="framework-boundary" data-framework-boundary></p>
  </div>`;
}

export function mountFrameworks(icons) {
  document.querySelectorAll('.framework-demo').forEach(root => {
    let scene = 'shared', index = 0, outcome = 'accept', timer = null;
    const q = selector => root.querySelector(selector);
    const button = action => q(`[data-framework-action="${action}"]`);
    const render = () => {
      const current = frameworkFrame(scene, index, outcome), config = frameworkScenes[scene];
      root.dataset.frameworkScene = scene; root.dataset.frame = index;
      root.dataset.outcome = outcome;
      root.dataset.frames = config.frames.length;
      q('[data-framework-title]').textContent = current.title;
      q('.framework-batch').hidden = scene === 'async';
      q('.framework-async-info').hidden = scene !== 'async';
      q('.framework-outcome').hidden = scene !== 'async';
      if (scene === 'async') {
        const states = (outcome === 'retry' && config.retry.batchStates[index]) || config.batchStates[index];
        q('[data-batch-first]').textContent = states[0];
        q('[data-batch-second]').textContent = states[1];
      }
      q('[data-framework-status]').textContent = `${current.ready}/8 完成 · ${current.updated ? '本批已更新 v8' : '本批未更新'}`;
      root.querySelectorAll('[data-answer]').forEach((el,i) => {
        el.classList.toggle('complete', i < current.ready);
        el.classList.toggle('waiting', current.ready === 7 && i === 7);
        el.setAttribute('aria-label', `${el.dataset.answer}：${i < current.ready ? '完成' : '未完成'}`);
      });
      q('.framework-lanes').innerHTML = current.lanes.map((row,i) => {
        const tracks = config.timelines && (i === 1 && outcome === 'retry'
          ? [{name:'生成', cells:config.retry.generationCells}, {name:'训练', cells:config.retry.trainerCells}]
          : config.timelines[i]);
        const steps = config.timelines
          ? `<div class="framework-timeline" aria-label="${row.name}的生成与训练时间线">${tracks.map(track => `<div class="framework-track"><span class="framework-track-name">${track.name}</span><ol>${track.cells.map(([text,kind],step) => `<li class="work-${kind} ${step === index ? 'active' : step < index ? 'past' : 'future'}"${step === index ? ' aria-current="step"' : ''}><span>${text}</span></li>`).join('')}</ol></div>`).join('')}</div>`
          : `<ol>${row.nodes.map((text,step) => `<li class="${step === row.active ? 'active' : step < row.active ? 'past' : ''}"${step === row.active ? ' aria-current="step"' : ''}><span>${text}</span></li>`).join('')}</ol>`;
        return `<div class="framework-lane lane-${i}"><h3>${row.name}</h3>${steps}<p>${row.detail}</p></div>`;
      }).join('');
      q('[data-framework-takeaway]').textContent = current.takeaway;
      q('[data-framework-boundary]').textContent = config.boundary;
      q('[data-framework-progress]').textContent = `${index+1} / ${config.frames.length}`;
      button('back').disabled = index === 0;
      button('next').disabled = index === config.frames.length-1;
      root.querySelectorAll('[data-framework-tab]').forEach(el => {
        const selected = el.dataset.frameworkTab === scene;
        el.setAttribute('aria-selected', String(selected)); el.tabIndex = selected ? 0 : -1;
      });
      q('[role="tabpanel"]').setAttribute('aria-labelledby', `framework-tab-${scene}`);
    };
    const stop = () => {
      clearInterval(timer); timer = null;
      button('play').innerHTML = icons.play;
      button('play').setAttribute('aria-label', '播放'); button('play').title = '播放';
    };
    const select = key => { stop(); scene = key; index = 0; render(); };
    root.querySelectorAll('[data-framework-tab]').forEach(el => {
      el.onclick = () => select(el.dataset.frameworkTab);
      el.onkeydown = event => {
        if (!['ArrowLeft','ArrowRight','Home','End'].includes(event.key)) return;
        event.preventDefault(); event.stopPropagation();
        const keys = Object.keys(frameworkScenes), current = keys.indexOf(scene);
        const next = event.key === 'Home' ? 0 : event.key === 'End' ? keys.length-1 : (current + (event.key === 'ArrowRight' ? 1 : -1) + keys.length) % keys.length;
        select(keys[next]); q(`[data-framework-tab="${keys[next]}"]`).focus();
      };
    });
    button('back').onclick = () => { stop(); index = Math.max(0,index-1); render(); };
    button('next').onclick = () => { stop(); index = Math.min(frameworkScenes[scene].frames.length-1,index+1); render(); };
    button('reset').onclick = () => { stop(); index = 0; render(); };
    button('play').onclick = () => {
      if (timer) { stop(); return; }
      if (index === frameworkScenes[scene].frames.length-1) { index = 0; render(); }
      button('play').innerHTML = icons.pause;
      button('play').setAttribute('aria-label','暂停'); button('play').title = '暂停';
      timer = setInterval(() => {
        index++; render();
        if (index === frameworkScenes[scene].frames.length-1) stop();
      }, Number(q('[data-framework-speed]').value));
    };
    q('[data-framework-speed]').onchange = stop;
    q('[data-framework-outcome]').onchange = event => { stop(); outcome = event.target.value; render(); };
    document.addEventListener('slidechange', stop);
    document.addEventListener('visibilitychange', () => { if (document.hidden) stop(); });
    render();
  });
}
