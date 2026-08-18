# 2026 Weekly Research Index

> Coverage: 2026-W01～2026-W33
> Last Updated: 2026-08-17
> Research Mode: Retrospective Backfill + Live Weekly

## Archive Contract

- Weekly 使用 ISO week-year 和完整 Monday～Sunday。
- 2026-W01 覆盖 2025-12-29～2026-01-04；跨年日期仍属于 `2026-W01`。
- 历史回填只生成 Weekly，不创建 Daily；事件日期直接记录在对应 Weekly。
- 早期回填曾生成的 2026-07-01、07-06、07-08、07-16、07-22 高分事件 Daily，已在确认
  关键证据完整进入 W27～W30 后清理；Live Daily 从 2026-07-27 起保留。
- Live Daily 每自然日生成；Live Weekly 只在 Sunday 完成当日流程后生成。
- Live Weekly 链接七份 Daily 并进行跨日去重、演进重建与 Books 决策；生成 Weekly 后不删除
  Live Daily。历史回填仍只生成完整 ISO Weekly，不补造 Daily。
- 2026-W31 已在 2026-08-02 Sunday 完成七份 Live Daily 聚合、跨日去重与 Books 决策；
  Coverage Window 为 2026-07-27～2026-08-02，没有生成 provisional Weekly。
- 2026-W33 于 2026-08-16 Sunday 生成初版，原 21 项 Full Source Review 与 16 Refine / 5 No Change
  disposition 保留。2026-08-17 discovery replay 发现遗漏的 8 月 14 日 arXiv 展示批次，现已补完四项
  Full Source Review，并建立 32 项 Discovery Review queue；W33 Discovery/Evidence Gate 与 correction
  Books Gate 均重新打开。
- W01～W30 共包含 93 个评分行：20 个 `25～30` 分、60 个 `20～24` 分和 13 个低于
  20 分的边界候选。80 个 retained rows 对应 79 个唯一事件；W27 的 Seed2.0 Model Card
  是同一事件的重复评分行。
- Forward repair status: `2026-W13～W32 Complete under explicit blocked-skip`。单向游标已经逐周到达
  最新完整 ISO week，所有 ordinary pending 清零，无法访问项逐项保留为 blocked/gap；这不等于
  all-history Evidence Gate 通过。全局状态仍为 `2026-W01～W32 Historical Evidence Gate Open / Books
  Gate Closed`，既有 Books 正文与 disposition 只作 provisional input，不删除或回滚。
- Baseline ledger: `30/30` ISO Weekly、`93` score rows、`92` unique Source Review packets、
  `20` 个 25～30 分、`60` 个 20～24 分、`13` 个低于 20 分的边界候选。当前重新核验
  screened → deduplicated → `>=20` retained → Source Review 的 discovery recall；冻结窗口仍截至
  2026-07-26，W31 只作为 Live Daily 对照，不参与历史改写。
- Historical research contract：`CODEX_HISTORICAL_RESEARCH_PROMPT.md` 已在仓库中，Live Weekly 与历史
  repair 分别遵守 Daily/History Gate；W33 不重启已结束的 W01～W30 forward sweep。
- 2026-08-08 checkpoint：W08 从旧版 2 项恢复为 23 项候选；22 项完成非模板化 Full Source Review，
  MapTrace 完成低分来源/日期/拒绝核验，故候选层为 `23/23`。历史 GitHub release/RFC 覆盖仍不完整，
  W08 不标记为 archive fully complete。2026-08-13 已完成 23/23 Books disposition 与周级独立 Review：
  18 项 Integrate/Refine、4 项 No Change、1 项 Weekly Only，更新 12 个 Stable Node owners；
  Source-Family Books Gate Complete，Archive Completion Gate Open。
- 2026-08-13 W09 Books checkpoint：62/62 candidates completed final dispositions after owner and adjacent-
  chapter review: 52 Refine, 6 No Change, 4 Weekly Only. Durable mechanisms were integrated across 24 Stable
  Node owners spanning representation/evidence, long-context state, multimodal generation/VLA, training data/
  optimization/distribution, inference execution/runtime/PD, platform evaluation/security, and Agent context/
  retrieval/memory/tool/planning/reflection/multi-agent/platform. Each owner group and the unified 62-row ledger
  passed independent reverse review. W09 Source-Family Books Gate is complete; Google Scholar/OpenAlex historical
  discovery coverage keeps only the Archive Completion Gate open.
- 2026-08-09 W05 checkpoint：原 3 项经两轮回扫扩展为 43 项。PaperBanana 与 Sweet Spot Learning
  最初受大文件 reader 限制暂记 blocked；本轮分别通过同一论文的公开全文渲染、arXiv HTML/PDF 可检索文本、
  官方项目页与作者 artifact 补齐 method、implementation、evaluation、ablation、limitations 和 appendix
  复核。W05 当前为 `43/43 Full Source Reviews`，Candidate Evidence Gate 已通过。2026-08-13 又完成
  43/43 逐项 Books disposition 与周级反向检查：28 项 Integrate/Refine、11 项 No Change、3 项 Weekly Only、
  1 项 Reject，共 refine 17 个 owner chapters；机器可复算 discovery census 仍未完成，所以 Archive Gate 保持 Open。
- 2026-08-13 W06 checkpoint：39 个新增候选中 38 项已有完整 Source Review；Claude Opus 4.6 的官方
  system-card PDF identity、目录与局部索引已核验，但全文 reader 因约 14 MB 文档大小失败，直接浏览器访问又被
  用户侧网站权限拒绝；没有绕过权限，也没有用 announcement/snippets 伪造全文阅读。按用户确认的
  blocked-skip 规则，Claude 独立保持 `Unverified / Blocked / No Books Change`，不再锁住其余 family。
  W06 的 41/41 scored rows 已完成最终 disposition：21 Integrate/Refine、15 No Change、4 Weekly Only、
  1 Unverified；15 个 Stable Node owner 已完成正文整合与周级反向检查。Source-Family Books Gate Complete，
  weekend/cross-index discovery 与 blocked source 使 Archive Gate 保持 Open。
- 2026-08-09 W07 checkpoint：49 个恢复候选中 48 项完成非模板化 Full Source Review。InternAgent-1.5
  因 22.8 MB PDF 超出直接 reader 而 blocked；本轮已通过同一 arXiv v1 的可检索原文 passages、目录与
  Appendix 范围、上海 AI Lab 发布页、官方仓库及 2 月开放的 solution-refinement artifact 补齐详细
  partial packet，并完成 Ch72～78 去重，但没有把片段重建冒充逐页全文阅读。W07 Candidate Evidence
  Gate 在该检查点为 `48/49 / Unverified Blocked 1`；历史 release/RFC 与 Scholar/OpenAlex discovery
  cross-check 也仍不完整。当时的 Discovery/Books 状态已由下方 2026-08-13 checkpoint 取代。
- 2026-08-12 W07 backlog checkpoint：SPEED-Bench 的 arXiv submission history 确认 v1 为
  2026-02-10；异常的 `2604.*` 编号前缀没有改写 event week。v1/v2 正文、Qualitative/Throughput
  splits、thin-client measurement flow、实验、Appendices、NVIDIA dataset 与 Ch43～45/62 邻接已完成
  审计。它证明 speculative-decoding evaluation 必须绑定 semantic distribution、ISL、concurrency、
  draft/target/engine/hardware identity，却没有超出 Ch44 已有设计结论，故为 `No Change — Already
  Covered / Experimental Evaluation Case`。W07 当前 49/49 accessible Full Source Reviews、1 个
  InternAgent blocked、0 ordinary pending；Candidate Review Checkpoint 按 blocked-skip 规则通过。
- 2026-08-13 W07 Books checkpoint：52/52 scored rows 已逐项给出最终 disposition：39 项
  Integrate/Refine、7 项 No Change、3 项 Emerging/Experimental、2 项 Weekly Only、1 项
  Unverified/Blocked。机制合并进 16 个 Stable Node owner，并完成章节相邻性、旧方案共存、证据边界与
  周报反向检查。W07 Source-Family Books Gate Complete；InternAgent full text 与历史 engineering/
  discovery recall gap 仅使 Archive Completion Gate 保持 Open。
- 2026-08-09 W09 evidence checkpoint（已由上方 2026-08-13 Books checkpoint 取代）：旧版 2 项经同周扫描、03-02～03-06 discovery-lag、DBLP 交叉索引与
  source-family first-public 去重，恢复为 62 个 in-window candidates；58 项完成非模板化 Full Source
  Review，4 项低分完成来源/日期/评分/拒绝核验，Replicate-and-Quantize、MINAR、CUPID 三项分别归回
  2024、2025-W39、2025-W51。最后补入的 Qwen3-Coder-Next 与 SkillNet 已完成论文、Appendix、官方
  model/repository 和相邻章节联读，故 Candidate Evidence Gate 为 `62/62 Passed`。Google Scholar/
  OpenAlex 历史窗口仍是 documented Discovery Limitation；该检查点当时尚未执行 Books Integration，
  当前最终状态以上方 2026-08-13 checkpoint 为准。
- 2026-08-09 checkpoint：W10 从 baseline 3 项恢复为 23 项并完成该 candidate set 的 23/23 Source
  Review 与 18/18 Books disposition；但 W11 discovery 随后又确认 11 个 first-public date 属于 W10 的
  漏项，因此 W10 Discovery/Evidence Gate 曾再次打开。原 Ch20、Ch23～25、Ch29、Ch39、Ch45、
  Ch62、Ch68、Ch72～73 写入保留，不代表新增候选已经审查或整合。新增候选现已完成 MLRA、
  DistriVoting、ProRes、BandPO、Sparse-BitNet、ATLAS、Terminal Coding Agents、AutoResearch-RL、HCAPO、
  Scaling Data Difficulty 与 MicroCoder-GRPO 十一份 Full Source Review；AutoResearch-RL 因 arXiv 管理员
  撤稿降级为 `Withdrawn / Disputed / Weekly Only`。W12 curation-lag audit 随后又恢复 1 个 03-07
  spillback；Nemotron 3 Super 也因 03-04 base-checkpoint 首发从 W16 回拨。2026-08-12 已完成最后一个
  spillback：Recursive Language Models Meet Uncertainty 的 31 页 sole-v1、全部实验/Appendix 与
  Ch22/72/76/62 邻接均已审计。W10 当前为 36/36 scored reviews、0 pending；SRLM 以 25/30 暂定
  Ch22 Experimental refine，且明确 K=8 并行只匹配 wall-clock、不匹配 calls/tokens/FLOPs。已记录候选
  Evidence queue 闭合，但 broader Discovery Gate 与全历史 Evidence Gate 继续打开。Nemotron 的 51 页报告、
  base/post-trained model cards、公开 artifacts 与 Ch20～22/24/29/41/45 已审计；其 28/30 暂定 Ch21
  Experimental refine，但不外推厂商 serving 倍率。
- 2026-08-13 W10 Books checkpoint：36/36 candidates 已完成最终 disposition：27 Refine、4 No Change、
  5 Weekly Only/Disputed。长期机制融入 15 个 Stable Node owners，覆盖 compressed-state shardability、
  selection distribution state、latent-coordinate MoE、programmatic Context interaction、depth-time residual
  activation、probability-aware trust region、hindsight/truncation credit、lazy tool schema 与 persistent execution。
  Sparse-BitNet artifact conflict 与 AutoResearch-RL withdrawal 没有进入正文；OpenDev 与 Scaling Data
  Difficulty 经章节级去重为 No Change。W10 Source-Family Books Gate Complete，Archive Completion Gate Open。
- W11 checkpoint：旧版 2 项已扩展为 55 个 scored in-window candidate families，并识别上述 11 个 W10
  spillbacks。RAGEN-2 已按官方 repository 的 2026-03-12 release 从 W15 回拨；其唯一 arXiv v1、全部
  appendices、project/repository、current artifact 与 Ch27～29/62 邻接完成 Full Source Review。当前 scored
  ledger 为 52/53 个 `20+` 候选完成 current-schema Full Source Review，Neural Thickets 与 SFT versus RL
  survey 完成低分
  来源/日期/拒绝核验。新增 EvoScientist 已完成 sole-v1、全部方法/实验/appendices、later artifact boundary
  与 Ch73/77/76/62 邻接审计；其长期机制已由现有 Memory/Workflow/Evaluation 章节覆盖，故为
  `No Change — Already Covered / Experimental Case`。MEMO 的 current-v2、v1/v2 history、算法、全部
  evaluation/ablations/appendices、五-commit official repository 与 Ch73/62/77/78 邻接也已审计；它以
  25/30 暂定 Ch73 Experimental refine，增加 retention、fresh exploration 与 seed-preserving replay 的耦合，
  但不外推五个 text-game benchmark。Groundsource 的 preprint metadata、Google Research 技术长文与
  dataset record 已核验，但 EarthArXiv full paper 受站点校验及用户侧浏览器权限阻塞，故保持
  `Unverified / Blocked` backlog，并按用户确认的 blocked-skip 规则不再阻塞前向审计。RAGEN-2 暂定 Ch29 Experimental refine，但 MI 是 batch/scorer-dependent proxy、
  RV filtering 对原 objective 有 bias 且会损失 prompt coverage，故不保存 headline。W12 curation-lag audit
  共恢复 28 个 03-09～03-15 spillbacks；EvoScientist、MEMO、Reasoning as Compression、Deep Tabular
  Research、FinToolBench、LookaheadKV、UCIP、One-Eval、LMEB、Video Streaming Thinking、daVinci-Env /
  OpenSWE、MM-CondChain、ReBalance 与 Expert Threshold Routing 已完成，FineRMoE
  已按 2025 首发路由回历史 backlog；Safe Web Agent Learning 因无法解析唯一 primary identity 保持 unscored
  blocked；HomeSafe-Bench 与 Think While Watching 因无 HTML 且官方 PDF 被用户浏览器权限阻止，保持未评分
  `Unverified / Blocked Full Text`；BAVT 与 EnterpriseOps-Gym 已完成全文、实验/附录、official artifact
  boundary 与 owner/adjacent-chapter 审计，前者暂定 Ch75 Experimental refine，后者为 Ch62 `No Change /
  Experimental Evaluation Case`；EvoClaw / SWE-Milestone 的 v1/current revision、完整论文、artifact 与
  Ch62/77/80 去重审计也已完成，结论为 Ch62 `No Change / Experimental Evaluation Case`；TERMINATOR 因
  official PDF text不可读保持未评分 blocked；GradMem 完成 sole-v1、全部 appendices、官方实现和 Ch22/39/73
  邻接审计，暂定 Ch22 Experimental refine；SFT versus RL survey 完成全文证据类型核验后以 19/30 保留为
  Weekly-only secondary synthesis。AI Can Learn Scientific Taste、AgentProcessBench、V-JEPA 2.1 与 KServe
  v0.17.0 也已完成 primary-source、revision/artifact 与相邻章节审计，分别归为 Ch27 No Change、Ch62
  provisional refine、Ch5 provisional refine 与 Ch49/57 No Change。ordinary pending 已清零；五个 blocked
  items 保留 backlog，W11 forward candidate checkpoint 按 blocked-skip 规则通过。LookaheadKV
  的 sole-v1、官方实现、
  效率合同与 Ch39/41/50 邻接审计支持暂定 Ch41 Experimental refine；UCIP 的 current-v4、公开结果 artifact、
  adversarial/scaling failures 与 Ch62/68 邻接审计只支持 `No Change / Experimental Evaluation Case`；One-Eval
  的 sole-v1、official repository、planning evaluation contract 与 Ch61～63/76～78 邻接审计只支持
  `No Change / Experimental System Case`；LMEB 暂定 Ch73 Experimental refine，Video Streaming Thinking
  暂定 Ch71 Experimental integrate；daVinci-Env / OpenSWE 暂定 Ch23 Experimental refine，MM-CondChain
  暂定 Ch62 Experimental refine。W11 Evidence Gate
  打开，Books Integration 尚未开始。
- 2026-08-09 W12 discovery/source-review checkpoint：旧版 3 项扩展为 49 个 in-window candidate families；48 项
  评分 `>=20`，Astrolabe 在来源复核后为 19/30。推荐流按 arXiv v1 first-public date 重新归周，并识别出一批
  W10/W11 spillbacks，避免用 03-16～03-24 的推荐日期制造 W12 伪事件。Attention Residuals 已完成
  21 页论文、Appendix、官方仓库与 Ch16～18 的 Source Review，owner 从 Ch15 更正为 Ch17；MoDA
  也已完成 18 页论文、Triton artifact 与 Ch14～19 的审计。两者被确认是 selective depth retrieval
  的平行分支，而非先后替代。OpenSeeker、POLCA、PokeAgent Challenge 与 Code-A1 也已完成全文、
  关键 Appendix、官方 artifacts 和章节联读：OpenSeeker owner 更正为 Ch72，POLCA 更正为 Ch77，
  PokeAgent 保持 Ch62，Code-A1 收敛到 Ch29。HorizonMath、MiroThinker-1.7/H1、Online
  Experiential Learning 与 TRUST-SQL 也完成同级审计；owner 分别为 Ch62、Ch76、Ch73、Ch29。
  Efficient Reasoning on the Edge、SWE-Skills-Bench、FlashSampling 与 MetaClaw 也已完成全文、
  revision、可访问官方 artifact 与章节邻接审计；owner 分别从 Ch42/45、Ch62/77、Ch44、Ch73/78
  收敛为 Ch26、Ch80、Ch20、Ch80。FlashSampling 的 v1 约 19% headline 已由 v2 的 10% 摘要
  supersede，历史与当前 revision 分开记录。Complementary RL、BenchPreS、AdaMem 与 VTC-Bench
  现也完成全文、appendix、可访问 artifact 与章节邻接审计；owner 分别收敛为 Ch29、Ch73、Ch73、
  Ch62。前三项分别是新机制、新机制与既有论证精化候选；VTC-Bench 因长期观点已由 Ch62/Ch74
  覆盖而归为 `No Change`，其 32/35 tools 元数据冲突保留为 disputed。Efficient Exploration、training-free
  MTP、RAMP 与 PRISM 也已完成全文、appendix、artifact 状态和章节邻接审计；owner 分别收敛为 Ch27、
  Ch44、Ch45、Ch24。前两项与 PRISM 为 Historical Books Gate 后的 integrate/refine 候选，RAMP 因无
  artifact、contract 内部不一致且无直接 runtime 复核而保持 `Emerging / Experimental`。AI Scientist、
  Nemotron-Cascade 2、Memento-Skills 与 AndroTMem 也完成 full-paper、artifact 与章节邻接审计；owner
  分别收敛为 Ch25、Ch29、Ch80、Ch73，前两项为新机制候选，后两项为既有论证精化。当前总计
  ProRL Agent、Reasoning over Mathematical Objects、Hyperagents 与 λ-RLM 也完成 full-paper、关键
  appendix、公开 artifact 与章节邻接审计；owner 分别收敛为 Ch29、Ch27、Ch77、Ch77。前两项为
  新机制候选，后两项精化 evaluator-driven search 与 deterministic workflow spine。Subgoal-driven
  Agents、LoopRPT、BEAVER 与 Reintroducing Markov States 也完成 full-paper、appendix、evaluation
  contract 与章节邻接审计；owner 分别收敛为 Ch75、Ch24、Ch71、Ch29。当前总计
  AgentDS、OpenResearcher、BubbleRAG 与 HopChain 也完成 full-paper、revision、evaluation contract
  与章节邻接审计；owner 分别收敛为 Ch62、Ch23、Ch72、Ch23。AgentDS 是章节级 `No Change`，
  后三项为 Historical Books Gate 后的 integrate/refine 候选。官方/Infra 收口又恢复并审计 Vera Rubin、
  DSX Air、Dynamo v1.0.1/v1.1.0-dev.1、Kubeflow Distribution 26.03、Trainer v2.2 与 SDK v0.4.0；
  KServe v0.17 归回 W11，PyTorch 2.11 归入 W13，JAX 页面时间戳不替代 changelog date。当前
  48/48 项 `20+` Full Source Review 与 1/1 low-score verification 均完成，W12 Discovery/Evidence
  Gates 通过。新增的 vLLM expert-weight tiering family 按 3 月 16 日 open PR 归属 W12；3 月 26 日
  RFC 只作为 W13 architecture follow-up。Vera Rubin、Trainer v2.2 与该 vLLM family 是 provisional
  refine candidates；DSX Air 只保留产品事实，
  Dynamo、Kubeflow Distribution 与 SDK 为章节级 `No Change`。全历史 Books Gate 仍关闭，下一检查点
  自动进入 W13。
- 2026-08-09 W13 checkpoint：旧版 3 个 score rows 经论文、官方 release、工程来源与 source-family
  normalization 恢复为 26 个 scored candidate families。22 项达到 `20+`，现已全部完成非模板化
  Full Source Review；DSPA 覆盖双 SAE、
  conditional map、token-active intervention、理论与 evaluation/limitations，DRTriton 覆盖 v1/v2、
  CSP-DAG、verifier、curriculum DRPO、compositional search、hardware/overhead 与 revision boundary。
  `TRITON_MLA_SPARSE` 又补出 build/dispatch/indexer/attention/graph 的 portability failure chain，并保持
  open-PR / Experimental 边界。另外 4 项为
  低分或跨周 artifact 边界；Cross-Context Verification 只在 9 个 SWE-bench problem、单一模型的
  contract 下成立，Astrolabe code release 归为 W12 paper 的 artifact follow-up。W13 Candidate
  Evidence Gate 因 discovery recall 未闭合而保持打开，Historical Books Gate 继续关闭；
  同时已经重开 W14，不再等待逐周人工提醒。
- 2026-08-12 W13 spillback-intake correction：W14 curation-lag ledger 中有 20 个 first-public date 位于
  2026-03-23～03-29 的候选，现已逐项写回 W13 `Audit Pending` 队列；因此 26 scored / 22 reviewed 只描述
  旧 recorded set，不能再支持周级完成声明。Sommelier、SEAR、FIPO 的 provisional date 是 3 月 20 日，
  已路由到 W12 backlog，不计作 W13 候选。后续已完成 `Lie to Me`、MedOpenClaw 与 Composer 2 三项
  primary-source review；ClawKeeper 因 primary text 无法访问而转入 unscored blocked backlog。Hybrid Memory
  随后完成 paper、supplement、project、repository 与相邻章节审计，暂定 Ch10 Experimental refinement。
  Trace2Skill 又完成 v1 全文、实验/ablation/limitations、后续 revision、official spreadsheet artifact 与
  Ch73/76/77/80 邻接审计，暂定 Ch80 Experimental refinement。它把 trajectory evidence 编译为
  declarative Skill artifact，但不替代 sequential edit、retrieval memory 或 human authoring；work-in-progress、
  partial artifact、same-model correlated errors、validation selection 与未解决的 patch/section attribution 均
  保持为证据边界。Natural-Language Agent Harnesses 随后完成 v1 全文、RQ1～RQ3、module/migration
  ablations、limitations、appendices、v2 revision、post-window LinguaClaw artifact 与 Ch77/78/80/62 邻接
  审计，成为 28/30 provisional Ch77 refinement。它只把 natural language 赋予 harness pattern layer；code
  仍拥有 deterministic enforcement，small single-seed benchmark、runtime contamination、prompt confound 与
  changed action substrate 阻止 OSWorld headline 被解释成 representation 因果收益。Density-aware Soft Context
  Compression 也已完成 sole-v1、公式、training/evaluation、official code/data/LoRA artifact 与 Ch22/71/41
  邻接审计，成为 26/30 provisional Ch22 refinement；continuous density estimate 只选择有限离散 ratio
  buckets，summary-length proxy、短输入、无硬件/SLO/variance 与 correlation-only evidence 继续保持为
  Experimental boundary。Learning to Commit 随后完成 sole-v1、dataset construction、全部四组 experiments、
  metrics/analysis/future-work 与 Ch73/80/62 邻接审计，成为 25/30 provisional Ch73 refinement；它把
  repository snapshot、blind attempt、accepted oracle diff 与 derived Skill 分离，但单一内部仓库、24/7
  commit pilot、synthetic issue、无公开 artifact/variance/cost 与 judge/maintainer gap 要求保持
  Experimental。TAPS 随后完成 sole-v1 21 页、五个 RQ、formula/setup/results、tree-merge lossless proof、
  depth/entropy appendices、official code/weights/datasets 与 Ch44/42/41/45/55 邻接审计，成为 29/30
  provisional Ch44 refinement。它把 draft training distribution 与 inference-time specialist composition 纳入
  artifact/runtime contract，但 acceptance length 未证明端到端 latency，双 draft 与 larger verification tree
  仍是未闭合成本。DataFlex 又完成 sole-v1、三类 dynamic data action、distributed implementation、全部
  experiments/efficiency appendix、official code/docs/datasets 与 Ch22～24/35/56/62 邻接审计，成为 28/30
  provisional Ch23 refinement。它把 data selection/mixing/weighting 变成有 cadence 与 state 的 control-plane
  action，但多卡 headline 不是 matched-resource scale-up，且项目 2025-12-23 起点、03-17 ZeRO-3 support 与
  03-27 paper node 已按 Source Family 分开。Ask or Assume 又完成 v1/v2、五种 setting、question/difficulty/cost appendices、official
  code/evaluation path 与 Ch75/77/78/62 邻接审计，成为 28/30 provisional Ch77 refinement。它把 intent
  detection 变成每轮 workflow gate；v2 的 Kimi over-query 说明 calibration 依赖 backbone/tool semantics，
  simulated-user resolve rate 不等于真实协作能力。XpertBench 又完成 v1/v4、expert task/rubric pipeline、ShotJudge、
  Gold-subset results、appendices、platform/empty-dataset boundary 与 Ch61～63 邻接审计，成为 25/30
  `No Change` Ch62 case；arXiv ID 的 April prefix 未覆盖 03-27 submission timestamp，52% CDR 也不等于
  human-equivalent judge。EpochX 又完成 sole-v1、task/delegation/asset/credits 机制、三个 cases、official
  product/live-platform boundary 与 Ch77～80/55 邻接审计，成为 23/30 `No Change` Ch80 case；其公开证据
  没有 implementation、transaction traces、longitudinal reuse/incentive、fraud/dispute 或 programmable
  verifier，因此不把 acceptance 写成 correctness proof。W13 当前因此为 39 scored + 6 unscored pending +
  1 blocked，35/35 scored `20+` reviews complete。Discovery/Evidence Gates 继续打开，
  Historical Books Gate 关闭。
- 2026-08-12 W13 daVinci-LLM checkpoint：已读 sole-v1 49 页全文、L0～L9 data-processing taxonomy、
  3.09B/Qwen2 架构、8T-token 四阶段 training trajectory、200+ ablation、mixture/QA ratio、PPL-versus-
  generative evaluation、全部相关 appendices，并核对 official repository/model/data cards 与 Ch23～25/56/62
  邻接。其稳定增量是把 data operator semantics 与 checkpoint-dependent mixture/format value 分开；L0～L9
  不是单调质量阶梯，stage ratio 也不是通用配方。hardware/compute/seeds/variance 未披露，pretraining
  pipeline 仍为 `Coming soon`、data card 只开放 subset，因此为 28/30 provisional Ch23 refinement，状态
  `Experimental / Artifact Partially Available`。W13 当前为 40 scored + 5 unscored pending + 1 blocked，
  36/36 scored `20+` Full Source Reviews complete；Discovery/Evidence Gates 仍 Open，Historical Books Gate Closed。
- 2026-08-12 W13 Emergent Social Intelligence Risks checkpoint：已读 v1 完整正文、formal lifecycle、15 类
  incentive/cognition/governance/structural risk scenarios、全部实验与 appendices，并核对 v2 revision boundary
  和 Ch78/62/68。论文提供 interaction-level risk taxonomy 与外部 indicator 设计，但不同 backbone/trial/judge、
  无统一 sampling/variance、无真实部署对照、无独立 Limitations section 和无公开 artifact，不能形成生产
  发生率或已验证 mitigation。该项为 27/30 provisional Ch78 refinement，状态 `Experimental / Artifact Not
  Available`。W13 当前为 41 scored + 4 unscored pending + 1 blocked，37/37 scored `20+` Full Source Reviews
  complete；Discovery/Evidence Gates 仍 Open，Historical Books Gate Closed。
- 2026-08-12 W13 PRBench checkpoint：已读 sole-v1 全文、30-task curation/evaluation contract、全部
  experiments/failure analysis、Appendix A～D、official project/public harness 与 Ch62/61/63。其 scientific
  reproduction pipeline 强化了 `artifact + environment + trace + hidden reference + hard gate`，但这一 first
  principle 已由 Ch62 覆盖，故为 27/30 `No Change`。公开 artifact 只含一个完整 sample task，且缺完整
  judge/sampling/cost 与 30-task runs，状态为 `Experimental / Artifact Partially Available`。W13 当前为
  42 scored + 3 unscored pending + 1 blocked，38/38 scored `20+` Full Source Reviews complete；两道历史
  Gate 状态不变。
- 2026-08-12 W13 MuSEAgent checkpoint：已读 sole-v1 全文、transition/hindsight/multi-view retrieval 机制、
  全部 experiments/ablations、tool/prompt appendices、official repository 与 Ch73/76/72/74/62。它把整条
  trajectory retrieval 细化为 state-level derived procedural memory，但完整轨迹仍拥有 provenance、replay 与
  跨步因果上下文；四个多选 VQA、固定 1:1 split、无 hardware/latency/cost/multi-seed variance，以及 GPT-4o
  hindsight 同时拥有 filter/guidance 权力，要求保持 `Experimental / Artifact Available`。该项为 28/30
  provisional Ch73 refinement。W13 当前为 43 scored + 2 unscored pending + 1 blocked，39/39 scored `20+`
  Full Source Reviews complete；Discovery/Evidence Gates 仍 Open，Historical Books Gate Closed。
- 2026-08-12 W13 KAT-Coder-V2 checkpoint：已读 sole-v1 22 页全文、KwaiEnv 五模块、五类 expert
  data/SFT/RL、turn-level objective、MCLA、KRL/Tree Training、on-policy distillation、全部 evaluation 与
  Ch28～30/36/56/77/62。长期增量是把 Agent RL identity 表为 environment/tool/scaffold/task/verifier，并将
  专门化、student-on-policy fusion、credit granularity、MoE estimator 与 tree trajectory compute 分层；模型
  架构、训练硬件/precision、关键 ablation、seeds/variance 与 KwaiEnv/KRL implementation 未披露。该项为
  29/30 provisional Ch29 new-mechanism candidate，状态 `Experimental / Implementation Not Disclosed`。
  W13 当前为 44 scored + 1 unscored pending + 1 blocked，40/40 scored `20+` Full Source Reviews complete；
  Discovery/Evidence Gates 仍 Open，Historical Books Gate Closed。
- 2026-08-12 W13 LongCat-Next / forward checkpoint：已读 sole-v1 全文、DiNA/dNaViT、vision/audio
  hierarchical RVQ、统一 autoregressive MoE backbone、训练阶段、全部主实验/methodology analysis、RL
  mismatch、VHalf/quantization appendices、official repository/model card 与 Ch11/12/21/29/34。长期增量是
  把 tokenizer 提升为跨 modality 的可版本化离散 input/output protocol，并把 codec、shared backbone、
  modality head 与 decoder/refiner 的 ownership 分离；continuous projection 与 specialized branch 仍是有效
  alternatives。训练 hardware/topology/cost/variance、VHalf workload contract 与完整 pretraining pipeline
  未披露，故为 29/30 provisional Ch11 new-mechanism candidate，状态 `Experimental / Artifact Partially
  Reproducible`。W13 现在为 45 scored、0 current-review pending、1 blocked，41/41 scored `20+` Full Source
  Reviews complete；W13 Forward Candidate Evidence Gate Passed，forward cursor 移至 W14，broader
  Historical Evidence Gate Open，Historical Books Gate Closed。
- 2026-08-13 W13 external-discovery checkpoint：45 scored families、41/41 `20+` Full Source Reviews、
  4/4 low/cross-week boundary checks、0 ordinary pending 的候选账目再次通过。ClawKeeper exact arXiv HTML
  受保存的用户访问策略禁止；OpenAlex 周窗口请求被拒；Scholar/DBLP 仍无可机器复算目录快照。以上记录为
  primary-source/discovery limitations，不被写成 negative discovery evidence。按 blocked-skip 规则 W13
  Candidate Gate 保持 Passed，backlog cursor 进入 W14；broader Historical Evidence Gate Open、Books Gate Closed。
- 2026-08-13 W14 blocked-skip ledger checkpoint：27 scored（14 high / 12 mid / 1 low）、26/26 `20+`
  Full Source Reviews、1/1 low-score boundary、2 unscored attribution blockers、0 ordinary pending 再次对账。
  `Backdoor Attacks on Decentralised Post-Training` 与 `Cactus` 没有被评分、分配 owner 或冒充全文审计；
  同一外部访问限制不重复绕过。W14 Candidate Gate 保持 Passed，backlog cursor 进入 W15；broader
  Discovery/Historical Evidence Gate Open、Books Gate Closed。
- 2026-08-13 W15 blocked-skip ledger checkpoint：31 scored（19 high / 7 mid / 5 low）、25/25 accessible
  `20+` Full Source Reviews、5/5 low-score boundaries、1 GameWorld primary-text blocker、0 ordinary pending
  再次对账。GameWorld 的 metadata/project/repository packet 没有被算作全文或 Books disposition；同一 arXiv
  访问限制不进行替代浏览器绕过。W15 Candidate/Discovery checkpoints 保持 Passed，cursor 进入 W16；
  broader Historical Evidence Gate Open、Books Gate Closed。
- 2026-08-13 W16/W17 ledger checkpoint：W16 为 42 scored（14 high / 28 mid）、42/42 `20+` reviews、
  3/3 named low-score rejection checks、0 pending；W17 为 22 scored（15 high / 4 mid / 3 low）、19/19
  `20+` reviews、3/3 low-score boundaries、0 pending，且 31 topical hits 的 scored/cross-week/rejected
  关系可复算。两周 Gate 保持 Passed，backlog cursor 进入 W18；Historical Books Gate Closed。
- 2026-08-12 W14 cross-week attribution checkpoint：W16 的 second-pass ledger 暴露两个尚未真正写回的
  W14 identities：`Backdoor Attacks on Decentralised Post-Training`（03-31）和 `Cactus`（04-05）。当前没有
  arXiv ID、作者、artifact 或可读 primary text，二者已转入 W14 `Unverified / Blocked Backlog`，不评分、
  不分配 owner、不阻塞 cursor。W18 又暴露 GLM-5V-Turbo 04-02 official product node；该节点以 18/30
  `Weekly Only — Version/Product Fact / Mechanism Not Disclosed` 回拨 W14，04-29 technical report 与机制
  仍由 W18/Ch34 拥有。W14 当前为 25 scored（13 high / 11 mid / 1 low）、24/24 `20+` Full Source Reviews、
  1/1 low-score boundary、2 blocked、0 current-review pending；fixed official/Infra 与 academic cross-index
  尚未闭合，故 W14 fixed-source Discovery Gate Open；已发现候选的 Forward Evidence Gate Passed，cursor
  移至 W15，Historical Books Gate Closed。
- 2026-08-12 W14 fixed-source checkpoint：已回放可访问的国内外一线模型/研究机构入口与主要 AI Infra
  release/repository 页面，恢复 Amazon Science 04-01 的 LLM-based TTS official-engineering node。该项
  24/30，完成唯一官方材料、Ch38～40 与 Ch62/68 邻接审计；长期候选是
  `phoneme/duration plan -> acoustic generation -> post checks -> bounded regenerate/fallback`，但无 paper、
  model/data card、code、hardware、tail-SLO 或 immutable artifact，故仅为 provisional Ch38 Experimental
  refine，不沉淀厂商 MUSHRA/error headline。Microsoft ADeLe、inference energy 与 relevance-labeling 的
  04-01 formal-publication/communication nodes 经 first-public 去重后回到 2025/更早 source families，不重复
  评分。W14 现为 26 scored（13 high / 12 mid / 1 low）、25/25 `20+` Full Source Reviews、1/1 low-score
  boundary、2 blocked identities、0 ordinary pending；official Research checkpoint 已推进，academic cross-index
  与剩余 Infra 历史 release coverage 仍 Open，Historical Books Gate Closed。
- 2026-08-12 W15 spillback checkpoint：W16 second-pass ledger 列出的 SkVM、GameWorld、Process Reward
  Agents、BERT-as-a-Judge、Many-Tier Instruction Hierarchy、SCOPE (OPD) 与 Tracing the Roots 已写回
  W15。七项当前均缺可定位 arXiv ID、作者、artifact 或 primary text，故为 unscored `Unverified / Blocked
  Spillbacks`，不分配 owner、不阻塞 cursor。W15 仍为 17 scored（8 high / 6 mid / 3 low）、14/14 scored
  `20+` Full Source Reviews、3/3 low-score boundaries、0 current-review pending；Forward Candidate Evidence
  Gate Passed，fixed-source Discovery Gate Open，Historical Books Gate Closed。
- 2026-08-12 W15 fixed-source checkpoint：模型/研究机构、04-11 arXiv 与 AI Infra release 回放新增
  Meta Advanced AI Scaling Framework v2、SGLang v0.5.10、Think in Strokes、FinTrace、SinkTrack、CodeComp
  六个 `20+` source families，以及 Microsoft New Future of Work 一个 19 分 research-synthesis boundary。
  六项均完成非模板化 Full Source Review、first-public/revision、章节邻接、机制/状态/数据流、evaluation
  contract、证明与未证明、trade-off、旧方案共存与 provisional disposition；Microsoft 条目完成低分来源边界。
  vLLM v0.19.0 已按 official 04-03 release 留在 W14。W15 现为 24 scored（13 high / 7 mid / 4 low）、
  20/20 `20+` reviews、4/4 low-score boundaries、7 blocked identities、0 ordinary pending；Forward Candidate
  Evidence Gate Passed，04-12 academic cross-index 与 remaining immutable Infra history 仍 Open，Historical
  Books Gate Closed。
- 2026-08-12 W14/W15 attribution-and-closure checkpoint：七个原 attribution-only identities 均已定位。
  SkVM 的 arXiv:2604.03088 v1 是 04-03，故以 29/30 及完整 compiler/runtime Source Review 回拨 W14；
  W14 更新为 27 scored（14 high / 12 mid / 1 low）、26/26 `20+` reviews、2 blocked identities。
  W15 的 PRA、BERTJudge、ManyIH、SCOPE 与 Tracing the Roots 已完成 Full Source Review；GameWorld 的
  arXiv:2604.07429、project 与 repository 已核对，但 23 页 primary PDF 未取得稳定可读入口，故保持
  27/30 `Unverified / Blocked Backlog`，不计 Full Source Review、不进入 Books。固定 Infra 复核另加入
  TensorRT-LLM `v1.3.0rc11` 的 18 分 pre-release boundary。W15 当前为 31 scored（19 high / 7 mid /
  5 low）、25/25 accessible `20+` reviews、1 blocked、5/5 low-score boundaries、0 ordinary pending；
  academic 与 accessible fixed-Infra forward checkpoint 按 blocked-skip 规则通过。Historical Evidence
  Gate 与 Books Gate 仍关闭。
- 2026-08-09 W14～W16 continuation checkpoint：三周均已从“旧摘要即完成”恢复为
  `Discovery Recall Reopened / Evidence Gate Open`。W14 已从 2 个 baseline 恢复为 23 个 scored
  families，其中 21 个新增候选均按 arXiv v1 / first-public date 归周，另将 discovery-feed 中
  23 个实际早于 W14 的 spillback 显式移出；两项 baseline、HISA 与 Kernel-Smith 共完成 4/23
  Full Source Reviews，其余 19 项保持 `Audit Pending`。HISA 已完成 v1/v3 正文、公式、实验、
  appendix、artifact、章节邻接与 revision-drift 审计，暂定 Ch39 refine、Ch22 handoff；
  Kernel-Smith 已完成 v1/v2 metadata、完整方法/训练/evaluation、公开仓库与 SGLang/LMDeploy
  merged PR 联合审计，暂定 Ch45 refine、Ch52/Ch77 handoff，并明确 isolated kernel speedup
  不等于端到端 serving 收益。Marco DeepResearch 又完成完整论文、公开 inference artifact 与
  Ch72/74～78/62 邻接审计，使本周达到 5/23、18 pending；它把 verification 从 final answer 前移
  到 QA construction、trajectory 和 test-time search，暂定 Ch76 refine、Ch72/77 handoff，同时
  保留 same-model verifier、600-call budget 与 mixed-baseline contract 的限制。Combee 随后完成全文、
  appendix、ACE/GEPA artifact boundary 与 Ch72～74/77～78 审计，使 W14 达到 6/23、17 pending；
  它将并行经验合并定位为 bounded fan-in、redundant exposure、sync/version ownership 问题，暂定
  Ch73 refine、Ch77/78 handoff，并拒绝把 context aggregation 当作 gradient AllReduce 等价物。
  Stochastic KV Routing 随后完成 19 页正文、appendix、Apple Research 入口与 Ch18～22/39～41
  邻接审计，使 W14 达到 7/23、16 pending；它把 depth-wise KV sharing 定位为 checkpoint
  semantics、deployment mapping 与 runtime layout 的联合设计，暂定 Ch19 refine、Ch40/41 handoff，
  同时保留未公开 artifact、GPU/backend/方差/SLO 条件的证据边界。
  MiroEval 接着完成全文、robustness/human-study appendix、公开 evaluator repository 与 Ch62/63
  邻接审计，使 W14 达到 8/23、15 pending；其 report synthesis、claim factuality、process intrinsic
  quality 与 process↔report provenance 被拆成四个 evidence planes，暂定 Ch62 refine、Ch63 handoff，
  并明确 trace availability、judge calibration、live-web drift 与 unmatched tool budget 的限制。
  AgentHazard 随后完成全文、taxonomy/results/prompt appendix、公开 dataset/code/trajectories 与
  Ch62/68/69/77 邻接审计，使 W14 达到 9/23、14 pending；它将 locally plausible actions 的累积
  harm、framework-as-subject 与 trajectory-level evaluation 定位到 Ch68，Ch62/77 短 handoff，并
  明确单一 judge、无 benign calibration、无 executable side-effect verifier 和无 artifact release 的边界。
  LightThinker++ 随后完成全文、公式、general/agentic experiments、appendix、公开实现说明与
  Ch22/41、Ch71～74/77 邻接审计，使 W14 达到 10/23、13 pending；它把固定、不可逆 compression
  演进为 `raw step + summary + visibility state` 的可逆 working-memory projection，暂定 Ch73 refine，
  Ch71/22/41/77 短 handoff，同时保留自合成 trajectory、LLM judge、unmatched proprietary baselines、
  无 immutable release 和未披露完整 inference hardware/SLO 的边界。
  SKILL0 随后完成 v1 全文、理论/实验 appendices、v2 revision、作者仓库、两套公开训练 recipe 与
  Ch28～30/71/80 邻接审计，使 W14 达到 11/23、12 pending。它把 runtime Skill 重新定位为训练
  scaffold：按 on-policy helpfulness 过滤/排序，再把 skill budget 退火到零；但当前 recipe 同时耦合
  GRPO、visual rendering、compression reward 与 curriculum，且 skill-free success 不是参数因果定位。
  因而暂定 Ch29 refine、Ch80/71 handoff，并明确 versioned、可撤销、带权限的运行时 Skill 仍是
  共存分支；Books Gate 继续关闭。
  GrandCode 随后完成 v1 全文、公式与全部相关 appendices、v2/v3 revision、官方项目页、报告及
  contest-submission artifact、Ch28～30/75～78 邻接审计，使 W14 达到 12/23、11 pending。它把
  multi-stage rollout 的 stage reward、final correction、per-token behavior-policy version 与
  staleness 组合为训练状态；但 independently normalized immediate/correction updates 不等于 terminal
  GRPO，过旧 correction 会被丢弃，且论文没有算法级独立消融、训练代码或完整 compute contract。
  因而只暂定 Ch29 Experimental refine、Ch77/78 handoff，不沉淀 live-contest headline。
  Self-Distilled RLVR 随后完成 v1 全文、全部理论 appendices、v2 revision、当前作者实现/configs 与
  Ch28～30 邻接审计，使 W14 达到 13/23、10 pending。它把 verifier-owned update sign 与
  privileged-teacher magnitude modulation 分开；论文的 zero-leakage 定理只约束 sign/support isolation，
  不代表 privileged magnitude 不改变参数轨迹，Bayesian credit 解释也依赖强 conditional-approximation
  假设。关键 component ablation、matched extra-forward cost、lambda/objective 内部 specification
  ambiguity 与 event-bound release 仍缺失。故暂定 Ch29 Experimental refine、Ch28 handoff。
  Towards a Medical AI Scientist 再使 W14 达到 14/23、9 pending。其 30 页论文、唯一 v1、官方项目页/
  cases 与 Ch62/69/77/78 已完整审计；domain evidence→code→run→manuscript workflow 和分级 autonomy
  被保留，但公开 GitHub/Hugging Face 仍为 coming-soon/404，随机 data subsampling、非 matched GPT-5
  workflow、judge calibration 和单任务 manuscript study 限制因果与科学有效性。现有章节已经覆盖
  claim provenance、executable≠ground-truth、approval、durable state 和 correlated roles，因此暂定
  `No Change — Already Covered`，不复制 benchmark headline。
  GEMS 随后完成唯一 v1 全文、全部实验/appendix、项目页、当前核心实现与 Ch73/76/77/78/80
  邻接审计，使 W14 达到 15/23、8 pending。其 criterion-wise loop、raw attempt + compressed
  experience 与 manifest→按需 Skill 提供了具体案例，但同源 MLLM roles、字符串 `yes/no` verifier、
  等权 best-of-history、进程内 memory 和无治理 Skill 限制长期结论；现有 Ch73/76/80 已覆盖这些
  contracts，故暂定 `No Change — Already Covered`，不沉淀模型排名或 benchmark headline。
  Terminal Agents 随后完成 v1/v2、8 月 v3 的 granularity/open-weight/limitations/reproducibility/safety、
  全部 appendices 与 Ch68/74/77/79/80 审计，使 W14 达到 16/23、7 pending。v3 的 generic API-call
  control 表明主要差异是 narrow catalog 与 flexible request surface，而非 terminal 或 MCP 协议本身；
  filesystem/shell、typed domain tools 与 browser 分别保留 scratch/batch/protocol、governance 和 UI-only
  state 的成立条件。故暂定 Ch74 Experimental refine、Ch68/79/80 handoff，不沉淀模型/成本 headline。
  MemRerank 接着使 W14 达到 17/23、6 pending。其 v1/v3 全文、实质 revision drift、公开 dataset schema
  与 Ch29/62/68/72～74 邻接已审计；query-independent preference memory 被定位为 downstream-utility-
  trained derived materialized view，而 same-reranker reward/evaluation、synthetic purchase/query labels、
  缺 code/checkpoint/compute 及 consent/correction/delete lifecycle 均保留为证据边界。故暂定 Ch73
  Experimental refine、Ch29/62/68/72 handoff，不沉淀 headline metric。
  ASI-Evolve 随后使 W14 达到 18/23、5 pending。其唯一 v1 全文、circle-packing appendix、当前公开
  pipeline/database/cognition 实现、artifact/release coverage 与 Ch23/29/62/73/77 邻接已审计。Cognition
  的 cold-start prior 与 Analyzer 产生的 run-derived lesson 被拆成两种 memory plane；只有 circle packing
  提供三次重复的 component ablation，三项高成本主任务缺 causal isolation、硬件/总算力与可重放 artifacts。
  故暂定 Ch77 Experimental refine、Ch73/62 handoff；SOTA 数量、benchmark headline 与 README 的
  “fully open-sourced”不被外推为主实验可复现。
  Simple Self-Distillation 随后使 W14 达到 19/23、4 pending，并在全文后从 24 调整为 26 分。v1 的
  五模型论文、完整理论/实验 appendices、v2 revision、作者 generation/evaluation code、checkpoint
  cards 与 Ch20/24～29/62 邻接已审计。它把 non-unit temperature + truncation 产生的 self-target
  distribution 通过 SFT 编译进参数，再独立选择 serving decode policy；但 v2 才加入 GPT-OSS，current
  generator 又以 bottom-10% length filter/1.5 temperature 偏离论文最小过滤/部分主配置，且无公开
  Megatron training recipe、重复/置信区间和独立 tuning split。故暂定 Ch25 Experimental refine、
  Ch20/62 handoff，不把 raw wrong code、pass@k headline 或后续 revision 外推为通用 self-improvement。
  HippoCamp 随后完成 official-artifact 级详细审计，但不增加 Full Source Review 计数：arXiv 只有
  24.5 MB v1 PDF 且无 HTML，当前 reader 与已保存的 arXiv 站点安全偏好都无法完成 primary-paper
  全文读取。项目页、作者仓库/history、官方 dataset schema 与 evaluation surfaces 能建立
  `raw snapshot → hidden evidence/locators → capability labels → QA/profile claim` 评估对象，却不能替代
  论文 Method、完整实验契约、ablation 与 Limitations。故 HippoCamp 为 `Unverified / Blocked`，
  likely owner Ch62、Ch72/73/68 handoff；current leaderboard 不回写为 W14 event-time 证据。W14 仍为
  19/23 complete，现有 1 个 detailed blocked review 与 3 个 pending。
  Omni-SimpleMem 接着完成 v1/v2 全文、公式、五-backbone results、ablation/efficiency、全部 appendices、
  prompt catalog、author repository 与 v0.2.0 release 审计，使 W14 达到 20/23、1 blocked、2 pending。
  其 hot MAU metadata / cold raw evidence、dense+sparse+graph candidate preservation 与 token-budgeted
  progressive expansion 暂定由 Ch73 owner，Ch72/62/68/77 handoff；同时明确 novelty filtering 是 destructive
  write gate，current main 的 CLIP/relation schema/MCP 已发生 version drift。论文最大增益多来自 response-format、
  timestamp、tokenization 与 data-completeness repair，因此长期结论是先验证 harness/data correctness，再归因
  architecture；相对 naïve baseline headline、无硬件的 8-worker throughput 与 benchmark-specific prompt 不进入
  Books。S0 Tuning 随后完成 v1/v2 全文、全部 appendices、repository/package、trained-state 与 dataset card
  审计，使 W14 达到 21/23、1 blocked、1 pending。它把 recurrent launch state 确认为 weight/prompt 之外的
  adaptation surface，暂定 Ch26 Experimental refine、Ch22/31/46 handoff；但 paper 与 model card 在 24+8 vs
  21+6 layer layout、A10G vs A100 和 base identity 上冲突，故 Source Reliability 下调、总分 24→23，任何
  checkpoint/layout 或通用性能结论均不进入 Books。Meta-TTL 再使 W14 达到 22/23、只余 HippoCamp
  detailed blocked review。其 v1/v2 全文、全部 appendices、v3 revision boundary、repository/entrypoints 与
  Ch62/73/75～77 已审计；它把 fixed reflection rule 演进为 offline learned meta-policy + runtime mutable actor
  prompt，暂定 Ch76 Experimental refine。但 v1 无 seed/variance/hardware/token-cost，current code 的 episodes、
  proposer/model 与 selection surface 已 drift，且 OOD Web 增益集中在结构相近 domain，故 24→23，不写 headline。
  以上均不打开 Books Gate。MegaTrain 随后按作者 2026-04-05 正式发布页从 W15 回拨 W14，使 W14 为
  23/24 Full Source Reviews、只余 HippoCamp detailed blocked review。其唯一 v1、全部 evaluation/appendix、
  作者发布页、current repository 与 Ch31～36 邻接已审计；CPU authoritative state → per-layer transient GPU
  cache 暂定 Ch35 Experimental refine，Ch32/34/31 handoff。checkpoint ablation 与 1K-context TFLOPS 的
  表格/正文冲突、缺失 SLO/恢复/成本以及 later repository drift 阻止 headline 外推。
  2026-08-11 再次核验时，HippoCamp 的 official arXiv primary text 已可读取；其 benchmark construction、
  evidence/trajectory schema、Atomic Units、annotation/QC、三种 evaluation regime、metrics、capability
  analysis 与 appendices 已和既有 project/repository/dataset packet 联合复核。W14 因而达到 24/24 Full
  Source Reviews、0 blocked、0 pending。最终 disposition 为 `No Change — Already Covered / Experimental
  Evaluation Case`：Ch62 已拥有 subject/environment/scorer identity、evidence contract、dataset governance
  与 judge calibration，Ch72/73/68 已拥有 retrieval、memory lifecycle 与 derived-sensitive-data 边界。
  W14 recorded Candidate Evidence 已闭合，但 fixed-source Discovery Gate 仍为 Open，Historical Books Gate
  仍为 Closed。
  W15
  已从 4 个 baseline families 恢复为 18 个 scored families；14 个新增候选按 first-public date
  归周，9 个 curation-lag 条目回写 W11/W13/W14。Seeduplex、TriAttention、Memory Intelligence Agent 与
  SkillX 完成首批 retained Full Source Reviews；SPPO 又按 v1 2026-04-10 从 W16 curation feed 回填 W15。
  Beyond Accuracy / PTE 随后完成 v1 全文、全部 appendices、v2/ACL publication boundary、current
  artifact 与 Ch39～41/62～63/77 邻接审计，使本周达到 5/16 `20+` reviews。它把 flat
  output-token count 推进为按 turn 累积的 Prefill/Decode state cost，暂定 Ch62 Experimental refine；但
  单节点 8×H200 validation 仅测纯 generation latency，排除 tool/network time，跨 GPU 结果只是以 datasheet
  peak FLOPS 重算同一批 trajectories，且 partial KV hit、batch/scheduler、actual utilization 与 SLO 未纳入，
  因而 proxy 不得替代 observed trace-level SLI。TriAttention 已完成全文、公式、实验、appendix、artifact 与
  Ch19/22/40/41 邻接审计，暂定 Ch41 refine、Ch22 handoff。W16 后续已从 3 个 baseline 扩展为
  42 个 scored families；CodeTracer、BEHEMOTH、Sema Code、OccuBench、Agentic Aggregation、ClawGUI、
  On-Policy Distillation、AiScientist、AgentSPEX、Exploration/Exploitation Errors、Dive into Claude Code、
  Memory Transfer Learning、DR3-Eval、Corpus2Skill、OpenMobile、Scaling Test-Time Compute、SkillFlow、EvoMaster
  与三项 baseline，以及第二轮 academic、official/infra 恢复项合计完成 42/42 Full Source Reviews；
  3 个 named below-threshold items 也完成拒绝核验。OpenReview/TMLR/formal proceedings、weekend
  discovery、固定机构与 release/RFC/PR list 已完成 first-public-date/dedup closure，W16 Evidence Gate Passed。
  AiScientist repository release record 将 event date 从 arXiv v1 的 04-14 修正为 04-13；全文、
  PaperBench/MLE-Bench contract、File-as-Bus ablation、current artifact 与 Ch76～78/80 邻接已审计。
  暂定 Ch77 refine：compact workspace map 只是 authoritative state 上的 derived navigation view，文件
  本身不提供 versioned transition、conflict handling、provenance、replay 或 rollback；不采纳 benchmark
  headline 或通用 production claim。Nemotron 3 Super 已按 03-04 首发回拨
  W10。AgentSPEX 的唯一 v1、18 页全文、全部 appendices、七项 benchmark、23 人 user study、formal-
  verification 示例、current six-commit repository 与 Ch76～80 邻接已审计。Ch77 已覆盖其 deterministic
  spine / durable state 机制，故归为 `No Change`；缺少 component ablation、repeated runs、cost/SLO、
  exactly-once side-effect semantics 与真实形式验证证据，使分数从 26→23。YAML spec 不等于 durable runtime。
  Exploration and Exploitation Errors 的唯一 v1、36 页全文、全部 appendices、公式/edge cases、prompt/
  harness/semantic experiments、additional results、current 11-commit artifact 与 Ch62/73～75/77 邻接已审计。
  它暂定 Ch62 Experimental refine：process metric 可不读 model policy，却依赖 evaluator 的完整 map/DAG、
  productive target 与 distance，所以 policy-agnostic 不等于 environment-agnostic；trajectory-conditioned
  denominator 使其只能补充 final outcome，不能形成通用模型排名。三 seeds、symbolic grid 和 bundled
  harness ablation 阻止结果外推。
  Dive into Claude Code 的 v1 46 页全文、v2 revision drift、companion repository、当前官方 docs 与
  Ch68/73/74/77～80 邻接已审计。它是对公开 v2.1.88 package 的独立 reverse-engineering snapshot，
  不等于 Anthropic 官方 architecture 或 production-path evidence；无 benchmark、ablation、failure
  injection、cost/SLO 或 user study。其 loop、graduated compaction、deny-first authorization、append log、
  isolated subagent 与 extension boundary 均已由现有章节拥有，故归为 Ch80 `No Change`，不重复写 Books。
  Memory Transfer Learning 的唯一 v1、全部 tables/appendices、negative-transfer cases、formal abstraction
  assumptions、project page、7-commit placeholder repository 与 Ch72～74/77/80 邻接已审计。它暂定 Ch73
  Experimental refine：跨域 procedural memory 的核心 contract 是在 specificity benefit 与 mismatch risk
  之间选择，并将 source/target model、language/tool/environment/evaluator compatibility 带到 adoption gate；
  但公开 code 仍为 `Coming Soon`，且缺 seeds/uncertainty、cost/SLO 与 contamination audit，故 25→24。
  DR3-Eval 的唯一 v1、全部 appendices、DR3-Agent、corpus/retrieval/framework ablations、live-web
  comparison、judge validation、current code/data 与 Ch61～63/72/77 邻接也已审计。它暂定 Ch62
  Experimental refine：Deep Research EvalSpec 需要把 user files、frozen source snapshots、support/noise
  taxonomy 与 corpus budget 一起纳入 environment identity，并按 component/slice 对齐 static sandbox 与
  live web；aggregate 接近可能只是 recall/citation 等相反变化抵消。当前公开 dataset 未显式列出论文
  所需 sandbox corpus，正文与 Appendix D 又分别报告 50/4 和 30/2 的 human-validation protocol，故
  Source Reliability 4→3、总分 25→24；不把 reproducible 或 human-aligned 宣称升级为已核验事实。
  OpenMobile 的唯一 v1、appendices、environment-memory/task-synthesis/policy-switching control flow、
  current code/data/model artifacts 与 Ch23/25/62/77/80 邻接已审计。它暂定 Ch25 Experimental refine：
  demonstration contract 从 successful expert path 扩展到 learner-reachable error/recovery states，但同一
  Gemini family 同时拥有 annotation/filter/monitor/expert/rewrite，且 event-time artifact identity、训练
  硬件、cost/SLO、完整 contamination 与真实设备/reset 证据缺失。SR 与 Longevity 各降一分，25→24；
  AndroidWorld suite 内结果不外推为通用 mobile-Agent 能力。
  Scaling Test-Time Compute for Agentic Coding 的 sole v1、Appendix A～H、RTV/PDR 公式、full 500-task
  SWE-Bench Verified 与 88-task Terminal-Bench v2.0 contract、five-model results、ablation 与 Ch62/75/77/78/80
  邻接已审计。它暂定 Ch78 Experimental refine：bounded trajectory representation 是 parallel selection 与
  sequential reuse 的共同接口，但 summary/judge 都由同源 model 生成，主实验缺 total-compute-matched
  baseline、artifact、cost/latency/SLO/seed。iteration 1 的平均 pass@1 上升同时伴随 pass@16 下降和更多
  0/16 tasks，暴露 bad-context amplification；TN/PV/SR 下调、Longevity 上调后 27→25。
  Don't Retrieve, Navigate / Corpus2Skill 的 v1 全文、Appendix A～I、完整 traces、v2/v3 generalization/
  metric/cost drift、current 7-commit WIP artifact 与 Ch71～73/80 邻接也已审计。它暂定 Ch72
  Experimental refine：Agent-visible hierarchy 是 source 之上的 versioned derived index，只有在 corpus
  存在可恢复 topical taxonomy 时才可能换取 coverage/backtracking；HAGRID/TatQA/CUAD 的 later revision
  反例保留 flat retrieval 的成立条件。hard/multi-parent routing、map/source identity、ACL/delete propagation、
  incremental rebuild 与 route trace 属新的系统状态；单 Wix event-time study、同源 judge、无 uncertainty/
  production SLO 和 WIP artifact 使 TN 5→4、SR 4→3、总分 26→24。
  04-14 arXiv v1 只作为 later formal report。Sema Code 因只有两个功能性 deployment cases、无 stress/
  ablation/security/scale evaluation 且缺 event-bound immutable code release，从 26 调整为 23 分；
  Ch74/77～80 已覆盖其长期机制，故归为 Ch80 `No Change`，不采纳 production-ready、strict
  isolation 或 zero-residue 宣称。OccuBench 已完成两版论文、公开 dataset/reimplementation、
  simulator/fault/verifier code 与 Ch61～63/68/77 邻接审计；它暂定 Ch62 Experimental refine，长期价值是
  把 simulator 视为需独立校准的 evaluation subject，而非把 synthetic occupation score 当作真实职业
  胜任力。论文内部 proprietary harness 未公开、缺 domain-expert/real-environment anchor，且跨 simulator
  会改变绝对分数和部分排序，因此不采纳 production reliability 或通用 reasoning-compute 宣称。
  Agentic Aggregation 已完成 33 页论文、全部 appendices、公开 rollout/code 与 Ch62/76～79 邻接审计；
  它从 vote/select/summarize 演进到把 immutable trajectories 作为外部 read-only evidence environment，
  暂定 Ch78 Experimental refine。但 `full fidelity` 只表示存储未预压缩，不证明有限 context、ROUGE-L
  search 与 early finish 实际找全证据；开放式结果又依赖修改过的 model-judge prompt，故 26→25，
  不采纳通用 scaling、production reliability 或“更多 Agent 必然更强”结论。
  ClawGUI 已完成全文、RL/Eval/Agent modules、当前仓库与 Ch27～30/62/68/73～80 邻接审计；其分数
  由 26 调整为 24。它暂定 Ch29 Experimental refine：长期价值在于把 GUI rollout 的 environment
  generation、reset、health、lease、spare failover 与 verifier semantics 纳入训练状态机，而不是把
  GUI policy 当作孤立模型。论文的 GiGPO+dense 对照同时改变算法与 reward，reproduction 指标是非对称
  tolerance hit rate，且缺 seeds/variance、PRM calibration、大规模真机与 security/privacy evidence，
  因此不采纳 production-ready、通用可复现性或 hybrid CLI/GUI 优势宣称。
  Rethinking On-Policy Distillation 已完成唯一 v1、全部 appendices、OPD/verl/LLaMA-Factory artifact 与
  Ch24～26/29 邻接审计，27→25，暂定 Ch25 Experimental refine。它把“更强 teacher”拆成 student-
  visited states 上的 support compatibility 与 genuinely new capability，并揭示长 trajectory 中 teacher
  reward 随 prefix drift 退化；但所有实证来自小型 math/model-family 配对，gradient anisotropy 仍是作者
  未验证 hypothesis，故不外推 97%～99% overlap mass、3K/7K sweet spot 或 sampled-token sufficiency。
  W17 feed 暴露的 BEHEMOTH、AgentSPEX、OpenMobile、Scaling Test-Time Compute、
  SkillFlow 与 EvoMaster 已按 arXiv v1 日期回拨 W16。CodeTracer 已完成正文、全部 appendices、evaluation/ablation、artifact 入口与
  Ch62/64/65/77/80 邻接审计，暂定 Ch80 refine；其 replay 诊断成本未计入 matched run budget，
  因此不外推生产收益。BEHEMOTH 已完成唯一 v1、全部 appendices、CluE repository 与
  Ch72～74 邻接审计；它把 memory extraction policy 明确为带 heterogeneous-feedback isolation、
  model/reward/task identity、regression 与 rollback 需求的 derived artifact，暂定 Ch73 Experimental
  refine。作者协议只隔离 extraction stage，shared-model/judge blind spot、完整 lifecycle、真实长期
  drift 与 production SLO 仍未验证。SkillFlow 已完成唯一 v1、全部 appendices、project/repository/data
  artifact 与 Ch62/73/77/80 邻接审计；family-local fixed-order protocol 提供 skill repair/negative-transfer
  的条件性证据，却不测跨 family retrieval/forgetting，且 history-context control 在正文与表格分别为
  47.41%/51.04%，故 25→24 并归为 `No Change — Already Covered`。EvoMaster 已分离审计 v1 四项
  OpenClaw 对照、v4 十项扩展、repository/tags 与 05-18 才加入的 run-level evolution；specialized workflow
  confounding、无 component ablation/matched compute/seeds/CI 与 event-bound artifact 使其 25→23，归为
  Ch77/78/80 `No Change`。三周都已恢复 fixed official、academic 与 Infra source coverage
  limitations，旧版“没有其他论文/stable release”的空结论不再被当作证据。外部 primary-source
  枚举恢复后继续扩展 candidate census；期间后续周仍连续重开，不等待逐周人工指令。
  MIA 已阅读全文、全部 appendices、v1～v4 revision、repository/model/dataset artifact 与
  Ch29/31/62/72～77：它暂定 Ch73 Experimental refine，证明的是 external workflow memory 与
  parametric Planner update 的实验组合，不证明可逆双向转换或 production-safe online learning；
  memory clear、weight unlearning、model-version swap、rollback 与 correlated judge feedback 均保留为边界。
  SkillX 的 v1 全文和全部 appendices、v2 revision boundary、current
  repository/SkillKB、Ch73～75/77/80 已审计。它暂定 Ch73 Experimental refine，保留 raw trajectory→
  hierarchical procedural skill→pseudo-plan-conditioned step retrieval 的演进；论文自身的 per-model
  composition 退化与 third-iteration overfitting 证明 hierarchy 不是单向收益，故 25→24，tool schema、
  plan/workflow authority 与 registry governance 不交给生成的 skill 文本。
  Agentic Skills in the Wild 随后完成唯一 v1 全文、全部 appendices、author code/data、single-commit/no-release
  artifact boundary 与 Ch62/73～75/77/80 邻接审计，使 W15 达到 6/15、9 pending。它把 curated Skill 上界拆成
  self-selection、distractor、large-pool retrieval、no-curated adaptation 与 task-local refinement 的 progressive
  EvalSpec，暂定 Ch62 Experimental refine。三次运行、pair-level model+harness confound、不同 timeout、缺失本地
  serving hardware/完整成本，以及 refinement 在部分条件下回归，阻止具体模型排名或“Skill 必然有益”进入 Books。
  RAGEN-2 已按官方 03-12 release 回拨 W11，4 月 7 日 arXiv v1 只保留为 later formal-source boundary。
  MARS 随后完成唯一 v1、全部 appendices、author repository 与 Ch40/41/44/48/52 邻接审计，使 W15
  达到 7/15 Full Source Reviews、8 pending。它把同一 AR backbone 的 masked block proposal 确认为
  exact speculative sampling 之外的 Experimental branch：clean/noisy 双流与 AR loss 保住 one-token
  competence，confidence threshold 决定 lossy left-to-right commit，block KV cache 则把收益暴露给 batch
  synchronization。作者的 1.71× 只属于未完整披露 inference hardware/runtime 的 Qwen2.5-7B GSM8K
  contract；训练约 2× H200-hours、低 threshold 质量下降和大 batch barrier 阻止 headline 外推。暂定
  Ch44 refine、Ch40/41/52 handoff，Historical Books Gate 仍关闭。
  FP4 Explore, BF16 Train / Sol-RL 再使 W15 达到 8/15 Full Source Reviews、7 pending。其唯一 v1、
  theory/全部 appendices、NVIDIA project、Sana recipes/docs 与 Ch28～32/35 邻接已审计。它把低精度限制在
  deterministic seed exploration：NVFP4 preview 只负责 ranking，selected seeds 必须用 BF16 policy 重生后
  才能进入 update。该分层暂定 Ch29 Experimental refine、Ch31/32/35 handoff；但 4.64× 是 reward-threshold
  convergence，不是 iteration throughput，实际 iteration 只有作者 B200 contract 下的 1.25～1.62×。理论还
  依赖 bounded perturbation、Lipschitz 与 i.i.d. Gaussian rewards，且无 seeds/variance/multi-node/immutable
  commit，不能外推到不可 deterministic replay 的 LLM/Agent trajectory；Historical Books Gate 仍关闭。
  Flux Attention 随后使 W15 达到 9/15 Full Source Reviews、6 pending。其唯一 v1、全部 Appendix、author
  repository/training paths、Block-Sparse-Attention 与 nano-vLLM integration tree，以及 Ch22/39～42/52 邻接
  已审计。它把固定 hybrid topology 推进为 prompt-conditioned layer hard route：以较粗粒度牺牲 head-level
  flexibility，换取整层 contiguous execution 与 KV traffic bypass。作者的 2.8× Prefill 是 256K E2E，接近
  2.0× Decode 则是单 A800、BF16、batch-1 kernel latency，不能合并成 production serving speedup；缺少
  continuous batching、TP、TTFT/TPOT/p99、route/KV identity 和 immutable release。暂定 Ch22 Experimental
  refine、Ch39～41/52 handoff，Historical Books Gate 仍关闭。
  SkillClaw 接着使 W15 达到 10/15、5 pending。其唯一 v1、24 页全文、全部 appendices、author repository
  的 client/evolve/validation boundaries、无 release 与 later-feature drift，以及 Ch62/68/73～75/77/79～80
  邻接已审计。论文把 user-local/manual Skill 推进为 session evidence aggregation → candidate synthesis →
  same-environment validation → controlled shared release；但只展示六类任务中的四类，executor/evolver/validator
  均为 Qwen3-Max，缺少 independent judge、held-out isolation、uncertainty、privacy/consent、tenant/poisoning、
  revoke/rollback 与 immutable event-time artifact。Source Reliability 4→3、25→24；Ch80 已覆盖 Skill identity、
  provenance、evaluation/policy/revocation、canary、in-flight pinning、rollback 和 global-memory 写入边界，故暂定
  `No Change — Already Covered`，不为制造 Books diff 重复写入。Historical Books Gate 仍关闭。
  DMax 随后使 W15 达到 11/15、4 pending。其 v1 全文、公式、Algorithm 1、全部 experiments/ablations、
  v2/v3 revision boundary、author repository、Math/Coder model/data artifacts、无 release 与 Ch29/40～44/48/52
  邻接已审计。它把 one-way mask→token commit 推进为 on-policy self-error correction + confidence-carrying
  hybrid embedding + block convergence commit；直接在原模型上套 soft decoding 会 collapse，说明这不是纯
  runtime optimization。作者结果只绑定 LLaDA-2.0-mini、math/code self-distillation、8×H200 training、
  2×H200 TP、batch 1 与 2048 generation；缺少 uncertainty、continuous batching、KV/cache、TTFT/TPOT/p99、
  energy 和 general-domain evidence。Source Reliability 4→3、26→25，暂定 Ch40 Experimental refine，
  Ch29/44/52 handoff；Ch48 不拥有该机制。Historical Books Gate 仍关闭。
  Externalization in LLM Agents 随后使 W15 达到 12/15，只余 KnowU-Bench、MolmoWeb、SPPO。其唯一 v1
  54 页已覆盖 memory、Skill、protocol、harness、组件交互、parametric/externalized trade-off、failure taxonomy
  与 future work；但它是 narrative systems synthesis，没有 systematic review protocol、原始 implementation、
  benchmark、ablation、hardware/SLO contract 或 uncertainty。因此其贡献是 ownership vocabulary，而非因果
  performance evidence。Ch71/73/74/77/79/80 已覆盖 context budget、memory provenance、tool authority、durable
  workflow、protocol lifecycle 与 platform governance，故 23 分不变，暂定 `No Change — Already Covered`，
  Ch80 为 owner。Historical Books Gate 仍关闭。
  KnowU-Bench 再使 W15 达到 13/15，只余 MolmoWeb 与 SPPO。其 sole v1、全部正文与 Appendix、project、
  current code 的 Android/container/task/profile/log/agent/evaluator 边界已审计。可迁移机制是把 proactive Agent
  evaluation 从 static intent 扩成 act/ask/silent/stop-after-rejection 的 feedback-conditioned policy，并用 Act、
  Silent、Stop 分离 initiative 与 restraint；hard side effects 由 rule verifier，soft preference 由 rubric judge。
  四个 synthetic personas、LLM-generated logs、gpt-4o simulator、26 trajectories/four human raters 的有限 judge
  calibration，以及缺失 simulator-human fidelity、uncertainty、hardware/cost/SLO 阻止真实用户与生产外推。
  24 分维持，暂定 Ch62 `Refine — Existing Argument (Experimental)`，Ch68/73/75/77/80 handoff；Historical
  Books Gate 仍关闭。
- 2026-08-10 MolmoWeb event-date correction：全文、官方 release、Hugging Face collection 与 repository
  联合核验后，首次公开日期确定为 Ai2 2026-03-24，而非 arXiv 2026-04-09。该 Source Family 的完整
  review 已从 W15 移入 W13；该检查点当时将 W13 更新为 25 scored families、21/21 recorded `20+`
  reviews。后续 vLLM fixed-source replay 又使 W13 更新为 26 scored families、22/22 recorded `20+`
  reviews；W15 更新为
  17 scored families、13/14 retained reviews，仅 SPPO pending。MolmoWeb 暂定 Ch23 `Refine — Existing
  Argument (Experimental)`，核心是 teacher/student observation、action schema、browser、verifier 与
  judge lineage，以及 `pass@k` candidate coverage 不等于 deployable selector reliability；不沉淀模型排名、
  固定配比或 synthetic/visual 单向替代 human/DOM 的结论。Historical Books Gate 继续关闭。
- 2026-08-10 W15 SPPO checkpoint：sole v1、全部 appendices、五个 classic-control RLVR tasks、official
  verl fork/run scripts、核心 `sequence_level_adv` code path 与 Ch28～30 已审计。SPPO 保留 learned Critic，
  只把它从 token-prefix return 降维为 policy-conditioned prompt solvability，并把 `R-V(prompt)` 广播到
  response tokens；因此它用 Critic state/calibration/version coupling 换取 `N=1`，不等于解决 step-level
  causal credit。作者证据绑定 1.5B/7B math RLVR、binary verifier、4×A100/H100、`beta_KL=0` 与无多 seed/
  uncertainty 的 contract。26 分维持，owner 修正为 Ch28、Ch29 handoff，暂定 Experimental refine；W15
  recorded `20+` reviews 达到 14/14，但 discovery source coverage 仍未闭合，Evidence Gate 保持打开。
- 2026-08-09 W17～W30 continuation checkpoint：所有后续历史周均已逐周恢复明确的
  Discovery/Evidence Gate，不再沿用“recorded set 完整即 week recall 完整”的隐含假设。W17、W23、
  W25、W26 的合并评分行分别暴露多个 Source Families；W18 的 zero-high-score 结论必须由完整扫描
  证明；W27 的 9 个评分行对应 8 个 unique families，Seed2.0 两行已确认共享一个明确 packet，故
  recorded set 为 8/8 independent reviews。W28～W30 已按 expanded discovery list 恢复为
  21、26、25 个 scored families；这只关闭候选结构恢复检查点，三周仍有 49 项 Full Source Review
  pending。所有既有 Books decisions 统一视为 provisional input，Historical Books Gate 保持关闭。
- 2026-08-10 W17 Gate checkpoint：W17 已从 5 个 baseline families 恢复为 22 个 scored
  families；19 项达到 `20+` 且 19/19 均完成非模板化 Full Source Review。31 个具名 topical hits
  已对账为 22 个 scored families、8 个跨周归档和 1 个 below-retention patch。academic cross-index、
  official institution 与 Infra fixed lists 已闭合；KServe v0.18.0 RC family 作为 pre-release/version
  fact 恢复，Ray 2.55.1 patch 低于门槛。W17 Discovery 与 Candidate Evidence Gates 均通过，cursor
  前移至 W18；Historical Books Gate 仍关闭。Stochastic KV Routing 按 4 月 3 日 v1 回拨 W14，
  TCOD 按 4 月 27 日 v1 归 W18。
- 2026-08-10 W18 recall-correction checkpoint：W18 当前为 75 个 scored families，其中 69 项
  `20+`，current scored retained set 的 69/69 已完成非模板化 Full Source Review。扩展 title/date
  reconciliation 确认的 9 项中 World-R1、Tuna-2、Conversational User Simulation、Perceval 与 Turning TIDE
  已完成评分与全文审计，Step-level Optimization、InteractWeb-Bench、FlashRT 与 ReVSI 也已完成。ReVSI
  的 40 MB arXiv PDF 直接提取阻塞通过作者公开全文副本、ICML/OpenReview metadata、official repository、
  project page 与 dataset 联合核验解除。继续逐项回放 HF 全页后又确认 10 个此前遗漏的 in-window
  families，已登记 title/arXiv/date/initial owner。Step-Level Advantage Selection 已完成 v1 全文/Appendix、
  official VeRL artifact 与 Ch28～30 邻接审计；28/30，暂定 Ch29 Experimental refine。Semi-DPO 也已完成
  ICLR conference full text、Appendix 6.1～6.11、project page、current 404 code boundary 与 Ch29～31
  邻接审计；27/30，暂定 Ch30 Experimental refine、Ch31 handoff。其五-scorer consensus、timestep-conditioned
  self-labeling 与 derived-data lifecycle 提供机制增量；scorer/evaluation coupling、3,992-pair controller leakage、
  无 human audit/seeds/可用 artifact 阻止外推。Onchain Operating-Layer Controls 随后完成唯一 v1、全部
  表图/Limitations/Appendix prompt template、官方 AgentVault/Core Contracts/whitepaper/Terms 与 Ch79～80
  邻接审计；28/30，暂定 Ch80 Experimental refine、Ch68/77 handoff。其 99.9% 只是 policy-valid submitted
  transactions 的 settlement 条件率，不是 rejection-inclusive mandate success、收益或安全率。Visual
  Generation survey 又完成 v1 全文、v2 revision metadata、作者 living-roadmap artifact 与 Ch61～63/
  Ch9～10/Ch38 邻接审计；24/30，因 Ch62 与 Ch10 已覆盖 task-specific verifier、structured/executable
  evidence 和 world-model action-faithfulness，结论为 `No Change — Already Covered`。论文对闭源模型的
  VLM/dual-encoder/silent verifier loop 是作者明确标注的 speculative reading，selected stress tests 也不能
  形成模型排行榜或证明 causal mechanism。Edit-R1 随后完成 arXiv v1 全文、公式/实验/prompts/appendices
  与 OpenReview source-family/date 核验；同一九位作者和同一 principle decomposition、GCPO、RRM-guided
  GRPO 机制已于 2025-09-03 first-public，故归入 2025 backlog，不计 W18 score。Meta-CoT 随后完成
  唯一 v1 主文、公式/算法、训练/评估合同、公开 artifact surface 与 Ch25/27～30/62 邻接审计；26/30，
  暂定 Ch29 Experimental refine，Ch25/62 short handoff。其 task/meta-task/target plan、CEC reward、
  early-timestep Flow-GRPO 与冻结 understanding expert 形成机制增量；但五类 primitive 的完备 basis/
  entropy 论证只在未能独立读取的 supplement 展开，训练和评估又依赖闭源 judges，不能外推为通用
  编辑 ontology 或可靠 reasoning。Compliance versus Sensibility 随后完成作者公开全文、probe/CAA
  intervention、judge validation、hardware/seed contract 与 Ch16～18/27～28/62 邻接审计；26/30，暂定
  Ch17 Experimental refine，但不把线性可读出或 `up to 29%` 外推为 deliberate reasoning choice 或生产
  compliance control。Zero-to-CAD 又完成作者公开全文、OpenReview/官方 dataset、distributed synthesis、
  execution/geometric/export validation、downstream bootstrapping 与完整训练/评测合同审计；28/30，暂定
  Ch23 Experimental refine，Ch77/62 handoff。它支持 verifier-bounded executable synthetic programs 与
  受限 synthetic-to-program bootstrapping，不证明 DFM、真实设计意图或 matched dataset superiority。
  FAMA 与 Terminal Task Synthesis 随后解除访问阻塞并完成全文审计。FAMA 的 failure-conditioned helper
  subset 选择在 Ch78 已由 single-agent headroom、trace-triggered topology repair、coordination tax 与
  correlated-judge boundary 覆盖，27/30，最终为 `No Change — Already Covered`。Terminal Task Synthesis
  将 scenario-skill support、graph coverage 与 inverse-frequency path sampling 接入 executable task
  construction，28/30，暂定 Ch23 Experimental refine；但 giant-component counting semantics 与公开 artifact
  缺失保持争议边界。Microsoft Research/EuroSys cross-index 还恢复 Concord。18 页论文、formal
  proceedings、DBLP/DOI 与作者 publication/news surface 已审；2025-08 acceptance announcement、
  Microsoft PDF 的 `2025/10` path 与 2026-04-27 formal publication 无法证明唯一 first-public date，故登记为
  `2025 Backlog — Disputed First-public / W18 Formal-Publication Node`，不在 W18 重复计分。其长期机制是
  learned best-effort configuration guard 与 semantic verifier/release gate 分层，owner 候选为 Ch69；Books
  Gate 关闭。原有
  21 个 academic reviews
  保留有效；system-integrated speculative rollout 已完成全文、NeMo RL v0.6 artifact、8B measured/
  235B simulated evaluation boundary 与 Ch29/44 邻接审计，暂定 Ch44 Experimental refine；KServe
  v0.18.0 stable 作为 W17 RC family 的 stable node，已通过 official release、blog、
  CRD/control-plane docs 与 Ch56～58 联合核验，结论为 `Weekly Only — Stable Release`。HF W18
  二次回放新确认 GLM-5V-Turbo、RL rollout speculative decoding、Synthetic Computers、Agent-Native
  Research Artifacts、agentic data-analysis process reward、Step-Audio-R1.5 与 tabular retrieval
  robustness 七项 first-public 在本周；rollout paper、Agent-Native Research Artifacts 与 tabular retrieval
  stability 已审。后两者分别暂定 Ch80、Ch72 Experimental refine，并由 Ch77、Ch71 接收 handoff。
  DataPRM 也完成 v1/v2 boundary、当前 artifact、tool-augmented ReAct verifier、ternary reward、GRPO、
  evaluation/cost/limitations 与 Ch29/61～63/77 邻接审计；暂定 Ch62 Experimental refine，不能把 active
  verifier 的作者结果外推到 data-analysis contract 之外。GLM-5V-Turbo 又完成 v1/v3 boundary、official
  API/GLM-V/ImageMining/Skills artifacts 与 Ch33～39、44、62、71/73 邻接审计；长期机制是 visual-token
  shape 对 PP/CP/TP、RL stage overlap、bin-packing 与 context state 的反向约束，owner 从 Ch21/38 修正为
  Ch34，暂定 Experimental refine。Synthetic Computers 也完成 v1/PDF（含 retrospective Appendix）、
  Microsoft Research publication、官方 Hugging Face dataset/schema/artifacts 与 Ch23/62/71/73/76～78/80
  邻接审计；其长期机制是从 task-only synthesis 演进为 environment/state synthesis，再由 evolving file graph、
  跨日 event history 和 scoped derived skills 形成可回放闭环。论文的 1,000-run/100-computer 叙述、当前
  98-computer artifact、setup/work/judge 同源和 data-dependent rubric 共同限制外推，故只暂定 Ch77
  Experimental refine。Step-Audio-R1.5 最后完成 v1/v2、official repository、三套 benchmark 的 schema、
  prompt 与 scorer contract，以及 Ch27～30/38/62 邻接审计。其 text-only output 和全部 S2T evaluation
  无法测量报告宣称的 prosody/naturalness，且没有 RLVR/RLHF controlled ablation、直接 human study 或
  training contract，故 owner 从 Ch38 修正为 Ch27，最终为 `No Change — Claim–Evidence Mismatch`。
  World-R1 已覆盖 v1/v4、官方 code/dataset、camera-noise state、3D/VLM/aesthetic reward services、
  periodic objective/data switching、完整 evaluation contract 与 Ch28～30/61～63 邻接；暂定 Ch29
  Experimental refine，reward/evaluation shared ontology 仍限制外推。Tuna-2 已覆盖 v1/v2、project page、
  当前官方 code、pixel-space architecture、mask/data-mixture/evaluation contract 与 Ch4～6/23～24 邻接；
  由于 v1/v2 配比冲突、v1 HTML temporal anomaly、paper-run weights/recipe 未开放，维持
  `Disputed Revision Integrity / Experimental`，潜在 owner 为 Ch5，但不进入 Books。Conversational User
  Simulation survey 也已完成 v1 全文、taxonomy、evaluation、limitations/ethics 与 Ch61～63/71～74/77
  邻接审计；23/30，因 Ch62 已拥有 population/subject/simulator/scorer/calibration contract，Ch71/73 已拥有
  history/memory/drift/provenance，结论为 `No Change — Already Covered`。Perceval 也已完成 CVPR/arXiv v1、
  official code/checkpoints、token-span advantage、truncate/regenerate、evaluation/sensitivity 与 Ch28～30/62
  邻接审计；26/30，暂定 Ch29 Experimental refine，但 PRM span accuracy 未独立校准，作者的 self-reported
  hallucination plateau 不能证明没有 reward hacking。扩展队列原包括 ReVSI、Turning TIDE、computer-use
  step-level optimization、InteractWeb-Bench 与 FlashRT；其中 Turning TIDE 已完成 v1 全文/Appendix、official
  code/model/data、TIDAL/CompDemo/Reverse CALM 两条 pipeline、training/evaluation contract 与
  Ch24～26/30/40 邻接审计；26/30，暂定 Ch25 Experimental refine。其 0.6B/512-token/two-teacher 范围、
  aggregate 小幅收益、无多 seed/compute matching，以及单 H100 contract 下 same-size AR 更快的结果，均
  阻止把 dLLM 写成普遍替代。Step-level Optimization 随后完成 HTML/PDF、缺失于 HTML 的 Appendix
  prompts、StepWise detector weights、event-driven route/verification、evaluation 与 Ch57～59/61～63/76～80
  邻接审计；28/30，暂定 Ch77 Experimental refine。所称 hysteresis/bounded recovery 没有公开实现，
  overlapping-window 80/20 split 也未说明是否 trajectory-grouped，故不外推 benchmark economics。
  InteractWeb-Bench 随后完成 v1 HTML/PDF、完整 prompts、project/repository/data、四种 synthetic persona、
  hidden-answer user、self-defined verification 与 model-judge contract 及 Ch61～63/73～77 邻接审计；25/30，
  因 Ch62 已拥有相同 feedback/evidence/calibration 边界而为 `No Change — Already Covered`。FlashRT 随后
  完成 v1 全文/Appendix、current author code、selective forward recomputation、context-subsampled
  gradient、stagnation resampling、完整 evaluation/sensitivity 与 Ch22/49～51/67～69 邻接审计；28/30，暂定
  Ch68 Experimental refine。其四 H100/BF16/white-box target-output 结果不能写成一般 Serving KV 优化或
  deployment incident probability。ReVSI 随后完成全文、Appendix、visibility/frame-budget/dummy-video
  contract、official artifact 与 Ch61～63 邻接审计；28/30，暂定 Ch62 Experimental refine。它支持将
  observation transform 纳入 input identity，并以 evidence-removal counterfactual 测量先验依赖；不支持把
  ranking reversal 外推为通用 3D reasoning 能力。新恢复队列包括 Visual Generation survey、Verifier-Based
  RL、Meta-CoT、FAMA、terminal task synthesis、reasoning controllability、Zero-to-CAD、step-level
  advantage selection、onchain agent controls 与 Semi-DPO；Step-Level Advantage Selection、Semi-DPO 与
  Onchain Operating-Layer Controls、Visual Generation survey、Meta-CoT、Compliance versus Sensibility 与
  Zero-to-CAD、FAMA 与 Terminal Task Synthesis 均已审；Edit-R1 已移入 2025 backlog。Kubernetes v1.36
  controller staleness mitigation 又完成 official design、client-go v0.36.0 cache API 与 Ch53/54/63
  邻接审计；27/30，暂定 Ch53 Version-Grounded refine。它只证明四类 built-in controllers 的
  read-your-writes guard 与观测 API，不证明 global linearizability 或所有 custom controllers 已受保护。
  Suspended Job mutable resources 也完成 official blog、Jobs concept、feature-gate/API reference 与
  Ch56/59/60 邻接审计；28/30，暂定 Ch56 Version-Grounded refine。其长期边界是 execution 前受控
  resource negotiation、resume 后冻结；4→2 GPU 仅为说明性示例，不证明训练拓扑、收敛、成本或 fairness。
  Tiered Memory QoS 又完成 feature Blog、QoS/resource/cgroup v2 与 kernel docs、Ch59/63/67 邻接审计；
  27/30，暂定 Ch67 Alpha/Version-Grounded refine。它把 request 下沉为 hard/soft reclaim protection，
  并将 throttling 与 reservation 解耦；没有 workload benchmark，故不证明减少 OOM、提高 utilization 或
  改善 latency。In-place Pod-level scaling 又完成 feature Blog、resize task/status docs 与 Ch53/56/59
  邻接审计；28/30，暂定 Ch53 Version-Grounded refine。它显式区分 spec intent、node-admitted
  `allocatedResources` 与 applied `status.resources`，不证明 recommendation 正确、无中断或优于 recreate。
  Pod-Level Resource Managers 随后完成 feature Blog、resource-manager/feature-gate docs 与
  Ch53/56/59 邻接审计；28/30，暂定 Ch59 Alpha/Version-Grounded refine。它把 aggregate Pod budget
  分解为 exclusive slices 与 shared remainder，并暴露 scope、quota、persistent pool 与 checkpoint rollback
  contract；官方材料没有 workload benchmark，不能外推 ML throughput、tail latency 或 utilization。
  至此首轮显式恢复的 4 个 Kubernetes resource-management families 均已审。Broader index 的 7 个
  相邻条目也已完成日期/Source Family 分流：Manifest Admission、Sharded List/Watch 与 DRA 属于 W19，
  PSI 与 Workload-Aware Scheduling 属于 W20，Agent Sandbox 属于 W12；Gateway API v1.5 的 release
  属于 W09、4 月 21 日 article 只是 W17 publication node。它们不进入 W18 denominator。earlier-week
  spillbacks 只记入 backlog，不回拉 forward cursor。其余 HF 标题与 fixed-source lists 仍待 date/dedup，故 W18
  Discovery Recall 与 Evidence Gate 继续打开。Agentic World Modeling、ClawMark 等已归 W17；Sapiens2、
  DIVERT、Memanto、AgentSearchBench 等 earlier-week spillbacks 进入 backlog，不回拉 forward cursor。
  Microsoft Research 固定源又恢复 4 月 30 日 multi-agent network red-team，并完成 official report、
  100+ Agent internal-platform contract、四类 attack cases、qualitative emergent defense、mitigation/
  evidence boundary 与 Ch68/78/80 邻接审计；28/30，暂定 Ch78 Experimental refine。它证明指定
  platform 上存在 propagation、reputation amplification、Sybil verification capture 与 proxy-chain
  invisibility，不给出普遍攻击率、model ranking 或防御有效性。NVIDIA 固定源又恢复 4 月 30 日
  TileGym cross-DSL kernel translation，并完成 official Blog、Python/Julia semantic mapping、17-rule
  skill、static validator、CPU-reference tests、reported-run contract 与 Ch45/77 邻接审计；24/30，因
  Ch77 已拥有相同长期 contract，结论为 `No Change — Already Covered`。repository 未独立核验，单次
  GEMM 的 4-minute/78K-token 结果不能外推为通用 productivity 或 correctness。
  Historical Books Gate 继续关闭。固定机构扫描又恢复 xAI Custom Voices 与 ERNIE-5.1 Preview：前者
  完成 announcement、current API、两阶段 enrollment、team-scoped artifact lifecycle 与 Ch67～69 邻接
  审计，24/30，暂定 Ch68 Version-Grounded refine；后者只有 4 月 30 日 leaderboard announcement，
  15/30，保留为 Product/Leaderboard Fact，不借 5 月正式发布材料反向补写机制。Mistral 官方索引随后
  恢复 4 月 27 日 Workflows public preview；announcement、当前 workflow/activity/event/deployment/
  security docs 与 Ch76～80 已完成联合审计，28/30，结论为 `No Change — Already Covered` / Ch77。
  Z.ai 固定源又恢复 4 月 30 日 Scaling Pain incident report；PD abort/RDMA completion/KV reuse、HiCache
  read-before-ready、speculative anomaly telemetry、LayerSplit、evaluation contract 与 Ch19/44/50～52/63
  已完成审计，29/30，暂定 Ch51 Version-Grounded refine。Amazon Science 固定源随后恢复 4 月 29 日
  privacy-training-data reproduction；全文、related-primary entry points、三类 disclosure surfaces、DP/MPC
  layering、evidence limits 与 Ch63/67～69 已完成审计，24/30，因 Ch68 已完整覆盖而为 `No Change —
  Already Covered`。同一索引的 C3LLM official explanation 已联读 20 页 v3 论文，但 arXiv v1 为
  2025-10-04，故归入 2025 backlog，不在 W18 重复计分。OpenAI、Apple、Ai2、DeepSeek、NVIDIA、
  Amazon、Cohere、Qwen Code 与 MiniMax 官方索引边界也已记录。PyTorch fixed-source pass 另恢复
  AutoSP 与 LightSeek-SMG：AutoSP 完成 arXiv v1 全文、compiler rewrite、sequence-aware
  rematerialization、evaluation/ablation 与 Ch22/24/32～36 邻接审计，28/30，暂定 Ch33 Experimental
  refine；LightSeek-SMG 完成官方 engineering report、CPU/GPU ownership、gRPC/tokenizer-cache/routing、
  benchmark contract 与 Ch38/46/49/52/58/67/80 邻接审计，27/30，暂定 Ch38 Experimental refine。
  两项 repository surface 都没有绕过当前访问权限，作者实现与最大 benchmark 不被外推。IBM Research
  固定源又恢复 4 月 29 日 Granite 4.1 release；announcement 已全文读取，Language、Vision、Speech、
  Guardian、Embedding 五类产品进一步按机制拆成 7 个 source-family reviews，避免以 bundle 或单一 Speech
  行隐藏不同 state machines。Language 已完成
  official technical article、3B/8B/30B cards、8B config/history、training/evaluation 与章节邻接审计，24/30，
  暂定 Ch24 Version-Grounded refine；512K training exposure 不再与 131,072 released contract 混写。其余
  Vision 也已完成 card/config/history、ChartNet v1/dataset、multi-depth/spatial feature injection、training/
  evaluation 与章节邻接审计，24/30，暂定 Ch17 Experimental refine；current 4.2M dataset 及后发 subsets
  未倒写为 launch training manifest。Speech NAR 也完成 NLE sole-v1 全文、current card、conditional-editing
  控制流、matched CTC/AR experiment、全部 ablations/sensitivity/error/limitations 与 Ch38～41/44/62 邻接
  审计；27/30，暂定 Ch40 Experimental refine。NLE、NLE++ 与 current artifact 的 data/projector/LoRA/
  batch contract 已分离，27× 不外推到其他 workload。Speech AR 也完成 current card、2025 predecessor
  architecture paper 与 W11 Self-Speculative paper全文，覆盖 dual-head/importance pooling、Q-Former modality
  alignment、174K-hour data/task schema、relaxed verification 与安全/评测边界；26/30，暂定 Ch5 Experimental
  refine。4.1 artifact、earlier paper runs 与 current runtime examples 保持分离。Speech Plus 随后完成 current
  card、SAA 与 In-Sync 两篇 related paper 的全文审计，覆盖 structured speaker/time output grammar、session/
  prefix/client state、synthetic data lineage、baseline/ablation、malformed-output 与 Ch5/38/40/62 邻接；26/30，
  暂定 Ch38 Experimental refine。当前 2B artifact 与两篇 8B paper 的 architecture、长度、timestamp encoding
  和 evaluation contracts 保持分离，incremental decode 不外推为 bounded-compute streaming。Guardian 又
  完成 current card/docs、2024 predecessor paper、risk/policy prompt grammar、score formula、data lineage、
  OOD/BYOC/function/RAG/JETTS evaluation 与 Ch62/68/69/77 邻接审计；26/30，暂定 Ch68 Version-Grounded
  refine。4.1 claims 与前代机制已拆分，thinking trace 与 vendor score 不等于 calibrated safety guarantee。
  Embedding 最后完成 current 97M card、W20 later-public paper、pruning/vocabulary/multi-teacher KD、完整
  retrieval/speed/context/dependency evaluation 与 Ch22/45/62/71～73 邻接审计；27/30，暂定 Ch72
  Version-Grounded refine。April artifact 与 May paper 没有混写，Transformers dependency 引起的 throughput
  regression 保留为 runtime contract evidence。Granite 七个 mechanism families 至此全部审完。Kimi
  model-evolution 与 MiniMax model-release surface 也已完成日期边界核对；Hugging Face Blog 另补回
  DeepInfra provider integration（19/30）和 NVIDIA/Siemens Raw2Insights-US（17/30）两个低分 families，
  均完成 source/date/rejection 核验且不增加 `20+` review 分母。其余具名机构、framework/
  RFC/PR 与 academic cross-index 尚未闭合，因此 W18 Gate 仍保持打开。framework release pass 随后恢复
  vLLM v0.20.0 与 Transformers v5.7.0：前者完成 official release、stale request-slot、tenant cache salt、
  IR/kernel dispatch、HMA/offload/NIXL 与 Ch41～52 邻接审计，29/30，暂定 Ch46 Version-Grounded refine；
  后者完成 release、长生成 PR #45530、tag-pinned Continuous Batching API/architecture 与相同章节邻接审计，
  26/30，暂定 Ch42 Version-Grounded refine。独立页面不可访问的 PR 只保留 release/docs 级事实。
  SGLang v0.5.10 按 4 月 6 日分回 W15；该检查点结束时 W18 为 75 scored families、69 个 `20+` 且
  69/69 Full Source Reviews，Discovery/Evidence Gate 仍因剩余 fixed-source 与 academic cross-index
  保持 Open。
- 2026-08-10 W18 daily-page replay checkpoint：Hugging Face 2026-04-27～05-01 daily pages 的逐日
  重放证明 weekly landing-page pass 仍漏候选。Diffusion Templates 已完成唯一 v1 全文、框架/训练/
  model-zoo/evidence boundary 与 Ch54～56 邻接审计；28/30，暂定 Ch55 Experimental refine，Ch26/45
  handoff。Refinement via Regeneration 随后完成唯一 v1、官方 current repository/inferencer/model card、
  experiments/ablations 与 Ch22～24 邻接审计；27/30，暂定 Ch23 Experimental refine，Ch25/62 handoff。
  其 semantic-alignment 结果没有外推为 identity/locality、multi-round convergence 或 production cost 结论。
  Mutual Forcing 随后完成唯一 v1、全部 method/experiments/appendices、official project、demo-only repository
  与 Ch24～26 邻接审计；28/30，暂定 Ch25 Experimental refine，Ch38/40 handoff。4/8 NFE、25 秒和 FPS
  只保留为作者实验，不外推；所谓 teacher-free 也保留 online fake-model state 边界。当前 W18 为 78 scored
  families（56 high / 16 mid / 6 low），72/72 当前 `20+` Full Source Reviews。Co-Director 随后完成唯一
  v1、全部 method/evaluation/appendices/prompts、current official code 与 Ch62/76～78 邻接审计；27/30，
  `No Change — Already Covered` / Ch77。T=4 MAB 只保留作者实验，factored reward 的 judge-attribution/
  forced-correlation 边界没有被写成 causal credit。当前 W18 为 79 scored families（57 high / 16 mid / 6 low），
  73/73 当前 `20+` Full Source
  Reviews。MAIC-UI 随后完成唯一 v1、全部 method/evaluation/appendices、current official implementation
  与 Ch62/76～78 邻接审计；28/30，`No Change — Already Covered` / Ch77。论文与 current code 支持
  human-selected element scope、structured intermediate state 与 diff-first patch 的可实现性；full-system
  lab comparison 没有隔离组件因果贡献，单校 observational deployment 也不能证明学习收益。当前 W18
  为 80 scored families（58 high / 16 mid / 6 low），74/74 当前 `20+` Full Source Reviews。GoClick 随后
  完成唯一 v1、全部 method/evaluation/limitations、current official repository/model/data/eval surfaces 与
  Ch10/23/62/74～78 邻接审计；28/30，暂定 Ch10 Experimental refine。L20、batch 1、BF16 的 latency 与
  frozen-trajectory Step SR 只保留为作者 workload evidence，不外推真实 mobile SLO 或 online task success。
  当前 W18 为 81 scored families（59 high / 16 mid / 6 low），75/75 当前 `20+` Full Source Reviews；但 denominator
  未冻结，另有 7 个已确认在窗 families 等待评分/全文审计，EmbodiedMidtrain、
  DiagramBank、IndustryAssetEQA 等仍待 primary-date reconciliation。How Much Is One Recurrence Worth
  按 4 月 22 日 v1 归 W17，4 月 27 日 v2 只记 revision node；另外十项 earlier hits 也分流至 W16/W17
  backlog。AutoGUI-v2 随后完成唯一 v1、51 页主文/Appendix、current official repository、公开 dataset
  surfaces 与 Ch61～63/75/77 邻接审计；27/30，`No Change — Already Covered` / Ch62。它提供 static
  functionality/hard-negative evaluation evidence，不提供真实 action、multi-step planning 或 task-success
  evidence。W18 当前为 82 scored families（60 high / 16 mid / 6 low），76/76 当前 `20+` Full Source Reviews，
  ElementsClaw 经 arXiv submission history 核验为 4 月 26 日 W17 v1 / 4 月 29 日 W18 v2 revision node，
  不在 W18 重复计分。X-WAM 随后完成 v1 全文/Appendix、项目页、current later-release artifact、evaluation
  contract 与 Ch9～10/20/38/62 邻接审计；28/30，暂定 Ch10 Experimental refine。其 modality-specific
  completion deadline 与 coupled noise schedule 形成长期机制候选，但 predicted RGB-D 不等于 causal world
  state，6 月才发布的 code/checkpoints/datasets 也不能倒写为 W18 同步 artifact。W18 当前为 83 scored
  families（61 high / 16 mid / 6 low），77/77 当前 `20+` Full Source Reviews。ExoActor 随后完成唯一 v1、
  case/failure/ablation/latency/discussion、Appendix prompts、项目页及 404 code boundary 审计；24/30，
  `No Change — Already Covered` / Ch10。它支持 modular representation handoff 与 error amplification，
  但没有任务/trial denominator、success rate、uncertainty 或可复现 artifact。W18 当前为 84 scored families
  （61 high / 17 mid / 6 low），78/78 当前 `20+` Full Source Reviews。Representation Fréchet Loss 随后完成
  唯一 v1、全部 appendices、current official repository surface、population estimator、evaluation contract 与
  Ch23～25/62 邻接审计；29/30，暂定 Ch62 Experimental refine。论文支持 population window 与 gradient
  window 解耦，也暴露 stale Queue/EMA state 和 scorer-as-loss 的 Goodhart surface；不支持把 FD-SIM 或
  one-step 写成通用优势。W18 当前为 85 scored families（62 high / 17 mid / 6 low），79/79 当前 `20+`
  Full Source Reviews；该过程快照中的 ViPO 与 Safety Drift 当时都因 primary text / author artifact 不可读而
  保持 `Unverified / Blocked Backlog`。2026-08-13 ViPO 已恢复并完成 Full Source Review，当前只剩 Safety
  Drift 未评分且不计入 review denominator。用户于 2026-08-11 明确授权暂时标记后跳过，因此 forward cursor 已进入 W19；W18 Historical
  Evidence Gate 与 Historical Books Gate 仍保持关闭，后续 backlog sweep 必须回补两项。
- 2026-08-12 W19 fixed-source checkpoint：W19 已从 3 个 baseline 扩展为 35 个 scored families；
  ARIS、HeavySkill、T2PO、PhysicianBench、OpenSeeker-v2、Reasoning-Intensive Retrieval、Workspace-Bench、
  AI co-mathematician、Auto Research with Specialist Agents、A2TGPO、STALE、UniPrefill、LLMs Improving LLMs、
  HyperEyes、Soohak、MCP-Cosmos、MemPrivacy、Geometry Conflict、GPT-5.5 Instant、EMO、ERNIE 5.1、
  Kubernetes Manifest Admission、Declarative Validation、Server-Side Sharded List/Watch、DRA 1.36、
  NCCL Inspector、vLLM 0.20.1～0.20.2 与三项 baseline 合计完成 `30/30` accessible `20+`
  Full Source Reviews；NSF OMAI 完成 1/1 低分来源与机制边界核验。MolmoAct2 因 paper full text 当前不可访问转入
  `Unverified / Blocked Backlog`；OpenSearch-VL、Skill1、StraTA 同样因 primary text 当前不可访问
  转入 blocked backlog。当前 scored candidate review queue 无 pending；四项 blocked source 与尚未闭合的
  cross-index discovery surface 留在 post-forward backlog，因此不宣称 W19 Historical Evidence
  Gate 通过；fixed official/Infra checkpoint 已通过，forward cursor 保持在 W20 之后的既有位置。新增完成项均已覆盖全文、evaluation/appendix 与章节邻接审计；
  STALE、UniPrefill、LLMs Improving LLMs、HyperEyes、MemPrivacy 与 Geometry Conflict 分别暂定 refine
  Ch73、Ch39、Ch77、Ch29、Ch68 与 Ch25；后两项标记 `Experimental`。Geometry Conflict 只支持
  state-relative/global geometry 是方法相关的诊断与 merge control candidate，不支持把 isolated pairwise
  conflict 写成统一因果解释；其正文 `+5.78` 与表格 `+1.44` 的 1.7B 增益冲突不得进入 Books。
  ARIS 已覆盖
  三层 architecture、cross-model review、三阶段 evidence-to-claim audit、skill/wiki/workflow
  implementation、meta-optimization、deployment evidence、limitations 与 Appendix A～E。其单条
  overnight run 只是 observational evidence；compute-matched cross-family benchmark 仍是 future
  work。W20 推荐流中的 MemPrivacy、Soohak、LLMs Improving LLMs、HyperEyes、MCP-Cosmos、
  Geometry Conflict、STALE 与 UniPrefill 已按 v1 归回本周。ARIS、HeavySkill、T2PO、PhysicianBench、
  Reasoning-Intensive Retrieval、Workspace-Bench 分别暂定 Ch77、Ch78、Ch29、Ch62、Ch72、Ch62 refine；
  OpenSeeker-v2 暂定 No Change / Ch23。这些只作为 provisional disposition，Historical Books Gate继续关闭。
  EMO 暂定 Ch21 Experimental refine，强调 modularity 必须由 objective 与 selection contract 共同形成；
  Kubernetes 四项机制分别恢复 bootstrap policy、validation shadow/takeover、controller-state partition 与
  device readiness/fallback 的控制面演进；NCCL Inspector 暂定 Ch63 refine；GPT-5.5 Instant、vLLM patch
  series 与 NSF OMAI 分别只形成 source-family no-change、version evidence 与 availability boundary。
- 2026-08-12 W20 fixed-source checkpoint：W20 已从 2 个 baseline 扩展为 31 个 scored families；
  30 项达到 `20+`，29 项 accessible Full Source Reviews 完成，Qwen-Image-2.0 转入
  `Unverified / Blocked Backlog`，current-review queue 无 pending，forward cursor 已进入 W21。
  MinT 已覆盖 30 页 technical report、Appendix、公开 SDK/runtime/cookbook、adapter revision 与
  policy record 分离、training/rollout/export/serve/rollback state ownership、Scale Up/Down/Out、
  workload/SLO contract、native-vLLM compatibility caveat 与 aggressive prewarm negative result。
  δ-mem、SDAR、Long-Context VLM Beyond 128K、RubricEM、BetaPRM 与 RTPurbo 也完成全文审计；
  RTPurbo 的两阶段训练各约 600 steps，H20 数字仅为 attention operator microbenchmark，不能把标题
  或局部 speedup 外推为百步总训练或端到端 serving speedup。
  WildClawBench 又完成 v1 全文、所有 evaluation/limitations appendices、current repository、container/
  grader contract 与 Ch62/61/63/68/77/80 邻接审计。它确认 model、harness、tools、budget、environment
  与 scorer 共同定义 Agent evaluation subject；5-task human-judge case study 不足以把 GPT judge 泛化为
  真值，故 disposition 为 `No Change — Already Covered` / Ch62。
  ToolCUA 也完成唯一 v1、全部 implementation/limitations appendices、project/repository/model/eval surface
  与 Ch74/29/62/68/77 邻接审计。它把 hybrid action-space expansion 识别为 trajectory-level branch-policy
  问题；synthetic next-state grounding 不等于真实 API execution，success-gated path reward 也不证明全局最优
  或安全最短路径，故暂定 `Refine — Existing Argument` / Ch74，`Status: Experimental`。
  MemEye 与 Anti-Self-Distillation 也完成全文、Appendix、artifact 与章节邻接审计。前者的 stronger-caption
  ablation 表明 raw-image advantage 依赖 caption policy/detail budget，真正稳定的是 evidence granularity 与
  temporal authority 的分层诊断；后者把 privileged-context log-ratio 解释为 conditional PMI，但其 `2～10×`
  只表示 optimizer-step first-reach ratio，且 nonlinear JSD shaping 不自动继承 linear PMI 的 telescoping。
  两者分别暂定 Ch62 与 Ch29 `Refine — Existing Argument / Experimental`。
  Video2GUI 也完成 30 页 v1、全部 appendices、project repository、后续 WildGUI release/schema 与
  Ch23/22/24/74/75/77 邻接审计。它把 observation-derived GUI trajectory 建模为 metadata filter、video
  scorer、segment annotation、high-resolution grounding 与 three-task pretraining 的 compiler chain；当前
  repository 未公开完整 pipeline code，6 月 personally reprocessed dataset 的 94.2M rows 也不得与论文
  12.7M task trajectories 混算。它暂定 Ch23 `Refine — Existing Argument / Experimental`。
  π-Bench 随后完成 v1/v3 全文、全部 appendices、官方 benchmark artifact 与 Ch62/61/63/73/75/77
  邻接审计。它把 proactive requirement discovery 与 final workflow completeness 拆为两个 outcomes，
  并以 persistent workspace、hidden-intent state machine 与 hybrid artifact/tool verification 实现；但
  oracle-like simulated user 会补齐全部 intents，Proc 又没有 false-positive、越权或 harm penalty，因此
  高 Proc 不能外推为更安全或更高 user value。它暂定 Ch62 refine / Experimental。
  HarnessAudit 最后完成 v1/v2 全文、implementation appendices、官方 repository/dataset 与
  Ch62/68/74/77/78/80 邻接审计。它把 harness 形式化为 agents/tools/resources、permission、
  information-flow 与 coordination protocol，并通过 hidden post-hoc policy artifacts、normalized append-only
  trace 与 backend/workspace snapshot 分离 boundary、fidelity 和 stability。Table 2/正文最高总分、91/94
  tool count、S@T threshold 三处不一致，加上单次 run 与未按 opportunity/length 归一化的 violation count，
  使具体排行榜标记 `Disputed Accounting`；长期 mechanism 暂定 Ch62 refine / Experimental。
  EVA-Bench 又完成 v2 全文、A～R Appendices、官方 code/data 与 Ch62/61/63/65 邻接审计。其长期机制是
  生成式 user simulator 也必须拥有独立 validity gate，并把 pass@1、pass@k 与 pass^k 分别绑定平均、peak
  与重复可靠性；bot-to-bot、mock tools、commercial simulator 与日志时序不能替代真人/生产证据，故暂定
  `Refine — Existing Argument` / Ch62，`Status: Experimental`。
  EvolveMem 也完成唯一 v1、全部 Appendix、current implementation surface 与 Ch73/72/74/62/77 邻接审计。
  它把 retrieval configuration 建模为区别于 facts 的 derived policy revision，并用 per-question evidence、bounded
  proposal、best-so-far、revert 与 stagnation exploration 管理离线演化；但未清楚分离 evolution 与 final-test split，
  extraction-quality ablation 又远大于移除 self-evolution 的增益，故只暂定 Ch73 refine / Experimental。
  MemLens 随后完成 63 页 v1、A～I appendices、官方 evaluation code、memory-agent adapters、dataset/schema
  与 Ch62/72/73/17/22/23 邻接审计。其 durable contribution 是把 original multimodal evidence、write-time
  representation、retrieval、answer-time representation 与 judge 分层，并用 image/oracle-retrieval ablation
  区分 fidelity、retrieval 与 reader failure；27 个 LVLM/full-789 与 7 个 agents/195-subset、异构 input adapters、
  proxy image-token accounting、synthetic dialogues 与 partial judge audit 阻止把 leaderboard 外推成通用架构
  优劣。论文没有实现 hybrid architecture，故只暂定 Ch62 refine / Experimental，Books Gate 继续关闭。
  fixed official / Infra replay 又补齐 Kubernetes PSI、Workload-Aware Scheduling v1alpha2、Service
  `externalIPs` deprecation、Mixed Version Proxy Beta、CCM route-sync metric、OpenAI TanStack incident、
  cross-conversation safety summaries、NVIDIA Fleet Intelligence、Vera Rubin agentic-inference scale-up contract、serving pipeline contract 与 Transformers
  v5.8.1。长期候选分别定位 Ch63、Ch60、Ch68、Ch53、Ch68/73 与 Ch63/68；route-sync counter、serving
  checklist 和 patch release 分别为 No Change、No Change 与 Version Fact。所有新项都保留官方事实、
  evaluation boundary、未披露项和旧方案适用条件；没有据此修改 Books。
  W21 curation feed 又恢复 6 个 v1 日期属于 W20 的 spillbacks，并已回拨本周。MinT 暂定 Ch55
  refine，但 Historical Books Gate 继续关闭。
- 2026-08-09 W21 recovery checkpoint：W21 已从 3 个 baseline 扩展为 25 个 scored families；
  25 项均为 `20+`；SkillsVote 与 LongLive-2.0 因 primary text 当前不可访问转入
  `Unverified / Blocked Backlog`；WorldKV 又因 15 MB full paper 当前无法完整取得而转入同一 backlog。
  当前 `21/21` accessible Full Source Reviews 完成、0 项 current-review pending；W21 forward Evidence Gate
  已通过，forward cursor 进入 W22。OpenComputer 已覆盖
  full paper、主要实验、self-evolving verifier ablation、limitations、Appendix case studies、公开
  artifact 与 Ch62/77/80 邻接审计。它把 verification 从末端 scorer 提升为 environment/task synthesis
  的先决约束，并保留 checkability bias、schema drift、checker regression 与 visual criteria 边界；
  暂定 Ch62 refine。HRM-Text 已覆盖唯一 v1 全文、Appendix、MagicNorm/truncated-credit 机制、
  task-formatted data、matched-compute/architecture/objective ablations、contamination、公开实现入口与
  Ch16～18/23～25 邻接。它暂定 Ch17 `Refine — Existing Argument / Experimental`：参数共享的双时间尺度
  recurrence 与 PrefixLM、response-only loss 是联合合同，不能用异构 baseline headline 宣称普遍优于
  标准 Transformer。Code as Agent Harness 已覆盖 1,208-line HTML 全文、三层 taxonomy、PEV control、
  adaptive harness、shared-state/convergence、open problems 与 companion bibliography；因无 systematic-
  review protocol、统一实验或 executable artifact，且其稳定主张已由 Ch62/74/75/77/78/80 具体覆盖，
  disposition 为 `No Change — Already Covered` / Ch80。6 个 first-public date 属于 W20 的条目未在 W21
  重复计分。DelTA 已覆盖唯一 v1、Appendix A～L、gradient-proxy/centroid derivation、完整 evaluation
  contract、ablation/sensitivity/overhead、当前 veRL-based artifact surface 与 Ch28～30 邻接；它暂定
  `Refine — Existing Argument / Experimental` / Ch29。其 repeated-generation significance 不是 multi-seed
  training evidence，额外 actor forwards、batch composition 与 proxy bias 保持显式边界。两个 blocked
  candidates 均不阻塞 forward cursor，待 W30 sweep 后重试。OSCAR 已覆盖 35 页 v1、全部理论/系统/
  实验 appendices、official SGLang-based artifact 和 Ch40～43/45/50 邻接；它暂定
  `Refine — Existing Argument / Experimental` / Ch41，并记录 calibration 文档冲突、frozen-error theory、
  mixed-precision page lifecycle、H100-specific kernel/workload 与 prefix identity 边界。EnvFactory 已覆盖
  唯一 v1、全部 appendices、official environment/data/model/training surface 与 Ch62/74/77/79/80 邻接；
  它暂定 Ch77 `Refine — Existing Argument / Experimental`，并明确区分 generated artifact self-consistency
  与真实 API conformance，保留 failed-call filtering、simulator/judge correlation、isolated-session throughput、
  MCP-Atlas subset、paper/repository data-unit 差异和 Appendix H 伪代码歧义。Mix-Quant 已覆盖唯一 v1、
  完整 phase-aware quantization method/ablation、two-commit official repository、pinned vLLM/NIXL launch path
  与 Ch39～41/45/50～52 邻接；它暂定 Ch51 `Refine — Existing Argument / Experimental`，把 role-specific
  precision/artifact 与 KV compute provenance 纳入 PD handoff identity，同时明确作者约 3× 只属于 RTX 5090
  isolated Prefill latency，不证明 TTFT/TPOT/goodput 或同预算 topology 胜负。ACC 随后完成 v1/v2、
  Appendix A～F、dataset/checkpoint cards 与 Ch22～25/62/77 邻接审计，暂定 Ch23
  `Refine — Existing Argument / Experimental`。它把 successful interactive trajectory 转换为 derived
  direct-answer long-context data，而不是继续训练原 action policy；answer-verified selection、random
  shuffle、SWE privileged-patch rationale、question-only leakage test 与 post-hoc attention/router selection
  均保持显式证据边界。GoLongRL 随后完成唯一 v1 的 39 页全文、全部相关 Appendix、official
  training/evaluation repositories、dataset/checkpoint cards 与 Ch22/23/28～30/62 邻接审计，暂定 Ch29
  `Refine — Existing Argument / Experimental`。它把 capability-native reward 的 scale、within-task difficulty
  与 task sampling mass 拆为三个控制面；task-level normalization 不能修复样本量失衡。model-solvability
  filtering、benchmark-guided dataset revision、query-only 13-gram overlap、单次训练、30B 无算法消融、
  evaluation alignment 差异与 YaRN 1M 混杂均保持显式边界。WorldKV 只完成 official project/repository
  artifact-level 核验；camera-pose retrieval、GPU/CPU KV bank 与 anchor/novelty compression flags 可确认，
  但约 2× throughput、full-KV fidelity、完整 evaluation/ablation/limitations 不据摘要外推。它不计 Full
  Source Review，也不阻塞 cursor。PlanningBench 随后完成 v1/v2、27 页 v2、全部 Appendix、official
  one-commit repository、467-row evaluation data/license 与 Ch23/24/61～63/76～78 邻接审计；其最终
  disposition 为 `No Change — Already Covered` / Ch62，Ch23 仅 data-pipeline handoff。task/constraint
  taxonomy、generator/responder/critic difficulty loop、All-pass/Avg-pass 与 determinate optimum 是有用受限
  案例，但 Ch23/62 已拥有 constraint-derived data、shared verifier blind spot、rubric formation、criterion
  execution 和 global-validity boundary；未发布 300-row training data、single critic、default inference、
  hardware/seed/statistics 与 benchmark-as-reward channel 仍是证据限制。Gated DeltaNet-2 随后完成唯一 v1、
  Appendix A～E、official seven-commit implementation surface 与 Ch14～15/17/22/39～40/45 邻接审计；
  channel-wise decay、key-side erase/read 与 value-side write 被拆为三个 state-control planes，并以 compact-WY
  chunk training、gate-aware backward、fp32 state/solve policy 与 recurrent Decode kernel 闭环。其最终为
  Ch22 `Refine — Existing Argument / Experimental`，而 1.3B/100B-token、4K training、2K SWA、single-H100、
  无 multi-seed 与 Decode-SLO 的条件阻止通用化。Post-Trained MoE/ZEDA 又完成 v1/v2、Appendix A～D、
  official 16-commit training/evaluation surface、两份 checkpoint cards 与 Ch21/25/40/45/52 邻接审计；
  parameter-free zero routes、frozen-teacher SFT→OPD、group-level balancing 与 no-renormalization 共同把已完成
  post-training 的 static top-k MoE 迁移为 token-dependent active-expert count。它暂定 Ch21
  `Refine — Existing Argument / Experimental`；作者约 20% 只属于单 H200、8192 sequence、concurrency 32、
  256 training-prompt examples 的 phase throughput，不是 TTFT/TPOT/goodput 结论。SkillOpt 随后完成
  v1/v2、Limitations、Appendix algorithm/prompt contracts、official repository/docs/releases 与
  Ch62/73/76/77/80 邻接审计；它把 Skill 明确为由 bounded edits、rejected evidence、selection gate 与
  slow/meta state 管理的外部 optimization artifact，暂定 Ch80 `Refine — Existing Argument / Experimental`。
  single split seed、repeated selection queries、同 scorer 驱动 gate/final evidence、有限 transfer、未披露
  hardware/API snapshot/multi-run variance 和 Skill security lifecycle 阻止把 `52/52` 外推为通用结论。
  Foundation Protocol 又完成唯一 v1、完整 architecture/scenario/Appendix reference stack、official protocol/
  application repositories 与 Ch68/69/77～80 邻接审计。其 seven-object/four-plane/checkpoint/evidence spine
  是 early architecture proposal；没有 benchmark、formal threat model、interop/conformance/fault/scale evidence，
  且稳定观点已被现有章节具体拥有，故为 `No Change — Already Covered` / Ch80。下一检查点进入 SciAtlas；
  SciAtlas 随后完成唯一 v1、KG schema/index/prompt appendices、current official client/CLI/API surface 与
  Ch72/23/62 邻接审计。其 lexical/semantic/title tri-path recall、typed graph expansion、RWR reranking 与
  source/derived-state separation 暂定 Ch72 `Refine — Existing Argument / Experimental`；论文没有 quantitative
  retrieval benchmark、baseline/ablation、hardware/cost/load/freshness SLO，current repository 又无 event-time
  tag，且 12-vs-11 edge schema、author identity、`RELATED_TO` provenance、无向 citation、popularity/language/
  PDF selection bias 均保持显式边界。QUEST 的 official project/repository/model/data surface 虽可访问，
  但 28.7 MB full paper 无 HTML，当前 permitted path 无法完整取得；它转入 `Unverified / Blocked Backlog`，
  不计 Full Source Review，也不阻塞 cursor。ThriftAttention 随后完成唯一 v1、完整 method/kernel、
  LongBench/RULER/HELMET/PG19 contract、sparse/selector ablation、Limitations、current official artifact 与
  Ch39～41/45/50 邻接审计。它把 uniform FP4 与 support-pruning sparse attention 之间再分出 block-wise
  precision allocation：per-query-block selector 提升少量 key blocks 到 FP16，其余保持 NVFP4，并在同一
  online-softmax state 合并。该机制暂定 Ch45 `Refine — Existing Argument / Experimental`；单 RTX PRO
  6000、batch 1、未披露 output/concurrency/SLO、下游无 multi-seed/CI，以及 dual cache 多 28% footprint
  阻止把 aggregate quality recovery 与 latency headline 外推为生产结论。SkillEvolBench 随后完成唯一 v1、
  完整 protocol/results/capacity/cost/family catalog、current runnable repository/dataset surface 与
  Ch62/73/76/80 邻接审计。它用 acquisition/replay/frozen deployment 和 context-shift/adversarial/composition
  分解，将 local repair 与 transferable procedure 分开；Raw-Trajectory control 与 forced Tier-3 ablation 共同
  表明当前瓶颈是 selective abstraction，而非单纯 library capacity。暂定 Ch73 `Refine — Existing Argument /
  Experimental`；co-designed family/seed/verifier、无 multi-seed/uncertainty、未披露 hardware/token/runtime、
  provider/harness confound 与长期 drift 阻止通用化。NITP 随后完成 v1～v3、完整 method/theory/experiments/
  Appendix、official repository 与 Ch23～25/17 邻接审计；其 `t -> t+1` shallow-state stop-gradient cosine
  objective 暂定 Ch24 `Refine — Existing Argument / Experimental / Revision-sensitive`。local GGN/alignment/
  projector assumptions、未披露 hardware/precision/multi-seed、repository 尚未发布 implementation code，以及
  v1 45B Appendix 在 v2/v3 被移除，均保持为显式证据边界；
  W22 feed 又回收 SkillOpt、Foundation Protocol、SciAtlas、QUEST、ThriftAttention 与 SkillEvolBench
  六项 W21 spillbacks；W23 feed 回收 NITP v1 05-24。Historical Books Gate 继续关闭。
- 2026-08-12 W21 fixed-source checkpoint：W21 现为 31 个 scored families（19 high / 11 mid /
  1 low）；30 项达到 `20+`，其中 26 项完成非模板化 Full Source Review，SkillsVote、LongLive-2.0、
  WorldKV、QUEST 四项保留 `Unverified / Blocked Backlog`，1 项低分边界完成，current-review queue
  为 0。新增 OpenAI layered content provenance、NVIDIA verified Agent Skills、Slurm topology-aware
  scheduling simulation、Agent evaluation guide、Transformers v5.9.0 与 token-metered reference
  architecture。前三项分别暂定 Ch68、Ch80/68 与 Ch59 refine；Agent evaluation 已被 Ch62 具体覆盖，
  Transformers 仅为 Version Fact，token-metered 条目为低分商业/reference-architecture boundary。
  W21 fixed official / Infra checkpoint 通过；academic cross-index 与四项 blocked retry 仍使 Historical
  Evidence Gate 保持 Open，Historical Books Gate 保持 Closed。
- 2026-08-09 W22 recovery checkpoint：W22 已从 3 个 baseline 扩展为 37 个 scored families；
  36 项达到 `20+`，当前 `9/9` accessible Full Source Reviews 完成、27 项 blocked backlog、0 项
  current-review pending，1 个低分 governance fact；W22 forward Candidate Evidence Gate 已通过，cursor 进入 W23，
  但 broader discovery 与 Historical Evidence Gates 仍保持 Open
  已核验。ScientistOne/Chain-of-Evidence 的 v1 归 W22；其全文、Appendices、audit procedure、
  failure taxonomy、limitations 与 Ch62/77 邻接阅读已从 W31 source-family audit 归正到本周，07-30
  official article 仍只属于 W31 publication node。它是 Ch62 已吸收内容的章节级去重，不新增 Books。
  Gamma-World 已覆盖唯一 v1、完整论文与 Appendix、NVIDIA project、后发官方 artifact 和
  Ch10/13/14/40 邻接，暂定 Ch10 `Refine — Existing Argument / Experimental`；two-player training、
  qualitative four-agent/robot evidence、未披露数据与不完整 24-FPS contract 保持为显式边界。
  AgentDoG 1.5 只能核验唯一 v1 metadata/abstract/44-page surface，完整 primary text 当前不可读；W08
  trajectory audit 中的 AgentDoG judge 不能替代本篇审计，故转入 `Unverified / Blocked Backlog`，不阻塞 cursor。
  DVAO 已覆盖唯一 v1、全文与三项理论 proof、dual-objective experiments、implementation/limitations 和
  Ch28～30 邻接；暂定 Ch29 `Refine — Existing Argument / Experimental`。其 variance-adaptive weighting
  仍保留 base weights，只在 `G=16` dual rewards 上验证；small-group/noisy-high-variance reward、三目标以上、
  multi-seed/CI、code 与 compute overhead 保持为显式边界。
  OmniRetrieval 已覆盖唯一 v1、完整 method/evaluation、official current repository/code path 与 Ch71/72/74
  邻接；暂定 Ch72 `Refine — Existing Argument / Experimental`。它保留 heterogeneous KB 的 native
  search/SQL/SPARQL/Cypher operators，经 top-k routing、native execution 与 late evidence selection 统一接口；
  但 single-gold-source evaluation、single-best-candidate selector 不证明 cross-source join，freshness、ACL、
  schema drift、query safety、partial failure、provenance 与 production SLO 也未被验证。
  MobileGym 已覆盖 v1/v2 revision、完整正文/Appendices、official project/repository 与 Ch61～63/29/80
  handoff；暂定 Ch62 `Refine — Existing Argument / Experimental`。它把 authoritative structured environment
  state 同时用于 configure/reset/fork、deterministic judging、side-effect diff 与 RL reward；但 browser surrogate
  舍弃 real backend/stochastic service/完整 feature surface，59-task outcome-stratified real-device subset 只构成
  transfer existence proof，不能外推为完整 Sim-to-Real contract。
  BES 已覆盖唯一 v1、全部 Appendices、theory assumptions、三类 evaluation、ablation/cost、official
  project/repository 与 Ch19～21/29/75/77 邻接；暂定 Ch20 `Refine — Existing Argument / Experimental`。
  它把 expansion-only candidate support 扩展成可重组 trajectory pool，并用 backward goal tree 稠密化
  selection，但 entropy-shell escape 不等于 correctness，exponential advantage 依赖 independent subgoals、
  reliable decomposition/verifier/recombination；最大 8B post-training、三项 3-seed program search 与不完整
  compute accounting 也阻止通用化。
  ResearchMath-14K 已覆盖唯一 v1、全部 Appendices、current official dataset/schema/files/history 与
  Ch22～25/62 邻接；暂定 Ch23 `Refine — Existing Argument / Experimental`。它把 source quote、
  self-contained rewrite、mutable status evidence、teacher attempt 与 filter verdict 分开；但 current artifact
  未见 220K/5K/code/adapters，filter 定义、split/card、license/status supersession、benchmark decontamination
  与完整 LoRA contract 均未闭合，因此不能把 incorrect attempts 一般化为可信 supervision。
  How LoRA Remembers? 的 arXiv HTML/PDF 被当前保存的访问权限明确拒绝，且仓库无可审计本地正文或作者 artifact；
  它转入 `Unverified / Blocked Backlog`，不计 Full Source Review、不分配 Books owner、不推断标题暗示的机制，也不阻塞 cursor。
  MemTrace 的 arXiv 与 Hugging Face paper surface 同样被保存权限拒绝，本地无对应正文或作者 artifact；它也转入
  blocked backlog，不把 taxonomy、trace attribution、overhead 或 intervention pending focus 当作论文结论。
  CUA-Gym 的 arXiv 与最直接 QwenLM/CUA-Gym official artifact surface 亦被保存权限拒绝，本地无对应材料；
  它转入 blocked backlog，不由产品或仓库 identity 反推 environment、verifier、reward 或 RL 机制。
  LaRA 只列出同一受限 arXiv primary-source surface，且本地无正文或作者 artifact；它转入 blocked backlog，
  不把 layer-wise geometry、contamination protocol、RL-vs-SFT controls 或 false positives 的 pending focus 写成结论。
  FluxMem 同样只有受限 arXiv paper surface 与没有 release/commit identity 的 `planned code` 占位，本地无 paper/code/
  artifact；它转入 blocked backlog，不从名称推断 connectivity、feedback、pruning 或 consolidation 机制。
  Skill0.5 的 Sources 也只有受限 arXiv URL；Pending 表的 `+ code` 没有 repository/release/commit identity，本地无
  artifact，因此转入 blocked backlog，不推断 internalize/externalize router、difficulty/OOD 或 skill conflicts。
  SkillGrad 同样只有受限 arXiv URL 与无 repository/release/commit identity 的 `+ code` 标签，本地无 artifact；
  它转入 blocked backlog，不把 textual gradient、momentum、patch safety 或 held-out regression 当作已验证机制。
  Claw-Anything 只有受限 arXiv URL 且本地无 primary material；它转入 blocked backlog，不从名称推断
  always-on execution、authority/privacy、proactivity metrics 或 environment realism。
  Crafter 的 Sources 只有受限 arXiv URL；`+ code/benchmark` 无 repository/dataset/release/commit identity，
  本地无 artifact，因此转入 blocked backlog，不推断 roles、SVG representation、verifier 或 visual evaluation。
  Domino 的 Sources 同样只有受限 arXiv URL；`+ code` 无 repository/release/commit identity，本地无 artifact，
  因此转入 blocked backlog，不推断 parallel backbone、refinement head、curriculum 或 acceptance/latency contract。
  COLLEAGUE.SKILL 的 `open-source artifact` 也无 URL/owner/release/commit identity，本地无材料；它转入
  blocked backlog，不推断 trace-to-skill、capability/behavior split、correction/rollback 或 measured claims。
  GrepSeek 的 `+ code` 同样无 repository/release/commit/data/model identity，本地无材料；它转入 blocked
  backlog，不推断 Tutor/Planner、GRPO、sandbox、sharding 或 byte-equivalence mechanisms。
  TASTE 的 `+ benchmark` 无 repository/dataset/release/split/version identity，本地无材料；它转入 blocked
  backlog，不推断 tool-sequence generation、judge validity、coverage/difficulty、contamination 或 grader independence。
  Trust-Region Behavior Blending 只有受限 arXiv source 且本地无 primary material；它转入 blocked backlog，
  不推断 KL direction/bound、annealing、prefix distribution、two-setting generality 或 stability。
  Trust Region On-Policy Distillation 同样只有受限 arXiv source 且本地无材料；它转入 blocked backlog，
  不推断 reliable/outlier regions、reverse/forward-KL estimator、mask/clip 或 off-policy guidance。
  LongTraceRL 的 `+ code/data/models` 无 repository/dataset/model/release/commit/version identity，本地无材料；
  它转入 blocked backlog，不推断 trajectory distractors、positive-only rubric、reward hacking 或 contamination。
  dMoE 的 `+ code` 无 repository/release/commit identity 且本地无材料；它转入 blocked backlog，不推断
  block/expert distribution、state ownership、memory traffic、runtime 或 quality/latency contract。
  SkillAdaptor 只有受限 paper surface 与没有 immutable artifact 的 `planned code` 占位；它转入 blocked backlog，
  不推断 fault attribution、skill responsibility、acceptance/rollback 或 benchmark gains。
  Draft-OPD 只有受限 arXiv surface 且没有 supporting artifact；它转入 blocked backlog，不推断
  target-assisted rollout、verification-error replay、on-policy signal 或 acceptance/throughput contract。
  SCOPE 只有受限 arXiv surface 且没有 judge/experiment artifact；它转入 blocked backlog，不推断
  challenger/solver ownership、co-evolution、self-judge、open-ended reward validity 或 compute-matched controls。
  Harness Updating 的 `+ code` 没有 immutable identity 且本地无材料；它转入 blocked backlog，不推断
  updater/consumer separation、activation/following failures、model-tier controls 或 harness identity。
  SAAS 的 `+ code` 没有 immutable identity 且本地无材料；它转入 blocked backlog，不推断 self-awareness
  reward、search-depth shaping、curriculum、accuracy/cost Pareto 或 live-search validity。
  RAMP 的 platform artifact 没有 URL/version/run identity 且本地无材料；它转入 blocked backlog，不推断
  serial workflow identity、staged recovery、utility/resource accounting 或 production transfer。
  Masking Stale Observations 的 trajectories 没有 URL/version/schema identity 且本地无材料；它转入 blocked
  backlog，不推断 inverted-U、retriever/model interaction、token-for-turn trade-off 或 evidence-loss failures。
  ResearchClawBench 只完成 W24→W22 的 v1 日期回拨；其 benchmark/code 无 immutable identity 且本地无材料，
  因而转入 blocked backlog，不推断 research chain、grader validity 或 contamination。
  Smaller Models Are Natural Explorers 只完成 W25→W22 的 v1 日期回拨；其 paper 与 artifact 不可审计，
  因而转入 blocked backlog，不推断 scale→exploration、policy ownership、annealing 或 rollout compute。
  W23 feed 的 16 个 v1 05-26～05-31 families、W24 ResearchClawBench 与 W25 Smaller Models Are
  Natural Explorers 已回流 W22；
  candidate score 与 focused diff check 均通过。
- 2026-08-12 W22 fixed-source checkpoint：W22 现为 43 个 scored families（30 high / 12 mid /
  1 low）；42 项达到 `20+`，其中 15 项完成非模板化 Full Source Review，27 项保留 blocked backlog，
  1/1 low-score boundary 完成，current-review queue 为 0。新增 Dynamo Snapshot、DynoSim、DOCA
  in-silicon security、Vera CPU agentic-workload contract、DSX OS control plane 与 STAC-AI LANG6
  workload-contract case。它们分别暂定 Ch46/53、Ch62、Ch68、Ch50、Ch53/63 refine 与 Ch62 No Change；
  snapshot 的未 upstream/future support、simulation calibration、DPU trust domain、vendor hardware claims、
  IT/OT correlated failure 与 benchmark workload boundary 均显式保留。Historical Books Gate 保持关闭。
- 2026-08-12 W23 fixed-source checkpoint：W23 已从 5 个 baseline families 扩展为 33 个 scored
  families；33 项均为 `20+`，当前 `21/33` current-version Full Source Reviews 完成、0 项 current-review
  pending、12 项 `Unverified / Blocked Backlog`。forward Candidate Gate 按用户确认的 blocked-skip 规则通过，
  cursor 进入 W24；W23 discovery 与 Historical Evidence Gates 仍保持 Open。
  StreamMA v1 event snapshot 与 runnable artifact 进入 blocked backlog，不阻塞后续 queue。On the Scaling
  of PEFT 已完成 43 页 PDF、全部主章节/figures/tables、evaluation、limitations 与 Ch25～27、
  Ch54～56、Ch73 邻接阅读。其稳定贡献是把 adapter 从 trainable tensor/file 扩展为 policy record、
  mutable training session、immutable revision 与 tiered residency，但 controlled benchmarks/
  simulations 不证明百万 personal-model deployment。Code2LoRA 已完成完整 HTML、implementation、
  evaluation、limitations、appendices 与 Ch25/26/55/71～73 审计；其 repository-conditioned adapter 只在
  Python assertion-completion、Qwen2.5-Coder-1.5B 与单 H100 contract 内成立。Harness-1 已完成 63 页
  PDF、state-transition algorithms、SFT/RL recipe、八套 retrieval benchmark、same-model harness control、
  component ablations、limitations 与 Ch71～74/77 审计；其结果不能外推到 adversarial web、open-ended
  research 或通用模型排行。DRIFT/TELBench 已读完整 HTML、annotation pipeline、claim-ledger/support/
  dependency-tracing method、五类模型与四类 harness 评测、消融、token cost 和相关附录；其 corpus 统计
  不等于生产 incident rate，first-error prediction 也不是 authoritative root cause。KVarN 已读完整 v1、
  magnitude/direction decomposition、pseudo-decode、dual-axis variance normalization、2-bit evaluation、runtime、
  limitations 与全部附录；其结果只属于披露模型、layout、sampling 与抽象 GPU contract。Cosmos 3 已读
  139 页 technical report 的 architecture、data/training/Serving、reasoner/generator/action evaluation、消融和
  关键附录，并审计 Ch9/10、Ch13/14/17/18、Ch23/24、Ch62/75；其稳定贡献是统一 token interface 内仍保留
  parameter tower、mask/objective、modality clock 与 runtime boundary，不证明生成视频等于因果世界模型。
  AdaPlanBench 已读完整 v2、interaction protocol、data/judge construction、主评测与全部 ablations/human
  validation/limitations，并审计 Ch62/71/73～77；它只支持 synthetic judge-mediated plan revision 下的
  constraint-ledger 与 regression-gate 机制，不证明 embodied execution 或真实 preference adaptation。
  CHERRL 已读完整 v1、全部附录、dual-judge/onset/RHDA control flow、current repository 与数据缺口，并审计
  Ch27～30/62～65/68；它只支持人工注入单一 bias 的 Qwen3-4B 六条 hacking runs 和离线 detector contract，
  不证明真实 composite bias 的 online detection、mitigation 或 rollback。AutoLab 已读完整 v1、全部 task/
  experiment/analysis appendices、官方 project、current repository/task contract 与 commit history，并审计
  Ch62/66/76/77/80；它只支持 36 个 executable tasks、固定 terminus-2、三次 rollout 与 2～12 小时 budget
  contract 下的 long-horizon 证据。persistence 是关联而非独立因果干预，25-task harness ablation 不建立通用
  model/runtime 排名；current main 含 W23 后 v1.1 提交与公开 reference/solution，不能作为事件日 immutable
  artifact，并使未来训练污染成为 live-benchmark governance 问题。因相关机制已由 Ch62 及相邻章节完整拥有，
  disposition 为 `No Change — Already Covered`。StreamMA 已读完整 v2 的 protocol、theorems、
  eight-benchmark/role/tool/scaling/cost experiments、limitations、prompts 与 artifact statement，并审计
  Ch77～79、Ch71/65/66/32。它暂定 Ch78 `Refine — Existing Argument / Experimental /
  Revision-sensitive`：稳定缺口是 communication granularity、partial-progress visibility、arrival order 与
  production failure contract；26.9×、cost Pareto 与 step-level scaling 不外推。由于 v1 正文抓取失败，且
  current official repository 只显示 README/images、缺少 README 所指 `StreamMA.py`，v2 模型/结果不倒写
  W23，代码级 backpressure/completion/cancellation 仍未验证。
  SDPG 已读完整 v1、理论与实验 appendices、当前作者 implementation surface，并联读 Ch25、Ch27～30。
  它把 binary verifier 的 trajectory selection、same-policy privileged-context full-vocabulary reverse KL 的
  local shaping、fixed-reference anchor 与 beta warmup/decay 组合起来；但 paper 没有独立 seeds、matched
  compute/memory、gate/schedule factorial ablation 或错误 privileged context 实验，current repository 也没有
  可定位 event-time release/tag。其 disposition 为 provisional `Refine — Existing Argument / Experimental`，
  owner Ch29；Historical Books Gate 关闭，本轮不修改 Books。
  M3Eval 已读完整 v1、四类 cognitive task construction、dataset/question pipeline、model/human evaluation、
  全部 appendices 与 current official project/repository/dataset surface，并联读 Ch14/22/62/73。它支持把
  long-video aggregate accuracy 拆为 divided attention、interference、interleaving 与 N-Back slices；但
  split-screen、order/recency、hard cuts、source binding、不同 frame budget、未披露 human protocol 与不可审计
  sample/scorer revision 都阻止把结果解释成独立 memory mechanism。Ch62/22 已具体拥有 failure taxonomy、
  evaluation-object identity、slice/confound contract 与 effective-utilization 边界，故 disposition 为
  `No Change — Already Covered / Experimental Case` / Ch62；Ch73 不接收 model-forward working-memory 案例。
  Continual Experience Internalization、Agents' Last Exam、SWE-Explore、Unembedding Matrix Feature Lens、
  Geometry of On-Policy Distillation、Retrospective Harness Optimization、LatentSkill、OpenSkill、When Tools Fail、
  Graph Memory、Program-of-Layers 与 SkillHarness 的 arXiv primary-paper domain，以及需要联读的 GitHub
  artifact domain，均被当前保存的访问策略拒绝；它们转入 `Unverified / Blocked Backlog`。原评分只保留为
  provisional discovery priority，pending focus 全部是“不得推断”的边界，不形成机制证据或 Books owner。
  NVIDIA 05-31 official release 属 W22，W23 只计 06-01 report node。上述候选都只形成 provisional
  Experimental refine，Books Gate 仍关闭。Language Models Need Sleep first public 于
  2025-09，W23 arXiv node 不重复计新事件。W24 display feed 的 Agents' Last Exam、SWE-Explore、
  unembedding lens、on-policy distillation、retrospective harness、LatentSkill、OpenSkill 与
  When Tools Fail、W25 feed 的 Graph Memory/Program-of-Layers，以及 W26 feed 的 SkillHarness 已按 v1 回填 W23。W23
  score arithmetic 与 focused diff check 通过；Historical
  Books Gate 继续关闭。
  fixed official/Infra 重扫新增 SGLang parallel speculative-decoding roadmap、vLLM v0.22.1、
  Transformers LightGlue nested-config RCE disclosure 与 Hugging Face Datasets 5.0.0。四项均完成直接
  primary-source review：SGLang 暂定 Ch44 `Refine / Experimental / Revision-sensitive`，但 current roadmap
  不倒写为事件日实现；vLLM 是 Ch46/53 的 backend-lifecycle patch fact；LightGlue 是 Ch68 已有
  deny-by-default remote-code contract 的 corrective case；Datasets 是 Ch23/62 已有 schema、shuffle、
  checkpoint 与 trace-identity contract 的 breaking version fact。后三项均 `No Change / Weekly Only`；
  Historical Books Gate 未开启，未修改 Books。
- 2026-08-12 W24 fixed-source checkpoint：W24 已从 35 扩展为 38 个 scored families（26 high /
  11 mid / 1 low）；37 项达到 `20+`，`6/37` Full Source Reviews 完成、31 项 blocked、0 项 ordinary
  pending，FastContext 保留 withdrawn low-score boundary。fixed replay 新增 KServe v0.19.0、AA-AgentPerf
  与 NVIDIA FP8 checkpoint→ONNX Q/DQ→TensorRT chain。KServe 暂定 Ch57 `Refine / Version-sensitive`，
  补 applied/observed topology、cache/adapter/routing/migration/readiness/termination state；AA-AgentPerf 暂定
  Ch62/66 `Refine / Live Benchmark`，补 workflow trajectory、tool delay、SLO-constrained concurrency 与
  measured-power boundary；FP8 chain 为 Ch45 `No Change / Bounded Engineering Case`。vLLM v0.23.0 官方
  release date 为 06-15，已归 W25；Historical Books Gate 保持关闭。
- 2026-08-12 W25 fixed-source checkpoint：W25 从 32 扩展为 35 个 scored families（24 high / 10 mid /
  1 low）；新增并完成 vLLM v0.23.0、NVIDIA sync-free MoE fused kernels 与 MLPerf Training v6.0
  primary-source review；该时点为 `7/34` `20+` Full Source Reviews、27 blocked、0 current-review pending，
  已由 2026-08-13 post-forward checkpoint 的 `32/34 + 2 blocked` 状态取代。
  vLLM 暂定 Ch46 `Refine / Version-sensitive`；MoE fusion 暂定 Ch21 `Refine / Bounded Case`，由 Ch36/45
  短接 training runtime 与 kernel execution；MLPerf v6.0 暂定 Ch62 `Refine / Benchmark Contract`。vendor
  microbench、submitter narrative 与 suite owner/rules 已分开，fixed checkpoint 通过并推进 W26；W25 broader
  discovery/Historical Evidence Gates 仍开放，Historical Books Gate 关闭。
- 2026-08-12 W26 fixed-source checkpoint：W26 从 38 扩展为 40 个 scored families（25 high / 14 mid /
  1 low）；新增 DFlash cross-runtime integration 与 TensorRT 11 multi-device inference，两项均完成
  primary-source review；该时点为 `6/39` `20+` Full Source Reviews、33 blocked、0 current-review pending，
  已由 2026-08-13 post-forward checkpoint 的 `37/39 + 2 blocked` 状态取代。
  DFlash 与 W06 algorithm/W16 DDTree 显式去重，只保留 W26 engineering integration node，暂定 Ch44
  `No Change`；TensorRT 11记录 preview→supported、graph-native collectives、rank-local engine/context、
  communicator lifetime、all-rank progress与support matrix，暂定Ch45 `Refine / Version-sensitive`。fixed
  checkpoint通过并推进W27；W26 broader discovery/Historical Evidence Gates仍开放，Books Gate关闭。
- 2026-08-09 W24 recovery checkpoint：W24 已从 2 个 baseline 扩展为 35 个 scored families；
  34 项达到 `20+`，当前 `3/34` Full Source Reviews 完成、0 项 current-review pending、31 项
  `Unverified / Blocked Backlog`；FastContext 撤稿记录为
  17 分。MiniMax Sparse Attention
  已覆盖 30 页论文全部主章节、kernel design、109B matched-training experiment、Related Work、
  Appendices/ablations、作者 repository 以及 Ch21～24/Ch39 邻接章节。其稳定贡献是把 selector
  gradient ownership、GQA-group block granularity、KV-outer execution、hot-block load balancing 与
  dense-to-sparse migration 放进同一 contract；H800 headline 与当前 SM100 artifact 被明确分开。
  8 个 W23、1 个 W22 spillback 和 1 个 2025 cross-year node 已归正；W25/W26 feed 共恢复 12 个 W24
  families。31 项所需的 arXiv primary-paper domain 与部分 GitHub artifact domain 被当前保存的访问策略
  拒绝；原评分只保留为 provisional discovery priority，pending focus 不作机制证据。forward Candidate Gate
  按 blocked-skip 规则通过，cursor 进入 W25；W24 discovery/Historical Evidence Gates 仍 Open，Historical
  Books Gate 继续关闭。
- 2026-08-09 W25 recovery checkpoint：W25 已从 4 个 baseline families 扩展为 32 个 scored families；
  31 项达到 `20+`，当前 `4/31` Full Source Reviews 完成、0 项 current-review pending、27 项
  `Unverified / Blocked Backlog`，Project Fetch 的 18 分
  boundary review 保留。TokenPilot 已覆盖 arXiv v1 全文、公式、global/local state machine、两套
  benchmark、baselines、ablation/sensitivity、Limitations、全部 Appendix、当前 LightMem2 artifact 与
  Ch70～73/Ch66/cache 邻接。其稳定机制是把 Context reduction、prefix identity、recoverable artifact
  与 delayed lifecycle eviction 联合优化；commercial token-cost 结果不外推为 GPU latency/goodput。
  W26 feed 又恢复 14 个 W25 families；其余 spillbacks 已按 v1 回拨 W22～W24。27 项所需的 arXiv
  primary-paper domain 与部分 GitHub artifact domain 被当前保存的访问策略拒绝；原评分只保留为
  provisional discovery priority。forward Candidate Gate 按 blocked-skip 规则通过，cursor 进入 W26；W25
  discovery/Historical Evidence Gates 仍 Open，Historical Books Gate 继续关闭。
- 2026-08-09 W26 recovery checkpoint：W26 已从 4 个 baseline families 扩展为 38 个 scored
  families；37 项达到 `20+`，当前 `4/37` Full Source Reviews 完成、0 项 current-review pending、
  33 项 `Unverified / Blocked Backlog`。Agent-Native
  Memory / MemoryData 已覆盖完整 HTML、四模块 taxonomy、全部 end-to-end RQ、component ablation、
  cost contract、Conclusion、author testbed 与 Ch72～74/80 邻接。其长期结论是 Memory 必须按
  representation/storage、extraction、retrieval/routing、maintenance 分层归因，且没有脱离 workload
  bottleneck 的单一最优结构。原 17 个 later-feed candidates 已按 v1 回拨 W23～W25，W27 display
  feed 又回拨 10 项到 W26。33 项所需的 arXiv primary-paper domain 与部分 GitHub artifact domain
  被当前保存的访问策略拒绝；原评分只保留为 provisional discovery priority。forward Candidate Gate
  按 blocked-skip 规则通过，cursor 进入 W27；W26 discovery/Historical Evidence Gates 仍 Open，
  Historical Books Gate 继续关闭。
- 2026-08-12 W27 fixed official/Infra checkpoint：W27 已从 9 个评分行恢复为 33 个评分行、32 个 unique
  families；23 项 high、10 项 mid，当前 11/32 unique Full Source Reviews 完成、0 项 current-review
  pending、21 项 `Unverified / Blocked Backlog`。
  Program-as-Weights 已覆盖完整 HTML、compiler/interpreter 数据与控制流、Text-to-LoRA 与 prefix
  分支、training contract、baselines/ablations、quantization/local execution、case studies、Limitations、
  public SDK 与 Ch25～27/55/74 邻接。其长期价值是把 adapter 从每任务训练技巧推进为
  specification-compiled、versioned、hot-swappable neural artifact；但 single-step synthetic task、
  opaque binary、compiler/interpreter coupling 与不完整 production SLO 阻止外推。21 项所需的 arXiv
  primary-paper domain 与部分 GitHub artifact domain 被当前保存的访问策略拒绝；原评分只保留为
  provisional discovery priority。fixed replay 新增 Secure Agent Workspace Reference Design 与 TensorRT
  Edge-LLM v0.9.0；前者形成 Ch80 provisional refine（Ch68 handoff），但只作 target reference architecture，
  当前 OpenShell alpha/experimental 状态不倒写；后者只作 Ch45 version fact，不由支持矩阵推断机制。
  fixed checkpoint 通过，cursor 保持 W28；W27 discovery/Historical Evidence Gates 仍 Open，Historical
  Books Gate 继续关闭。
- 2026-08-09 W28 recovery checkpoint：W28 已从 6 个 baseline candidates 扩展为 21 个 scored
  families；10 项 high、10 项 mid、1 项 low，当前 7/21 Full Source Reviews 完成、0 项 current-review
  pending、14 项 `Unverified / Blocked Backlog`。
  LLM-as-a-Verifier 已覆盖 arXiv 全文、verifier decomposition、training/evaluation contract、
  ablations、limitations 与 Ch62/64/65 邻接；其长期价值是把 verifier quality 拆成 criterion
  coverage、evidence grounding 与 aggregation，而不是把单一 reward 当作 correctness。其余候选
  已完成 metadata、v1 date、评分与 owner 定位，但因所需 arXiv primary-paper domain 与部分 GitHub
  artifact domain 被当前保存的访问策略拒绝，转入 blocked backlog，不得视为全文完成。forward Candidate
  Gate 按 blocked-skip 规则通过，cursor 进入 W29；W28 discovery/Historical Evidence Gates 仍 Open，
  Historical Books Gate 继续关闭。
- 2026-08-12 W28 spillback / fixed-source checkpoint：W29/W30 已明确回拨、但 W28 未实际接收的
  ABot-AgentOS、GRASP、Weak-to-Strong Direct OPD、What LLM Forecasters Know、PolicyShiftGuard、
  Root Causes 与 DeepSearch-World 共 7 个 source identities 已补入 W28。当前只能确认 owner week 与
  primary ID，无法稳定打开 metadata/正文，故它们保持 unscored blocked，不从标题补机制、不计 Full
  Source Review。后续 identity repair 又加入 ReflectWorld-MM 与 ReOPD；两者均已完成全文、artifact/
  implementation、评分和相邻章节审计。W28 当前有 23 个可复算评分行、30 个 unique families：9 reviews
  complete、14 scored blocked、7 unscored blocked、0 current-review pending。ReflectWorld-MM 的
  mixed-provenance benchmark、answer-time ablation 与未披露 production contract 均保留为边界。fixed checkpoint 通过；Historical
  Books Gate 关闭。
- 2026-08-12 W30-to-owner attribution checkpoint：W30 列出的 14 个 pre-W30 spillbacks 已完成
  identity/date 归属。RESOURCE2SKILL（2606.29538v1，6 月 30 日）回写 W27；ReflectWorld-MM
  （2607.09759v1）与 ReOPD（2607.04763v1）按 7 月 6 日回写 W28；其余 11 项按 7 月 16～19 日
  回写 W29。ReOPD、ReflectWorld-MM、OPD²、Recursive Harness Self-Improvement、Muon Agentic RL、
  Xiaomi-Robotics-1、DSWorld、Cost-Aware Security Agents、SeerGuard 与 Environment-free API data 随后完成
  全文、artifact/implementation boundary、评分及相邻章节审计；其余 4 项
  继续作为 unscored identity，
  不能计作 Full Source Review 或 Books candidate。
- 2026-08-11 W29 recovery checkpoint 先把 W29 从 6 个 baseline candidates 扩展为 26 个 scored
  families；当时为 9 项 high、17 项 mid、7/26 Full Source Reviews、0 current-review pending、
  19 项 `Unverified / Blocked Backlog`。SearchOS
  已覆盖 arXiv 全文、SOCM shared state、schema-bound evidence extraction、continuous dispatch、
  skills/middleware、evaluation/ablations/appendices 与 Ch62/72/73/76～78/80 邻接。它支持的稳定
  结论是 deep-research orchestration 必须显式拥有 frontier、evidence、coverage 与 failure state；
  作者在特定模型、budget 与 benchmark 上的结果不外推为通用 superiority。其余候选依赖的
  arXiv primary-paper domain 与部分必要 GitHub artifact domain 被当前保存的访问策略拒绝；
  原评分仅为 provisional discovery priority。forward Candidate Gate 按 blocked-skip 规则通过，
  cursor 进入 W30；W29 discovery/Historical Evidence Gates 仍 Open，Historical Books Gate 继续关闭。
- 2026-08-12 W29 OPD² checkpoint：OPD² 完成 v1 全文、公式、三域 14-benchmark evaluation、
  training dynamics、ablation、H100 compute、appendix、official code/recipes 与 Ch27～30/23 审计，
  评分 28/30。W29 更新为 27 scored + 11 unscored / 38 unique，8 reviews complete、19 scored +
  11 unscored blocked。其 provisional Ch29 refinement 把 teacher/base lineage delta 与原 OPD direction
  gate 记录为独立分支；Historical Books Gate 关闭，未修改 Books。
- 2026-08-12 W29 RHI checkpoint：Recursive Harness Self-Improvement 完成 v1 全文、objective/algorithm、
  synthetic repository benchmark、judge/resource contract、component ablations、information-theoretic
  hypothesis、appendices 与 Ch76～78/62 去重，评分 27/30。W29 更新为 28 scored + 10 unscored /
  38 unique，9 reviews complete、19 scored + 10 unscored blocked。其 provisional Ch77 refinement 记录
  trajectory-local harness search 与 contract/hop evolution；Historical Books Gate 关闭，未修改 Books。
- 2026-08-12 W29 Muon checkpoint：Muon Agentic RL 完成 event-time v1 全文与全部 appendices，并将
  7 月 20 日、7 月 30 日、8 月 2 日 revisions 和 official `verl-muon` repository 作为 post-window
  verification 单独核验；评分 26/30。v1 的单 seed / 0.5B / ALFWorld 结果只支持探索性 optimizer-estimator
  interaction，v4 的 multi-seed、scale/transfer 与 RMS-matched control 把结论收窄为特定 KL/clipping recipe
  下的 effective-update-scale headroom，不证明 universal optimizer ranking 或 spectral causality。W29 更新为
  29 scored + 9 unscored / 38 unique，10 reviews complete、19 scored + 9 unscored blocked；provisional Ch29
  refinement 另向 Ch35/31 handoff sharding 与 checkpoint identity。Historical Books Gate 关闭，未修改 Books。
- 2026-08-12 W29 Xiaomi-Robotics-1 checkpoint：完成 v1 全文、model/data/training flow、pretraining scaling、
  real-robot/downstream/simulation evaluation、Related Work 与 Ch23～25/10/62 邻接，并把 7 月 22 日 v2 与
  8 月 3 日 official code/checkpoints 作为 post-window verification 分开核验；评分 27/30。其稳定价值是
  `embodiment-free UMI breadth → embodiment/action-schema/instruction alignment` 的两段 data contract，
  不是 100K-hour headline 或作者 benchmark。W29 更新为 30 scored + 8 unscored / 38 unique，11 reviews
  complete、19 scored + 8 unscored blocked；provisional Ch23 refinement 向 Ch24/25/10/62 短 handoff。
  Historical Books Gate 关闭，未修改 Books。
- 2026-08-12 W29 DSWorld checkpoint：完成 sole-v1 architecture、state/transition ownership、data construction、
  SFT/reflective GRPO、evaluation、limitations、Appendices A～D 与 Ch75～77/10/62 审计；评分 27/30。
  W29 更新为 31 scored + 7 unscored / 38 unique，12 reviews complete、19 scored + 7 unscored blocked。
  provisional Ch77 refinement 保留 exact-execution / learned-simulation fidelity routing、predicted versus
  authoritative state 与 timeout reconciliation；论文约 14× 对 Compiler 的文字和 Table 2 的 335/277 min 冲突，
  anonymous artifact 也不可访问，故 headline 为 `Disputed`。Historical Books Gate 关闭，未修改 Books。
- 2026-08-12 W29 Cost-Aware Security Agents checkpoint：完成 event-time v1 的 evaluation design、
  refusal/cost accounting、Cybench/BOTS results、contamination/scaling、limitations、Appendices A～E 与
  Ch62/66/68 审计；v3 expanded models/provider conditions 只作 post-window verification。评分 28/30。
  W29 更新为 32 scored + 6 unscored / 38 unique，13 reviews complete、19 scored + 6 unscored blocked。
  其 workload-specific operating-point、run cost、policy refusal 与 contamination-control 机制已由 Ch62/66/68
  明确覆盖，故为 `No Change — Already Covered / Experimental Evaluation Case`，未修改 Books。
- 2026-08-12 W29 SeerGuard checkpoint：完成 sole-v1 的双阶段 guard pipeline、SAWM data/training、
  MobileSafetyBench / MobileRisk / Next-State-QA evaluation、ablations、latency、appendices、当前 project/
  repository/model artifacts 与 Ch68/74/77/62/10 邻接审计；评分 27/30。W29 更新为 33 scored + 5 unscored /
  38 unique，14 reviews complete、19 scored + 5 unscored blocked。稳定增量是把 pre-execution semantic
  consequence prediction 放在 instruction filter 与 deterministic authorization 之间，同时保留 actual environment
  state ownership、uncertainty/approval 与 prediction reconciliation；不把作者二元 benchmark、提前拒绝混合后的
  平均 latency 或当前 artifact 状态外推为通用 production claim。只形成 provisional Ch68 refinement，Historical
  Books Gate 关闭，未修改 Books。
- 2026-08-12 W29 Environment-free API data checkpoint：完整阅读 82 页 event-time v1 的 task synthesis、
  per-task/per-app simulated state、deterministic validation、simulator/judge retry、trajectory filtering、
  AppWorld/OfficeBench experiments、yield/failure/coverage、training contract 与全部相关 appendices；v2 和 Apple
  Research page 只作 post-window verification。评分 29/30。W29 更新为 34 scored + 4 unscored / 38 unique，
  15 reviews complete、19 scored + 4 unscored blocked。provisional Ch23 refinement 将 spec-only stateful
  simulation 定位在 static tool examples 与 executable-environment trajectories 之间；write responses 只有结构检查、
  model-judge evidence 无 recall/prevalence、per-app history 不证明 cross-app invariant，故真实 side-effect state、
  sampled execution calibration 与 final evaluation 仍不可替代。Historical Books Gate 关闭，未修改 Books。
- 2026-08-12 W29 remaining-attribution access checkpoint：重新尝试 Distilled RL 的 arXiv HTML/PDF 与
  作者仓库、JoyNexus primary full text、DataFlow-Harness primary full text/artifact，均被已保存的访问策略
  阻断。三项保持 unscored `Unverified / Blocked`，不从摘要推断 reverse importance、multi-tenant batching
  或 typed-DAG mechanism；W29 账目不变，blocked-skip 规则允许 forward sweep 保持在 W30/W31 边界，
  Historical Evidence Gate 仍 Open、Books Gate 仍 Closed。
- 2026-08-13 W29 exact-source checkpoint：arXiv HTML 恢复后，19 个未完成来源中有 15 个完成
  metadata/revision、method、state/control flow、evaluation/ablation、limitations、相邻章节与 disposition
  审计；包括此前归周未闭合的 Distilled RL、JoyNexus、DataFlow-Harness 与 Data-Centric Parallel。
  W29 当前为 38 scored families（21 high / 17 mid）、34/38 Full Source Reviews、0 ordinary pending、
  4 explicit blockers：Multi-Agent Exploration、AI Scientist Capability、Generative Compilation、LongStraw。
  forward Candidate Gate 通过并抵达 W30；broader Historical Evidence Gate Open、Books Gate Closed。
- 2026-08-12 forward-terminal / backlog-sweep checkpoint（过程快照，已被 2026-08-13 recovery 覆盖）：W31 与 W32 均重新核对完整 Monday～Sunday
  Daily 覆盖；当时 W32 的 44 scored families、24 Full Source Reviews、16 blocked、2 unscored discovery gaps
  与 0 ordinary pending 账目一致，因此 forward sweep 已抵达截至本次运行最新结束的完整 ISO Week W32。
  这只关闭 forward cursor，不关闭全历史 Evidence Gate。post-forward sweep 随即从最早开放周重试：W13
  ClawKeeper 以及 W14 `Backdoor Attacks on Decentralised Post-Training` / `Cactus` 仍无法取得可核验
  primary identity/text，保持 unscored blocked；W15 GameWorld 的 abstract/HTML/PDF/project/repository 与 W18
  ViPO / Safety Drift 的精确 arXiv/author-artifact 入口也已顺序重试，仍未取得完整 primary paper text。
  W16/W17 没有 ordinary pending；W19 的 MolmoAct2、OpenSearch-VL、Skill1 与 StraTA 又完成一次精确
  arXiv/title/ID access retry，仍未返回正文，因此保持 scored-but-blocked。backlog cursor 继续进入 W20；
  W20 Qwen-Image-2.0 的 arXiv PDF、official repository 与等价镜像也已重试，46 MB report 仍无可读正文，
  因此保持 24/30 blocked。W21 SkillsVote、LongLive-2.0、WorldKV 与 QUEST 的精确 HTML/PDF/题名/ID入口
  随后也已重试，仍没有完整 primary text；WorldKV/QUEST artifact 不替代论文。backlog cursor 进入 W22；
  Books Gate 继续 Closed。
- 2026-08-12 W22 post-forward backlog checkpoint：按 Agent/Memory、Skill/Serving、RL/Evaluation 三批，
  逐项重试周报 ledger 中 27 个 blocked candidates 的精确 arXiv HTML。全部入口仍未返回可验证正文；
  discovery scores、review denominator、owner 与 disposition 均不变。W22 保持 15/42 reviewed + 27 blocked，
  Historical Evidence Gate Open、Books Gate Closed；post-forward cursor 进入 W23。
- 2026-08-12 W23 post-forward backlog checkpoint：逐项重试 12 个 blocked families 的精确 arXiv HTML，
  并单独重试 StreamMA v1 PDF；全部入口仍未返回可验证正文。W23 保持 21/33 current-version reviews、
  12 blocked 与一个 v1/artifact sub-gap；post-forward cursor 进入 W24，Books Gate 继续 Closed。
- 2026-08-13 W24 post-forward backlog checkpoint：逐项重试原 31 个 blocked families 的精确 arXiv
  identity，29 项 HTML 全文恢复并完成非模板化 Full Source Review、evaluation/limitation boundary、
  相邻章节审计与 provisional disposition。W24 现为 35/37 `20+` reviews，只有 VIA-SD 与 Agentic
  Environment Engineering survey 保留 `Unverified / Blocked Backlog`，0 ordinary pending；post-forward
  cursor 进入 W25。W24 Historical Evidence Gate 仍 Open，Historical Books Gate 仍 Closed。
- 2026-08-13 W25 post-forward recovery checkpoint：逐项重试 27 个 blocked identities，25 篇 arXiv HTML
  正文恢复并完成非模板化 Full Source Review、evaluation/limitations、相邻章节与 provisional disposition；
  LLM-Designed Training Environment 与 MemGUI-Agent 仍无可验证正文。W25 现为 32/34 completed、
  0 ordinary pending、2 blocked；JetSpec 旧账名已按论文标题统一为 JetFlow。post-forward cursor 进入 W26，
  W25 Historical Evidence Gate 仍 Open，Historical Books Gate 继续 Closed。
- 2026-08-13 W26 post-forward recovery checkpoint：逐项重试 33 个 blocked identities，31 篇 arXiv HTML
  正文恢复并完成非模板化 Full Source Review、method/evaluation/limitations/关键 Appendix、相邻章节与
  provisional disposition；AOHP 与 Self-Compacting Agents 仍无可验证正文。W26 现为 37/39 completed、
  0 ordinary pending、2 blocked；post-forward cursor 进入 W27，W26 broader Historical Evidence Gate
  仍 Open，Historical Books Gate 继续 Closed。
- 2026-08-13 W27 post-forward recovery checkpoint：逐项重试 21 个 scored blocked families 与 1 个 unscored
  RESOURCE2SKILL identity，20 个 scored papers 和 RESOURCE2SKILL HTML 正文恢复并进入 Full Source Review
  queue；仅 AgenticSTS 仍无可验证正文。W27 当前为 11/32 scored unique reviews、20 scored + 1 unscored
  recovered pending、1 scored blocked；post-forward cursor 固定 W27，Historical Books Gate 继续 Closed。
- 2026-08-13 W27 post-forward Full Source Review checkpoint：上述 20 个 recovered scored papers 与
  RESOURCE2SKILL 均完成非模板化全文审计，覆盖机制/状态/数据流、evaluation contract、limitations 或公开
  披露缺口、相邻章节和逐项 disposition。RESOURCE2SKILL 由 unscored identity 正式评分为 28/30；W27
  现为 34 score rows / 33 unique families，24 high / 10 mid，32/33 unique `20+` Full Source Reviews、
  0 ordinary pending、1 blocked（AgenticSTS）。Forward Candidate Evidence Gate 按 explicit-backlog 规则
  通过并推进 W28；W27 broader discovery/Historical Evidence Gate 仍 Open，Historical Books Gate Closed。
- 2026-08-13 W28 post-forward Full Source Review checkpoint：精确重试 14 个 scored blocked 与 7 个 unscored
  spillback identities；其中 11 + 7 篇正文恢复并完成 method/evaluation/limitations/相邻章节与 disposition，
  七个 spillbacks 全部正式评分。W28 现为 30 scored families（19 high / 10 mid / 1 low）、27/30 Full Source
  Reviews、0 ordinary pending、3 blocked（AgentLens、UP、Ideas Have Genomes）。KVpop、SAO、Linear
  Attention、SDM、proactive memory、world/VLA、ABot-AgentOS、Direct OPD、STRACE、DeepSearch-World 等
  形成 provisional refine；GRASP、forecast probe、PolicyShiftGuard、Infinite Worlds、UniClawBench 由现有章节
  去重。Forward Candidate Evidence Gate 通过，cursor 保持 W29；broader Historical Evidence Gate 与 Books
  Gate 仍分别 Open / Closed。
- 2026-08-11 W30 recovery checkpoint：W30 已从 8 个 baseline candidates 扩展为 25 个 scored
  families；11 项 high、13 项 mid、1 项 low，当前 9/25 Full Source Reviews 完成、0 项
  current-review pending、16 项 `Unverified / Blocked Backlog`。
  OpenForgeRL 已覆盖 arXiv 全文、harness/proxy/sandbox/orchestrator/policy-server ownership、
  rollout reconstruction、task synthesis、Claw/GUI contracts、cross-harness evaluation、limitations
  与 Ch28～30/62/77/78/80 邻接。其稳定信号是训练 runtime 必须保留 deployment harness identity；
  但 task synthesis、teacher、harness、RL 与 evaluator 的耦合阻止把作者结果外推为通用结论。
  其余候选依赖的 arXiv primary-paper domain 与部分必要 GitHub artifact domain 被当前保存的
  访问策略拒绝；原评分只保留为 provisional discovery priority。forward Candidate Gate 按
  blocked-skip 规则通过，cursor 进入 W31；W30 discovery/Historical Evidence Gates 仍 Open，
  Historical Books Gate 继续关闭。
- 2026-08-13 W30 exact-source checkpoint：此前 16 个 blocked candidates 均从精确 arXiv HTML
  恢复并完成 non-template Full Source Review；W30 当前为 25 scored families（11 high / 13 mid / 1 low）、
  25/25 reviews、0 blocked、0 ordinary pending。14 个 pre-window identities 也已完成 W27/W28/W29
  owner-week attribution 与 owner-week review 对账。forward sweep 抵达 W30 历史边界；broader discovery/
  Historical Evidence Gate 仍 Open，Historical Books Gate Closed，本轮未修改 Books。
- 2026-08-09 source-family normalization checkpoint：W15 已从 3 行恢复为 4 个独立 families，
  W17 从 3 行恢复为 5 个，W23 从 3 行恢复为 5 个，W25 从 3 行恢复为 4 个，W26 从 3 行
  恢复为 4 个；每项均有独立 score、date/evidence boundary 与 disposition。Project Fetch 因只有
  三次 trial 从合并 22 分中拆出为 18 分；GPT-5.6 preview 从 telemetry report 中拆出为 19 分。
  W13 的 TRIBE v2 / SAM 3.1 也已拆成两个低分 families；DSPA、DRTriton 与
  `TRITON_MLA_SPARSE` 完成后，当前 26 个 score rows 均有对应 review/boundary record。W27 的
  Seed2.0 packet 经标题规范化后可由机器计为
  8/8 unique reviews。上述规范化不关闭各周
  discovery replay，也不打开 Historical Books Gate。
- W31 Live Weekly 已在 2026-08-09 复核：7/7 Daily 均存在，24/24 score totals 可复算，Daily links、
  Coverage Limitations、跨周去重、Books Decision、Markdown 与 focused diff check 通过。W31 继续保持
  Live Weekly 完成状态，与 W13～W30 尚未闭合的历史 discovery gates 分离。
- W32 Weekly 已在 2026-08-12 完成 coverage repair：7/7 Daily 存在；48 个 Daily score rows 经跨日与
  跨周去重后对应 44 个 unique families（21 high / 21 mid / 2 low）。8 月 9 日 Daily 从单一 Beyond
  Routing 扩展为 10 个 source families；Tangent、subjective reasoning / RLVR、Business Arena、PIRL、
  pre-pretraining stability、activation steering、carbon-aware fine-tuning 与 AquiLLM 完成全文后，W32
  Full Source Reviews 达到 24，普通 pending 清零。15 项 paper 与 KServe
  mechanism review 保持 `Unverified / Blocked Backlog`；ElastiCo / OasisKV 保持 unscored discovery-only
  gaps。W32 Evidence Gate 继续 Open，Historical Books Gate 继续关闭。
- W32 forward archive checkpoint 随后按用户确认的 blocked-skip 规则通过：16 个 blocked families 与
  ElastiCo / OasisKV 两个 unscored discovery-only identities 均保留在 backlog，普通 Full Source Review
  pending 为 0，单向游标已追到当前最新完整 ISO week。这里的“追到最新”只表示 forward sweep 没有
  静默遗留可访问候选；它不关闭 W01～W32 的 Discovery / Historical Evidence Gates，也不打开 Books Gate。
- 2026-08-13 W18～W23 ledger checkpoint：六周评分行逐项复算均无 Total 差异；当前账目分别为
  W18 `85 / 79 reviewed + 2 unscored blocked`、W19 `35 / 30 reviewed + 4 scored blocked + 1 low`、
  W20 `31 / 29 reviewed + 1 scored blocked + 1 low`、W21 `31 / 26 reviewed + 4 scored blocked + 1 low`、
  W22 `43 / 15 reviewed + 27 scored blocked + 1 low`、W23 `33 / 21 reviewed + 12 blocked`，普通
  pending 均为 0；StreamMA 另保留 event-time v1/artifact sub-gap。Blocked 不冒充 Full Source Review，
  也不拉回 forward cursor；六周 broader Historical Evidence 仍 Open、Books 仍 Closed。
- 2026-08-13 W24～W30 与 Live W31～W32 continuity checkpoint（恢复前过程快照）：W24～W28 已完成 exact-source
  recovery 后的非模板化 review 与 blocked-ledger 对账，W29/W30 分别为 `34/38 + 4 blocked` 与
  `25/25 + 0 blocked`；该快照中 W31 的 7/7 Daily 与 24/24 scores、W32 的 7/7 Daily、44 unique scores、
  24 reviews、16 blocked、2 unscored gaps 与 0 ordinary pending 均保持一致。Forward cursor 因而已到
  2026-W32，但这只是 archive checkpoint，不是 all-history Evidence Gate 或 Books Gate pass。
- 2026-08-13 final material-ledger checkpoint（后发状态，覆盖上方过程计数）：ViPO、Qwen-Image-2.0、
  W21 四项、W22 二十七项、Continual Experience Internalization、VIA-SD、AgenticSTS、ElastiCo、
  OasisKV、TAOT 与 KServe v0.20.0 已恢复并完成 Source Review。当前可复算 archive 为 1143 rows
  （707 high / 383 mid / 53 low），`Review Pending = 0`；仍需用户材料的 41 个唯一 items 已集中列入
  `W01～W32 Remaining Primary-Source Material Ledger`。其中 36 个为 source families、1 个为 StreamMA
  revision/artifact sub-gap、3 个为 W32 identity gaps、1 个为年度 Scholar/OpenAlex discovery export。
  Historical Evidence Gate 因这些材料与 cross-index
  recall 继续 Open，Historical Books Gate 继续 Closed。
- 下方 `Baseline Final Disposition Ledger` 继续冻结 discovery-recall 前的 93-row baseline，供新旧候选数
  对账；在所有 W01～W30 修复完成前不做局部累加，不把尚未重算的年度总量写成当前事实。

## Current Provisional Recovered Ledger

这份账本与下方 93-row baseline 分开：baseline 记录修复前系统曾经承认的候选，当前账本记录每份
Weekly 文件此刻实际存在、且六维分数可复算的 candidate rows。它仍然不是 final discovery census；
任何 `Discovery Gate Open` 的周都可能继续增加候选。

| Window | Scored Rows | 25–30 | 20–24 | Below 20 | Gate Meaning |
| --- | ---: | ---: | ---: | ---: | --- |
| W01～W12 | 407 | 243 | 144 | 20 | 已完成大规模恢复；W12 新回拨 vLLM MoE expert-weight tiering；W07 SPEED-Bench Full Review complete；W11 普通 pending 清零并新增完成 Scientific Taste、AgentProcessBench、V-JEPA 2.1 与 KServe v0.17.0；五个 blocked items 保留 backlog，FineRMoE 路由回 2025；其他 spillback/blocked 项仍按各周记录 |
| W13～W30 | 666 | 428 | 210 | 28 | ViPO 恢复后 W18 增加 1 个 high-score row；W28 30 rows、W29 38 rows、W30 25 rows 已纳入复算；全文审计仍未闭合 |
| Historical W01～W30 | 1073 | 671 | 354 | 48 | Provisional recovered ledger；Historical Books Gate Closed |
| Live W31 | 26 | 13 | 10 | 3 | 7/7 Daily；ResKV / SLIM 按 07-31 v1 回拨并完成 Full Source Review |
| Live W32 | 44 | 23 | 19 | 2 | 7/7 Daily；36 paper Full Source Reviews；3 blocked identity gaps；0 ordinary pending / discovery gap；candidate checkpoint passed，broader Historical Evidence Gate Open |
| Archive W01～W32 | 1143 | 707 | 383 | 53 | 只用于算术对账，不表示 all-history Evidence Gate 已通过 |
| Live W33 | 25 scored + 32 discovery pending | 22 | 3 | 0 | 原 21 项 + 4 correction Full Reviews；32 项尚未评分/去重；Gate reopened |
| Archive W01～W33 | 1168 scored + 32 discovery pending | 729 | 386 | 53 | provisional arithmetic；W33 correction 未闭合，不是 final census |

结构复核同时确认：W08 的 23 个评分候选现在有 23 个对应 review/boundary packets；W09 有 62 个
in-window score rows，另有 3 个全文读取后移出本周的跨周去重 packets；W27 的 34 个 score rows 只对应
33 个 unique source families，因为 Seed2.0 在两个来源组重复计分。三种差异均为显式关系，不再用简单的
“评分行数 = Review 标题数”误判。

## Coverage Map

| Weeks | Calendar Window | Main Evidence Cluster |
| --- | --- | --- |
| W01～W05 | 2025-12-29～2026-02-01 | behavior specification、data sampling、multi-agent scaling |
| W06～W10 | 2026-02-02～2026-03-08 | conditional computation、capacity scheduling、agent telemetry、model/system cards |
| W11～W15 | 2026-03-09～2026-04-12 | accelerator co-design、workflow-aware serving、quantization、evaluation、full-duplex runtime |
| W16～W20 | 2026-04-13～2026-05-17 | scalable oversight、synthetic data、Agent memory、privacy、interpretability、sustainable scheduling |
| W21～W26 | 2026-05-18～2026-06-28 | executable evaluation、private telemetry、long-term memory、dual-use workflow、MTP |
| W27～W30 | 2026-06-29～2026-07-26 | asynchronous PP、MoE-aware routing、speculation scheduling、stateful selection control plane |
| W31 | 2026-07-27～2026-08-02 | semantic KV、claim-level provenance、explicit protocol state、bounded Agent repair |
| W32 | 2026-08-03～2026-08-09 | typed state、conditional graph factorization、Agent testing adequacy、causal repair、workflow resource contracts |
| W33 | 2026-08-10～2026-08-16 | 原三条路线保留；discovery correction 新增 generation/transport、scientific-workflow authority、process evidence 与 world-state memory 待综合 |

## Live Weekly Ledger

| Week | Daily Coverage | Main Decisions | Books |
| --- | --- | --- | --- |
| [W31](2026-W31/README.md) | 7/7（2026-07-27～2026-08-02） | 26 scored；ScientistOne official node；ResKV / SLIM 按 07-31 v1 回拨并完成 Full Source Review；Anthropic cryptanalysis 仍为受限 Weekly evidence | 原 Daily 决策保持；ResKV / SLIM 只形成 Experimental candidates，Historical Books Gate closed |
| [W32](2026-W32/README.md) | 7/7（2026-08-03～2026-08-09）；08-09 retrospective recovery + 08-13 blocker recovery | 44 unique families；36 paper Full Source Reviews；3 blocked identities；0 pending / discovery gap；typed state、P/D/A/F accounting、Agent testing、safe commitment、skill/memory 与 off-HBM KV 演进重建 | 验证 Daily refinements；恢复候选只形成 provisional dispositions，不修改 Books |
| [W33](2026-W33/README.md) | 7/7 + 08-17 correction | 25 scored Full Reviews；32 Discovery Review Pending；原三条演进链保留，correction Gate reopened | 原 16 Refine / 5 No Change 保留；correction 为 3 No Change / 1 Books Pending；暂无新 Books 写入 |

## Cross-Week Evolution Routes

### Agent Execution and State

```text
W05 task-aware multi-agent topology
→ W08 autonomy becomes production telemetry
→ W12 serving optimization expands from request to workflow
→ W17 experience becomes retrieved memory
→ W23 long-term memory becomes synthesis and consolidation
→ W21～W25 evaluation moves from answers to executable/physical artifacts
→ W31 protocol state becomes explicit and runtime topology repair stays bounded
→ W32 goals become typed contracts and repair/skill artifacts become auditable
→ W33 derived state becomes selectively retrievable, repairable and transactionally activated
```

这些节点不是一条单一产品路线。W05、W08、W12 是 Agent system 的 `Direct Evolution` 候选；
W17 与 W23 是不同 memory owner 下的 `Principle Reuse`；W21～W25 位于 evaluation /
external-action layer，与 inference serving 是 `Layering / Dependency`。

### Evidence and Governance

```text
W04 behavior specification / representation
→ W09 runtime persona and malicious workflow
→ W14 rater uncertainty and behavioral evaluation
→ W17 policy-bound privacy sensing
→ W22 privacy-preserving telemetry
→ W24 dual-use execution context
→ W28 training-state capability isolation
→ W31 run evidence expands to typed claim provenance
→ W32 causal repair and reusable skills acquire provenance and review gates
→ W33 richer proposal channels retain explicit verifier and commit authority
```

演进重点不是“更强模型需要更多安全功能”，而是 evidence object 从 output 扩展到 internal
state、trajectory、tool action、artifact、identity 与 aggregate telemetry；每次扩展也增加
privacy、false-positive、measurement drift 和 governance 成本。

### Compute, Memory and Scheduling

```text
W06 conditional attention
→ W11 workload-specific accelerator
→ W13 compression with executable-kernel boundary
→ W20 multi-objective scheduling
→ W26 MTP tied to mobile hardware/runtime
→ W27 asynchronous training and conditional service locality
→ W28 adaptive speculation and pluggable communication
→ W29 router objective shapes executable dispatch
→ W30 state-aware selection and heterogeneous cache identity
→ W31 semantic state composition adds writer/reader compatibility
→ W32 finer execution cuts require full-fleet provisioning and failure accounting
→ W33 communication, cache and elasticity units follow downstream sufficient information and state liveness
```

关系以 `Principle Reuse` 和 `Layering` 为主：减少理论计算、压缩存储、定制硬件与改变
scheduler objective 并非互相替代。每项收益都必须绑定模型、hardware、precision、
workload、并发与 SLO。

## Historical Decision Chronicle（Provisional, Non-additive）

下表保留旧 93-row baseline 的原始决策与后续逐周修复检查点，因此是演进沿革，不是同一时点的
可加总 census：W01～W09 行仍展示早期 baseline，而 W10～W30 行已经嵌入恢复后的 current checkpoint。
当前可加总数字只以 `Current Provisional Recovered Ledger` 为准；非模板化阅读证据、实验边界和拒绝
理由保留在对应 Weekly 的 `Full Source Review`。缩写：`R` = `Refine — Existing Argument`，`N` =
`No Change — Already Covered`，`W` = `Weekly Only`，`E` = `Emerging / Experimental`，
`D` = `Disputed`。W27 的 Seed2.0 两个评分行明确指向同一 source family，不计作两个事件。

| Week | Scored Rows | Final Disposition |
| --- | ---: | --- |
| W01 | 0 | No scored candidate |
| W02 | 1 | NVIDIA open models/data/tools — W / mechanism not disclosed |
| W03 | 3 | Economic primitives — N；MedGemma 1.5/MedASR — W；NeuralGCM precipitation — W / low-score |
| W04 | 3 | Assistant axis — N；Claude Constitution — W / official specification；GIST smart sampling — N |
| W05 | 43 | 43/43 Full Source Reviews；28 Integrate/Refine；11 No Change；3 Weekly Only；1 Reject；Source-Family Books Gate Complete；Archive Gate Open |
| W06 | 41 | 41/41 final dispositions；21 Integrate/Refine；15 No Change；4 Weekly Only；1 Unverified；15 owner chapters；Source-Family Books Gate Complete；Archive Gate Open |
| W07 | 52 | 52/52 final dispositions；39 Integrate/Refine；7 No Change；3 Emerging/Experimental；2 Weekly Only；1 Unverified/Blocked；16 Stable Node owners；Source-Family Books Gate Complete；Archive Gate Open |
| W08 | 23 | 23/23 final dispositions；18 Integrate/Refine；4 No Change；1 Weekly Only；12 Stable Node owners；Source-Family Books Gate Complete；Archive Gate Open |
| W09 | 2 | Persona selection — N；Malicious-use disruption report — N |
| W10 | 36 | 36/36 Full Source Reviews or trusted low-score checks；0 pending；27 Refine / 4 No Change / 5 Weekly Only or Disputed；15 Stable Node owners；Source-Family Books Gate Complete；Archive Completion Gate Open |
| W11 | 55 scored + 1 unscored blocked identity + 3 unscored blocked full text + 1 cross-year reroute | 52/53 `20+` Full Source Reviews；2/2 low-score checks；31 Integrate/Refine / 20 No Change / 1 Emerging / 2 Weekly Only / 1 scored blocked；17 Stable Node owners；4 unscored blockers；FineRMoE — 2025 backlog；0 ordinary Books pending；Source-Family Books Gate Complete；broader Historical Archive Gate Open |
| W12 | 49 | 48/48 `20+` Full Source Reviews；1/1 low-score check；34 Integrate/Refine / 11 No Change / 3 Weekly Only / 1 Emerging；17 Stable Node owners；0 Books pending；Source-Family Books Gate Complete；broader Historical Archive Gate Open |
| W13 | 45 scored + 1 unscored blocked source | 45/45 final dispositions；41/41 scored `20+` Full Source Reviews；10 Integrate / 23 Refine / 6 No Change / 2 Disputed；4 low-score or cross-week Weekly Only；18 Stable Node owners changed or revalidated；ClawKeeper `Unverified / Blocked / No Books Change`；0 Books pending；Source-Family Books Gate Complete；Archive Completion Gate Open |
| W14 | 27 scored + 2 unscored blocked identities | 27/27 final dispositions；26/26 scored `20+` Full Source Reviews；5 Integrate / 18 Refine / 3 No Change；1 low-score Weekly Only；15 Stable Node owners changed；Backdoor Attacks、Cactus `Unverified / Blocked / No Books Change`；0 Books pending；Source-Family Books Gate Complete；Archive Completion Gate Open |
| W15 | 31 scored; 1 scored source blocked | 31/31 final dispositions；25/25 accessible scored `20+` Full Source Reviews；21 Refine / 3 No Change / 1 Emerging；GameWorld `Unverified / Blocked / No Books Change`；5 low-score/pre-release Weekly Only；13 Stable Node owners changed；0 Books pending；Source-Family Books Gate Complete；Archive Completion Gate Open |
| W16 | 42 | 42/42 final dispositions；23 Refine / 14 No Change / 3 Weekly Only / 1 Emerging / 1 Disputed；12 Stable Node owners changed or revalidated；0 Books pending；Source-Family Books Gate Complete；Archive Completion Gate Open |
| W17 | 22 | 22/22 final dispositions；13 Refine / 4 No Change / 4 Weekly Only / 1 Emerging；8 Stable Node owners changed；0 Books pending；Source-Family Books Gate Complete；Archive Completion Gate Open |
| W18 | 86 scored + 1 unscored blocked family | 86/86 final dispositions；56 Refine / 21 No Change / 7 Weekly Only / 2 Disputed；80/80 scored `20+` Full Source Reviews；Safety Drift `Unverified / Blocked / No Books Change`；Source-Family Books Gate Complete；Historical Archive/Discovery Gate Open |
| W19 | 35 | 35/35 final dispositions；25 Refine / 6 No Change / 3 Weekly Only / 1 Unverified-Blocked；33/34 `20+` Full Source Reviews；19 Stable Node owners changed or revalidated；StraTA 无 Books Change；Source-Family Books Gate Complete；Historical Archive/Discovery Gate Open |
| W20 | 31 | 31/31 final dispositions；25 Refine / 4 No Change / 2 Weekly Only；30/30 `20+` Full Source Reviews；15 Stable Node owners changed or revalidated；0 blocked / pending；Source-Family Books Gate Complete；Historical Archive/Discovery Gate Open |
| W21 | 31 | 31/31 final dispositions；22 Refine / 6 No Change / 3 Weekly Only；30/30 `20+` Full Source Reviews；17 Stable Node owners changed or revalidated；0 blocked / pending；Source-Family Books Gate Complete；Historical Archive/Discovery Gate Open |
| W22 | 43 scored; fixed official/Infra checkpoint passed | 30 high / 12 mid / 1 low；42/42 `20+` Full Source Reviews；27 former blockers recovered 2026-08-13；0 blocked / pending；Historical Evidence Gate Open only for cross-index replay；Books Gate Closed |
| W23 | 33 scored; fixed official/Infra checkpoint passed | 21 high / 12 mid；22/33 current-version Full Source Reviews；11 blocked families；StreamMA v1/artifact remains a revision sub-gap；0 ordinary pending；其他 disposition 见周报；Historical Evidence Gate Open；Books Gate Closed |
| W24 | 38 scored; fixed official/Infra checkpoint passed | 26 high / 11 mid / 1 low；36/37 `20+` Full Source Reviews；VIA-SD recovered；Agentic Environment Engineering survey remains blocked；0 pending；Historical Evidence Gate Open；Books Gate Closed |
| W25 | 35 scored; fixed official/Infra checkpoint passed; post-forward cursor advances to W26 | 24 high / 10 mid / 1 low；32/34 `20+` Full Source Reviews；LLM-Designed Training Environment、MemGUI-Agent — Unverified / Blocked Backlog；0 ordinary pending；25 recovered families have non-template reviews and provisional dispositions；JetSpec label corrected to JetFlow；Project Fetch — 18-point boundary review；TokenPilot — provisional R / Ch71；ZPPO — provisional I / Ch29 Experimental；GateMem — provisional I / Ch68 Experimental；vLLM v0.23.0 — provisional R / Ch46 Version-sensitive；NVIDIA MoE fusion — provisional R / Ch21 Bounded Case；MLPerf Training v6.0 — provisional R / Ch62 Benchmark Contract；Near-autonomous chemist — N / Ch77；LifeSciBench — N / Ch62；coding expertise — N；W25 discovery/Historical Evidence Gate Open；Books Gate Closed |
| W26 | 40 scored; fixed official/Infra checkpoint passed; post-forward cursor advances to W27 | 25 high / 14 mid / 1 low；37/39 `20+` Full Source Reviews；AOHP、Self-Compacting Agents — Unverified / Blocked Backlog；0 ordinary pending；31 recovered papers have non-template reviews and provisional dispositions；Qwen-AgentWorld — provisional R / Ch10；Wan-Streamer、Multi-Block DLM — provisional I / Ch38 Experimental；Verification Horizon、OSWorld 2.0 — provisional R / Ch62；EDV — provisional R / Ch73；InfoKV — provisional R / Ch22；Agentic Abstention、DiscoBench — provisional R / Ch75；GBC — provisional R / Ch78；Agent-Native Memory — provisional R / Ch73；DFlash integration — N / Ch44 Engineering Node；TensorRT 11 multi-device — provisional R / Ch45 Version-sensitive；W26 discovery/Historical Evidence Gate Open；Books Gate Closed |
| W27 | 34 score rows / 33 unique families; fixed official/Infra and Forward Candidate checkpoints passed | 24 high / 10 mid；33/33 unique `20+` Full Source Reviews；AgenticSTS recovered 2026-08-13；0 blocked / pending；Seed2.0 duplicate relation closed；其他 disposition 见周报；broader discovery/Historical Evidence Gate Open；Books Gate Closed |
| W28 | 30 scored families; fixed official/Infra and Forward Candidate checkpoints passed; cursor remains W29 | 19 high / 10 mid / 1 low；27/30 Full Source Reviews；0 ordinary pending；AgentLens、UP、Ideas Have Genomes — Unverified / Blocked Backlog；J-space/Jacobian Lens — N / Ch5；GRAM — R / Ch68 Experimental；DSpark — N / Ch44/52；Length Penalty — E；PyTorch 2.13 — R / Ch32；KVpop — R / Ch41；Linear Attention、SDM — R / Ch22；SAO、Direct OPD — R / Ch29；RynnWorld/AlayaWorld — R / Ch10；proactive memory、LaMem-VLA、ReflectWorld-MM — R / Ch73；STRACE — R / Ch65；ABot-AgentOS — R / Ch80；DeepSearch-World — R / Ch77；GRASP、forecast probe、PolicyShiftGuard、Infinite Worlds、UniClawBench — N；W28 broader discovery/Historical Evidence Gate Open；Books Gate Closed |
| W29 | 38 scored families; fixed official/Infra and Forward Candidate checkpoints passed; cursor advances to W30 | 21 high / 17 mid；34/38 Full Source Reviews；0 ordinary pending；Multi-Agent Exploration、AI Scientist Capability、Generative Compilation、LongStraw — Unverified / Blocked Backlog；OPD signal transfer/regulation、ShortOPD、SEED、Distilled RL — provisional R / Ch29 Experimental；Function-FIM — R / Ch24；Oat failure attribution — R / Ch65；PalmClaw — R / Ch80；BadWAM — R / Ch68；Pixels-to-States — R / Ch10；JoyNexus — R / Ch56；DataFlow-Harness — R / Ch77；DCP — R / Ch32；LightMem、AdvancedMath、KnowAct、Harness Evaluation — N；KV graft — Emerging / Disputed；其他既有 disposition 见周报；W29 broader discovery/Historical Evidence Gate Open；Books Gate Closed |
| W30 | 25 scored; fixed official/Infra and Forward Candidate checkpoints passed; forward sweep reached W30 boundary | 11 high / 13 mid / 1 low；25/25 Full Source Reviews；0 blocked；0 ordinary pending；pre-window identities reconciled to W27/W28/W29；SWE-Pruner Pro — R / Ch71；LLM Coach、SAT — R / Ch29；FlashRT、AREX — R / Ch77；Self-State — R / Ch68；AgentDebugX — R / Ch65；AutoIndex、setwise retrieval — R / Ch72；SLAI T-Rex — R / Ch32；RECAP — R / Ch5；ICAE/Evolving Intent — R / Ch62；Experience Distillation — R / Ch73；SkewAdam — Emerging / Disputed；DocOps、OpenForgeRL、Dynamo — N；SGLang — R / Ch47；其余 disposition 见周报；W30 broader discovery/Historical Evidence Gate Open；Books Gate Closed |

Legacy baseline checkpoint（不可与上表后续恢复行相加）：`93/93` final dispositions；`20/20` 高分和
`60/60` 中分完成当时范围内的 Source Review；`13/13` 低分完成来源、日期、评分与拒绝/升级核验；
`80` retained rows 对应 `79` unique events。它只证明旧 admission set 的处置完整，不证明当前 discovery
recall 或 all-history Evidence Gate 完整。

## W01～W32 Remaining Primary-Source Material Ledger — 2026-08-13

本表是逐周 blocked、revision 与 identity ledger 按 `Source Family ID + primary identifier + first-public
date` 去重后的唯一材料请求。`Review Pending = 0`：能读取的候选已完成当前版本审计；以下 41 项仍需要
材料或唯一身份，其中 36 项为 source family、1 项为 StreamMA revision/artifact sub-gap、3 项为 W32
identity gaps、1 项为跨全年的 discovery export。`Books Pending` 不计入 Weekly 缺失。按 ADR-007，Archive Completion Gate 继续 Open；已完成全文、证据边界与 owner 审计的 family 可独立通过 Source-Family Books Gate。下方带日期的旧 `Historical Books Gate Closed` 行只记录当时状态，不应覆盖当前 Gate 语义。

| Priority | Week | Candidate / Source Family | Known ID / URL | Missing Material | Why Insufficient / Acceptable Substitute | Suggested Filename | Audit after Recovery |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P1 Full Text | W06 | Claude Opus 4.6 source family | Anthropic announcement + linked system card | 可解析的完整 system card | announcement 只能证明版本/API；接受官方 PDF、HTML 或逐页文本导出 | `W06-claude-opus-4.6-system-card.pdf` | capability/safety methodology、eval contract、limitations |
| P1 Full Text | W07 | InternAgent-1.5 | arXiv:2602.08990 | 事件时完整 technical report | 现有官方 release/code 只能形成 partial packet；接受 v1 PDF/HTML/TXT | `W07-internagent-1.5-v1.pdf` | generation/verification/evolution、memory、lab approval、完整实验/Appendix |
| P1 Full Text | W11 | Groundsource | EarthArXiv repository 12083 | EarthArXiv preprint 全文 | 官方 Blog/dataset 不能核验 sampling、dedup、annotation 与 bias；接受 PDF/TXT | `W11-groundsource-eartharxiv.pdf` | data construction、label lineage、precision/recall、limitations |
| P0 Identity | W11 | Safe Web Agent Learning | intake label only | 准确标题、作者及 arXiv/DOI/official URL | 无唯一 identity，不能用相似论文替代；接受检索导出或作者页 | `W11-safe-web-agent-identity.md` | 从 metadata、日期、评分到完整 Source Review 重建 |
| P1 Full Text | W11 | HomeSafe-Bench | arXiv:2603.11975 | v1/v2 正文及 Appendix | project page 可读但 36 MB PDF 无法解析；接受 PDF、HTML、TXT | `W11-homesafe-bench-v1.pdf` | annotation、HD-Guard control flow、latency、ablation、limitations |
| P1 Full Text | W11 | Think While Watching | arXiv:2603.11896 | v1 正文及 Appendix | repository 仅支持 inference boundary；接受 16 MB PDF/TXT | `W11-think-while-watching-v1.pdf` | training data、causal mask、backend selector、hardware/latency |
| P1 Full Text | W11 | TERMINATOR | arXiv:2603.12529 | event-time paper + Appendix | project/model artifacts 不能替代 Method/ablation；接受 v1 PDF/TXT | `W11-terminator-v1.pdf` | exit-label construction、calibration、quality/latency、failure cases |
| P0 Identity | W13 | ClawKeeper | alleged arXiv:2603.24414 | 正确 title/authors/identifier 或官方撤回记录 | ID 无法返回 metadata；接受 arXiv export、author page、PDF | `W13-clawkeeper-identity.md` | 先验证身份/日期，再决定评分、owner 与全文范围 |
| P0 Identity | W14 | Backdoor Attacks on Decentralised Post-Training | name/date only, 2026-03-31 | title、authors、arXiv/DOI/URL | attribution-only，不能由标题推断机制 | `W14-backdoor-decentralised-post-training-identity.md` | identity、threat model、method/eval、score/owner |
| P0 Identity | W14 | Cactus | name/date only, 2026-04-05 | title、authors、arXiv/DOI/URL | 名称高度歧义；接受 discovery export/作者页 | `W14-cactus-identity.md` | identity、first-public date、全文、score/owner |
| P1 Full Text | W15 | GameWorld | arXiv:2604.07429 | 23 页 v1 paper | project/repository 只证明 artifact surface；接受 PDF/TXT | `W15-gameworld-v1.pdf` | state verifier、dataset/eval、limitations、Ch62 disposition |
| P1 Full Text | W18 | Safety Drift After Fine-Tuning | arXiv:2604.24902 | v1 paper + author artifact | 目前只有 identity/date；接受 PDF/HTML/TXT、官方 project | `W18-safety-drift-v1.pdf` | mechanism、eval/ablation、failure boundary、score/owner |
| P1 Full Text | W19 | StraTA | arXiv:2605.06642 | v1 paper + author artifact | 现有 metadata 不足以区分 latent/explicit abstraction；接受 PDF/HTML/TXT | `W19-strata-v1.pdf` | trajectory abstraction、credit/state ownership、overhead |
| P3 Revision | W23 | StreamMA v1 / runnable artifact | arXiv:2606.05158v1; EnVision-Research/StreamMA | v1 snapshot + `StreamMA.py` 对应 commit/release | current v2 与 README-only repo 不能倒写 W23；接受 v1 PDF、tag/zip | `W23-streamma-v1-and-artifact.zip` | v1-v2 diff、runtime dataflow、artifact reproducibility |
| P1 Full Text | W23 | Agents' Last Exam | arXiv:2606.05405 | paper + immutable benchmark/code snapshot | 需核验 living revision、grader 与 cost；接受 PDF + repo tag/zip | `W23-agents-last-exam-v1.zip` | provenance、harness identity、grader、cost/limitations |
| P1 Full Text | W23 | SWE-Explore | arXiv:2606.07297 | v1 paper + artifact | abstract 不足以核验 exploration causality | `W23-swe-explore-v1.pdf` | trace、information gain、tools、leakage、ablation |
| P1 Full Text | W23 | Unembedding Matrix Feature Lens | arXiv:2606.07502 | v1 paper + code if public | 需区分 probe 与 intervention | `W23-unembedding-feature-lens-v1.pdf` | geometry、causal boundary、cross-model generality |
| P1 Full Text | W23 | Geometry of On-Policy Distillation | arXiv:2606.07082 | v1 paper | metadata 不能证明 divergence/support claims | `W23-opd-geometry-v1.pdf` | derivation、estimator、stability、revision |
| P1 Full Text | W23 | Retrospective Harness Optimization | arXiv:2606.05922 | v1 paper + artifact | 需核验 offline/self-preference bias 与 rollback | `W23-retrospective-harness-optimization-v1.pdf` | harness state、evaluation、transfer、failure modes |
| P1 Full Text | W23 | LatentSkill | arXiv:2606.06087 | v1 paper + adapter artifact | 标题不足以证明 text-to-weight compilation | `W23-latentskill-v1.zip` | base/adapter identity、forgetting、held-out transfer |
| P1 Full Text | W23 | OpenSkill | arXiv:2606.06741 | v1 paper + artifact | 需核验 open-world discovery 与 lifecycle | `W23-openskill-v1.zip` | validation、conflict、supersession、stability |
| P1 Full Text | W23 | When Tools Fail | arXiv:2606.05806 | v1 paper + environment artifact | 需核验 fault injection 与 environment realism | `W23-when-tools-fail-v1.zip` | observation/action contract、replanning、grader |
| P1 Full Text | W23 | Graph Memory for LLM Agents | arXiv:2606.06036 | v1 paper + code/data | 需核验 derived graph ownership 与 provenance | `W23-graph-memory-v1.zip` | reconstruction、retrieval、consolidation、failure |
| P1 Full Text | W23 | Program-of-Layers | arXiv:2606.06574 | v1 paper + implementation | 需核验 routing state、control 与 runtime cost | `W23-program-of-layers-v1.zip` | composition、objective、latency/overhead、limitations |
| P1 Full Text | W23 | SkillHarness | arXiv:2606.20636 | event-time paper + benchmark revision | ID/date relationship itself needs confirmation | `W23-skillharness-event-snapshot.zip` | provenance、安全执行、benchmark/revision history |
| P1 Full Text | W24 | Agentic Environment Engineering survey | arXiv:2606.12191 | complete paper / appendices | 搜索镜像只证明存在，不能作为全文证据；接受 official PDF/TXT | `W24-agentic-environment-engineering.pdf` | taxonomy sources、environment ownership、synthesis/eval gaps |
| P1 Full Text | W25 | LLM-Designed Training Environment | arXiv:2606.17682 | v1 paper + environment artifact | abstract 不足以核验 environment-policy coupling | `W25-llm-designed-training-environment.zip` | revisions、failure evidence、testbed validity |
| P1 Full Text | W25 | MemGUI-Agent | arXiv:2606.19926 | v1 paper + artifact | 需核验 proactive context 与 GUI state | `W25-memgui-agent-v1.zip` | state ownership、memory lifecycle、long-horizon eval |
| P1 Full Text | W26 | AOHP | arXiv:2606.23449 | v1 paper + OS artifact | metadata 不足以核验 object/permission model | `W26-aohp-v1.zip` | OS objects、permissions、personal state、failure recovery |
| P1 Full Text | W26 | Self-Compacting Language Model Agents | arXiv:2606.23525v1 | v1 paper + code | 需核验 model-triggered compaction fidelity | `W26-self-compacting-agents-v1.zip` | trigger/state、rubric、recovery、limitations |
| P1 Full Text | W28 | AgentLens | arXiv:2607.06624 | v1 paper + artifact | 需核验 trajectory labels 与 verifier coupling | `W28-agentlens-v1.zip` | review schema、formal verifier、regression contract |
| P1 Full Text | W28 | UP asymmetric optimization | arXiv:2607.06987 | v1 paper + code | 需核验 objective derivation 与 stability | `W28-up-v1.zip` | asymmetry、exploration、ablation、failure modes |
| P1 Full Text | W28 | Ideas Have Genomes | arXiv:2607.08758 | v1 paper + dataset/artifact | 需核验 lineage ground truth 与 novelty leakage | `W28-ideas-have-genomes-v1.zip` | lineage、workflow evidence、benchmark validity |
| P1 Full Text | W29 | Multi-Agent LLMs Fail to Explore Each Other | arXiv:2607.11250 | v1 paper + artifact | 需核验 communication topology 与 causal failure | `W29-multi-agent-exploration-failure-v1.zip` | regret、polarization、topology/ablation |
| P1 Full Text | W29 | Capability-Oriented Benchmark for AI Scientists | arXiv:2607.11079 | v1 paper + benchmark | 需核验 claim/assumption/code grading | `W29-ai-scientist-capability-bench-v1.zip` | task construction、grader、leakage、limitations |
| P1 Full Text | W29 | Generative Compilation | arXiv:2607.13921 | v1 paper + code | 需核验 compiler feedback control flow | `W29-generative-compilation-v1.zip` | state、latency、correctness、fallback |
| P1 Full Text | W29 | LongStraw | arXiv:2607.14952 | v1 paper + training artifact | 需核验 2M-token RL system contract | `W29-longstraw-v1.zip` | parallelism、memory budget、quality/eval、SLO |
| P0 Identity | W32 | PrefixPlace | alias only | exact title/authors/arXiv/DOI/official URL | 名称未唯一解析，现有 24 分为 discovery priority 而非 evidence | `W32-prefixplace-identity.md` | identity/date 后从零评分与全文审计 |
| P0 Identity | W32 | xPress | alias only | exact title/authors/arXiv/DOI/official URL | 名称高度歧义，不能沿用推测机制 | `W32-xpress-identity.md` | identity/date 后从零评分与全文审计 |
| P0 Identity | W32 | Resource-Fair Scheduling | descriptive label only | exact title/authors/arXiv/DOI/official URL | 描述性标签不能唯一归属 source family | `W32-resource-fair-scheduling-identity.md` | identity/date 后从零评分与全文审计 |
| P4 Discovery Export | W01～W32 | Google Scholar / OpenAlex recall closure | 2026-01-01～2026-08-09 date-window queries | 带 query、result title、authors、date、DOI/arXiv/URL 的 CSV/JSON export | 当前环境无法稳定访问可复算的历史查询结果；接受 Scholar `Publish or Perish` 导出或 OpenAlex API/网页导出，重复结果可保留 | `2026-W01-W32-scholar-openalex-export.csv` | 按 ISO week 分流、与 1143 rows 去重、补遗漏候选并重开受影响 Weekly Gate |

### Recovery Results and Material Boundaries

- 本轮已成功恢复并完成非模板化 Source Review：MolmoAct2、OpenSearch-VL、Skill1、Qwen-Image-2.0、
  SkillsVote、LongLive-2.0、WorldKV、QUEST、W22 的 27 个 paper families、Continual Experience
  Internalization、VIA-SD、AgenticSTS、ViPO、ElastiCo、OasisKV、TAOT 与 KServe v0.20.0。
- HomeSafe-Bench、Think While Watching、TERMINATOR 与 InternAgent-1.5 的官方 PDF 可定位，但当前
  text-reader 分别因 36 MB、16 MB、15 MB 与 23 MB 左右的文档体积拒绝解析；这属于 `P1 Full Text`，不是
  identity gap。它们可以直接由用户提供原 PDF 或文本导出。
- Claude Opus 4.6 只保留版本/API事实；如果 system card 仍无法取得，最终 disposition 应保持
  `Version Fact / Mechanism Not Disclosed`，而不是反推 architecture 或 training。
- Google Scholar / OpenAlex 的历史结果在当前环境仍无法形成可复算导出，因此年度 discovery recall 尚未
  闭合。只需提供一个包含查询与结果 metadata 的合并导出，不需要逐周提供 32 份文件。
- `Disputed` 不等于缺材料：例如 W18 Tuna-2、W29 KV-graft 与 W30 SkewAdam 已有可读来源但证据/条件冲突，
  继续保留争议状态，不列入上表的下载请求。

## 7-Part / 84-Chapter Legacy Mapping — 2026-08-13

2026-08-13 起，Books 使用 Stable Knowledge Node ID。历史 W01～W32 的旧章节号保留当时语义，按下表解释；不得把旧 Ch23 误读为当前 Ch23：

| Historical reference | Current reference | Stable owner range |
| --- | --- | --- |
| Legacy Ch1～22 | Current Ch1～22 | `WORLDVIEW-*` / `MODEL-*` |
| No legacy chapter | Current Ch23～26 | `MULTIMODAL-*` |
| Legacy Ch23～37 | Current Ch27～41 | `TRAIN-*` |
| Legacy Ch38～52 | Current Ch42～56 | `INFER-*` |
| Legacy Ch53～69 | Current Ch57～73 | `PLATFORM-*` |
| Legacy Ch70～80 | Current Ch74～84 | `AGENT-*` |

以后新增/更新的 Integration 记录统一写 `Owner + Current chapter + Legacy chapter`。完整 84 节点表位于 `ROADMAP.md`。

## Source-Family Books Integration Checkpoint — 2026-08-13

Source-Family Books Gate 与 Archive Completion Gate 已按 ADR-007 分离。已通过周级 Gate 的 family
可以进入唯一 Stable Node owner；新多模态主线另由 Part III 承载。41 项材料缺口、存在争议的性能
claim 和 `Version Fact / Mechanism Not Disclosed` 仍冻结，因此 **W01～W32 Archive Completion Gate
仍为 Open**。

### W01 weekly-gated Books Review

W01 已按“逐候选 Integration → 周级反向检查 → 状态同步”完成独立 Gate：11/11 retained families
拥有最终 disposition，10 项写入或 refine 8 个 owner chapters，DiT-HC 以章节级去重证据判定 `No Change`。
OrchestrRL 的主 owner 在周级 Review 中从 legacy Ch32 修正为 `TRAIN-GRPO` / current Ch33 / legacy Ch29；
Distributed Training 只保留 topology/communication handoff。W01 的 discovery coverage 仍有限，因此
Source-Family Books Gate Complete 不等于 W01 Archive Completion Gate Closed；后续新增候选会重新打开
本周 Books Review。

| W01 Source Family | Stable owner | Current / Legacy | Final disposition |
| --- | --- | --- | --- |
| RIMRULE | `AGENT-MEMORY` | Ch77 / Ch73 | Refine — failure-derived procedural rule |
| Beyond Perfect APIs | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | Refine — isolated/cumulative API complexity |
| Revati | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | Integrate — simulator fidelity ladder |
| FlexSpec | `INFER-SPECULATIVE-DECODING` | Ch48 / Ch44 | Refine — Experimental edge/cloud control |
| FwPKM | `MODEL-LONG-CONTEXT` | Ch22 / Ch22 | Integrate — Experimental mutable fast weights |
| OrchestrRL | `TRAIN-GRPO` | Ch33 / Ch29 | Integrate — RFabric Experimental |
| Does Memory Need Graphs? | `AGENT-MEMORY` | Ch77 / Ch73 | Refine — controlled component attribution |
| FLOP-Efficient Training | `TRAIN-PRETRAINING` | Ch28 / Ch24 | Integrate — Experimental lifecycle objective |
| Tarragon | `INFER-PD-DISAGGREGATION` | Ch55 / Ch51 | Integrate — Experimental role-specific recovery |
| HardGen | `TRAIN-DATA` | Ch27 / Ch23 | Refine — Experimental failure-driven curriculum |
| DiT-HC | `TRAIN-DISTRIBUTED-TRAINING` | Ch36 / Ch32 | No Change — existing mechanism coverage |

### W02 weekly-gated Books Review

W02 已完成 5/5 retained families 的逐项 disposition 与周级反向检查：四篇全文可访问论文分别进入
MoE、KV lifecycle、execution plan 与 scheduling 的现有演进链；NVIDIA portfolio 因只证明资产组合
发布而保持 Weekly Only。Review 修正了两个 provisional owner：MoEBlaze 由训练并行改归 execution-plan
owner，AIConfigurator 由旧编号歧义改归 inference scheduling。W02 Discovery Recall 仍为 Open；后续
恢复的新候选会重新打开本周 Books Review。

| W02 Source Family | Stable owner | Current / Legacy | Final disposition |
| --- | --- | --- | --- |
| NVIDIA open asset portfolio | `PLATFORM-FOUNDATIONS` | Ch57 / Ch53 | Weekly Only — mechanism not disclosed |
| Routing by Analogy / kNN-MoE | `MODEL-MOE` | Ch21 / Ch21 | Refine — retrieval correction and fallback |
| Crystal-KV | `INFER-KV-CACHE` | Ch45 / Ch41 | Refine — Experimental workload-aware eviction |
| MoEBlaze | `INFER-TENSORRT-LLM` | Ch49 / Ch45 | Integrate — indexed conditional execution |
| AIConfigurator | `INFER-SCHEDULING` | Ch56 / Ch52 | Integrate — calibrated configuration search |

### W03 weekly-gated Books Review

W03 已完成 7/7 scored candidates 的最终 disposition 与独立反向检查。四项长期机制进入 Ch21、Ch45、
Ch51、Ch55；Economic Index 以 Ch66/67 的具体 evidence contract 去重，MedGemma 与 NeuralGCM 留在
Weekly。复核 primary source 时发现 RAPID 原记录的 `arXiv:2601.12727` 属于无关论文，已纠正为
`arXiv:2601.12241` 后重新核验全文。W03 Discovery Recall 仍为 Open，不能据此宣称档案完整。

| W03 Source Family | Stable owner | Current / Legacy | Final disposition |
| --- | --- | --- | --- |
| Anthropic Economic primitives | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | No Change — existing evidence identity |
| MedGemma 1.5 / MedASR | `PLATFORM-MODEL-REGISTRY` | Ch59 / Ch55 | Weekly Only — version/domain fact |
| NeuralGCM precipitation | `WORLDVIEW-REPRESENTATION` | Ch5 / Ch5 | Weekly Only — low-score domain evidence |
| KVzap | `INFER-KV-CACHE` | Ch45 / Ch41 | Refine — learned eviction; no engine speed claim |
| Principled MoE Design | `MODEL-MOE` | Ch21 / Ch21 | Refine — architecture under joint constraints |
| TableCache | `INFER-SGLANG` | Ch51 / Ch47 | Integrate — dependency-aware reusable blocks |
| RAPID | `INFER-PD-DISAGGREGATION` | Ch55 / Ch51 | Integrate — Experimental power/role control |

### W04 weekly-gated Books Review

W04 已完成 23/23 scored candidates 的逐项 disposition 与周级反向检查：16 项长期机制进入或 refine
13 个 owner chapters，4 项以现有章节具体机制去重，2 项仅保留 Weekly，1 项因 2025 first-public 且
仅有 CPU MPI evidence 被拒绝。Review 将所有 legacy 章节号迁移为 Stable Knowledge Node owner，并检查
了训练异步、checkpoint、MoE spill、KV tiering、deterministic verification、barrier routing、security、
context、workflow 与 shared-repository commitment 之间的层次关系。Faramesh 和 Universal Load Balancing
保持 `Emerging`；W04 Discovery Recall 仍为 Open，不把当前 source-family Gate 误写为档案完整。

| W04 Source Family | Stable owner | Current / Legacy | Final disposition |
| --- | --- | --- | --- |
| Anthropic assistant axis | `WORLDVIEW-REPRESENTATION` | Ch5 / Ch5 | No Change — evidence ladder covered |
| Claude constitution | `WORLDVIEW-SYSTEM-EVOLUTION` | Ch9 / Ch9 | Weekly Only — official specification |
| Google GIST | `TRAIN-DATA` | Ch27 / Ch23 | No Change — data selection covered |
| StaleFlow | `TRAIN-GRPO` | Ch33 / Ch29 | Integrate — trajectory staleness invariant |
| Sutradhara | `AGENT-WORKFLOW` | Ch81 / Ch77 | Integrate — orchestrator–engine contract |
| HeteroCache | `INFER-KV-CACHE` | Ch45 / Ch41 | Integrate — recoverable tiering |
| DataStates-LLM | `TRAIN-CHECKPOINT` | Ch35 / Ch31 | Integrate — composable state providers |
| Scaling All-to-all | `TRAIN-DISTRIBUTED-TRAINING` | Ch36 / Ch32 | Reject — 2025 first-public and CPU-only |
| Kareus | `TRAIN-MEGATRON` | Ch40 / Ch36 | Integrate — time–energy frontier |
| Faramesh | `PLATFORM-SECURITY` | Ch72 / Ch68 | Integrate — Emerging action authorization |
| LLM-42 | `INFER-CONTINUOUS-BATCHING` | Ch46 / Ch42 | Integrate — selective deterministic verify |
| Universal Load Balancing | `INFER-SCHEDULING` | Ch56 / Ch52 | Integrate — Emerging barrier load control |
| CooperBench | `AGENT-MULTI-AGENT` | Ch82 / Ch78 | Integrate — shared-state commitment |
| Jet-RL | `TRAIN-GRPO` | Ch33 / Ch29 | Refine — precision-flow identity |
| LongCat-Flash-Thinking | `TRAIN-GRPO` | Ch33 / Ch29 | Refine — domain-mixture contract |
| SWE-Pruner | `AGENT-CONTEXT` | Ch75 / Ch71 | Integrate — structured pruning |
| Endless Terminals | `TRAIN-DATA` | Ch27 / Ch23 | No Change — executable data pipeline covered |
| Least-Loaded Expert Parallelism | `TRAIN-DISTRIBUTED-TRAINING` | Ch36 / Ch32 | Integrate — dynamic token/weight spill |
| Agentic Search in the Wild | `PLATFORM-MONITORING` | Ch67 / Ch63 | Integrate — session trajectory sensor |
| Fast KVzip | `INFER-KV-CACHE` | Ch45 / Ch41 | No Change — learned eviction covered |
| RM-RF | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | Weekly Only — experimental proxy |
| Fission-GRPO | `TRAIN-GRPO` | Ch33 / Ch29 | Refine — failure-derived corrective branch |
| KD Memorization | `TRAIN-SFT` | Ch29 / Ch25 | Integrate — memorization inheritance boundary |

### W05 weekly-gated Books Review

W05 已完成 43/43 scored candidates 的逐项 disposition、目标及相邻章节阅读和周级反向检查。28 项长期机制
进入或 refine 17 个 owner chapters；11 项以现有具体机制去重；AI assistance/coding skills、TTCS、Routing
the Lottery 仅保留 Weekly；energy-performance scheduler 因 simulation-only evidence 拒绝。Post-LN 与
Multi-Agent scaling 没有重复写入，分别由 Ch17 的 controlled coexistence 与 Ch82 的 task-topology/capability
boundary 承担。W05 Discovery Recall 仍为 Open；恢复新 source family 时必须重开本周 Books Review。

| W05 Source Family | Stable owner | Current / Legacy | Final disposition |
| --- | --- | --- | --- |
| ODC | `TRAIN-DISTRIBUTED-TRAINING` | Ch36 / Ch32 | Integrate — minibatch commit boundary |
| FP8-RL | `TRAIN-GRPO` | Ch33 / Ch29 | Refine — precision-flow identity |
| Scaling Embeddings | `MODEL-EMBEDDING` | Ch12 / Ch12 | Integrate — hashed n-gram capacity |
| ConceptMoE | `MODEL-MOE` | Ch21 / Ch21 | Integrate — compress before conditional routing |
| HALO / HypeNet | `MODEL-LONG-CONTEXT` | Ch22 / Ch22 | Integrate — hybrid-state checkpoint migration |
| ReGuLaR | `MODEL-DECODER-ONLY` | Ch18 / Ch18 | Integrate — Experimental latent reasoning branch |
| Golden Goose / SAGE | `TRAIN-DATA` | Ch27 / Ch23 | Refine / No Change — policy-relative curriculum |
| daVinci-Dev / SERA / ASTRA | `TRAIN-DATA` | Ch27 / Ch23 | Refine — repository/executable trajectory lineage |
| ECO / Quartet II / Learning What to Predict | `TRAIN-PRETRAINING` | Ch28 / Ch24 | Integrate/Refine — low-bit graph and adaptive objective |
| Real-Time Aligned RM | `TRAIN-RLHF` | Ch31 / Ch27 | Refine — policy-relative reward state |
| MAPPA / Sweet Spot / Continual GUI | `TRAIN-GRPO` | Ch33 / Ch29 | Refine — process credit, bounded shaping, continual adaptation |
| TAPPA | `INFER-KV-CACHE` | Ch45 / Ch41 | Integrate — temporal-pattern budget signal |
| AgentLongBench / SABER / TAM-Eval | `PLATFORM-EVALUATION-SYSTEM` | Ch66 / Ch62 | Integrate/Refine — evidence shape, risk curve, artifact maintenance |
| Token filtering / THINKSAFE | `PLATFORM-SECURITY` | Ch72 / Ch68 | Refine — training-state and safety-data boundaries |
| DeepSearchQA | `AGENT-RAG` | Ch76 / Ch72 | Refine — set completeness and stopping |
| MemOCR | `AGENT-MEMORY` | Ch77 / Ch73 | Refine — heterogeneous visual compression |
| SPARK | `AGENT-PLANNING` | Ch79 / Ch75 | Integrate — dynamic branching |
| Deep Search Monitor | `AGENT-REFLECTION` | Ch80 / Ch76 | Refine — selective slow monitor |
| KAPSO | `AGENT-WORKFLOW` | Ch81 / Ch77 | Refine — repository-as-state loop |

其余 disposition 与章节级去重证据见 W05 Candidate Scoring；该表只列形成主线或组合 family 的 owner，
不是用一行替代 43 项审计。

### W06 weekly-gated Books Review

W06 已完成 41/41 scored rows 的最终 disposition 与周级反向检查。21 项长期机制进入或 refine 15 个
Stable Node owners；15 项以相邻章节中的具体机制去重；4 项只保留 publication/version/domain state；
Claude Opus 4.6 因 system card 无法全文读取，独立保持 `Unverified / Blocked / No Books Change`。
Review 同时纠正了周报中遗留的全周 Books-blocked 状态和两处与 primary source 不一致的 URL，并确认
Sequential Attention 的 2022 feature-selection family 不是 Transformer Attention 演进。Discovery Recall
仍为 Open；恢复 Claude 全文或新增 in-window family 时必须重开本周 Gate。

| W06 mechanism family | Stable owner | Current / Legacy | Final disposition |
| --- | --- | --- | --- |
| ERNIE elastic subnetworks | `MODEL-MOE` | Ch21 / Ch21 | Integrate — deployment profile contract |
| HySparse / LycheeDecode | `MODEL-LONG-CONTEXT` | Ch22 / Ch22 | Integrate/Refine — selector ownership granularity |
| Focus-dLLM | `MULTIMODAL-GENERATIVE-PARADIGMS` | Ch24 / N/A | Refine — mutable-state refresh |
| Fast AR Video / Infinite-World | `MULTIMODAL-WORLD-MODELS` | Ch25 / N/A | Refine — temporal/spatial split and lossy hierarchy |
| SPARKLING | `TRAIN-PRETRAINING` | Ch28 / Ch24 | Integrate — parameter/optimizer state migration |
| D-CORE | `TRAIN-SFT` | Ch29 / Ch25 | Refine — decomposition-aware tool trace |
| Multi-Task GRPO / LUSPO | `TRAIN-GRPO` | Ch33 / Ch29 | Integrate/Refine — effective gradient mixture and length weighting |
| Token Sparse / POP | `INFER-PREFILL` | Ch43 / Ch39 | Integrate/Refine — reversible sparsity and phase-aware plan |
| FASA | `INFER-KV-CACHE` | Ch45 / Ch41 | Refine — query-dependent staged recall |
| DFlash | `INFER-SPECULATIVE-DECODING` | Ch48 / Ch44 | Integrate — target-conditioned diffusion drafter |
| Anthropic 0-days | `PLATFORM-SECURITY` | Ch72 / Ch68 | Refine — proposal/reproduction/disclosure lifecycle |
| Sage | `AGENT-RAG` | Ch76 / Ch72 | Refine — Agent-query/retriever interface |
| MemSkill | `AGENT-MEMORY` | Ch77 / Ch73 | Refine — versioned memory-operator policy |
| OpenAI CFPS lab | `AGENT-WORKFLOW` | Ch81 / Ch77 | Refine — typed physical experiment authority |
| Kimi K2.5 / WideSeek / AOrchestra | `AGENT-MULTI-AGENT` | Ch82 / Ch78 | Refine — bounded dynamic fan-out and executor contract |

其余 20 个 `No Change / Weekly Only / Unverified` disposition 及章节级证据见 W06 Candidate Scoring；
该组合表用于呈现演进主线，不代替逐项 Source Review。

### W11 weekly-gated Books Review

W11 已完成 55 个 scored candidates 的逐项 disposition 与周级反向检查：31 项长期机制进入或 refine
17 个 Stable Node owners；20 项以 Books 中的具体机制去重；Lost in Backpropagation 因缺少可部署替代
head 的端到端证据保持 Emerging；Neural Thickets 与 SFT-versus-RL 保持 Weekly Only；Groundsource 及
4 个未评分 identity/full-text gaps 按用户确认的 blocked-skip 规则保留，不进入 Books。每个新增段落均保留
旧方案成立条件、作者实验边界、新状态与 failure mode；没有把厂商 benchmark、单篇 speedup 或版本功能表
写成通用结论。

主要 owner 路线为：representation objective 与 multimodal/audio state；Attention/Sampling/MoE/Long Context；
data/pretraining/GRPO；prefill/KV/execution plan；evaluation；Context/Memory/Planning/Workflow。完整 55 项账本、
No Change 的章节级理由和 5 项材料缺口见 W11 Candidate Scoring 与 Books Integration Decision。W11 Source-
Family Books Gate Complete 不关闭 broader Historical Archive Gate；任何新恢复的 in-window family 都必须重新
打开本周 Gate。

### W12 weekly-gated Books Review

W12 对 49 个 candidate families 完成最终 disposition：48/48 个 `20+` Source Reviews 与 Astrolabe
低分边界均已复核；23 项新机制和 11 项既有论证精化进入 17 个 Stable Node owners，11 项以具体章节
论点去重，GPT-5.4 mini/nano、DSX Air 与 Astrolabe 保持 Weekly Only，RAMP 保持 Emerging。

整合以演进链为单位，而非按论文逐条追加：单 residual state 到 depth routing；完整 logits 物化到 exact
fused sampling；静态数据到 graph/evidence-grounded trajectory；pretraining 到 mid-training/adaptive depth；
固定 feedback/verifier 到 uncertainty selection、adaptive verifier、phase credit 与 rollout service；静态
offload 到 conditional expert cache；flat Context/Memory 到 structured selection、typed stores 与 evidence
anchors；静态 Agent workflow 到 verifiable milestones、editable policies、recursive spine 与 two-timescale
adaptation。每条路线都保留旧方案适用条件、实验边界和新增 failure mode。

W12 Source-Family Books Gate Complete 不关闭 broader Historical Archive Gate；新增 in-window evidence
仍会重新打开本周 Gate。完整候选到 owner 的 mapping 见 W12 Books Integration Decision。

### Cross-week Multimodal Source-Family Owner Table

下表是跨周的新 Part owner 汇总，不是 W11 的候选明细；W11 的 55 项最终账本只位于 W11 周报。

| Source Family | Stable owner | Current / Legacy | Final disposition |
| --- | --- | --- | --- |
| OmniSIFT | `MULTIMODAL-REPRESENTATION` | Ch23 / N/A | Refine — modality-role-aware compression |
| Unified Latents | `MULTIMODAL-REPRESENTATION` | Ch23 / N/A | Refine — bounded rate/capacity contract |
| LongCat-Next / DiNA | `MULTIMODAL-REPRESENTATION` | Ch23 / N/A | Integrate — Experimental |
| Qwen-Image-2.0 | `MULTIMODAL-REPRESENTATION` | Ch23 / N/A | Refine — bounded case |
| Scaling Native Multimodal Pre-Training | `MULTIMODAL-REPRESENTATION` | Ch23 / N/A | Emerging / Experimental |
| LLaDA2.1 | `MULTIMODAL-GENERATIVE-PARADIGMS` | Ch24 / N/A | Integrate — editable generation |
| ProSeCo | `MULTIMODAL-GENERATIVE-PARADIGMS` | Ch24 / N/A | Refine — correction-aware generation |
| DDTree | `MULTIMODAL-GENERATIVE-PARADIGMS` | Ch24 / N/A | Refine — budgeted tree verification |
| Multi-Block Diffusion LM | `MULTIMODAL-GENERATIVE-PARADIGMS` | Ch24 / N/A | Integrate — Experimental block branch |
| Diffusion Templates | `MULTIMODAL-GENERATIVE-PARADIGMS` | Ch24 / N/A | Refine — bounded refinement evidence |
| DDiT | `MULTIMODAL-GENERATIVE-PARADIGMS` | Ch24 / N/A | Refine mechanism / Disputed performance |
| SenCache | `MULTIMODAL-GENERATIVE-PARADIGMS` | Ch24 / N/A | Integrate — Experimental approximation cache |
| Agent World Model | `MULTIMODAL-WORLD-MODELS` | Ch25 / N/A | Refine — synthetic environment boundary |
| Hybrid Memory / HyDRA | `MULTIMODAL-WORLD-MODELS` | Ch25 / N/A | Refine — static/dynamic memory |
| Looped World Models | `MULTIMODAL-WORLD-MODELS` | Ch25 / N/A | Refine — recurrent transition |
| WorldKV | `MULTIMODAL-WORLD-MODELS` | Ch25 / N/A | Refine — state/memory layering |
| Persistent-State World-Model Evaluation | `MULTIMODAL-WORLD-MODELS` | Ch25 / N/A | Refine — evidence contract |
| MolmoAct2 | `MULTIMODAL-EMBODIED-VLA` | Ch26 / N/A | Integrate — reasoner/controller layering |
| MPAIL2 | `MULTIMODAL-EMBODIED-VLA` | Ch26 / N/A | Refine — online dynamics and real feedback |
| DreamZero | `MULTIMODAL-EMBODIED-VLA` | Ch26 / N/A | Refine — world-action policy |
| Xiaomi-Robotics-1 | `MULTIMODAL-EMBODIED-VLA` | Ch26 / N/A | Refine — breadth to embodiment alignment |
| ExoActor | `MULTIMODAL-EMBODIED-VLA` | Ch26 / N/A | No Change — already covered; evidence limited |

Tuna-2 继续 `Disputed`；GameWorld、blocked revision 和 identity gaps 继续留在材料账本。新 Part 不是前沿论文容器：只有形成 representation → generation → world state → physical action 主线的机制进入正文。

## Owner Coverage Audit — 2026-08-13

- 已完成 Source Review 且保留 legacy Ch1～80 owner 的候选，通过上方 legacy mapping 获得唯一 Stable Node owner，无需机械改写历史周报。
- 四个曾明确缺少 owner 的可访问 family 已处理：OmniSIFT 与 Unified Latents 归 `MULTIMODAL-REPRESENTATION`，DDiT 与 SenCache 归 `MULTIMODAL-GENERATIVE-PARADIGMS`；DDiT 只吸收机制，争议性能 claim 继续冻结。
- 其余新 Part family 逐项记录在 Source-Family checkpoint；ExoActor 为 `No Change — Already Covered`，Tuna-2 为 `Disputed`，GameWorld 与材料账本 family 为 `Unverified / Blocked`。
- compiler/kernel/quantization/accelerator co-design 沿 `MODEL-* / TRAIN-* → INFER-TENSORRT-LLM → PLATFORM-GPU-SCHEDULER` 读取；AI for Science 沿 `TRAIN-DATA → PLATFORM-EVALUATION-SYSTEM → AGENT-WORKFLOW → PLATFORM-SECURITY` 读取。二者是明确的跨章路线，不是未分配材料。
- 本轮没有仍可访问、已完成全文审计但因七 Part 结构无法承载的 `Structural Candidate`。若新候选不能由 Stable Node、明确 `No Change` 或证据状态解释，必须重新打开结构审计，不能静默留在 Weekly。

## Prior Books Integration Summary（Provisional, Legacy Numbers）

以下段落记录 7-Part 迁移前的 provisional checkpoint，章节号均为 Legacy Number。后续结构审计已推翻“无需增加 Part”的判断，并由 ADR-008 替代；其已核验机制桥梁仍保留：

- Model / Training / Hardware：Ch17 的可控 Post-LN 分支、Ch21 的 router-to-dispatch
  coupling、Ch32 的 communication backend contract、Ch34 的 asynchronous PP 演进、
  Ch45 的 workload-contract co-design；
- Inference / Runtime：Ch44/52 的 adaptive speculation、Ch47 的 heterogeneous cache
  identity、Ch48 的 expert/KV locality 与 selection control plane；
- Evaluation / Governance：Ch62 的 executable artifact、Ch63 的 autonomy telemetry 与
  private aggregation、Ch68 的 policy-bound privacy sensor 与 experimental GRAM；
- Agent / Workflow：Ch73 的 derived memory、Ch74 的 deterministic domain tools、
  Ch77 的 workflow-visible serving 与 physical experiment authority、Ch78 的
  task–topology matching。

J-space、ELDR、DSpark 与 Dynamo 已有正文经全文重审后保留并补足证据边界。Sequential
Attention 和 overthinking 修正了 first-public/publication-state；TurboQuant 标记为
`Disputed`。其余候选有明确 Weekly-only disposition，未为制造 diff 强行写入 Books。

最终相邻章节审计还补上三条跨 owner handoff：

- Ch47 → Ch48：engine 拥有 typed cache payload 与 restore/replay correctness，distributed
  selector 只拥有带 generation/freshness 的摘要，远端命中仍需目标 engine 重新验证；
- Ch68 → Ch63 → Ch62：入口 privacy sensing、受证明约束的 aggregate observability 与
  evidence judgment 分层，任何一层都不能单独推出匿名、合规或证据充分；
- Ch73 → Ch77：derived memory 是带 provenance/scope 的 advisory state，不因历史成功而
  自动获得修改 approval、retry、budget 或 side-effect semantics 的 authority。

## Sources and Evidence Boundary

每周来源、完整阅读结论与 claim/evidence boundary 位于各自 `README.md`。年度索引不将
机构页面、作者 benchmark、arXiv 预印本或 discovery index 升级为更高 Evidence Level。

## 2026-08-14 W22 Books Integration Checkpoint

W22 已完成 43/43 final dispositions：38 Refine、3 No Change、2 Weekly Only；42/42 `20+`
families 均有 current-version Full Source Review，旧 27 个 access blocker 已恢复为 primary-text evidence。
17 个 Stable Node owners 完成逐项与相邻章节复核。长期机制沿 World Model、Training、Inference、
Platform 与 Agent 主线吸收，重点包括 multi-agent world state、stubborn-token recall、heterogeneous
retrieval、Memory counterfactual diagnosis、parallel-draft architecture/training split、execution snapshot、
DPU security plane、Skill benefit decomposition 和 digital-twin promotion Gate。

Source-Family Books Gate Complete；Scholar/OpenAlex/DBLP cross-index recall 仍使 Archive/Discovery Gate
保持 Open。W22 无 blocked、pending 或 Disputed family，Books cursor 进入 W23。

## 2026-08-14 W23 Books Integration Checkpoint

W23 已完成 33/33 final dispositions：10 Refine、7 No Change、4 Weekly Only、1 Emerging /
Revision-sensitive、11 Unverified / Blocked。22 个 current-version Full Source Reviews 与 blocked-skip
边界逐项复核；StreamMA v2 没有倒写缺失的 v1 event snapshot 或 runnable implementation。

长期机制集中为 shared-interface/separate-owner World Model、repository-derived adapter、harness-owned
recoverable Context、autoregressive KV-quantization feedback、cumulative planning constraints、reward-hacking
onset audit 与 decoupled speculative commit protocol。Archive/Discovery Gate 继续为 11 blocked families、
StreamMA revision gap 与 cross-index recall 开放；Source-Family Books Gate 完成，游标进入 W24。

## 2026-08-14 W24 Books Integration Checkpoint

W24 已完成 38/38 final dispositions：25 Refine、9 No Change、1 Weekly Only、1 Emerging /
Revision-sensitive、1 Withdrawn provenance record、1 Unverified / Blocked。36/37 个 `20+` families
有 current-version Full Source Review；blocked environment-engineering survey 不获得机制 owner。

长期 refine 将 sparse-attention selector gradient 接到 KV-outer execution，将 binary speculation 扩展为
有回滚边界的 multi-tier verification，分开 continuous trust-region correction 与 branch counterfactual credit，
并补齐 KServe desired/applied/observed state、workflow-level Agent serving capacity 和保留 epistemic status 的
note-to-Skill compilation。Archive/Discovery Gate 仍为 blocked family 与 cross-index recall 开放；
Source-Family Books Gate 完成，游标进入 W25。

## 2026-08-14 W25 Books Integration Checkpoint

W25 已完成 35/35 final dispositions：24 Refine、7 No Change、1 Weekly Only、1 Emerging、2 Unverified /
Blocked。32/34 个 `20+` families 有 current-version Full Source Review；两项 blocked family 不获得机制 owner。

长期 refine 将 Context token reduction 与 canonical prefix/segment lifecycle 联合起来，为 vLLM 定义跨 KV spec、
tier policy、connector、scheduler、parser 与 security gate 的 request revision contract，并补齐 MoE fusion 与
communication headroom、training convergence benchmark、multi-principal Memory ACL/forgetting，以及 typed
Agent Session 的 branch/merge/persist/replay。Archive/Discovery Gate 继续开放，Books cursor 进入 W26。

## 2026-08-14 W26 Books Integration Checkpoint

W26 已完成 40/40 final dispositions：30 Refine、7 No Change、1 Weekly Only、2 Unverified / Blocked。
37/39 个 `20+` families 有 current-version Full Source Review；AOHP 与 Self-Compacting Agents 不获得机制 owner。

长期 refine 将 Memory 的 representation/extraction/retrieval/maintenance 拆分进一步连接 workload bottleneck，
为 TensorRT graph-native collective 补齐 per-rank engine、communicator lifetime 与 all-rank progress，增加实时
多模态 thinker/performer 的 state-preserving deployment branch，并把 Computer-use evaluation 扩展到 dynamic
checkpoint、user-simulator 与 persistent artifact state。DFlash W26 只作工程演进节点。Books cursor 进入 W27。

## 2026-08-14 W27 Books Integration Checkpoint

W27 已完成 34/34 score-row 与 33/33 unique-family dispositions：21 Refine、7 No Change、5 Weekly Only，
另有 1 行 Seed2.0 source-family 重复关系。33 个 unique `20+` families 均完成 current-version Full Source
Review，无 blocked、pending 或 Disputed family。

长期 refine 把 adapter 从 repository-derived state 继续推进为 specification-compiled、可签名与撤销的 neural
program artifact；把 Memory 从无限 transcript 推进为 bounded typed visibility；把 resource/trace ingestion
连接到 temporary-pool、held-out-evaluation 与 publish/rollback Skill Gate；把长期 Agent workspace 定义为隔离、
凭据、审批与恢复的生命周期单元；并在 Evaluation 中加入 reference-artifact replay 与 dense proxy/future-return
alignment。asynchronous Pipeline Parallel 与 ELDR 的既有演进经复核保留。Archive/Discovery Gate 继续开放，
Source-Family Books Gate 完成，游标进入 W28。

## 2026-08-14 W28 Books Integration Checkpoint

W28 已完成 30/30 final dispositions：18 Refine、6 No Change、2 Weekly Only、1 Emerging 与 3 Unverified /
Blocked。27 个可访问 family 均完成 current-version Full Source Review；AgentLens、UP 与 Ideas Have Genomes
严格 blocked-skip，没有获得机制 owner。

长期 refine 将 on-policy distillation 拆成 same-prefix online、teacher-prefix replay 与 weak-to-strong relative
policy-shift 三个共存分支；为长期视觉流补齐 entity resolver、identity-critical commit 与 asynchronous enrichment；
把 linear trace 推进为保留原证据的 dependency/root-cause derived view；并定义 deterministic offline world 只拥有
数据生成与回归证据，live shadow/canary 才拥有 deployment promotion。既有 J-space、DSpark、PyTorch、GRAM、
KV 与 Attention 结论经相邻章节复核保留。Source-Family Books Gate 完成，Archive/Discovery Gate 继续开放，
游标进入 W29。

## 2026-08-14 W29 Books Integration Checkpoint

W29 已完成 38/38 final dispositions：22 Refine、9 No Change、2 Weekly Only、1 Disputed 与 4 Unverified /
Blocked。34 个可访问 family 均完成 current-version Full Source Review；四个 blocked family 无机制推断。

长期 refine 把 on-policy distillation 的 absolute teacher、matched-base delta、outcome Gate 与 optimizer/sharding
recipe 放到同一训练身份中；为 Harness evolution 增加相邻 revision 的 bounded local-search 分支；把 semantic
next-state prediction 降级为不能越过 IAM/policy/approval 的 sensor，并要求 actual-state reconciliation；将
variable-length batch 变成在合法 plan 集中选择的 runtime state，同时保持 global-token/update 与 checkpoint
不变量。K3 与 Xiaomi-Robotics-1 的既有 integration 经复核保留。Source-Family Books Gate 完成，Archive/
Discovery Gate 继续开放，游标进入 W30。

## 2026-08-14 W30 Books Integration Checkpoint

W30 已完成 25/25 final dispositions：17 Refine、3 No Change、3 Weekly Only、1 Emerging 与 1 Disputed；
25/25 均有 current-version Full Source Review，无 blocked 或普通 pending。

长期新增机制集中为两项：把 Agent instruction/config/memory 视为分层可变的 self-state asset，联合静态保护、
workload-conditioned detection、semantic authorization 与 recoverable backup；以及将 RAG 从 point/list ranking
推进到显式 coverage、redundancy、conflict 与 complementarity 的 set-level evidence utility。Dynamo、SGLang、
HiKV、Native Multimodal 等既有 integration 经复核保留。Source-Family Books Gate 完成，Archive/Discovery
Gate 继续开放；历史游标完成 W30，下一步进入 W31 live-week Books review。

## 2026-08-14 W31 Books Integration Checkpoint

W31 已完成 26/26 final dispositions：14 Refine、7 No Change、5 Weekly Only；全部评分行都有最终
Source-Family decision，无 blocked、pending 或 Disputed family。

本周新增而非重复的长期机制只有两个：`INFER-KV-CACHE` 将 fixed-budget compression 从 hard eviction / merge
推进为 exact main 与 approximate residual 分离，并保留 stale residual、双路径 kernel 与 workload drift 边界；
`INFER-SCHEDULING` 将单点 profiling / linear extrapolation 推进为 saturation-aware component model、在线校准
与 silicon canary 的闭环。ScientistOne、Kimi K3、MCP、vLLM 与 Agent 相关机制经逐项联读保持原 owner；五项
版本或机制不足的记录没有被强行写入 Books。Source-Family Books Gate 完成，Archive/Discovery Gate 继续开放，
游标进入 W32。

## 2026-08-14 W32 Books Integration Checkpoint

W32 已完成 44/44 final dispositions：24 Refine、7 No Change、5 Emerging、3 Unverified / Blocked Identity、
3 Weekly Only Version Facts 与 2 low-score / pre-release boundary records；0 Review Pending。三项 identity gap
没有获得机制 owner，Archive/Discovery Gate 继续开放。

除 Daily 已落地的 tokenizer、Long Context、Workflow、typed Memory、PD accounting 与 Evaluation 主线外，本轮
补齐九个 Stable Node 的演进缺口：router choice 与 topology-aware replica placement 分责；verifier-state
semantic draft retrieval；bounded formal verification 与 plausible-world safe commit；dependency-localized Memory
update 与 search-derived Skill publish Gate；state-matched distillation 与 prompt-robust RLVR；brief-to-task contract；
elastic GPU configuration portfolio；sparse off-HBM KV working set；以及 versioned stateful counterfactual evaluation。
Source-Family Books Gate 完成；没有新增 Part、章节或 Stable Node。

## 2026-08-16 W33 Live Weekly Checkpoint（Superseded by 2026-08-17 Correction）

W33 完成 7/7 Daily 与 21/21 candidate Full Source Reviews；最终 disposition 为 16 Refine、5 No Change，
0 Review Pending、0 Blocked。Beyond Routing 按 8 月 9 日 v1 日期留在 W32，Intern-S2 report 只作为已有
model family 的 related primary source，不重复制造 release event。

长期 refine 收束为三条路线：TP/KV/MoE/Autoscaling 的控制粒度由 consumer semantics、state liveness 与
可验证 cost regime 决定；Prompt/Memory/Workflow/Skill 从追加状态推进到 provenance、selective repair、
transactional activation 与 bounded associative read；diffusion tree、latent prefix、selective teacher signal 与
Agent-generated proof artifact 均保持 proposal/authority 分离。W33 Source-Family Evidence/Books Gates 通过，
7 Part / 84 章结构、ROADMAP 与 DECISIONS 不变。该完成声明已由下方 discovery correction 取代。

## 2026-08-17 W33 Discovery Correction

W33 原 21 项 Full Source Review、16 Refine / 5 No Change 与既有 Books 修改保留，但 discovery replay 证明
Sunday scan 没有召回 8 月 14 日展示批次。QuoteBench、OmniScientist、Beyond Final Scores 与 AlayaWorld 已
完成正文、实验、限制和关键 Appendix/artifact 审计，令 scored Full Reviews 增至 25；另有 32 项仅完成 identity
发现，尚待 event date、revision、去重、评分与全文审计。

因此 W33 状态为 `Discovery/Evidence Gate Reopened`：三项 correction 为章节级 No Change，QuoteBench 为
`Books Pending`，32 项 queue 不进入 Books。年度 `1168 scored + 32 discovery pending` 只作 provisional arithmetic，
不能用来宣称 archive census 或 W33 Books Integration 完成。7 Part / 84 章结构、ROADMAP 与 DECISIONS 不变。
