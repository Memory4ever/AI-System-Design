# Apr21 实际 Books 写后复核

复核者：root（非报告作者）；日期：2026-09-27。复用 apr02 有效、未变的精确 v1 来源→owner 审阅，实际顺读正文及相邻交接；不是实验复现或整日验收。

## 首批五项

- **16481 / Ch72**：实际正文区分 projector 扰动与恢复模块、模块移除与干净资产恢复；额外恢复训练、retained utility、不完全擦除及资产版本责任在附近。与前面曲率近似和后面拒答/参数擦除两轴相接，没有宣称 tamper-proof 或永久删除。通过。
- **16968 / Ch72**：实际正文把固定 backbone 上良性外部经验的行为回归从 provenance 治理中分出，与前面的 sleeper channel、后面的历史行为不拥有当前授权相接。启用/停用、读取量、执行/拒绝与utility分别验收；归因不证明因果、等长度 system instruction 仍有混杂、ASR 非事故率均保留。通过。
- **17210 / Ch72**：局部拒绝 token logits 的平方锚、额外 base forward 与模板/tokenizer/权重 identity 实际入正文；局部坐标不固定完整 softmax 更不保证序列拒答，明确为对象边界推理。与 attribution 路线是替代约束分支，独立 safety/utility Gate 和 KL/数据/小更新回退保留。通过。
- **17215 / Ch72**：实际正文区分 loss 预筛→逐样本 norm→中位邻域支持选择与 clipping 改幅度，未把 norm 当危害或安全方向识别。forward/求导成本、稀有切片漏失、比例非单调与连续任务边界就近；接续前面的输出锚且不覆盖旧数据支持/clipping路径。通过。
- **17237 / Ch76**：实际正文把监督 heads/attention 权重读出/截断层作为联合排序 artifact，准确区分无排序 decode 与无 attention、局部读出与完整模型答案。211 query 不等免费计算、训练及attention materialization、窗口不完全同配与不利slice保留；Packing 引句和列表连续未被插断。通过。

五项带 family 身份的机制实际存在于正文而非只有 Review notes，可以记真实整合。尚未验收其余本日候选、来源与日级 Gate，不据本批声称 Apr21 Complete。

## 第二批五项

仍复用 apr02 对上述精确版本的有效必要源核验，root 实际顺读本批正文与前后段落。

- **16656 / Ch11**：在联合词表/checkpoint迁移中实际补入 item 可组合性筛选与 hidden mapping 初始化；不将表示读出当固定词义。added-item 优先匹配可能增加 token 数、实际执行路径/质量/原语言回归与成本、旧 vocabulary/LAPT 回退保留；与前一 alignment 初始化和后续 fertility 论证衔接。通过。
- **16972 / Ch33**：实际区分过滤零优势组的学习/补采责任与已掌握行为保持，所采 token hinge 只是 drift 惩罚不保证未来正确。全对分支与零分母、共同 checker 错误、难度重加权和取消 filter 的分布/成本混杂、14B反向切片在附近，与 DYPO 和普通 Dynamic Sampling 共存。通过。
- **16918 / Ch33**：实际区分 priority 寿命/重算、buffer 非均匀采样纠正与 action policy ratio，未给年龄或 ESS 赋予真值/状态支持保证。FreshPER 无 buffer IS 与 Standard PER 有 IS 的对照差异、失败衰减尺度及重算/均匀/fresh-only 回退保留，接续 replay 的成本与历史相关性主线。通过。
- **16864 / Ch45**：实际 dense/nonzero/metadata pools 与 signed map、稀疏首 operand、online softmax、Prefill→Decode再压缩和阶段身份完整。重排/metadata/encoding成本、模型/K/V敏感性及质量回归、L40S有限范围与FullKV共存均在正文，Ch49只是kernel handoff。通过。
- **16883 / Ch45**：实际区分本步历史KV跳读/零更新与永久 eviction、驻留容量与读取预算；proxy和单次误差界不保证全生成。RTX PRO6000/bf16、质量下降、短上下文弱收益与repeat_kv混杂、完整读取回退保留；接续head稀疏分支且不把恢复性写成安全保证。通过。

第二批五项 actual write-after 通过，累计本文件十项；没有签日期、全来源或整日 Gate。

## 第三批四项：Ch66

复用 apr02 已完成且未变的四项精确 v1 来源审阅，实际顺读写入段及交接。

- **16916**：MCQ candidate admissibility、列表外拒绝与格式合规并未合并成安全保证；judge 共同偏差、最大 ASR 不是部署事故率及工程回退与论文实证的区分保留。通过。
- **16965**：物理 clock 换算、组件/接口/应用三层观测与因果 issue/commit 分开；两阶段不能撤销已产生的错误响应，GPU 与生产范围限制就近。通过。
- **16812**：冻结行为差分上的 report adapter 与自知/安全保证分开，base 身份、独立 holdout、hallucination/FPR、跨 family 成本及旧 scalar probe 分支实际存在。通过。
- **16587**：completed span 与视觉区域 mask 标签、异步线性 attention-feature probe 和有限相对关系准确入正文；正确回答条件选择、attention materialization、离线 mask 与队列成本保留，不把局部 speedup 外推为生成加速或 faithful causality。通过。

## 第四批四项：Ch21 / Ch23 / Ch24 / Ch29

复用 apr02 有效来源→owner 审阅，root 顺读实际新段及前后文。

- **17228 / Ch21**：full/cheap 分叉标签绑定 future policy，quality teacher 不等于 load auxiliary；标签构造成本、低预算反向结果与未证明唯一归因保留。与前后的负载稳定性主线衔接，未把所有 auxiliary 判有害。通过。
- **17087 / Ch23**：离线 gold-loss mask 搜索、监督 compressor 与线上无 gold selector 三阶段输入权责实际分开；训练/搜索成本、质量反向切片、dense 与静态 selector 回退保留。通过。
- **16514 / Ch24**：clean-prefix next-token teacher 与同 corrupted-state/同位置 diffusion anchor 区分，anchor 构造与多阶段蒸馏不免费；ChartQA 退步、预算未全匹配与 AR/小 block 共存边界明确。通过。
- **16423 / Ch29**：训练期 trait vector 对表示/梯度的干预与输入 prompt 控制面分开；单模型 LoRA 范围、prompt 失败不唯一证明解释机制、直接梯度干预的 coherence 风险与独立 trait/安全回归保留。通过。

本文件累计十八项实际写后通过；加上恢复时原有十项，Apr21 可以计 28 项实际整合。尚未验收最后五项、来源与整个日期，不写整日完成。

## 最后五项实际写后

仍复用 apr02 未变的必要来源核，root 实际重开以下正文及邻段；没有把作者的 proposed 标签当作写入证明。

- **16391 / Ch26**：action-free forward/inverse 预训练、固定 forward、丢弃 reconstruction decoder 与 action adapter 的交接均在机制正文；模块成功不越过 action/controller 验收，全模块训练非唯一梯度干扰因果、连续尝试与模块时延非单次成功/SLO保留。通过。
- **16880 / Ch36**：switch 进度反馈与 reduction offload 分层，额外 ECN 同普通 congestion 标记 OR、端侧 DCQCN 调节；proxy 不签 collective completion，模拟与双流原型范围、正常领先惩罚及普通路径回退保留。通过。
- **17198 / Ch49**：coiteration 访问成本而非坐标宽度决定分区，outer intersection 发现后的 remap/prefix 前提实际存在；数学所选成本界非 wall-clock，assembly/sort/reduction、反向 SpGEMM 及 vendor/dense 回退保留。通过。
- **16682 / Ch70**：降频→寿命→驻留 Context→eviction/recompute 的反馈与 admission 联动完整；最慢5%累计 token/s、录制回放、设备功率不冒充请求 tail/任务成功/整机目标能量。与现有频率曲线接续，Ch56仍拥有状态接纳。通过。
- **17180 / Ch81**：保留已有 COW/branch identity 分支，只细化创建量与活跃执行容量的差异；共享池/独立 compute 的预算与吞吐混杂明确。Live Fork标题在新增段之后，没有切断旧论证；timeout/采样/完成步骤限制及并发、回收、evaluator revision 保留。通过。

本文件累计23项真实写后通过，加恢复时原有10项，Apr21真实整合33项。普通 Books 写入0；这仍不替代候选冻结、其他处置及日级来源/日期 Gate。

## 最终日级复核（2026-09-27 18:47 北京时间）

复核者：root，非报告作者。实际重新读取当前研究/Report合同、每日来源组、正式报告§1～3和§5～6，以及已有来源/准入独立记录和本文件全部写后记录。原有精确版本、采用命题与独立证据未变化的逐组复核继续有效，不把作者最终表或机器校验当作来源阅读。最终146唯一家族为33整合、14已有覆盖、81仅报告、18窄争议；66深入、79标准、1争议，普通Books和证据待办均已收口。

否定侧在原有首批15项准入校准、最小消歧与具名安全/理论裁决之外，本次实际打开六项官方v1完整题摘：16625（kernel搜索中的失败记忆与局部/结构搜索组合）、16762（credential broker/非导出capability）、16694（rank proxy路由/steering）、16804（OR合成/verifiable RL课程）、16778（跨Agent文本经验库）、16498（NPU编译四阶段）。抽样按执行、保护行为、模型路由、训练、共享记忆和编译理由分层；它们直接相关，但所披露组合/局部结果没有建立报告当前需要保留的新有效性条件或重要设计反证，维持具体前分母关闭。不因成熟组件、窄任务、小模型或没有新runtime协议统一排除。其他已具名核验的强信号排除和纠错结果复用；本次六项抽查不是270完整题摘或1260宽身份的全量非作者阅读。

14源的实际历史停点及官方分页/artifact限制已逐项核对；GitHub两次403后的网页只含lastUpdated，不推造created事件或零更新。日期组合遵循实际公告槽/永久ID分配及单项processing邻界，submitted/Updated不独立当首发；更早正文、跨截点及withdrawn例外在§5隔离，不纳入确定候选。原始覆盖缺口和18个中心命题争议均不支持正面采用、Books或无遗漏保证，重开材料明确；这不是将Coverage缺口标作已证明。

33实际采用的source→owner及正文/邻段已通过有效非作者复核；14已有覆盖、81仅报告、18窄争议的必要依据由正式§4和具名分组审计承载。根任务再次检查正式终态与这些记录之间没有遗留普通提案、撤回selected或日期隔离项混入采用。31条旧Review notes已由作者按同family最小同步，未改变已核正文。格式validator实际通过。**日级语义验收通过**；作者同步正式完成状态及本段范围后再次执行scoped检查即可，不再为本次换版重复未变化证据。此验收不声称实验复现、全部研究目录恢复或全网零遗漏。
