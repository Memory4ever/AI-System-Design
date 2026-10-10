# 2025-10-01 补查首批独立复核

复核者：Dewey，非本日作者Euler。记录时间：2026-10-07T16:01:00+08:00；实际检查延续至写后校验。对象：[当前Report](../../01/README.md)、[Euler补查记录](supplement-20261007.md)及其必要原件。11/01作者停点已保存后独立切入本日；恢复时重读主AGENTS、当前研究/Report/来源合同、统一Prompt、ROADMAP及当日材料。最新State只用于路由，不授年度完成。

**结论：未通过。首批准入可按下面限定继续，不能授本轮日级验收；有4项普通可执行校正，不是全由外部日证据缺失阻塞。** 原OpenAI七案例家族、原日期、5分及有效审阅不变。尚无确定新增当窗家族；本复核不评分新线索、不编辑Report/Books/State、不授Books POST。

## 1. 作者需要处理的校正

### R1 / P1：撤回信号不能被普通贡献关闭或日期held覆盖

本轮已实际打开三份官方abs的页首、Comments和Submission history，原件中的当前摘要仍保留正面收益，不能因此恢复采用权限：

| 身份及当前版本 | 官方位置与事实 | 必要处理 |
| --- | --- | --- |
| [PoseDiff 2509.24591v2](https://arxiv.org/abs/2509.24591) | 页首L8已撤回；Comments L21指实验设置/指标不严谨、比较公平性受影响；history L30的v2标withdrawn | 从普通潜力/待日归属集合移至撤回排除，不入选、不评分、不进入Books；不继续请求日期或泛读附件来挽救该正面命题。 |
| [Social Science 2509.24877v3](https://arxiv.org/abs/2509.24877) | 页首L8及history L31撤回；Comments L21指语料、方法、框架和结论已根本重构 | 不能只记taxonomy无增量。保留撤回与研究重构原因；不采用旧稿结论。 |
| [BiHDTrans 2509.24425v2](https://arxiv.org/abs/2509.24425) | 页首L8及history L32撤回；Comments L23指方法局限和实验设置缺陷 | 从“19条标题范围外、没有可见纠错信号”中分离；必要纠错检查已执行，不把withdrawn当访问故障。 |

当前官方修订字段分别为2025-10-30、2026-09-05、2026-09-10；只是当前页面的版本/撤回身份，不是本复核确认的公告公开日，不生成本窗修订候选。不能以旧v1还有摘要/下载入口静默恢复失效结论。

共同原因是未处理当前官方状态。本复核有界扩查四份已保存API的125个唯一ID的Comments，撤回/纠错相关命中共4项：上述3项和NVFP4 Eq2 typo。前三个再定点打开官方abs，NVFP4已有明确纠错隔离保留。没有为证明无标记打开125个abs或遍历全版本史；其余无Comments信号也不等于已证明无修订。

### R2 / P2：Qwen列表后侧判断与真实原件不符

对[API原件](supplement-20261007/qwen-api.raw)逐项解析`date`，确为60条、Sep30日期0条；但最新字段是2025-12-23，不是09/24。BJT相邻记录为09/24 `Qwen3-Max: Just Scale it`和11/13 `Qwen DeepResearch: When Inspiration Becomes Its Own Reason`，原UTC字段经时区解析后比较，不使用小时门槛排新增。

请同步Report/补查记录中“最新止09/24、没有后侧”的事实与缺口原因。可以说本次返回配置库存有前后侧、无Sep30对象；不能由此声称库存历史完整或全站零事件。真正未披露的是此配置是否完整保留目标历史事件，不是解析依赖、请求失败或后侧缺失；不要求为这项纠正重扫全部60正文。

### R3 / P2：重开EQUISeg的贡献关闭

[2509.24505](https://arxiv.org/abs/2509.24505)完整题摘见[CV/RO API](supplement-20261007/arxiv-multimodal.raw)。摘要明确提出优势模态退化时整体失效的问题，以equal encoding、四阶段CMTB及SGM mutual guidance调节模态贡献，并评价degraded conditions。这个“模态依赖失衡 → 互相引导/贡献调节 → 退化条件下融合选择”的链条属于`MULTIMODAL-REPRESENTATION`主线，不能只因segmentation任务或局部实验关闭为task-specific fusion。

**首批准入结论：保留机制潜力，未证明实验有效、普遍迁移或新颖性。** 仍需官方日归属；若落窗，读精确版本核心、balanced baseline/模块消融与退化协议，核等编码和SGM各自收益及额外代价。不要因Books已有融合主题取消这项，亦不把本复核的owner路由当长期采用。

### R4 / P3：EOE机制不是替代AdamW

[2509.24436](https://arxiv.org/abs/2509.24436)完整摘要明写先执行AdamW，再在当前/最佳expert间对tensor weights施加crossover、PSO、mutation。作者“参数演化替代优化”宜改为“AdamW与expert参数演化混合”。潜力保留，未核吞吐、质量对照或训练成本，不为这一措辞返修读完整附件。

## 2. 所有新潜力的准入校准

本轮独立读完[96个具名ID](supplement-20261007/abstract-read-ids.json)的完整标题/摘要，实际来自四份官方Atom，不接受作者已读标签作证明；输出截断的9项已另行重读。对另29项读身份、标题及Comments，BiHDTrans再读当前abs完整摘要/撤回说明。**这是题摘准入校准，不是96项历史Evidence通过。** 当前API后期修订摘要不能回填2025。

原96项含76项保留潜力、20项拟关闭。原76潜力全部校准：PoseDiff撤回排除，AMemGuard保留机制潜力但公告月October退出本窗，其余74项保留潜力；EQUISeg从20项关闭中重开。净75个September身份潜力仍只是日期恢复线索，非本日候选分母；这些数量不授窗口召回或全文审阅完成。

下面各行覆盖原潜力身份，按具体贡献层列出；AMemGuard/PoseDiff另如上述处置。作者原“约束→增量→选择”链可复用，但采用命题和精确版本仍须后续Evidence限定。

| 层/已实际读完整题摘的身份 | 校准及需要限定的关键点 |
| --- | --- |
| 解码/训练/系统：2509.25188,25176,25149,25073,25041,24859,24626,24381,25279 | Learn2PD、SIRI、NVFP4、PTG、GRACE-MoE、HARP、SparseServe、RServe、RL in the Wild均有具体机制或设计反证；不能只按倍率、模块名称或负面结果收/删。RServe摘要核心称REDServe，后续绑定精确版本而非误合并。 |
| 表示/优化：2509.25174,25148,25300,25040,24945,24935,24808,24653,24781,24483,24436,24416,24372,24389 | 条件数/归一化、anchor、RL缩放、token聚类理论、数据重采样、GAN scaling反证、输入trace、二跳监督、error amplification、prompt干扰、混合演化、CLQ、无反传ES、LLaDA-MoE均保留机制/边界潜力；EOE按R4改述。XQC是SAC连续控制，不自动称LLM RLHF改进，须限定优化条件数问题如何影响主线选择。 |
| 多模态/运行时：2509.25187,25182,25178,25177,25162,24948,24837,24734,24702,24695,24527,25160,24473,24405,25155,25304,24979,24896,24791,24776,24768,24427,24387,24385,24365,24241,24081,24072,25001 | 图像条件shortcut、codec迁移、幻觉诊断、语义token、模拟环境反馈、剪枝敏感度、联合对齐、物理guidance、视频状态、Dreamer4、视觉/几何reasoning、语言任务边界、NPU算子、时频anchor、latent噪声、主动distillation、选层干预、感知reward、分层VLA、UI2V盲点、动作entropy、几何prior、梯度冲突、动作条件、cube预测、grounding因果、LVT局部view几何都不能按模态/3D/机器人题名排除。DAM保留数据适配机制边界，不能外推foundation pretraining。 |
| Agent/系统理论：2509.25189,25084,25052,25047,25299,24726,24704,24524,25282,24803,24378,24932,25140,25301 | entity难度、multi-turn训练稳定性、playbook、可验证任务生成、identity状态、动态课程、latent memory、VLA反馈编排、distribution-shift因果反证、时序语义、FedSpan通信聚合、ReasoningBank、DAG搜索均有明确待核命题。FedSpan须限定卫星拓扑与模型分布式学习约束，不能只有通信类比就准入；CVP不因synthetic局部结果关闭。 |
| 安全/负侧：2509.25003,24566,24488,24359,24368,25302,24675,24413 | ScoreMIA、TokenSwap、Self-Sanitize、DRIFT、DLM watermark、自复制、unlearning反证、DynaMIC均覆盖必要安全/评价反侧；不能因防御已有章节、结果负面或日期未核丢掉信号。 |

安全/反证逐项限定：ScoreMIA单query不等全威胁模型；TokenSwap关系词攻击不等部署绕过；Self-Sanitize流式repair需核privacy与开销；DRIFT须检自适应攻击/梯度遮蔽；watermark任意顺序不等任意改写稳健；自复制当前v2含后期OpenClaw语境不回填2025，overuse指标不等失控风险；unlearning拒答不等知识删除；DynaMIC区分误导识别和真实执行拒绝。GHOST、LayerCD、World-Env、Physical plausibility、UI2V、PTG、CVP、NVFP4等负侧也已在对应完整题摘校准，不按小模型/负面/局部筛掉。

TokenSwap、Self-Sanitize、DRIFT的09/30旧有效审阅只能按确切版本/未变化命题复用，不从本轮当前摘要重新搬归10/01。AMemGuard 2510.02373机制不是被判无贡献；只保留October恢复身份，不由Sept submitted搬入本窗，不授该真实归属日完成。

## 3. 代表排除与旧事件复用

arXiv普通贡献关闭不是只抽标题：本轮实际读了作者20个拟关闭的完整题摘。R1的Social Science、R3的EQUISeg必须改判；其余18个在摘要可支持的最小范围接受关闭：

- 整理/测量层：2509.25043、24422提供Roadmap/分类或相关性分数，未建立本项目具体机制或重要评价盲点；不因为综述形式排除。
- 流程/任务层：2509.25297、24855、24826、24515分别TDD、角色协作、HIL界面、spec加验证反馈；未从题摘建立新的可靠性/失效条件或可归因机制。PhysicsMinions不是仅因physics名称关闭；Move MSG的验证反馈保留为局部工作流事实，不称没有验证。
- 任务数据/课程层：2509.24163、24651的偏好stacking数据/示例顺序，题摘未建立foundation/Agent通用选择变化；不是机器人类别退出。
- 暂缓领域与具体应用层：2509.24597、24267、25143、24888、24739、24231，分别脑障碍模拟与MRI/PET等研究目标；题摘的模型/data/evaluation服务领域机制，未给本项目可采用的基础模型机制链。Dyslexia确有VWF unit ablation和选择性读字效应，不能写“没有机制”；接受本次关闭的依据是研究目标/结论仍为人脑疾病计算模拟，非否定其因果实验。TemMed局部时间推理不足亦保留，不假造已无局限。
- 领域评价层：2509.24958、24922、25286、25283的临床询问/法律协作/政治量表/人口模拟，未建立本项目新的模型机制或可复用评价协议；局部结果未因规模小被否定。

另29项中：10个October ID的身份/月份隔离接受，未核具体日；19个标题范围退出中BiHDTrans按R1分离，余18只支持标题明确的领域应用/非主线范围退出，不宣称完整题摘已审。没有审这些普通项的全文附件；若新安全/纠错信号到达，只重开受影响项。

机构样本按来源/理由层检查：

| 样本 | 实际检查及裁决 |
| --- | --- |
| Sora2 / Sonnet4.5 / Claude Code，旧归属去重层 | 定点读09/30候选/相关证据与BOOKS_HANDOFF，三家族原事件已有有效审阅，仍留09/30。Sora初始PDF与旧件独立sha256同为`1a74678aacf0499a3b4d2ae71da9bdbb1221a8211a9c3890fe87748a5ccdcd51`，不重读全部附件。当前characters/撤销细节/2026停服不回填初始card。 |
| GLM4.6，版本发布/贡献关闭层 | 实读本轮核心模块，09/30官方date字段、与旧模块同SHA`6dde83a7bceacd9fcb2a915ad07340ae6eecb9d8b0cf68d7a86f89368fd47b8a`复现。更难CC-Bench、任务/200K/token效率发布事实不自动成为新机制/评价盲点。接受当前限定关闭，不采用性能宣传，不追无关轨迹附件。 |
| Google两Blog，介绍事件层 | 实读`google-core-web.json`两原文核心：AlphaEvolve L104-163有限gadget/固定lifting框架与最终原始验证；PHA L104-163三角色动态编排、单体/并行对照及研究非产品反侧。接受没有另披露独立release/revision的Blog事件关闭，**不判原论文无贡献/已审窗外**；2509.18057/2508.20148 first-public缺口保持。医疗名称不是PHA关闭依据。 |

普通来源不全量读所有历史卡片正文；完整有界题摘已超过本轮要求的代表抽检，但不冒称全部125/整月全量Evidence。

## 4. 14source实际请求、停止与授权边界

实际检查本轮headers、native-recovery/last-fetch、两Advanced日志、四主题请求记录及必要原件；对结构化返回用JSON/ElementTree/HTMLParser，不按搜索参数推定过滤有效。下表是原件复核，不是独立重演14站抓取；必要新网络只定点打开R1三份官方abs。作者首轮15:09-15:12的记录与后续07:15-07:38 UTC记录保留，不虚构本复核执行那些curl。

| 来源 | 本轮独立实际核到的边界 | 裁决/限制 |
| --- | --- | --- |
| SRC-OPENAI | Research403；RSS1251逐项XML日期，Sep30三Sora、Oct1七case；Sora初始原件指纹 | 当前RSS切片及同事件去重成立，不授全站/整PDF历史首公开。 |
| SRC-ANTHROPIC | Flight JSONDecoder复现174对象/172身份，Sep30零；邻接BJT09/16与10/04 | 此返回数组成立，不是News全站零。 |
| SRC-GOOGLE-AI | 保存web归档首12卡Sep30两条后Sep25；两核心；DeepMind p2 L115 selection/30条，10/30→09/29；News p5及两个邻接原页10/06、09/25 | 有限Blog/selection成立；Google pubs当前列表与超时不能恢复历史日段，不授全Google覆盖。 |
| SRC-META-AI | 连接重置、web无有效列表；global_search page5打开实际400 Timeout | 真受阻，不把搜索片段/旧年结果记零事件。 |
| SRC-QWEN | API200/57428bytes、JSON60条全日期解析 | 按R2更正；有前后侧、无Sep30对象，但历史完整性未披露。 |
| SRC-DEEPSEEK | 保存News可见Research10项，10/21→05/14；News09/29；无Sep30记录 | 当前有限列表切片成立，非仓库全覆盖；“News最近09/29”须理解为目标日前最近，不是当前全列表最新（当前含2026）。 |
| SRC-MOONSHOT | 原Blog明确11/07、11/06→09/16及后续日期 | 越窗停止成立，非全部repo release。 |
| SRC-TENCENT-HUNYUAN | publicList真实API/POST字段记录，en total9/list9，zh total11/list11；全displayPublishTime2026 | 当前返回库存穷尽但2025缺段；没有AX/browser历史证据，不能写2025零。 |
| SRC-ZAI | 原p2累计18日期/末12/07“没有更多”；notes/core Sep30GLM身份 | Research历史缺段真实；具名release可独立关闭，不能以此填Research覆盖。 |
| SRC-BYTEDANCE-SEED | 原API4页、count20/page_token0/20/type1/2/year2025；JSON实际paper18+20、blog18+18，总94/45，IsPinned另读 | 非置顶papers10/21→09/22、blog10/23→08/21已跨窗，无Sep30目录记录；page20分别至05/20/02/12后止，不把94/45排队。PublishDate非原论文first-public。日志URL不显示US，本文只授实际返回的英文内容，不额外证明locale请求头。 |
| SRC-BAIDU-ERNIE | 两页实际日期卡10+6，末页上一页1/2；10/16→09/12 | 当前两页目录停止成立，非repo全覆盖。 |
| SRC-XIAOMI-MIMO | 官方async JS静态AST解析Paper8条，09/19→10/21；local More源码为现数组slice/toggle而非历史分页 | Paper切片成立；Blog无历史日期，不能以More或Paper完成填补。 |
| SRC-MINIMAX | EN/CN原日期卡10/27→CN01/15；Agent重定向原件只2026/05/13 | Blog有限切片与Agent历史缺段分开，非零事件证明。 |
| SRC-ARXIV | 两日路径400、月首25/2215、Advanced50/3126，同日200表单错误；四Atom159records/125ID | 下面日级隔离成立，绝不授本窗Coverage通过。 |

arXiv精确边界：

1. 同日正确CS checkbox查询的HTTP200原HTML第350行确为`End date must be later than start date`，不是有效空结果。两日路径400也不是0篇。
2. 跨日Advanced原query只勾`classification-computer_science_archives=all`，缺真正CS checkbox，不能称有效CS范围；页尾首公告只有年/月，没有Sep30日授权。当前v2 submitted2026本身也不是首公告过滤失败证明。
3. 四主题API以`submittedDate:[202509281800 TO 202509291800]`发现，复现models81/50、systems15/15、multimodal44/44、agents90/50，唯一125。该提交边界非公开窗口；Updated:v1、DataCite加公告日程均不补日证据。
4. 未请求models31、agents40明确是宽库存，不默认变成逐篇队列；但真实日批次标题补检和本窗召回仍未成立。外部请求应为2025-09-30官方announced/list与ID关联或具体作者/机构精确正文公开日证据；只有这些恢复后才按真实日批次定点处理，不能取当前API摘要充历史v1。

## 5. 原OpenAI家族与完成权限

实读原FIRST/FINAL非作者记录，保持其有效复核范围；当前正文没有扩大采用命题。旧七case仍为1个家族，日期`2025-10-01T08:00:00+08:00`及`2+1+2=5`原样保留；本輪RSS再次复现七个`Wed, 01 Oct 2025 00:00:00 GMT`。原纠错/安全深审及Books仅报告复用，不重新改分或搬入补充自然日。

Stop News是发布方自身2024 Category3→2纠错，不证明本项目曾采用错误分级或第三方调查已独立核验；Russian直接拒答与跨会话构件共存，不证明实际恶意组装/执行/攻击成功。当前候选仅授case页面日期，不授整份October PDF在Oct1 first-public或全文已审。原Ch66/Ch72最小命题未变化，本轮没有重做Books全章或POST，不把旧通过授补查完成。

**普通待办：** Euler落实R1-R4及目标日前News措辞收窄，更新潜力/关闭数与本輪独立校准引用；回传变化处作窄复查。未变化的74项潜力、18项关闭及机构有限范围不用无差别重读。日归属恢复后再开展对应精确版本Evidence/Books比较，校准通过不等Evidence通过。

**确切外部保留：** arXiv官方Sep30日批次/个体公开日、Google两原论文first-public、Google Research/Meta/Hunyuan/Z.ai Research/MiMo Blog/MiniMax Agent历史目标日段；Qwen是库存历史完整性未披露，不能仍写没有后侧。以上不支持正面候选/Books/无遗漏，必要恢复条件保持身份与范围。未取得日期无需泛读普通held附件；撤回三项不再把日期缺口当继续采用理由。

本文件仅授本轮首批准入校准与所列来源/排除复核边界，**不授DAY、年度分母或新Books整合验收**。没有新确认当窗家族、没有新评分/Books修改；新增发现是3项撤回排除、1项机制关闭重开及2项事实措辞校正。独立核验未覆盖普通18标题退出的完整摘要/附件、未请求宽库存、所有受阻历史段、原报告PDF全文或任何实验复现。

## 6. 写后检查

本轮唯一写入为本文件，保持未暂存；作者Report及其既有dirty状态、Books、State、合同、脚本、索引均不改。2026-10-07T16:04:05+08:00实际写后检查：本文件5个本地引用目标均存在、无尾部空白；新文件对空文件的`git diff --no-index --check`无诊断（有新增差异返回1）。当前10/01 Report V3校验通过，但语义复核仍按上面未通过处理。另限定11/01作者README的diff检查无空白诊断，root此前指出的标题尾空白已修。身份集合机械交叉核对：74项潜力表无漏项，原76中只另分离具名PoseDiff与AMemGuard；不授74项Evidence或公开日核验。
