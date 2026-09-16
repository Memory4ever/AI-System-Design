# 2026-05-15 V3 Fresh Non-author Final Gate Review

- 复核者：`fresh-nonauthor:may15-final-gate-20260915`
- 独立性：未参与 05-15 作者 V3 重建及 root 的 19 项 Books 写回。
- 复核时间：2026-09-15T19:04:29+08:00。
- 结论：**未通过；Daily 必须保持 Ongoing。** 分母、来源与 Evidence 数量闭合，但 Books 写后语义和当前正文台账均有可定位失败，不能把 validator 或 marker 存在替代语义 Gate。

## Gate 总览

| Gate | 结论 | 复核结果 |
| --- | --- | --- |
| 14 个 Daily sources | 通过 | README 的 13 个机构源加 arXiv 共 14 槽；各槽均有窗口终态。Seed Hand-in-the-Loop 与 `2605.15157v1` 合并为同一 Source Family，THEMol 在候选分母前关闭。 |
| Candidate denominator | 通过 | `679 = 95 retained + 584 pre-denominator closure`；95 与 584 集合内无重复，withdrawn=`0`。 |
| Evidence | 通过并规范 route | 作者冻结为 `95 = 59 deep + 36 standard`；Books conflict/confirmed gap 强制 override 后为 `95 = 66 deep + 29 standard = 93 HTML + 2 PDF fallback`。blocked=`0`，Materials Request=`0`；README 有 95 个候选行和 95 个 Evidence 小节。 |
| 作者冻结 Books 算术 | 仅证明旧 artifact 自洽 | `95 = 5 prior binding + 19 Integrate + 71 No Change` 在 `books-comparison-v3.json` 内部相加成立，但与当前 Books 正文不一致，不能作为最终分区。 |
| 19 项 root 写回位置 | 部分通过 | 19 个 canonical marker 各出现一次且均在本章 `Review notes` 前；`2605.15053` 的 marker 被另一个 Source Family block 隔开，不能唯一绑定其前置 TFGN 段落。 |
| 19 项 root 写回语义 | 未通过 | 13/19 通过，6/19 失败；失败项见下表及 root repair queue。 |
| 5 项 prior binding | 通过 | `2605.14005/14038/14175/14186/14220` 的 title-derived binding 各一组并位于正文；它们不是本轮新增写回。 |
| No Change / false-positive / false-negative challenge | 未通过 | 6 个当前正文 canonical binding 被错记为 No Change，1 个 No Change marker 孤悬，5 个空白 No Change 未被现有正文命题承载；另 4 个 No Change 可由具名现有命题维持。 |

## 19 项 Books 写后逐项结论

| arXiv | 结论 | 语义判断 |
| --- | --- | --- |
| `2605.13864` | 通过 | 保留手写 kernel 基线；lowering 只拥有 transformation proposal，编译/数值/性能回归提交；可移植性代价、未命中回退和 §5–§9 边界均明确。 |
| `2605.13915` | 通过 | 把 dequant bottleneck、activation range decomposition、版本化 controller/kernel 与数值误差、硬件适配、标准 dequant/high-precision fallback 串成一条链。 |
| `2605.13935` | 通过 | 区分 diffusion trajectory credit 与 outcome truth；覆盖 normalization、exploration、variance、GRPO/offline fallback 和 Appendix H 边界。 |
| `2605.13981` | **失败** | 生命周期分母正确，但只写“增加计量与摊销假设”，没有声明这些假设失效/上游成本不可得时的失败状态，也没有给出固定已部署 student 的 marginal serving-cost 共存/回退。 |
| `2605.14062` | 通过 | 完整生成后过滤是合理基线；in-flight filter 只拥有 early-stop proposal，最终质量 owner、误杀/漂移代价与 full-generation fallback 明确。 |
| `2605.14071` | 通过 | 离线 teacher trace 基线、distribution-ratio proposal、支持集/方差失败、clipping/online/ordinary-SFT fallback 与 exact-v1 边界完整。 |
| `2605.14163` | 通过 | committee 仅扩大 verifier coverage，不拥有 soundness；scheduler/selector/evidence owner、相关错误与单 verifier/abstain fallback 均明确。 |
| `2605.14212` | 通过 | multi-agent aggregation 的旧基线、角色/状态控制、分歧成本、失败升级与单 Agent fallback 均由正文承载。 |
| `2605.14249` | **失败；false-positive Integrate** | 新段仅重复 Ch70 已有“预测模型只排序 proposal、真实 workload/质量/SLO 决定部署、漂移时回退实测”的命题，没有新增持久状态或控制边界，应移除重复 binding 并改回 No Change。 |
| `2605.14483` | 通过 | agent 组合的 state/authority、通信成本、错误放大、单体/人工回退与实验边界明确。 |
| `2605.14514` | 通过 | defense interaction matrix、clean utility、failure attribution、组合冲突和 layered/reject fallback 完整。 |
| `2605.14591` | 通过；不是重复项 | 既有正文只定义 membership/memorization/extraction 的审计对象与一般校准；新增段引入“不重跑训练、以 observational study 代替 interventional rerun”的状态变化，并保留 propensity/support/threshold 失败与 shadow/canary fallback，因此是具体增量而非主题相似。 |
| `2605.14786` | **失败** | trace fingerprint 的 privacy owner、误报和最小化 fallback 已写出，但没有写 exact-v1 的 passive co-located site operator、单一 Midscene.js harness、14 个模型、四个 web environments、单任务转移弱与 open-set 不完美等 non-proof。 |
| `2605.15053` | **失败** | marker scope 不唯一；正文把 TFGN 写成已披露的“新旧任务读写梯度分量分解器”，而 exact-v1 只披露 internal overlay/capability-level mechanism，并明确无 replay、无 task ID/phase boundary、内部规格受 NDA 限制。 |
| `2605.15077` | 通过 | serial tool baseline、可取消 read-only speculation、authority/schema/version/permission checks、waste/stale/race 代价和 serial fallback 完整。 |
| `2605.15134` | 通过 | forecastability 与 accuracy 分离；sensor/action/evaluator owner、slice/calibration 失败、external verifier/conservative threshold 与作者设置边界明确。 |
| `2605.15138` | **失败** | artifact identity、量化后 removal/control survival 与 stop-release fallback 已写出，但缺少 clean utility、precision/recipe matrix、额外 PTQ 与 circuit-floor 优化成本的 trade-off。 |
| `2605.15152` | **失败** | detector proposal、量化后 regression 与高精度/拒绝 fallback 已写出，但缺 anomaly false positive、clean accuracy/precision/memory/calibration 成本，也未把证据收窄到作者所测 attack/quantizer/model。 |
| `2605.15172` | 通过 | positional trigger 相对 token/weight scan 的约束变化、matched probes、sensor-only authority、误报/因果失败、retrain/isolate/manual fallback 和受测攻击边界完整。 |

因此本轮 19 项为 `13 pass + 6 fail`。marker 唯一与位于 `Review notes` 前只通过结构检查，不抵消上述 6 个语义失败。

## False-positive 与 No Change 挑战

### 现有正文已 Applied，却被 artifact 记为 No Change

以下 6 项均有 canonical marker 和真实正文命题，必须机械改为 `Applied — current main-body binding verified`，不能继续占 71 个 No Change：

| arXiv | 当前正文命题 |
| --- | --- |
| `2605.14241` | Ch78“同功能 Provider 的选择属于运行时路由，不属于模型授权”：只在已授权的等价 Provider 集内按 live telemetry 路由，Router 不扩大权限；不等价/高风险时回退 allowlist 与静态绑定。 |
| `2605.14421` | Ch77“Provenance 必须进入 read、action 与 repair 路径”：冻结 source versions、typed derivation edges、claim 与 action justification closure；lineage 缺失/撤销时 fail closed。 |
| `2605.15051` | Ch48“Acceptance 不是独立常数，在线决策必须结算系统状态”：按 live load、emergent batch、draft/verify cost 与 acceptance estimate 决定 speculate/shorten/bypass。 |
| `2605.15079` | Ch27“元数据生成也必须是可治理的数据变换”：source snapshot 经 schema/profile/annotation 生成 typed Croissant/JSON-LD artifact，并保留 validator 与 manual override。 |
| `2605.15109` | Ch76“GraphRAG 的 Citation 必须绑定实际 Traversal”：冻结 graph revision、visited/supporting subgraph、claim citation 与 entailment check。 |
| `2605.15185` | Ch25“视觉逼真与三维一致性是两份不同证据”：把 perceptual evidence 与 multi-view/temporal geometry evidence 分开，并明确几何一致不等于 causal controllability。 |

### 现有命题不足，不能维持空白 No Change

以下 5 项的 `existing_proposition_excerpt` 为空，且定点搜索没有找到承载 adopted claim 的等价正文；应转为 Integrate 并由 root 写入唯一 owner：

- `2605.14305`：Ch24 只有一般 `Draft + exact verification`，没有“独立 token-wise clean posterior 产生 factorization error → prefix-conditioned exact factorization 保留依赖”的 target-distribution 命题。
- `2605.14368`：Ch24 没有“用 geometry proxy 选择 hidden interface，并以 diffusion bridge 替换下层、保留 transformer suffix/LM head”的 Locate-and-Replace 边界。
- `2605.14621`：Ch67 Monitoring 不是该 decoding mechanism 的 owner；现有视觉 hallucination sensor 也没有 shared-prefix、late-layer image masking、internal contrastive decoding 与 white-box/cache 开销命题，应重路由到 Ch23 的视觉证据写入/读取链。
- `2605.15041`：Ch78 有 tool necessity、schema gate 与历史反馈，但没有把历史 execution cases 压成 complexity/failure profiles，再分别校准 reasoning budget 与 schema-level reward 的机制。
- `2605.15157`：Ch26 有通用 deployment→intervention→update loop，但没有 takeover 时 hand pose 与 policy command mismatch、relative retargeting/arm residual shared control 以避免 gesture jump 的连续性合同。

### 可维持 No Change，但必须补具体正文命题

- `2605.15141`：Ch24 已有“few-step student 的 off-trajectory state 落在固定 anchor 之间会产生 truncation drift；连续/更密 state coverage 换训练与校准成本，失稳时回退更多 sampling steps”的命题。exact-v1 的 frame-wise 1–2 step/Causal CD 是该前沿的局部实现。
- `2605.15153`：Ch26“从模块化机器人到 VLA”与“World-action model”已区分 single VLA、joint future/action generation、共享 representation 与独立 execution authority；统一模型名和作者 benchmark 不改变该长期命题。
- `2605.15178`：Ch25“从单尺度预测到 Abstraction × Timescale Hierarchy”与“Pixels vs latent”已覆盖长视频把慢语义/快细节分层、效率与跨层 drift 的取舍；GDN/softmax、dual camera conditioning 与 refiner 是作者实现，不产生新的 owner/control contract。
- `2605.15190`：Ch24“Training / Inference mismatch”已明确 AR teacher forcing 看到正确前缀，而推理消费 self-generated history；synthetic correction 是否覆盖真实 rollout error 仍需验证。这正是 adopted claim 的长期命题。

`2605.15132` 仍可维持 No Change，但 Ch81 的 canonical marker 当前孤悬在 `2606.14672` latent-handoff block 之后、`Resource Lease` 之前，没有 APWA 正文；必须删除该孤悬 marker，不能用它制造虚假 Applied 状态。

完成上述确定性重分类后，目标 Books 分区应为：`95 = 11 Applied + 23 Integrate + 61 No Change`。其中 23 个 Integrate 包含原 19 中排除 `2605.14249` 后的 18 项，加上 5 个已确认 false-negative。root 已按队列应用返修；目标仍须由另一位 fresh reviewer 按当前正文复核，不能提前写成 Complete。

## 精确剩余 Gate

1. root 已按 `V3_ROOT_SEMANTIC_REPAIR_QUEUE_20260915.md` 应用 12 个有界 Books 动作。
2. README、`books-comparison-v3.json`、`exact-v1-locator-audit-v3.json`、root queue 与 checkpoint 已机械同步；当前分区为 11/23/61，route 为 66/29。
3. 唯一剩余 Gate：由未参与上述 root 修复的另一位 fresh non-author 只复核这 12 个 Books 动作、marker、7 个 deep override 及 95 项 disposition 集合对账；不得重开已通过的 13 个初始写回、5 个 prior binding、679 分母、95 Evidence、14 source slots 或邻日。

## 本轮机械检查

- `scripts/validate_research.py`：通过；只证明结构接口，不覆盖语义验收。
- JSON parse、`679=95+584`、作者冻结 `95=59+36`、当前规范 `95=66+29`、`95=93+2`、withdrawn/blocked/materials=`0`：复算通过。
- 当前 23 个 Integrate marker set 唯一并位于主 `## Review notes` 前；`2605.14249` 与 `2605.15132` 的旧 marker 已删除。该结构结果不替代另一 fresh reviewer 的语义验收。
- scoped `git diff --check`：通过；本轮报告/状态文件无行尾空白。
