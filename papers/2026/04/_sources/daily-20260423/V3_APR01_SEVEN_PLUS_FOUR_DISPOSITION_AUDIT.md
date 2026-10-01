# Apr23 有限处置复核：七项与四项

非作者 apr01；只核具名采用/保证，不核本日来源、日期、全部材料或dayGate；不改Books。未完成项不因此文件存在获得PASS。

## 已实际核的三项中心保证

- **19795 Prism：6纠错深入、窄争议通过。** 已重新读官方exact-v1 §3.4 Eq8–12与§3.5 Eq13–15。Eq9明确weighted fitness又除memory数量，两memory f=.8/κ相同→fbar=.4；λ=.1/μ=.01使κdot=.3κ+.01，正confidence没有有限fixed point，符合原取值范围。只反驳该打印系统Theorem3.3无条件收敛，不否定所有memory操作/经验。§3.5仅被用strategy收到反馈，而直接引用full-information Hedge，需补bandit estimator/反馈假设，不能代入regret。重开修公式/充分条件即可，不需整版历史。
- **20193 edge safety：6保护深入、限定争议通过。** 已实际重开§4.2/4.3原文，作者确把10000次profiling的观测上界称WCET，并据双节点不停机称ISO Category3持续安全。Sensor Fault2010.45ms、Heartbeat51.87ms与40s重启不被perception平均25ms覆盖；没有对应完整故障/actuator路径和common-cause qualification材料，不能采用上述保证。不是证明机器实际不安全，不把所有工程分支否定；请求只限拟采用保护范围的独立资格/时序或作者收窄。
- **19792 OpenCLAW-P2P：6保证纠错深入、窄争议通过。** 已实际重开exact-v1 §12.2 Theorem12.1 Eq13；norm内积上界只约束logit，不给normalized mass/输出误差。q=0、各value相同非零时，logits全0而full attention仍返回该value，θ>0会按文字规则删所有块；安全旁路结论缺mass/output桥。只隔离这条优化保证，不反驳Cauchy–Schwarz本身或声明其Lean对象内容已审。版本题名必须沿作者已实际核的v1 v6.0，不能用raw v7数学修正题名。

## 追加四项实际必要处置

- **19782：5分标准仅报告通过。** 实际重开官方 v1 §3.4 的 SCF：先保留模型在文本条件答对的问题，再在同题输入冲突语音，因而 EAR 对应的是这个条件化子集，不是全部问题上的语音理解准确率。有限冲突协议值得报告，但不能把文本正确子集上的退化写成通用听觉能力或唯一因果；不提出新的 Books 改动。
- **19998：6分标准仅报告通过。** 实际读 §2.1–2.4 与 §3：AC anchor 可以含噪声、减权处理 blocker；exact/partial/related 匹配和 FDR 中“accepted blocker 为 operational zero”均依赖官方 verdict，并不构成技术真值。48篇、670 concerns、79 decisive 与170个 resolved 中40项不在PDF，明确是有限 review-paper support。camera-ready accepted 与原 rejected 稿的版本支持不同，severity extraction/default-reject 也可能改变分母；不采用“concern 被处理就证明结论正确”，不强写 Books。
- **20158：具体前分母关闭通过。** 实际读 §3.2/§4.1–4.4：不可变 log 上单一 projection、预算/seed 固定与中间状态 pin 是已有 replay 机制的具体 retrofit。作者自己承认 stateful 场景需 logs、namespace 和状态约束；deterministic-backend 的纯函数命题不能提升为 temperature=0 下所有 live Agent 字节级复现。未给出足以改变项目已有 replay/状态身份边界的独立结果，关闭不是因为方法有现成 owner 或没有新架构。
- **19936：具体前分母关闭通过。** 实际读 §IV-A–C/§V：ResNet18/CIFAR 的固定30k样本支持、augmentation/early-stop 与 shadow-config 变化下的 train–test gap/MIA 关联，是局部 operating point；1000模型不自动给隐私资格、普遍 attacker 上限或新的可迁移识别条件。所测复杂 augmentation 的关联不能推广为攻击者通常无法改善。关闭依据为未超出已有泛化差距与攻击支持条件的局部证据，不是因小模型或非LLM而拒绝。

以上四项在本轮实际打开必要原文，未复现实验、未读无关附件；与前三项合计七项有限处置通过，不等于日级 Gate。

## 末四项必要评价对读

- **20244 HPD：5标准仅报告通过。** 重新读[官方v1](https://arxiv.org/html/2604.20244v1)§4.2 Eq11–15及§5.2，并复用此前未变方法定位。student token来自固定offline prefix，不能称完整student trajectory on-policy；非expert token的负权重与expert补权是具体有限实现。2k steps/batch256的personalization评价不等所有训练预算或最终效用普遍占优，保留受限operating point，不制造新的Books长期保证。
- **20246 Cortex2：6标准仅报告通过。** 实际重开[官方v1](https://arxiv.org/html/2604.20246v1)§3.2–3.3、§5.1–5.2：冻结PRO由真实执行轨迹训练、在想象latent上评分，推理I固定1；同latent space不证明reward transfer可靠。200 GPU hours是任务训练比较，未计预训练/部署数据总成本；human intervention从最后可恢复状态继续，不等于episode reset。rollout预算k=2及30Hz条件明确，仅保此受限组合和评价，不采用普适安全/自治保证。
- **20267 ATIR：5标准仅报告通过。** 实际重开[官方v1](https://arxiv.org/html/2604.20267v1)§5.4/Table4–7并复用已核selector方法。WER .0281仍不能排除ASR影响，同retriever换source text实际改善；selector对pooling和interleaving shuffle有有限控制证据，因此不能单凭组件成熟关闭。16.8ms是query embedding（文本路线含ASR），不包括完整检索/回答SLO；保留局部可迁移表示取舍但不强写Books。
- **20300 FSFM：具体前分母关闭通过。** 实际重开[官方v1](https://arxiv.org/html/2604.20300v1)§3.2/§4.4/Table2–3：importance/decay/capacity pruning与风险分类的成熟组合，未提供新可执行保护边界。预定义dangerous类别零retention不是未知攻击零风险，sensitive与important实际也丢失；不能采用perfect security或Pareto-optimal宣传。具体关闭这些贡献主张，不因Memory主题或现章owner存在而关闭。

本文件十一项有限必要处置已完成；没有签署日期、整日来源、Books实际写入或日级Gate。无新增Books请求，未复现实验；未核无关附件或完整版本史。

### 本轮恢复核对

恢复时已核实该文件与 `V3_APR01_THREE_ONLY_20244_20267.md` 的具名实际审阅记录存在；这些未变结果直接复用，不另建同范围平行审计。19782 的模型数须限定 Tables2–3 五模型，而摘要 six 不混成同一实测分母；19792 原版题名继续用实际 v1 的 v6.0。19936 中相同 test accuracy/loss gap 下 MIA 仍可不同的负面结果保留，不把低泛化差距等同低 membership risk；本结论仍只关闭新的项目贡献，不否定该局部实证。
