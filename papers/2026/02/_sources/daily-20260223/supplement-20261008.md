# 2026-02-23 增量来源补查

作者：supplement_20260223。执行：2026-10-08T20:04～20:15+08。补充窗口：2026-02-22 ～ 2026-02-22；旧09:00窗口、原候选0、评分及连续§4不改。只本日README/_sources写权，无Books、索引、LEARNING_STATE写入；未stage/commit/push。

## 1. 冻结与复用

[完整基线](./supplement-baseline-20261008.md)81行/13146字节，cmp与启动README逐字一致，sha256 `4868278fe28637f13418b473a93bf3648a821f185b180c162ec1536461942b27`。第一次合并输出被工作树库存截断后，已单独完整重读报告与V3_SCREENING，不从截断输出保存基线。基线保存本身使用独立完整输入；cmp实际通过。原候选0及§4无需重审，不继承旧完成标签为本轮验收。

本轮确定新增0、深/标准审阅0、Books实际写入0。完整题摘32是具名有限查漏，不是32份证据审阅：27潜力因首公开日期未证终态隔离，5贡献前关闭。没有以日期难恢复降低分数或用Books覆盖缩池。

## 2. 查询范围与停止

原入口HTTP/请求/执行时间见[首次native](./supplement-native-20261008.json)、[有限恢复](./supplement-native-recovery-20261008.json)、[主题查询](./supplement-topic-requests-20261008.json)。正文响应保存为同目录`supplement-<入口名>-20261008.raw`。web辅助搜索仅用于恢复线索：[四组日期词](./supplement-date-search-20261008.json)、[加官方域名限制后](./supplement-narrow-search-20261008.json)；首组误命中OpenAI社区特性建议/作品，不视为官方研究，已收窄且未将其变为题摘队列。

| 来源 | 本轮实际入口与停止 | 结果和限制 |
| --- | --- | --- |
| SRC-OPENAI | 官方RSS完整XML；实核Feb20 First Proof 14:30Z→Feb23 Frontier Alliance05:30Z/SWE-bench11:00Z | 已检查feed自然日；无Feb22事件，非全站无遗漏 |
| SRC-ANTHROPIC | 官方Research raw完整发布数组publishedOn；Feb18 autonomy15:10Z→Feb23 fluency11:52Z/persona11:53Z | 已检查该发布数组；无Feb22，不用插图_createdAt |
| SRC-GOOGLE-AI | Blog page6十二卡片含Feb17→Mar4相邻；Pubs首页年/会议信息；DeepMind Research和news page6实际为当前汇总页 | Blog有界检查；论文/DeepMind日切片受阻，G1保留，不把page参数证明历史页 |
| SRC-META-AI | Research首页及Blog page2；Feb09 DINO→Mar11 MTIA，混有2025卡片 | 历史论文日切片受阻，G2，不称列表完整 |
| SRC-QWEN | 新blog客户端壳+旧github.io迁站提示；限定域名日期辅助搜索 | 历史日期目录受阻，G3，无新窗内原源，不以空结果授覆盖 |
| SRC-DEEPSEEK | 当前主页模型入口；限定域名Feb22查询 | 无历史研究切片，G4；受阻不是不适用或零命中 |
| SRC-MOONSHOT | Platform Blog可读列表最新2025-11-07；限定域名Feb22查询 | 2026历史切片受阻，G5 |
| SRC-TENCENT-HUNYUAN | 首查Research；IAB一次63.97s timeout；正确POST publicList pageNum1/pageSize100/renderType0返回totalNum9英文9条，Feb13 token-gradient→04/22显示事件 | 英文9条非中文“全部”，G6；GET405已修成POST，不拿错误响应授零 |
| SRC-ZAI | Research完整15卡片，Feb21 GLM-5→Mar15 Turbo，早于Feb22/晚于Feb22 | 已检查当前日期排序卡片；目录入库不作当窗修订或首公开 |
| SRC-BYTEDANCE-SEED | asc2026论文page_token0,count100实际20卡片，Feb13 FLAC→Feb25两项；Blog9卡片Feb14→Apr1，后3pinned均窗外，has_more/next20记录后停 | 已越Feb22边界，不翻后窗库存；PublishDate仅目录显示不是候选首次公开 |
| SRC-BAIDU-ERNIE | Blog首页日期Feb06→Apr15；限定官方域名日期查询 | 已检查该Blog切片，无Feb22线索 |
| SRC-XIAOMI-MIMO | Blog实际客户端壳+限定官方域名日期查询 | 完整历史切片不能恢复，G7；不把当前壳或零搜索记正面覆盖 |
| SRC-MINIMAX | 英/中blog完整可读卡片到Forge英Feb14/中Feb12、M2.5Feb12→Mar18；中站重定向minimax.cn | 已检查目录有限范围；日期都窗外，不为解决不存在的当窗归属读全文 |
| SRC-ARXIV | availability原文周五/周六无公告，Feb22 BJT周日对应ET周六/周日上午，无标准批次。四主题及相关标题补检见下 | 标准批次边界已查；非标准原源日期不能由Submitted证明，27终态日期保留不授完整Coverage |

arXiv首次四查询误用`date-date_type=announced_date`返回表单，不计有效零。原表单明示`announced_date_first`仅年月精度。随后改为Submitted(original) Feb21–22作线索，不是扩大准入窗口。第一次OR字符串systems命中82条仅看首50相关标题，已收窄，不翻第二页且不把82逐项关闭。修正为独立OR字段的主线题摘查询：MODEL(language model/transformer/MoE)首页50/85；SYSTEM(LLM inference/GPU kernel/distributed training)19/19；MULTIMODAL(multimodal/world model/VLA)41/41；AGENT(language agent/RAG/tool calling)15/15。仅相关/含糊的具名32完整题摘保存并读取，跨查询去重；这些命中数不是Feb22首次公开数量。其余宽标题不被统计为题摘已审，首页停止限制保留，不承诺全学科召回。

用于补检公告日的月列表`/2602?show=2000`五分类404；格式恢复为`/2026-02?show=2000`后返回官方“Authors and titles for February 2026”月表，没有日头。一次解析期望h3未命中，另检查原HTML确认只有月份h2、身份链接带空格，故`matched=[]`不是身份不存在/零命中。只为具名身份恢复日期，不读月表全部标题，不把月表变队列；月表不是本次日期证明。请求见[列表尝试](./supplement-date-lists-20261008.json)、[原源有限日期恢复](./supplement-public-date-recovery-20261008.json)及[实际必要HTML片段](./supplement-month-list-signal-20261008.md)。不再恢复全月分页/后续周批次。

## 3. 首批准入校准与完整题摘

[完整题摘32](./supplement-selected-abstracts-20261008.md)131行/46587字节完整保存，已分段读取；原长输出截断不充当完整读取证明。root已独立实际读MoBiQuant、Blackwell、Habilis、RoboCurate、WANSpec、DualScale、HillInfer、ACAL八潜力与四代表EX，随后完整读余20，认可27潜力并将incTNP贡献前关闭。全部27潜力与5EX均覆盖题摘准入层，不授Source全文完成。root六部分DAY已通过，实际边界见§6。

五贡献前关闭项：CHORUS(2602.19016)是专业翻译用户工作流收益，完整摘要未给改变通用执行机制/失效判断的增量；DeepInnovator(2602.18920)与Vibe-Proving(2602.18918)明确科学研究应用，按AI for Science暂缓，不用Agent/Training重引；Flow-GRPO survey(2603.06623)按目标/模态整理既有研究，没有具体设计纠错证据。incTNP(2602.18955)明确借用LLM causal masking/KV/AR训练用于TNP流式回归；implicit Bayesianness测的是TNP规则，未提出新的LM cache正确性/学习条件或足以修正通用机制的反证，不能把应用“流式一致性/成本”改名当长期增量。此处不因模型小、负面结果或局部实验排除潜力，也不把综述身份本身当排除理由。五项已明确关闭贡献，不为其日期再造请求；incTNP先前原件字段已取得，保留而不建终态日期请求。

## 4. 27具名潜力的安全终态与一次日期请求

下列各项已读完整题摘，增量是作者声明、尚未证据审阅，不作本文采用命题。统一一次请求：需要对应身份精确版本的**首次公开正文日期**原始公告/作者发布字段，明确2026-02-22北京自然日归属；可接受官方日公告或作者带明确公开日期的原件+身份链接。arXiv ABSv1的Submitted、citation_date/citation_online_date，编号、月份列表和搜索Date均不能替代。已一次取28个exact-v1 ABS、轻量核日期/相关撤回纠错字段，未观察到官方撤回/勘误状态；摘要里reflection correction等不是修订信号。见[原件请求与字段](./supplement-date-originals-20261008.json)，每项原页完整保存为`supplement-DATE_<ID>-20261008.raw`。

| 身份（精确v1原源） | 具体潜力与为何值得日期核验 | 当前终态 |
| --- | --- | --- |
| [2602.18733](https://arxiv.org/abs/2602.18733v1) Prior-Aware metric | 常见后缀误判memorization→跨IID前缀先验比较→重评泄漏评价 | 日期未证，不评分/全文/Books |
| [2602.18734](https://arxiv.org/abs/2602.18734v1) CoRAG | reranker不对称依赖→联合协作目标→重评检索/生成训练边界 | 日期未证，不评分/全文/Books |
| [2602.18739](https://arxiv.org/abs/2602.18739v1) PhysCond-WMA | 感知质量不保证动力学正确→物理条件攻击→重评world-model安全 | 日期未证，不评分/全文/Books |
| [2602.18742](https://arxiv.org/abs/2602.18742v1) RoboCurate | 视频可看不保证action正确→sim-replay动作验证→重评合成数据准入 | 作者页datePublished Feb21及项目页无初公开链；仍不证Feb22 |
| [2602.18746](https://arxiv.org/abs/2602.18746v1) MIRROR | 文本反思脱离图像→区域grounded验证监督→反思证据边界 | 日期未证，不评分/全文/Books |
| [2602.18750](https://arxiv.org/abs/2602.18750v1) HillInfer | SSD I/O与CSD算力瓶颈→只下沉importance+分层KV/预取→状态成本取舍 | 日期未证，不评分/全文/Books |
| [2602.18755](https://arxiv.org/abs/2602.18755v1) DualScale | PD不同阶段动力学→placement+DVFS双时标→能耗/SLO协调 | 日期未证，不评分/全文/Books |
| [2602.18782](https://arxiv.org/abs/2602.18782v1) MANATEE | 二分类边界被绕过→benign流形密度/hidden-state投影→安全/utility边界 | 日期未证，不评分/全文/Books |
| [2602.18813](https://arxiv.org/abs/2602.18813v1) Habilis | reset成功率漏漂移→TPH/MTBI连续运行+cyclic示范→VLA可靠性协议 | 日期未证，不评分/全文/Books |
| [2602.18846](https://arxiv.org/abs/2602.18846v1) DUET-VLM | 合并/丢弃各有限→视觉压缩+层间文本引导丢弃→训练/推理质量成本 | 日期未证，不评分/全文/Books |
| [2602.18849](https://arxiv.org/abs/2602.18849v1) Exact Attention Sensitivity | 集中度不等于敏感度→softmax精确Jacobian/分布二分量→稳定性判断 | 日期未证，不评分/全文/Books |
| [2602.18851](https://arxiv.org/abs/2602.18851v1) Rank-Aware bounds | rank-blind溢出界粗→交互矩阵rank/谱范数尺度→FP8安全条件 | 日期未证，不评分/全文/Books |
| [2602.18896](https://arxiv.org/abs/2602.18896v1) Beyond Stationarity | codebook更新滞后encoder drift→未选code同步/映射→量化崩塌归因 | 日期未证，不评分/全文/Books |
| [2602.18904](https://arxiv.org/abs/2602.18904v1) PCA-VAE | VQ非微分/崩塌→Oja在线PCA瓶颈→latent表示替代 | 日期未证，不评分/全文/Books |
| [2602.18916](https://arxiv.org/abs/2602.18916v1) ACAL | unstructured解释不可contest→argument图/冲突裁决/人工修改→执行透明性 | 日期未证，不因法律实验场景自动拒 |
| [2602.18922](https://arxiv.org/abs/2602.18922v1) Agent caching | 分类准确率≠cache安全→key一致性/精度分解+RCPS→cache评价边界 | 日期未证，不采用成本投影 |
| [2602.18931](https://arxiv.org/abs/2602.18931v1) WANSpec | 跨地域闲置容量→远端draft+冗余→通信/latency取舍 | 日期未证，不评分/全文/Books |
| [2602.18940](https://arxiv.org/abs/2602.18940v1) DREAM | 静态citation评价漏时间事实→评价agent工具能力对等→评价盲区 | 日期未证，不评分/全文/Books |
| [2602.18948](https://arxiv.org/abs/2602.18948v1) Symmetry reduction | 坐标冗余→invariant relational变量→架构/优化参数化 | 日期未证，不评分/全文/Books |
| [2602.18968](https://arxiv.org/abs/2602.18968v1) Layered orchestration | 精细计划脆弱/成本高→粗层依赖+局部schema修复→重规划粒度 | 日期未证，不评分/全文/Books |
| [2602.18993](https://arxiv.org/abs/2602.18993v1) SeaCache | 原feature差混noise/content→谱过滤再cache调度→质量/latency归因 | 日期未证，不评分/全文/Books |
| [2602.18997](https://arxiv.org/abs/2602.18997v1) Matrix SMD | 标量implicit bias不足→matrix mirror/Bregman插值解→优化inductive bias | 日期未证，理论适用假设未审，不外推LLM |
| [2602.19008](https://arxiv.org/abs/2602.19008v1) Canonical path | 同模型同任务随机失败→within-unit轨迹漂移/monitor→能力vs可靠性 | 日期未证，不采用因果/干预数字 |
| [2602.19017](https://arxiv.org/abs/2602.19017v1) Why ReLU | Real-RAM忽略有限精度→activation bit-complexity二分→可学习计算假设 | 日期未证，不评分/全文/Books |
| [2602.19041](https://arxiv.org/abs/2602.19041v1) Blackwell | 循环多目标无单最优→MaxEntBW/PROSPER非标量化→偏好优化解概念 | 日期未证，不评分/全文/Books |
| [2602.19043](https://arxiv.org/abs/2602.19043v1) COIN | NTP编辑绑定前文→local-scope编辑与context恢复测试→知识更新边界 | 日期未证，不评分/全文/Books |
| [2602.20191](https://arxiv.org/abs/2602.20191v1) MoBiQuant | bit-width间outlier迁移→递归残差+token-router→精度弹性设计 | 作者页仅2026；日期未证，不评分/全文/Books |

这些潜力的必要日期与原件已经一次有界恢复，未证落Feb22即停止；不展开全文、完整修订史、后续周批次或全年历史队列。材料到达只重开对应身份的日期，然后才准入/评分/必要深审；在此之前不支持候选、正面Evidence/Coverage、Books或任何性能/安全保证。不是普通pending，也不需要用户等待全文。

## 5. Books与后续

确定候选仍为冻结0+新增0；Books No Change，未构造未证日期的具体采用命题，故没有书稿提案或共享owner锁。原G1～G7继续隔离，不改原有效Source层结论。来源/题摘/有界日期工作已停止，普通待办0；本日独立DAY及完成态静态验收通过，结束本日，不自行换日。

## 6. 非作者DAY与最终静态验收

复核者：root（非本轮报告作者）。结论：通过。

实际完整读六部分、32完整题摘（27潜力日期隔离/5贡献前关闭）、必要月份HTML信号；复核十四入口请求、正确OR查询实际50/85、19/19、41/41、15/15及有限停止，错误表单/空解析不授零命中。27潜力全部复核准入与终态隔离，5EX全部实际核验；不把具名集核验称为宽列表全量或全学科召回。原0、原窗口和连续§4保留，新增确认0/Books0，27仅准入潜力不授Source完成，G1～G7精确隔离。19008因果/能力固定是待核主张，18739安全与18733测量反证潜力保留。没有Books写后内容需验，普通待办0。

完成态`validate_research.py --report papers/2026/02/23/README.md`V3通过；README12+补查Markdown17本地引用29全部存在（字节冻结baseline以原README路径为链接基准）；原候选0、旧窗口及连续§4逐字验证通过；本日README/_sources限定cached和unstaged diff-check通过。机器不授语义truth，验收边界以root上述DAY为准。未stage、commit、push或清理；用户既有与并发修改保持原样。
