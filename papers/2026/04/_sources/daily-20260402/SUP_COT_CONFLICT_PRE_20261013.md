# CoT reward conflict — TRAIN-RLHF 窄 PRE

`SF-2026-ARXIV-2603-30036`，`2+2+3=7`。root实际v1§3/4概念及完整§6/7必要评价、关键反侧通过 Source；正常公告复合日门/owned字段见本日三正常日证。未写Books，不自授PRE/POST。

## 唯一 owner 和实际差额

`TRAIN-RLHF` — `books/part-04-training-system/31-rlhf.md`。当前823–841区分reward source/verifier不完备、特权judge与counterfactual CoT simulator的行为预测增量；这并没有按 `R_out/R_cot` 对相同计算的透明表达是否兼容分类。原CoT simulator改变训练监督的定义，新材料则界定监督output/trace目标关系与训练后的monitorability，不重复已有“奖励可被hack”或Ch66评价harness。两段插原simulator收益/反側之后、skill-conditioned curriculum转场之前，保原论点及下游objective章节分工。

已读ROADMAP/项目/学习/写作/current2026LS规定上下文，Ch31intro及816–855、1120–1173实际局部/交接、Ch30与32intro（其handoff见下）；不跨写Ch66/32/33。无结构候选。

## OLD 完整锚

```markdown
[有限二元任务对照](https://arxiv.org/html/2602.20710v1#S5)显示cue条件下的simulatability改善，却在部分generic任务主要改善outcome一致性而非CoT增量；人工cue/拒绝样本人口与反向cue限制外推，作者未观察到cue-based与model-generated两类counterfactual之间的transfer，分别训练不授统一introspection。额外重写、simulation与训练均计费，任务准确率仍须独立验收；simulator共同偏差、增量不成立或质量下降时，回退原outcome verifier、人工/独立过程审计，不把可模拟性替正确性或causal faithfulness。

当 feedback 可以自动验证后，下一层瓶颈会从“怎样打分”转向“怎样持续生成既有学习价值、
```

## NEW 完整替换（只插两段）

```markdown
[有限二元任务对照](https://arxiv.org/html/2602.20710v1#S5)显示cue条件下的simulatability改善，却在部分generic任务主要改善outcome一致性而非CoT增量；人工cue/拒绝样本人口与反向cue限制外推，作者未观察到cue-based与model-generated两类counterfactual之间的transfer，分别训练不授统一introspection。额外重写、simulation与训练均计费，任务准确率仍须独立验收；simulator共同偏差、增量不成立或质量下降时，回退原outcome verifier、人工/独立过程审计，不把可模拟性替正确性或causal faithfulness。

同时优化输出与推理文本，还要先问两种奖励是否允许透明表达同一种计算。令 `R_out` 评价最终输出、`R_cot` 评价显式推理链：若获得较高输出奖励所需的相关计算，在如实写进 trace 后反被第二种奖励惩罚，两者存在冲突；若文本奖励不区分这项计算，则可正交；若它鼓励相同表达，才是相容分支。这是一份依赖具体 task、reward pair 与 monitor 的关系，不是所有 CoT 监督都促使隐藏，也不是从 reward 代码即可自动判定的标签。语言预训练偏向透明表达只是该解释的假设，不能当作实际内部计算已被完整观察。<!-- source-family:SF-2026-ARXIV-2603-30036 -->

[必要的训练对照](https://arxiv.org/html/2603.30036v1)将 monitorability 限为指定 LLM 能否从 CoT 分类指定任务特征：换 monitor 或特征，关系也可能变化。冲突设置有无法同时提高两reward的结果，正交设置仍可发生语义漂移，部分长度惩罚的低监控率只是空 trace；相容设置初始监控已完美，未实测主动提高监控率。CAPO、GRPO 与 in-context 优化的范围不同，reward sweep又选择联合reward最好的policy，不能据此给任意optimizer/长度惩罚的安全或危险保证。双reward评估、monitor调用、搜索预算与独立质量审计都要计费；文本可读但检测失败、奖励人口改变或结果冲突时，应保留单独的 outcome 验证与独立 trace/行为审计，不由奖励提高签发真实内部透明性。

当 feedback 可以自动验证后，下一层瓶颈会从“怎样打分”转向“怎样持续生成既有学习价值、
```

## 本人末注完整尾锚与拟追加

当前最后项原样保留：

```markdown
- `SF-2026-ARXIV-2603-24844` — [exact-v1](https://arxiv.org/html/2603.24844v1) §2–4/T1–2、§6、B/E必要范围；仅单response集合reward/去重与置信读出身份，保top1反退、setmetric人口、coverage口径/K增减和串行/训练全费边界，不授conformal/joint概率/clinical/SLO保证。未核artifact/复现。
```

其后只新增静态注：

```markdown
- `SF-2026-ARXIV-2603-30036` — Daily `2026-04-02`补`04-01`；[exact-v1](https://arxiv.org/html/2603.30036v1) §3–4 reward-pair概念、§6–7必要实测/直接反側，`2+2+3=7`。只采task/monitor条件下output/CoT奖励相容关系；transparentbias为假设，监控是文本分类非内部真值。sweep选最好、正交semanticdrift、长度空trace、aligned初始完美未主动提升等反側保留，不授一般lengthpenalty安全/危险、任意optimizer或部署透明保证。未核代码或复现。
```

申请仅Ch31上述两段与本人静态注窄锁，root实际PRE/授权前不写。写后本作者读完整邻接/注，再由root非writer actualPOST；不授DAY。

实际写入/独立POST：root已actualPRE读810–855局部后授权两段/本人注窄锁；作者实际apply_patch写843/845与本人1499静态注，顺读829–861完整simulator→pair→curriculum邻接和注，限定diff-check通过。root已实际nonwriter readback832–853完整新段/前后及本人注，限定相容分类不是内部truth/长度一般安全，POST通过、锁释放。未授本日DAY。
