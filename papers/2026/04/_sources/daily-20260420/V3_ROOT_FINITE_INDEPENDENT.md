# Apr20 有限命题独立复核

复核者root，非日报作者。当前合同§7允许复用未变化的实际证据；这里检验本次处置所需的命题与反证，不声称重读全部附件、完成日期/日Gate或复现实验。采用范围均限报告，不授新的Books写入资格。

- [16146 exact-v1](https://arxiv.org/html/2604.16146v1)：实际§2、§3/Table1、§4.1。rejection使用proxy分布的信息，而proxy可以劣于base；Table1的Qwen CSQA在λ0为74.7，base76.9，dual KAD .3为81.3，不能由“confidence bet”推所有任务改善。OLMo p*74.1减p34.1是40pp，正文37.4不能合并；概率分散于合理token也不等知识不足。条件等价与dev选择阈值只支持局部替代分支，5标准仅报告通过，不成为安全alignment或端到端费用保证。
- [16158 exact-v1](https://arxiv.org/html/2604.16158v1)：实际§3.1～3.4/Eq2～5与§6。c=-.4，Eq3 H/c在H=c时1、H=0时0，而Eq4～5正向最大化；因此印刷式不支持“重新启用越强、reward越高”的直述。零mask不使一般CE为零；若T真是0/1下三角，Hadamard未来logit0也不是softmax禁止访问。后一点严格条件化，不断言未披露代码实际泄漏。48A100/200mask步的成本与GSM pass4 90→89.6退步保留；§6作者自己未验证faithfulness。6定点深入、中央语义争议隔离通过；保局部compression结果，精确重开只需reward/causal/zero-CE说明。
- [16171 exact-v1](https://arxiv.org/html/2604.16171v1)：实际§3与§4.2，核LoRA更新经JumpReLU选择支持再merge进入sharedbase，OA/BWT/FWT是不同观测而非同一“不遗忘”指标。作者已读取的warm-start/表/任务预算证据未变，不能从稀疏更新或平均OA推功能完全独立。5标准仅报告的窄目标与负BWT边界通过；没有签总体训练更省资源或无干扰保证。
- [16197 exact-v1](https://arxiv.org/html/2604.16197v1)：实际§2.4～2.5与D.2～D.3；topmass残差和sketch后L2归一化改变估计对象，不能把head原始无偏结论传到normalized完整gradient因果。D.2原印刷constant-1 variance上界错误：K=1、x=y=(1,1,1)，三独立公平sign穷举得Z=(Σs)^2，EZ=3、Var=12，大于||x||²||y||²=9；所有hash collision为1满足其假设。这只反驳该常数与依赖bound，不否定无偏或O(1/K)。6窄争议隔离通过，有限实现/规模观察仍保留；重开为交叉项修正与target明确，不要求所有训练复现。
- [16211 exact-v1](https://arxiv.org/html/2604.16211v1)：实际§4.1、4.3、4.5/Tables5～6，核supported type coverage、已支持type的precision、perceptual salience与整体speech quality分开。Table6 EN GeminiPro相对neutral自然度-.24、质量-.18而expressiveness+.05，不应概括必然质量提升；表外未知type不由有限45类coverage证明成功。作者原始协议记录未变、正式标题仍NVBench，局部多轴实证不升级blind安全控制或全系统公平因果排名。6标准仅报告通过。
- [16217 exact-v1](https://arxiv.org/html/2604.16217v1)：实际A Eq17～22与C Eq24～28。A的候选缺失不可由阈值补回这一子集下界成立；C的事件等价在q=∞时失效。N=1、α=.5、采样器在所有可交换样本上只产生错误答案，则其经验floor=.5满足宣称范围，q=∞；s≤q成立但集合内无正确答案，coverage0<.5。6窄争议隔离通过，不删LI排序与有限表、不声称交换性秩证明本身错误；只不采用有限candidate无条件coverage，需要fallback/定义或含sampling失败的正确风险界定才能重开。

以上六项有限处置复核通过；其中三项中心争议不作为Books/保证依据。其他未审候选、日期、来源与整日报验收不由本文件提前通过。

## 接续的五项有限处置

- [15719 exact-v1](https://arxiv.org/html/2604.15719v1)：实际读取 §4.4/Table3 和 §5，复用本日作者已核未变的方法/评价设置。Table3 的 N、choice/numeric 数量仍是 `[fill in]`，不能据其文字签匹配 cohort 或完整归因。NoHarness 同时取消 notes/harness 读写，未独立隔离 temporal feedback；provisional notes 与最终 resolution truth 的分责可以作为作者提出的局部分支保留，但不是已证实的普遍 promotion 方法。6分标准仅报告通过；不否定所有结果，也不补造缺失样本数。
- [15725 exact-v1](https://arxiv.org/html/2604.15725v1)：实际 §3、§5.1.5、§5.3 必要消融/迁移段和 §6，并实际顺读 Ch72 CoT Monitor 四命题、channel/parser 以及 attempt opportunity 段。answer equivalence 与 visible-reasoning harmfulness 是两个 judge 对象，final answer 未变不保证 surface 无害；GPT-4o 与三次取优的协议不提供单次真实危险概率或完整内部 computation 可见性。§6 防御是建议，不是验证后的消除保证。6分具体保护深入、仅该 sensor/outcome/authority 与预算命题已有覆盖通过；不声称 PRJA 全部机制已有覆盖，不新增攻击配方。
- [15741 exact-v1](https://arxiv.org/html/2604.15741v1)：实际 §2.3、§3.2 中必要 ablation/跨域结果与 Limitations。ordered all-token dispersion 加监督 sequence head 确实不同于只取末 token；Table2 的若干 Full 反退及 Table3 internal variance 的 OOD AUC60.56 高于 Full58.67，直接限制“组合恒优”和 model/task agnostic 宣传。监督 correctness labels、全层状态与 compute 仍是代价。5分标准仅报告通过，保留具体 sensor support 分支，不升级事实真值或无条件校准。
- [15756 exact-v1](https://arxiv.org/html/2604.15756v1)：实际 §3.1～3.4 和 §4 的 bank update/时间与存储必要对照。冻结 ID/classname/encoder、只训 OOD prefix，并以 pseudo-label 分组和离 ID 最远的有限 bank 调整 score，是局部适配分支。式4～5空子组/污染循环不能由高 confidence 自证，保全部 features 的对照更差也不证明所有流漂移稳健。单3090的11.40ms高于静态8.18ms，early stop8.36ms时FPR95又从12.46升14.21；TTL-V4→8MB另有收益/代价。5分标准仅报告通过，不采零成本或普遍 insensitive。
- [15760 exact-v1](https://arxiv.org/html/2604.15760v1)：实际 §7.5、§8 和 §10，复用已核评分/样本协议。作者明确无 recognition ablation、无 human baseline、single judge；gated failure 与其他 criteria 成功是关联，不是同题 cue 的配对因果验证。必须撤销初筛时“formal isolation 已经成立”的表述，但仍保 mandatory framing 与执行质量不同分母的受限证据。6分标准仅报告通过，不由 oracle routing 或 best-of-three 推生产收益。

以上五项必要非作者裁决通过，日期及日级来源/冻结分母仍由后续整体核验决定；未读工作继续执行，不因本批通过而宣称整日报完成。

## 接续的生成/多模态四项

- [16056 exact-v1](https://arxiv.org/html/2604.16056v1)：实际 §3.3～3.4、§4.2，并复用作者已核评价设置。LCS/ASR 将 source latent/condition 的匹配区间与新内容拼接，再用有限权重 mel guidance，确有处理编辑时长变化的分支；但该 latent-copy 不保证 waveform 逐样本保真。Table2 SpkSim/WDTW 改善同时 WER2.91 高于 base2.43、DNSMOS3.792 低于3.841；不照录“perfectly preserves identity”。6分标准仅报告通过，保对齐/ODE/边界与额外推理成本，不用成熟 latent-copy 原则冒签整篇 Existing。
- [16060 exact-v1](https://arxiv.org/html/2604.16060v1)：实际 §3 必要对照与 §4/Limitations，复用未变化的模型/任务表。NoImage++同时加入新正确选项，和原图任务不是单一视觉 cue 的纯因果对照；custom/native prompt、训练史及 toolcall 循环混杂必须保留。VisionG1/Qwen 与 GPT 若干正向切片限制 always-degrades 主张。6分标准仅报告通过，保有限视觉证据/提示格式反证，不扩大为所有文本 CoT 有害或 RL 造成普遍能力损伤。
- [16079 exact-v1](https://arxiv.org/html/2604.16079v1)：实际 §2、§3 Stability tests 及 pruning 对照，复用作者已核训练设置。相同随机 seed 下的 ArcFace 输出相似度不能证明内部 vectorfield/trajectory 相同；固定 VAE/同类人脸域也是条件。disjoint .69、异构 .55、换同域数据 .58 的下降，以及 Grad inverse/Loss 的 FID 反退均保留，pair SD 不是训练 seed CI。5分标准仅报告通过：有限映射稳定性证据有价值，但不成立全域无损剪枝或数据删除不影响模型。
- [16135 exact-v1](https://arxiv.org/html/2604.16135v1)：实际 §IV-E/TableII、§IV-G/TableIV，复用已核 structural mask 方法/限度。484 benchmark motions 同时纳入2652 evaluator 数据，80/10/10 分割未说明 benchmark 与训练是否 disjoint，因此不签独立真实动作 oracle。MotionDiffuse baseFID4.733 只低于 MDM base8.019，仍高于自身 adapter3.719；Transition 以接近 GT1.872 为目标，masking-step1.416 比 full1.381 更近，限制“所有指标退步”的正文断言。6分标准仅报告通过，保结构 mask 与晚期融合的局部生成分支，不升格物理控制或 training-free 全系统保证。

本四项采用范围与反证通过；没有授新 Books 写入，仍非日级验收。

## Fleet source→实际owner与literal

root实际读15379v1 §4.1、§5.1～5.3、§6.1～6.2和§6.4/Table4，并顺读Ch49 persistent/event tensor/per-SM queue→TaxBreak主干。partitioned-L2输出列分配、M-major局部复用与last-worker writeback/GPU event，是当前event-tensor段没有承载的具体硬件作用域分支；6分真实缺口深入采用通过，不由作者宣传升为通用加速。

提案两段的immutable descriptor、局部计数、必要writeback及global完成责任符合原文；不能写任意memory model免fence。Table4的HBM .82/.63与M-split1.20以及8/256常驻开销已限定。实际§6.2还有重要对照：batch64 Fleet M-tile18.61ms慢于vLLM约11～12ms，且作者归于未做K-split/attention优化；它对Mirage的改善不证明相对成熟serving engine或端到端普遍获益。literal需在原配置段加入这一负对照后才实写；其余采用范围通过。写后另核，未预支整合或日级完成。

### Fleet 实际写后

root实际顺读Ch49 event-tensor/per-SM queue、15379新增两段及后接TaxBreak/dispatch归因段，并核Review1947。新增正文91/93已落实硬件cache作用域→任务分配→分层完成责任，保必要writeback、不免fence与常驻开销；实际18.61ms对vLLM约11～12ms反退已在正文，和对Mirage局部改善明确分开。相邻论证通顺，未写普遍serving/SLO收益；非作者真实写后通过，可计本单篇整合，不替代整日日级Gate或实验复现。Review只同步本结果，不改其他正文。

## RPA / EasyRider source→actual owner与literal

15464：root实际§3.1.4、§3.3～3.4/3.6、§4.2后段/4.3～4.4，并顺读Ch49 Semantic Portability、SGLang-JAX与后接compiler-first。离线weight形状可能被XLA中间layout重排、静态capacity不决定有效ragged分布，这两个具体边界没有由原离散shape预编译充分表达。作者剩余已核且未变的packing/融合依据复用。两段采用通过：动态DMA不等静态计算无padding，mixed分布调优/重排尚未全实现，d128 MFU用50%调整分母，历史backend吞吐演进不归单kernel因果。6分真实缺口深入通过，未签production吞吐或SLO；写后另核。

15522：root实际§5.3、§6必要内外时间尺度、§7.1/7.4及§8，并顺读Ch70 Installed Power、前能耗proxy与后水耗dispatch。功率波形/频谱与总能耗分责、被动快滤波/辅助储能/慢SoC纠偏是当前容量预算未承载的分支。两段采用通过：400V/25A/10kW实物、normalized训练trace与两TitanX125M分开；inner-loop恢复不能传递为outer aging或全部任意trace验证，软件离线有headroom期限。$66k/$3.7M约1.78%，不是§8声称<1.25%，因此literal不采用这条推算成本比率。6分实际缺口深入，不采用未核全局QP保证或完整MW电网合规；写后另核。

### 15464 与 15522 实际写后有限复核

复核者 root，非本次两章写入作者。已重新打开两篇官方 exact-v1 的必要机制与评价入口，并顺读 Ch49 新两段及相邻 SGLang-JAX→compiler-first、Ch70 Installed Power→新两段→水耗调度的实际正文。**结论：两项均通过写后复核。** Ch49 清楚区分静态 capacity、ragged 有效长度、DMA 与仍有 padding 的 compute tile；compiler layout 可重排的风险以及 d=128 MFU 调整分母保留，未把 TPU kernel 指标冒充通用服务 SLO。Ch70 把 ramp-rate/频谱与总 energy、快滤波/储能与慢 SoC 恢复分开；400V/25A/10kW 与两 Titan X 训练 trace 是不同证据层，未采用 §8 相互矛盾的成本百分比或声称 MW 级长期电网合规。两章 Review notes 已同步真实写后状态，scoped diffcheck 通过。

这里只验收具名两项正文、相邻衔接和证据边界，不签 04/20 其它候选、来源日期、全日分母或日级 Gate；未复现实验。
