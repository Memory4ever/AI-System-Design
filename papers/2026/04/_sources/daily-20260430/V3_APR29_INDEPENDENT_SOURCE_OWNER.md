# 04/30 有限非作者准入与 source→actual owner 复核

复核者：`apr29_close`，不是 04/30 报告或下列新 Books 段落的作者。范围限本日作者收口包、八份采用包与争议包，按当前 AGENTS/研究/Report 合同重读；不继承旧 Weekly 或旧完成标签。逐项对照必要原版方法、评价/反例和实际 owner；身份、版本与命题不变的既有 ROOT/APR01 审阅及写后记录复用，不无差别重读附件。本文是一次有限复核汇总，不代替最终来源覆盖、日期 Gate、实际新写后及正式 Report 日级验收。

结论：原拟 33 个家族保留；负侧 `26516` 的安全保证反例需要保护性恢复，成为 **34 家族建议集合**。作者已接受改判。其余七个具名排除项在下文有限范围内赞成关闭；不把这些抽检称为 1034 个库存的全量摘要/正文验真。17 个新 gap 的 source→owner 窄采用可成立，但尚未实写，不能登记整合；Ch66 三项仍等既有写锁释放。

## 34 项逐家族结果

以下论文链接均显式 v1；HTML 缺必要公式时仅定点补官方 PDF。三项实际整合与一项 Existing 的既有记录已核，不重新制造 diff。评分应由作者在正式报告绑定下列受限新命题，不能借已知原则、章节广度或 Books 处置加分。

| 家族 / 必要原始证据 | 实际 owner / 有限裁定 |
| --- | --- |
| [ZAI Scaling Pain](https://www.zhipuai.cn/zh/research)；本日 ROOT/APR01 原始研究 159 与写后记录 | `INFER-GPU-MEMORY` Ch54 LayerSplit 与 `INFER-PD-DISAGGREGATION` Ch55 Abort/RDMA retire；同一家族的两处实际采用，复用有效写后，不新增计数。 |
| [26340 DMEP](https://arxiv.org/html/2604.26340v1) | `TRAIN-LORA` Ch30；物理裁掉 expert 与 optimizer state，路由稳定后关闭 balance objective。原有效 source/写后命题未变，可复用实际整合。 |
| [26622](https://arxiv.org/html/2604.26622v1) | `AGENT-MEMORY` Ch77；视觉压缩状态先定位、原始日志再精确读取，压缩表示不能代替事实证据。原有效 ROOT/APR01 写后可复用。 |
| [26505](https://arxiv.org/html/2604.26505v1) | `PLATFORM-SECURITY` Ch72；同 batch 动态 per-tensor scale、共置和 logit 可观察条件已有具体正文，复用 ROOT_TWO_BOOKS_BOUNDARY_FINITE 的 Existing，不造新改动。 |
| [26039 RaMP](https://arxiv.org/pdf/2604.26039v1) §IV/§V | `INFER-TENSORRT-LLM` Ch49；同 compiled kernel binary、同路由结果的 histogram 可以决定 CTA/grid/tile/wave 配置，区别于 expert placement。认可两窄段；H200、vLLM eager、串行 prompt/full restart 不是并发 SLO。 |
| [26074 DAK](https://arxiv.org/html/2604.26074v1) §4.2–4.3/§6 | `INFER-GPU-MEMORY` Ch54；远端 host DRAM 经 TMA 直达 SMEM 可绕 HBM staging，逐 operation offload 比率与 inflight 主机拥塞独立约束。认可两段；GH200/C2C 与 Blackwell/PCIe 的路径不能混写为普适最优或零成本。 |
| [26557 DualBlade](https://arxiv.org/html/2604.26557v1) §IV–V | Ch54；同 layer K/V unit 在初始化绑定 page-cache 或 LBA-direct 路径，lazy materialization 与 pinned staging 需保身份/extent 边界。认可两段；不是 GPU-direct，DRAM-rich 时全直读反可慢。 |
| [26837 SPIN](https://arxiv.org/html/2604.26837v1) §4.1/§5 | Ch54；Index/Select/Attention 与 Offload/Retrieve 分责，逻辑容量 metadata 和活跃物理 page tables 不能同算。认可两段；pinned CPU 元数据 GPU 读取、检索及线上 TPOT 有成本，较大 batch 可劣于 dense。 |
| [26256 DORA](https://arxiv.org/html/2604.26256v1) §3/§4.2–4.4 | `TRAIN-GRPO` Ch33；每组固定 policy version，较大 rollout 池先消费完整训练批，旧版本长尾继续收集；全部轨迹完成/转交后才滚动窗口。认可两段；保 group membership/behavior logprob，不把随意丢部分组说成 objective 等价，KV 移动须同权重。 |
| [26779 NeMo Speculative](https://arxiv.org/html/2604.26779v1) §2–3 | Ch33；policy hidden state detach 后更新 draft head，draft 生命周期与 policy objective 分离。认可两段；acceptance 高不保证 wall-clock 快，ngram/长 draft 负例及异步投影不冒称实测。 |
| [26378 CoQuant](https://arxiv.org/html/2604.26378v1) §3.2/§4–5 | Ch49；联合 W/A 输出误差 surrogate 导出被高精度保护的子空间，区别于现有权重敏感度 allocator。认可两段；小误差/AQNM、丢二阶交互及 isotropic proxy 跟随，不称实际混精 kernel 已加速。 |
| [26274 Praetor](https://arxiv.org/html/2604.26274v1) §4.1–4.2/§5 | `PLATFORM-SECURITY` Ch72；从可信轨迹编译正向工具调用 pDFA/参数 profile，执行前按 session 状态校验，拒绝不推进状态。认可两段；O(1) edge lookup 不是全检查时延，profile 污染/合法路径恶意参数及结构攻击有限样本边界保留。 |
| [26102 SWE-Edit](https://arxiv.org/html/2604.26102v1) §3.1/§4.2 | `AGENT-WORKFLOW` Ch81；Viewer 负责完整文件中相关片段、Editor 负责格式化修改，二者隔离 context 噪声和 edit-format failure。认可两段；provenance 是工程要求而非论文完整实现，Editor-alone 成本负例保留。 |
| [26197 HLTM](https://arxiv.org/html/2604.26197v1) §3.2–3.7/Table2 | `AGENT-MEMORY` Ch77；业务实体树共同承担授权子树、聚合范围和 ancestor invalidation，而非普通语义聚类。认可两段；LLM parent/“lossless”不证事实完整，precision/完整 recall 负例与权限动态更新边界保留。 |
| [26294 TSP](https://arxiv.org/pdf/2604.26294v1) §III/§VI | `TRAIN-DISTRIBUTED-TRAINING` Ch36；同一 D 轴同时存 weight 与 sequence shard，Attention/MLP 分别采用相应 broadcast/allgather/ring，非 TP×SP 正交 mesh。认可两段；更多通信/recompute/topology 成本跟随，不推广作者特定 forward/training 配置。 |
| [26604 Who Trains](https://arxiv.org/html/2604.26604v1) | Ch36；population enrollment 与每轮参与是两层抽样，已到 update 重加权不能消除未加入 population 的支持偏差。认可一段；mean-ignorability/positivity、已知 inclusion 与 calibration 充分性不得省，合成 logistic 非 LLM 集群结论。 |
| [26694 XWAM](https://arxiv.org/html/2604.26694v1) §3.3/Algorithm2/Table4 | `MULTIMODAL-EMBODIED-VLA` Ch26；动作更早去噪并冻结、视频继续去噪要求训练覆盖该异步路径。认可两段；同延迟消融与 sequential 质量/成本对照保留，时间分布不等于所有离散采样路径或物理安全。 |
| [26836 UPSi](https://arxiv.org/html/2604.26836v1) §5.1–5.3/§6 | Ch26；整条预测 state-action 除 reachable/unsafe 约束还须位于 ensemble certain set。认可至多两段；初始 robust backup、保守噪声/无偏均值、单调改善/Lipschitz 跟随；K=0/零 Lipschitz/soft constraints 实验简化不具原形式保证。 |
| [26052](https://arxiv.org/html/2604.26052v1) §3–4 | `PLATFORM-EVALUATION-SYSTEM` Ch66；独立 prompt/response 标签的双向风险转移是实际差额。认可两段但未授权占用 Ch66；条件分母 `P(prompt safe | response harmful)` 不得改成另一方向，单轮英语人工样本不是因果比较。 |
| [26180 Evergreen](https://arxiv.org/html/2604.26180v1) §3–5 | Ch66；claim 的量词/聚合查询决定 evidence tuple、stopping 与 provenance。认可两段但等锁；universal witness/counterexample 与带容差 CS 估计必须区别，exchangeable shuffle/多重 budget 与 predicate 误差保留，不把近似 bool_and 当确切全称真值。 |
| [26511 Tatemae](https://arxiv.org/html/2604.26511v1) §2–3 | Ch66；中性、压力及声明监控条件配对，区别能力缺失/压力/监控恢复。认可两段但等锁；JSON/XML 工具选择非实际 effect 执行，理由标签不证明隐藏欺骗意图。 |
| [26209 HPD](https://arxiv.org/html/2604.26209v1) §4–6 | `INFER-SPECULATIVE-DECODING` Ch48 对照路径；条件独立字段可改变 joint factorization，逻辑位置 mask 不能按物理 cache 追加顺序。保留标准/仅报告：受限 AVE 输出协议，不是原 AR sampling-law 保真或通用替代；目前不足改写通用验证链。 |
| [26508 MetaAE](https://arxiv.org/html/2604.26508v1) Eq7–11/TableIII | `MULTIMODAL-REPRESENTATION` Ch23 Edge split；progressive latent 的质量估计控制传输有条件设计增量。保留标准/仅报告：TableIII 在 1Mbps、100% LTL 测 E2E，不是在线停止策略单因子因果验收；reconstruction/error head 不拥有下游 truth。 |
| [26649 ReaLM-Retrieve](https://arxiv.org/html/2604.26649v1) §4.1–4.5/§7.5 | `AGENT-RAG` Ch76、Ch77 交接；logical reasoning-step checkpoint 决定何时 evidence injection，开放权重 prefix KV 与 completion-only refeed 是不同成本。保留标准/仅报告：边界分类器和 proxy 不是真值，三 QA 的受限 OOD/overhead/多次注入退化不足新增长期 authority。 |
| [26848 STARRY](https://arxiv.org/html/2604.26848v1) §3/Table4 | Ch26；geometry 专家仅调 action→visual attention，不能升级为 video/semantic truth。保留标准/仅报告：同表示 GASAM 开关有局部增量，但现 action proposal/read/independent controller 已承载责任，不为局部 actuator 强造正文。 |
| [26167](https://arxiv.org/html/2604.26167v1) §3–6/Algorithm1 | Ch72；token 不变但连续输入 embedding 每请求已改变。保留保护性深入/仅报告：当前 soft-channel artifact/activation 与独立 effect gate 可承载身份要求；同 moderation oracle 同时优化和 Flagged 评价不证安全，text-only API 不适用。 |
| [26391](https://arxiv.org/html/2604.26391v1) §II–III | Ch36；异质保护/共谋集合×两跳拓扑改变通信/相关密钥率。保留标准/仅报告：独立均匀有限域、预置 key server、无误广播与诚实好奇模型不支持真实 FL 掉线/版本/非IID及生产协议替换。不是因理论标签关闭。 |
| [26706](https://arxiv.org/pdf/2604.26706v1) §2–5/Theorem1 | Ch66；fixed-target CI→selected-target noncoverage 加平均 TV/MI 泄漏界，带噪 screening 是独立 holdout 之外的受限设计。保留标准/仅报告：联合律的设计上界不能由一次 leaderboard 后验估计，Gaussian 例不验证 release safety；界超过1无效用。 |
| [25931 PHC](https://arxiv.org/html/2604.25931v1) Theorem1 | Ch66/RAG 交接，争议/Books 暂缓；“任意 post-generation U 的信息不低于 pre-generation g”在 U 为常数时不成立，DPI 不支持该比较方向；局部 PHC 诊断/GraphRAG benefit 保留，不正面采用普遍保证。 |
| [26130 Reward Lens](https://arxiv.org/pdf/2604.26130v1) Eq3/AppendixB、D | Ch31，争议/暂缓；最终 LayerNorm 非线性，不能通用吸收到线性 head 并分解各 residual。作者 exact sanity claim 与当前构造冲突保留，未执行代码不称已复现/断言通过。 |
| [26525 PRAG](https://arxiv.org/pdf/2604.26525v1) §VI.4/Appendix、Algorithm3 | Ch72，争议/暂缓；score gap 小于2ε仅允许翻序，bounded error 不推出近随机排名；零误差即反例。virtual weighted node 的可遍历映射也待明确；不将此扩大为全 CKKS 安全定义被证伪。 |
| [26467 DPGCL](https://arxiv.org/pdf/2604.26467v1) Theorem2/AppendixA | Ch72，争议/暂缓；随机重分组与相邻数据中所有未变 pair 同组的证明耦合不自动兼容。组大小2的原两项加入第三项后边界足以暴露缺桥；不是已构造 DP 泄漏攻击，稳定分组/accountant 可重开。 |
| [26809 AFUIC](https://arxiv.org/html/2604.26809v1) §III/Algorithm1 | Ch72，争议/暂缓；旧 snapshot unlearn 结果覆盖 current global，未定义 retained update 的 merge/replay/CAS；旧0→当前1→覆盖0 是有限丢更新反例。augmentation KL 一致不能单独证明删除，保留受限实验。 |
| [26516 SAS](https://arxiv.org/html/2604.26516v1) §2.2–3.2 | Ch26，新增保护性争议/暂缓；见下节有限安全反例，不能按 prompt/VAE 共模旧覆盖直接排除。 |

## 负侧校准与一次必要恢复

`25975` 的 §3.2–3.5 在 linear-Gaussian surrogate 下得到 logdet，实际 leverage/历史 query proxy 又做近似；对读 Ch45 future-query 质量、selector/kernel 成本和 FullKV 回退后，赞成当前贡献前关闭：不把 surrogate 信息量等同真实 Attention 的质量证明，没有使现存 eviction 选择翻转。`26103` 的 §7 将 ScaleSim/AstraSim 与 H100 profiling 拼接，Rubin 为投影，只覆盖 Attention 路径；MLA 长序列的反胜修正受限设计空间，但 Ch49 已按完整执行/compute-memory-fabric 分支验硬件，赞成当前关闭，不因小规模或模拟本身排。`26821` 的 bank placement/row-buffer conflict、core groups 是真实编译硬件协同分支；对读 Ch49 execution plan/物理路径与仿真边界后，赞成当前关闭，不把设计空间数字当独立长期选择证据。`26768` 的 frozen task 与 document LoRA 软/硬正交是真训练配方；Ch77:856–862 已有共享 reasoning/可寻址文档事实分权，Ch30 composition/admission 已要求行为重评。软罚可因 A/B gauge 缩放变小而函数不变，硬投影可裁有用方向；赞成关闭，不把参数几何当语义独立证明。

`26688` 交错 belief-DFA 构造与 game solving 是真实算法差额，但有限布尔隐藏变量/realizability 合成并未给当前 Ch26:1103 的已给 automaton 检查或 Ch84 开放 effect 新的实际选择；赞成具名关闭，不笼统拒绝形式方法。`26288` 的人类注释是有意识光标而非 eye gaze；受控 saliency 相关下降和 hint 在已正确正常样本引入 hallucination 已核。当前 Ch23 sensor 与 Ch66 独立 outcome 分权已承载它强化的限制，赞成关闭，但保存负证据，不称注释带来内部注意对齐。`26324` 给缺类别客户端新增 synthetic 支持而非到达梯度重加权，确实不同；Ch27 synthetic source/mixture/质量与 Ch36:1149 缺支持共同负责既有选择。仅类别条件 generator、设备域未进生成条件、无预训 F1 反向与未证明隐私不足形成新的独立 owner 责任，赞成关闭，不因医疗标签关闭。

**`26516` 从排除恢复为争议候选。**§2.2 Eq4 把 occupancy 下界与 concentrability 当 CMDP cost 安全充分条件，但未提供 cost–density 的必要联系；同一支持/高密度可赋高成本，使密度门槛成立而成本超预算。更直接的 §2.3 折扣条件 `G≥γ E[min G']` 不能推出作者紧接的逐路径 non-increasing 或不逃 `R_c`：令 γ=.9、当前 G=1、唯一后继 G'=1.1，则1≥.99成立，却逃出 c=1 的 sublevel set。加入平衡点0/其他点正值也不排除这一局部转移。此反例只否定相应推导桥，不宣布全部受限 SAS 实验无效；density/prompt/VAE 回路仍可作 heuristic，不进 Books 安全保证。重开需真正未折扣逐路径下降/barrier 或明确 cost–density 关系与模型误差条件的修补证明。作者已同意34家族与隔离，不删除原实验反证。

## 采用授权与未完成范围

17 新 gap 的上述内容已逐批发作者，除 Ch66 锁待释放外按列出的段数窄写；Ch49/72 的 Apr29 窄段已经 root 写后通过并释放，不挡 Apr30 不冲突增量。作者负责实际写入、Report 六部分及处置矩阵，写后必须由非写入者检查正文、前后衔接和边界，未写前不能算整合。Evergreen 特别禁止把带容差/随机顺序估计的全称判断写成 exact truth；所有 kernel/安全/控制材料保留对照、代价及 fallback。

本次没有新增扫描机构或全学科入口，没有改日期、共享索引或 LEARNING_STATE，没有改 Apr30 正式报告或新 Books，没有 stage/commit/push。日期组合、八条历史入口及具名窗外/首公开隔离继续按本日既有记录独立验收；本文不宣称来源零遗漏。最终日级结论仍为**未验收**，普通剩余至少为17实际写入及写后、34行正式报告和来源/日期/日级 Gate。
