export function softmax(values) {
  const weights = values.map(v => Math.exp(v - Math.max(...values)));
  const total = weights.reduce((a, b) => a + b, 0);
  return weights.map(v => v / total);
}

export function expectedStep(logits, rewards, rate) {
  const before = softmax(logits);
  const mean = before.reduce((s, p, i) => s + p * rewards[i], 0);
  const gradient = before.map((p, i) => p * (rewards[i] - mean));
  const updated = logits.map((z, i) => z + rate * gradient[i]);
  return { before, mean, gradient, updated, after: softmax(updated) };
}

export function sampledStep(logits, chosen, reward, rate) {
  const before = softmax(logits);
  const gradient = before.map((p, i) => reward * ((i === chosen ? 1 : 0) - p));
  const updated = logits.map((z, i) => z + rate * gradient[i]);
  return { before, gradient, updated, after: softmax(updated) };
}

export function groupStats(rewards) {
  const mean = rewards.reduce((a, b) => a + b, 0) / rewards.length;
  const std = Math.sqrt(rewards.reduce((s, r) => s + (r - mean) ** 2, 0) / rewards.length);
  return { mean, std, advantage: rewards.map(r => (r - mean) / (std + 1e-8)) };
}

export const groupCases = {
  mixed: { answerIds: [0, 1, 2, 3], rewards: [1, 1, 0, 0] },
  wrong: { answerIds: [0, 1, 2, 3], rewards: [1, 0, 0, 0] },
  'all-one': { answerIds: [0, 1, 0, 1], rewards: [1, 1, 1, 1] },
  'all-zero': { answerIds: [2, 3, 2, 3], rewards: [0, 0, 0, 0] },
};

export function clippedTerm(ratio, advantage, epsilon = 0.2) {
  return Math.min(ratio * advantage, Math.max(1 - epsilon, Math.min(1 + epsilon, ratio)) * advantage);
}

// These are teaching traces, not engine logs or model-generated trajectories.
const flows = {
  4: {
    caption: '同一道两步文字题的三种监督信息；主线不开放工具，也不是必须依次执行的三个阶段。',
    labels: ['示范', '偏好', '结果反馈', '两条反馈路线'],
    frames: [
      ['SFT：告诉模型“照着什么回答”', '输入：文字题 + 示范解法', ['原有 17 本，再新增 20 本和 5 本', '示范：17 + 20 + 5 = 42', '提高这条示范的概率'], '需要给出可模仿的回答；它不是“只告诉模型对不对”。'],
      ['Preference：告诉模型“哪条更好”', '输入：题目 + 一对回答 + 排序', ['A：42', '偏好 B 的清楚步骤', 'B：17 + 20 + 5 = 42'], 'A、B 都正确；清晰度偏好不是算术正确性标签。偏好对可用于训练评分器，也可进入 DPO。'],
      ['在线 RL：让模型尝试，再评价结果', '输入：模型本次采样的回答 + 反馈', ['生成：42', '最终答案验证：正确', '奖励 R = 1 → 构造更新'], '验证器只核对终局数字，不证明每一步可靠；梯度需要已采样回答的概率。'],
      ['反馈来源决定怎样评价，算法决定怎样更新', '人类偏好可以训练评分器，也可以直接用于偏好优化', ['偏好 → 评分器 → 在线 RL', '偏好 → DPO', '规则验证 → RLVR'], 'RLHF 强调人类反馈，RLVR 强调可验证奖励。PPO、GRPO 是更新方法，后面逐一展开。'],
    ],
  },
  5: {
    caption: '先用迷宫认识行动与反馈，再映射到生成。“4”“2”是自建教学 token，不是实际 tokenizer 的结果。',
    labels: ['迷宫直觉', '语言状态', '第一个 token', '第二个 token', '整条路径'],
    frames: [
      ['在路口选择方向，走完再收到反馈', '当前路口是状态；选择左或右是行动；选择概率是策略', ['观察所在位置', '选择下一步方向', '到达出口获得奖励'], '一次完整行走就是轨迹。这个简化迷宫只在终点给分，反馈没有告诉我们每一步应怎样走。'],
      ['状态是模型现在看见的前缀', '状态 s₁ = “17 本书，又新增 20 本和 5 本，共多少？”', ['题目 x', '还没有输出', '下一步从词表中选择'], 'Policy πθ 是参数 θ 定义的概率规则，不是某一个固定答案。'],
      ['采到“4”，前缀随之改变', '教学概率：P(“4” | 题目) = 0.6', ['题目 x', '行动 a₁ = “4”', '新状态：题目 + “4”'], '这里是人为选定的一条示意轨迹，其他 token 分到剩余 0.4 概率。'],
      ['在新的前缀下采到“2”', '教学概率：P(“2” | 题目,“4”) = 0.8', ['题目 + “4”', '行动 a₂ = “2”', '新状态：题目 + “42”'], '第二个概率依赖第一个 token；不是对两个独立事件相乘。'],
      ['整条路径的概率由条件概率相乘', 'P(“4”,“2” | 题目) = 0.6 × 0.8 = 0.48', ['log 0.6', '+ log 0.8', '= log 0.48'], 'log 是对数，把乘积变成和；log probability 不是外部评分。本例固定两步停止，真实生成还要处理 EOS。'],
    ],
  },
  10: {
    caption: '先区分旧基准、正在更新的策略与长期参考。本同步例中，旧策略也负责生成本批数据。',
    labels: ['生成 v7', '更新到 v8', '继续到 v9', '下一批数据'],
    frames: [
      ['先记录“这批回答从哪里来”', 'old = v7：本批旧基准；reference = v0：长期参考', ['v7 生成回答', '保存 old logprob', 'reference v0 保持冻结'], '本例 old 也负责生成数据。old 比较本批更新幅度，reference 比较离参考行为的偏离。'],
      ['参数变了，旧概率不随之改写', 'current = v8；old 仍是 v7；reference 仍是 v0', ['current / old', '比较本轮变化', 'current / reference：另一种比较'], '概率比约束如何使用这批旧样本；KL 参考项关注偏离原参考多少。'],
      ['同一批的后续更新仍用原 old', 'current = v9；old = v7；reference = v0', ['样本仍来自 v7', 'v9 重新计算概率', '不能把分母偷偷改成 v9'], '否则概率比会失去原本含义；异步或数值差异还需额外处理。'],
      ['新采样批次才建立新基准', '下一批由 v9 生成，old = v9；reference 仍为 v0', ['同步 v9 权重', '重新生成', '保存新批次 old logprob'], '实际生成数据的策略叫 behavior，本例与 old 一致；异步时可能不同。reference 是否更新也需明确定义。'],
    ],
  },
  12: {
    caption: 'PPO 的数据依赖示意；并行评分和 value 计算不一定按画面顺序串行执行。',
    labels: ['Actor', 'Reward / Critic', 'Advantage', '更新'],
    frames: [
      ['Actor 负责尝试', '输入题目 → 生成回答与行动 token', ['题目', 'Actor：42', '保存回答和旧概率'], 'Actor 是要改进的生成策略，不负责证明自己的答案正确。'],
      ['两个“分数”，回答两个问题', 'Reward：实际得分；Critic：预期回报', ['验证器：实际 R = 1', 'Critic：预期 V = 0.6', '两者不是同一个评分器'], '本例只有终局奖励，折扣为 1，因此从该状态的 return 为 1。'],
      ['比较实际结果与预期', '简化优势 A = return − V = 1 − 0.6 = 0.4', ['好于预期 +0.4', 'old 概率 → 概率比', 'reference 概率 → KL 参考'], '这里用 Monte Carlo 例子解释优势；完整 token-level PPO 常使用 GAE。'],
      ['Actor 和 Critic 学不同目标', 'Actor 学行为；Critic 学预测回报', ['Actor：策略损失 → backward', 'Critic：回报误差 → backward', '冻结的 reference 不更新'], '下一轮再生成并评价，不是只对同一条回答无限重复训练。'],
    ],
  },
  15: {
    caption: '换一种数据条件：已有偏好对，不是 GRPO 的下一版本。A、B 都正确，本次偏好展示算式的 B。',
    labels: ['偏好数据', '当前与参考', '偏好差距', '训练目标'],
    frames: [
      ['先有比较标签，不必当场生成', 'x = 题目；y+ = B；y− = A', ['同一道题', 'chosen：17 + 20 + 5 = 42', 'rejected：42'], '偏好对已事先准备；本轮不再先采四条回答逐条打分。rejected 是相对不偏好，不代表答错。'],
      ['当前模型和 reference 都给这对答案算概率', '教学设置：p(B)=0.4，p(A)=0.1；参考均为 0.25', ['B：当前 / 参考 = 1.6', 'A：当前 / 参考 = 0.4', '两条都进入比较'], '先看流程：读偏好对、算概率、构造损失、更新模型。数值是假设状态，不是实际 DPO 训练结果。'],
      ['相对参考，现在更偏向哪一条？', '当前 B:A = 4:1；参考 B:A = 1:1', ['参考：A、B 同样可能', '当前：更偏向 B', '符合这对偏好的方向'], '比较的是两条回答的相对倾向；chosen 的绝对概率并不保证每步单调增加。'],
      ['用偏好差距构造训练目标', '更符合这对排序 → 偏好损失更小 → 计算梯度', ['两条回答都参与', '参考模型用于校正', '优化器更新共享参数'], 'loss 是训练要减小的数值目标。它下降说明更满足这对偏好，不代表未见任务一定更好；完整公式可展开查看。'],
    ],
  },
  22: {
    caption: '把迷宫映射为语言 Agent 的工具交互；这是流程示意，未运行 LLM。mask=1 进入策略 loss，mask=0 只作上下文。',
    labels: ['用户问题', '模型行动', '环境观察', '再次行动', '终局反馈'],
    frames: [
      ['用户输入不是模型行动', '用户：从起点走到出口', ['来源：用户', '地图进入上下文', 'action mask = 0'], 'Attention 可读取这些 token，但训练不把它们当作模型选择的行动。'],
      ['模型选择调用工具', '模型：move(right)', ['来源：策略', '记录调用 token 概率', 'action mask = 1'], '工具执行所选方向，不负责替模型规划正确路线。'],
      ['工具返回结果', '环境：位置 (2,1)，尚未到达', ['来源：环境', '加入下一轮上下文', 'action mask = 0'], '不能因为坐标出现在对话里，就假装是策略生成的 token。'],
      ['模型依据新观察继续行动', '模型：再次 move(right)', ['来源：策略', '状态含环境观察', 'action mask = 1'], '继续到出口可能还需多次行动；这里只展开前两次，整段轨迹共同接受反馈。'],
      ['成功奖励属于整个任务', '走到出口后：获得成功奖励', ['行动 token：训练', '环境观察 token：不训练', '累计回报：构造优势'], '到达不意味着每一步都必要；如何把整体结果分配给行动，仍是信用分配问题。'],
    ],
  },
  23: {
    caption: '一轮同步 GRPO 的数据交接示意，不代表具体框架必须串行运行所有阶段。',
    labels: ['生成', '评分', '整理', '更新', '同步', '下一轮'],
    frames: [
      ['用策略 v7 生成八条不同长度的回答', 'vLLM / SGLang 加速尝试，不执行本轮梯度更新', ['短回答退出', '空槽接入新请求', 'KV 随序列增长'], '连续批处理减少空等；分页 KV 降低预留浪费。这里仍是在生成训练数据。'],
      ['奖励绑定具体轨迹', '回答 → 验证器 → 每条一个 reward', ['轨迹 ID', '奖励值', '评分器版本'], '不能只保存一个 batch 平均分，否则丢失各个行动的反馈。'],
      ['整理训练所需的关系', 'token + mask + group_id + old logprob → advantage', ['同题回答成组', '过滤非行动位置', '保留行为版本 v7'], '长度相同不代表语义对齐，分组和 mask 都会影响更新。'],
      ['训练端产生 v8', '前向 → loss → backward → optimizer', ['rollout 仍是 v7', 'trainer 已是 v8', '生成不会自动切换参数'], '两个引擎的参数状态可能暂时不同，这是实际交接问题。'],
      ['把新权重交给生成端', '建立交接窗口 → 传输 / 加载 → 确认 v8', ['处理在途请求', '处理旧 KV 状态', '恢复新版本生成'], '同步策略参数，不是把 Critic 合并给 Actor；异步旧轨迹还要单独检查。'],
      ['新策略生成新数据', 'v8 再次生成回答，再次获得反馈', ['更改的参数', '新的回答分布', '新的训练样本'], '在线 RL 的数据分布会随模型变化，闭环在这里真正形成。'],
    ],
  },
};

const demoIds = new Set([4, 5, 6, 8, 10, 11, 12, 13, 14, 15, 20, 22, 23]);
export function hasLesson(id) { return demoIds.has(id); }

export function lessonMarkup(id, icons) {
  const ppo = id === 11;
  const labels = flows[id]?.labels ?? (id === 6 ? ['生成', '评分', '算概率', '梯度', '更新', '新分布'] : id === 8 ? ['起点', '奖励', '平均', '梯度', '更新', '新分布'] : id === 13 ? ['奖励', '均值', '差值', '优势', '策略目标', '更新'] : id === 14 ? ['奖励', '均值', '差值', '标准化'] : id === 20 ? ['0 步', '1 步', '10 步', '50 步', '200 步'] : []);
  let settings = '';
  if ([13, 14].includes(id)) settings = '<label>奖励组 <select data-case><option value="mixed">两对两错</option><option value="wrong">B 被错误判零</option><option value="all-one">全部得 1 分</option><option value="all-zero">全部得 0 分</option></select></label>';
  if (ppo) settings = '<label>优势 A <select data-sign><option value="1">+1：好于预期</option><option value="-1">−1：差于预期</option></select></label><label class="ratio-control">概率比 ρ <input data-ratio type="range" min="0.4" max="1.6" step="0.01" value="1.5" aria-label="概率比"><output data-ratio-value>1.50</output></label>';
  return `<div class="lesson" data-lesson="${id}">
    <p class="lesson-caption">${flows[id]?.caption ?? (id === 6 ? '本页把参数简化为四个分数 z；softmax 把分数转换成总和为一的概率。追踪一次抽到 A、得一分的更新。' : id === 8 ? '完整枚举四个回答，计算平均更新方向；与单个样本的更新不同。' : [13, 14].includes(id) ? '同题四次采样，允许重复回答。总体标准差，分母加 10⁻⁸；误判案例单独标注。' : ppo ? 'ρ = 当前概率 ÷ 旧概率；旧概率固定为 0.25，裁剪范围参数 ε = 0.2。' : '回放 CPU 实验的五个实测记录点；过渡动画不是额外测量值。')}</p>
    ${labels.length ? `<ol class="lesson-steps">${labels.map((label, i) => `<li><span>${i + 1}</span>${label}</li>`).join('')}</ol>` : ''}
    <div class="lesson-settings">${settings}</div>
    <div class="lesson-visual"></div><div class="lesson-explanation" aria-live="polite"></div>
    ${!ppo ? `<div class="lesson-controls"><button data-action="back" aria-label="上一步" title="上一步">${icons.back}</button><button data-action="play" aria-label="播放动画" title="播放动画"><span data-play>${icons.play}</span><span data-pause hidden>${icons.pause}</span></button><button data-action="next" aria-label="下一步" title="下一步">${icons.next}</button><button data-action="reset" aria-label="重新开始" title="重新开始">${icons.reset}</button><output data-position></output></div>` : ''}
  </div>`;
}

const number = (n) => (Math.abs(n) < 0.00005 ? 0 : n).toFixed(4);
const signed = (n) => `${n > 0 ? '+' : ''}${number(n)}`;
const vector = (v) => `[${v.map(signed).join(', ')}]`;
const percent = (n) => `${(n * 100).toFixed(2)}%`;

function policyFrame(root, step, sampled) {
  const data = sampled ? sampledStep([0, 0, 0, 0], 0, 1, 0.2) : expectedStep([0, 0, 0, 0], [1, 1, 0, 0], 0.2);
  const visual = root.querySelector('.lesson-visual');
  if (!visual.children.length) visual.innerHTML = `<div class="probability-head"><span>路线</span><span>初始概率（灰） / 当前显示（彩色） · 横轴 0～100%</span><span>概率</span></div>${['A · 绕路到达', 'B · 短路到达', 'C · 绕圈超时', 'D · 未到出口'].map((name, i) => `<div class="probability-row"><strong>${name}</strong><div class="probability-track"><i class="old-bar" style="width:25%"></i><i class="new-bar ${i >= 2 ? 'wrong' : ''}" style="width:25%"></i></div><output>25.00%</output></div>`).join('')}<div class="calculation"></div>`;
  root.querySelectorAll('.probability-row').forEach((row, i) => {
    const p = step === 5 ? data.after[i] : data.before[i];
    row.classList.toggle('selected', sampled && step > 0 && i === 0);
    row.querySelector('.new-bar').style.width = `${p * 100}%`;
    row.querySelector('output').textContent = percent(p);
  });
  const sampleText = [
    ['先看行动之前的分布', '四条固定路线各 25%；本例追踪抽到 A：绕路到达。把整条路线压缩成一次选择，便于手算。'],
    ['验证器给 A 打分：R = 1', '评分是外部事实，此时参数没变。正确不等于已经完成了学习。'],
    ['真实模型：log πθ(y|x) = Σₜ log πθ(aₜ|sₜ)；本页 log p(A) ≈ −1.3863', '固定已经采到的 token，重新前向算概率，不再采一条新回答。累加 log 概率并用奖励加权后，才对参数求梯度。'],
    ['梯度 g = R × ∇log p(A) = [0.75, −0.25, −0.25, −0.25]', '训练程序沿模型概率求导，不对评分器求导。∇ 表示对分数求变化方向：A 为 1−0.25，其余为 0−0.25，再乘奖励。'],
    [`新分数 z′ = z + 0.2 × g = ${vector(data.updated)}`, 'z 是 softmax 前的可学习分数；0.2 是学习率。本例做梯度上升，常见代码则最小化负目标。'],
    [`softmax 后：A 从 25.00% → ${percent(data.after[0])}`, '一次样本提高了 A，也压低了未抽中的 B，即使 B 也正确。多次采样用于估计平均方向，完整推导见附录 A。'],
  ];
  const expectedText = [
    ['起点：四个分数 z 都是 0 → 四个概率都是 25%', '把每条完整回答当作一个动作；不是实际 LLM 的独立知识槽位。'],
    ['逐个评分：A=1，B=1，C=0，D=0', '现在枚举四个结果，不是在一次采样中同时抽到四条。'],
    ['平均奖励 J = 0.25×1 + 0.25×1 + 0.25×0 + 0.25×0 = 0.5', 'J 是按出现概率加权的平均分；不是简单挑出最高奖励。'],
    ['每个分数的梯度 gⱼ = pⱼ × (Rⱼ−J)', 'A：0.25×(1−0.5)=+0.125；C：0.25×(0−0.5)=−0.125。B 与 A 同向，D 与 C 同向。'],
    [`z′ = z + 0.2 × g = ${vector(data.updated)}`, '这次梯度来自所有回答的期望；A、B 同时提高。η=0.2 只控制本次迈多大一步。'],
    [`正确概率 p(A)+p(B)：50.00% → ${percent(data.after[0] + data.after[1])}`, 'softmax 重新把分数换成总和为 1 的概率。单步变化很小，不等于一次就学会全部任务。'],
  ];
  const [formula, meaning] = (sampled ? sampleText : expectedText)[step];
  root.querySelector('.calculation').textContent = formula;
  root.querySelector('.lesson-explanation').textContent = meaning;
}

function groupFrame(root, step) {
  const choice = root.querySelector('[data-case]').value;
  const { answerIds, rewards } = groupCases[choice];
  const stats = groupStats(rewards);
  const calculation = [
    '先保留每次采样的回答与奖励。全对组采到 A/B，全错组采到 C/D。',
    `μ = 四个奖励的平均值 = ${number(stats.mean)}`,
    'R − μ：每条回答比本组平均结果好多少？',
    `A = (R − μ) / (σ + 10⁻⁸)，σ = ${number(stats.std)}（奖励的分散程度）`,
    '每个行动 token：当前概率 ÷ 旧概率 = ρ；用组优势 A 加权，并沿用 PPO 的裁剪项。',
    '汇总行动 token 的目标与参考约束，反向传播更新共享参数，再用新策略生成下一组。',
  ][step];
  root.querySelector('.lesson-visual').innerHTML = `<table class="group-table"><thead><tr><th>路线</th><th>奖励 R</th><th>减去均值 μ</th><th>优势 A</th></tr></thead><tbody>${rewards.map((r, i) => `<tr><th>${['A · 绕路到达', 'B · 短路到达', 'C · 绕圈超时', 'D · 未到出口'][answerIds[i]]}</th><td>${r}${choice === 'wrong' && i === 1 ? '（误判）' : ''}</td><td>${step >= 2 ? signed(r - stats.mean) : '—'}</td><td class="${stats.advantage[i] < 0 ? 'negative' : 'positive'}">${step >= 3 ? signed(stats.advantage[i]) : '—'}</td></tr>`).join('')}</tbody></table><div class="calculation">${calculation}</div>`;
  root.querySelector('.lesson-explanation').textContent = step === 5 ? '同一回答的 token 可以共享序列优势，但它们的概率梯度不同。算出优势还未更新参数。' : step === 4 ? '优势来源从 critic 改成同题比较；概率比、裁剪与参考约束仍各有职责，完整目标见静态公式。' : step === 3 ? stats.std === 0 ? '组内没有差异，所以这组任务奖励的相对优势为零；不代表其他损失或优化器状态也不更新。' : choice === 'wrong' ? '只错判 B，也改变了整个组的均值和优势。修正奖励后应重算整组，而不只是替换一个数字。' : '正优势提供提高相应行为倾向的信号，负优势相反；下一步把它放入策略目标。' : '同一道题的回答互相比较，不需要另训一个 critic；完整 GRPO 不只有这一步。';
}

function ppoFrame(root) {
  const ratio = Number(root.querySelector('[data-ratio]').value);
  const advantage = Number(root.querySelector('[data-sign]').value);
  const x = r => (r - .4) / 1.2 * 600;
  const y = v => 120 - v * 68;
  const points = Array.from({length: 121}, (_, i) => .4 + i * .01);
  const raw = points.map(r => `${x(r)},${y(r * advantage)}`).join(' ');
  const clipped = points.map(r => `${x(r)},${y(clippedTerm(r, advantage))}`).join(' ');
  const result = clippedTerm(ratio, advantage);
  root.querySelector('[data-ratio-value]').textContent = ratio.toFixed(2);
  root.querySelector('.lesson-visual').innerHTML = `<div class="plot-labels"><span>纵轴：目标项（越高越好）</span><span>横轴：概率比 ρ</span></div><div class="ppo-chart" role="img" aria-label="概率比与最大化目标的曲线；虚线未裁剪，实线为PPO目标"><div class="axis-y"><span style="top:${y(1)/2.4}%">+1</span><span style="top:50%">0</span><span style="top:${y(-1)/2.4}%">−1</span></div><div class="plot-area"><svg viewBox="0 0 600 240" preserveAspectRatio="none" aria-hidden="true"><rect x="${x(.8)}" y="0" width="${x(1.2)-x(.8)}" height="240" fill="#edf4f0"/><line x1="0" y1="120" x2="600" y2="120" stroke="#8b9790"/><polyline points="${raw}" fill="none" stroke="#bc7d28" stroke-width="2" stroke-dasharray="7 5" vector-effect="non-scaling-stroke"/><polyline points="${clipped}" fill="none" stroke="#167350" stroke-width="3" vector-effect="non-scaling-stroke"/></svg><i class="plot-marker" style="left:${x(ratio)/6}%;top:${y(result)/2.4}%"></i><div class="axis-x">${[.4,.8,1,1.2,1.6].map(r=>`<span style="left:${x(r)/6}%">${r}</span>`).join('')}</div></div></div><div class="plot-legend"><span>虚线：ρ × A</span><span>实线：PPO 的 min 结果</span><span>浅色区：0.8～1.2</span></div><div class="calculation">当前概率 = 0.25 × ${ratio.toFixed(2)} = ${(ratio * .25).toFixed(3)}；目标项 = ${result.toFixed(2)}</div>`;
  root.querySelector('.lesson-explanation').textContent = advantage > 0 ? 'A=+1：好于预期。当概率比超过 1.2，继续提高它不再增加这一项的收益；概率本身没有被锁住。' : 'A=−1：差于预期。当概率比低于 0.8，继续降低它不再增加这一项的收益；右侧仍会惩罚概率上升。';
}

function curveFrame(root, step, results) {
  const good = results.correct_reward_exact[step], wrong = results.wrong_reward_exact[step];
  const items = [['正确奖励 · 训练平均分',good.reward],['正确奖励 · 真正答对概率',good.true_success],['错误奖励 · 训练平均分',wrong.reward],['错误奖励 · 真正答对概率',wrong.true_success]];
  const visual = root.querySelector('.lesson-visual');
  if (!visual.children.length) visual.innerHTML = items.map(([label], i) => `<div class="metric-row"><label>${label}</label><div class="metric-track"><i class="${i >= 2 ? 'wrong' : ''}"></i></div><output></output></div>`).join('') + '<div class="calculation"></div>';
  visual.querySelectorAll('.metric-row').forEach((row, i) => { row.querySelector('i').style.width = `${items[i][1] * 100}%`; row.querySelector('output').textContent = number(items[i][1]); });
  visual.querySelector('.calculation').textContent = `训练第 ${good.step} 步 · 固定四路线 policy · 学习率 0.2 · 两组只改变奖励定义`;
  root.querySelector('.lesson-explanation').textContent = '四路线抽象的实测数值，非逐格迷宫实验：上两行奖励到达出口；下两行只奖励绕圈超时的 C，奖励与真实成功背离。';
}

export function mountLessons(results) {
  document.querySelectorAll('[data-lesson]').forEach(root => {
    const id = Number(root.dataset.lesson);
    let step = 0, timer = null;
    const count = root.querySelectorAll('.lesson-steps li').length;
    const play = root.querySelector('[data-action="play"]');
    function stop() {
      clearInterval(timer); timer = null;
      if (play) { play.querySelector('[data-play]').hidden = false; play.querySelector('[data-pause]').hidden = true; play.setAttribute('aria-label', '播放动画'); play.title = '播放动画'; }
    }
    function draw() {
      root.dataset.step = String(step);
      root.querySelectorAll('.lesson-steps li').forEach((node, i) => { node.classList.toggle('active', i === step); node.classList.toggle('done', i < step); });
      if (flows[id]) {
        const [heading, state, trace, meaning] = flows[id].frames[step];
        root.querySelector('.lesson-visual').innerHTML = `<h2>${heading}</h2><div class="flow-state">${state}</div><div class="trace-row">${trace.map((part, i) => `<div class="trace-node"><span>${i+1}</span>${part}</div>`).join('')}</div>`;
        root.querySelector('.lesson-explanation').textContent = meaning;
      } else if ([6,8].includes(id)) policyFrame(root, step, id === 6);
      else if ([13,14].includes(id)) groupFrame(root, step);
      else if (id === 11) ppoFrame(root);
      else if (id === 20) curveFrame(root, step, results);
      if (play) {
        root.querySelector('[data-position]').textContent = `${step+1} / ${count}`;
        root.querySelector('[data-action="back"]').disabled = step === 0;
        root.querySelector('[data-action="next"]').disabled = step === count-1;
      }
    }
    root.querySelectorAll('[data-action]').forEach(button => button.addEventListener('click', () => {
      const action = button.dataset.action;
      if (action === 'play') {
        if (timer) { stop(); return; }
        if (step === count-1) { step = 0; draw(); }
        play.querySelector('[data-play]').hidden = true; play.querySelector('[data-pause]').hidden = false; play.setAttribute('aria-label', '暂停动画'); play.title = '暂停动画';
        timer = setInterval(() => { step++; draw(); if (step === count-1) stop(); }, 2600);
      } else { stop(); step = action === 'reset' ? 0 : Math.max(0, Math.min(count-1, step + (action === 'next' ? 1 : -1))); draw(); }
    }));
    root.querySelectorAll('select,input').forEach(input => input.addEventListener('input', () => { stop(); draw(); }));
    document.addEventListener('slidechange', stop);
    document.addEventListener('visibilitychange', () => { if (document.hidden) stop(); });
    if (id === 14) { root.querySelector('[data-case]').value = 'all-one'; step = 3; }
    draw();
  });
}
