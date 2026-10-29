# root尾五最小逐字稿

必要Source/date复用ROOT_REVIEW R13。04038为中心争议，不拟Books。

## 04375 / Ch78

锚点：typed data path及Schema/semantic validation完整段后、安全评价call admission段前。

逐字正文：

同一调用跨 adapter、renderer 与 shell 时，还须比较 receiver 真正解析出的动作，而非两侧字符串是否相等。可沿每个 hop 用接收方自己的 parser 产生 executable、ordered argv、control flow、cwd／env／stdin 的非执行 witness，定位 first divergence，再仅修该命名 hop、固定 reply 重演以检验归因。[IntAct 的受限路径审计](https://arxiv.org/html/2610.04375v1)保的是 emitted tool contract，不证明用户目标正确、witness已经执行或后续 hops 全部无错；首个坏 hop 还能遮蔽后续缺陷。有限注入中只有部分实际改变动作，拒绝也不等恢复原动作，原始提案错误与域外 rendering 仍在。逐hop解析、witness、重演与独立 effect 验收均计费；parser或语义映射不受支持时保留原始记录、显式失败及经验证的窄 typed path，不让自动修复替代 authorization、真实执行回执或完整路径正确性。<!-- source-family:SF-2026-ARXIV-2610-04375 -->

逐字本人注：

- `SF-2026-ARXIV-2610-04375` — [exact-v1](https://arxiv.org/html/2610.04375v1)，Daily2026-10-07/Oct6窗，2+2+2=6；root R13必要§2–4/6、日期与失效归因深入；literal PRE/实际POST另记，未核实现或复现。

## 03980 / Ch24

锚点：prompt-free instance unlearning完整两段及2603-10445 marker后、概念key-step修订段前。

逐字正文：

视频概念修订还须按 frame 与 denoising time 检查重新显现，而不让 clip 平均残留替最差帧签字。一条[受限选择性遗忘分支](https://arxiv.org/html/2610.03980v1)联合闭式 K／V 编辑与逐 concept 的 FFN LoRA，以 frame／timestep gate 控制干预、固定 prompt 软路由选专家；hard negatives约束其他概念，不构成开放恢复攻击的安全证书。去 frame gate 的平均残留可更低而 peak-gap／FVD 更差，单 LoRA 合训也可残留更低却严重损伤视频质量，因此删除代理与选择性保持须分账。新增 concept 要重做闭式编辑，旧 hard negatives 也会失配；长于81帧、AR生成及专门攻击 router／gate 未验。训练随 concept 数增加，路由、全部生成／安全／保留评价均计费；误激活、质量或局部恢复未过时保留原模型、较温和修订与独立输出过滤，不由平均低残留宣称完全删除。<!-- source-family:SF-2026-ARXIV-2610-03980 -->

逐字本人注：

- `SF-2026-ARXIV-2610-03980` — [exact-v1](https://arxiv.org/html/2610.03980v1)，Daily2026-10-07/Oct6窗，2+2+2=6；root R13必要§3–5及日期，安全域深入；只v1不借Oct9 v2，literal PRE/实际POST另记，未核代码或复现。

## 04009 / Ch26

锚点：UniW(A)M接口/mask及部署router完整两段后、显式rollout/direct policy比较段前。

逐字正文：

共享 video／action 序列还可以用 disjoint token 集合共用 embedding／输出头，并独立采样各模态 mask 率；action-free video 的对应位置不计 action loss，跨 block 因果而 block 内双向，使训练任务由可见性与标签人口共同定义。[SUAVE 的受限分支](https://arxiv.org/html/2610.04009v1)仍有冻结 MAGViT-v2 视频 codec，不能称无 encoder；只缓存重复不变的 clean prefix，下一轮继续读取真实 camera，不把生成 goal 当新观测。主要收益来自 in-domain robot pretrain，人视频边际在实机上未统计可分，单训练 seed、固定长度／单7DoF与专用视频质量反侧限制外推。Codec、模态mask、全部预训练与动作生成均计费；标签、prefix identity或闭环质量失配时，保留专用 video／policy、显式条件与原 controller，不因统一词表或共享权重批准跨本体、安全或全任务优越。<!-- source-family:SF-2026-ARXIV-2610-04009 -->

逐字本人注：

- `SF-2026-ARXIV-2610-04009` — [exact-v1](https://arxiv.org/html/2610.04009v1)，Daily2026-10-07/Oct6窗，2+2+2=6；root R13必要§III–V及日期、in-domain／humanvideo ladder；literal PRE/实际POST另记，未核代码或复现。

## 04198 / Ch24

锚点：2604-08302软状态／结束条件完整两段后（其marker后）；原下一分支前。

逐字正文：

未提交位置的中间状态也可保留为跨内循环 hidden，而不每轮都回到 token embedding；已 commit 位置才恢复离散条件。Entropy 决定提交哪些 token，learned exit gate 决定未解位置还做多少 recurrent depth，是两个不同控制；max-depth 与最低熵 fallback 只保进展，不保正确。[ALoDLM 的受限分支](https://arxiv.org/html/2610.04198v1)将联合 schedule 写进条件 NELBO，但该推导不自动认证实际放松 KL、minibatch平均与中间 losses 精确无偏。质量主表逐步只提交一个 token，吞吐 frontier 却用并行协议，不能拼成同一工作点；高质量区局部优势也不抹去极快区较弱、prefill／TTFT使短答反转及baseline训练不同。循环 hidden、exit训练、全部重算与完整请求计费；质量、状态或净预算不合时保留固定深度、保守揭示和原模型，不由早停分数或更少平均depth自签正确性与SLO。<!-- source-family:SF-2026-ARXIV-2610-04198 -->

逐字本人注：

- `SF-2026-ARXIV-2610-04198` — [exact-v1](https://arxiv.org/html/2610.04198v1)，Daily2026-10-07/Oct6窗，2+2+2=6；root R13必要§3–5/Alg1及日期、串行质量/并行吞吐反侧；literal PRE/实际POST另记，未核实现或复现。

## 04391 / Ch26

锚点：Contact Feedback Loop开篇三段后、反应式反馈之外的预测表示段前。

逐字正文：

Commanded closure 到终点，还不等物体已获得支持。一条[受限执行监督分支](https://arxiv.org/html/2610.04391v1)只在该时点检查设备 motor-effort proxy，再暂停 body-reference 的推进、保持 stabilization，按 finger 提议修正；accept 保留 override，reject 释放 override 而不等主动张手。恢复时以 fresh observation 生成新 chunk并丢弃旧排队 chunk，rearm 还要求实际与命令均 reopen，避免把一次确认重复消费。75配对 blocks 支持相对原 policy／无条件 close-to-stall 的局部收益，另一100-block消融中 full 与无条件的成功差不显著，选择性 gate 主要减少干预，不能独占全部提升。Effort 不是标定力，三support不保稳定，soft物体漏检、retention误拒及VLM迟到默认nominal均限制安全解释。传感标定、监督调用、暂停与重新推理均计费；支持或上下文不足时保留经验证的低层controller／停机或人工接管，并在fresh observation下重新规划，不把命令完成、proxy或监督建议当物理安全授权。<!-- source-family:SF-2026-ARXIV-2610-04391 -->

逐字本人注：

- `SF-2026-ARXIV-2610-04391` — [exact-v1](https://arxiv.org/html/2610.04391v1)，Daily2026-10-07/Oct6窗，2+2+2=6；root R13必要§III–V及日期、gate／override／freshchunk与paired/ablation反侧；literal PRE/实际POST另记，未核代码或复现。
