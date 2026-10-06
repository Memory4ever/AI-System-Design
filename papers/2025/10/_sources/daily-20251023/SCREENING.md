# 2025-10-23 有限筛选与必要反侧

作者 Cicero；本日窗口 BJT10/22 09:00～10/23 09:00。实际请求时间、URL、提交发现带及页0/max80见FETCH.json；恢复见RECOVERY_FETCH.json、EXTRA_FETCH.json。仅本日，未继承其他日池。32→35是本日前15标题中三含糊项补题摘，不是候选改判。

## 范围与停止

四主题为MoE/长上下文/预训练/语言模型蒸馏；LLM memory/RAG/tool-use/prompt-injection；World Model/VLA/生成AR；LLM训练推理/KV系统，各API只有页0，total9/2/6/4，21唯一当前完整题摘。submittedDate UTC10/22 00:00～10/23 00:59只恢复线索。CL月目录身份带2510.19000～21500前15标题，止19208；13相关或含糊完整题摘，另Seed3D完整题摘，35唯一家族。标题明确范围外19036生物医学术语归一、19144藏语资源综述不建全文队列。其他月目录标题未逐项筛选。

API当前版本/题摘全部实际读，当前v2/v3/v4不冒充v1：supplement.raw是Atom原响应，非HTML；arxiv_supp2.raw三份追加原响应。日期尚无官方首公开完全落窗依据，不用API submission或DataCite注册补造。重要修订仅版本号不确证，未遍历全史。

## 贡献处置

完整题摘关闭4家族：19986 Iconclass为木刻领域分类使用LLM/RAG，未给新检索机制；19364 ProTerrain为相关地形参数不确定性/物理预测，非foundation-learning/world状态学习链；19577 gem5 co-pilot为领域DSE数据库/DSL/搜索，未建立新的LLM执行可靠性或AI计算设计证据；19030 Re:Member是三帧采样+WhisperX对齐+情绪语音模块的L2学习互动probe，未新增memory representation或适应机制。日期未核实但这些具体关闭理由不依赖日期。

其余31家族全部潜力/日期版本隔离，不是确定候选，不评分：19897实例批评/语义记忆与suggestibility；20860语音预训练数据处理/合成/交错消融；19779 selective KD与接受率；19488视频逆动力学GUI监督；19875稀疏attention tracing；19366细粒度expert/k-aware服务；19363短RL长上下文泛化；19338hybrid比例与训练推理operator；19290ensemble分布蒸馏不确定性；19266attention bridge跨架构迁移；19818未来语义world模型；19752VLA失败经验条件affordance；19654state/action协作规划及并行token；19430world合成VLA数据与RGBD/CoT；19195合成数据训练预算反证；19873图搜索迁移CUDA优化；19296signal级正确片段DPO；19225token级抢占迁移；19005动态过拒；19028社交推理/CoT负面；19116参数/上下文知识冲突与steering；19117谱幻觉诊断；19131跨语言voice谱与head干预；19171结构RAG/终止；19172时变事实；19181KG检索小paraphraser替代；19186工具对话错误评价；19208分布式能力自路由；19944simulation-ready资产；19032judge绝对/一致评分分离；19167人格问卷的同意偏差。不以小模型、局部结果、负面或已有主题将其关闭。

## 十二精确v1必要核心

原件下载成功不作已读证明。以下实际读指定方法、评价或关键反侧，支持范围足够即停；不是十二家族标准/深入审阅完成、没有正面Evidence授权。

| 原件 | 实际位置与边界 |
| --- | --- |
| [OverBench](2510.19005v1.html) | §2、3.1～3.3、4.1～4.4、Limitations及AppA原HTML841～879：proxy只过滤，OSR用目标模型；Hard30k由至少五模型拒绝选择，不是普通请求部署率。500人工样本核拒绝标签94%precision/91%recall，不等所有450k语义良性已逐项证明；未评价true-positive拒绝，不授放松安全。 |
| [Social reasoning](2510.19028v1.html) | §3.2/3.3、4.2、5：v1为1147场景（580/567），三标注无重叠13.2%排除；movie动态关系并非唯一全球标签。Thinking单run；o3/GPT4o跨模型比较混杂；CoT文字不是内部心理证据。当前v3摘要约1.1k不替代v1细节。 |
| [Deprecated](2510.19116v1.html) | §3、4.2/4.3、5.1、6、7：PK/CK是来源非真值；Python人为函数/操作符替换，测试转换才给正确性。Llama1/3/8B；跨域多数层接近50%，80.65%是层峰。steering成功0.126不等12.6pp通用正确率或所有冲突可修。 |
| [Spectral detector](2510.19117v1.html) | §4、5.5/5.6、7：连接/度与中心化假设下的扰动readout界不证明事实真实性；三GPT架构各三基线run，80test=50事实30幻觉，按语义域调阈值。语义幻觉主指标可落事实方差内，88.75%不授普遍检出。 |
| [TSSS](2510.19171v1.html) | §2.1/2.2、3.1/3.2：cosine>=0.85重复终止不是证据充分证明；主问题/历史queries比对。Llama3.1-8B、e5-base、21M Wikipedia、top3、上限10、单H100。比StandardRAG约2～3倍慢；只比迭代RAG-CoT更快，不授所有负载加速或任意context可缓存。 |
| [evolveQA](2510.19172v1.html) | §2、3.1/3.2、4.1、Limitations、B.5：AWS/Azure/WHO、12模型六cutoff；当前知识与过时/错误分别判。100人工sample四作者但每点一人，整体问题质量80%、gold91.57%、judge95.9%；不能用judge准确率证明数据全部正确。无完整演化事实真值无法量召回，静态对照知识召回也不确定。 |
| [TRACE/SCOPE](2510.19186v1.html) | §2.2、3.1/3.2、4.1/4.2、Limitations：v1确有SCOPE，当前v3摘要不能抹掉该版本。516=141human gold+375silver，tool执行由LLM模拟；5fold、40/60、两judge，同user满意掩盖tool错误。hardNEG准确率0.33/0.48仍大量漏检，不授真实API错误完备检出。 |
| [Dream4Drive](2510.19195v1.html) | §3.2、5.1～5.4：nuScenes700train/150val/150test；旧合成方法双epoch收益在等epoch时大减。本法420assets、256×512与512×768、1/2/3epoch分开；naive插入对照显示多数收益和render附加收益不能混并。远/左/同数据源asset效果有域偏差，不宣称合成普遍无用或普遍更好。 |
| [RLBoost](2510.19225v1.html) | §2、4.2/4.3、6.1/6.5、7：§2将critic与reference/reward合称frozen的概述不能推广，是对训练PPO critic的不准确描述；PPO critic须更新，不能推出所有RL辅助模型冻结。本论文实验为同步GRPO、无critic，故其同步/迁移结论限该配置。token prefix迁移仍prefill，无需重生成不等无状态损失/bitwise等同。同步同step权重；H1008GPU训练+2GPUrollout，Qwen3 8/14/32B，batch128×group8，14K；真实spot三段2小时trace在on-demand回放，非实时spot全分布。reward曲线近似非相等；WAN/异构/异步扩展属讨论，不授已验证。继续first-public隔离，不作正面采用。 |
| [ReGraphT](2510.19873v1.html) | §3.1/3.2、5.1开头、AppD/F：图offline由LLM轨迹与验证构建，部署SLM不等全pipeline不上传私有代码；MCGS每步编译/功能测试/benchmark，测试通过不等任意输入证明。budget200比较；AppD测试A10080GB/Qwen7B/budget100/batch16，313样本6.02h，4090 7.53h为外部估算不是本次实跑。筛选可漏复杂edgecase。 |
| [MentalAlign](2510.19032v1.html) | §4.3、5.1～5.3、Limitations：三临床专家1000conversation仅reference非绝对真值；先聚合conversation成model均值，九model bootstrap1000，ICC(C,1)/ICC(A,1)分排序与尺度；不能外推逐样本安全可靠。单轮英语、部分生成数据、selffamily排除不等全部偏差消除。不因应用是心理健康排其judge设计反侧。 |
| [Hiring](2510.19167v1.html) | §3.1 Data Collection、4.1、Limitations：实际一份人格问卷1～9同意尺度，12模型/2志愿者，无标准解只reference；单调用未控制温度方差。原HTML数学元素的mn与TeX annotation均显示同一个2，不能把HTMLParser双显示拼成22；此前22为提取后误读，已纠正。差异/RMSE/Pearson与同意偏差仍可留潜力，此人数纠正不改变潜力判断或first-public日期隔离；不支持“不能胜任工程师”或所有招聘测试失败。 |

## 官方核心与检索

Google Blog真实October页1实际网页读取，12条标题，目标相邻Oct23 EarthAI、Oct22 quantum，止页1。EarthAI核心Building blocks/Increased predictive power/Geospatial reasoning实读；新增遥感/人口模型、风险embedding融合和专用工具编排以地学/科学领域任务为对象，未证明新的通用Agent执行机制；按当前AI for Science边界关闭，不扩论文/全部附件。Quantum计算优势非LLM训练推理机制。Blog原curl超时不作成功原件，pubs独立查询curl超时/web不可达未替代。

OpenAI本日RSS1245按本窗实际解析三条：UK sovereign AI pubDate10/22 16:00Z、South Korea Blueprint10/23 00:00Z、Company Knowledge10/23 00:00Z。前两官方core是部署合作/政策建议/数据驻留区域，不是实现研究；不授首次全网公开。Company Knowledge原页首读timeout，尾斜杠路径恢复How/Privacy/Limitations：多source训练GPT5版本但未披露训练机制/对照；ACL沿用、citation与manualmode限制只产品功能，未据此创造成熟原则贡献或安全保证，贡献关闭。午夜RSS时刻不擅自升级原页面日名精度。

两组官方域日期补检，各首屏停止：`("2025-10-22" OR "October 22, 2025") (site:openai.com/index OR site:anthropic.com/research OR site:deepmind.google OR site:ai.meta.com) (model OR training OR inference)`；`("2025-10-22" OR "2025年10月22日") (site:qwen.ai OR site:platform.kimi.com OR site:seed.bytedance.com OR site:mimo.xiaomi.com OR site:minimax.io) (模型 OR agent OR training)`。主要错年/后续TPU合作/政策线索，不作逐篇队列。

Qwen原旧主页后实际迁移qwen.ai/blog200但只有Qwen壳，web0正文。自身p_home-index、main、1721、p_blog-index、9e22d361以及实际依赖4467有限恢复，最后4467 404；未恢复历史articles列表，停止这次有限恢复，不能称无事件。原件均本日真实下载。Hunyuan browser本日getTab research?page=1 15s超时，正确API total9最早2026/02/03。Seed自己响应type1/2各18、total94/45、has_more=true、token20；目标邻接10/22/21/09与10/23/09，止页0；未拿置顶旧项冒充新事件。Zai实际页2累计18、hasMorefalse/next3止页2；最早12/07，历史缺段。

DeepSeek/news十research目标10/21～05/14；Kimi25当前条目11/07～09/16目标邻接；ERNIE页2六条末页11/07～10/16。MiMo八Paper实读06/29(2026)至05/12(2025)，目标10/21～09/19；15Blog/More非历史分页。MiniMaxEN12/CN13当前单页，目标10/27～01/15，Agent独立md只2026/05/13。Anthropic本日内嵌publishedOn10/14与10/29；DeepMind原Research当前非10月历史列表；Meta、Moonshot组织失败不当无事件。没有周级扫描或无关发布触发。

## 作者停点

07:35本日fresh窄恢复：正确Google `https://research.google/pubs/?category=2025&search=language%20model`真实18秒超时exit28/0字节、web失败，旧year/query不作有效过滤。Qwen `https://qwen.ai/research`真实200/94344字节、web0行，HTML实际matchedIds layout/home、CSR，无历史列表；own本日已有main指向p_research-index.js，实际新下载该route200/16887字节，核X=44467、cy GET和type=qwen_ai/language=en-US、$.data.articles合并路径。止两入口及该必要资源，未全量chunks/猜API，未跨日复用响应；本日RSS已有效处理而未重抓。原请求为TARGETED_SOURCE_RECOVERY.json、web原响应TARGETED_SOURCE_WEB_ORIGINAL.json及qwen_research_route.js/header。

root FIRST六精确v1与3/4 arXiv排除已实际通过潜力/版本校准。MoE-Prism 19366v1应为offline neuron partition+online QoS，前文current v2细粒度/k-aware仅早期当前题摘线索，不是历史v1贡献。四arXiv关闭分母含Re:Member，不含另行机构公告Google EarthAI；第四未由root重读，不能称4/4独立验证。root FINAL已实际读完十二必要反侧、三官方公告、Google EarthAI核心与有限来源；作者五处窄修已保存（正确Google参数、Qwen /research、MoE-Prism v1、Hiring2、RLBoost critic边界），仅待root变化回核，尚未获得DAY通过。人数/概述纠正不解除任何日期隔离，也不授正式候选、正面采用或Books。

本日作者可执行研究已处理到必要有限停点；无确证候选/评分、候选证据完成、Books提案/写入均0。31潜力家族精确首公开及部分历史v1仍缺，只有可验证官方历史公告/完整bounds取得才定点重开并评分，独立证据通过后读owner/邻接比较。没有以Books主题相似声称已有覆盖。FIRST已到、DAY尚未到，作者不填日级通过；所有隔离项不用于正面Evidence、Books、无遗漏断言。
