# 第三十二包：自评训练、冻结VLM条件与未来/工具消费者

Books/ROADMAP有效。actual Ch24复合reward标准化全文/marker与lean-adjoint完整下段；Ch23 projector瓶颈完整段与音频caption完整下段；Ch25 WorldMAP完整段及预测channel完整引入/三channel，Ch78选择性调用全文/inline marker及Tool Contract完整字段均读。Ch77/79开头交接本轮有效，首必要R40/R41复用，不第二Methods/实现/复现。

## 12784 SRUM / 2+1+2=5 / MULTIMODAL-GENERATIVE-PARADIGMS Ch24

reward候选搜索未承担自生成/自评局部map乘全局归一权重、训练velocity本身；插完整SF2509-19831独立marker后、lean-adjoint首段前。

正文：

质量参照也可以进入生成器的训练权重，而不只在部署挑候选：让统一多模态模型自产样本、读出局部reward map，再乘归一后的全局权重，重加权velocity目标。[受限自评后训练分支](https://arxiv.org/html/2510.12784v1#S3)把局部位置与整例偏好分开，但同源generator/judge可能共同确认旧错，某些实例还需外部box或分割器，不是闭环无外资源。打印的reference velocity平方不是policy KL，也不证明防reward hacking；负权/regularizer条件未闭时不补稳定训练recipe。样本/指令分集、box/局部map、judge/归一与生成器版本须共同保存，理解bench和部分生成指标仍可退步。全部自产、定位/分割、自评、后训练和独立质量回归都计费；参照、权重或旧能力失配时保原生成目标、可信外部评价与较窄更新，不由自改进名称批准真实效用、全维提升和无hacking。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12784 -->`

本人末注：

- `SF-2025-ARXIV-2510-12784` — Herschel，Daily2025-10-16补Oct15；消费Cicero R40 exact-v1 §3/4/A/C首次必要，2+1+2=5，仅局部reward map×归一全局权重的velocity后训练差额。保Bagel另SAM/Blipnative、reference非KL/负权lambda未闭、理解与GenEval切片反退/WISE非全zero-shot、40kcontext/512–1024与HWprecision预算未知、全部生成/boxes/judge/后训费，不授防hacking。未第二Methods/代码/复现；PRE/SAVE/selfread/solePOST只canonical实际层。

## 12789 UniFusion / 2+2+2=6 / MULTIMODAL-REPRESENTATION Ch23

普通modality encoder→language projector未承担冻结VLM多层LAP汇聚→bidirectional refiner→仅DiT消费的反向生成条件；插完整“当目标以理解为主”段后、音频caption首段前。

正文：

复用语言主干的表示也可以朝生成器输出条件，而不只接收视觉后生成文字：冻结VLM，间隔抽取中层特征并汇聚，再经双向refiner交给DiT。[受限理解—生成接口](https://arxiv.org/html/2510.12789v1#S2)改变了特征层位与消费者，不是末层表示直接替换任意文本encoder；更多图像tile仍要付token、feature与融合费用。生成过程中保留原attention再改写条件，免额外重新encode也不免自回归decode。VLM/层位、汇聚/refiner、tile与DiT训练人口须共同绑定，初始比较可弱于普通文本encoder，延长训练后的差额不能冒同预算结构因果。精选生成不是通用zero-shot，新增judge/CoT、宏微均值和best-of协议也不能与旧榜混排。全原模型、refiner/DiT训练、改写/特征驻留及独立理解/生成回归均付费；接口、旧能力或总预算失配时保原文本encoder、独立projector与已验生成器，不由统一名称批准任意条件替换、全VLM能力保持和免费多模态。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12789 -->`

本人末注：

- `SF-2025-ARXIV-2510-12789` — Herschel，Daily2025-10-16补Oct15；消费Cicero R41 exact-v1 §2–4/B1–2首次必要，2+2+2=6，仅frozen VLM每三层LAP→双向refiner→DiT条件接口差额。保tile/feature费、Verifi仍ARdecode、5B200k架构与8BDiT+8BVLM/830M终训分设、初Llama弱T5/延训混杂、DPG口径与新Gemma27B/CoT宏微/best4协议、全部费用，不授全zero-shot或旧能力保持。未第二Methods/代码/复现；PRE/SAVE/selfread/solePOST只canonical实际层。

## 12796 DriveVLA-W0 / 2+2+2=6 / MULTIMODAL-WORLD-MODELS Ch25

WorldMAP部署移除整条伪路径teacher，未承担同backbone未来视觉辅助目标与action joint-attention、部署绕过未来生成的分责；插完整WorldMAP inline段后、预测Channel标题前。

正文：

未来生成还可以只在训练中塑造动作模型的共享状态，而不在每次决策先rollout视频：以未来视觉token预测或latent diffusion作辅助目标，再由action expert读取与大backbone共同交互的状态，部署绕过视觉生成头。[受限训练期未来分支](https://arxiv.org/html/2510.12796v1#S3)区分预测监督与运行时规划，不把移除生成头叫作免跑主干或稀疏expert。视觉/动作目标、冻结集合、上下文和动作query/AR/flow消费者须共同保存；模态数变化、action-only/vision-only的局部对照不证明唯一迁移原因，排名随训练人口变化也不是纯数据规模定律。未来保真与动作结果须分验，best-of与单样本、不同传感输入和延迟点不能合成一个实时SLO。全预训/辅助生成、action训练和真实闭环回归均付费；未来支持、动作或净时限失配时保action-only/原policy、真实观测与独立controller，不由更好辅助预测批准真实未来、在线imagined planning或实路安全。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12796 -->`

本人末注：

- `SF-2025-ARXIV-2510-12796` — Herschel，Daily2025-10-16补Oct15；消费Cicero R41 exact-v1 §3/4/B1–3/D首次必要，2+2+2=6，仅future视觉辅助训练/部署bypass与action消费者差额。保jointattention仍跑大backbone、6VA→2VA/单模态有限、Emu3-8B/Qwen2.5VL7B/NAVSIM8L20B48BF16与inhouse64GPU70M帧分设、query74.3/AR95或170/flow145ms非SLO、单frontcam/best6/4scontext反退及全费，不授实路安全。未第二Methods/代码/复现；PRE/SAVE/selfread/solePOST只canonical实际层。

## 12801 DeepMMSearch-R1 / 2+2+2=6 / AGENT-TOOL-CALLING Ch78

选择性invoke/skip偏好未承担gold过滤的搜索/免搜索混合示教→在线GRPO、retrieved span作观察而非target loss的调用学习支持；插完整SF2606-00510 inline段后、Tool Contract标题前。不跨Ch33复制优化器推导。

正文：

何时搜索也可以由混合示教与真实工具反馈训练，而不预先要求每题固定检索：先保留最终答案匹配gold的教师轨迹，混入无需搜索的示例，再在在线rollout中更新调用与回答策略。[受限多模态搜索分支](https://arxiv.org/html/2510.12801v1#S2)把检索span作为新输入、不是直接模仿的loss target；gold匹配不认证整条工具理由或来源真值，私有搜索/裁剪/摘要仍是独立依赖。Search/free比例、taxonomy、工具/API与索引快照、调用上限和reward版本须共同保存，reward主附文身份冲突不能补成唯一版本；固定两次RAG也不代表全部RAG。有限混合比例最佳、少调用或均值上升仍伴局部任务反退，不授通用零搜索或无遗忘。全部teacher造数、grounding/search/摘要、冷启/多rollout和独立答案/工具回归均付费；来源、reward或净质量失配时保明确检索规则、原回答路径/不调用与独立executor，不由训练过的调用意愿批准真实证据、权限和服务SLO。

独立marker：`<!-- source-family:SF-2025-ARXIV-2510-12801 -->`

本人末注：

- `SF-2025-ARXIV-2510-12801` — Herschel，Daily2025-10-16补Oct15；消费Cicero R41 exact-v1 §2–4/D首次必要，2+2+2=6，仅gold-filter/search-free混合→在线调用学习与retrieved span观察资格差额。保DINOcrop/私有API/top5摘要、Qwen2.5VL7B/SFT8H100B8三ep与RL32H100B256八rollout20ep8192/10calls、GPT5chat对GPT4o reward冲突、AOKVQA/MathVista反退/50:50只本基准及全部费，不授私有历史索引复原/安全或SLO。未第二Methods/代码/复现；PRE/SAVE/selfread/solePOST只canonical实际层。

请sole reader整体核四完整原稿/独立marker/本人注与完整邻接；未SAVE/不预POST。
