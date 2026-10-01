# 04/23 三项评价研究：有限非作者准入与 owner 对读

2026-09-28。仅核 `2604.19966v1`、`2604.20157v1`、`2604.20202v1` 的必要 exact-v1 方法、关键反证及当前 Ch25/Ch66 论点；不复现实验、不核整日来源/首公开、不代替 04/23 日级 Gate。三项目前仍须以官方公告批次确认日期，不能由 submitted、v1 metadata update 或 DataCite created 单字段归属。

| Family | 独立判断 | 具体证据与 owner 边界 |
| --- | --- | --- |
| [2604.19966v1 DistortBench](https://arxiv.org/html/2604.19966v1) | 保留 5 分、标准审阅；`No Change — Existing Coverage`，不为单个畸变 benchmark 新写 Books。 | exact-v1 §2.2–2.3、§3.8：type×severity 的无参考四选诊断使两种错误不混成单一准确率，故旧泛称“局部视觉任务”不足以前分母关闭。但 Ch66 已在 clean/corruption/missing-modality 矩阵、故障切片与 response-rate/conditional-quality 分母分别保留测量责任；本论文新增的是受限视觉仪器与受测反例，不改变评估 owner 或发布权。主分数仅 answered-only，未解析比例另列；三名人评/256 图，两个 rotation 等级未同样众包验证。五组 base/thinking 中四组下降不能归因为思考本身：token budget/解析与模型配置同时改变。 |
| [2604.20157v1 HumanScore](https://arxiv.org/html/2604.20157v1) | 保留 5 分、标准审阅；`No Change — Existing Coverage`。 | exact-v1 §3–5、§6.2 将单人生成视频拆成 anatomy、kinematics、kinetics 代理，13 个生成器里 VBench imaging/aesthetic 与 kinetics 的 Spearman 约 .349/.328，是“好看不等于物理合理”的受限评价反例，足以保留而非凭 video benchmark 标签关闭。Ch25 开篇已将 video generation 的 perceptual quality 与 action consequence/closed-loop outcome 分开，后续 §World Model 评价亦把 physical-consistency proxy 与真实 transition 分权；Ch66 管 EvalSpec/切片。单目 pose/mesh 重建不适定，真实视频也非满分；model-level human preference 排序不提供逐视频物理真值，更不证明可控 world model。局部六轴 scorer 尚不足改变这条长期链。 |
| [2604.20202v1 Hallucination Inspector](https://arxiv.org/html/2604.20202v1) | 保留 5 分、标准审阅；`No Change — Existing Coverage`。 | exact-v1 §2–4：Android SDK XML 符号表与 AST/局部类型链能确定一部分不存在或 scope 不合法的 API，并非整个 app 的编译或行为正确性。51 组迁移上 precision 1.00、recall .73/.90；参数类型与 callback/signature 漏报，不能把未报警当正确。Ch66 已要求形式化条件先由 deterministic schema/executable verifier 验收、开放歧义才交 judge，并保存 oracle/spec 身份；SDK XML 是这一原则的受限实例，不形成另一发布 authority。正文 RQ2 称 GPT-5 而 §4.2 比较写 gpt-5-mini，模型优劣排序不能采用。 |

以上是三个 Source Family 的有限准入/Books 判断，非 04/23 来源、日期、全部候选或写后审计。没有建议共享 Books 写入。未触及其他日期正式日报。
