# 第三有限题摘包：8 篇精确 v1

作者 mar14_supplement 2026-10-09，实际完整 title/AB/Comments/可见版本史，入口来自既有四个主题发现查询，不增加分类/机构范围。精确 URL、UTC 查询时刻、200/bytes 在 `SUP_ABS_THIRD_MANIFEST_RESULT.json`，八原件为 `SUP_ABS_<ID>.raw/.txt`。Submitted 只作机会发现；下面潜力不等日期、Evidence、评分或 Books。

| ID | 完整题摘后的最小语义判断 | 当前层 |
| --- | --- | --- |
| 11542 ReHARK | 一次样本 CLIP cache 的局部估计/边界偏差 → RKHS global proximal 与 semantic/visual anchor、bridge、distribution rectification、多尺度 kernel；可能改变小样本 adaptation 的 regularization 接口，但多模块组合的必要增量尚不清楚 → 定点核 global objective 和局部 estimator 差额即可。Related SSRN DOI 明示先稿身份线索，若准入再核决定性公开事件。 | 决定 core |
| 11556 DIAE | 内容相同但 aesthetic 不同的完美 paired data 稀缺 → 同语义弱匹配对上的 dual-branch supervision + explicit multimodal guidance → 生成编辑的 supervision 不能只当完美对应关系，须核分支如何隔离内容/属性信号；不是仅 aesthetic 指标或领域应用准入。 | 窄潜力 |
| 11558 RoboClaw | 采集/部署 controller 分离且人手 reset → forward/inverse Entangled Action Pair 的 self-reset collection loop 与同 controller 部署 policy primitives → 数据采集与动作执行的上下文一致性/恢复失败路径可能改变；25%/53.7%只是待核作者数，不授物理安全。最新 v3 存在但本次用 v1，轻量当前说明未见纠错宣告。 | 窄潜力 |
| 11563 SVLL | 联训过早 temporal binding、相对 DPO 只提升 preference gap → spatial/temporal staged grounding 与 ground-truth absolute likelihood Bias-DPO → 判断偏好优化是否保持可行动作应核 likelihood/affordance 的实际约束；摘要“ensures strict”不授保证。 | 窄潜力 |
| 11578 Hikari | 流式 speech 的 READ/WRITE 独立 policy/heuristic → probabilistic WAIT token、Decoder Time Dilation、delay recovery SFT → streaming causal commit 与质量/延迟选择可变化，不能只收 BLEU。实际 v1 AB 不继承最新 September IWSLT 描述；v2 修改信号没有当前勘误说明，不无差别比版。 | 窄潜力 |
| 11583 UtilityMax | 多目标自然语言 prompt 歧义 → influence diagram/expected utility 的形式化 prompt → 目前只见目标改写和 MovieLens 收益，尚不清楚是否有新的优化/执行或有效性条件；定点 core 核图/utility 是否由模型自述或独立求解及对照。 | 决定 core |
| 11617 NA-MVP | noisy labels 污染 VLM prompt global alignment → region-aware unbalanced OT、clean/noise 双向 prompt 与 selective relabel → prompt 学习的标签/跨模态对齐选择可能改变；不把自动 relabel 说成真实标签恢复，需独立噪声/区域反侧。 | 窄潜力 |
| 11619 Taming OpenClaw | 点式防御难捕捉跨时段 agent authority 漂移 → 五生命周期 taxonomy 和 compound threat case；摘要未说明哪条实际失效能改变已有权限/记忆安全设计 → 只读必要案例与防御失败/信任接口，不能以安全题目直接排除或自动准入，也不读攻击战术全篇。 | 决定 core |

本包五窄潜力、三决定 core已由root实际完整题摘/当前说明校准；三core随后实际必要原件独核为1窄P/2具体EX，见`SUP_CORE_DECISIONS_THIRD.md`。11542SSRN早稿事件门另核，五明确潜力仍需日期与最低评分投入；不是默认五项都5分或有Books缺口。不得将八篇或四查询全部标题机械变成全文队列。
