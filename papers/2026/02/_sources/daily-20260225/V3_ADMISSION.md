# 02/25 当前合同准入重建

执行：2026-10-05。旧914宽库存仅作本窗主题命名查漏，不承认旧914/914或18候选完成标签；全文题摘来自本日inventory，拟采用时以当前官方事件页、精确v1核版本和日期。首次公开待核时不先授落窗候选。

首批准入校准：以下为实际读完题摘后的贡献判断，不是Evidence/Books完成。原始题摘与身份：`inventory.json`对应arxiv_id。未列者尚未判贡献；后续只继续项目相关主题线索。

| ID尾号 | 原约束 → 实际增量 → 改变选择 | 拟分数 |
| --- | --- | --- |
| 18437 | 单次引用生成混淆匹配与相关性 → 逐引用错误定位/修复和过程奖励 → 核查反思训练是否控制噪检索与答案收益 | 2+1+2=5 |
| 18446 | 报告流畅不等于论证可审计 → 宏观/解释/主张支持三级标注及表面扰动 → 改变报告judge验证协议 | 2+2+2=6 |
| 18447 | 步级target验证本身贵 → draft校准置信度选择性升级 → 不再默认所有推理步用target验证，核准确性代价 | 2+2+2=6 |
| 18449 | 黑箱prompt只能全句改写 → DLM遮罩跨度去噪利用交互轨迹 → 核局部改写与扩散步预算的稳定边界 | 1+1+2=4 |
| 18450 | 多Agent语义趋同解释模糊 → 不动锚点的黎曼投影/熵归零定理 → 核模型假设能否支持语义坍塌，而非术语类比 | 2+1+2=5 |
| 18458 | 论文叙述审查不能辨重现性 → 执行代码/数据验证mechanistic研究并揭露漏检问题 → 改变评估证据链而非仅judge分数 | 2+2+2=6 |
| 18487 | label/context联合编码限制NER标签扩张 → label embedding预计算的bi-encoder对照 → 核规模收益与表示质量的具体取舍 | 2+1+2=5 |
| 18492 | 单judge错收不稳 → 统一执行ground truth下1～6人一致委员会FPR/TPR → 改变验收阈值与冗余选择 | 2+1+2=5 |
| 18493 | 流式事实更新被延至问答 → 共享CRUD memory与branch QA回报分层GRPO → 区分记忆维护credit和逐问题策略 | 2+2+2=6 |
| 18494 | 有限资源如何约束语义结构不明 → Landauer约束推导离散组合必要性 → 核定理是否真的支持所声称必然性 | 2+2+2=6 |
| 18505 | 输出遗忘掩盖表示保留 → SAE恢复测试含retraining对照 → 区分抑制与删除及验证协议 | 2+2+2=6 |
| 18523 | 单任务grokking不能解释共享任务动态 → 跨seed/WD控制及正交梯度删减 → 核低维轨迹与压缩/脆弱性的非等价 | 2+1+2=5 |
| 18527 | 单声道2D表示不能显式定位声源 → RGB-D+FOA Neural IV与重叠源对照 → 改变跨模态空间表示条件 | 2+1+2=5 |
| 18528 | 持续TTA更新造成遗忘 → fusion参数buffer检索/选择 → 核跨域迁移是否来自融合层而非源数据 | 2+1+2=5 |
| 18532 | VLA论文协议混杂 → 同baseline/评价拆组件/感知/动作12控制结论 → 核设计归因与sim-real边界 | 2+2+2=6 |
| 18533 | 名称屏蔽是否阻止身份恢复未知 → 描述词自蒸馏与随机词控制 → 核身份表示/版权guardrail边界，不外推机制必然性 | 2+1+2=5 |
| 18534 | 外库opaque类型使代码迁移难验 → 公开API adapter建立跨语言I/O等价验证 → 区分编译通过与语义验证 | 2+1+2=5 |
| 18537 | 静态Notebook源码缺运行状态 → kernel结构状态对照 → 核crash因果诊断与执行工具观测价值 | 2+1+2=5 |
| 18541 | OpenAPI冗余token但压缩可丢语义 → LAPIS集中错误/trigger/flow表示 → 核尺寸对照与语义兼容边界 | 2+1+2=5 |
| 18548 | design-to-code指标混工具链 → 固定React runtime+缺陷IR+多轮执行反馈，posttrain收益不稳 → 核反馈有效与奖励稀疏反证 | 2+1+2=5 |
| 18568 | 推理长输出memory-wall → capacity-for-bandwidth chiplet和解耦管线ISO-TDP模拟 → 核存储容量/带宽/能耗约束而非照录45x | 2+2+2=6 |
| 18571 | test-fix观测贫乏 → debugger子Agent及两层消融 → 核工具与委派收益是否分开 | 2+2+2=6 |
| 18582 | terminal reward难表达how → 语言到层级行为reward → 核spec编译和层级credit边界 | 2+1+2=5 |
| 18583 | judge多token输出使guardrail延迟不可控 → 共享SLM单token多LoRA任务head → 核determinism/质量/资源的成立条件 | 2+2+2=6 |
| 18584 | Adam对角几何忽略LoRA耦合 → validation梯度子空间投影 → 核selection预算控制及压缩成本 | 2+1+2=5 |
| 18600 | 跨模态推理混感知与规划 → map/table与多criteria拆分含multimodal负收益 → 核评价盲区与感知瓶颈 | 2+1+2=5 |
| 18613 | reranker比较混retrieval → 同8-document证据池/345cluster → 核selection budget与冗余的模型差异 | 2+1+2=5 |
| 18628 | task continual更新遗忘 → weight-field区域anchor锁承诺 → 核有限anchor是否真保证非干扰，零遗忘不先采用 | 2+2+2=6 |
| 18633 | 私有合成raw-access/保真矛盾 → DP近邻vote给PPO reward → 核隐私预算/奖励访问与utility对照 | 2+2+2=6 |
| 18639 | JEPA视觉slow-feature干扰latent规划 → bisimulation等价约束+背景控制 → 核control-relevant latent与尺寸/鲁棒性 | 2+1+2=5 |
| 18645 | 全序列encode与问题无关 → controller选择segment+reasoner层级RL → 核信息选择控制和额外预算 | 2+1+2=5 |
| 18647 | fixed噪声分布在modality shift失效 → I-MMSE entropy-rate在线schedule且固定objective/weight → 核采样分配与目标不混改 | 2+2+2=6 |
| 18649 | trajectory低秩误推weight可压缩 → 3尺度/5WD下跨矩阵SVD vs轨迹PCA → 区分学习方向低维与参数矩阵低秩 | 2+1+2=5 |

代表性排除（已完整读题摘）：18445是网页dark pattern检测/法律合规场景而非模型或Agent执行机制；18456以既有冗余安全原理类比实验室case，没有新控制/联合错误实测，不重引暂缓科学应用；18468 tokenizer阿拉伯膨胀局部测量加哲学解释，未提供超越已知分词长度/公平成本约束的机制，attention/维度坍塌归因题摘仅主张；18483访谈red-team风险观念，不提供可修正模型系统设计的具体新控制/失败机制；18495 relational聚合再off-the-shelf tabular ICL的领域prediction recipe，非当前模型训练/推理主线机制；18518内容平台prevalence sampling，LLM只是标签器，不是模型/Agent评估证据。18533准入仅局部身份恢复/控制，不把phonestheme解释或zero contamination宣传当证明。

首批非作者实际准入校准：root已读33项完整题摘与8代表性排除；33潜力入口基本通过，但不授日期或Evidence。18449的4分允许在身份/日期核实后关闭。两项排除理由撤回并定点重开：18511本身是LLM优化Agent，不能因目标程序不是LLM kernel而排除，补读一次intent/refine/realize控制是否新增验证边界；18581是允许的学习理论/小模型入口，不能因toy或未桥LLM而排除，补读stress/two-timescale是否改变更新条件而非换名目标。18450/18494仅核定理必要假设及中心桥，不遍历全proof。

日期恢复与证据审阅后可因具体新证据改判；不能因深审数量改分或缩池。

### 两项核心补读的准入修正

- 18511：精确v1 §3.1～3.3、§4.5已读；intent是有序区域变换行动，按pass描述匹配并静态提取`getResult`分析依赖，实际运行LLVM分析将约束输入refine/realize，非只有plan/refine改名；§4.5分别去refine与去analysis，90.5%→77%组合correctness、2.660×→1.122×去refine对照提供可检验贡献。改为潜力准入2+2+2=6；只保留“计划行动决定环境分析观测”及正确性/速度非等价，不宣称形式全程序证明。Submitted 02/19早于本窗必要下界；日期未证实，不授确定候选，留精确dated公告/snapshot缺口，不继续无关全文。
- 18581：精确v1 §IV.3～IV.8、V已读；stress指数平滑、on/off迟滞、有限commit/refractory、早abort/force-rearm实际决定何时进行covariance塑性更新，fixed spectral radius防目标缩零；continuous-plasticity保留其余组件对照支持“事件更新形成分段而非持续漂移”的局部机制，不是声称不优化就必然可学习，也不把homeostasis叫学习证明。改为潜力准入2+1+2=5。必要审阅继续核对照/参数和适用边界；任何open-ended intelligence与learnability普遍保证均不采用。HTML正文署August24,2026而页面标v1需身份/版本定点核，不能先把该正文授2月首次版本证据。
