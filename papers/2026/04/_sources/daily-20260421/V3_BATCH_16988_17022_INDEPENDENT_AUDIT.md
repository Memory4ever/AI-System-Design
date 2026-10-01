# Apr21 五项有限非作者必要复核

审阅人：weekly39_discovery（本批作者为 apr01，本人未参与本批来源/候选作者工作）；执行日2026-09-27。实际完整读取作者 `V3_BATCH_16988_17022.md`，独立重开下列官方exact-v1必要原文，并对读现有owner正文。结论只对五个具名采用边界有效；不审17009/17022，不增加全日题摘/全文数、不冻结日期/分母、不签日级Gate、不写Books，也不将作者摘要当原文。

## 16988：标准 Only 通过

实际读[HTMLv1](https://arxiv.org/html/2604.16988v1) §2.1–2.2构造/定理/Remark1/Corollary2、§3.1–3.2全部必要设置和对照、§5限制。prefix统计、按候选split做segment subtraction及posterior averaging是具体构造，满足基础模型机制准入，不能因后续应用于疾病/金融关闭。定理条件为单变点、线性模型、有界输入/标签、Gaussian prior/noise；未知候选可能需O(t) heads，已知split缩为O(1)，定理是BMA近似而非通用变点恢复。存在权重不保证GD找到。30步/5,000轨迹及训练10–20隐含支持已对齐；anticorrelated regime对照保留旧样本作为prior，直接反对“变化后总丢旧context”的泛化。

2+1+2=5合理。当前Ch5「表示为何会随上下文改变」L263–277已承载context可供任务身份或统计估计、生成过程/查询分布决定解释与容量/训练动力学边界；该论文的精确Bayesian构造未在书稿，不伪称Existing。其受限信息—资源案例可Only，不要求为局部构造新增普律。硬件/precision、总成本无完整采用依据，未复现，不外推现代LLM/真实连续控制。

## 17010：标准 Only 通过

实际读[HTMLv1](https://arxiv.org/html/2604.17010v1) §3.1–3.4、§4、§5.3–5.4及§8。SEQ先验证LiquidHaskell proof；SINQ须实际执行divergent input，生成标签先验收再交Bob学习。实施是rejection-sampling SFT而非RL。E2/E3约150pair仅控制验证后数据量，不控制全生成/验证compute；SEQ低proof yield确实改变训练buffer，限制反射/PLE/终止片段。CodeXGLUE Table5的recall与F1负结果实际核过，不把局部语言迁移提升扩为任意代码安全保证。

2+1+2=5及Only通过。Ch31 L633–695已有task proposer/validator/solver分权、可靠验证与task diversity共存及监督噪声—rollout成本；新增的是受限proof与execution两类监督的具体实现对照，不是证明生成者或judge自动可信，也不冒称该recipe已Existing。原文没有完整硬件/总预算/precision/SLO采用信息，实验未复现。

## 17019：标准 Only 通过

实际读[HTMLv1](https://arxiv.org/html/2604.17019v1) §3、§4.1–4.4（含Table5/语言移除/视觉instruction predictor/attention诊断）和§7。20离散任务、每任务50训练/10评价；width先依赖symbolic features/optimal plan，再由阶段一相关性选择用于分组，不是生产在线真值。粗粒度成功率反弹与语言必要性变弱可同时发生；Table5 width≥4仅3任务、多配置全0，不能隐去slice覆盖。合并label概率恒等式不独立证明每个视觉输入的最大certainty更高；attention仅补充诊断，原文也声明不是唯一机制解释。

2+1+2=5及Only通过。实际对读Ch26 L159–168直接融合允许视觉捷径及带条件的interface/representation边界；论文提供controlled granularity的局部替代解释与训练配比，不要求新增全具身U形法则，也不声称精确width配方现书已有。离散symbolic动作不等连续真机吞吐，原文相关硬件/precision/并发/SLO不充分，未复现。

## 17000：安全深入 Only 通过

实际读[HTMLv1](https://arxiv.org/html/2604.17000v1) III-B/C、IV-A/B、V-A/B、VI的TableIII/V/VI/VII及相邻论证。声纹embedding匿名化与ASR→NER→对齐→生成替换是不同对象；四类NER与仅PII utterance的C-ASV限制明确。utility实际是在匿名化训练集重训ASR/TTS/SER、原测试集验收，不能以现成ASR打分代替。负speaker weight提高ignorant EER，但知规则的lazy-informed EER下降；随机化亦非不可逆或DP证明。五seed只重复inference，不是五次独立retraining。

8×3090/500k steps/180M、192维anonymizer与5,000epochs、单3090 batch1/16步RTF操作点均可定位。2+1+2=5、安全反证深入及Only通过。当前Ch72 L155–189已定义detector/rewrite/utility的policy-bound sensor、attacker/task/distribution/threshold身份和非DP边界；此实现是受限语音案例，不升级平台匿名化保证。TableV级联ASR误差和语言style残留保留，未复现、未补造precision/并发/生产SLO。

## 16995：仅负KL×minimize窄争议通过

独立重开[HTMLv1](https://arxiv.org/html/2604.16995v1) §4.1 Eq4及AppC.1 Algorithm1；再读[官方PDFv1](https://arxiv.org/pdf/2604.16995v1)对应文本。两入口同为负forward KL loss，算法明确minimize。固定经验q=(1,0)、p=(a,1−a)，负KL=log(a)，最小化将a推向0，与匹配q相反。这是目标符号/方向的内部冲突，不仅HTML转换孤例；不证明公开代码照此执行或整体经验全部无效，不扩读完整代码/证明附录。该窄目标正面采用应继续暂缓，恢复条件为目标符号或优化方向的可靠澄清及实际采用目标的必要实现说明。

定位校准：本轮web PDF文本把Eq4标为零基P4、Alg1标为零基P14，即物理PDF第5/15页。作者原“p4/p14”需明确是零基页索引，或改为第5/15页，避免读者误入前页。截图两次cache miss；本次独立核的是PDF提取文本加HTML公式/算法，不伪称视觉渲染检查成功。本人没有重新签完整SPS深入Gate、三维评分或全实验因果审计。

## 签署范围与修改项

16988/17010/17019的Standard Only、17000的安全必要深入Only通过；16995仅中心目标隔离裁决通过。唯一修改建议是16995的PDF页定位明确零基或改物理页5/15。四项Only为受限新贡献报告而非全部Existing，均不需要本批新Books写回；本记录不覆盖本日来源/首次公开/去重分母或作者未决Books队列。当前Books未因本复核发生改动。
