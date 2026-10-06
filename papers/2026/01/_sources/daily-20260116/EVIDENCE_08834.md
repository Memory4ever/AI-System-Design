# 2601.08834v1 — 格式分解奖励的局部增量

[精确 HTML](https://arxiv.org/html/2601.08834v1)，实际§3.2、§4主要评价/Tables3–6与§6.2配置。2+1+2=5；单组件文档解析的奖励表示/筛选替代，不把成熟GRPO或通用reward设计原则另算增量。root实际必要原源与Ch31现owner写前通过；typed matching/eligible denominator缺口深入受影响证据，两段已写Ch31多目标聚合末、Gradient-space前。root实际Ch31:224–239两段/前后衔接及末注非作者POST通过，窄锁释放；整合。日级Gate未授。

GT/pred通过regex拆text/formula/table；普通文字NEd，formula转LaTeX后BLEU，table TEDS；总奖励只平均GT非空类别。所谓expression correctness实际BLEU不验证数学等价或可执行正确性。Eq1所谓entropy是采样输出token均值负对数概率，即surprisal/NLL，不是全词表Shannon熵。16k格式密集数据保留最高50%=8k；比例消融仅一epoch，筛选比例变化可能改变token/update预算，没有matched-budget控制，不能归因真实模型uncertainty。

Qwen3-VL-4B：SFT冻结vision与MLP、LLM full tune，16GPU BF16 seq8192 batch1 lr1e-5 cosine10%warmup 1epoch；RL GRPO/EasyR1/verl G8 temperature1 response10240 rollout/train batch32 lr1e-6 WD1e-2 BF16 all params unfrozen，无KL，8GPU约10hrs，GPU型号NotDisclosed。OmniDocBench1355pages/9类/2语言；overall=Text(100×1-Edit)、FormulaCDM、TableTEDS均值，不与单项accuracy混合。seed/repeats/置信区间NotDisclosed。

Table5过滤0/25/50/75% overall88.47/89.53/90.41/88.58，支持局部非单调筛选取舍，不授50%普遍最优。Table6统一string-match88.64→拆格式string-match89.61→加formulaBLEU89.80→加TEDS90.41，text error并未单调改善；支持在同模型任务下对表示/结构评分分工的局部验证。Table3多源/SFT/RL联合提高不能全归因本奖励。采纳仅局部reward分解与不同比例取舍，未证明形式有效性、跨任务泛化或预算受控加速。
