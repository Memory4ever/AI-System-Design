# Daily Research — 2025-07-03

**规范：** V3
**窗口：** 2025-07-02T09:00:00+08:00 ～ 2025-07-03T09:00:00+08:00
**窗口说明：** 用户授权2026-10-07补已有日报来源遗漏，原窗口、候选日期/评分及有效审阅保持；新增按前一完整自然日，不搬旧材料。
**补充窗口：** 2025-07-02 ～ 2025-07-02
**状态：** 完成
**Books：** 纳入本次
**检查时间：** 2026-10-11T10:53:27+08:00

## 1. 结论

只补北京时间2025-07-02自然日，原窗口、原0候选与有效证据保持。六个修正Advanced主题查询实际99出现/90唯一发现，官方cs.CL月表只浏览前25标题；均非本日新论文数或全池逐篇队列。新增60个唯一精确v1题摘已实际读取：本地38（首14由Bernoulli独核、额外23另由Ptolemy独核、00460撤回另列）与网页22不重复。原52有效判断只作去重和限定复用；题摘/core不计候选Evidence完成。

新增60题摘当前裁决为51贡献潜力、8具体关闭、1撤回不采用：首14为13P/1C，第二批23在两个准入疑点补正文后为19P/4C，网页22在SAFER最小版本核对后为19P/3C；00460另列撤回。潜力含更早家族与其他日期事件线索，不是51篇July02候选。安全/隐私/空间能力/修复安全限制及RAG-R1 v1已有11.1%的纠正已写回。WebArXiv v1为275 tasks，当前510不能反填；SAFER审批撤回门已由官方v3恢复及必要方法比对解除，保留v1窄P但仍缺首次公开日，不采用撤回v2。00460后续撤回不写成2025事件。Seed旧metadata-only已恢复真实数组，其余历史源和公开日继续隔离。

确定新增候选0、标准/深入候选Evidence完成0、Books新增0。没有把未知日期当无贡献或声称Books已有覆盖。原52家族的43日期保留/9具体关闭及两处core仅复用原权限，不搬材料、不重算日期/评分。

**本轮已完成隔离后的补查验收：** 来源、60题摘准入及必要消歧差额已具名独核并写回，Ptolemy已实际顺读最终六部分、核冻结与分层处置并签署[最终非作者DAY§6](../_sources/daily-20250703/second-calibration-supplement-20261011.md#6-july03-当前六部分最终非作者-day2026-10-11)，普通可执行待办0。依据另见[续跑观察](../_sources/daily-20250703/resume-observations-20261011.md)、[来源与22项独核§11](../_sources/daily-20250703/source-review-supplement-20261011.md)、[补查记录](../_sources/daily-20250703/supplement-20261007.md)与[原档案](../_sources/daily-20250703/baseline-before-supplement-20261007.md)。完成不消除日期/历史源缺口，不继承旧完成标签/作者旧非作者角色，不授外部缺口正面Coverage/Evidence、无遗漏或性能/安全保证。

## 2. 来源覆盖

以下为本轮实际有界切片，[新原件/请求](../_sources/daily-20250703/supplement-20261007/)保留URL、时刻、参数与状态。网页观察与HTTP失败分账；200表单/400/403/reset/浏览器超时不作零命中。原轮的有效范围保存在档案和SOURCE_NOTES，不把下载数计阅读数。

| 来源 | 检查范围与依据 | 结果 | 缺口 |
| --- | --- | --- | --- |
| SRC-OPENAI | [RSS](https://openai.com/news/rss.xml)新响应1251项，近窗July1 18:00BJT→July8 15:00；Research403 | 受阻 | RSS可见段无July2卡不替代Research历史覆盖 |
| SRC-ANTHROPIC | [Research](https://www.anthropic.com/research) publishedOn数组174出现/172唯一，近窗June27→July15停止 | 已检查 | 不用图片时间、不逐审172正文，不授未展示历史 |
| SRC-GOOGLE-AI | [July archive](https://research.google/blog/2025/07/)网页工具9卡，July2 SpeechCompass旧范围关闭复用；正确[Publication page2](https://deepmind.google/research/publications/page/2/)30卡Oct30→Mar28，近窗July13→July1 Refract→June26 | 受阻 | ?page=2是page1，不能当历史；curl失败与网页成功分账，Google年度LM Pubs必要入口失败，不由blog授全机构覆盖 |
| SRC-META-AI | [Research](https://ai.meta.com/research/)SSL reset无payload；本次[Blog?page=6](https://ai.meta.com/blog/?page=6)网页有2025-02/2024/2023混排，顶栏2026，停止该页 | 受阻 | 非July02切片，无目标卡不等无研究 |
| SRC-QWEN | [Blog page2](https://qwenlm.github.io/blog/page/2/)五卡July22→June27/26→June5/Apr29，越窗停止 | 已检查 | 限可见Blog，不授未展示研究/全release |
| SRC-DEEPSEEK | [Updates](https://api-docs.deepseek.com/updates)近窗August21→May28 | 已检查 | 限官方公告序列，不授Research全覆盖 |
| SRC-MOONSHOT | [Kimi Blog](https://platform.kimi.com/blog)可见July11→May6停止 | 已检查 | 普通Git提交不等首次正文公开 |
| SRC-TENCENT-HUNYUAN | [Research](https://hunyuan.tencent.com/research)SPA，publicList pageNum1/pageSize100/renderType0成功9/9、日期全2026；浏览器30秒超时/reset | 受阻 | 未取得“全部”UI及2025列表，9条不授2025零研究 |
| SRC-ZAI | [Research?page=2](https://www.zhipuai.cn/zh/research?page=2)实际18卡2026→December7 2025、“没有更多”；旧GLM-V July1发布字段限定复用 | 受阻 | 不说20或猜伪分页，July历史缺段/GLM旧归属不动 |
| SRC-BYTEDANCE-SEED | US locale type1/2、tokens0/20真实数组；论文18+20=38 IDs/94，博客18+18=36/45，next40/has_more true；paperJuly4→June27、blogJuly14→June28/25夹窗后停止20 | 已检查 | 移除旧metadata-only请求；不是94/45全文或全站，未翻页为有界停止 |
| SRC-BAIDU-ERNIE | [Blog page2](https://ernie.baidu.com/blog/zh/page/2/)末页2/2六卡November→June30 | 已检查 | 无July02可见卡，不迁June30报告 |
| SRC-XIAOMI-MIMO | [主页](https://mimo.xiaomi.com/)和8557/6159 chunks成功；Paper8项May12/June4→Sep19及后出；Blog15项，More用本地slice不发历史请求 | 受阻 | Blog不能写全2026，含2025版本但无可核July历史段/日期 |
| SRC-MINIMAX | [EN](https://www.minimax.io/blog)12卡尾Oct27；[CN](https://www.minimaxi.com/blog)13卡含Jan15却缺June M1，停止可见列表 | 受阻 | 稀疏目录非完整July archive，当前无卡不授零事件 |
| SRC-ARXIV | 六Advanced CS/cross-list、original submission June30～July2、size25/start0、sort -announced_date_first：model25/254、training25/52、inference6/6、MoE6/6、multimodal25/105、agent12/12；99出现/90唯一。model/training/multimodal有Next未读，其他末页；月cs.CL前25/1672标题及相关摘要定点核 | 受阻 | 最初缺hidden的200表单/不支持sort的400均不算命中；提交非公开日、公告仅年月，不使用catchup，不把宽库存转逐项队列或授重要修订日级覆盖 |

未扫每周源；按需仅同身份必要原文/版本，不扩全会议。[来源独核§1～6](../_sources/daily-20250703/source-review-supplement-20261011.md)已核实际请求、真实数组、六查询与有限停止；网页成功观察与本地失败请求的权限分开。有界切片不证明历史缺口消失。

## 3. 候选与判断

没有已核实完全落窗的新增候选，表中不填条目、不提前评分。原43日期保留项只复用旧权限，见[FIRST](../_sources/daily-20250703/FIRST.md)。本轮独核潜力另见上述两份具名校准；明确贡献关闭、撤回和更早家族均保留实际理由，不借日期未定缩池。0候选不表示没有重要贡献，也不将准入窄读累计为候选证据审阅完成。

| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |
| --- | --- | --- | --- | --- |

## 4. 证据与知识整合

暂无满足日期准入的材料，因此没有标准/深入完成的候选证据，也没有可执行的正面Books增量。现有owner覆盖足够与否未由这些日期不明材料判定；必要日期到达后才定位实际owner、对比其具体论点和证据，并由root协调共享写入。

首批校准触发了必要的最小核心补读，而非全部PDF/版本考古：CARE-RAG v1 §3/Table1–2与AppendixB.3有reference修订对评价改变的潜在反证，但模板残留、数据集命名不一致使错误比例/安全可靠性数字不可直接采用；EdgeLoRA v1 §3.2/Algorithm1明确top-k质量候选内优先缓存驻留adapter，是质量与换入成本的实际决策；TriVLA摘要的future video dynamics conditioning改变只按当前观测的policy设计分支。三项关闭撤回、进入日期隔离，不由此给性能或安全保证。核心原件与具体限制见FIRST；这些不是本窗技术结论。

以上两段为原有效正文，连续保留；以下仅补本轮准入与反证，不是未知日期材料的正面Evidence或Books采用。

首14独立校准实际为13潜力/1关闭，九处决定性core见[Bernoulli§5～6](../_sources/daily-20250703/review-supplement-20261007.md)。PB-LLMs为成熟NER加合成简历，关闭不等隐私已保证。GAFGuard的动态结果不全优于G-Eval；PromptInjection的两例/模型名冲突不授通用成功率；CodeFix的功能通过和安全检查不是同一集合；InvisibleInk仅在固定参考、邻接及生成范围给隐私命题；空间推理的随机任务不证明无泄漏，SMART不证明推理忠实。用户行为entropy proxy不等原生概率校准，GateRecursive线性复杂度对象是模态而非tokens，RAG-R1 v1已含11.1%声明，不能误记新版新增。其余APARL、4D、LLMMesh与SDAcc均限具体机制和配置，旧版LLMMesh不反填新版SLINFER。均不据作者数字授普遍能力或安全。

第二批具名反侧见[23项校准](../_sources/daily-20250703/second-calibration-supplement-20261011.md)：PokéAI完整三Agent集成尚属future work，保留的是局部无效动作/权限与资源混杂；DigitalMe是虚构persona演示中的事实与情绪失配，不是神经可塑性或真实用户泛化；人类响应校准为输出choice回归而非LLM权重更新；Qualcomm设备比较含栈、设备数和能耗口径差异，不授硬件因果排名。Autonomy Security的CMDP/primal-dual与yProv4ML的PROV/存储组合没有所述新机制，分别关闭，不以survey、科学用例或Books已覆盖代替裁决。

网页22的独核见[§7～10](../_sources/daily-20250703/source-review-supplement-20261011.md)。00601必要正文后改关闭；00606教师确有按题选择模板，改保留窄监督潜力，不证明学生自主路由。Reasoning-Infused有总体改善却少数类恶化/解释不忠实；Question Decomposition有非等检索池及实际延迟，不能称所有指标提升或与baseline同成本。WebArXiv v1锁定275任务；Driving Video只给符号场景到生成画面的验证问题，未证事件/时序保真。安全反侧Refused Knowledge、Memorization、Interference、Ad Co-Evolution保留，不因负面或广告应用关闭。所有实际窄读的版本、位置与未证事项在具名记录，不冒称完整全文、代码或实验复现。

两个U已由[独立决定性PDF读段](../_sources/daily-20250703/second-calibration-supplement-20261011.md#5-两个-u-的最小核心独核追加2026-10-11)转窄P。01067的TimesFM六年/最近两年优胜翻转、根因与误差指标差异、小样本微调反侧会改变模型选择；但根因标注年限、测试期lag选择与泛化仍有限。02975的增量只保留评价推断边界：context不答题不等整库缺证据，同PubMed系统也可因检索/生成/judge而不同；三Boolean本身不授新颖性，更不引入医疗有效性。其同分母对照是1739子集，不能混总体比例；原样本2972与表2942冲突保留，不授来源优胜的因果结论。

SAFER[版本窄核§11](../_sources/daily-20250703/source-review-supplement-20261011.md#11-safer版本普通待办定点关闭v改窄p)确认v2为发表审批撤回、v3已官方恢复；v1/v3的SAE→chosen/rejected特征对比→偏好数据评分链路及必要公式同向，未见取消该窄P的具体勘误。解除旧版本门，不机械等待“证明所有版本无差异”的作者声明；不采用未读v3新消融、不反填2025结果，也不为v1实验背书。当前只缺v1日级公开归属。

## 5. 缺口与下一步

本轮可执行工作：无。两项U、SAFER版本门、来源写回与最终六部分非作者DAY已实际完成，不继续列为普通/外部缺口；日级验收依据具名实核，不从局部通过或机器校验继承。来源检查和其他有效独核复用，不重扫90发现/1672月库存，不调整原候选时间。

下列为已隔离的外部终态保留项，缺少具名必要的原始公开日、先稿身份或历史目录材料，不支持正面证据、Books、完整覆盖或无遗漏断言；具体替代材料和定点重开条件见A～C，到达只重开对应身份/历史切片。它们不是候选Evidence完成，也不恢复已关闭的普通待办。原轮DAY不验收本轮。

### A. 精确家族的实际首公开时间

以下42个原有arXiv v1家族共享同一日期缺项，保持原归属未决而不迁日：API提交字段、abs submission history及发布排班不证明真正首次公开。旧有限恢复已试REG/CompactDS abs、目标cs.CL日列表（cache miss）、REG OAI（不可达）、SciRate历史页（不可达）、定点公告/作者线索，未取得实际公告。接受原始arXiv公告/公开列表的日级批次边界，或作者首次公开正文的可核日期；不要求秒级时刻。原项按原授权窗口处理，新增按July02自然日，只定点重开相关家族，窗外线索不扩本窗。本日不评分、不采用/进Books、不支撑无遗漏；日期到达后按FIRST机制问题补必要证据，不提前通读全部论文。

| 精确v1身份 | 日期到达后重开的问题 |
| --- | --- |
| [FlashDP 2507.01154v1](https://arxiv.org/abs/2507.01154v1) | per-layer梯度融合能否同时避显式per-sample内存与GhostClip重算 |
| [JAM 2507.01201v1](https://arxiv.org/abs/2507.01201v1) | 冻结骨干跨模态对齐的实际约束，不混新版本 |
| [PAE MobiLLM 2507.01216v1](https://arxiv.org/abs/2507.01216v1) | activation传输/缓存与prediction-difference隐私边界 |
| [Beyond First-Order 2507.01241v1](https://arxiv.org/abs/2507.01241v1) | 随机conjugate方向与采样复杂度假设 |
| [CompactDS 2507.01297v1](https://arxiv.org/abs/2507.01297v1) | simple RAG推理失败是否由datastore覆盖条件决定 |
| [LaRoSA 2507.01299v1](https://arxiv.org/abs/2507.01299v1) | 旋转+Top-K训练自由稀疏的稳定质量/真实系统开销 |
| [ICLShield 2507.01321v1](https://arxiv.org/abs/2507.01321v1) | 不改权重的示范投毒与概念偏好防御边界 |
| [Activation RM 2507.01368v1](https://arxiv.org/abs/2507.01368v1) | few-shot activation reward与hacking风险 |
| [REG 2507.01467v1](https://arxiv.org/abs/2507.01467v1) | 语义token参与去噪vs仅训练期对齐 |
| [SafePTR 2507.01513v1](https://arxiv.org/abs/2507.01513v1) | vulnerable-layer剪裁/后层恢复的效用与攻击范围 |
| [SPRO 2507.01551v1](https://arxiv.org/abs/2507.01551v1) | policy内生process reward与masked advantage |
| [Muon analysis 2507.01598v1](https://arxiv.org/abs/2507.01598v1) | 四变体收敛、LR/decay与critical batch假设 |
| [DaiFu 2507.01628v1](https://arxiv.org/abs/2507.01628v1) | 运行上下文原地恢复与一致性/重执行范围 |
| [LASAD 2507.01652v1](https://arxiv.org/abs/2507.01652v1) | 2D位置decay与线性attention图像AR取舍 |
| [AsyncFlow 2507.01663v1](https://arxiv.org/abs/2507.01663v1) | streaming调度、延迟更新与policy staleness |
| [SODA 2507.01693v1](https://arxiv.org/abs/2507.01693v1) | exact next-token logits inversion的输入长度/可见性边界 |
| [DisCon 2507.01756v1](https://arxiv.org/abs/2507.01756v1) | 离散表示从target转为continuous生成条件 |
| [Evaluation Awareness 2507.01786v1](https://arxiv.org/abs/2507.01786v1) | testing/deployment可分性不等于有意欺骗 |
| [Modality conflict 2507.01790v1](https://arxiv.org/abs/2507.01790v1) | router heads干预与模态偏好、指令偏好的区分 |
| [CPU LoRA meta-generation 2507.01806v1](https://arxiv.org/abs/2507.01806v1) | 前置adapter-bank训练换CPU更新生成的范围 |
| [HARP 2507.01900v1](https://arxiv.org/abs/2507.01900v1) | 头位置与adaptive rescaling，幅值是否解释损失 |
| [GAPO 2507.01915v1](https://arxiv.org/abs/2507.01915v1) | 多目标gradient/Pareto保证与用户权重假设 |
| [NaturalThoughts 2507.01921v1](https://arxiv.org/abs/2507.01921v1) | 控制预算后的trace难度/策略多样性 |
| [AC-DiT 2507.01961v1](https://arxiv.org/abs/2507.01961v1) | 移动底座影响条件化与阶段2D/3D权重 |
| [CARE-RAG 2507.01281v1](https://arxiv.org/abs/2507.01281v1) | 修复reference改变指标是否可信；模板残留/命名错误须解决 |
| [TriVLA 2507.01424v1](https://arxiv.org/abs/2507.01424v1) | future dynamics参与policy的实际机制/消融 |
| [EdgeLoRA 2507.01438v1](https://arxiv.org/abs/2507.01438v1) | 先核family更早首次公开身份：v1首页列MobiSys June23–27 2025与DOI10.1145/3711875.3729141，可能会议正文已在arXiv上传前公开；须恢复真实正文首次公开，不能把July2上传当首公开/重复算事件。其后才核top-k驻留质量损失/换入成本与LRU/LFU不一致 |
| [Global/Pairwise Scores 2507.01633v1](https://arxiv.org/abs/2507.01633v1) | 稀有错误/置信及ties下ranking可靠性的条件 |
| [Vision Understanding 2507.01955v1](https://arxiv.org/abs/2507.01955v1) | API任务表达下semantic/geometric能力与prompt敏感性 |
| [HOI-Dyn 2507.01737v1](https://arxiv.org/abs/2507.01737v1) | dynamics预测误差的residual loss与训练/推理成本分离 |
| [PULSE 2507.01271v1](https://arxiv.org/abs/2507.01271v1) | pretrain/finetune遗忘差别、批量/顺序请求效用反证 |
| [ReFlex 2507.01496v1](https://arxiv.org/abs/2507.01496v1) | mid-step inversion结构保持与attention编辑性 |
| [MiCoTA 2507.01887v1](https://arxiv.org/abs/2507.01887v1) | student容量/CoT长度、分布接近是否解释可学性 |
| [LEDOM 2507.01335v1](https://arxiv.org/abs/2507.01335v1) | reverse AR与Reverse Reward的posterior评价 |
| [LTDR 2507.01351v1](https://arxiv.org/abs/2507.01351v1) | 视觉tail vs语言均匀expert routing假设 |
| [Low-Perplexity 2507.01844v1](https://arxiv.org/abs/2507.01844v1) | 低PPL不等于verbatim training recall；corpus可见性 |
| [Look-Back 2507.03019v1](https://arxiv.org/abs/2507.03019v1) | 隐式attention视觉回看而非外显重注入 |
| [FUSE 2507.02135v1](https://arxiv.org/abs/2507.02135v1) | CPU/GPU/Memory联合DVFS与独立governor能耗边界 |
| [SPoT 2507.01654v1](https://arxiv.org/abs/2507.01654v1) | oracle continuous位置上界不等于实现高效token routing |
| [Spherical Diffusion Policy 2507.01723v1](https://arxiv.org/abs/2507.01723v1) | 全去噪链SE(3)等变而非仅编码等变 |
| [Latent CoT 2507.02199v1](https://arxiv.org/abs/2507.02199v1) | probe/layer依赖和深度收益反证，不预设内部CoT |
| [Diffusion Loss Comparative Study 2507.01516v1](https://arxiv.org/abs/2507.01516v1) | sample quality/likelihood目标在不同条件发散，条件与目标选择需核验 |

单独保留[GLM-4.1V-Thinking 2507.01006v1](https://arxiv.org/abs/2507.01006v1)：[官方GLM-V Project Updates](https://github.com/zai-org/GLM-V)原始字段`2025/07/01`为model与report发布（此前07/02 artifact线索撤回），未给可核本窗归属；不改已有日期，不据未知时区造July02。接受首次公开公告或可核所属自然日的日期边界，不要求具体时分秒。到达后只重开该家族RLCS curriculum贡献及相关真实日报，后续GLM4.5V不用于v1证据。

### B. 来源/修订批次历史payload

本次只需July02必要原始目标段：OpenAI Research、Meta研究目录、Hunyuan“全部”2025列表、Z.ai July历史卡、MiniMax July官方archive、MiMo2025 July Blog、Google/DeepMind publications，以及arXiv实际日级公告/重要修订批次。共同必要性是这些历史范围不能由动态首页、有限feed或提交池代替；恢复后先按主题浏览目标段，有具体身份才局部核验，不请求全年全站重扫。Seed本轮真实论文/博客数组已恢复，旧metadata-only不再作为当前材料请求；有界停止未展示部分不授全机构覆盖，也不伪装成访问故障。

### C. 本轮新增潜力的日级公开与更早家族

以下是本轮独核后51个P身份，而非正式候选；完整标题、primary链接、具体增量和限制保存在三份具名复核。所需日期只为决定是否纳入July02新增，不请求全篇或重复恢复已读段。原52的请求与本轮身份无交集，不重复计数。

- [首批13P](../_sources/daily-20250703/review-supplement-20261007.md#5-全14-first校准及必要安全设计读段)：2507.05266、02990、02986、02985、02984、02978、02976、02974、02962、01327、01099、00507、01309（短ID沿用2507前缀，均v1）。
- [第二批19P](../_sources/daily-20250703/second-calibration-supplement-20261011.md)：2506.23635、23689、23826、24019；2507.00330、00394、00418、00439、00534、00707、00754、00990、01067、01339、01347、02964、02975、02982；2509.16204（短ID沿用各段前缀，均v1）。
- [网页19P及SAFER更新](../_sources/daily-20250703/source-review-supplement-20261011.md#7-新差额22项精确v1独立准入校准)：2507.00390、01016、00938、00401、01264、00152、00210、00214、00216、00239、00246、00258、00322、00355、00389、00509、00606、00297、00665（均v1）。

除下述已知先稿/其他事件线索外，各身份缺真正首次公开日：提交池、abs submitted和公告年月不提供日级归属，所读月表也不是当期日级公告。已穷尽本轮有限原始入口，无可替代日证；不按日程算公开日、不以日期未知关闭贡献。接受官方历史公开列表/公告、作者首次公开正文或明确覆盖本日的日期范围；到达只重开相应身份的日期准入，再评分、读足拟采用命题所需证据并比较唯一Books owner。必要日期未到，不采潜力结论为本窗事实、不先写书。

00297博士论文已定点核出2020/2022的两条旧公开家族；这些贡献不计2025新事件。只有具名区别于旧稿的新增命题与其首次公开证据，才重开2025事件，不重新阅读博士全文。23635有RACS2024/DOI先稿线索，先恢复同家族真实正文而非把2025上传当新首公开；16204当前arXiv事件另属September，若有真实更早作者稿线索才核那个事件，不迁已有归属/扩本窗。00665只缺v1公开日，旧V门不再请求。

八个具体关闭为02966、2506.23844、2507.00163、00579、01075、05125、00601、00540；其短ID前缀沿用2507，完整理由在校准记录，均不因日期不明或成本关闭，不另索日期。00460官方后续原创性撤回单列，不采用该版本、不评分、不进Books；不说本日发生撤回。月表另三明确范围外标题不计60完整题摘或全文关闭。

## 6. 复核

复核者：Bernoulli（首14）；Ptolemy / second-calibration-supplement-20261011（第二批23、最终六部分DAY）；Anscombe / July03 source reviewer（14来源、网页22及SAFER窄核）。均非本轮报告作者root / Codex。

结论：通过

上述分层校准已实际完成，全部潜力、安全/纠错/设计反侧与具名争议关闭项在必要范围独核；首14/9core、第二批23与六已有core加两决定性PDF、网页22及最小正文/版本核分账，不称60篇全文或候选Evidence。来源49请求形态/停止、真实Seed数组及网页成功与curl失败权限已经独核。代表范围外三标题未独立全文读取，月库存/后页不作全量审阅。Ptolemy[最终DAY§6](../_sources/daily-20250703/second-calibration-supplement-20261011.md#6-july03-当前六部分最终非作者-day2026-10-11)实际核51P/8C/1撤回与身份去重、14来源停止、0候选/0Books、全部六节采用边界及外部恢复条件，确认普通待办0；原窗口/原0候选/连续原§4保持。通过的是本轮安全终态，不继承下述旧轮裁决，也不授日期/来源正面覆盖。完成态V3、Markdown/本地引用与限定diff在同步后再次核验，机器检查不代替上述语义复核。

### 原轮复核（不验收本轮）

原轮复核者：root（非作者，首批校准及DAY）

结论：通过

通过的是隔离后的安全终态，不是日期/候选证据通过。

root首批实际完整读14份精确v1题摘：FlashDP、JAM、HARP、SODA、Evaluation Awareness、SafePTR、AsyncFlow、AC-DiT与当时六关闭CARE-RAG、TriVLA、EdgeLoRA、Agent-as-Tool、TD-MPC-Opt、Keye-VL。八潜在方向可保留、不采宣传数字；CARE-RAG/TriVLA关闭过窄，EdgeLoRA需一处核心消歧。作者已按反馈定点改判三项、保存原件/边界并移除活跃旧关闭。root后续实际补读余16份、GLM v1及追加22份（含REG重复），共52唯一家族完整题摘校准；扩散Loss比较不能只因overview关闭，已按目标选择有效性线索重开。其余追加六关闭理由可保留，finance不是自动排除标签。新增纠错/设计反证没有因日期未定被关闭，9个当前关闭只按具体贡献理由，不要求无意义日期恢复。此为52题摘独立校准，不是52篇全文或证据审阅完成。

DAY实际完整读取本README、FIRST、SOURCE_NOTES以及52独立题摘；另定点核CARE-RAG §3 Tables1–2 / AppendixB.3及EdgeLoRA §3.2 Algorithm1 / §4.2，确认QA reference反证线索的可信度限制和top-k驻留取舍，不采宣传数字。发现EdgeLoRA首页更早MobiSys/DOI身份；[Crossref原始响应](https://api.crossref.org/works/10.1145/3711875.3729141)published-print为`[2025,6,23]`、published-online为`[2025,9,25]`、created为2025-10-02，ACM正文403，元数据冲突不能证明实际首公开，故明确隔离更早身份并禁止arXiv上传重复记家族。该问题已修正，不再追查。

DAY验收包括记录中的14来源实际范围/停止点、错误查询不作覆盖、公开日期与修订缺口隔离、0确定候选/0证据审阅完成及0Books写入。未独立重读原始宽列表全部条目或补齐受阻机构历史目录，未确认43保留项落窗，未证明全源无遗漏；源/日期隔离不算Coverage或Evidence通过。此范围内没有未处理的可执行工作，后续原始材料到达只局部重开。

机器校验：`python3 scripts/validate_research.py --report papers/2025/07/03/README.md`通过（1份V3、0候选行）。相对文件引用全部存在，42行共同日期请求加GLM单独请求与43保留计数一致；未新增确定候选。diff/空白与本日写入范围检查通过；未stage/commit/push、未写共享Books/索引/LEARNING_STATE。静态通过不替代上述语义复核。
