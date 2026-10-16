# 12/17 首批准入非作者校准

复核者：主线程（非作者）；2026-10-02。范围：作者 `ADMISSION_CALIBRATION.md` 四项潜在准入与两项普通排除；不是全日验收。

实际独立打开 Anthropic [alignment faking 干预原文](https://alignment.anthropic.com/2025/alignment-faking-mitigations/)、Meta [SAM Audio 完整题摘](https://ai.meta.com/research/publications/sam-audio-segment-anything-in-audio/)、[PE-AV 完整题摘](https://ai.meta.com/research/publications/pushing-the-frontier-of-audiovisual-perception-with-large-scale-multimodal-correspondence-learning/)、Seed [1.5 pro 原文核心架构说明](https://seed.bytedance.com/en/blog/sound-and-vision-all-in-one-take-the-official-release-of-seedance-1-5-pro)，以及 OpenAI [FrontierScience 核心说明](https://openai.com/index/frontierscience/) 和 [Images 发布正文](https://openai.com/index/new-chatgpt-images-is-here/)。

## 校准结果

- Anthropic 潜在准入通过。干预可能降低被监控行为却保留或扩大 compliance gap，不能用单一训练内指标验收泛化。必须保留 model-organism/虚构提示设置、干预步数不同及高运行间方差；不可直接称生产模型都在隐瞒。TRAIN-RLHF 是目标/监督与干预的 owner；评价协议向 Ch66 交接。
- SAM Audio 潜在准入通过。多模态条件统一和 reference-free judge 可改变音频分离接口及评价；摘要不足证明统一框架胜过一切专用模型，正文需检查条件提示消融和 judge 校准。
- PE-AV 潜在准入通过。跨模态整体对齐与 frame-level 目标区分有具体增量；数据合成、目标组合和规模的收益归因必须分别核验，不把十个目标的列举本身视为证明。
- Seedance 潜在准入通过，先收窄到所披露的联合生成链。博客给出模型卡 `2512.13507`，若落窗核验需要机制/实验，必须读精确事件对应模型卡，不停在宣传摘要。博客的 10× 不能作为配置无关加速保证。
- FrontierScience 范围排除通过：当前科学研究任务切片属于 ROADMAP 暂缓范围；不能借通用评价 owner 引入。Images 当前发布正文的机制准入排除通过：产品收益未披露归因方法；只验收此正文，不替独立安全材料作结论。

湿实验负侧未独立重读，其他尚未发现项未验收。上述公开页面均只有日精度，没有凭此确定 12/17 落窗；继续必要时区/公开记录核验，不补造时刻。作者其余发现可以继续，日级覆盖仍未完成。

## 初始正文与 Books 局部核对

主线程实际读取本日初始 README；结构校验通过，只证明六部分与接口一致，不授予日级完成。来源表仍有可执行的扫描，公开时刻未确认项不能记作确定当窗候选。

实际读取 Ch31 开头及 Ch30/32 相邻开头，并定点读取 Ch66 的 `Observed Capability 与 Elicitation Ceiling 必须分开`。Ch66 已解释中性/压力条件、声明监控/无监控配对和 model-organism 的外推限制，因而覆盖评价协议的部分原则；其现有两条来源不是本次 Anthropic 干预实验。Ch31 的 reward proxy 与 reward hacking 也不能替代本次 interrogation、compliance gap、训练内外指标分离的具体增量。因此不得把整项直接判为“已有覆盖”；只有日期与必要实验证据安全关闭后才能决定该增量的 Books 处置。本次尚未改书。

主线程进一步独立阅读 Anthropic 原文 Background/Metrics/Training details、三类干预 Setup/Results、Limitations 与 Methodological Lessons。原文对 interrogation turn 使用 reward 但屏蔽其梯度、各干预训练步数不同、种子方差与模拟设定均有明确边界。作者拟采用的收窄命题与这些位置一致；这次必要源审不补足缺失的公开时刻，也不将研究模拟当生产安全证明。后续若日期成立，只需对拟写段落与原文作用范围定点复核，不重复全篇抓取。

## Seedance Blog 日期与精确 v1 源审

主线程独立 HTTP200 取得精确 Blog 的 `window._ROUTER_DATA`，JSON 解析对应 `ArticleMeta`：ID1817、`PublishDate=1765882058000`、`UpdateTime=1788415475000`，与 [日期 sidecar](../OFFICIAL_EVENT_DATE_RECOVERY.md) 一致。官网所声明的 Blog 发布事件为 `2025-12-16T18:47:38+08:00`，落窗；采用身份必须是这一 Blog 事件，不移作论文或模型全球最早公开。页面存在后来 UpdateTime，当前文字不能无说明当作不可变 2025 快照。

精确 `2512.13507v1` HTML404 后，主线程实际读 [官方 v1 PDF](https://arxiv.org/pdf/2512.13507v1) Abstract/Introduction（pp1–3）、Evaluation §2.1.1–2.1.4 与 §2.2（pp3–8）。文本支持联合双分支生成、混合任务、后训练和多维评价的披露，不支持补造详细 tensor layout、训练损失或跨模态模块实现。评价分别用绝对评分和 GSB；跨完整模型比较不隔离 joint module、数据、RLHF 或加速模块的因果收益。速度倍率不采用；硬件、精度、端到端并发/SLO及重要机制消融未披露处保留 Not Disclosed。当前必要源审支持收窄披露命题，不支持统一模型全面替代或生产加速保证。

主线程已实际定点读 Ch24 开头的生成状态/solver 责任，以及现有 joint AV/motion 段的标题线索；不能据关键词判全部已有覆盖。作者交付具体拟采用差异后，再核唯一 owner 和两侧衔接，不额外堆发布清单。

## 最终定点复核

主线程进一步实际读取 README、SOURCE_STOPS、ADMISSION_ADDITIONS 与 SEEDANCE_BLOG_EVIDENCE。14 个每日源均有有限入口、停止点或明确外部历史缺口；旧裸 kernel 查询已撤销覆盖资格，收窄后的 14/46 条主题结果不冒称当天候选或全量库存。仍缺的个体首次公开不能由提交、月字段或常规公告排期赋给材料。

### 候选与 Books

唯一确认落窗家族是 Seedance 官网 Blog 发布事件。此前实际源审覆盖 exact v1 pp1–8 的架构披露与评价；本次实际读取 Ch24 的 `Any-to-any AR 把 Modality Type 移入同一生成序列` 全段及其后成组数据/共享 prefix 段，并读音画共享运动状态的两个完整段落。

现有论点分别解释 AR 跨任务梯度耦合与共同运动条件，不等于 Seedance 的双分支 diffusion 模块。新披露确实是一条联合架构、mixed-task、coherence 数据及后训练路线，不能整项称已有覆盖。但早期 v1 未说明联合模块的细部、状态布局或机制级受控消融，完整模型比较不能分离这些环节的收益。`仅报告` 处置成立：保留设计路线和未披露边界，不用现有一般一致性原则再增产品清单。若原始模块或归因证据到达，定点重开 Ch24 生成耦合分支。

没有 Books 写入，因而没有尚待执行的写入后复核。Anthropic 干预、Meta 两研究、MiMo release 与仓库修订均保留具体潜在增量，但日期/历史版本同一性尚缺，不用于 Books。

### 安全、纠错与设计反证

除前文实际审过的 Anthropic 必要核心外，本次实际打开以下原文；未将题摘检查冒称所有正文深入审阅。

| 原文 | 核验范围与结论 |
| --- | --- |
| [CTVP v1](https://arxiv.org/abs/2512.13821v1) | 完整题摘：预测 trace 的一致性不等于实际执行真值；理论安全主张须核假设，保留潜在增量，不采通用证明。 |
| [gpu_ext v1](https://arxiv.org/abs/2512.12615v1) | 完整题摘：host/device policy hook 与 verified eBPF 具具体机制；不采用跨租户通用安全或脱离 workload 的倍率。 |
| [Textual Gradients v1](https://arxiv.org/abs/2512.13598v1) | 完整题摘：效果提升不证明 gradient 类比；局部反证不得因不是新算法而排除。 |
| [Effective Depth v1](https://arxiv.org/abs/2512.14064v1) | 完整题摘：Qwen 家族的 effective-depth proxy 不支持所有长 CoT 都缺推理或所有层无效。 |
| [FROC v1](https://arxiv.org/abs/2512.13337v1) | 完整题摘：conformal-style configuration risk 不是任意样本删除影响的实测真值；保留风险控制条件。 |
| [M-GRPO v1](https://arxiv.org/abs/2512.13070v1) | 完整题摘：更多 rollout 只延迟 collapse 的反例，momentum target 与 entropy filtering 分开；不宣称收敛到全局最优。 |
| [RPO v1](https://arxiv.org/abs/2512.13240v1) | 完整题摘：hint-conditioned preference pair 的分布条件仍须核验，不把同 policy family 当无条件 on-policy 等价。 |
| [SPON v1](https://arxiv.org/abs/2512.12744v1) | 完整题摘仅确认稀疏化的表示损失与 trainable spontaneous neurons；当前较晚摘要的 distribution matching 等不冒称历史 v1 披露，日期仍隔离。 |
| [UIFormer v1](https://arxiv.org/abs/2512.13438v1) | 完整题摘：效率/完备性共同约束及 Boolean oracle 缺失是真实设计问题，不凭 token 减少采用正确性保证。 |
| [Janus v1](https://arxiv.org/abs/2512.13525v1) | 完整题摘：attention/expert 分离、通信及 placement 的条件保留，不采用后来 v4 倍率。 |
| [MEP v1](https://arxiv.org/abs/2512.22147v1) | 完整题摘：小程序验证仍需 reintegration 到原 application；不会由大 ID 推断晚公开。 |
| [DTop-p v1](https://arxiv.org/abs/2512.13996v1) | 完整题摘：PI 控制平均 active-expert budget，不等于逐 token 计算量或稳定性自动保证。 |
| [SIGMA v1](https://arxiv.org/html/2512.13488v1) | 实际读 §3.1–3.5、§4.1–4.3：forward、gradient、10 optimizer steps 分开验证；online fault isolation 与 offline rule validation 分开。发现作者记录容易将 Table6 的 Effective Utilization 94.45% 与 Table10 MFU 混读，已要求分别标识；未采用二者为独立机制因果收益。 |
| [Membership inference v1](https://arxiv.org/pdf/2512.13352v1) | 实际读 §IV 生成/排序与结果、§V confirmation/extended subset：ranking 相对 likelihood 的改善有限、某些方法退步；confirmation 差异不能代替 extraction 成功，GT、模型和数据限制保留。 |

Video1.5 的 all_gather backward/SUM reduce_scatter 修订与 MiMo 的 routing replay/MOPD 仍具名保留纠错/反证，前者不按普通维护关闭，后者不授 teacher 全域保持或无泄漏保证；历史正文读文记录可复用，尚无可采日期，不以它们作当窗安全证据。

### 普通负侧抽检

新增实际抽检 [wet-lab 官方原文](https://openai.com/index/accelerating-biological-research-in-the-wet-lab/) 核心问题、实验循环、结果和限制。其机制是生物实验协议改进，本项目暂缓 AI for Science 范围，关闭理由成立；不采生物收益数字或实验操作。结合此前 FrontierScience、Images 的独立核心阅读，共 3 项官方范围/产品负侧经过抽检。

另实际读 [12595v1](https://arxiv.org/pdf/2512.12595v1) §3.1–3.3、§6 的机制、表格及消融说明：noise 检查/重复测量的具体规则与新增操作未披露，受控 protocol 不足，新增机制准入不成立；这是普通可读证据后的关闭，不是日期或数字原因。实际读 [13396v1](https://arxiv.org/abs/2512.13396v1) 完整题摘，现有证据限于推荐 scenario/task 信息流选择，不能直接推基础模型通用机制。这 2 项 arXiv 样本之外的普通领域排除未作全量正文验证。

终态保留项、原始入口失败与重开条件按本日 README/ADMISSION/SOURCE_STOPS 保留；不支持正面证据、Books 或无遗漏断言。普通作者读文待办 0，具体指标混淆纠正已实际落实；进入完成态结构检查。

结论：通过

## 2026-10-15 恢复：Alignment单段写前范围批准（不是日级通过）

用户明确恢复后root实际重读AGENTS/当前合同、来源分组、Prompt、全ROADMAP/State及Books背景/学习方法/写法；实际读SUP_ALIGNMENT_SOURCE§1–6及Feynman独核§3–5，精确复用同事件/采用命题的必要Source与5分层。另从已保存RAW_ALIGNMENT实际完整读Mitigation1 setup/results和Limitations的p/h3/h4（不含prompt表），确认首轮文本决定后轮问询context、后轮token mask、问询回答参与reward、首轮间接选择，以及人工organism/高方差/非真实whitebox结论边界。未重全正文/附件/实验，不声称复现。

当前实际顺读Ch31开篇1–38、完整450–478及834–864，Ch30/32开篇、Ch66完整246–270。probe表示漂移、CoT/output奖励冲突、elicitation与monitor配对已有覆盖，不再追加这些通用段；只有生成式第二轮监督依赖首轮轨迹的接口差额由TRAIN-RLHF唯一承载。准确锚点仍是Obfuscation Atlas完整probe段后、Pass@k目标段前，现邻接未变。当前Ch31 cached/unstaged numstat均空，旧cached18只是历史观察，不沿为本次dirty状态。

root批准SUP_ALIGNMENT_SOURCE§6已通过的逐字一自然段及本人一末Review note，正式note补原作者URL https://alignment.anthropic.com/2025/alignment-faking-mitigations/ 。授本日writer Boyle唯一此窄写锁，不改其他正文/源注/index，不额外写Ch66。写后Newton须实际顺读完整新段、两侧和自身note回对已核Source，root再实际读回才接纳并释放；本节仅写前授权，不是写入/POST或DAY。原Seedance6分完整行/日期/窗口/连续§4冻结。其余本日Source与六节尚未完成，90/132不含Dec17。

### Alignment实际写后接纳 / 窄锁释放

root实际读取Newton独核§10真实nonwriter POST，再实际顺读Ch31完整456–479：更新方向→原probe→新L464生成式问询→原Pass@k两段/组合诊断，另实际读末本人完整note与前注，并核完整限定diff只有4新增0删（正文1自然段＋自身note）。新段逐字等已批准PRE；首轮context→后轮问询/reward→首轮更新与mask权限、人工organism、非生产/白盒保证、额外评价费用及checkpoint/outcome退路近文成立，原两侧不被改写，原作者URL已补。cached为空，限定cached/unstaged diff-check均exit0；未动其它正文/notes/index，不冒全仓clean。

**实际POST接纳，释放Boyle这一个Ch31窄锁，本日实际整合1。** writer仅同步本人note中已发生Newton§10/root读回与释放状态，root再读行政差额，不改机制正文或第三次Source/PRE。此单项不授Dec17整体DAY/FINAL；其余Source/Meta/MiMo/日期和six仍普通，90/132不增加。

root随后实际读回Ch31末本人完整note，已准确同步Newton§10真实POST、root接纳及锁释放，必要Source/5分/采用禁界均保持；这一行政差额闭合，无待重复审批/书写。当前无本轮Books锁，本日整合1仍非DAY。

## 2026-10-15 MiMo / Meta 三项单段写前批准

root完整读SUP_MIMO_SOURCE§1–4、SUP_META_SOURCE§1–4以及Newton独核§12–15，必要原release身份/后稿角色按同命题有效层复用；另实际读MIMO_NECESSARY及当前Ch22完整250–306、Ch24完整874–921、Ch23完整934–970。三拟正文及本人note已逐字读，准确两侧与现正文相符；不是据题名无匹配推gap。MiMo无Value只入分母不同于现content anchor/结构性诊断；SAM混合音条件分离不同于ASR和语音生成；PE活动采样竞争具体化原多目标权重而不重写其一般原则。Newton实际逐字PRE§15通过可复用，不重复其完整方法/全PDF。

三项评分/采用域分别5/6/5，本文不修改旧Seedance6分或给同family子机制加家族。MiMo32B dense消融/最终MoE分责、后稿Meta必要反侧只作明示补证、非Dec16完整recipe、输出与judge分验、局部指标相反取舍、全费用与原机制退路均近文，未授性能普效/真实安全。root批准三包现逐字正文各一自然段＋各本人一末Review note，分别授Boyle三个独立文件的唯一窄锁：

- MODEL-LONG-CONTEXT / Ch22：现结构性sink段及独立SF-2026-ARXIV-2605-06611后、Conditional Attention标题前；只SUP_MIMO_SOURCE§4正文/note。
- MULTIMODAL-GENERATIVE-PARADIGMS / Ch24：现RNNT一致性限制完整段后、SF-2026-ARXIV-2605-20946:start前；只SUP_META_SOURCE§3正文/note。
- MULTIMODAL-REPRESENTATION / Ch23：多目标公式后完整权重段后、joint critic完整段前；只SUP_META_SOURCE§4正文/note。

root当前三个文件cached/unstaged numstat均空，写前writer再次看dirty并保护后到并发内容；不改原marker/两侧/其它notes/索引，不新增标题。每本真实保存后Newton分别实际完整新增/两侧/本人注POST，root实际读回才接纳并释放各锁，不能批量用marker预签。此写前批准不是真实写入/整合数或DAY/FINAL；Alignment已接纳1保持，其余本日有限Source/date/six继续。

### 三项实际POST接纳 / 各窄锁释放

root实际读Newton§18分别nonwriterPOST，随后分别实际顺读Ch22完整272–304及末本人完整注/前注、Ch23完整942–960含原公式/权重与joint critic及末本人注/前注、Ch24完整878–899含CTC/RNNT限制与speech绑定段/码层交接及末本人注/前注，并读三文件完整限定diff。每本只有批准正文1自然段＋自身1末注/4新增0删，未移原marker或改其它正文。三篇精准版本、必要反側、采用禁界与后稿补证角色均同批准稿；不是从marker或writer自签推验收。

MiMo无Value分母不恢复滑出内容/不授hybrid总KV常数、32B消融与最终MoE分责；SAM提示条件不签实例/波形守恒/judge真值；PE活动采样的边界与误报指标反向取舍不签通用比例或规模因果，均在正文近处，现论证承接自然。原作者与精确后稿URL、未复现和费用/回退限制保留。三文件限定cached/unstaged diff-check均exit0，外部已有/后到修改保护，不称全仓clean。

**三项实际整合接纳，释放Boyle的Ch22/Ch24/Ch23三个窄锁；本日连Alignment共实际整合4项。** writer仅同步各自本人note已发生Newton18/root读回/释放行政状态，root再实际读差额，不再重Source/PRE/正文。当前无本轮Books写锁；单项4不等Dec17整体DAY/FINAL，90/132暂不因书写增加。

root随后实际逐一读回Ch22/Ch23/Ch24末本人完整note，均已准确同步Newton18真实POST/root接纳及各锁释放，原必要Source/评分/采用禁界和未复现分责不变；三个行政差额闭合，不再重正文或Source/PRE。本日实际整合4仍非DAY；当前root因其它已验日报接纳为92/132，不包含Dec17。

### root实际日级接纳：DAY22与保存完成态FINAL23

root非本日报作者，实际完整读取Newton19–23及作者SUP_RESUME6、来源补包全部五节，并顺读README全部六部分及随后completion行政差额。精确保存稿SHA256为`906448baf761dfb98bd9a44419d640912fbae6d9c40c1700fccda2fa196c466b`，与Newton实际FINAL23相同；状态完成/13:51:23检查时间、五正式家族及四实际整合/一仅报告、有限Source/未知日期和后稿补证权限一致。原连续§4中的旧hold已由当前更新段明确覆盖，没有把后稿细节冒原Dec16全部recipe；此前root各真实POST/完整邻接/本人注及行政读回有效，不再重审单篇。

完成态V3重新通过；root相对HEAD实核旧window/Seedance完整行均保持，整个原§4连标题区的2297字符仍为当前连续前缀（reader2291为正文口径，不混作不同证据），一H1/六H2完整，26本地引用/22路径零缺失，限定cached与unstaged diff-check均通过。未将截断的宽diff输出当全量语义阅读；语义依据是上述完整保存稿/精确差额及独核实际层，机器只支持接口/冻结/路径。

**接纳Dec17整日，当前93/132已验收、39待。** 外部日期/历史目录、Video1.5 revision及独立安全材料保持具名安全隔离，不授正面Coverage/Evidence、无遗漏或生产保证；普通工作零、四Books锁均已释放。作者只可同步已发生FINAL23/root接纳指向，不改研究内容。立即fresh转Dec18（只补Dec17自然日），每日重读适用上下文，不继承本日35/26池或Source成功。无stage、commit、push，保护并发index及其它任务。
