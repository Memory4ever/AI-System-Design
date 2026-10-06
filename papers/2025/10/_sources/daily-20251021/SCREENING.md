# 2025-10-21 有限筛选与必要反侧

窗口 BJT [10/20 09:00,10/21 09:00)。只本日材料，未继承他日池。原请求时间、完整 URL、HTTP 与响应见 FETCH.json。四组主题只页0/max80，提交发现带 UTC10/20 00:00～10/21 00:59，不作为首次公开判据。agent/model/multimodal/systems total14/22/12/9，跨源去重55个当前家族题摘已实读。官方CL月目录只作身份恢复：2510.17000～2510.19000前30标题，止2510.17476；supplement.xml中的11份相关完整题摘已读，合计66份。没有把全月目录变成全文队列，没有声明它重建了官方日公开批次。

## 贡献初筛

明确排除：18155消费者营销模拟、2601.05257药品广告、2601.05256水文遥感、17064临床脑科学、18075化工蒸馏、18004通用时空聚类、17529前列腺MRI、17467 ECG应用、17414电池、17382非LLM多智能体路径规划、17250驾驶员身份、17330车牌修复、21791遥感夜光融合。完整题摘未给当前模型/系统主线的新增机制；科学应用不借Evaluation/Data节点绕过暂缓。共13家族，日期未核实但不影响明确排除，非作者按科学/领域应用、非主线通用方法分层抽检。

余53家族继续作为日期/版本与准入潜力保留，不评分，不等53个当窗候选：

- 18179/18032/17995：cooperation选择、交互图反馈、schema过滤合成agent轨迹；须判断具体反馈/失效机制，不借一般Agent闭环评分。
- 17281/17925/17235/2511.07426/17109：服务反馈记忆、索引时预计算、工具动作优化、MCP测量、明确可验证计划条件。加密货币任务的17235不因场景直接排除，但局部工具策略收益尚不外推。
- 18148/18121/17705/17937/17598/17555/17483：attention规则形成、无参数attention解耦、共用/专用轻分支、统一生成理解RL、代码结构蒸馏、语言混杂gate、邻层专家复用。要核原文差额，不由模型名或系统覆盖广度加分。
- 17421/17364/17363/17923/17921/17196：数据分布条件扩散、流式视频状态、跨任务视觉表示、self-answer奖励、创意/幻觉干预、CLS/残差稀疏attention。小模型/表示理论和局部负面结果保留。
- 21802/18135/17699/17482/17383/17171/17137/17131/17105：双采样器信息交换、视觉世界模型闭环评价、采样细节、稀疏query状态、latent层干预、频率分解、关节几何表征、OOD引导、低光conditioning。具体视频/视觉任务可能承载通用机制，不按应用词自动关闭。
- 18897/17505/2511.07427/2511.04684/17189/17158/2511.07425：LLM生成调度、稀疏einsum下沉、动态KV压缩、bit-exact熵编码、低比特非线性、kernel训练反馈、端侧容量评价；通用kernel/硬件研究不因非大模型专名排除。11月ID不按10月提交字段移进本窗。
- 补检17001/17028/17115/17139/17238/17354：词表裁剪、prompt校准、数据生成模块、compute-aware检索改写、流式thinking、混合模态检索。其余安全/反侧补检见下面。

## 必要核心实读

下列16份精确v1均只读命题所需核心，不计16个标准/深入候选完成。未复现、未核代码、未授正面Evidence；当前v2/v3/v4/v7不覆盖历史v1。

- [BadScientist](./2510.18003v1.html) §4.1/4.2及Limitations：GPT-5写稿，o3/o4-mini/GPT4.1评分，以200份ICLR记录校准阈值；GPT-5标记诚信关切。acceptance是评分阈值，不是实际录用；无代码运行、无人类复核是受控条件。关切与高分不一致的评价潜力保留，不宣称已证实现实会议被攻破。
- [KV corruption](./2510.17098v1.html) §3.2/§6/§9：能写缓存key的partial-white-box假设；GPT2-medium、Llama2/Gemma7B，选定长度/层/噪声、三seed，T4或A100。不能推出普通提示可越权修改缓存或跨租户攻击已实现。
- [SearchRL](./2510.17431v1.html) §3.1～3.3、§4.2、§5：3B/7B、PPO、QA exact-match奖励、local/wiki与SerpAPI top3，299有害单句、Prometheus评价/50人类核样本；拒绝与unsafe query可并存。v1只提出表示方向/安全gate作为未来方向，不能照当前v2摘要写成v1已实证mitigation；未分离预训练与retrieval的危害来源。
- [Unlearning](./2510.17210v1.html) §3.3/4.1/4.4：retain attention增强和adapter；ToFU比噪声TDEC更适合重要token估计。作者明确behavior suppression而非representation erasure，可被探测/重新微调恢复，不写删除保证。
- [Video bias](./2510.17247v1.html) §3.3与Limitations，另§7.2定点：16帧、三VLM多数/ensemble，42动作；US类别、单步latent-consistency协议、合成性别偏好。ensemble不能证明无judge bias，也非所有偏好优化必同样放大偏差；未遍历§7.2全部表。
- [Iterative jailbreak defense](./2510.17006v1.html) §3.1模型/设置/评价段、Limitations、AppendixB：在线rewrite更新的拒绝判断使用208短语，8H100受控测试；未知攻击不保证，实时成本仍是限制。附录作者few-ms/低5%声明仅适用于该配置，未作普遍SLO保证，未遍历所有基准数字。
- [SafeSearch](./2510.17017v1.html) §3.4/Limitations：在query closing token放安全reward，later-query折扣/K限制，依赖LLM judge；3B/7B及多超参数未尽查，最终答案安全不代表过程安全，也不把reward当hard授权边界。
- [Atomic instruction](./2510.17388v1.html) §3.1/3.2/3.4与Limitations：MCQ exact-symbol协议、4bit全部、70B仅5%样本。不得把标签格式失败泛化为所有指令/模型或不受量化混杂的能力上限。
- [Alignment calibration](./2510.17426v1.html) §3与Limitations：PT/IT权重插值、ECE与accuracy不同轴，SLERP/linear/DARE-TIES；必须开放权重，未穷尽复杂合并参数，不普遍保证API模型可恢复校准。
- [Social thinking](./2510.17062v1.html) §3.1/4.2/4.3与Limitations：BBQ含ambiguous/unambiguous避免总答Unknown虚高，StereoSet被改写；长度相关弱，transition token并非因果证明。英语文化与300例中等人类一致性限制，不能由文字thought证明真实内部心理。
- [SpecAgent](./2510.17925v1.html) §5.1/8：删定义仍留caller/tests可能未来信息泄漏；作者无法启动HumanEvo后用合成REPOCOD状态，非真实历史。索引时计算和更新成本不是免费，原benchmark高pass不作现实收益。
- [Query augmentation](./2510.17139v1.html) §4.1/4.2/Limitations：BM25/E5/Contriever、Hit@20与NDCG协议、3B/7B PPO对GPT4o-mini及其他SPQE；未以相同backbone简单推成RL总劣，control dense retriever与预算差额仍有潜力。
- [MemoryBench](./2510.17281v1.html) §2.4/3.2/6：反馈由Qwen32B与可编程动作映射模拟，只train生成feedback；on-policy只报告一天内能跑完方法。不是实际用户满意度或所有memory方法完整公平排序。
- [MiMo routing](./2510.11370v1.html) §4.1/4.2/5.1：replay离散mask但以train logits重算gate保梯度；prefix KV旁存mask，不是简单冻结router。Qwen3-30B-A3B、Megatron/SGLang、最佳checkpoint单run评价，不授任意MoE永不collapse。官方MiMo10/21标签对应家族v2，而v1submitted10/13；v2submitted10/21 17:19:46Z在本窗后，均不以submitted当首公开。搜索仅按官方标题首屏恢复身份，不扩会议扫描。误请求 `/html/11370` 的404原件保留，不当成功材料。
- [World-in-World](./2510.18135v1.html) §2.1/4：proposal/simulation/revision与真实新观察闭环；web priors可忽略动作、panorama增益不一致、接触物理与策略floor限制。图像合理不等预测对行动有用，MPC常识本身不当新贡献。
- [Two to Tango](./2510.21802v1.html) §5.2/6.3/8：33人25对同seed图像评价，增并行processor反而劣化的局部负面结果；不是普遍固定总compute下无代价优势。

## 本日机构查询与恢复

三次域内辅助日期查询实际为 `(October 20, 2025 OR 2025-10-20)` 与 OpenAI/Anthropic/DeepMind/Meta 的model/training/inference；`(2025-10-20 OR 2025年10月20日)` 与Qwen/DeepSeek/Kimi/Zai/Hunyuan的模型/agent；同日Seed/ERNIE/MiMo/MiniMax/Agent的model/训练/推理。均首屏停止，搜索不命中不证明无事件。

Seed own原页两入口独立请求，错误type响应不可用；正确article_type1/2、publish_year2025,count20,order_desc=true,page_token0、x-tt-localeUS。论文18/total94,next20,has_moretrue，相邻BJT10/22 Seed3D→10/21量子嵌入→10/09memory，量子嵌入明确AIforScience关闭；Blog18/total45相邻10/23→09/09，页0跨窗停止，置顶不代表有序年度全完。Zai实际?page2累计18/hasMorefalse最早12/07，历史缺段仍隔离。DeepSeeknews十条Research相邻10/21 OCR与05/14；OCR完整题摘实读，arXiv v1 submitted10/21 02:41:44Z已经本窗后，但这不是其首公开时刻，官方标签亦不够准入。Google Blog真实October页1十二条相邻10/20相册与10/17；相册core的DP来自contribution bounding+DP训练，不是caption压缩天然隐私；日标签只相交，pubs独立未恢复。MiMo自身index/4752 bundle有限身份恢复无论文href，后来官方标题搜索恢复上述原件；More未当分页。

所有上述日期/版本/历史缺口不用于正面证据、Books、零事件、无遗漏或性能/安全保证；恢复需要原官方历史公开公告/完全落窗bounds，之后只核相应事件精确版。

## 07:00 三源窄恢复与独立复核同步

fresh本日适用合同/ROADMAP/最新路由后，只处理root指定三源，不重读66池。实际请求URL、执行UTC时间/HTTP与失败见THREE_SOURCE_RECOVERY.json，旧FETCH保留历史且其Google year/query不是有效过滤。正确`https://research.google/pubs/?category=2025&search=language%20model`于22:52:01Z结束18秒超时，0响应正文；保存headers，网页打开也InternalError，止此次有限请求，不当无事件。

OpenAI首Research403后实际`https://openai.com/news/rss.xml`200，原响应openai_rss_recovery.raw共1245条。XML解析所有feed日期，仅UTC[2025-10-20 01:00,2025-10-21 01:00)保留Atlas一条，pubDate=`Tue, 21 Oct 2025 00:00:00 GMT`；下一相邻WhatsApp17:00Z在截点后。止单feed，不生成1245全文队列。feed时间不自动证明全球first-public或秒级精度；原文章仅October21日名，两者权限分开。

已实读[Atlas官方公告](https://openai.com/index/introducing-chatgpt-atlas/)的More capability, more control及Get work done for you全部核心：站点可见性关闭不建新记忆，删除历史连带记忆；登录网站的Agent有浏览器代码/下载/扩展及本地文件限制，敏感站点观看暂停、logged-out模式。原文同时承认隐藏网页/邮件指令可导致未授权行动或泄露，red-team不保证阻断所有攻击。实际新增潜力是浏览持久上下文删除与已登录执行的具体约束，不借通用权限原则评分，也不认证实现或安全效果。当前后来deprecated提示不是2025发布时的机制。curl原页403，成功web工具原响应保存atlas_web_original.json；不把curl失败当读完，也不扩linked system card全部附件。首公开/历史版继续隔离，候选/Books0；请求root对该新增有限命题/日期权限窄核。

Qwen实际`https://qwen.ai/research`200/94344字节，HTMLParser仅Qwen；web0行。IAB首次visible选项在subagent不支持，绑定无tab，再实际创建单次15秒超时/kernel reset，止此browser。own main.js实际有research路由；依引用下载p_research-index.js，实读listData由旧D过滤与`$.data.articles`转换拼接、GET参数type=qwen_ai/language=en-US。共享5fb222f6.js/9e22d361.js200未恢复请求常量；实际4467.js404。不由猜测请求URL构造成功，也不遍历全部chunk。原件及headers均保存qwen_recovery_*，停main/Research/两共享bundle与一404的有限集合。迁移入口已执行但历史日期目录仍受阻，不用壳200或旧09/23证明零事件。

root FIRST与FINAL实际文件已读：六精确v1潜力及4/13排除样本、16必要core和原来源有限段已非作者实读。未变结论复用，不授本日完成。当前仅三源/Atlas新增及作者变化待root窄回核。
