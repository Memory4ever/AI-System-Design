# 2025-09-30 实际有限发现与筛选

作者 Archimedes；窗口09/29 09:00至09/30 09:00北京时间。依当前研究合同§2–5，不把提交字段、月库存或宽搜索称为本日首次公开/全文队列。实际请求时间与原响应分别保存，不覆盖失败记录。

## arXiv 发现范围、停点与身份

`fetch-log.json` / `arxiv-query.atom` 为首100；`arxiv-pagination.json` / `arxiv-page100.atom` / `arxiv-page200.atom` 为后100+78。原查询为12分类与十个标题主题复合，submittedDate `[202509261800 TO 202509291800]`，descending，start0/100/200，max100；实际返回278/278，`arxiv-all-discovery.json`保留题、完整摘要、原published/updated和当前版本。该三天提交前缘用于周末公告恢复，不是授权三天报告窗口。末尾版本号去重，不采用早期打印时split('v')截断arxiv域名的错误计数。

官方`/list/cs.CL/2025-09`前2000仅标题查漏；尾2001–2214实际恢复并浏览相关标题，`30-finite-recovery.json`保留请求。月份并非逐篇题摘/关闭队列。日路径实际400，官方availability的常规公告窗口不能排除moderation延迟。月尾仅挑13个遗漏的相关新命名标题作一次id_list请求（`arxiv-tail13-fetch.json`、`.atom`、`.json`）：HTTP200、13/13，完整题摘均实际读，至此停止，不扩月库存。

278+13按论文身份去重实际291；44明确关闭、247保留潜力与日期隔离。后者不是247个当窗候选，更不是证据审阅完成。API返回v2/v3/v4等当前摘要不冒称v1；2510/2511编号与9月submitted字段不一致时保留原值，不用提交倒填first-public。相关/含糊摘要实际读；明确领域应用题名可按范围关闭。下表中的摘要关闭均实际读完整题摘。

## 44项关闭（原278数组零基位置）

| 位置 / 身份（保留API版本） | 实际理由与阅读层级 |
| --- | --- |
| 1 / 2509.25186v1 | 新超导体发现：明确科学应用，题名范围关闭。 |
| 34 / 2509.24895v2 | 完整题摘：SRV/graph filtration测ESM2与蛋白结构忠实层、残基关系，结论指折叠应用，不把其蛋白结构收益移成通用表示定律。 |
| 57 / 2509.24655v2 | mRNA层级编码，科学应用题名范围关闭。 |
| 70 / 2510.00063v2 | 完整题摘：天文多模态MCQ数据/排行，未识别通用评价混杂或新失效条件，科学应用暂缓。 |
| 90 / 2509.24327v2 | 宇宙参数反演，科学应用题名范围关闭。 |
| 97 / 2509.25280v1 | 解剖演化digital twin，科学应用题名范围关闭。 |
| 99 / 2509.24262v2 | DNA/RNA结合蛋白分类，科学应用题名范围关闭。 |
| 110 / 2509.24227v1 | 前列腺扩散MRI诊断，科学应用题名范围关闭。 |
| 114 / 2509.24196v2 | 任意形状metasurface设计，科学应用题名范围关闭。 |
| 117 / 2509.24185v1 | 化疗后乳腺MRI模拟，科学应用题名范围关闭。 |
| 119 / 2509.24134v1 | 天体光曲线表示，科学应用题名范围关闭。 |
| 128 / 2509.24080v1 | 多语言Transformer推文情感ensemble，明确领域方法使用题名关闭。 |
| 142 / 2509.25274v1 | DNABERT结直肠基因分类，科学应用题名范围关闭。 |
| 161 / 2509.23793v1 | QIAS领域知识问答混合RAG，明确领域方法使用题名关闭。 |
| 166 / 2509.23751v1 | 完整题摘：PVT/U-Net、residual/skip adapter与SE组合及polyp指标；未给适用条件或收益归因，不因“novel”标签准入，也不因医学标签直接关闭。 |
| 167 / 2509.25269v3 | 盲位置ptychography重建，科学应用题名范围关闭。 |
| 189 / 2509.23609v1 | 中国期货价格因子，领域应用题名关闭。 |
| 191 / 2509.23603v1 | 低剂量CT去噪，科学应用题名范围关闭。 |
| 197 / 2509.23560v1 | 中医方剂推荐，科学应用题名范围关闭。 |
| 216 / 2509.23344v1 | 牙科诊断VLM，科学应用题名范围关闭。 |
| 243 / 2509.23127v1 | 一般gradient boosting回归统计推断，不是模型/训练/推理主线的具体增量。 |
| 248 / 2509.23100v1 | 口腔任务比较既有ViT/ConvNeXt，明确应用benchmark题名关闭。 |
| 264 / 2509.23004v2 | AI-Noether科学规律与规范知识对应，科学应用题名关闭。 |
| 15 / 2509.25043v1 | 完整题摘：软件测试研究taxonomy/roadmap，没有新执行机制或受控失效证据。 |
| 35 / 2509.24888v1 | 完整题摘：MRI质量信号增强场景组合，未披露通用条件/归因。 |
| 37 / 2509.24877v3 | 完整题摘：LLM社会科学研究视角综述，不新增模型形成或系统边界证据。 |
| 39 / 2509.24866v2 | 完整题摘：隐喻识别RAG/prompt/fine-tuning任务比较。 |
| 52 / 2509.24739v4 | 完整题摘：越南PET/CT数据与专家增强任务成绩，未新增训练有效性条件。 |
| 85 / 2509.24369v1 | 完整题摘：Stable Diffusion/PanoGAN几何组合与跨视图指标，未给新设计成立条件。 |
| 92 / 2509.24322v1 | 完整题摘：情绪推理综述归纳，不是新评价反证。 |
| 108 / 2509.24231v1 | 完整题摘：医学可解释VLM的SFT/VRL应用，未披露新的训练机制。 |
| 109 / 2509.24229v1 | 完整题摘：三个role的multi-LoRA/vLLM游戏对话组合与成绩，未新增执行/隔离条件。 |
| 115 / 2509.24194v1 | 完整题摘：临床3D latent rectified flow生成。 |
| 130 / 2509.24024v1 | 完整题摘：受邀logic/automata理解Transformer回顾，未给新的理论结论。 |
| 138 / 2509.23972v1 | 完整题摘：RTL assertion locate/classify/fix流程，未披露新执行可靠性条件。 |
| 152 / 2509.23859v1 | 完整题摘：CNN/ViT/adversarial debiasing颜值预测组合和任务指标。 |
| 162 / 2510.00055v2 | 完整题摘：临床肤色任务300人反馈与适配；未识别可移交通用judge的具体混杂，不采用临床保证。 |
| 173 / 2510.02359v1 | 完整题摘：排放领域RAG/数据工作流组合，未披露新的执行边界。 |
| 175 / 2509.25266v1 | 完整题摘：教育情感/创造协作概念视角，不是可核验模型机制。 |
| 206 / 2509.23435v2 | 完整题摘：角色音频数据与语音质量任务比较，未识别新评价失效条件。 |
| 214 / 2509.23350v1 | 完整题摘：ABC音乐十任务benchmark，未识别通用blindspot/控制缺失。 |
| 226 / 2510.02347v1 | 完整题摘：课程小模型RAG/prompt方法使用与成绩。 |
| 242 / 2510.03270v1 | 完整题摘：1.7B diffusion coding适配发布，披露的既有训练步骤未建立新机制/条件。 |
| 268 / 2509.22926v2 | 完整题摘：药物管理三项临床性能分析，未建立通用模型或评价选择增量，不采用安全效能。 |

## 保留集合及必要反侧

上表以外247身份全部保持日期隔离，不以小改进/医学/科学kernel/缺实验细节机械关闭；其完整原題摘与版本在两个发现JSON中。定点额外恢复50的subject-specific archetype contrastive、124的跨discretization联合field/geometry表示、249的SELFIES负侧与typed post-repair：三项完整题摘已读，保留通用表示/类型修复潜力，领域收益不采用。123 HyMaTE、126道德条件泛化、201教育研究问题、202IRT推断、208评分理由比较、222policy trace、232contradiction feedback、247 HTMA kernel、259缺失模态、270 Extract0、273 HEART、275形式化网络等仍保留；不能因只是一个局部负面结果而删去。

月尾13项完整摘要均有具体潜力：Retro* rubric/trajectory rewards；RLHI真实交互反馈；MGM双轨chunk；VSSFlow联合条件训练；skill composition受控任务；MASLegalBench协作推理；SIRI压缩/扩张预算；Greedy的早期灾难探索反侧；logical density结构采样；SIREN selective entropy；ReasoningBank成功与失败memory；ORPO-Distill mixed-policy；Scaling-with-Collapse条件性停止。没有任何一项借submitted/API最新v2–v4授首公开或评分。

有安全/理论/设计反证信号的13项取精确v1 HTML200，见`necessary-v1-fetch.json`与`2509.IDv1.html/.text.json`。以下位置为零基text block，完整v1题摘全部实际读；仅说明实际必要阅读，不冒称13全文/代码/复现。

| 精确v1 | 必要实际位置及收窄 |
| --- | --- |
| 2509.24967v1 SecInfer | 1034–1099、3986–4017：trusted task/system不可改、输入污染；多样system prompt/同类污染存在残余，不授全安全。 |
| 2509.24566v1 TokenSwap | 406–459、535–573、650–675、1327–1359、1866–1899：对手训练数据/过程权限；subject-object swap、adapter/LoRA投毒，judge/human是测量，不授无权限攻击。 |
| 2509.24488v1 Self-Sanitize | 383–437、535–579、830–900、968–1004、1629–1669：monitor窗口→未流出m-token cache丢弃→冻结已发prefix后修复；不是撤销用户已见内容。 |
| 2509.24359v1 DRIFT | 847–889、1810–1869、2253–2289、3876–3901、4165–4194、3247–3289：光滑/Lipschitz假设、nonadaptive不知防御；BPDA+EOT40steps/5samples及5/10/20加强反侧，DiffPure完整梯度受内存限，非安全证书。 |
| 2509.24296v1 DiffuGuard | 602–649、3321–3344：logit权限、主要AR转移攻击；diffusion专有攻击少、不覆盖训练后门/投毒。 |
| 2509.24257v1 VeriLLM | 1638–1689、1892–1939：one honest online verifier、eventual sync、正确contract、数值噪声前提；全collusion需ZK、VRF不防scheduler omission；M4/RTX5090数值区分不证明任意job。 |
| 2509.24125v1 inverse permutation | 252–270、668–714：stylized attention-only/noMLP/非完整位置模型，expressivity非训练/样本复杂度；本次未读完整定理证明，不外推全部decoder。 |
| 2509.23971v1 VFSI | 198–244、562–587、2646–2657：energy guidance，实际validity94.2%非100%；>50agents二次成本、应急relaxation/地图错误/长horizon退步；未核附录充分必要性证明。 |
| 2509.23806v1 concolic | 365–429、3990–4012、4947–4949、5805–5824：math.exp concretization使softmax underapproximation，可能漏flip；原模型concrete re-execution仅验证发现的反例，不证明搜索完整。 |
| 2509.25252v1 FGA | 440–467、925–959、1924–1947：结构化KB/链接与truth authority前提，多hop与KB bias限制；未采用deterministic factuality宣传。 |
| 2509.23002v1 UCP | 1368–1434、3071–3097：exchangeable batches/permutation invariance与drift审计；几何coverage不等无标签事实真值保证，未读全证明。 |
| 2509.23412v1 scoring rationales | 571–629、858–879：score QWK/NMI与rationale cosine分账，R2无rationale，语义一致不证明忠实因果；保留评价潜力。 |
| 2509.22834v1 optical formal pipeline | 525–600：90intents；2/15模糊约束被省略后语法仍valid、13/13检测是条件分母；unsat回退LLM-only并非verified topology。 |

以上均日期未证，不评分、不正面采用或进入Books。重开只需对应v1首次公开公告/可靠先发全文时间及必要方法，不重扫291或整月。

## 官方核心与代表关闭

官方RSS本窗11原条目实际读：Sora三条归一、Parental/CSEA各一，六条内部应用各读core。六条为support、inbound sales、contract data、GTM assistant、research assistant、Building OpenAI with OpenAI内部series，原正文在`30ordinaryweb1/2/3.json`，身份以RSS的link/title为准。实际披露RAG、专家反馈、evals、SDK/trace的场景组合；未给新执行机制、具体失效条件或可比收益归因，收入/效率数字不采用，不按“产品”标题一概关闭。

GLM4.6已执行原页200但598B壳后恢复官方`/blog/assets/glm-4.6-DhdhX09M.js`（20011296B，`glm-core-fetch.json`、`glm46-core.js`），完整英/中核心实际读。上下文/benchmark/tool-use与48.6%用户偏好、15%token的厂商发布事实，CC-Bench是在4.5已有评价上提高难度；未披露新评价盲点或控制预算机制，未新增架构/objective。所链2508.06471是旧GLM4.5家族，不伪4.6新报告。按贡献关闭，不采用性能；9/30日字段TZ未知不影响该关闭，不再虚列可执行未读hold。

Google PHA与AlphaEvolve、Anthropic Context management均实际读完整必要core，日期只有相交日/TZ未恢复，保留潜力而非关闭：PHA计划/代码分账与并行对照；Alpha有限gadget+lifting与最终brute-force核验（不采用科学应用收益）；Context stale tool-output清理与client memory CRUD分责，未授external rollback/weight learning。最后窄搜索/原HTML/schema检查无更精确字段；只在原始日期到达时重开。

MiMo home chunks实际读8个有日期paper与15个无日期blog，More只是同数组slice展开，没有下一HTTP页。当前2026发布不回填2025，原件在`mimo-home-6159.js`、`mimo-home-8557.js`、`mimo-home-fetch.json`。这完成当前可执行恢复，不支持历史完整覆盖。
