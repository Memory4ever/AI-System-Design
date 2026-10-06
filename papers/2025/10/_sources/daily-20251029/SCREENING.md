# 2025-10-29 有限来源、筛选与反侧

作者Curie，窗口BJT [10/28 09:00,10/29 09:00)。每源request.json保存本日真实URL/时间/响应，原件不等已读；不引用其他日候选池。

## 来源及有界补检

原Research优先。DeepSeek/news/实际10项研究、5动态，仅10/21→11/01及09/29→12/01邻接停止；查看全部无href。Google原pubs/DeepMind未恢复日级历史；原October Blog10/27→10/29→10/30邻接，只定点StreetReaderAI核心。Z.ai实际page2补到18项、12/07且没有更多；Seed article_type1+US token80 total94/false，type2 token20 total45/next40/true含10/23→11/27，再已取token40末页false；PublishDate只定位展示日期。Hunyuan中文API page1 size20 renderType0 total11，最早2026/02；本日browser原Research一次15秒超时并reset，无成功状态，不以日历或旧状态授覆盖。MiniMax Agent独立techblog与原生md只2026/05/13，未把中英模型Blog替该入口。MiMo More不是历史分页。ERNIE第二页1/2，邻接10/16→11/07停止。

实际辅助query两条：`site:research.google/pubs/ ("October 28, 2025" OR "October 29, 2025") (language model OR transformer OR multimodal)`；`(site:ai.meta.com/research OR site:qwen.ai/blog OR site:hunyuan.tencent.com) ("2025-10-28" OR "October 28, 2025") model research`。搜索返回其他日期/旧文，只作定位，不授无事件；没有将结果扩为全年目录队列。

arXiv 12分类(CL/LG/DC/AI/AR/PL/OS/PF/IR/MA/CV/RO)三个主线query，submittedDate:[202510271800 TO 202510281800]名义周二批次提交线索：model标题transformer/MoE/attention/language model与training/optimization/architecture；system语言模型与标题inference/kernel/cache/parallel/serving；agent标题agent/multimodal/world model/VLA/diffusion且language/foundation/vision-language或world-model限制。start0/max50，29/9/32小于50即止，去重66非当日数；cs.CL月首50仅相关标题补检，不把2666月库存转队列。官方availability节律不提供这些ID实际first-public；当前summary后续版本与2511延迟ID尤其不能由提交时间准入。

## 完整题摘已读的具体潜力

潜力仅日期隔离，不评分/正面采用。现API版本是定位身份，重开需当窗官方公告或完全落窗bounds，再锁事件精确版。

- 模型/训练：2510.23912 query/key权重冗余假设与小模型；24208跨尺寸activation残差几何转移；24285图像/instance重建自训练；24318 synthetic GMM prior下Bayesian clustering(一般表示/学习潜力不因genomic应用整体排除)；24320先判别后helpfulness critic RL；24824跨loop token并行及共享首loopKV；24709 object-binding子空间受pretraining目标影响；24711视觉MoE显式router guidance；24821稀疏统一语音视觉生成；24514 AR中视觉latent scratchpad；24605 EOS原生变长dLLM。没有以小样本/小模型排潜力。
- 推理/Agent：2510.24051 Pie服务handler+Wasm inferlet；24273潜空间RoPE-free稀疏选token再局部重建；2511.00050 fused forward/backward adapter(提交范围命中不授10月事件)；24390依赖图扩展及generation/expansion跨query调度；24606层次在线sparsity；23822父plan回注与递归active context；24126长horizon训练/测试turn-budget关系；24168观察与验证state delta记忆；24284自动MCP数据生成；24358固定接口PRD judge评价；24636工具证据reward；24695有指导/无指导能力边界数据合成；24259语言→RL内部符号granularity反例。具体机制/有效性条件有潜力，不因现owner已有主题关闭。
- 评价：2510.23948动态ChessQA任务层次可作为窄评价潜力，24299内部相关矩阵rank只是correctness proxy待验证，24427平行真实/合成世界隔离知识与推理混杂。没有把headline正确率当证明。

## 代表排除

完整题摘：2510.24013 LLM发现单机tardiness启发式是组合优化领域算法收益，无新模型/系统机制；24031日志clustering/router/parser仅模块组合与ROUGE等应用指标；24152 driving问型prompt/router/裁图组合未披露新的通用执行边界；23824 grid goal ranking+固定index冲突规则无新协作机制；24109 speech/planner/converter/evaluator模块组合只有场景成功率；24014 TEXT2DB新任务及已有observe/plan/analyze组合，未披露足以改变一般设计的新条件；24030 human/agent trust三模块与城市模拟收益，机制仍是组织蓝图；24459 DOM/Hypermedia pattern语言整理未提供新执行或有效性证据；24337 content-analysis指南、24476 hallucination survey归纳本身不足准入。明确医学、化学、气象/遥感应用及astrophysics replication标题按ROADMAP暂缓，不借Evaluation回收科学应用。含糊或反侧材料没有仅凭主题排除。

GoogleStreetReaderAI原core128–174实际读：Gemini Live输入地理+每步field-of-view，session context“记忆”，11盲人实验有取向/真假判断困难。这是可访问地图应用与现有Live/context能力，未披露新的通用表示/状态执行机制或控制证据；不采用现实行走安全判断，日期仅日名未核实后贡献关闭。Doppel原Blog48–99实际读：filter→并行确认→RFT label→复验→人审回流，80%/3x未有可比数据/阈值/新失效条件，不借成熟反馈原则评分；其他OpenAI本窗组织转型/公司治理按明确标题关闭。

## 七项必要安全/反侧精确v1

均日期隔离，不属于完成候选Evidence；只读足该命题、不遍历全部附录。

- 2510.23766v1 BitSkip：core-bitskip §4(164–180)、§6/6.1(366–376)。Hadamard组合退化是TinyStories/三变体受限反侧，不能外推所有旋转量化失效，也不因局部排潜力。
- 2510.24236v1 faithfulness：core-faith §3–4(98–116)、§6(277–283)。accuracy与faithfulness可反向，CCF依赖LLM抽概念/重要性判定，未授内在因果真值；三模型两dataset，MedQA应用不扩科学支线，BBQ一般盲点保留。
- 2510.24331v1 VLM ICL：core-vlmicl §3.1(78–96)、§4必要黑图/无图对照(122–126)、§5/Limitations139–144，4–9B/三caption数据、英文；黑图保格式与去图改distribution分开，instruction tuning与视觉使用不能由总分等同。未采用截断中间行未读细节。
- 2510.23853v1 TicToc：core-time §3首(83–102)、§4.1末(280–285)、§5(302–310)。v1是34场景700+轨迹/六annotator，与现v3题摘76场景不能混；tool attempt不等正确effect，prefer-noTool不平衡、人类偏好不等环境真值。
- 2510.24411v1 OS-Sentinel：core-sentinel §4.1–4.2(211–233)、§5.1(332–345)、Limitations422–438。Formal Verifier实际SHA256 metadata、敏感词/regex/阈值；Android simulator/UIAutomator2 state trace前提，非完整形式证明，iOS不可直接继承，frozen/live push差异保留。
- 2510.23883v1 Agent security survey：core-security §6.1–6.2及§6.4/6.5(416–432)，既有研究汇总和未来挑战，不把taxonomy当新防线验证；长horizon、相关agent传播、adaptive攻击与人审被操纵的信号保持局部，未逐读全引用。
- 2510.24797v1 subjective self-report：core-experience §3.1–3.2(187–202)、§6首(221–227)。Llama3.3-70B SAE steering控制的是自述/TruthfulQA行为，十seed等不证明意识或SAE标签唯一因果机制；题摘已明确not direct evidence。不可因自述产生模型人格或意识结论。

## 拟候选gpt-oss-safeguard

原Blog及原PDF已实际读到§2/2.1、§3区分和§4.2–4.5必要反侧，PDF共10页但未以附件数作为任务。政策reasoning classifier命题等待独立校准；多policy exact-match与F1不可合并，internal Safety Reasoner非公开模型。聊天not_unsafe/注入层级与provided-policy分类不是同一协议；20B jailbreak和两模型hierarchy可退化，CoT未直接优化且可能偏离政策。硬件、batch、context、并发、SLO/evaluator完整细节Not Disclosed，不采用内部16%compute为公开模型成本。原PDFTable8末列标签重复120b，未擅自修成20b后引用该列。
