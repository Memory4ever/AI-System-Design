# 11/29 首批与有限来源校准

作者root；实际检查至2026-10-04T19:13:52+08:00。启动与恢复重读当日适用合同、Sources频率、Prompt、ROADMAP和STOP；未载旧Weekly或别日候选。窗口UTC `[2025-11-28T01:00:00Z,2025-11-29T01:00:00Z)`。

## 原入口与停止范围

`fetch.mjs`与`follow.mjs`只收原响应，逐份`*.receipt.json`保留URL、开始/结束、HTTP/失败和字节数，不把200当正文/历史成功。28份exact-v1摘要页全部200并实际逐份读完整题摘；没有读其全部方法或运行代码。

1. OpenAI RSS1245项结构解析，按pubDate本窗0；Research历史全文不是本RSS的保证。
2. Anthropic Research原HTML Flight解码`publicationList.posts`171项；目标邻接Dec1 00:00Z→Nov25 11:05Z，下接Nov24 15:10Z、Nov21 14:32Z，未见本窗字段。实际数组不是搜索首页。CMS `_updatedAt`不是研究公开时刻。
3. DeepMind canonical page4原目录有目标月份标题；实际读其当前可见标题。AlphaFold五年回顾原网页Nov25，image verification原网页Nov20，科学应用标题不送全稿。Google Research pubs/year与Blog year的两次native必要请求均失败/超时，web两个同入口不可访问；它们独立列受阻，不由DeepMind替代。辅助四域日期搜索返回当前2026目录和窗外旧文，不能证明本窗没有事件。
4. Meta native Research失败；web Research0行，定点日期搜索回当前Blog和2023/2025Apr旧文，不授历史覆盖。
5. Qwen Research仅4字壳；旧Blog当前5卡最新Sep23且明确迁移qwen.ai，不能用旧Blog证明11月无事件。日期搜索未恢复新站历史段。
6. DeepSeek原更新列表Dec1后接Sep29，无本窗API事件字段；非作者另实际补取[官网主页](independent-deepseek-home.html)和[更多Research原索引](independent-deepseek-research.html)，10项研究目标邻接Dec2→Nov27 Math-V2→Nov1→Oct21。root实际回读同一原件；Math-V2由本日窄题查询发现、完整v1题摘已读，不增加身份。Research自然日期未提供时区/正文首次公开时刻，保留论文公开时间缺口；API变更列表不替Research。
7. Kimi Blog可见完整目标邻接Nov7/6后接Sep16，无本窗目录项。
8. Hunyuan native shell+publicList(renderType0)9条均2026；本日真实浏览器打开Research后读取“全部”列表11条，首Sep22末Feb3 2026、没有可见历史分页控件。中文11与英文API9不是同一个分母。只证明本次所见，没有2025切片；未把浏览器空初始AX当失败后直接停止。浏览器已关闭。
9. Z.ai p1/p2 Flight原数据当前累计18，p2 nextPage3/hasMorefalse；最早Dec7 2025。真实停点p2，不拿CMS createdAt回填论文日期。
10. Seed按year2025/type1论文及type2Blog各p0/p20：实际18+20、18+18共74目录项，total94/45、next20/40、has_moretrue。置顶与普通倒序分开，已跨本窗到Oct/Jun；停历史邻接，不声称读完全年。论文p0 Dec2→Oct22，Blog p0 Dec2→Nov27→Oct23，无Nov28字段；PublishDate是目录字段，不自动为首次正文。
11. ERNIE两页真实2/2，Nov21→Nov11跨目标，无本窗条目；版本名1120不作日期。
12. MiMo原8 Paper及15 Blog可见标题，Paper最新当前2026后接Oct21 2025，Blog没有目标历史日期链。More折叠不当已恢复2025记录，缺口隔离。
13. MiniMax EN/CN当前目录Dec23→Oct27；Agent Tech原Markdown全文实际读（唯一2026May13）及真实llms索引取得，每日入口已查，不写未触发。保留2025历史缺段。
14. arXiv四主题原Atom限定SubmittedNov27–28作发现：learning108、runtime46、agent63、multimodal58；三种尾页从50补至各total，runtime46/46无需尾页。合计275条响应/204唯一当前身份，不是204篇本日公开或已题摘审阅。首轮范围偏宽，宽表仅原始查漏，不变整类逐项关闭队列；实际选择下面50个主线或含糊相关方向完整题摘，其中28用exact-v1、22仅当前Atom（仍保留版本）。其余宽命中只可作标题线索，未授全题摘完成。

arXiv2025帮助同commit `95c71658adbaa987dc2ba1105ef9c5201ecde4ce`本日raw请求失败；复用[已独立核身份的原快照](../daily-20251109/arxiv-2025-availability-api.md)仅稳定公告规则，不复用09候选/判断。实际重新读原文：Sun–Thu20ET、Fri/Sat无常规公告，Nov27 Thanksgiving停发；zoneinfo换算本窗为ThuNov27 20EST→FriNov28 20EST，左端假日/右端周五。规则只限定常规批次，不能证明某篇首次公开、其他渠道或例外不存在。原Atom submittedDate不改名public，后编号月份/当前晚版也不回填。

## 实际完整题摘与潜在增量

下列47个方向仅需确认首次公开身份/完全落窗上下界；没有确定当窗候选、评分、正面Evidence或Books采用。并非因缺实验、无owner、模型小或理论研究而排除。

28份exact-v1全部实际读：

| 精确v1身份（本目录abs-IDv1.html） | 原有压力 → 原文潜在增量 → 待改变选择 |
| --- | --- |
| 2511.22333 | 共前缀重复读KV → query pack/多tile/online merge → Attention访存调度；v1数字不抄当前v3 |
| 2511.22481 | MoE/cache/PD各自优化 → OmniInfer联合状态协调 → 系统瓶颈归因，不能直接采用616QPM |
| 2511.22570 | 答案对不等证明对 → verifier与generator共同改进 → 奖励证据与验证compute分配 |
| 2511.22677 | DMD收益归因含糊 → CA/DM分解 → 蒸馏驱动与稳定约束职责 |
| 2511.22697 | 全参数/统一LoRA忽视任务因素 → 定点head微调 → VLA适配范围 |
| 2511.22788 | 统一隐私扰动牺牲utility → entity-sensitive路由/semantic sketch → cloud-edge权限与成本 |
| 2511.22880 | 不同adapter rank共batch偏斜 → 动态placement/RDMA → 多LoRA容量/SLO，不先采用倍数 |
| 2511.22889 | 权重搬运memory wall → 固化权重电路/动态KV外置 → 可编程性与模型更新约束；仅架构提议 |
| 2511.22891 | 长CoT冗余 → 紧凑表示/长度偏好 → reasoning长度与质量；不是人类思维证明 |
| 2511.22904 | 语言只指任务不指动力学 → language-grounded Dreamer → policy泛化与无planning条件 |
| 2511.22924 | 单审计节点/高成本 → 分层分布式审计 → trust/效率；v1摘要名AgentShield，不回填当前MAS-Shield |
| 2511.22972 | exact分布保真限制接受 → semantic deferred verification → 延迟/质量与失去exact保证；保留反侧 |
| 2511.23034 | 视觉重建忽视物理 → 运动/场景latent+action监督 → action表示可迁移性 |
| 2511.23070 | missing modality/深层信息丢失 → feature buffer replay → 表示恢复代价 |
| 2511.23092 | 自评回馈奖励可被操纵 → reward-channel control反证 → self-eval与学习权限分离；safe普遍断言未采用 |
| 2511.23113 | 稀疏head/block负载不均 → dual-balance动态SP → 固定等切分的失效条件 |
| 2511.23225 | FP8 outlier → colinearity/loss约束 → 训练目标与Numeric Plan，不采用普遍数据无关 |
| 2511.23239 | 同loss不能解释学习 → 一层random-walk理论及小初始化反侧 → 理论假设与优化结果 |
| 2511.23262 | test任务新 → 双记忆/元推理与test RL → 在线适配/污染边界 |
| 2511.23281 | interface比较混杂 → 同e-shop四接口 → HTML/MCP/RAG成本协议，不能宣布MCP普遍更优 |
| 2511.23310 | RL baseline/lr启发式 → gradient-weight/SNR原则 → 方差控制；只v1，不借v4 KL定理 |
| 2511.23319 | 长度大不等随机访问 → HSA → sparsity/length generalization，不把retrieval当全任务智能 |
| 2511.23347 | 分布记忆/延迟 → interest matrix+树通信OCO → regret/网络假设 |
| 2511.23404 | 边端受硬件约束 → hardware-in-loop混合结构+distill → 架构与部署共同选择 |
| 2511.23436 | 自生成伪偏好 → frozen verifier/learner/replay → 持续学习风险；不接受minimal reliable universal |
| 2511.23465 | world model长rollout评价混杂 → isolated dynamics → 一步好与长期误差区分 |
| 2511.23476 | rigid多轮推理 → action efficacy reward/turn anneal → 内化动力学与任务反馈 |
| 2512.00207 | facts存储/可用性不能等同 → MLP构造容量/Transformer usability trade-off → 参数知识解释；编号12不倒填11 |

另19个当前Atom完整题摘实际读取，精确身份/版本保持原XML，不标v1审阅：PerfMamba2511.22849v1、Risk-EntropicFM2512.03078v1、INN2511.22813v1、VeriDispatcher2511.22749v1、ReversingLLM2512.02056v2、FlowMaps2511.22688v1、HarmoCLIP2511.22594v1、CoT4AD2511.22532v1、DocVAL2511.22521v3、GEO-Detective2511.22441v1、SuRe2511.22367v1、AutoTailor2511.22355v1、MCVQA2511.22341v3、EdgeDeployment2511.22334v2、SingleQuant2511.22316v2、Q-KVComm2512.17914v1、TokenMarginalization2511.22312v1、SHAPFaithfulness2512.00163v1、BPMN2511.22448v1。增量分别是SSM pruning边界、FM尾部目标、graph routing训练、预算路由、activation可逆、reward末端flow map、global-local对齐、动作CoT、validator监督、隐私攻击反侧、replay/双LoRA、SuperNet自动转换、格式混杂、跨硬件带宽归一、量化优化非光滑、跨模型KV表示、生成分类置信度、self-explanation/SHAP背离、OCR增益条件。后两者只保留潜力，不因金融/应用名自动否认诊断或ablation。日期与准确历史版均未授，必要时首先恢复精确稿而非扩全部实验。

## 三项完整题摘关闭与其他标题边界

当前Atom v1 DIPT2511.22739：病理中心domain-specific prompt averaging/distillation改善领域F1，题摘没有新增foundation机制失效边界或可辨别通用选择，关闭此材料范围，不关闭所有医疗/小模型研究。

MediGRAF2602.00009v1：10病人graph/vector/Text2Cypher组合取得领域QA指标，未给组合之外的机制/条件贡献；100%召回、0安全违规不当一般安全保证，关闭范围增量。后编号月份不为不影响处置另建日期请求。

AI-Meteorologist2511.23387v1：分层天气输入/keyword验证主要针对天气叙事，题摘未披露新的Agent可靠性或评价控制条件，AI for Science应用暂缓；关闭不是因为Agent数量或旧模块本身。若非作者发现具体一般机制则定点重开。

明确标题暂缓/范围外样本：protein agents2511.22311、perovskite2511.22307、tumor2511.22292、quantum-dot2511.22451、antimicrobial2511.23120；只核题意，不假称读全部摘要/方法。宽表其余条目不是已关闭研究分母。

## 日期恢复与权限

作者执行四个定点日期搜索：DeepSeekMath Nov28、LFM2report Nov28、LoRAServe November、Hunyuan Nov28；只得到二级转载/LinkedIn/arXiv镜像摘要与2026混元PDF等，未保存可绑定这四项请求的独立原响应，撤掉错误的web-search1.json引用（该文件实际只有OpenAI社区搜索）。非作者又实际执行四请求，原参数/返回见[independent-date-search.json](independent-date-search.json)，身份和权限见[FIRST_INDEPENDENT_REVIEW](FIRST_INDEPENDENT_REVIEW.md)。两次执行不能混为同一次receipt；现有结果没有精确原首次公开权限，没有用索引November28当本窗公告，也不以搜索空结果授无遗漏。

需要非作者首批校准：全部拟采用0；上述47潜力保留与3负侧、重要数学/安全/版本反侧边界；14入口及停止范围。准入/日期/来源与六部分未审完是普通工作，不能作者自授完成。Books预期No Change仅因无可采用当窗证据，不作全owner已有覆盖断言。root后续生成正式六部分后交Aristotle最终DAY。
