# 2025-10-25 有限筛选与必要反侧

Cicero作者，BJT[2025-10-24 09:00,10-25 09:00)。启动实际重读AGENTS、研究/来源使用说明/每日/按需/arXiv、Report、Prompt、ROADMAP及最新相关路由。只本日窗口与原请求，未加载他日候选池或旧Weekly。FETCH.json/RECOVERY_FETCH.json/EXTRA_FETCH.json保存实际URL、参数、UTC执行时间、HTTP及失败；下载不充当已读。

## 主题与有限补检

四组查询分别为：CL/LG的MoE、mixture of experts、long context、pretraining或language-model distillation；AI/IR/MA的LLM memory/RAG/tool use/prompt injection；CV/RO的world model/VLA/vision-language-action或generative autoregressive；DC/AR/PL/OS/PF的large language model/LLM inference/LLM training/KV cache。实际完整查询URL见FETCH；提交发现带UTC10/24 00:00～25 00:59，仅发现身份，不授first-public。各p0/start0/max80，total3/2/2/3，跨组去重9份当前完整题摘已读，止页0，不续宽类分页。

官方CL月列表skip0/show2000仅作标题线索，实际浏览2510.21000～23500身份带的前15个标题，止2510.21270。21220政治迁移tweets标题明确非模型/系统机制，关闭范围；余14相关完整题摘由id_list/max14单请求恢复，见arxiv_supp.raw/headers。共23唯一论文家族题摘已实读，不把2000月库或全年目录转换为逐项队列。APIcomments定点实读：VeriGray当前v4明确annotation updates/evaluation results，需受影响core；其他已读comments未出现withdraw/correction提示，不等全版本史无信号。

首批实际六精确v1题摘见arxiv_first_v1.raw、[FIRST_CALIBRATION](./FIRST_CALIBRATION.md)，独立校准待root。所有提交字段、月份ID、currentv2/v3/v4不能证明目标窗首次公开/重要修订事件。确定候选0、评分0、候选标准/深入完成0、Books提案/写入0。

## 贡献关闭与潜力

完整题摘明确贡献关闭4家族：21131v1是LLM/TAG方向分类与综述，未给新机制或修正重要判断的证据；21193v2增加原生Estonian七任务/模型与judge相关，没有具体评价盲区或新协议；21084v3是临床用药已有distill+RL组合与领域指标，AIforScience暂缓且未给主线差额；21228v1是临床taxonomy+现有AutoGen/RAG模拟组合，必要安全反侧读后仍无主线新机制。另21220仅明确标题范围关闭，未读摘要、不计23 AB。日期未核不影响这些具体贡献/范围关闭，不称所有历史版关闭。

19家族潜力保留，不因局部/小模型/负面/已覆盖主题缩池：

- 22037v2/v1 ATLAS多语言transfer与从头训/微调compute crossover；21908v2/v1 Hebbian/gradient fast plasticity的成立条件；21175v2/v1 approximate null-space low-rank持续适配。
- 21585v1 REVE的变长/任意电极4D位置表示可能承载跨setup输入机制，不能仅临床词排除；当前只题摘潜力，未认证通用表示或临床收益。
- 21571v1真实人手视频到VLA监督转换；21447v1 PhysWorld物理digital twin扰动→GNN可干预动力学；23629v1 TracePile显式执行监督；23642v2 VisCoder2多语言可执行多turn训练协议。
- 22087v3 QuArch的知识与架构高阶设计评价差异；21059v2 DR-IKE任务效用retrieval+learned阈值；21090v1 Self-Rewarding PPO的SFT/base log-ratio隐式reward；21270v2/v1 token permutation块稀疏prefill。
- 21049v1 reasoning低FPR反侧；21007v3/v1 confidence-gated CoT可校准预算；21034v2/v1输入结构与错误率混杂；21118v4/v1 external-knowledge标注权限与更新；21180v1多Agent一致/积极模拟偏差；21068v1 Indonesian multi-retrieval负侧；21258v1 correlation dimension的幻觉/退化proxy。

当前版本贡献线索与历史v1权限分开；未得到官方原公开公告或完全落窗bounds，不准入当窗，不评分或输出正面Evidence。

## 八必要家族核心

只读决定命题及重要反侧所需原节；全部精确v1原件与实际CORE_FETCH存本目录。没有复现、代码验收、临床/生产安全认证，不算八个候选完成。

- [Reasoning's Razor](./2510.21049v1.html) §3.1/3.3～3.6/Limitations：9安全与6 RAG faithfulness数据，class token logits归一化、ThinkOff空thinking tags，greedy与TPR@固定FPR不同协议。低FPR平均退步不是所有模型/数据集定律；§3.5实际QwQ-CovidQA ThinkOn70.6%优于Off26.6%，等权ensemble79.2%。自报离散confidence也有不同方向；prompt、decoding/context相互作用未尽查，不能宣称reasoning普遍损安全或ensemble无新增成本。
- [Confidence-gated CoT](./2510.21007v1.html) §3.3/4.1～4.3/5.1、AppendixB：Qwen3-8B/32B与GPT-OSS20B、七MCQ/短答任务，10%校准/1%accuracy容差/100 repeats；online随机顺序20warmup/10runs。oracle知道direct正确性不是可部署路由，预算是CoT比例/token proxy，不是服务SLO。两模型族不同默认sampling、7000thinking cap；Qwen8B全曲线不稳定胜随机但局部阈值可节省，不借平均结果保证每请求正确。
- [Input Matters](./2510.21034v1.html) §3.1～3.4/5.3/Limitations：30 NBA games/180 summaries，结构化由原事件解析atomic字段而非仅加JSON括号；按输入形式多次试调prompt，输入处理与prompt混杂，不能全归因serialization。一个作者标全量、第二人只9份/5%，两API模型和NBA限制；不外推全部领域JSON自动安全。
- [VeriGray](./2510.21118v1.html) §3/4.1/4.2/5.2/Limitations：允许external knowledge但假设与D不冲突；两研究生/Bing外源URL/五LLM error detector再human复核；412摘要2044句，只summary。二元评价删NotSure/NoFact不评价这些边界，ranking的标签顺序也是定义。currentv4 Atom明确annotation/evaluation更新，另实读[精确v4](./2510.21118v4.html) §4.2/5.3/Limitations：评价数字与GPT5+RAG、细粒度低recall均属v4，不混进v1；不采用旧6%/9%为跨版本定论。v4 updated12/29是后来提交字段线索，真实修订公开归属待核，不扩本窗或全附录。
- [Social simulations](./2510.21180v1.html) §4 Methods及§3实际偏差/因果说明：8模型4400受控文本对话，循环轮次2～8agents、Llama8B另12～32；human基线是双人crowd Topical/PersonaChat，不等自然多人数群体。default sampling跨模型；role GLM分类100人工核83%，VADER/BERT/LIWC均proxy。PRISM/UltraFeedback阈值关联不识别RLHF因果，不能由reasoning模型较少sentiment推理性普遍因果。组合输出曾截断，Methods单独重读完整，不把截断当已读全部Discussion或附件。
- [Adaptive Indonesian RAG](./2510.21068v1.html) III-A/IV-A～D/V-D4/VI：OPUS-MT无manual postedit，2RTX3090、BM25、Gemma3-4B/Qwen3-8B、740Hotpot/975IndoQA/500QASina。长prompt/multi-retrieval失败例值得保留，但翻译、backbone及长度混杂未隔离，不能证明所有低资源语言multi-hop都退步；单Gemini对照例也不证明参数规模因果。
- [Correlation dimension](./2510.21258v1.html) §4.4/6与C.4：幻觉关联是process-theism名单单case、七模型、temperature1.0代表生成；不能当所有幻觉可靠检测器。需要full logits；pairwise原成本O(N²Ω)，优化/FP32距离与quantization稳定性有协议边界，非闭源API当前可用/免费。只必要C.4，不全附件。
- [DispatchMAS](./2510.21228v1.html) §3.2/3.3/Limitations：five transcript校准、100模拟cases/四physicians/20全共评，auxiliaryagents响应LLM mock；临床helpfulness与contact评分不是实际调度或patient安全。未来才live/trueRAG/比较EMSBERT，current静态taxonomy及premature misclassification/question overload限制。该领域已有组合不准入本项目，但安全反侧不漏读；初次3.2/3.3合并输出截断后分别完整重读，不以下载证明审阅。

## 机构有限停止

OpenAI原Research403后own RSS1245，UTC[10/24 01:00,10/25 01:00)没有feed条目；止单RSS，不能证明全部Research历史无事件。Anthropic原Research publishedOn10/14～10/29夹目标段，实际读取本月3/6/9/14/29字段，单页停止。DeepMind原Research200、web8个LatestNews2026/09～05与六current publication标题；历史切片未恢复。独立Googlepubs正确category=2025&search=language%20model首查18秒超时、web失败；Blog真实October页1十二标题止10/09，目标邻接10/27与10/23，标签只后续归属线索，不证明全球first-public，Blog不代pubs。

Meta首Research18秒超时，仅域内日期主题补检首屏；Qwen旧原页迁移/5旧条目latest09/23，新Research200/94344bytes动态壳、web0行，own main/Research两bundle200实际核research路由及articles拼接/动态GET type=qwen_ai，历史日期列表仍未恢复；止该有限集合，不扩全部chunk或旧站历史。Kimi单页26个带日期入口：25篇文章另加1个11/07“新功能发布记录”汇总入口，文章目标邻接仍11/06～09/16；Moonshot org当前10of42 repo至2026/08，不能代2025历史，不扩普通commits。

DeepSeek own/news/十Research，目标邻接11/01～10/21，日标签不证明所有首公开边界；首页模型导航不代Research。Hunyuan首查壳，本日IAB创建research?page1设置15秒实际超时/kernel reset，正确API POST pageNum1,pageSize200,renderType0共total9/list9；全部publicAt/displayPublishTime 2026，最旧Feb03，止p1，当前历史缺段不是省略API。

Zai own?page2累计18条止12/07，nextPage3/hasMorefalse/没有更多，不拿首屏15末页。Seed两首入口及正确article_type1/2、year2025,count20,order_desc=true,page_token0,x-tt-localeUS；各18/total94及45、next20/has_moretrue；论文目标邻接12/02～10/22、Blog11/27～10/23，页0已越目标停止，置顶不是年度全完，PublishDate不授first-public。ERNIE ownpage2六条末页，11/07～10/16夹目标；没有本窗目录标签不代历史全召回。

MiMo own Paper8日期及Blog15标题全部实读，PaperJan08～Oct21夹目标，More未当历史分页；index与4752两个bundle200，实际新增dated blog最旧Dec18/19及2026段，不补造Oct。英文MiniMax12条止Oct27，中文13条Oct27～Jan15，独立Agent原生md唯一May13,2026；三个入口均处理但历史段限制不互代。

两实际域内日期主题查询是`("2025-10-24" OR "October 24, 2025") (site:openai.com/index OR site:anthropic.com/research OR site:deepmind.google OR site:ai.meta.com) (model OR training OR inference)`与`("2025-10-24" OR "2025年10月24日") (site:qwen.ai OR site:platform.kimi.com OR site:seed.bytedance.com OR site:mimo.xiaomi.com OR site:minimax.io) (模型 OR agent OR training)`。止各首屏，结果多数其他年月不转队列，不证明0事件。没有会议/框架按需触发，未扫Weekly。

全部19论文潜力/历史版本与机构历史缺段隔离，不支持正面Evidence、Books、零事件、无遗漏或安全/性能保证。只有官方原历史公告/公开列表或完全落窗bounds到达，定点重开对应身份/精确版本，不因保存raw扩大全文池。
