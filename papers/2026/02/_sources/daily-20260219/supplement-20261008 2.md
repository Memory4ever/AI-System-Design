# 2026-02-19 遗漏补查停点

执行日2026-10-08；补充窗口BJT2026-02-18完整自然日。原67候选/评分/日期/旧09:00窗口/有效Source与Books冻结。94359bytes[完整baseline](./supplement-baseline-20261008.md)在修改README前与只读git index逐字相同；不stage/commit/push或修改index。作者仅写本日README和本日_sources，root为非作者复核者。

## 实际漏斗

新增四有限主题查询均start0/max100/ascending，实际total=rows分别32/4/15/8，共59次跨主题出现；这是Submitted发现范围而非59当日论文。合并重复并对本日已有有效身份定点去重，31个new身份完整题摘已经作者与非作者读过。14具名贡献前关闭；17潜在贡献因必要first-public日期未恢复隔离。另机构EVMbench有官方Feb18日期，单独计1新增确定候选，标准审阅完成，2+2+2=6，已有覆盖/No Change；非作者root Source/PRE/DAY均已通过，原67+新增1=68。

四query主题：learning为cs.CL/LG的pretraining/representation/generalization/quantization/attention/test-time/reasoning/foundation；system为cs.DC/AR/PL/OS/PF的language model/Transformer/deep learning/LLM；multimodal为cs.CV/RO/SD的vision-language/world/action model/generative/codec/video/flow；agent为cs.AI/IR/MA的tool/retrieval/planning/alignment/collusion/verification/benchmark，要求language/foundation model相关。完整字符串、URL、返回身份与题摘见[原响应](./supplement-arxiv-narrow-20261008.json)与[查询程序](./supplement-query-20261008.py)。Submitted发现范围仅202602161900–202602171900，不能认定公开日。原已有效四主题61/13/20/35和有界CL相关标题前250结果复用，不新增整分类/月队列。补充LG/CV日期列表各一次原入口Cache miss，留下官方backstop历史切片限制，不称全分类召回。

## 17必要公开日期保留（不是确定候选，也不评分）

| 精确身份 | 已可继续的潜在命题 | 当前缺少及定点重开 |
| --- | --- | --- |
| [2602.15136v1 Universal priors](https://arxiv.org/abs/2602.15136v1) | Poisson EB固定prior的未知分布posterior适应及长度界，假设须核 | 同身份首次公开日原公告/作者dated全文；恢复后只读相应理论假设/证明 |
| [2603.04427v1 Thin Keys, Full Values](https://arxiv.org/abs/2603.04427v1) | key selection/value transfer分工、低秩key吸收到Q | v1首次可公开原证据；current v4不替代v1，恢复后核逼近/质量与cache成本 |
| [2602.15283v1 Complex-Valued Unitary](https://arxiv.org/abs/2602.15283v1) | head/readout与几何校准分账及负侧 | v1首次公开原证据；恢复后核同backbone/readout/OOD与sentiment对照 |
| [2602.15353v1 NeuroSymActive](https://arxiv.org/abs/2602.15353v1) | frozen-LLM soft prompt桥接、inner搜索/outer人审与human cost | v1首次公开原证据；决定准入事实已读§3.1–3.4/Algorithm1，不能据此采性能或理论保证 |
| [2602.15368v1 GMAIL](https://arxiv.org/abs/2602.15368v1) | generated数据先独立modality alignment再融合 | 同身份首次公开原证据；恢复后核domain接口而非只增加样本 |
| [2602.15514v1 DependencyAI](https://arxiv.org/abs/2602.15514v1) | dependency-only信号与跨域过预测边界 | 同身份首次公开原证据；恢复后核generator/domain人口与基线 |
| [2602.15552v1 Latent Regularization](https://arxiv.org/abs/2602.15552v1) | boundary测试validity/diversity/fault detection分轴 | 同身份首次公开原证据；恢复后核mix/search/truncation对照与代价 |
| [2602.15586v1 Uniform error bounds](https://arxiv.org/abs/2602.15586v1) | dependent quantized dynamics的block与bits统计条件 | 同身份首次公开原证据；恢复后核dependent-data假设，不外推LLM执行精度 |
| [2602.15336v1 Digital Logic](https://arxiv.org/abs/2602.15336v1) | 主观感知与技术正确性局部反侧 | 同身份首次公开原证据；恢复后核10题24学生/答案judge与顺序任务，不授一般因果 |
| [2602.15388v1 CoverAssert](https://arxiv.org/abs/2602.15388v1) | uncovered function point回映规格的反馈 | 同身份首次公开原证据；恢复后核AST/聚类模块收益与assertion语义 |
| [2603.12269v1 DART](https://arxiv.org/abs/2603.12269v1) | difficulty/DP联合early-exit与ViT质量反退 | 同身份首次公开原证据；恢复后限定model/workload/accuracy-cost对照 |
| [2602.15922v1 DreamZero](https://arxiv.org/abs/2602.15922v1) | video future/action耦合及闭环控制 | 原项目页无可用日期，需同版本作者dated发布/官方公告；恢复后核实时预算 |
| [2602.15819v1 Video Models Prior Enable Versatile Sequential Sketch Generation](https://arxiv.org/abs/2602.15819v1) | 几何ordering与手绘style两阶段信号 | v1首次公开原证据；current v2改题不混用，恢复后核两阶段和七例手绘对照 |
| [2603.08723v1 Alignment Is the Disease](https://arxiv.org/abs/2603.08723v1) | 语言×visible/invisible constraints的局部proxy反侧 | v1首次公开原证据；v1 261 runs与v2 262 runs不同，不用current Iatrogenesis标题/数字替代 |
| [2602.15918v1 EarthSpatialBench](https://arxiv.org/abs/2602.15918v1) | 文字/overlay/coordinate表示与空间任务分轴 | 同身份首次公开原证据；恢复后核表示控制，不因地理场景排除 |
| [2602.15724v1 Navigable retrieval](https://arxiv.org/abs/2602.15724v1) | exemplar/step imitation与candidate pruning分工 | 同身份首次公开原证据；恢复后核召回上限/两模块消融 |
| [2603.13239v1 Solidity prompt tradeoff](https://arxiv.org/abs/2603.13239v1) | CoT/ToT recall与precision反向变化 | 同身份首次公开原证据；恢复后限定400contract决策协议与对照 |

日期恢复已经一次原公告入口与有限具名作者/title查询；[date-backstop](./supplement-date-backstop-20261008.json)、date-search0–4与[精确v1身份](./supplement-exact-identities-20261008.json)、[ThinKeys/project定点](./supplement-author-date-20261008.json)可复查。能取得Submitted/Atom/DOI索引/论文编号/Updated或第三方Feb18，仍不能授权first-public。17项不作正面Evidence、Books、零命中或无遗漏断言；不继续无界日期/附件循环。

## 排除与独立复用

31题摘完整语义与14EX具名原因见[作者准入](./supplement-admission-20261008.md)及[非作者实核](./supplement-independent-20261008.md)。本轮 root 发现ThinKeys漏路由已经补齐，不复用current v4为v1。RUVA必要安全核心§2.1–2.3/§3–4已实际核，标准SQL级联+一次问答demo不建立派生状态删除闭包，维持成熟组合关闭，不为EX追日期；不声称一切图/向量删除不可行或法律合规。本轮新机构OpenAI India仍为capacity/adoption无模型机制，Google教育/science应用保持原有效关闭，无未处理更正信号。

## 14源与停止

实际入口原响应：[西侧](./supplement-entries-west-20261008.json)、[东侧](./supplement-entries-east-20261008.json)、[东侧2](./supplement-entries-east2-20261008.json)、[有限日期字段](./supplement-entry-dates-20261008.json)。官方相关标题/有限具名Feb18搜索仅作恢复线索，不拿当前首页/空响应/无命中证明0事件。

OpenAI Research当前首页及具体EVM/India；Anthropic Research与已有效autonomy初版hold；Google pubs2026 count396当前切片及DeepMind Research，历史缺片；Meta动态0行；Qwen Blog动态0行，有限恢复只见Feb15/Feb10窗外；DeepSeek无日期主页；Moonshot Blog当前2025年末/更早。后六历史限制保留，不借Updated/无hit闭合。

Hunyuan publicList page1 size20 render0，9/total9 title/publicAt/display，Feb13GradLoc与之后Apr/Jul之间无Feb18目录字段，限该目录；ZAI Research Feb11→Feb21和原ReleaseNotes；Seed 2026升序type1 count20 rows20 total82，读到row19 FlowPortrait Feb24UTC=Feb25BJT首次跨截止，type2 rows9 total23至row4 Mar31UTC=Apr1BJT跨截止，has_more仍true不冒充全站读完；ERNIE10可见标题日期Feb6→Jan29夹本日，停止无需更老page2；MiMo Paper Jun29/Mar13/Feb3/Jan8，Blog15无日期历史hold；MiniMax当前12可见标题恢复Mar18→Feb14Forge→Feb12M2.5→Jan27本日切片，不追窗外Forge，补充层已检查该目录但不改原hold。arXiv按上面有限范围，必要公开日/官方backstop缺口明确隔离。

仅Daily14源；未扫描Weekly、Live、缺日报或其他年份，未新触发固定按需名单。链接PDF和作者project仅为必要定点证据，辅助搜索不是全站任务。Coverage终态范围完成不等互联网上无遗漏，历史缺片/17必要日期不授Coverage通过。

## 当前停点

完成态实核：V3通过，原67行同序逐字/原窗口/连续§4前缀保持，六部分齐全。README277本地引用、本轮5 Markdown共294次引用均无缺失，23新JSON均解析通过，本日限定cached与worktree diff-check分别通过。不以静态校验授语义；DAY依据是root的独立实读裁决。

EVM必要Source/owner见[本项](./supplement-evmbench-source-owner-20261008.md)，root首包31题摘/RUVA/EVM日期准入、必要Source与actual owner已有覆盖PRE已通过；全部六部分DAY已非作者root实核通过，实际范围见[独立记录](./supplement-independent-20261008.md)末节。ordinary扫描/筛选/审阅/Books/独立语义待办0，README完成态已同步。进行中态实际V3校验与本日限定unstaged/cached diff-check均通过，原67行/旧窗/连续§4前缀保持，277个README本地引用无缺失（包含重复引用）。外部在本轮中暂存了修改，当前index不再等启动原版；作者与root均未stage/commit/push，不回滚index，以启动时已完整确认的baseline检查冻结，cached与worktree检查分别记录。共享Books无新写入，不写LS/月索引，不接下一日。
