# root必要原证复用与窄Books提案（待独核）

不重复root已完成的必要核心，不用旧done标签；全文题摘、精确版本身份/日级日期字段均为本轮原件。当前为author拟采用命题，不授写后结果或DAY。

## 12440 KernelFoundry / INFER-TENSORRT-LLM

[v1](https://arxiv.org/html/2603.12440v1) root非准备者实际§3.2–3.6/4/5.1/5.2/B2/B4/D与Ch49 1539–1566。score2+2+2=6，具体archive/proposal与独立admission差额深入。code静态memory/algo/sync描述符而非动态真实瓶颈，每格elite；parent→child经验结果proxy引导parent/自然语言变异，不是反传梯度。prompt archive共演化无单独消融；template实测调参与算法proposal分开。正文64cells/B4 dimensions4矛盾，不批准grid精确实现。fitness incorrect0.1是搜索信号，不授正确性；有限99%相对误差<1%+cosine不证明全输入。40代表/111过滤、Arc140V/B580/A6000与baseline模型/预算、backward孤立kernel/autograd计时不等，不采普遍2.3x/完整LLM速度。artifact未核。

作者实际Ch49 1539–1568顺读，拟在原compiler/verifier责任段之后、具体correctness段前，仅两段：

候选搜索还可以主动保留不同代码策略，而不只沿当前最快样本反复变异。一个质量—多样性分支按代码的memory/algo/synchronization静态描述符分格保留elite，用已测parent→child变化作为选父与自然语言变异的经验proxy，再把参数化template的实测调参与算法proposal分开。它扩大探索，却不由静态标签认证真实瓶颈，也不将所谓gradient启发式变成反向传播；prompt与kernel共演化同样只是proposal侧的选择，不能接管compiler或独立verifier的admission。<!-- source-family:SF-2026-ARXIV-2603-12440 -->

[KernelFoundry的必要原证](https://arxiv.org/html/2603.12440v1)仅支持披露任务、硬件与有限数值检查中的搜索分支；archive规格表述不一致、组件缺独立消融、任务过滤与baseline预算差异限制了归因，不能把整体speedup分配给每项模块。搜索fitness即使给incorrect候选非零值，也不是允许部署错误kernel，代表输入的相似度/误差门不等于全部shape与输入正确。生成、编译、template benchmarking、archive维护和held-out回归均计费，孤立kernel对autograd的计时差也不代表完整模型改善；稳定shape或探索预算有限时，保留手写/原template分支，只有独立correctness与workload-bound benchmark通过才接纳产物。<!-- source-family:SF-2026-ARXIV-2603-12440 -->

## 12631 CoMAM / score2+2+2=6，中心reward定义争议暂缓提案

[v1](https://arxiv.org/html/2603.12631v1) root实际§4.1–4.3/5.1–5.6/Alg1/B1–3/E、Ch77 153–173。增量group轨迹local/global ranking→NDCG→softmax角色权重，不是已有反事实或检索次数credit；保持候选/评分，不因争议删池。Eq15 local+w×global与Alg1 line15 global+w×local中心实现不一致；Table5 independent285+180+150=615但报415，32K的48+57+65=170但报160，steps相加或max也非totalFLOP/wallclock。PersonaMem >180hist/~6000MC，targetsession训练/fullhist验证、query split未明确history-disjoint；Seed1.6生成evidence+human。Qwen3Bcons/7Bret或Llama3B/8B，32kcontext/3koutput/batch128group8epochs5/temp1或.8/≥3seeds，hardware/precision/SLO ND。有限Table4 LG/adaptive不授唯一因果credit；static三步无update/delete/动态频率学习。

实际差额成立，但拟不将不确定reward配方进入Books：单次精确请求作者Eq15↔Alg1实际使用定义/实现及Table5分账解释，重开12631v1中心reward与成本比较，非普通未读附件受阻。不采用正面精确reward、因果credit或普遍效率；reader需确认安全隔离范围，root建议可沉淀的ranking proxy暂不变成独立无实现依据段。

## 12554 EG-SPO / TRAIN-GRPO 两段PRE

[v1](https://arxiv.org/html/2603.12554v1) root实际§4.1–4.4/5/5.2、A Lemma3/Prop5、B rewards、C settings/Alg1；Ch33 actual2514–2542复用，作者本次2513–2544读回。score2+2+2=6，不改分；exact completepath PG只在真实transition/action law下，Remark2 θ-independent选择省selection score，但confidence-dependent选择没完成此桥梁。entropy topK是有偏近似；Lemma A≤1/logit梯度界B。Eq17=(1+lambda)r−lambda Vhat，Vhat一步distribution/greedy近似，不是普通r−V。8A100/LLaDA8B LoRA128/gen256/T128/block32/K8/G8，greedy128/256/512、publishedbaseline预算不同、Sudoku0shotvsSPG3shot及FLOP图不等wallclock，precision/SLO ND。

现Ch33 frozen-state局部候选/完整trajectory-surrogate边界已承载credit；具体差额只entropy topK更新预算与stepwise completion proxy分开。拟在2602.06462两段之后、2602.14147 surrogate权重段前，逐字两段：

更新预算与信用估计还应作为两项独立选择：可按entropy只选择少数去噪step投入更新，再以一步completion近似的terminal reward作为局部baseline proposal。前者减少求值位置却引入截断偏差，后者仍不等于从该状态继续运行真实剩余trajectory；局部value proxy与最终reward的混合也不自动成为普通reward-minus-value advantage。若选择本身依赖当前policy的confidence，不能直接套用与参数无关的选择规则来省略selection score。<!-- source-family:SF-2026-ARXIV-2603-12554 -->

[EG-SPO的受限分支](https://arxiv.org/html/2603.12554v1)把entropy预算与一步value近似共同用于训练，但完整轨迹下的exact-gradient推导不认证实际top-k近似及confidence-dependent选择无偏；bounded advantage/梯度假设也不变成任意模型保证。候选completion、reward、组内中心化与裁剪/KL、额外backward均计费，FLOP估算和不同shots/已发表baseline不等同预算墙钟胜出。选择信号、value proxy或预算对照不可靠时，保留完整outcome rollout、原有frozen-state候选比较与标准diffusion surrogate，不以少更新step签发普遍效率或理论稳定性。<!-- source-family:SF-2026-ARXIV-2603-12554 -->

## 12465 TaxBreak现有句准确性修正PRE（不新增机制段）

reader必要原证发现现Ch49 177“每个kernel…精确拆”超出§III-B2 median/native/fallback与VII369 imperfectreplay。拟仅把“TaxBreak 把每个 kernel 的 host orchestration 精确拆为”改成“TaxBreak 按所设 baseline 将 host orchestration 作三层估计：”，并把“再用 HDBI 对照 host orchestration 和 device-active time。”改成“再用 HDBI 对照 host orchestration 和 device-active time；该工作比不是墙钟或精确因果分解。”原三层名称、责任、代价、粗profile合理性及source-family保持。不制造新论文段，仍已有覆盖+必要准确性修正；root窄锁/reader逐字PRE后才改，本项实际POST另核。
