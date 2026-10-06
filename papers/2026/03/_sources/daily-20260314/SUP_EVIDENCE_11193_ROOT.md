# 11193 DeReason：必要原证与具体已有覆盖

root 作者；只处理03-14补充窗口Mar13，原候选/窗口不动。此为待非作者核验的单篇记录，不授DAY。

## 身份与范围

[精确v1](https://arxiv.org/html/2603.11193v1)，题摘和官方元数据为本日 `SUP_TITLE_ABS_11193.txt/.raw`、`SUP_DATE_11193.raw`、`SUP_DATE_SECOND.md`。v1提交Wed18:01:55UTC晚于Wed截止，owning/findable注册Mar13给同日公开上界；这两类证据共同限定公开Mar13，不单用Submitted/Registered。未见当前事件的撤回或重要修订信号，不比较旧版。研究对象是后训练的人口分配，不因评价含STEM就当成暂缓的AI for Science应用。

## 实际必要阅读及结论

root实际打开v1并读§2.1–2.2/Eq1–3、§3.1–3.4/Table1、§4.1–4.5/Table2及直接结论。核心是同一问题池的stage-aware分配：Qwen3-4B-Instruct给1～5 reasoning-intensity分，≥4进入RL，其余广覆盖样本用于SFT；Qwen3-4B-Instruct-2507提供teacher responses，Qwen3-4B-Base经SFT后GRPO。评分者不是独立校准的题目难度oracle；冻结分数不自动代表SFT后的可探索性。

SFT batch128/LR1e-5，RL batch128/minibatch64/LR1e-6/maxresponse8192；两语料WebInstruct-Verified/Webscale-RL。General reasoning的reward用model-based语义等价判分，不是全部确定性规则。Eq1比率写pi_theta/pi_ref，不能据此替换实际old-policy实现。控制问题/数据量不等于控制全部训练tokens、epochs、rollout/judge费用或wallclock；硬件、precision、总预算和训练seed不充分披露，线上SLO不适用离线结果。

Table1 WebInstruct random-SFT→RL平均42.9，难度分配43.8，但MMLU-Pro68.6→68.4反退；Webscale SFT60.7 vs本方案60.3也非Pareto。Table2 Webscale AIME25 SFT23.3 vs本方案20.7，不能只报告平均增益。§4.1 score4/5的math人口约78%/96%，难度路由同时改变领域混合，未独立识别difficulty的因果作用。GPQA八次pass1是生成评价重复，不等八次独立训练seed；entropy/长度变化也不证明“SFT只记忆、RL天生泛化”或普遍省算。未核代码、未复现，不扩大到全部附件。

## 评分与Books判断

拟 **2+1+2=5，标准完成，已有覆盖**：新增是跨SFT/RL数据分配的局部受控对照及其适用边界；Reach只计后训练allocator这一局部责任，不借用完整生命周期加分。不是因Books已有覆盖而降低准入或分数。

实际连续读 [TRAIN-SFT / Ch29](../../../../../books/part-04-training-system/29-sft.md) 的 `Data Difficulty 在 Generalization 与 Extrapolation 间重新分配容量` 全节（当前727–737）：已有难度proxy/初始化/verifier身份、SFT与RL的目标及有效人口不同、静态probe按同池轨迹分到两目标、随机mixed/full-SFT/full-RL与完整预算对照、域外回归和混合覆盖回退。这不是仅主题匹配。DeReason以LLM评分替换梯度probe并补充4B两语料实验，不改变这些长期设计判断；本稿领域混合反侧正落在现有“难度由生成器/solver定义时引入测量偏差、以held-out切片选择配比”的边界。无需再向正文追加论文摘要或把≥4作为通用阈值；其具体结果与未证明内容留在本日证据区。

mar14_supplement已实际必要v1方法/关键评价与Ch29完整邻接独核通过，见`SUP_NC_11193.md`。若发现现有正文不能承载某个确切新命题，才重开相应差额；本次无Books写入、无共享锁，不自授整天完成。
