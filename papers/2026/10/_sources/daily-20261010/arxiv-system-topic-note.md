# 2026-10-10 系统主题准入与必要证据停点

范围：2026-10-09 北京时间自然日；执行者 live1010_topic，仅负责本文件，报告由 live1010_author、Books 由 root 负责。已完整重读当前 AGENTS、RESEARCH_CONTRACT、REPORT_CONTRACTS、每日来源与 arXiv 主题规则、Prompt、ROADMAP；LEARNING_STATE 最新历史路由为暂停，不执行历史。宽官方列表只作有界查漏线索，不建立整类队列。

## 第一批七家族完整题摘初筛

官方当日公开列表 `arxiv-official-titles.json` 的 `Fri, 9 Oct 2026` 日期段包含七项 v1；本执行者逐项读取 current 官方 abs 完整题摘与当前说明，均只有 v1、未见撤回/更正/先稿身份信号。submitted 2026-10-08 是提交日期，不用于公开归属；公开归属采用官方公告 2026-10-09。未把“未见信号”扩写成完整历史搜索已证无先稿。

| 精确版本/原文 | 原约束 → 摘要实际增量 → 改变的设计选择 | 初筛/拟评分/必要审阅 |
| --- | --- | --- |
| [Zepp 2610.11158v1](https://arxiv.org/abs/2610.11158v1) | MoE EP 常将均衡本身作为目标 → 把 GPU/NIC balance 当约束，联合副本placement、流split/merge、计算重排和权重movement直接压瓶颈通信 → 单维均衡可损害总执行成本，不该等同最快服务 | 准入 2+2+2=6；标准，性能条件必要；拟 owner INFER-DYNAMO，固定 expert choices 的 runtime EP，不是模型 router |
| [DynaTE 2610.11284v1](https://arxiv.org/abs/2610.11284v1) | dLLM 所有token并行执行与不等utility/依赖失配 → token skipping、局部dependent refinement、可重构PE/streaming vocab协同 → token动态执行不能只看算术节省，须检验serial/irregular overhead是否被硬件隐藏 | 准入 2+1+2=5；标准；拟 owner INFER-TENSORRT-LLM，Ch24 只交接，不双 owner 展开 |
| [QUILT 2610.11134v1](https://arxiv.org/abs/2610.11134v1) | 各query独立执行会重复读取与反量化共同KV → SCSD regularization、hierarchical sharing及tile-aware query-tail修剪 → sparse支持集合与共享tile利用率要联合设计，但修剪是近似算法改变，不等同纯kernel执行优化 | 准入 2+1+2=5；标准；拟 owner INFER-PREFILL |
| [PageWeaver 2610.11201v1](https://arxiv.org/abs/2610.11201v1) | sparse support小不确保高效Tensor Core tile → selected-page affinity query unions不改变support，加bounded GPU search与ID-aware两CTA实现 → online preparation/强native kernel可能消除reuse增益，whole-model收益与重组增量必须分开 | 准入 2+1+2=5；有具体设计反证，深入受影响评价；拟 owner INFER-PREFILL |
| [RaReCache 2610.11358v1](https://arxiv.org/abs/2610.11358v1) | 跨模型linear KV映射随尺寸差变大而失真 → rank disagreement定位低calibration-support输出方向的关键token后选择重算 → 是否重算看信息失配位置，不把尺寸小cache视为可无损跨模型复用 | 准入 2+2+2=6；标准；拟 owner INFER-KV-CACHE |
| [Read What Matters 2610.11245v1](https://arxiv.org/abs/2610.11245v1) | 保留bit数与每query读取bit数通常被合并 → progressive code按query的key-channel、attention的value-token分配prefix，受限最优及严格分离实例 → retention容量和read bandwidth是两预算，不应只优化静态cache低bit | 准入 2+1+2=5；标准含必要理论假设与局部runtime限制；拟 owner INFER-KV-CACHE |
| [4-bit AdamW 2610.12444v1](https://arxiv.org/abs/2610.12444v1) | moment-space低量化误差被当作update误差代理 → zero邻格下preconditioner误差不同，ZIP-SR改变rounding space、ZE-EDEN缓解positive floor → 优化器量化须面对递推后adaptive update，而非只看state distortion | 准入 2+1+2=5；具体反证深入局部理论/评价；拟 owner TRAIN-PRETRAINING |

七项均因具体机制/边界准入，不因能映射节点准入。本窄批没有为了配额制造 EX；代表 EX 可复用作者首批准入校准中已读的主题相关但无增量、领域应用、AI for Science 暂缓类，独立复核必须注明其复用而非本批新增筛选。

当前：root 已逐项打开七个 current 官方 abs 读取完整题摘并独立准入通过；七项精确 v1 的必要核心、主对照和近采用命题反侧已读，以下为 Source 交付提议。未下载附件、未追可选 code 复现。Evidence 仍待 root 独立核心复核，Books 由 root 判断并写入，本 note 不自授 DAY。

## 必要 Source 与采用边界

### Zepp — Experimental / Source 提议

[精确核心](https://arxiv.org/html/2610.11158v1)：§3–4.3 placement、routing/flow splitting/merging、intra-node swap；§5 CUDA greedy/water-filling 实现；§6.1–6.6 主对照、端到端与消融。模型选择的专家不变，balance 是容量约束而非优化终点；同构 GPU/等大专家下 token count 代理 compute，node coverage 与额外专家槽限制 swaps，重算须同时等 tokens 和移入 weights。routing/metadata 约占延迟 5%。A100/H100、每 GPU NIC 与 NVLink 组合、BF16 Kimi/Qwen traces，副本预算匹配 COMET/EPLB/EPIC/MoonEP；1.86×几何均值是逐配置最快竞品比较，6.68×只是 A2AV。SGLang/Qwen30B prefill 1.32–1.92×、decode 1.04–1.57×，小 batch 搬权重难隐藏趋近持平；不证明异构、全局最优或 tail SLO。

实际 PRE：Ch52 `从跨 Rank 同步到独立推进：移动请求还是移动权重`（151–157）已有异步拉权重与等待/带宽成本，缺固定 expert choices 下副本覆盖、GPU/NIC 双约束与 split/merge/swap 联合目标。建议两段最小差额：旧的固定 EP/单维 balance 合理条件→直接压 critical-path load；副本/历史漂移/规划与搬运成本→小 batch、弱互联、收益不足回退。Ch56 是 request/fleet routing 交接，不另展开。

### DynaTE — Experimental / Source 提议

[精确核心](https://arxiv.org/html/2610.11284v1)：§III-A–C 三策略，§IV execution/hardware，§V setup/quality、prior accelerator、消融。跳过低 utility token 的 query attention 与 FFN，仍逐层重算其 K/V 供其他 query 使用；不是删除 token 或任意 stale-KV reuse。FLDD 以截断 Top32-KL、Top4 overlap、entropy 提议 anchor/neighbor 串行依赖，仅捕获约 39–45% oracle 依赖；MSM 合并矩阵工作并重构阵列，streaming vocab 扫描仍校验完整候选，不能把 Top32 的精确选择当整个解码精确。LLaDA8B/Dream7B、32-token part/最多32步，五任务平均 −0.41pp、最大 −0.7pp；2.05–2.78×/2.99–3.93× speed/energy 属同资源 prior accelerator 对照。28nm/1GHz、HBM2 512GB/s 为综合与周期模拟，不是实测芯片；Orin 对比同时改变算法，不能纯归因硬件，serial refinement 约8.54% iteration overhead。

实际 PRE：Ch49 `从逐 Kernel Launch 到 Persistent Executor` 开头（135–137）已有 compressed artifact/precision/sparsity 联合编译但没有 dLLM token execution 与串行依赖—阵列映射。建议两段：query/FFN skip 与 K/V completeness 区别→anchor serial work 的矩阵合并/精度计划；approximation、irregular/serial cost与模拟边界→普通 dense/parallel denoising 回退。Ch24 拥有生成范式，Ch49 唯一拥有硬件执行链。

### QUILT — Experimental / Source 提议

[精确核心](https://arxiv.org/html/2610.11134v1)：§3 SCSD/hierarchical sharing/tile tail，§4.1–4.2.3 setup、质量、kernel及 sharing-factor 消融。unique Top-k 集合排序与 shift comparison 求共享/残余；cascade push-down 保留条目，但最终 query-specific tail 按 indexer 分数裁剪是近似改变 support，不可称完全等价执行。16×Ascend910C、CANN9.1、XYServe 匹配 scheduling/cache 的 OPS-Transformer 对照，DS3.2/GLM5.3 Top2048；有限 workload kernel 延迟最多 −55.1%，平均质量损失小但 HotpotQA/LCC 仍退步。重用弱时准备成本仍在，SP 短分片难摊销；没有 GPU 移植证明。本交付不使用未进一步核实定义的 TTFT headline。

### PageWeaver — Experimental / Source 提议（已深入必要反侧）

[精确核心](https://arxiv.org/html/2610.11201v1)：§3 support-preserving union/online grouping，§4 kernel/staging，§5 frozen/online/service/B300/FP32 reference。固定原 causal/query ID、dedup有效 pages、membership mask 保留所选边；两个4-query CTA分消费 union8，两槽buffer按全部consumer完成复用。W64/128 有界 grouping 不改物理Q，bitmap容量512页，超限identity fallback。H200/MiniMaxM3/Top16/FP8 KV+BF16输入Q，主要1.701×比较含 arithmetic/layout/kernel变化；匹配 Union4→8仅1.075×。在线W128收益3.26–7.66%含约34.6us准备，logical page visits不等于HBM bytes。服务 regroup 32/64K增量约+.47–.73%，8K反而负；frozen prompts/technical repeats不代表请求总体。B300没有一个在线窗口胜过更快 existing backend；support不变仍继承FP8误差，单output token不能证明长生成质量。

QUILT/PageWeaver 实际 PRE：Ch43 `Sparse Prefill`（62–90）已具 selection/gather/KV完整性/fallback；缺“支持集合是否固定”的 query-sharing execution 分叉。建议共同两段而非两份论文展示：固定 edges 用ID/mask保持身份、在union/tile复用与online准备间选择；tail pruning则改变算法，分别验quality，且更强native backend/短Context可取消增益，应回退原kernel。Ch49只交接kernel realization。

### RaReCache — Experimental / Source 提议

[精确核心](https://arxiv.org/html/2610.11358v1)：§3 ridge/derotation/rank-gap repair，§4 quality/budget/selector，§5 latency、low-load反侧。同family同tokenizer源KV闭式ridge映射，先去再补RoPE；full/reduced rank差异识别 calibration 弱支持方向，按跨层K/V分数挑token重算，selected queries仍读所有mapped/recomputed keys。匹配映射、rho=.3 的300 GSM8K selector比较rank90.3/random82.3/真实L2-error80.7；不是 CacheBlend/DroidSpeak 完整系统匹配对照。A100/PyTorch eager 测速假设source已prefill，rho=.3仍花38–63%完整target成本；饱和负载有TTFT收益，low-load95ms却慢于native51ms。逆向14B→.6B MMLU损失且多重算不充分修复，不是无损或任意跨family。

实际 PRE：Ch45 causal repair（204–210）已有同模型chunk因果失配与full fallback；缺跨模型表示映射及calibration弱方向repair。建议两段按“同tokenizer映射identity/去补position→rank gap选修复”串起；条件source cost、selector与full-key read、质量反側→不兼容/失准回退target Full Prefill，而非跨模型缓存直拷。

### Read What Matters / ReadKV — Experimental / Source 提议

[精确核心](https://arxiv.org/html/2610.11245v1)：main §2–5.1 allocation/theorem premises/certificate，§6–7 quality/runtime/limits；未遍历50页附录。稳定W-bit progressive codes：K的channel预算由query决定，V的token预算由attention决定；给定K/V预算拆分，非负递减边际gain使greedy对校准代理目标最优，不是实际输出误差全局最优或在线confidence。严格read/storage分离仅构造query族，部署深度8不支配所有unit-ball协议。质量flexible reader与A10G单层runtime restricted reader不同，不能拼接成e2e。A10G/8192/batch1已有cache：Read(8,2) .093ms快于Turbo(4,4).154ms，却慢于Dense .051ms；保留8MiB对4.19MiB，DRAM读减少不意味容量省、字节按比例下降或整模型更快。cache构建/其余模型不在runtime。

实际 PRE：Ch45 bitplane读取段（222）已讲host index通道前缀bit扫描；缺完整K-query/V-attention二阶段读取与retention/read两预算、受限优化目标。两段最小差额可在现段后补；不能把bitplane分离发明归本paper（prior已有），native dense更快/短Context/reader不支持时回退固定精度与成熟kernel。

### 4-bit AdamW — Experimental / Source 提议（已深入必要反侧）

[精确核心](https://arxiv.org/html/2610.12444v1)：§3.1/Prop1–2 rounding反证，§3.2–4 formats，Table3–4与§5 SFT、Appendix B1–B2必要训练条件。state-unbiased stochastic rounding不保证递推后preconditioner稳定；zero邻格、eps→0且next gradient O(eps)时，Pzero须O(eps)才能界定下一mean-error，UpdateSR满足而引入state bias；scalar quadratic等Prop2前提不证明任意LLM收敛。ZIP-SR将二阶状态映到当前preconditioner space，ZE-EDEN用非零floor，first moment NF4和last10%LM-head SR也是配置组成。Table3最大提升来自NF4，ZIP同时换format/rounding不能唯一归因。GPT/Llama小至2.7B、FineWebEdu、BF16+FP32master、block128、3paired seeds；70.1%是vsFP32 loss-gap缩小而非loss下降70%。eligible持久moment1.0625byte/param与8byte比约7.53×，所有4-bit方案footprint近同；不等整个训练显存/速度改善。SFT 5paired seeds vLoss改善不代表所有任务统一获益。

实际 PRE：Ch28 `Optimizer State Allocation`（538–546）已参数角色和write-back契约，没有state error→递推preconditioner误差边界。两段：保留成熟FP32 state条件→rounding space与zero邻格选择；实验配置/证明前提与费用→质量或恢复失配回退FP32 moments，Ch39只物理offload交接。

## 有限补检、代表 EX 与停点

本批在官方 `Fri, 9 Oct 2026` 首日段中，只补读 `cs.DC/cs.AR/cs.PL/cs.OS/cs.PF` 五类31条带跨类重复的题名行（12/9/5/1/4；先前口头32已按保存raw纠正）；这些行不是31候选/31全文队列。按具体系统机制线索选择五个额外精确ID全AB，止于该页当日段；未继续其他日期、其他topic或周源。未入选五类generic distributed/network/IoT/transistor/Ising题名不冒称完整AB EX。四topic API原query/total/start/max/results停止证据由 author 补manifest，此处不把submitted buffer定义为公开窗口。

| 精确材料 | 完整题摘贡献决定与必要核心/事件门 |
| --- | --- |
| [CABRA 2610.10610v1](https://arxiv.org/abs/2610.10610v1) | Repository benchmark的edited LOC不能受控诊断理解能力；生成call-graph任务，四轴调难度，工具把LLM弱点转成近满分agent表现，强理解任务才压出错误。retain 2+2+1=5，root完整AB准入通过；[cs.SE官方recent](https://arxiv.org/list/cs.SE/recent) Fri9原category区[32]，后[34]起明确cross-list，非只靠crosslist membership入窗，current onlyv1。必要core已读，见下。 |
| [DLCB 2610.10547 current](https://arxiv.org/abs/2610.10547) | 完整AB三tier：static形状AOT、fixed rank/dynamic dims参数AOT、unknown rank JIT，constraint减少host guards/kernel参数；拟机制retain5。current仅v1却submitted Aug19，官方Oct9题名raw未保留new/cross-list节；尚不能断言first public Aug19或Oct9，author核官方事件身份。date-only gate普通待办，不core、不先授Source。exact-v1 abs一次cache miss后current成功，不扩大为外部全材料受阻。 |
| [Galahad 50M 2610.10845v1](https://arxiv.org/html/2610.10845v1) | 完整AB后定点§2–8核增量，root独校EX-contribution通过。§2/refs18–20自承2609.39358 byte-exact memory layer、2607.23806的6M窗口、2607.14431 grafting；当前§3仍16k块NVMe存取、一块驻留。50M、vLLM、AES-GCM和nonce/blind/decoy/store-audit组合加强规模/证据，未给新的KV读取/身份/合并机制或采用边界。不得称same-paper去重，未追旧版本；也不把50Mdurable store当50Mattention。 |
| [TME residue cost 2610.10924v1](https://arxiv.org/html/2610.10924v1) | 完整AB与§1–4必要scope核验，root独校EX-scope/AIforScience暂缓通过。具体是scientific FP64 emulation、Ozaki/CRT residue deconstruction SIMD整数成本，GEMV/SpMV/stencil模型修正；当前全文未给LLM训练/推理适用命题，root实际Books也未有被纠正的Ozaki/TME旧命题。不是因“FP64”字样一般排除，也未声称方法数学错。 |
| [DEX 2610.11748v1](https://arxiv.org/abs/2610.11748v1) | 完整AB为BraTS/nnU-Net专用INT8 MSDF early ReLU/sign与离线Dice-budget低digit skip/prune，73cases/45nm综合加速器；无基础模型训练推理适用命题，root独校EX-scope通过，不以一般低bit accelerator映射retain，也不按medical关键词机械排除。 |

### CABRA — Experimental / Source 与实际 PRE 提议

[精确核心](https://arxiv.org/html/2610.10610v1)：§2–5.2/Table1–2/Fig4/§7，Appendix A3/A4必要协议限制。DAG五改写任务×四独立size轴×n5–200、三code类型共6840；all-pass用各函数50随机输入+改写规则，不是形式等价。单Copilot1.0.76六agents/八无工具LLM对照，AST/grep/exec绕过前3轴难度；LLM最多约10次、agent通常3次parseable重试，分数不能当全部请求部署成功率。SWE Verified Read+Analyze call r=−.200对LOC−.159，均弱相关非因果理解真值；classifier一位作者小抽样agreement94/89/94。Merge任务用等价变换+保留d行为差异，使agent仍可能保持>90%行为却未抽出充分共享逻辑。任务生成、LLM调用与工具/标注有费用，合成控制不代表真实repository分布。

实际 PRE：`PLATFORM-EVALUATION-SYSTEM` Ch66 `Agent and Outcome Evaluation`（946–953）已有跨层oracle与lucky pass，未覆盖工具把 intended complexity axis脚本化绕过。提两段：repo现实性与合成独轴诊断互补，须先核工具是否消除被测构念，再用semantic-merge压力轴；EvalSpec共同版本化generator、harness、tool权限、parseable-retry、classifier与黑盒oracle，工具call数不认证理解/因果，保留真实repo配对与独立verifier。非本执行者写书。

本执行者合计12个独立ID完整AB：8已root准入并必要核心读完（七系统+CABRA）、1事件身份曾未定(core未由本执行者启动)、3代表EX已root校准。root最新消息称DLCB已有author官方cs.PL new身份核验，将由author接core，本执行者不重复；相应最终日级计数由author合并，以上仍是本执行者实际工作口径。

## 实际非 writer Books POST

root 已写入八家族，本执行者随后逐字读实际新增正文与完整局部邻接，并与本轮实际读过的各精确 v1 必要方法、评价和反侧对应：

- Ch52 151–171：Zepp159/161、完整权重流到Adapter邻接。
- Ch49 133–147：DynaTE139/141、compressed artifact到persistent邻接。
- Ch43 98–124：QUILT/PageWeaver共同110/112、Topbudget到Hybrid邻接。
- Ch45 202–238：RaRe212/214、ReadKV228/230、causal repair/wrapper与bitplane/DiffLM邻接。
- Ch28 542–564：AdamW554/556、参数角色到Whitening邻接。
- Ch66 946–968：CABRA952/954、incident到FinalPass邻接。

实际非writer POST通过：无must-fix，原条件/费用/反侧/回退保持；未把support不变签成数值无误、少read签成容量减少、source-prefilled条件签成免费、scalar理论签成LLM收敛、工具call相关签成因果理解；新机制各有唯一owner。此结论仅覆盖这些新段及邻接，不冒称全章/全书语义复核。本执行者只改本note；检查本note无trailing whitespace，定点diff-check无报错（untracked新note仍另以直接文本检查），未stage/commit/push。报告写回与DAY由各owner完成，未自授全arXiv召回、source denominator、Report或DAY完成。

## 最后六项：非 Report author 独立 Source 窄核

本次受 root 定点委派，对 author 已准入的六个精确 v1 独立读必要方法、主对照与紧邻采用命题的反侧。复用 author 保存的官方原文 `arxiv-core-batch4.json`、`arxiv-core-batch5.json`、`arxiv-dlcb-core.json`，并实际打开六个官方 HTML；未扩附件、code、历史版本或发现队列。下面均是 Source 层，不是复现；原八项实际 Books POST 继续有效，六项尚未由本执行者做新增 Books POST。

### DreamTrue 2610.12468v1 — Source 条件通过

[原文](https://arxiv.org/html/2610.12468v1)：§3.1–3.4、§4/Tables1/4/5、§4.4、§5及 A1/B1/C1–C2 必要协议。

采用机制是离线 URDF render 配准 camera/robot state，将 image-space action 与多视角视频条件连接；StageII 用 SE(3) 终点扰动、轨迹插值和 IK 构造没有真实未来的视频条件，用视频缺陷奖励改进生成。奖励不读配对未来或 action condition，视觉缺陷减少不是 action/物理正确性的独立证明。

主对照是相同 StageI→StageII：160 反事实条件、三位盲评标注者；object/interaction defect 降至3.12%/6.25%，但 EWMScoreP 72.84→72.51。与 GE-Sim 的低缺陷区间仍重叠，不能普称全面领先。240 次 RoboTwin 评估的 MAE 改进来自 human-video outcome 与模拟器结果比较，仍有12 false positives，不是实机安全认证。遮挡、视角及视觉奖励可共同接受物理错误；保留真实执行/独立物理校验，不以视觉一致性代替。

### LeWAM 2610.12407v1 — Source 条件通过

[原文](https://arxiv.org/html/2610.12407v1)：§3–6、同预算 planner/policy 对照及 shell/mode 消融。

同一在线 encoder 联合 forward/backward/inverse/policy 四种 JEPA 任务，以 SIGReg 防 collapse；MPC 在 policy 的 Gaussian noise 空间搜索，再随 imagined state 解码 action，而非任意 raw-action 优化。投影到典型噪声壳限制搜索偏离，但不是所有候选都在训练支持集、预测都因果正确的证明。

主要证据为 PushT/Robomimic 模拟任务、5训练 seeds/250 evaluation runs，同 horizon/sample/iteration 预算的 DS/NS planners。NS 通常优于 raw-action MPC，仍有 Can DS78.8%低于 policy82.8%，Square 去 inverse 消融也未低于全部模式。目标来自 demo frame 检索且 planning 较慢；参数近配 reimplementation 与带预训练 VAE 的 RecWAM 不能当严格相同初始化。没有实机验证，保留目标构造、运行预算及控制闭环，而非用 latent probe 单签控制质量。

### REACT 2610.12007v1 — Source 条件通过

[原文](https://arxiv.org/html/2610.12007v1)：§3.1–3.3、§4.1–4.4/Tables1–3、§6。

H=KS 滚动 buffer 将不同 block 放在 K 个 denoise stage，每轮依最新观测做一步，提交前端 S actions 后移位补噪声；训练匹配该 timestep-position grid。Dual Decoupling 分离感知与去噪，选择 capture timestamp 单调的 latest-ready condition；仍要求感知池吞吐，K/S 是训练配置，不是任意 schedule 零成本切换。

同 pi0.5 backbone、相同 placement 的模拟/实机 chunk/RTC 对照支持反应—连续性折中，但 full DD clean44.86%低于 noDD49.71%，实机整体64.8%低于65.7%。Jerk 只统计成功 episodes，不能签全部执行的安全性。观测 age mean233/p95383/max416ms 不代表零陈旧或严格一个周期；39.96ms局部 update 也不是 sensor→motor。Reaction Game 734±94ms vs RTC747±123ms 是窄差，不能普称显著。无独立训练 seeds；优化 steps 减少不证明训练 wall-compute 降低。

### BudgetPix 2610.12307v1 — Source 条件通过

[原文](https://arxiv.org/html/2610.12307v1)：§3.2–3.4、§4、C4/C7及 D6/D9 必要消融。

Entropy quadtree 将低熵区域用 coarse token、细节区域用 fine token 表示，PA/PR 适配 pretrained pixel backbone；多 layout/budget 训练后，warmup 预测 clean image 再定 layout。Coarse encoding 是近似压缩，需要局部重构与质量预算；一步 MeanFlow 的 random layout 不能混称同一 warmup 方法。

七 backbone 与同 prompt/noise/solver 的原版采样对照，但 BudgetPix 另行 fine-tune，不能把全部质量收益唯一归因 token budget；faithfulness 参考各方法自己的100%结果。JiT-B512 FID3.94(full)→16.71(25%)直接否定低 budget 无损。H100 timing 含按 layout 的 graph replay/减少同步，且文本预编码，属于局部优化 forward，不是生产 e2e；更高 warmup 质量有额外费用，batch-pooled budget 在25%也可劣于 fixed。主文与 C4 的 random-layout 概率口径有细差，本采用判断不引用其精确比例。

### Caught in the Act 2610.12445v1 — Source 条件通过

[原文](https://arxiv.org/html/2610.12445v1)：§2.1–2.2、§4.1–4.4、§5.1–5.2/§6、B1/B2/B4及 F 必要反例。

163016 contextual-falsehood transcripts 训练 probes；六层 hidden states 上按 follow-up 的两种 prefilled answers 取 contrast，检测的是模型相信为假的陈述，不是所有恶意意图/真实世界谎言。每 step 重跑 prefix 并提取激活，只有该 step 的 branches 共用 KV，不能把 probe 小等同全部监督费用免费。

Qwen397B 主 AUROC .979–.984 vs Opus .960 是14/25人工筛选 SHADE 场景上的逐 step 排序；标签从 judge 判定 onset 起把所有后续 step 当 positive，无 onset attack episodes 剔除，不能签每个被标动作都属恶意。训练多样性并非每一配对都获益。Free-tier bird-labs 的 own-goal denial 只2% recall@2%FPR；math-sandbagger63%AUC，加行为例后93%，说明 persona/context/belief 会改变可检测对象。保留外部行为 oracle、阈值校准与漏检处理，不能用 introspection 单签部署安全或全模型通用。

### DLCB 2610.10547v1 — 公开门与 Source 条件通过

本执行者独立读 [cs.PL 官方 recent](https://arxiv.org/list/cs.PL/recent) 的 Fri,9 Oct 首段：[2]DLCB 是原 cs.PL new，紧随[3]明确 cross-list；不能把 Aug19 submission 当 first public，也不能只靠类别 membership 入窗。本段更新上面的旧 date-only pending，保留 submitted/announcement 不同事实，不追旧版本。

[原文](https://arxiv.org/html/2610.10547v1)：§2.1–2.3、§3、§4.5、§5.1–5.2/§7。supported subgraph 才编译、unsupported 留 native；static 依具体 shape，fixed-rank dynamic dims 用参数 AOT，unknown rank 回 JIT。Constraint solver 将常量、runtime 参数及 residual host program 分开，逐 thunk 校验 shape/broadcast，vector contiguity/divisibility 失败走 scalar；不等任意 equation solver 或任何输入均无需重编译。Cache 还依赖 type/rank/constant 等签名。

H100/fp16/TorchVision、3 warmup+5 timed 迭代：static1.10×、dynamic0.92× eager，直接显示少重编译可换取运行成本；compile median .84s vs torch.compile9.4s 不是端到端吞吐收益。符号 index/divmod、单 vector width、layout inference 仍弱，不签 LLM 服务或动态 rank 普遍收益。失配走一般/scalar/native/JIT 路径，采用须联合测 compilation lifetime、热态吞吐和签名覆盖。

六项独立 Source 结果已送 root/author；本次不重评分、不新造 Books PRE、不自授 Report/DAY。停止边界是这六项必要核心与反侧，非六套全部附件，也非新有限发现的召回声明。

## 最后六项：实际非 writer Books POST

复用上节已通过的必要 Source，不重开附件；本执行者实际逐字读 root 新写的12段、完整局部邻接及各六个 family/exact-v1 原文链接。

- Ch25 1006–1030：LeWAM 新1014/1016，前接 imagined-state/search owner，后接可识别表示条件。PASS：noise-space proposal 与 physical authority 分开，shell 不是支持集或安全证明，5-seed模拟/goal来源/预算与失败回退保留。
- Ch25 1187–1230：DreamTrue 新1207/1209，前接 action/off-expert/embodiment，后接 Reason/Execute/Render。首次 POST 要求收紧1207 reward 输入表述，避免把只看视频的缺陷评分写成显式读取几何/action/paired future；其余整体分数反侧、视频与实执行分离通过。待 root 最小修后定点复核。
- Ch26 894–926：REACT 新910/912，完整 Streaming VLA 到同次 denoising/fast-slow 邻接。首次 POST 要求将912『不带该分支』明确为无双解耦的 rolling 对照，避免归因去掉 rolling；其余 buffer commit不可逆、observation age、成功episode-only jerk、forward≠sensor-to-motor与fallback通过。待 root 最小修后定点复核。
- Ch24 1197–1217：BudgetPix 新1205/1207，前接 refinement/latent生成，后接 decoder artifact。PASS：布局训练/估计费用、低budget质量退步、动态质量与冻结layout timing区分、局部forward非服务SLO，原fixed patch路径保持。
- Ch72 1009–1030：Caught 新1015/1017，observation-point到跨执行安全性质完整邻接。PASS：条件belief非意图/authority、人工筛场景/onset人口、sandbagging/free-tier反侧、漏检不从真实风险分母删除、fork费用与外部effect/policy责任保留。
- Ch49 53–77：DLCB 新59/61，冷启动plan到Adapter/static-KV完整邻接。PASS：fixed rank与dynamic dims区别、host guards/JIT/native、dynamic低于eager、compile/runtime分账及LLM外推禁止，唯一执行owner不接管训练/adapter/state身份。

定点 Books diff-check 空；首次四项通过、两项仅上述表述修复待办，不签 Report/DAY，不写共享文件。原八项 POST 不变。

root 已实际窄修两句，本执行者随后定点回读 Ch25 1203–1215 与 Ch26 904–918：DreamTrue1207 明确视频缺陷奖励不读 action condition/paired future；REACT912 明确 full DD 对无 DD rolling。修后精确 family、v1链接及前后交接不变，两项均 PASS。六项12新段实际非 writer POST 全部通过、must-fix/普通 POST 待办0；仅签这些改动及已读邻接，不签整章/整书或 Report/DAY。修后定点 Books diff-check 空。
