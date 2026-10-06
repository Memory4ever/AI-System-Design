# Jan27 本窗增量准入

最新层级：原冻结60准入保持；OCR2因新恢复Jan27原repo首公开原件、完整题摘与resume_20260128_audit独立贡献裁决追加1，新增61/合计125。下文“拟准入/需澄清”是早期历史，不代表当前队列；全部61已完成本项必要证据与具体Books处置（中心争议不授正面Evidence），Source/PRE/实际POST有效范围见independent与README。18533采用offline LLM生成LCS/keywords与Pythonstyle runtime，不是旧表style judge；18731困难用户queryloss soft reweight不是minmax；其余有效原证据不删除。

每项完整题摘已实际读。精确题摘在 supplement-abs-ID-20261008.json；以下是拟处理命题，不是证据完成或 Books 决定。arXiv 下界 schedule/final-ID 与 created 上界联合；旧64原表不改。首7与四native root准入通过。jan28_review 分层核了明确关闭8项和需恢复3项；后续清单未以数量冻结。

## root 已首校准

18175 exact success-conditioning χ² conservative operator与proxy threshold alignment；18401 recurrent accumulated-key+covering candidate span+selected梯度；18510 memory-derived advantage的KL重加权；18486 demographic cue构念可交换性反证；18777 query层ranking metric与doc judge粒度对接PPI；18779 humanprefix条件on-policy+guided→unguided反侧；18795 prefix梯度mask/onpolicy续写+realizable objective consistency与backgeneralization。

Native四项：Keel decomposition of norm/residual/identity depth scaling；Seed Visual Generation生成过程作为空间/图形内部推理载体；Kimi PARL frozen workers/退火辅助奖励/CriticalSteps；M2-her NPC-side 100turn selfplay与online engagement/entropy earlystop边界。仅Jan27官方已公开说明支持的命题；后发PDF/Feb论文不倒写首次机制细节。

## 拟准入供独立校准（剩余分层）

| ID | 原约束 → 实际题摘增量 → 拟重新考虑选择 |
| --- | --- |
| 17172 | demographic前缀不仅直接影响输出，还能通过上下文动态放大bias；需分账conditioning强度与组差而非单prompt公平性 |
| 17471 | static patch生成不等continuous维护；两阶段patch搜索/去重与真实失败恢复 → AVR部署闭环条件 |
| 17705 | context语义shift难直接评价；pre/post context representation的动态ratio对比synonym/random edits → 编辑质量不能只下游分数 |
| 17676 | explicit prompt不等隐式intent；gaze表示选择与读任务个性化对照 → 模态表示/用户意图不能可互换 |
| 17910 | arbitrary KD update不一定well-defined/compositional；axiomatic adaptive distillation约束 → 可组合teacher/student policy条件 |
| 17915 | global LLM hypothesis隐含因果跳步；LLM只局部cause/symptom加deterministic belief graph/minimalfrontier → 搜索预算/证据职责 |
| 18067 | coding目标并非统一reward；functional correctness MCTS与performance optimization迭代不同 → 生成/优化的搜索控制选择 |
| 18089 | MoE参数容量不等执行代价；latent-space专家和硬件co-design → bandwidth/active容量约束 |
| 18129 | 本地语言/领域后训练可损通用分布；OPD/RL中的NWP保留项 → 专化与通用能力目标分账 |
| 18137 | 单步计划合理可隐藏全局约束失效；DeepPlanning长horizon多约束测量 → final plan评价不能局部逐步相加 |
| 18157 | 长历史视觉检索难关联scene/entity；entitygraph与跨视觉音频检索 → 事件身份/可回读条件 |
| 18125 | 用户privacy agency不止notice；不同UI控制改变disclosure/interception → 权限设计需测用户行为而非文本同意 |
| 18241 | test文件随代码变更不一定维护有效；pass/coverage/mutation联合TAM评价 → 代码维护成功与test可信性分离 |
| 18255 | replay通常被当抗遗忘；unstructured受益而fragile code反受损、OSWorthogonal safety → replay并非通用稳定性保障 |
| 18285 | 一刀history摘要丢意图/复用；U-Fold intent-aware retaining fullhistory工具compact → 当前任务intent与压缩资格分离 |
| 18302 | 高训练损失/entropy不能定位末层表示跳变；last-hidden angularjump/JREG → 训练稳定诊断与regularization对象 |
| 18321 | 多模态推理文本可能掩盖感知含糊/矛盾；先perceive后reason+consistency偏好 → 跨模态证据失配的训练目标 |
| 18345 | Agent trace mining只看成功outcome会丢failure-path；实测编码轨迹方法 → trace组织/挖掘是否改变判断需核心澄清 |
| 18418 | isolated coding instruction不等agent-native MT transitions；工具环境原生pretrain corpus → agent接口属于预训练分布 |
| 18467 | online researchAgentRL成本高；fullyoffline trajectory/SFT/DPO与性能预算对照 → offline支持与在线探索条件 |
| 18468 | 知识学习速度/泛化不只fact count；stochastic基线下latent knowledge预测acquisition/generalization/degradation → 数据关系如何决定可学性（不是AB已宣称ontology结构控制） |
| 18483 | 单attribute可控不等joint目标保持；humor/persuasion组合退化 → 属性控制需要interaction评价 |
| 18491 | binary safetylabel丢哪步/为何风险；trajectory何处/how/what诊断 → guardrail诊断不能冒充因果/safeallow |
| 18527 | longcontext retrieval专训不等unseen query robustness；任务专化与KV/OOd対照 → 长窗口效用边界 |
| 18533 | RLVR只verifiable事实覆盖不含expression；content verifier+style judge双轴 → reward可验证性与任务条件分账 |
| 18543 | imagegenerator toolquality与选择成本耦合；point/pairreflect jointRL与unseen tool → tool-use训练条件 |
| 18554 | 平均prompt compliance掩盖约束类型/位置/数量混合；MOSAIC组合切片 → 评测人口设计 |
| 18572 | 单persona probe不足以代表偏好；六persona cue组间/方差 → persona operationalization边界 |
| 18579 | 检索只embedding不保relations；FastInsight semantic+topological扩展/re-ranking → Graph检索采用预算与条件（原scope别名GraFine，exactv1身份优先） |
| 18588 | 常见entropy解释或parameter稳定解释不相同；parameter trajectory与生成退化机制理论 → 需核中心forward-KL/entropy含义，不能摘要授因果 |
| 18595 | deterministic symbolic solver缺commonsense仍不可答；神经符号迭代补信息/search → 哪层可提议事实与可验约束 |
| 18631 | 固定工具recipe不适配新工具；动态工具选择+GRPO/utility学习 → 工具变化的能力与评价条件 |
| 18681 | RL trajectory/discretization固定time有优化偏差；可学clock reparameterization+Gaussian objective → rollout时间与目标一致性 |
| 18692 | 大VLA训练规模不单独准入；LingBot latentdepth/codec与训练系统具体机制若存在 → 几何表示/吞吐条件待定点核心 |
| 18698 | 视频好看不代表地理知识/均衡；GAP attractivenessvslandmark对照 → generator质量与knowledge评价分离 |
| 18699 | continual预训练遗忘不只是新token比例；三机制及109B–400B规模声称 → 必要中心证据/模型身份核验 |
| 18702 | 普通数值float误差与LLM幻觉不相同；rational arithmetic AGI zeroerror大主张 → 必要证明，不能提前标签onlyreport |
| 18722 | 双回答同错时pairjudge无区分；privileged English参考辅助多语pair反馈 → evaluator能力条件 |
| 18730 | Constitutional反思通常改善安全说法需tail反侧；self critique修订的实际violation/cost → 定点安全可靠性条件 |
| 18731 | 一个global RM不代表fewshot用户；MAMLbase/linearweights与harduser minmax → 个性化RM适用边界 |
| 18734 | 自policy也可作特权teacher；额外context条件teacher与原student tokenKL → onpolicy数据与监督权限分离 |
| 18735 | decentralized多agent不只是广播；uncertainty assets+Thompson broker市场 → 通信/成本/激励条件 |
| 18751 | annotator仅非负信任无法描述反向一致偏差；negativevszero权重joint RM → identifiability/fliprecover须证明 |
| 18753 | data与reasoning hallucination风险不可同score解释；NTK decomposition/theory → 必要假设与实际误判边界 |
| 18760 | preference pairs之外human reasons/values constitution → human feedback表示与目标对齐评价 |
| 18790 | 数学task奖励不覆盖紧急危害响应；MortalMATH emergencypriority/latency150scenario → 安全与正确性竞争的evalslice |

## 具名有限准入澄清（不是关闭，也非外部终态）

17717 survey声称evaluation deficiencies，实际 §2.4/3.4/5.4/6.4/7.4需确认是具体评价盲区/反证还是“缺某项报告”；18415 uncertainty modeling未知且NAACL2025先公开身份，核必要机制与此前公开关系；18492 TFV+maskedentity两channel与sampling-only对照需核可靠性增量；18261 adaptive Fisher binarymask不同于EWC成熟softpenalty，需核差额；18393 visual OCR/audio双encoder+crossattention/audio distill条件；18771 dependency动作类型与memory/reward实际分责。六项精确HTML已恢复，下载不算审阅。

## 独立分层关闭已校准8项

18195 QualiRAG问题分解+四knowledge源相关检索无具体新的机制条件；18207 PaperSearchQA生医16M摘要/Search-R1领域配方，AIforScience暂缓且不以大数据规模准入；18642 FadeMem双层衰减/merge未给改变选择的新条件；18785 Dramamancer extendedabstract designtechniques未明确可保留机制；17292 risk taxonomy/层级映射+case无新增可靠性条件；18271 messy1446score extraction/prompt挑战无新测量盲区（2025发表线索不授Jan27首公开）；18346 portraitQA/human gap未明评价混杂或机制；18580 general continuouscontrol stateentropy未建立foundation/model-system直接关系。关闭均不以Books覆盖、局部/负面/工作量为理由；日期未知且无相关警示，不为关闭理由另查时刻。

SOAR18778仅原有效相同命题去重，不新增候选/首公开分数。后续撤回/纠错当前官方事件页若出现影响信号需重开受影响项。
