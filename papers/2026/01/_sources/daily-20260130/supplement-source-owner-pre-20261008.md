# 2026-01-30 增量必要证据与 Books PRE/POST记录

原63家族、原评分/日期和原有效Source/Books均复用，不在这里重审。

## SF-2026-QWEN3-ASR：5，标准完成，拟仅报告

公开日依据[官方News](https://github.com/QwenLM/Qwen3-ASR)的2026.1.29，日粒度解除旧小时隔离。精确artifact采用[Jan29初始README](https://github.com/QwenLM/Qwen3-ASR/blob/9567667698f195fa807b1581de5c03184e63d2b0/README.md)及同commit streaming example，原件 supplement-qwen-initial-readme-20261008.txt / supplement-qwen-initial-stream-20261008.txt。GitHub第一页5commits已到底，commit只版本身份，不代替public日证明。

初稿公开接口有实质可采用的局部分支：同一ASR模型提供offline/streaming，streaming当时仅vLLM、无batch、无timestamps；另一个NAR forced aligner给文本—语音配对词/字时间。初始example的state保存unfixed_chunk_num=2、unfixed_token_num=5、chunk_size_sec=2，逐段更新state.text，结束另调用finish；可支持这份接口区分中间转写状态和完成刷新，不授每次text不可变/真实commit保证。不以缺NAR内部细节忽略这个已公开runtime机制。

2000倍throughput仅宣传concurrency128，硬件/precision/音频长度/端到端测量配置未在该必要README披露；不用其证明SLO、timestamps准确度或普遍offline≈stream质量。示例静态核读非运行、无GPU验收；Jan30后unicode修复不回填本release，也不扩其它日期。

当前owner比较：MULTIMODAL-REPRESENTATION [Ch23](../../../../../books/part-03-multimodal-world-models/23-multimodal-representation.md) §Full-duplex输入（470–491）已明确channel-local状态/显式safe point与外部不可撤回输出不同；§时间空间（717–760）已明确timestamp proposal与采集时钟/provenance分责及数值head与AR时间接口的替代条件。Qwen为本次版本的ASR状态刷新与单独aligner提供可复查实现接口，但本日公开证据未增加相对于这些论点的新稳定适用条件或质量/成本反证；因此保留该局部runtime事实在日报，不以通用commit原则借分或强造书稿差额。不是整家族MechanismNotDisclosed。

## SF-2026-PADDLEOCR-VL-15：6，重要release受影响内容深入完成，拟仅报告

公开日[官方中文公告](https://ernie.baidu.com/blog/zh/posts/paddleocr-vl-1.5/) Jan29。必要原稿V3_PADDLEOCR_CORE.txt及 supplement-native-core-20261008.json，官网引言/能力/Real5/推理性能部分实际读。支持不规则polygon定位、文本spotting、Real5基于OmniDocBenchv1.5的scan/skew/warping/screen-photo/lighting五类真实场景slice；不是版本号或新增语言计分。

反侧：公告架构为图示，未用controlled factorial分开polygon/新训练/数据/模型共同变化；94.5总体分不能归因polygon，也不能由‘SOTA’认证所有物理畸变。速度图协议为单A100、batch512、含PDF渲染/Markdown、各系统默认DPI与PDF模块；不是相同输入分辨率/同模块的单因素收益或单请求latency。硬件A100披露，precision与concurrency未在必要段披露；长度/DPI各默认而非锁定。未运行pipeline/复现实验，论文后续v1公开不作本release新首次。

当前owner比较：Ch23 §§为什么文本token经验不能复制/四层identity（16–35）、§时间空间（717–741）已经承载region/reference-frame/augmentation lineage与估计几何非真值；PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) §Clean Ranking故障切片（761–783）明确clean总体与corruption分开、低光处理链身份/实际相机失配和不授唯一因果。新的polygon能力及五slice任务事实有局部release贡献，但现公告不足在这条已覆盖推理链上形成新机制/有效条件或controlled反证，所以仅报告，不强改两owner，不把领域排行榜代替长期知识。

## SF-2026-OPENAI-INHOUSE-DATA-AGENT：6，标准完成；具体 gap 定点深入，拟整合 AGENT-CONTEXT

必要[官方Jan29工程说明](https://openai.com/index/inside-our-in-house-data-agent/)保留 supplement-first-native-primary-20261008.json；本文核心 How it works、六context layers、evaluation/security、lessmore/guidegoal/meaningincode 已读。采用95–137的生产代码语义→每日离线归一化→相关context检索→无/陈旧context live query与用户确认save memory分责。148–161的golden SQL+result comparison和pass-through permissions是该内部实现的作者声明，不是独立安全认证或controlled效率归因。更少工具/少路径指令经验没有matched ablation，不能写成所有Agent定律。没有稳定性能数字采用；hardware、precision、batch、concurrency、SLO均Not Disclosed。

现Ch75§Context Serving102–125有source-linked multiview/freshness，但数据表的producer逻辑与schema/query-history的语义缺口没有具体承载；后邻接SPADE127–130只拥有build/test图且明确不替代代码语义。Ch76§Offline Ingestion45–68拥有索引编译/发布及source truth；Ch77§Context/Memory与Write分型拥有持久提交，Ch74prompt只软条件不授权限。差额属于派生Context生产与在线补查，唯一owner Ch75，不复制索引或Memory规则。

### 拟正文：置于Ch75 CodeNib段之后、SPADE段之前（两段）

对数据表，schema 与查询历史在命名稳定、表语义简单时足以导航，却不一定保留生成数据的过滤条件、粒度和更新逻辑。另一条派生视图分支从生产代码抽取这些语义，将它们与表使用信息、人工说明一起离线归一化，再让请求检索相关定义；无定义或视图陈旧时，回到已授权的实时数据与元数据查询。代码说明回答的是“如何构造”，live observation 回答的是“当前是什么”，用户纠错则可以提出需确认保存的持久 Memory；三者不能在一次摘要中获得同等事实与写入权威。<!-- source-family:SF-2026-OPENAI-INHOUSE-DATA-AGENT -->

预计算把重复语义探索移出请求路径，也增加代码抽取、离线刷新、存储与stale-view风险；静态代码理解不证明生产执行和数据 freshness。[内部数据Agent的公开工程说明](https://openai.com/index/inside-our-in-house-data-agent/)支持这条工作流实例，却未以受控消融证明各层的独立收益或通用正确性。生产逻辑难以恢复、权限不足或新数据与旧定义冲突时，应回读原代码、补实时检查或转人工；小语料与低复用任务仍可直接查询，不让自动丰富的Context代替原数据证据、索引发布或Memory提交。

### 拟自身末注（Review notes追加一条）

- `SF-2026-OPENAI-INHOUSE-DATA-AGENT` — Daily `2026-01-30`补漏；[官方Jan29工程说明](https://openai.com/index/inside-our-in-house-data-agent/)六层Context/Runtime Context、Evaluation/Security。2+2+2=6，producer-derived语义与live observation/user-confirm Memory差额定点深入；只采公开workflow，未采用controlled效率、安全认证或prompt普遍经验。未运行内部实现/复现实验；必要Source与实际owner PRE待root，正文未写，未授POST或DAY。

## 有限来源停止与15日期hold

本轮native-0～3补查询均精确Jan29，并复用本日旧14源/有限主题/分页记录，不扩monthly池或Weekly。SRC-OPENAI具名新项补入；SRC-QWEN/BAIDU官方Jan29解除hour hold，但不由此声称完整历史目录恢复。其余11源原明确缺段复用，本轮精确补线索没有新的具名未处理项；完整覆盖限制仍隔离。

15 early arXiv原准入保留且必要AB已有有效，追加current abs仅核身份和轻量notes，不重读全正文；Created只能上界，月列表有限23相关标题没有day下界。补4个代表官方精确identity+Jan29查询无结果，并不是0命中证明；17旧hold中2release已恢复、15arXiv仍终态保留。原19912/19904局部反侧复用、19944非LLM误排除继续撤销，不能借自然日合同将Submitted冒充first-public。

实际复核：root已读Jan29 exact README/stream example、Paddle官方必要核心与OpenAI六层/runtime等原正文，实际比较Ch23/66及Ch75/76/77，3准入与5/6/6评分、两Only和Ch75差额PRE通过。root授Ch75两段与自身末注窄锁；实际写127/129后释放，root顺读114–140与末注771并核完整6行新增差额，非作者POST通过，原CodeNib/SPADE及既有staged变更保留。

root已完成六部分独立DAY：新增3/所有必要Source/两Only/Ch75 POST、来源停止、15日期+2争议隔离和原63保护通过；返修旧/新增衔接为单一完整表与旧统计归属后，完成态V3/links/diff实际通过。本文件保存写前拟文过程，不将拟文中的待验标签作为当前停点。原63表行/原§4连续块逐字保留，合计66家族、6/1/57/2，普通待办0；15日期、历史缺段及2争议不授正面证据或完整覆盖。
