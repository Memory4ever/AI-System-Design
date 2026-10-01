# 04/20 三项贡献前关闭的有限独立反查

复核者：root，非本日作者。2026-09-28。仅核三项是否应进入本项目候选分母，以及已经披露的必要反证；不核首次公开归属、全来源、全部 50 项前关闭或整日 Gate。以下恢复的是**待本日作者同步的窄候选准入**，不是赞成论文宣传，也不自动触发 Books 新增。

## `2604.15675v1` C-Mining：恢复标准审阅／仅报告

[官方 exact-v1](https://arxiv.org/html/2604.15675v1) §3.2–3.4、§4.2–4.5／Tables 1、3、4、6 给出的有限选择不是“文化 embedding 即真值”，而是：在已决定从多语言原始文本合成低资源文化指令数据时，**seed 的跨语几何错位**可成为比随机或仅单语过滤更有针对性的筛选信号。固定 Qwen3-32B 的 Table 3 中，Random Seeds 的 CB-H/BLEnD 为 43.31/81.13，Monolingual 为 44.83/83.38，Full C-Mining 为 46.98/85.81；Random 相对 Base 44.62/82.63 还会反退。它使 Ch27 的“先定义数据选择目标与对照，再生成监督”在这一明确条件下有可报告的选择分支。原作者侧“未识别改变选择规则的条件”过严，且 apr02 已对标准证据／仅报告作过非作者有限核；恢复工作评分 2+1+2=5。

限制：同一合成流水线中 seed 数量、质量及文化真值并未被完全隔离；Eq2 的 cosine 行归一可能遇负值／零分母，不能无条件称合法概率熵；Table 1 的 77.12→80.94 是 3.82pp，不是原文文字的 3.13；Table 6 的 mining 费用不是完整数据合成与训练成本。该局部机制不修改 Ch27 已有的 selection/provenance/teacher 权限合同，也不能成为普遍文化正确性声明。若本日日期 Gate 确认落窗，本日 §3／§4 恢复 **标准完成、仅报告**，不写 Books。

## `2604.15583v1` SAGE：恢复标准审阅／仅报告

[官方 exact-v1](https://arxiv.org/html/2604.15583v1) §3.1–3.3、§4.4–4.7 中，本地较小 attention model **先对整文档分块 prefill**、合并 query→document attention，再按严格 token budget 选择连续窗口；同文档多 query 可以复用 encoding。它不是单纯“检索更深”或无成本压缩，而是把成本从远端 reader 的长输入转移到本地 selector 的全篇前向与缓存。QuALITY-hard 在 10% 文档 token budget 下的有限质量对照、3797 queries／3011 cache hits／690.9s 的报告，与 UAE 98.2s、Qwen3 embedding 370.7s 的较低检索时间一起表明质量—成本并非同向。这足以使 Ch76 的 context selection 在**同文档多 query、reader 输入受限、本地 prefill 可摊销**时有一个可报告的物理选择分支；原作者侧“prefill/cache 成本没有新可行条件”过严。建议工作评分 2+1+2=5，标准审阅后仅报告；若日级证据尚缺，则仍标待审，不因本独立准入核直接写完成。

限制：作者的 QuALITY、Paper 等配置不是生产端到端 SLO 对照；不同 RAG baselines 的一次建索引/embedding 时间与 SAGE 多 query 缓存复用不能直接当同一账本，且注意力信号不拥有事实权威。单次 query、频繁变更文档或本地模型开销较高时，常规 chunk/hybrid 检索仍可更合适。Ch76 已有预算、证据充分性和数据/查询责任，当前不需要把单篇 selector 强写为长期正文。

## `2604.15771v1` Skill-RAG：恢复标准审阅／仅报告

[官方 exact-v1](https://arxiv.org/html/2604.15771v1) §3／Table 1 将两道门分开：hidden-state prober 先判断是否重检索；若已有回答失败，router 读取该次 reasoning、answer 与 evidence，选择 rewrite、decompose、focus 或 exit。与无条件追加 top-k／同一重试动作相比，它提出了**失败后哪一类恢复动作应接管控制**这一窄分支。固定 Gemma2-9B、BM25、4-shot 的 OOD ACC 中，MuSiQue 13.9→20.0、2Wiki 38.9→52.5 是相对 Probing-RAG 的受限对照；不能抹去 Hotpot EM 24.2<DRAGIN 35.6。Ch76 已有 sufficiency→re-query/decompose/abstain 责任链，但不能以这些动作名称已出现就排除失败条件化选择的具体候选价值。原作者侧“没有超出现有责任”不足以关闭；建议工作评分 2+1+2=5，完成标准审阅后仅报告。

限制：probe 标签来自 gold answer、只在训练的三个域与所列两个 OOD 域测试；实验未隔离各 skill 相对更强的无 probe／等预算 router 方案，也不能由 t-SNE 可分簇推失败因果类型或跨模型可移植性。需要 probe、router 和多次检索额外成本；不能把“模型知道自己失败”或自动修复当成可部署保证。若后续有消融能改变 Ch76 现有动作选择/终止合同再重开 Books，目前不写入。

三项均只恢复到日作者侧有限候选工作态；日期、去重、其余负侧抽样及正式日报仍必须按合同独立收口。保留原前关闭记录和本次改判链，不能静默删除旧证据。
