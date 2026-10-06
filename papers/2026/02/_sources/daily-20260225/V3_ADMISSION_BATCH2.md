# 02/25 后批准入：18658～19049相关主题线索

执行2026-10-05。本日inventory对应完整title/abstract已实际逐条读；该文件保存贡献层，不继承旧筛选/评分/完成。只处理项目相关题摘线索，914宽库存不是关闭队列。日期先保留原Submitted/Registered，未确认落窗不列README确定候选。下表是潜力准入：实验可信度交证据审阅，不以未披露细节排除。

发现边界：已有914身份的title只用来查漏新命名机制；按ROADMAP主线挑选memory/RAG/Agent执行与验证、Transformer/表示/优化理论、模型训练与unlearning、推理memory/precision/PD/speculation、多模态生成/world model/VLA相关标题才读完整摘要。该批停止在已选相关title的19049；ID号段只是保存顺序，不是全号段逐项队列。其余明显领域应用、非模型系统标题未变为全文待办。补检原入口是本日inventory及官方cs月份列表V3_NATIVE_arxiv_month8000/10000，后者仅命名/身份补检而非本日日期证据；没有把月份分页数算作本窗扫描完成。

日期窄核：按精确ID从原DataCite gzip快照抽取Submitted:v1与Registered，而非扫描全月候选。67表项中18658～18749的18项满足Submitted >2026-02-20T19:00:00Z且Registered <2026-02-25T01:00:00Z。其余49项Registered晚于窗口，虽Submitted满足下界但不能确认上界，保留datehold；特别18750的Created=02/24 03:47:07Z而Registered=02/25 14:32:07Z，不能拿inventory doi_created替Registered。Updated:v1不补日期下界/公开证明。官方availability的Fri14～Mon14 ET→Mon20 ET公告配合Registered给18项本窗[2026-02-24T09:00:00+08:00,Registered+08:00]范围，不把Submitted视为公开。非作者准入优先这18项；其余不展开Evidence/Books。

| ID尾号 | 原约束 → 原文增量 → 拟核选择 | 分数 |
| --- | --- | --- | --- |
| 18658 | federated模型本地独立训练难线性混合 → mode-connectivity方差上界与闭式mix → 核mix可行条件 | 2+1+2=5 |
| 18671 | 幻觉概率只能靠多次生成 → spilled-energy两个logit度量 → 核无需训练检测与校准边界 | 2+1+2=5 |
| 18679 | in-context transfer-operator拟合黑箱 → tiny attention内算子机制分析 → 核Transformer如何用上下文而非科学任务指标 | 2+1+2=5 |
| 18690 | world-model空间拓扑与行动混淆 → motor-gated同构neural-field对照 → 核行动条件化表示 | 2+1+2=5 |
| 18694 | token rollout时间尺度与planner不匹配 → RQVAE temporal abstraction+MCTS → 核长程/部分可观测与模型误差 | 2+2+2=6 |
| 18700 | trajectory ownership可被改写 → outcome-preserving秘密action watermark → 核可检测性与任务无损边界 | 2+1+2=5 |
| 18702 | video reasoning full-frame混感知推理 → 按需grounding curriculum+gated selfreward → 核证据调用及训练预算 | 2+1+2=5 |
| 18710 | 同data/hypothesis不保证LLM分析一致 → persona分析差异与auditor → 核可复查分析执行的variance，不重引领域科学结论 | 2+1+2=5 |
| 18711 | hallucination编辑位置不明确 → layer-sensitivity局部编辑 → 核局部收益/保留能力 | 2+1+2=5 |
| 18721 | text伪标签修正不消费audio → 音频证据条件伪标签+textcorrector对照 → 核声学证据归因 | 2+1+2=5 |
| 18724 | bisimulation可退化表征坍塌 → pred/reward差异及potential探索 → 核任务相关等价条件 | 2+1+2=5 |
| 18733 | memorization混序列频率与prefix → common IID/specificprefix拆分 → 核检索/记忆解释边界 | 2+1+2=5 |
| 18734 | reranker与generator分别训练 → 同10k PopQA联合reward → 核可控证据选择/答案归因 | 2+1+2=5 |
| 18739 | video可视quality不等于下游action可靠 → HDmap/3D攻击并约束画质 → 核worldmodel表面保真安全盲区 | 2+1+2=5 |
| 18742 | video相似不保证action replay可用 → simulation replay筛训练视频 → 核数据质量与筛选成本 | 2+1+2=5 |
| 18745 | plot/image评分忽略几何语义 → symbolic验证与render对齐 → 核生成评价可执行性 | 2+1+2=5 |
| 18746 | textualreflection可脱离image → region verification → 核真正看图与纯反思对照 | 2+1+2=5 |
| 18749 | federation同量data分配不对应可学性 → learnability-gap驱动distillation allocation → 核通信/训练预算 | 2+1+2=5 |
| 18750 | 近存计算不能直接复用完整attention → SmartSSD轻量importance与cache分区 → 核容量/质量/带宽取舍 | 2+2+2=6 |
| 18755 | PD placement/DVFS独立控制混SLO能耗 → 双尺度placement+prefill MPC/decode slack → 核端到端控制收益 | 2+2+2=6 |
| 18758 | Winograd低比特outlier混误差通信 → 两轮协同量化/bitwidth → 核精度与通信而非单加速数 | 2+1+2=5 |
| 18767 | Lean搜索动作空间难控 → atomic tactic与ExprGraph → 核模型引导执行的语言/状态边界 | 2+1+2=5 |
| 18782 | 输出拒绝不约束内部多模态latent → benign density diffusion projection → 核安全/效用与攻击适用域 | 2+1+2=5 |
| 18799 | diffusion偏好引导成本/模式塌缩 → positive-negative contrastive guidance → 核采样机制和质量预算 | 2+2+2=6 |
| 18800 | operation风险不能直接从i.i.d.error推 → MDL scenario/domain perturbation界 → 核鲁棒性定义与假设 | 2+1+2=5 |
| 18813 | 单回合机器人成功不覆盖持续操作 → PRP连续TPH/MTBI+cyclic训练/edge蒸馏 → 核长程失效和协议 | 2+2+2=6 |
| 18825 | BNN剪枝量纲不等于确定权重 → magnitude/std lottery ticket界 → 核后验尺度与稀疏可行性 | 2+1+2=5 |
| 18830 | 场景时空tokens布局难一致 → spatiotemporal container+4DVQVAE → 核group autoregression结构 | 2+1+2=5 |
| 18845 | finetune可覆盖ownership watermark → double-trigger derivative injection → 核迁移/误报/保留能力 | 2+1+2=5 |
| 18846 | 仅vision压缩不能控总context → vision merge+text drop训练适配 → 核同token budget质量 | 2+1+2=5 |
| 18849 | attention集中度不直接量化扰动敏感 → exact Jacobian distribution theta+3runs → 核对“尖峰更脆弱”判断的反证 | 2+2+2=6 |
| 18851 | FP8 attention误差按统一scale估 → rank-aware几何bound → 核precision配置与误差条件 | 2+2+2=6 |
| 18856 | randompolicy复杂度忽略reward结构 → PIC/POIC sparse/dense差异 → 核探索评价混杂 | 2+1+2=5 |
| 18857 | metaRL更新belief在线成本高 → variational Bayes adaptive SMC → 核belief状态与sample成本 | 2+1+2=5 |
| 18861 | ViT PTQ无原数据校准错分布 → joint生成prompt校准 → 核重建数据与bitwidth控制 | 2+1+2=5 |
| 18868 | unlearning输出抑制可被学习恢复 → spectral parameter抵抗linear-width restoration → 核恢复攻击/容量边界 | 2+2+2=6 |
| 18882 | scene token长度/排列难扩 → permutation-invariant压缩token+flow → 核信息压缩与几何质量 | 2+1+2=5 |
| 18884 | next-token合格不证明task ordering形成 → next/prev任务与跨模态负侧 → 核训练顺序与能力条件 | 2+1+2=5 |
| 18887 | safety worldmodel不区分每Agent未来 → trajectory-conditioned sparse model+collision rule → 核闭环安全而非单预测误差 | 2+1+2=5 |
| 18896 | encoder drift使codebook失用 → NSVQ/TransVQ kmeans更新 → 核非静态codebook学习条件 | 2+2+2=6 |
| 18899 | phonological表示跨语言不可组合 → 96语言向量算术 → 核表示可迁移性及受控反侧 | 2+1+2=5 |
| 18904 | VQ离散codebook更新开销/死码 → online Oja PCA VAE → 核无codebook替代的压缩代价 | 2+1+2=5 |
| 18905 | CoT解释不能定位执行错误 → blind verification+perturbed DAG Shapley → 核causal reasoning评价边界 | 2+1+2=5 |
| 18914 | MCP描述可用性非协议schema覆盖 → 10831工具smell及受控mutation → 核description与成功/成本 | 2+1+2=5 |
| 18922 | 语义cache相似不保证答案同义 → W5H2 intent canonicalization+RCPS selective → 核一致性与覆盖率 | 2+2+2=6 |
| 18928 | codebenchmark复杂度混任务大小 → multiobjective controlled transforms → 核generator与grader有效性 | 2+1+2=5 |
| 18931 | WAN draft发送/target通信成本高 → 冗余draft局部验证分解 → 核WAN带宽与speculative质量 | 2+2+2=6 |
| 18936 | content/style LoRA分离不控noise-time → timestep content-style guidance → 核adapter归因与质量 | 2+1+2=5 |
| 18940 | judge强弱与时间/事实正确性混 → capability parity agentic evaluation → 核budget公平与judge可靠性 | 2+2+2=6 |
| 18948 | relationalTransformer对称冗余 → symmetry reduction → 核表示等价与计算收益假设 | 2+1+2=5 |
| 18952 | MDM ASR位置采样不看不确定性 → selfcorrection+position-entropy sampler → 核相同步数/质量 | 2+1+2=5 |
| 18968 | 工具局部schema失败引发全量replan → dependency graph局部repair → 核状态/重试边界 | 2+1+2=5 |
| 18971 | stated preference误当任务能力 → advice/refusal与performance拆分 → 核用偏好预测behavior的条件 | 2+1+2=5 |
| 18993 | token reuse噪声积累 → spectral-filter semantic cache → 核reuse预算与质量 | 2+1+2=5 |
| 18998 | Agent成功率混串行context/并行验证 → sequential ceiling与parallel verification gap → 核评价预算机制 | 2+2+2=6 |
| 19000 | multitaskAgent梯度互扰 → 2stage SFT+multitaskRL控制 → 核负迁移而非pipeline名字 | 2+1+2=5 |
| 19001 | personal memory检索混concept/event/aggregate → graph与visual source多级协议 → 核证据粒度盲区 | 2+1+2=5 |
| 19008 | 模型准确率不证明canonical path一致 → 22model/3run/108task path deviation控制 → 核归因/泄漏 | 2+1+2=5 |
| 19017 | 连续ERM复杂度掩有限精度 → polynomial #P/ReLU NP与bitbackprop → 核可计算学习假设 | 2+1+2=5 |
| 19019 | watermark单概念无法追多内容 → latent+text multiconcept query tracing → 核ownership误报与鲁棒性 | 2+1+2=5 |
| 19020 | passive membership inference受限 → RL active reconstruction → 核交互攻击预算/泄漏边界 | 2+1+2=5 |
| 19024 | CLIP概率confidence错校 → margin mean/variance momentmatch → 核不改classifier校准 | 2+1+2=5 |
| 19031 | photonic算力数字不等于模型执行 → wavelength tensor core ResNet推理 → 核compute/dataflow/精度可行性 | 2+1+2=5 |
| 19033 | modelcollapse只经验解释 → Markov ergodicity+direction contraction diffusion → 核假设与再训练表示衰减 | 2+2+2=6 |
| 19041 | cyclic偏好不存在统一scalar → MaxEnt/Blackwell多目标更新 → 核RLHF目标非标量条件 | 2+2+2=6 |
| 19043 | 编辑knowledge孤立query评价 → unstructured context依赖与prepend rescue → 核编辑时上下文失效 | 2+1+2=5 |
| 19049 | RL偏好鼓励verbosity混token credit → conditional MI token advantage与保证 → 核信息增量奖励/理论假设 | 2+2+2=6 |

以下必要准入事实含糊，仅定点核心补读即停，不先排除或自动5分：18674 local ReLU随机扰动bound是否真新增robustness条件；18695 data-dependent variable-length插入flow是否有通用离散生成机制，不把分子指标作为准入；18699 semantic substrate operator是否有新可验证结论而非框架命名；18806 Think2的dualcontroller是否改变effort/验证控制；18823 EvalSense perturb/meta-eval是否揭露具体评价盲区；18941 dual planning/grounding是否有新增动态subgoal/状态修复条件；18955 incTNP Bayesian一致性与causalKV是否改变缓存推断条件；19040 video multiAgent prior-trace memory是否有可核验协作机制。

明确排除，日期未核实且不再为不影响排除的日期开请求：18662 temporal causal discovery跨科学domain扩数据/scale叙述，题摘未建立新的模型训练/表示机制条件；18764 SGD/MCP经典收敛原则并列，无新增学习边界；18776阿拉伯number accuracy/format局部排行榜，未建立新的评价混杂或机制；18788 Burmese benchmark语言覆盖，无新增模型/执行机制或足以改判断的盲区；18812 diffusion maze planner普通组件应用，与CNN数量对比不辨新机制；18832/20059社交帖子parallelmonologue指标，未新增Agent实际执行/协调边界；18850力/按钮/voice人机意图实验非基础模型/系统机制；18920 scientific idea生成领域应用，未建立独立模型/Agent增量；18960综述modularity术语不新增机制或证据；18981 screen-only ARPG视觉FSM组件组合，题摘未建立新增控制条件；18986 failure×harm×severity经典Bayesian risk用于治理case，未新增模型系统特有失效或控制；19065 Act-Verify-Refine概念案例和迭代收敛框架，不用验证术语替代真实新增机制。

非作者后批准入校准：root实际独核18确定日期潜力完整题摘和18662/18764/18776/18788排除。16窄潜力通过；18679只承tiny attention ICL形成，不采用领域科学指标，18710只承固定spec/data仍有分析执行分散，不采用领域科学结论。18734/18745一次核心重开；18662/18764/18788排除通过，其他49datehold不声称全量校准。

18776排除撤回：题摘98～99%准确仍需fallback且format compliance≠correctness，是可改评价判断的潜力；原Registered晚窗，保持日期hold，不为不决定本窗处置的细节深入正文。

核心补读已实际进行：18734 §3.3不是纯jointtraining改名，历史成功率→平滑Bernoulli文档标签→pairwise ranking代理是显式延迟文档credit机制；§4.3 cross-swap又显示reranker单独收益弱/偶有下降，联合训练收益不等于模块可迁移。维持5分潜力，但删“严格GRPO等价”宣传（作者也说not strict equivalence），只审代理credit与组件依赖。18745 §3.2、4.5、Appendix B把图像重构绑定deterministic plotting IR，code/caption/none保持输入的对照和annotation-fidelity vs parse-valid诊断是实际表示/评价增量，不仅geometry合成配方；维持5分潜力，仅采用图像事实到可验证IR，不外推通用视觉推理。

18674一次必要核心：§3/4 Theorem4.2为ReLU+Heaviside classifier、uniform fixed-radius球面扰动、离activation-cell边界距离a(x)的条件bound，n exp[-a²d/(2r²)]限制随机扰动误分；它不是worst-case对抗安全，n随d多项式也仍须a/r不缩得太快。该具体条件及随机测试≠最坏扰动是可保留理论边界，2+1+2=5，继续必要证据核中心桥。18695 §3.1～3.3、5.1.1～2明确把insertion/unmask order做data-dependent hazard并保持terminal flow，fixed unmask vs learned的稳定性/顺序指标相反反侧，是通用可变长离散生成训练机制；准入2+1+2=5，只采用hazard/表示/稳定性，不采用分子领域结论。18699 §3～8/10只有embedding graph/JS/W1/operatorcomposition既有量组合；Prop1明标Imported contractivity，预测protocol未提供新推导或验证，不建立semantic curvature→fragility桥；核心后贡献排除，不因“theory-only”本身排除。
