# Daily Research — 2026-03-26

**规范：** V3
**窗口：** 2026-03-25T09:00:00+08:00 ～ 2026-03-26T09:00:00+08:00
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-02T04:36:50+08:00

## 1. 结论

确定候选1个唯一家族：Model Spec 发布说明及同时公开的 Model Spec Evals。深入审阅1项，已将 local rubric 的人工正反例校验、角色不兼容时的有效测量分母，以及重复评分不能消除共同偏差的边界融入 Ch66。两段正文已经非作者写后检查；mar01最终非作者日级验收通过，普通待办0。

23个相关线索因首公开日期或决定准入的事实未定而隔离，不评分、不计 Evidence 完成或 Books 成果。四主题 API 交叉返回84条仅为有限发现，不是84个当日新家族，也不是逐项全文队列。当前14每日来源的可用入口已处理至下表所述停止；历史切片与公开时刻限制不能支撑无遗漏断言。旧报告完整保留在[原文](../_sources/daily-20260326/V3_LEGACY_REPORT.md)，不继承旧候选、评分、EffectiveDate 或完成标签。

## 2. 来源覆盖

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | 实际 RSS 757893B/1242 items，仅 Mar24～27 六邻接 title/link/pubDate；25T10Z主文及 linked suite 本窗，原字段见[记录](../_sources/daily-20260326/V3_OPENAI_RSS_FIELDS.md) | 已检查 | 仅当前可恢复的定点历史切片，不认证全站 |
| SRC-ANTHROPIC | Research March九项原 publishedOn 字段；23T23Z三篇与24T10:41Z均左界前，31T22:17Z右界后 | 已检查 | 有限 Research March，不扫描科学应用论文 |
| SRC-GOOGLE-AI | Research March两页14 cards，25日XR必要核心已读；DeepMind page3 24 cards及 Lyria/Manipulation/FlashLive 原JSON-LD；pubs首页1～15/11569 | 受阻 | Google pubs本窗历史切片未恢复；不能用年度目录授本窗零命中 |
| SRC-META-AI | Blog页1 10/页2 12非日序；TRIBE完整核心按项目范围关闭；正确 results publication 当前444行，实际0～369含Sep→May→旧2019 | 受阻 | Research/publication本窗历史切片未恢复；不是所有正文无法访问 |
| SRC-QWEN | 官方API40/40完整title/id/date，Mar19T04+08→Mar30T04+08夹窗；原字段定点复用24目录记录 | 已检查 | 当前返回范围，不认证已删除历史项 |
| SRC-DEEPSEEK | 公开Research数组31条与News16 posts完整原字段，Feb25→Jun24、2025Dec1→Apr24夹窗 | 已检查 | 仅实际可见数组，不以17个日期字符串冒17篇文章 |
| SRC-MOONSHOT | 官方Kimi en/blog19 dated cards，Feb9→Apr20夹本窗 | 已检查 | 当前19项有限目录 |
| SRC-TENCENT-HUNYUAN | publicList renderType0/page1/size20，实际9/total9；Feb3/13→Apr23及以后两原字段完整对读 | 已检查 | display与publishedAt不互代首次公开 |
| SRC-ZAI | Research15 dated cards Mar15→Apr1；release16 Feb12→Apr7 | 已检查 | 当前返回，非全机构历史证明 |
| SRC-BYTEDANCE-SEED | type1/year2026/token20/count100实际18/82,next40,true；type2/token0实际14/19,next空,false；相交TopoMesh/RobotFlywheel完整v1题摘 | 受阻 | Blog返回少5项及两论文原公开日期未定；目录午夜不当正文精确首发 |
| SRC-BAIDU-ERNIE | Blog有限第一页10 dated cards，Apr/May→Feb6/Jan29夹窗 | 已检查 | 当前有限切片 |
| SRC-XIAOMI-MIMO | 首页Paper8 dated June29→Mar13→Feb3；Blog15无date；正确Pro/Omni原页为Mar18日字段 | 受阻 | 本窗dated Blog/SeeMore历史切片未恢复，不继承错误路径故障 |
| SRC-MINIMAX | EN12/CN13 dated cards，Mar18→Apr27/May26；AgentTech当前.md已恢复882B，仅May13 dated index项窗外 | 已检查 | 当前可见入口，无具体线索不额外扩历史档案队列 |
| SRC-ARXIV | [四主题API原返回](../_sources/daily-20260326/V3_ARXIV_THEME_RAW.json)：submitted Mar24T01Z～26T01Z，start0/max25/降序；系统9/9、学习25/119、多模态25/29、Agent评价25/166，另相关标题有界查漏 | 受阻 | 23潜在线索原公开精度/必要事实未定；未返回页不是逐项工作队列，不授全学科召回 |

上述目录只复用身份与原字段，窗口归属和贡献另判。必要 artifact 为表外：[dataset](https://github.com/openai/model_spec_dataset)、[harness](https://github.com/openai/model_spec_evals)，只读取拟采用命题需要的 README，不扫描所有 GitHub release。有限来源与准入停点见[本日唯一记录](../_sources/daily-20260326/V3_WORKING_STOPPOINT.md)。

## 3. 候选与判断

三维为 Design Delta、System Reach、Durability，各0～3。只给确定落窗且通过贡献筛选的家族评分；主文、suite与代码为同一发布家族，不重复计数。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |
| [Model Spec 发布及 Evals](https://openai.com/index/our-approach-to-the-model-spec) | 2026-03-25T18:00:00+08:00 | 从条款可追溯推进到条款—场景—local rubric的测量校验，分开rubric、grader与人工标签故障，并明确角色skip和相关评分边界；2 + 2 + 3 = 7 | 深入完成 | 整合：PLATFORM-EVALUATION-SYSTEM，[Ch66“长篇Policy要先编译成Versioned Atomic Tenets”](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)既有论证内两段 |

## 4. 证据与知识整合

### [Model Spec 发布及 Evals](https://openai.com/index/our-approach-to-the-model-spec)

必要套件：[Model Spec Evals](https://alignment.openai.com/model-spec-evals/)。

官方 RSS 原值 `Wed, 25 Mar 2026 10:00:00 GMT` 是主文的公开时刻；主文“同时发布”所链接 suite，因此同一发布事件落窗，不把 Evals 的日期显示擅自补成另一个时刻。作者实际读主文、suite 的 dataset/grading/limitations，以及必要 dataset/harness README；没有复现实验或认证全部实现。

Dataset针对225条款建立596短文本场景，local rubric只说明该场景对应的部分规范。人工构造合规/不合规假想答案用来查rubric误译、grader误用和人工标签错误，而不是假定条款清楚就评分正确。Blog的配置为20 target samples和五次grader评分取中位数、6～7判合规；harness默认target/grader各一次，不能把默认运行称为Blog结果复现。Dataset README指向2025-12-18 Spec，公开API消息角色限制导致9例skip：要保留有效分母，不能把未运行义务当通过。

这是受限测量方法，不是校准概率或部署安全率。五次同grader采样不能消除共同rubric偏差；短文本、日常、非对抗场景不覆盖工具/多模态/真实Agent长交互。原结果没有重要性或生产流量加权，旧模型按新政策测还混入训练年代差异。没有采用速度/吞吐结论，hardware、precision、长度、batch、concurrency、SLO性能条件不适用；具体grader、场景及阈值仍必须随评价协议固定。

对照当前[Ch66](../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)的atomic-tenets段：原有多轮规范编译与finding追溯，但未在该链中展开“rubric本身先被人类正反例检验”和角色无法保真时的skip分母。实际将两段插在该机制之后、Annotator/Policy Identity之前；保留原规范编译、多轮对抗成本和旧静态rule适用条件。新段落交接为：条款可追溯 → 测量翻译正确性 → 重复评分的偏差边界 → annotator/policy身份。来源标记为 `SF-2026-OPENAI-MODEL-SPEC-EVALS-20260325`；Review notes只保存精确配置与限制，不承载机制正文。mar01已实际原core、owner/邻接写后PASS；最后新增role-skip句亦独立实际核验，不把作者自检当验收。

具名负侧：XR完整核心是源码模板/提示与既有API封装，60内部prompt/5次模拟器实验混合framework bug和不存在API，没有独立归因出新的执行/适用边界；Lyria3 Pro时长与结构控制发布未披露新内部机制或受控的质量/成本边界，旧SynthID/过滤器重述不另当机制增量。TRIBE是fMRI/临床预测研究，属暂缓Science而非本项目世界状态机制。CoDesign综述完整v1题摘归纳data movement、quantization、scheduling与层级角色，未提出可检验的新LLM设计边界；不是因为“综述”标签一律排除。上述只是具体关闭依据，不代表全部原始库存均已全文审阅。

## 5. 缺口与下一步

普通待办0。必要证据、实际Books修改及非作者日级验收均已完成；下列外部保留项不是正面Evidence或Coverage通过。

本窗终态保留项共23个潜在线索，不支持正面证据、Books或无遗漏断言，既不是确定候选，也不是23篇证据通过：

| 身份/精确版本 | 必须进一步判定的命题 |
| --- | --- |
| [2603.23640v1](https://arxiv.org/abs/2603.23640v1) | Edge持续热约束改变端侧serving边界 |
| [2603.24652v1](https://arxiv.org/abs/2603.24652v1) | pruning隐藏/logit稳定不等生成probability轨迹稳定 |
| [2603.24579v1](https://arxiv.org/abs/2603.24579v1) | MARCH孤立checker与多Agent纠错控制 |
| [2603.24533v1](https://arxiv.org/abs/2603.24533v1) | UIVoyager分叉轨迹监督与训练控制 |
| [2603.24517v1](https://arxiv.org/abs/2603.24517v1) | AVO变体内核与Agent训练调度 |
| [2603.24440v1](https://arxiv.org/abs/2603.24440v1) | CUA连续视频/运动学相对稀疏截图的信息损失 |
| [2603.24587v1](https://arxiv.org/abs/2603.24587v1) | DreamerAD shortcut latent及reward/GRPO路径 |
| [2603.24584v1](https://arxiv.org/abs/2603.24584v1) | TAG原观察与object-erased预测差值的steering |
| [2603.24581v1](https://arxiv.org/abs/2603.24581v1) | LatentWAM几何蒸馏压缩与动作动态 |
| [2603.24506v1](https://arxiv.org/abs/2603.24506v1) | PhyGenesis无效轨迹纠正与条件生成 |
| [2603.24458v1](https://arxiv.org/abs/2603.24458v1) | OmniWeaving交错跨模态对齐；新增机制相对组合的准入事实仍未定 |
| [2603.24329v1](https://arxiv.org/abs/2603.24329v1) | GameplayQA角色/时间/决策密度评价盲区 |
| [2603.24270v1](https://arxiv.org/abs/2603.24270v1) | ScrollScape全景时序先验与ScanPE/ScrollSR |
| [2603.24060v1](https://arxiv.org/abs/2603.24060v1) | v1 SOMA三组件是否产生新可靠性条件尚未定；不改用后版RoboHarness身份 |
| [2603.24558v1](https://arxiv.org/abs/2603.24558v1) | LensWalk自适应观察时间/密度是否构成新接口条件 |
| [2603.24586v1](https://arxiv.org/abs/2603.24586v1) | TRACE人类部分context与judge混杂 |
| [2603.24278v1](https://arxiv.org/abs/2603.24278v1) | TopoMesh监督/预测DMC同拓扑对应 |
| [2603.24570v1](https://arxiv.org/abs/2603.24570v1) | Anti-I2V双空间防御；不由摘要采用防护率 |
| [2603.23117v1](https://arxiv.org/abs/2603.23117v1) | TRAP从patch经CoT到VLA动作的安全反证 |
| [2603.25583v1](https://arxiv.org/abs/2603.25583v1) | RobotFlywheel factor-space collection/training；Seed日期与Submitted不一致 |
| [2603.23049v1](https://arxiv.org/abs/2603.23049v1) | PCR prefix-tree lookahead/层加载并发/SSD预取改变queue与reuse关系 |
| [2603.28795v1](https://arxiv.org/abs/2603.28795v1) | StepCache任务验证→局部patch/fallback；不能把局部可验证性外推所有任务 |
| [2604.03279v1](https://arxiv.org/abs/2604.03279v1) | Lightning TTS精度脆弱性与NoC/SRAM/LoFi联合设计；不由单成本数采用 |

首19个原Submitted/Created/registered/Updated/Available及完整v1题摘在[精确字段](../_sources/daily-20260326/V3_EXACT_ABSTRACT_DATE.json)（该文件另含CoDesign负侧）。常规最早计划slot并非实际公告：除TRAP/PCR跨左界外，大多数最早26BJT08～DOI findable登记上界跨右端09；24652登记更晚。Registered不是精确公开时间，月份Available与v1Updated也不能补造时刻。RobotFlywheel Submitted26T16:00:39Z在本窗后，Seed26整日午夜仍未证原文早公开；PCR registered25T02:15:12Z跨左界，StepCache/Lightning登记分别Apr1/Apr7，不按ID或Submitted强塞March。完整新增题摘与原字段见[有限补检](../_sources/daily-20260326/V3_EXTRA_DATE_STOP.md)。

每个材料只请求一次：需要其 exact-v1实际官方公告/批次及可取正文上界，或可核作者原首次公开时刻/完全落窗区间；Robot/Topo另可接受Seed原事件字段语义与对应首次正文时间。Omni/SOMA/Lens还需决定准入的具体机制或条件位置，不要求无差别全文附件。现有题摘/必要安全核心已读，不再请求同份PDF；收到证据只重开该身份的日期→准入→必要证据/Books，不顺带重跑整月。暂不进入Books或性能/安全保证。

来源限制：Google pubs本窗dated slice；Meta Research/publication本窗slice；MiMo当前15无日期Blog的本窗dated slice；Seed type2少5项的身份/日期或差额解释；arXiv本窗实际公告身份/时刻或版本公开范围。请求这些具体切片，不要求全机构全历史export，也不将有界主题未展开页转成永久逐项任务。

## 6. 复核

复核者：mar01（非作者；实际suite/必要artifact、Books两段及role-skip句写后，以及最终全日Gate）。

结论：通过

mar01实际完整读六部分、唯一停点、四主题参数/返回数、RSS六行、20项exact身份/原日期与EXTRA四题摘/字段；对23保留项核日期和采用隔离，不称23项全文审计。具名分层实际核CoDesign完整v1题摘及SOMA/Omni/Lens准入消歧，Lyria265～294、TRIBE40～53、XR必要core；四负侧理由通过，不授84交叉返回全审或全学科召回。唯一ModelSpec的必要主文/suite/dataset/harness以及Ch66两段/role-skip句实际POST通过，本轮又读2838～2884邻接与4245源注，Blog20/5与harness默认1/1边界准确。完成态V3校验、本日报/来源/Ch66限定diff-check通过；格式检查不代替上述语义判断。旧有效证据完整保留，未stage、commit或push。
