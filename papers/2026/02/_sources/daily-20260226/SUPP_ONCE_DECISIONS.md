# 一次决定核心：2026-02-26补查

首批root指明四项只核准入决定事实，已读取下列exact-v1核心。只是决定贡献，不是标准/深入Evidence；支持日期尚缺的潜力不继续实验/全文。

| 身份 | 实际位置及贡献判断 |
| --- | --- |
| 2602.20610 SpecMind | §4 Algorithm/Fig2，SUPP_ONCE_2602.20610.txt L475–920：`type∈{explore,submit}`，只有submit评test/mutant-derived completeness并更新best-so-far；探索/提交历史进入后续prompt，threshold/diminishing returns/max μ控制stop。不只“多turn反馈”命名：拟保checker调用与reasoning探索机会分离的局部执行/预算机制潜力；未采用其correctness保证或效果。日期未证，保留不评分，不继续实验。 |
| 2602.21009 HiSAC | §3.3–3.5，SUPP_ONCE_2602.21009.txt L480–715：RQ-VAE离散codebook复用，top-k层级vote选择interest centers；明确`frozen semantic similarity`决定所有history到centers的路由，而`trainable ranking embeddings`独立决定所汇总的value，使未匹配SID的长尾history仍输入。拟保路由语义与下游value更新分开的可迁移压缩状态机制潜力，而非CTR、interest-agent命名或映射longcontext。日期未证，不继续实验。 |
| 2602.20597 InterFormer | §3.2开头L740–805/§3.4 L1583–1675：contact-boundary选择语义feature再与learned query结合；CoCo根据预测hand mask pixel-count≤τ惩罚关联object pixel-count，hand被判断present则不罚。确有任务新loss配方，非“没新技术”，但该增量为六个EgoHOS语义mask的手/对象关系规则和boundary prior组合，未改变foundation表示、VLA学习/动作接口或通用query/更新的有效性条件；不将预测mask逻辑当物理因果，拟当前主线贡献EX，不因小模型或没有生产试验而拒。 |
| 2602.20644 Scenic | §2.2–2.4，SUPP_ONCE_2602.20644.txt L220–395：新schema把TARGET waypoint列表换为behavior intent+relative positioning，Jinja2 topology templates用既有VerifaiRange注入速度/距离采样；LLM自身semantic check、deterministictoken normalization和missing-field hard-coded defaults。不是仅因分层结构而EX：比旧DSL的实际变化为traffic场景表示/地图renderer适配和已有probabilistic language工具使用，未新增通用模型schema约束、独立verifier或执行失效判据；CVC violations目标验证不是representation一致性的通用proof。拟具体贡献EX，停止，不采legally-grounded/safety或全部variant忠实保证。 |

除表中局部段外没有投入评价/消融/附录，也不声称文章全proof或实验已经核验。原件SUPP_ONCE_*.raw/.txt与真实fetch批次V3_FETCH_supplement-once.json保留，等待root非作者窄核。

## root非作者最终窄核（2026-10-08）

root实际读四个once核心及10完整AB。SpecMind的explore/submit与checker调用、best-so-far支持局部Agent预算机制潜力，InterFormer/Scenic具体贡献EX通过。HiSAC作者初案“可迁移压缩state”撤销：实际RQ-VAE/层级interest vote和frozen semantic QK/trainable ranking V是推荐暴露偏差/长尾SID的具体方案，原文没有foundation long-context、模型压缩或通用更新成立条件新证据；把成熟attention分工迁移为longcontext是我们的类比，不是原文增量，最终贡献前EX。保留完整AB/已读核心和本改判依据，不降评分（尚未确认落窗而未评分），不因为推荐领域/小实验一律EX。最终4日期潜力＝WoG/20569/20826/20610；10AB中其余7明确EX，无普通审阅/once剩余，待六部分DAY。
