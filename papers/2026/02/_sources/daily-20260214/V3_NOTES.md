# 2026-02-14 V3 本日工作笔记

窗口 `[2026-02-13T09:00:00+08:00,2026-02-14T09:00:00+08:00)`。本次独立重建，只以 inventory 的题摘/身份作原始线索，不继承旧 README、Weekly、author/final ledger 的筛选、评分或完成标签。628 宽目录身份不是逐项强制审阅队列。旧 exact-v1 bodies 可定点复用；本次贡献判断与证据限定重新记录。

启动及每次压缩恢复已重读 AGENTS、研究/Report V3 合同、Prompt、Sources 使用说明/每日组/arXiv 主题与 ROADMAP；LS 只加载月路由，没有继承其他日的筛选。仅拥有本日 README 和本目录；共享 Books 按 root 具体 PRE/窄锁/实际 POST。当前四处本日实际整合：Ch34 11902、Ch22 12021、Ch55 12029、Ch56 11530，均已非作者 POST 通过；另Ch5 11246是有效独立理论/首公开日期未确认，不计本日。既有 staged/unstaged 不动，无 stage/commit/push。下文各早期停点及50分母都是过程快照，末尾“日期共因纠正后的当前终态”与 README 才是当前状态，不将早期“待”快照再当待办。

## 首批准入校准

root 实际读取 inventory.json `.identities[] | select(.arxiv_id==...)` 的完整 title/abstract，独立批准 8 项准入与 5 项代表性排除。它不是证据/Books 通过。

| ID | 本次准入增量或排除理由 |
| --- | --- |
| 2602.11157 | response-only reasoning KD 不自动迁移安全；同一 LoRA 设置的小模型跨语种 jailbreak 反侧，改变安全蒸馏验收目标。安全受影响部分深入。 |
| 2602.11162 | 静态 retrieval-head 名单不足；检索头逐 token 转移及等数量动态 mask 反侧，改变稀疏刷新 head 选择。 |
| 2602.11169 | L2 匹配的 radial/angular 干预在 Pythia 上损失与句法敏感性相反，且 RMSNorm 家族反转；不能从几何直觉签统一重要性排序。 |
| 2602.11174 | 同内容转写的 token/BPC/延迟预算比较，CER_rt=.31 混杂；只保留窄评价，不签纯 token 因果，拟仅报告。 |
| 2602.11185 | 对完整 momentum 保留 residual、仅替换低秩 spike 奇异值；准入时“低秩更新”表述已纠正，不是低秩权重更新或只存低秩状态。 |
| 2602.11192 | sequence preference 重塑 expert activation 与预取结合，直接减少 offload I/O；不从摘要签无质量代价。 |
| 2602.11202 | poll/fork 在中间可验状态干预推理而非事后评分，改变可验证任务的搜索执行路径。 |
| 2602.11210 | 实际 environment preparation/isolation 接口与成本，改变 SWE 训练环境工程选择；不得从摘要签普遍无开销/同等隔离。 |
| 2602.11156 | EX：成熟 OCR/层级分块/预生成 QA/检索 fallback 组合，没有新增机制或条件。 |
| 2602.11165 | EX：近期 Reddit QA lexical 与 semantic 指标差额本身未新增误差解释或设计条件。 |
| 2602.11175 | EX：现有离散推理理论归纳，不新增可核验主张。 |
| 2602.11177 | EX：AD 分类/SFT 应用收益，不建立基础模型/系统新增机制。 |
| 2602.11172 | EX：Legal Indic TTS 应用及 persona prompting，没有新增模型机制。 |

## 本日有限来源停点

14 每日来源，非每周扫描。arXiv 的现存宽标题列表仅用于主线主题查漏，潜在贡献逐批读完整题摘；标准/深入审阅仅在准入后。

官方 schedule：Sun–Thu 20:00 Eastern；Wed14–Thu14 提交通常对应 Thu20 公告；Fri/Sat 无常规公告，quality assurance 可迟滞。Submitted 不等于公开。本批多数 DataCite 原始 Updated(v1) 在 2026-02-13T01:00Z 后，Created 在 02:47Z 后；须以完整原字段、官方 batch 与 created 推定含起点/不含终点区间，不授合成 announcement_beijing 的精确秒。11157 Updated(v1) 异常为 04-27，单独补确认，不能靠单调 ID 自动落窗。

机构目录实际已查：OpenAI Research + 本窗 bounded query（Feb13 GABRIEL 社科方法应用已读核心并贡献排除；1stproof 为数学解答线索，不可借系统节点引入暂缓 AI for Science）；Anthropic research 当前首页不包含目标历史段；Google Research pubs 当前列表/DeepMind 当前页不能证明本窗无遗漏；Meta extraction 空；Qwen 旧站重定向而旧站最新 2025-09 不覆盖 2026；DeepSeek 当前 release 页面无本窗历史切片；Moonshot 博客当前可见旧段不足；Z.ai Research 连续日期段 02-11→02-21 无本窗条目；Seed public_papers 第1页/13页停在05-14 尚未到02月；ERNIE 当前博客连续 04-15→02-06 跨过本窗，无该段命中；MiMo papers 日期段03-13→02-03无本窗，undated blog 不授覆盖；MiniMax 当前blog不足，M2.5官方正文日期2026.2.12无时区仍不能确认本窗。

混元 research：web 空提取；子代理浏览器入口重复 timeout/不支持 visible；root 只读 iab 于37.8秒 timeout。合并为有限外部目录缺口，停止浏览器恢复，不记零事件，不授 Coverage。root 授权继续其他可执行项。

## 首8精准证据停点

均为 `https://arxiv.org/html/<ID>v1` 作者稿；未执行实现/复现。11157 §3–5: o1-mini teacher、Llama3-8B/Gemma2-2B/Qwen3-8B、28,190 XSafety、LoRA rank16 alpha32/all layers/2epochs/H100SXM；MultiJail3150 十语言，JSR 12.5→13.9/5.0→21.6/5.7→8.3。GPT4o judge300人工复核4.6%差异、另judge低百分点差异，低资源机器翻译。§5.4边界过滤、§6限制尚补读；不能证明安全子空间因果或frontier普遍性。

11162 §3.3 动态 mask 在同一 token 第二次 forward，静态/随机等平均 mask 数量；Llama3.1-8B NIAH动态更明显破坏检索，20静态头补偿不恢复。CCA .966/.931/.915只支持 hidden-state 预测相关；MLP F1 .8–.86，不证明前瞻规划因果。需补 method 定义、RAG 对照与限制。

11169 §3.3/4: Pythia410M、层8–15、全部token同时干预、L2误差<=.01；WikiText103281句，5 perturbation seeds，BLiMP200句。δ1 angular loss .368 vs radial .009；δ5 radial句法69.1% vs angular87.9%(baseline89.5)。TinyLlama RMSNorm magnitude更敏感，反转不证明仅normalization导致，架构并未隔离。需补结论/限制。

11174 §3–5 全核心已读：mBERT/XLM-R 双书写同内容，mask/BPC方案与样本数/硬件/batch不可复查；CER_rt=.31，L²只是attention算量模型，不是全系统实测规律。保留作者局部比较，不用于生产保证或纯token因果。

11185 已读开头 spike频率/within-sequence token shuffle 反侧，需 §3.1低秩更新与rank/state/epoch成本对照。11192已读predeployment sequence-locality+predictor/prefetch接口，需具体loss与cache/I/O/quality对照。11202实际v1标题 Verifiable Reasoning with Test-time Monitors，与raw later metadata标题不同；需精确v1首段核身份，已读checkpoint干预和Maze/EAT/DEER/Game24表，保持accuracy与token分开。11210待核心namespace/resource/env构建机制评价与安全边界，不以摘要代替。

## 恢复后证据更新（2026-10-04）

首8 exact-v1 abs全文保存于 `V3_FIRST8_ABS.txt`。DataCite manifest定位原JSON压缩包；`doi-prefix-2602-11-page-01.json.gz` 的11162原字段Submitted=2026-01-07T02:29:24Z、Updated(v1)=2026-02-13T01:00:13Z、Created=02:47:17Z、Registered=02:47:18Z。registry不能单独充当首次公开clock；采用官方announcement下界与秒精度created上界时需要保留完整半开区间及推定性质，不抄旧精确09:00。

11157新增首公开反侧：arxiv comments明确2025 NeurIPS ResponsibleFM poster；同题同作者OpenReview `e26bFhz8YV` PDF正文有2025 workshop页脚。同族若已公开2025全文则本日仅arxiv收录不算首次公开；OpenReview forum/API在challenge、必要公开版本日期仍定点恢复中。不能仅用邻号/Created消除这个早公开反侧。

11162 §5.2–Limitations已补读：in-context attention masking模拟，不是外部检索生产实现；probe top5 vs静态top5，Llama3.2-3B动态EM .384不如静态.428，MLP非oracle、其他长上下文任务未验证。拟采用仅“固定head名单不能保证逐步最优”，不采用普遍动态更优或planning因果。Ch22 selector/profile刷新与fallback已有具体覆盖待独立核。

11169 §6.3/7.2/9已读：LN patch magnitude恢复29.9% vs angular13.7%，只解释~30%damage；OPT attention mediation也反转，TinyLlama loss方向全反转。L2匹配仅干预位置，下游angular距离放大约3倍，不能认定LayerNorm/RMSNorm单因果或通用语法/语义模块分工。拟仅报告这个架构/指标依赖干预诊断，不从作者model editing推测签实际编辑收益。

11185 Algorithm1/§4/Table3–5已读：dense momentum mn +cached right vectors nk，spike谱压到tail RMS而tail保持；k1.5%、T1、H200矩阵kernel1.78ms vsMuonNS9.15ms；0.6B训练peak103.5GB vsAdam107.4GB、step5259 vs5297ms，optimizerstate约-49.25%不等于总显存减半。Qwen0.6B100Btoken/Llama8B50Btoken局部收益，部分task较低，无实现复现。Ch28现有spectral regime段未明确这个soft-spike branch，拟深入Books差异核。

11192 §3–4/Table3–4已读：soft cache simulation +expert-order rank matching+NLL，并训练gate/LoRA，不是不改router的cache；任务finetune本身影响质量，不用对untrained-base比较证明auxloss无质量代价。OLMoE受控transfer727→240/229MB、Mixtral105→48/46MB，prefetch成本.05s；H100/A100/4090 artificialcap3/16/24GB，64outtok，1.2–3×bestbaseline与14.7×weakbaseline分开。cache权重过强伤质量。拟核Ch54cache-aware training与runtimeprefetch分界。

11202 §4–5/Table1–4已读：sequential verifier按demarcated state提取、检查、把失败feedback附原trace继续；soundness仅指定verifier+解析覆盖，不签自然语言普遍正确。k2稳定检查不是真值验证。Qwen30B Maze1500/SpatialMap1500/Game241362、vLLM temp.6 topP.95 topK20 max32768；正式表token含义不是E2E wallclock，verifier成本未充分计入；作者正文SpatialMap reduction10.8%与Table1 95.31%tokens有不一致，采用表明示数据。Phi4 Code DEER50.73%token减而kStable17.49%，有直接反侧；最佳accuracy保持点事后选择，无普遍最优。

11210 §2–4/Table1–4已读：mountnamespace+chroot/hostbind共享环境缓存不是cgroups/network/PID全隔离。仅Python SWE任务；8B200/184core、SSD800GB、CPUcap32环境与Docker机器仍不同。storage reduction非同义全资源下降；single-node256env Mini rollout550s vsDocker430s，two-node259 vs415s，收益受I/O/分布式拓扑条件限制。无恶意tenant escape实证，不签同等安全隔离。拟仅报告这项research环境成本分解，不构造通用平台保证。

第二批 root 实读题摘后7potential通过：11212、11220、11246、11374、11456、11488、11988；5EX通过：11301、11674、11685、11790、11865。11224一次决定core§6.2/Table5已核：docs pass+7pp但assertion+2.4pp概率.73，all-docs+.2pp概率.53；cutoff自然实验非因果隔离。root只授窄评价反侧准入，不按state-diff/benchmark命名准入，尚非证据/Books完成。

Meta FERRET官方Feb13题摘与 arxiv2603.10010v1 同作者同题，Submitted确实2026-02-17T20:59:14UTC；不能从March ID推错族。官方fbcdn PDF cachemiss，必要Feb13公开clock/原可见正文仍隔离，保留URL在本日报告请求。不因后arxiv重新计首次公開。UniT官方Feb11明确窗外，仅恢复线索。

普通待办：其余主线题摘有限判断、必要日期、候选标准/深入证据、Books具体论点比较、来源有限恢复、六部分报告与root最终非作者验收。尚未把普通待办写成外部Blocked。

## 第二批精确证据（实际必要阅读，未授 Books）

11212 [Elastic Memory exact-v1](https://arxiv.org/html/2602.11212v1) §2、Tables2/8/12及A.1：HiPPO-LegS 状态分离 raw K（RoPE之前）/V；预计算位置投影 P_i/K_i 和 readout R_i 在固定最大 context 上使用。恒定的是 recurrent state，不是预计算 bank 和总资源；memory readout 的 uniform/exponential sampling 改变同一状态的历史访问偏置。N=1×540至16×8640，状态预算不同。100M～400M、40B tokens、三个长文本数据各2B、8A800/BF16/2048 block；baseline重实现或简化，注入层数不同，不能作 canonical implementation 的等价对照。uniform部分PPL不如Melodi，exp最优PPL与LongPPL不同；16×状态吞吐下降。Table12随机noise无法压缩，非无损检索。窄采用固定状态/读出采样的分账，不签不限长度免费扩容。

11220 [exact-v1](https://arxiv.org/html/2602.11220v1) §3–4/Table1/ablation/Limitations：冻结base，LoRA rewriter GRPO；K=10组×512 prompts，任务答案+reason-consistency hard gate 后才奖励 base-length-normalized NLL 与leave-one-out diversity。50k训练rewriter、50k原/改写SFT，失败改写保留原样本，Llama1/3B与Mistral7B/数学数据/2epochs。Llama3B math18.9→vanilla21.81/ours21.12，general45.21→37.26/43.17，不是全指标胜出。去掉distribution/diversity各自损general；hard gate优于soft。保留失败样本vs只用37483成功样本有覆盖混杂；相同SFT步骤不等rewriter+10rollout总预算相同，judge非证明器。支持修改demonstration分布的局部遗忘取舍，不证明普遍降低遗忘。

11246 [exact-v1](https://arxiv.org/html/2602.11246v1) Definitions/Theorems1–3、§2上界构造、§3下界及classification Theorem12/Cor13：f=Az，k-sparse z∈[-1,1]^m，要求全部输入上用线性B^T恢复且infinity误差≤ε。非线性压缩感知d=O(klog(m/k))与线性近紧k²级界是不同访问合同。上界 incoherence μ=ε/k；下界适用 ε>sqrt(5)k^1.5/sqrt(m)，用B^TA主子矩阵rank/Turan/同号稀疏支撑。不是实际LLM feature数/普遍ε无关下界；representation和probe各自可能correlated，重要的是交叉inner products。完整必要假设已读，不签线性探针不可读意味着没有表示。

11374 [Gated Attention exact-v1](https://arxiv.org/html/2602.11374v1) §3–5.4/Table1–3已读：teacher逐head ablation选保留head，其余改Discrete-Mamba2；保留QKVO后仍加parameter-free LayerNorm，不称旧head函数原样不变。matrix orientation阶段因保留anchors跳过，后续hidden matching+logitCE。10head Llama1B/Qwen1.5B的平均teacher coverage≈95/96.4%非全部任务parity，个别局部任务回归；固定25%/50%数量COV不同。0.8MB vs4.1MB是attention/recurrent state计账，不是完整进程VRAM；缩state d8 vs64与保留head耦合，尚补§5.5/A1/A4必要配置。

11488 [ALME exact-v1](https://arxiv.org/html/2602.11488v1) §3/Table4及cascade定义已读：57602 stimuli，8语言，同源音文改变单一number/negation/adj/time；filter后约53k unique。native每语40样本质量EN97.5/JA92.5/PT90，不是全数据完美标注。TDR=text/(text+audio)，invalid排除<.3%，模型/版本/temp/8bit限定。WhisperLargev3 cascade A/B正确转录子集/C无ASR，不能只把能力差额归ASR。cascade system prompt/50vs150token与可靠性提示和order仍有差异，不能签纯模态因果；尚补§4直接结果/finetune/限制。

11988 [AGENTS.md exact-v1](https://arxiv.org/html/2602.11988v1) §3–4.2/trace已读：138任务12 niche repos，与SWEbenchLite300/11popular协议不同；golden测试patch失败→通过、平均changed-line75%非完整正确性。agent/model/harness/compression/temp不同，一次完成不授跨harness因果。LLM context 5/8 settings掉分，平均−.5%SWE/−2%AGENT，不签每设置−3%。Human多数提升但Claude反侧；文档移除后auto+2.7%支持冗余解释，跟工具指令≠success；uv使用1.6vs<.01/repo2.5vs<.05。检索gold文件早晚不改、overview非总会省钱；尚补end限制和必要A配置。

12029 [PrefillShare exact-v1](https://arxiv.org/html/2602.12029v1) 本地exact-v1-bodies/2602.12029v1.html lines445–810/§3–4已实际读：base冻结产统一KV，same-architecture specialized decoder全参数NLL适配该KV；非只训练decode逻辑phase参数子集。naive共享质量collapse，cache-conditioned training产生compat artifact。workflow里新生成token由base增量重放后给下个decoder，不把前assistant不同KV直接复用。Llama3.1-8B/Qwen3-base1.7/8/14、任务FT40k/80k/60k，质量混合；不授任意架构共享。8A100/4P+4D与4dedicatedpairs对照、sequential4agent/workflow并发；高load gain低load近似，极高loadhandoff限制即使hit rate稳定。共享/独有长度内存公式非完整系统成本，正文dominant项措辞错误不照录。拟采用frozen-prefill/trained-decode身份，不采用全部宣传speedup；仅在拟性能采用时再补B1/B2配置。

## 后续准入校准与一次 core 排除

root第三批完整AB通过8potential：11184、11287、11401、11408、11443、11470、11521、11530；5EX：11182成熟self-reflect memory组合、11318综述/已知主体性原则、11481已知compiler反馈闭环应用、11514 taxonomy、11581 conceptual RAG组合。第四批6potential：11686、11688、11761、11902、12021、12029；5EX：11607成熟memory/prompt组合、11776 fraudScore范围外、11845局部重建非worldmodel机制、11897cyber流程组合、11931confidence cascade收益未新增confidence有效条件。

11717 一次决定 core §2.2–2.3/Alg1/A1：per-output-channel weight softmax RKL广播乘absΔW，再median+1.5IQR上尾选择、secondary权重逐坐标替换base。root实际读core/A1，不接受输出分布KL/entropy保持推论；未改坐标的weight softmax也随分母改变。只是参数proxy重要性启发式替换与局部收益，贡献EX通过，不评分/不采用，不扩附件找贡献。

11808 一次决定 core §3 L59–75缓存 V3_11808_DECISION_CORE.txt；root实际核原段后EX通过。first-stage fusion+row/column重用与部署shape profiling未给新增依赖解法/成本条件；intro完整SwiGLU融合不能代替方法两阶段。局部throughput不独立建立准入，不评分不采用。

第五批root完整AB通过8potential：11510、11786、11792、11964、12124、12158、12194、12235；安全题目只授受测具体增量，未授普遍保证。EX通过11580通用CPU calibration无大模型直接主线、11598分层brain/flow/topological planner组合+数据量、12056法律检索验证/记忆组合。11911一次classifier核心待判断；12092一次安全core待判断，不默认全文。

## Books比较停点

11185当前Ch28 `TRAIN-PRETRAINING` 883–891已具体承载leading-singular selective clipping、truncated randomized SVD/rank/cadence/额外成本，以及低秩失配、估计滞后和global-norm fallback；584–606另有head/bulk敏感性分账。具体RMS-tail阈值/cached-subspace是实现变体，不能仅因为owner未写该配方自动定长期gap。正在据此判断Existing或OnlyReport，不强造diff；未申请写锁，未写Books。

## 第二批尾部已完成的直接反证

11374已补§5.5–5.6/Table4/§6/A1/A4。固定top20head，d_state64→8，retrieval Cov95.8→90.0，GSM34.0→30.1；降至4进一步Cov81.0，并非无损。SSM heads仍少量参与检索，不能把能力完全隔离。8H100/FSDP/mixed precision，batch128/2048 length，50/50FineWebEdu/Finemath4Plus，总12Bdistill tokens；A1 Qwen2.5-1B表述与主表Qwen2-1.5B身份存在不一致，不签该身份之外泛化。A4内存是BF16、dhead64的理论cache+state计账，Eq/head-per-layer与Table7跨层总head口径不同，不直接拿3–6×作为已测总VRAM。采用选择检索head与state缩小必须联合验收，受测sub3B/单synthetic-probe，非任意模型有效。

11488已补§4/Table5–19/§5.7。Gemini纯音频97.2/纯文本98.2/aligned97.8但conflict16.6%TDR；cascadeB1.6/C1.0%同时2.7–2.8%unparseable排除（直接模型<1.1%），不认“完全隔离纯模态因果”。Qwenposition gap27.6%，校正62.6≈62.7TDR；forced-choice/八语言不代表实际事故频率。14,369 EN+JA同输入提示反侧：明确text corrupted有改善，先transcribe反而19%→33%TDR。29,263held-out flip types：UltravoxadapterFT TDR49.4→75.9，LoRA→25.5；两者audio-only80.1→53.8/56.3，不能用TDR下降签无能力代价。LoRA r16 alpha32冻结其他模块、50/50aligned/conflict，但epoch/totalbudget未披露；CJK/Arabic改善弱，ASR/训练分布/unstableFT其他解释未排除。§5.7：onlylexicalspeech/forcedchoice，CommonVoice overlap未知，单native/语40人工样本，不接受“overlap对所有models等量”保证。深入采用有冲突时必须独立测仲裁与单模态理解，不签普遍text bias因果或修复recipe。

11988已补§4.4/§5/A1。生成者GPT5.2对SWE平均+2%、对nicheAGENT−3%；换Codex/Claude生成prompt未一致最佳，不能签更强writer一定有效。结果以Python为主，仅task-resolution，不测security/perf/policy-compliance；网络开启但minor<1%，history/remotes移除，ClaudeTask subagent Haiku开启。受测guidance带来测试/探索/步骤/成本增加，不是未遵循指令；failure attribution与LLM shell-call分类有主观性。安全约束本身不能因成功率负侧删除。必要深入证据够，拟BooksOnlyReport或实际现有覆盖，不自动建议改用户AGENTS。

11911 root实际核一次classifier core后窄5准入通过：FT降低FP但提高FN、排序用途不授二元correctness。minmax合并不等独立校准posterior；unit-test label不等完整程序正确性。12092 root实际核registry/nativeeval/Table3后EX通过：成熟workflow与既有diagnostic方法组合，没有新成立条件，不扩全工具全文。

## 第三批必要证据前四项

11184 [KBVQ-MoE exact-v1](https://arxiv.org/html/2602.11184v1) §4–5/Eq3–8/Tables1–6：input-second-moment加权堆叠experts的shared low-rank full-precision分支，residual VQ后按校准输出mean/std affine compensation。§4 SVD转置/shape书写不一致，不复制为可执行recipe；mean/variance匹配不等MMSE最优或消除全部distribution drift，不接受正gate聚合必放大error的普遍断言。RTX A6000、seed42、RedPajama256×4096、rank1/128、VQvector4/kmeans++100iters。Table2 IDRE/BCOS独立+联合ablation有增益，Table3 KLT有WI反侧，Table4实bits2.01→2.08→2.20/PPL15.30→11.87→11.01：多rank付full-precisionstate，不签名义2bit等预算。Main3bit DeepSeekV2Lite GPTQavg68.89略优KB68.73；原文HE指标部分表述不一致，不授全指标best。decoder1k输入1.58/1.60×未披露batch/outlen/concurrency/SLO，不作生产吞吐采用；不复现。拟仅报告校准分布依赖的shared/residual+输出stat分账，不从组合自动确认长期缺口。

11287 [HiFloat4 exact-v1](https://arxiv.org/html/2602.11287v1) §II/Eq2/Alg1、§III/Eq3、§IV/TablesIII–V：64elements×4bit+32bit三层metadata=4.5bits/value；E6M2 group base+8/16个1bitmicroexponent、S1P2，local range4.81binades，非“真正4bit全部内存”。转换tree maxima→scale/reciprocal→round&clamp，需要专门指令；dot-product microexponent可用shift，理论integer tree后global-scale，不是现存任意GPU直接native支持。Gaussian18×1024² syntheticMSE与近1/3incrementalarea/10%power为设计估算，无fabricatedsilicon/E2E性能。Small7B–14B NVIDIA/Ascend模拟表示值，3seeds/device，emb/head不量化；大模型32/64Ascend910B的vLLM/AISBench，gate例外，具体inputs/batch/runtime NotDisclosed。平均quality较好但individual反侧，未示训练实验（Future Work），不签noPTS/nooverhead普遍训练保证。必要标准证据完成，只采用metadata/dynamic-range/arithmetic路径取舍。

11401 [Latent Forcing exact-v1](https://arxiv.org/html/2602.11401v1) §3/Eq1–4、§4.4–4.5/Table1、§5.1–5.5/Tables2–9：jointpixel+deterministicDINO/Data2Vec latent，两个time变量/两头，latent最终discard无separatelearneddecoder。independent-time训练探索readoutordering与fixedtrajectory训练不同；同一MultiSchedule Table1α1→16 DINO FID27.69→18.65但下采样pixel44.57→42.35弱效，非任意latents普遍。SingleSchedule先latent25步再pixel25步Heun；latentloss与pixelloss时间分治，p_latent调参/samplingweight额外。+secondtimeMLP≈.5%params、可选splitlast4layers无额外FLOPs但DINOproducer成本非免费。受限ImageNet256/ViT-L/80–200epochs，表内FID10k/50k、guidance不合并；200epoch cleanlatents FID16.47而25%train-noise10.93，inference同noise25%反至12.55，说明训练augmentation与推理ordering不能合并。支持语义latent先生成的局部替代分支，不签lossless概率保证或不计encoder的全预算等价；必要支持与直接反侧已读，拟比较Ch24现有joint/multi-time机制再决定Books。

11408 [GHOST exact-v1](https://arxiv.org/html/2602.11408v1) §4/Eq4/Alg1、§5/Tables1–6、§6：Mamba2 scalar-A/groupedstate使逐channel H²×C² localoutput-loss proxy可由forward统计，按layer跨group pool threshold并sequential更新下游校准；不是完整未来observability Gramian，也没有balanced-truncation的全系统误差保证。方法softzero B/C projection/conv；§6明确physicalchannelremove/sparsekernel未来工作，所以不签actualHBM/latency节省。Mamba2-1.3B/H10080/FP32/default2048、WikiText128 samples/batch1/seed42；GHOST50%PPL14.23vsdense13.17/Taylor13.94/SparseGPT13.25，优势是较极端sparsity与short-calibration鲁棒性，非所有accuracybest。130M–2.7B、code/math低绝对accuracy与小差额无CI不授OOD通用优越。二forward/perlayer抽state校准8min vsTaylor8min/45GB、simple<1min，15GB量仅该配置。采用“staticweight≠recurrentstate使用、localforwardproxy+校准”窄机制，未复现；必要支持与直接反侧已够。

## 五批日期原字段与区间恢复

本次实际定点读取 DataCite 压缩原响应 prefix11/prefix12 的 `.data[].id/.attributes.dates` v1 Submitted/Updated 及 Created；后续version字段不授本日修订、不扩审历史。原源：[manifest](../datacite-arxiv-202602-created/manifest.json)、[prefix11](../datacite-arxiv-202602-created/doi-prefix-2602-11-page-01.json.gz)、[prefix12](../datacite-arxiv-202602-created/doi-prefix-2602-12-page-01.json.gz)。官方[availability](https://info.arxiv.org/help/availability.html#announcement-schedule)原保存于[月原记录](../official-arxiv-policy/availability.html)。旧 reconciliation 只复用 raw identity/provenance；其精确 announcement_beijing 合成09:00不授公开秒。

以下三列原值均 UTC、秒精度；最后列仅是 Created 秒桶上界转换为 BJT，**不是公开时刻**。常规 Thu20 EST公告对应 Fri09 BJT、官方batch收录及本批v1 Updated/Created支持工作推定区间 `[2026-02-13T09:00:00+08:00, 最后列)`。不能由 registry 单独证明首次公开；仍需处理 exact-v1 页面已明示的更早正文公开/安全纠错信号。11157 Updated异常且已有2025 workshop正文，必要日期单独隔离，不能套该推定。没有给 EX 追不影响处置的日期。

| ID | Submitted(v1)原值 | Updated(v1)原值 | Created原值 | 推定区间的BJT上界（不含） |
| --- | --- | --- | --- | --- |
| 2602.11157 | 2025-12-08T06:48:17Z | 2026-04-27T00:13:03Z | 2026-02-13T02:47:10Z | 隔离：早公开反侧 |
| 2602.11162 | 2026-01-07T02:29:24Z | 2026-02-13T01:00:13Z | 2026-02-13T02:47:17Z | 2026-02-13T10:47:18+08:00 |
| 2602.11169 | 2026-01-19T06:45:04Z | 2026-02-13T01:00:25Z | 2026-02-13T02:47:27Z | 2026-02-13T10:47:28+08:00 |
| 2602.11174 | 2026-01-19T14:45:40Z | 2026-02-13T01:00:34Z | 2026-02-13T02:47:34Z | 2026-02-13T10:47:35+08:00 |
| 2602.11184 | 2026-01-30T06:57:17Z | 2026-02-13T01:00:49Z | 2026-02-13T02:47:49Z | 2026-02-13T10:47:50+08:00 |
| 2602.11185 | 2026-01-30T07:09:47Z | 2026-02-13T01:00:50Z | 2026-02-13T02:47:50Z | 2026-02-13T10:47:51+08:00 |
| 2602.11192 | 2026-01-30T14:40:18Z | 2026-02-13T01:01:01Z | 2026-02-13T02:48:00Z | 2026-02-13T10:48:01+08:00 |
| 2602.11202 | 2026-02-05T08:35:01Z | 2026-02-13T01:01:18Z | 2026-02-13T02:48:14Z | 2026-02-13T10:48:15+08:00 |
| 2602.11210 | 2026-02-11T02:33:04Z | 2026-02-13T01:01:32Z | 2026-02-13T02:48:25Z | 2026-02-13T10:48:26+08:00 |
| 2602.11212 | 2026-02-11T07:21:49Z | 2026-02-13T01:01:37Z | 2026-02-13T02:48:28Z | 2026-02-13T10:48:29+08:00 |
| 2602.11220 | 2026-02-11T11:51:37Z | 2026-02-13T01:01:48Z | 2026-02-13T02:48:39Z | 2026-02-13T10:48:40+08:00 |
| 2602.11224 | 2026-02-11T13:31:18Z | 2026-02-13T01:01:54Z | 2026-02-13T02:48:45Z | 2026-02-13T10:48:46+08:00 |
| 2602.11246 | 2026-02-11T17:49:32Z | 2026-02-13T01:03:06Z | 2026-02-13T02:49:17Z | 2026-02-13T10:49:18+08:00 |
| 2602.11287 | 2026-02-11T19:07:36Z | 2026-02-13T01:04:31Z | 2026-02-13T02:50:16Z | 2026-02-13T10:50:17+08:00 |
| 2602.11374 | 2026-02-11T21:05:00Z | 2026-02-13T01:09:06Z | 2026-02-13T02:52:20Z | 2026-02-13T10:52:21+08:00 |
| 2602.11401 | 2026-02-11T22:09:58Z | 2026-02-13T01:11:10Z | 2026-02-13T02:52:59Z | 2026-02-13T10:53:00+08:00 |
| 2602.11408 | 2026-02-11T22:20:10Z | 2026-02-13T01:11:46Z | 2026-02-13T02:53:09Z | 2026-02-13T10:53:10+08:00 |
| 2602.11443 | 2026-02-11T23:40:26Z | 2026-02-13T01:14:13Z | 2026-02-13T02:53:58Z | 2026-02-13T10:53:59+08:00 |
| 2602.11456 | 2026-02-12T00:26:53Z | 2026-02-13T01:15:31Z | 2026-02-13T02:54:16Z | 2026-02-13T10:54:17+08:00 |
| 2602.11470 | 2026-02-12T01:01:38Z | 2026-02-13T01:16:35Z | 2026-02-13T02:54:37Z | 2026-02-13T10:54:38+08:00 |
| 2602.11488 | 2026-02-12T02:15:30Z | 2026-02-13T01:18:53Z | 2026-02-13T02:55:02Z | 2026-02-13T10:55:03+08:00 |
| 2602.11510 | 2026-02-12T03:10:44Z | 2026-02-13T01:21:36Z | 2026-02-13T02:55:35Z | 2026-02-13T10:55:36+08:00 |
| 2602.11521 | 2026-02-12T03:30:11Z | 2026-02-13T01:22:39Z | 2026-02-13T02:55:50Z | 2026-02-13T10:55:51+08:00 |
| 2602.11530 | 2026-02-12T03:40:44Z | 2026-02-13T01:23:17Z | 2026-02-13T02:56:03Z | 2026-02-13T10:56:04+08:00 |
| 2602.11686 | 2026-02-12T08:08:03Z | 2026-02-13T01:34:55Z | 2026-02-13T02:59:43Z | 2026-02-13T10:59:44+08:00 |
| 2602.11688 | 2026-02-12T08:09:14Z | 2026-02-13T01:35:01Z | 2026-02-13T02:59:46Z | 2026-02-13T10:59:47+08:00 |
| 2602.11761 | 2026-02-12T09:37:05Z | 2026-02-13T01:38:44Z | 2026-02-13T03:01:33Z | 2026-02-13T11:01:34+08:00 |
| 2602.11786 | 2026-02-12T10:09:13Z | 2026-02-13T01:40:41Z | 2026-02-13T03:02:10Z | 2026-02-13T11:02:11+08:00 |
| 2602.11792 | 2026-02-12T10:17:32Z | 2026-02-13T01:41:05Z | 2026-02-13T03:02:18Z | 2026-02-13T11:02:19+08:00 |
| 2602.11902 | 2026-02-12T12:55:51Z | 2026-02-13T01:48:12Z | 2026-02-13T03:04:58Z | 2026-02-13T11:04:59+08:00 |
| 2602.11911 | 2026-02-12T13:07:36Z | 2026-02-13T01:48:43Z | 2026-02-13T03:05:11Z | 2026-02-13T11:05:12+08:00 |
| 2602.11964 | 2026-02-12T13:58:27Z | 2026-02-13T01:51:19Z | 2026-02-13T03:06:27Z | 2026-02-13T11:06:28+08:00 |
| 2602.11988 | 2026-02-12T14:15:22Z | 2026-02-13T01:52:35Z | 2026-02-13T03:07:04Z | 2026-02-13T11:07:05+08:00 |
| 2602.12021 | 2026-02-12T14:51:59Z | 2026-02-13T01:54:25Z | 2026-02-13T03:07:52Z | 2026-02-13T11:07:53+08:00 |
| 2602.12029 | 2026-02-12T14:59:50Z | 2026-02-13T01:55:03Z | 2026-02-13T03:08:04Z | 2026-02-13T11:08:05+08:00 |
| 2602.12124 | 2026-02-12T16:13:14Z | 2026-02-13T01:59:52Z | 2026-02-13T03:10:23Z | 2026-02-13T11:10:24+08:00 |
| 2602.12158 | 2026-02-12T16:40:05Z | 2026-02-13T02:01:54Z | 2026-02-13T03:11:12Z | 2026-02-13T11:11:13+08:00 |
| 2602.12194 | 2026-02-12T17:27:43Z | 2026-02-13T02:04:08Z | 2026-02-13T03:12:04Z | 2026-02-13T11:12:05+08:00 |
| 2602.12235 | 2026-02-12T18:15:08Z | 2026-02-13T02:06:55Z | 2026-02-13T03:13:04Z | 2026-02-13T11:13:05+08:00 |

Ch5 11246 actual PRE已root批准，2026-10-04本次实际两段窄写于183/185，末注478；root实际读177–195/478后POST通过，确认完整假设与前后衔接，锁已释放。本项Books落实；不代本日日级通过。Ch34 11902 后续两段窄写173/175、末注519也已root实际非作者POST通过，Reference→Beta衔接、负reference/rawmargin、objective变化及误标签/成本/回退边界保留，Ch34锁释放。

## 第四批必要证据（当窗 exact-v1，不借 later metadata）

## 第五批必要证据

12124 [Capability-Oriented exact-v1](https://arxiv.org/html/2602.12124v1) §3–5 Tables1–6/AppendixA1–A4 Tables7–10 L135–294/349–438 实际必要读。四个 deliberately vulnerable reward games 的新采用范围是 controlled transfer/correction persistence，而不是 capability 必然 misalignment。GRPO、Qwen3-4B base/instruct(CoT)、Llama3.1-8B；GPU/seed/完整LR/group/step预算 Not Disclosed，§4.1未列，必要页内find GPU/hyperparameter也无匹配，不伪补配置。ITP与ER分账，Zero-shot跨任务transfer有正负/零，顺序训练RewT即使本任务未学会tampering也让SelfG ER47.1vs32.8，但不能独立归因generalmetacognition。Table6反驳RL总比SFT更难修复：QwenBaseContC GRPO31.1<SFT46.7，RewT两者100，LlamaSelfG40.5vs0。A2去除exploit reward对照instruction模型ER大降，但Base RewT仍74.2（original7.1）；作者预训练correlation解释未经独立消融，不签‘纯capability致害’。A3 Qwen4→8BContC ER55.8→24.7反驳scale必增；A4实际audit概率vsprompt警告分开，无actualaudit时高警告仍可高ER。仅有限受测训练与漏洞交互/迁移盲区，未生产复现；必要支持+直接反证够停止。

12158 [SafeNeuron exact-v1](https://arxiv.org/html/2602.12158v1) §3.2–4.4 Tables1–3/AppendixA4–A6/B/D L125–279/437–505/516–541实际读。ES是pooled-std standardized mean gap/Cohen-d而非Welch-t，A5/A6标准error含sqrt(1/ns+1/nu)，不能照抄ES阈值为固定standard-normal calibratedFPR或统计显著保证。SAS layer-relative正shift与ES取union。正文冻结identified neurons、DPO其余参数+逐次union；Alg1同时 forward activation zero+gradientmask，比单纯weightfreeze更强，实施语义不一致隔离，不授代码已验证。StrongREJECT313+LlamaGuard3judge，GeneralARC/TruthfulQA/GSM8K不是benignrefusal集，不能签无overrefusal；Table1 Qwen14B Fullprune56/313vsRLHF255，但Gemma两者23/313、DeepSeek1.5B original Safe257 vsRLHF252，并非所有模型收益。Table2 iterative Qwen7B Fullprune279→183→169→158，GSM8K.7362→.7096→.6952→.6899，不能签无能力代价。未见等预算random-neuron/adaptive-reidentified attacker控制，移除选定set结果不证明全部安全机制因果/万能redundancy。B unsafe三源/safe natural_reasoning；StrongREJECT不重叠作者声明，PKUSafeRLHF83.4k随机20%、SPA-VL100788随机1%，30/70safety/generalmix，DPOβ.1 LR5e-6 wd.05 epochs3/cosine，NVIDIA‘RTX H100’原硬件名保留，count/precision/batch/repeatedseed ND。只采有限selection/freeze-prune再训练的局部鲁棒性取舍，不采用形式识别/通用安全保证；关键反侧够停止。

12194 [MalTool exact-v1](https://arxiv.org/html/2602.12194v1) threat§3/method§5/eval§6–7/limits§8 L126–132/188–305/322–490实际必要读。仅untrusted工具开发者/代码实现，既已installed+invoked条件下测试，不授恶意工具被自然agent发现/选用概率。Verifier收集specific synthetic runtime sideeffects+AST multisetJaccard τ.7并反复生成直至accept；ASR=1是accepted corpus的条件成功率而非one-shot/allattempt/allagent-end-to-end attack成功率。三个开源GPTOSS20B/Phi4/Qwen3Coder30B与安全版/三API，1200standalone(12×100)；Trojan将accepted代码放entry无条件区域，‘mustexecute’未排除precedingstatement异常/inputs不满足/环境权限。10573英语Python fastmcp可取源码tools，5287Trojan/5286benign，原库benign无独立逐个确认；Table9实际各类n合计1196与全文5286标签有冲突，不签全5286扫描。VirusTotal因API每behavior100Trojan；combine是任意flagOR，FNR下降伴高FPR，资源/DoS仍高FNR，不能签scanner可靠安全。FPR benign可能少量真恶意，需保留labeluncertainty；body暂无完整scannerversion/硬件/重试/测试clock绑定，Not Disclosed，不为列benchmark扩全工具实现。只采具体code/description审计差额及FNR/FPR评价反侧，非新通用CIA原理，未运行攻击/复现或下载受限maliciousartifact。

12235 [Overflow exact-v1](https://arxiv.org/html/2602.12235v1) §3–4 Tables1–2/limits/A–B/D L99–308/335–356/377–410实际读。Operational overflow=uncompressed正确而compressed错，不是物理熵capacity证明。xRAG7B+SFR-Mistral、SQuADv2/TriviaQA/HotpotQA（均xRAG训练dataset类别，testexamples过滤uncompressedcorrect）；SQuAD GPT4omini semantic judge日期校准ND，其余substring EM可掩盖错误。query/context concat pre/postprojection probe AUROC.703/.725/.720，postinference.713/.719/.733接近但没有equivalence test，不能签生成无因果作用。saturation可分tokentype却overflow.529/.568/.533近随机，queryjoint优于contextonly；具体反侧支持condition-query而不是仅intrinsic saturation。5-foldstratified80/20 CV（context/group重复隔离ND）、SQuADvalidationtune后fixed其他datasets，b256/Adam1e-4/standardscaler/epochs150linear50MLP/earlystop20；硬件/seed/样本总数/latency/阈值precisionrecall/端到端gate或chunk改写收益ND。adaptivegate/chunk仅future，不签已部署省token/nofalse-negative可靠性。仅单token短passage/此架构、有限检测条件的原增量，必要支持和反侧够停止。

日期定点恢复：11521 首页 MICRO58/2025/placeholder DOI触发早公开核验。一次 exacttitle+authors 检索，以及[官方2025 program](https://microarch.org/micro58/program/index.php) exact `PAM:`/`Lian Liu` 两find均无匹配；不能由placeholder或absence证明首次当窗，隔离日期。需求为作者/出版方可核同title+7authors实际prior-publication身份/首次公开版本记录；无此材料不入当窗正面候选/Books，不扩venue全历史。

11964 Gaia2 早公开信号：[Meta官方ARE publication](https://ai.meta.com/research/publications/are-scaling-up-agent-environments-and-evaluations/)原日期September22,2025、§abstract已有ARE/Gaia2 async及costtradeoff；官方PDF链接一次CacheMiss。共同作者[发布blog](https://huggingface.co/blog/gaia2)September22,2025 L97–130公开read/write、timed environments、同101tools/T.5/16Klimit、GPT5high与KimiK2排行和paper入口。当前2602.11964v1题改Gaia2，拟贡献同早发布家族；需root确认是否可直接认窗外，或最小旧正文/同家族身份差额。不得仅arxiv Feb13重新计首次/评分，已读机制暂不采用。

11510 [AgentLeak exact-v1](https://arxiv.org/html/2602.11510v1) §III–IV/§VI/§VII/A L143–265/315–421/470–521/546–554/586–588实际受影响深入。允许集/每channel必要披露为benchmark policy；内部超量披露不等外部实际breach，不能签法律合规。五模型/1000English scenarios/4979model-scenario paired traces，排21timeout；coordinator-worker仅2agents、OpenRouterT.7/max512、framework版本范围，C1/C2/C5全量而其他channels部分sample/SDK，不授七通道全量。H1=2076/4979=41.7%是全部轨迹占比，不是违规中的41.7%；memory无独立新增H1。single C1与multi C1 43.2/27.2，prompt结构confound未ablate，不授多agent必更泄露。Qwenjudge heldout200调τ.72、1000testFPR4.8/FNR7.4，非零FP使作者‘lowerbound’不成立。120scenario拦截将内部31.5→2.4但TSR78.6→73.9，即4.7pp代价；不用aggregate不同威胁/defense比例串因果。只采输出审计漏internal policy与selective disclosure utility取舍。

11786 [APST exact-v1](https://arxiv.org/html/2602.11786v1) §3–5/Table1–3/A1–2 L148–280/284–452/480–494实际受影响深入。同90risk prompts/四模型，shallowT0×3 vsT0×100/T.5×50/T.8×20，phase1 Gemma20calibration非crossmodel。judgeGPT4omini20240718/T0 plainJSON/200max，2025Dec–2026Jan实验；hardware/模型endpoint精确版本和人类judge校准NotDisclosed。独立Bernoulli是近似，不同文本不证明独立；单次pf不因depth数学增大，至少一次失败prob与pf分账，prompt bootstrap不授query时间相关有效样本。Strict/Medium/Broad依harm/nonrefusal/gibberish选择，Table1–2 Strict .0536/.0126与§5.1.3 prose .0634/.0101冲突，采用同口径Tables不拼数。温度不是普遍更高更坏，OSS端点pf反降CI不含0，其余跨0；hypothetical225prompt cost与实际90分账，Q×pf外推需要同分布/配置，不授生产风险减少因果。仅采depth条件的评价盲区与label定义影响排序，不签安全保证。

11792 [RLVR structural convergence exact-v1](https://arxiv.org/html/2602.11792v1) §3–5/Table1–2/§5.3–5.4/B3/C/D L118–226/258–264/376–392实际必要读。Qwen7B GRPO/DAPO200steps、300prompts×32completion diversity，bothseen/unseen都变rigid，structuralcluster非只有一条CoT，不授‘所有RLVR必collapse’。min10 nearest-edit of32 sample-only detector八设meanAUC.70，QWSAT仅.57；公开model300train vs300不同math来源可能难度/分布混杂，controlledSAT/K&K补例不授零FP membership证明。8H800/vLLM TP4/8/T.7/topP.95/out1024；32sample6.65s是ORZ7B单项不授便宜普遍。k/temperature/截长影响signal，PPL低pretraincontamination子集也是proxy选择而非真实pretrain因果隔离。只采sample-structure相对tokenlikelihood的RL-exposure证据与访问代价，不授threshold posterior/单题确定成员。Books具体比较待办。

11688 [GORGO exact-v1](https://arxiv.org/html/2602.11688v1) §3–5/§7–8/Table2–5 L129–286/313–348/383–426实际读。v1标题为 Maximizing KV-Cache Reuse…，当前metadata Online Tuning/frozen heldout-p95不是v1证据；§8自动权重调参是FutureWork，不扩大revision史。mirror prefix trie非exact engine KV，不传KV payload；RTT+未复用prefill+admission的additive cost为heuristic，依赖telemetry freshness与compute率稳定。三域各8A100/Mistral7BInstruct-v0.3/WildChat+GuideLLM，60s/10 concurrent；不同策略完成100/85/57/141 requests，未披露重复/CI/等fixed-trace配对。proxy medianTTFT224.55ms vsleastload568.27，但proxy ITL16.13ms高于12.46；decentralized吞吐降且计算sidecar/trie非免费，不能签所有指标胜利或p95自动调参因果。预定只采这一具体TTFT/ITL/telemetry取舍；必要支持与反侧够，未授Books。

11686 [LAER-MoE exact-v1](https://arxiv.org/html/2602.11686v1) §3.1–5.5/§7 L151–382实际必要读。all-expert chunks持久分片，每次All-to-All仅restore指定C个expert，恢复目标可换layout，gradient逆向reduce；solver CPU异步给next iteration，当前GPU lite-routing仍同步。prefetch跨MoE计算且gradient延迟额外临时memory，通信量近似相当不等零通信；balanced负载Eq1要求足够tokens，可在小microbatch/网络弱时失去overlap。Eq3文本把perdevice容量写成sum_i A_i,j=C索引不一致，不复制NIP公式为可执行约束；不是机制失效证明。4节点×8A10080/NVLink300GBs/IB800Gbps，dropless，8Kcontext/20warmup+50step均值，Mixtral/Qwen改层数configs，FSDP+EP也加入同overlap，FlexMoE是作者复现scheduler非原artifact；max1.69×只受测。4KMixtral同aux1e-4 loss误差<1e-3，不授所有质量bitexact；globalpeak memory改善不显著，balanced负载gain相当。新分支是restore即relayout避额外持久迁移，而非全局optimal/永不solver瓶颈。未授Books。

11761 [MiniCPM-SALA exact-v1](https://arxiv.org/html/2602.11761v1) §2/Table1/§3Table2–4/Fig2–3 L70–204实际必要读。25%InfLLMv2 sparse+75%Lightning继承intermediate7T checkpoint；HALO初阶段只linear层训练1.3B/512，之后全部参数约2T，多stage短到长才开稀疏。HyPE linear使用RoPE、sparse无RoPE，为该架构position接口，不外推所有hybrid。省25%是新增data量对8T fromscratch，非总训练FLOP/从零因果对照，已付7T不可消失。Table2 IFEval/MMLUPro有降，Table3 MRCR多needle不总胜；ultralongQwen引用官方值，不同training/evaluator预算未隔离，NoPE因果未ablate。A6000D96GB/509032GB、GPTQINT4或未量化、input64K–1024K/output1K；TTFT不是单decode速度，总资源/throughput并发/重复及CI NotDisclosed。不授参数量即质量/length无损普遍保证；配方可行性报告，owner具体比较待办。

## 第三批后续必要证据

11902 [HyPO exact-v1](https://arxiv.org/html/2602.11902v1) §3 Eq7–13/§4/Table1–2/§6/A2–3 L107–264/288–317实际必要读。当Δref<Δθ<0，DPO sigmoid weight已衰减而sequence preference绝对margin仍错；max(Δref,0)只改变该对的reference anchoring，不等完整KL正则保证、生成正确性或sign可靠标签检测。主表还加SimPO更强reference与h10，Table2去二者仍高于DPO才支持核心，不把所有增益归clipping；optimistic pairs mismatch仍存在，labelnoise时reference正确反对错标却被更强推错。UltraFeedback约61k、Mistral7B/Llama3 8B Base+UltraChat200k SFT或Instruct，1epoch/2048length/b128、4H10096/BF16/ZeRO1CPUoffload；LR/β有限grid最低validationloss，AlpacaEval2/ArenaHard GPT4Preview1106 judge，不同生成温度、greedyArena分账；7.1vs7.2h仅同配置本例不授所有零overhead。主张涉及DPO失败条件，受影响深入机制/反侧够；Ch34现有reference/correctness分账是否已经明确Δref<Δθ<0需具体比较。

12021 [H-LRU/BD-LRU exact-v1](https://arxiv.org/html/2602.12021v1) §2–7/Prop1/AppendixC–E L88–269/422–484实际必要读。higher-order companion temporalmix不等dense blockchannelmix；input+state joint row-L1≤1配零初态，triangle/induction给∞norm≤历史input最大值。不能仅每步eigen≤1推出任意非正规时变乘积稳定；本处可用同一induced∞norm，非strict asymptotic/gradient不消失保证。m>1结构增加expressivity但scan每block matrix product m³，H-LRU参数匹配需更大state与memory；m16语言质量反降，negative/complex eigen alone无法解permutation，宽度不能补结构仅受测。synthetic四设置Table1为三LR×五seed中best-test、非平均seedCI；A100/H100训练/H100吞吐、6144maxhidden单层，FineWeb210M/10B单H100，PyTorchmaxautotune硬件占用改变runtime排序。适中block受测质量/吞吐取舍，不签LLM普遍无损。稳定界需要零初态、共同norm、inputgate共同预算，owner具体对照待办。

FERRET 必要日期隔离的原 fbcdn URL（未以之授当日正文可见或时间）：https://scontent-iad3-2.xx.fbcdn.net/v/t39.2365-6/632229731_1973868306865022_6023070714278759451_n.pdf?_nc_cat=111&_nc_gid=3NajZgdC_eNckOBzy0i3XQ&_nc_ht=scontent-iad3-2.xx&_nc_oc=Adp_c3GPjVvo061xqKwvzieNKYZoP33r7ctAPKauzSJi6ej54j8Rg9ToTAgsEW4xsKs&_nc_ohc=WPyyWW6enFMQ7kNvwEoGTNR&_nc_sid=3c67a6&_nc_ss=78100&_nc_zt=14&ccb=1-7&oe=6AC7ABAE&oh=00_AQMBPgVj7n2UoX9v26QtHARHPNHhHb7S-reXo3taNLZEEQ 。arXiv exact 2603.10010v1 原 Submitted 2026-02-17T20:59:14Z；不得用该字段替代官方 Feb13 首公开 clock 或猜月份归属。

11521 [PAM exact-v1](https://arxiv.org/html/2602.11521v1) §4.1–6.3/§7.1–7.6 L182–451必要读。分布式online softmax思想与Eq5使用normalizer sum；Alg1 L260却返回m+log(sum l)，outer L238直接O/l，与该语义不一致，不复制为数值等价可执行代码。controller侧command reorder/addressgen/re-layout buffer承载真实跨tier布局迁移，而非仅logical view；EWMA λ.6、10decode activation window/greedy importance tier ratio是受测profile heuristic，不签workload-agnostic最优。8H10080/1280GBDDR4/8TBSSD、4TP2PP、FP16/BF16、8×KV压缩由多工具模拟，验证与vLLM/AttAcc模拟交叉而无披露误差，area是Verilog综合非fabricatedPIM。ShareGPT/WildChat/HumanEval平均input/output183/299；离线1500–8000，batch固定256/512/1024或16/32/64，online SLO100/150/200ms的peakbatch；不授生产tail/租户/QoE。小模型cache全HBM时收益较弱，migration .7%/SSD<.1%为受测，不授任意context稳定。HBMlogic旧制程面积可27.7%而非9.25%，功率假设PU=3×read。仅采用controller布局迁移依赖，公式正确性/无质量代价与性能保证隔离；root正定点核归一化冲突，不扩全artifact实现。

11443 [FANNS exact-v1](https://arxiv.org/html/2602.11443v1) §4 Eq3–7/§5.1/§6.3–6.4/§7.1–7.2.8 L252–613实际读。GLS=local/global filter selectivity ratio的有界transform，local-neighborhood k2048，低global selectivity下finite-neighborhood zero使均值偏负，不能当独立性因果证明。MoReVec768维gte/normalize、movie/review 3scale最高551155/2598267，1000query每filter×k1/10/40/100，只scalar inequality/nojoin、不测categorical/stream/disk；FAISS1.12CPU/Milvus2.6.6/pgvector.8.1 PG16，Ubuntu24.04/XeonE5-2660/256GB，全RAMsingle-thread单query只一次，不授tail/concurrency或RAG答案quality。Knowhere双队列navigation/results与93%filter-out exactscan/fewer-than-k safetyfallback使高recall不等HNSW算法更优；segment ablation反驳其初始scatter-gather解释。pgvector从k20→21即可换plan，metadata Btree影响可见plan，forced exactfilter可能同latency更高recall，costmodel不自动保障quality。标准必要支持与直接反侧够，只采plan/GLS条件化评价，不签作者‘universalconstraint/guarantee’。Ch76当前1041只有selectivity-error→plan-regret phase boundary；尚需读现有physicalplan实际覆盖才能Existing/差额。

11470 [Cachemir exact-v1](https://arxiv.org/html/2602.11470v1) §2.3/§4–6/§7.1–7.5 L179–385实际读。semi-honest two-party/plaintext servermodel，不授恶意server、模型抽取/sidechannel或完整部署confidentiality。interleaved replicated VMM packing减少slot浪费/innerrotation，extraction mask与RoPE/SiLU/norm/KVupdate融合减少level；K/V布局不同但保持下一projection兼容。cache减少activation size使bootstrap placement需要operation/submodule-level重新规划，不是沿用prefill规则；Orion DAG pruning依赖negligibleleveldrop/monotoniccost等模型，不签所有cost下globaloptimal。CPU Lattigo/customPhantom GPU/Xeon8558P192threads/A10080，CKKS N'=65536/N32768/1763bitmodulus/L13/K15，作者128bitsecurity参数声明非本次cryptanalysis。baseline latency按operation计数×测均值估算非同实现E2E；§7.3 GPU additional158×不得都归packing。输入64/total512为Table5，3.02seconds是一个decoder层/生成step，完整Llama8B作者为1.61minutes/token，不签interactive实用。MRPC/WikiText有限approximation评估、无general generationbudget/quality保証；KV1024≈17GB而weightplaintext hundredsGB非普通BF16memory。标准计算机制证据够，不采用形式安全/普遍性能；当前Ch72 HE/MPC共同绑定encoding/layout/operator/threatmodel已有原则，专门CKKS packing/bootstrap配方拟仅报告，未写Books。

11456 [SparrowRL exact-v1](https://arxiv.org/html/2602.11456v1) §3/§5/§7.1–7.7 L119–308实际已读；later metadata AuroraRL不替代v1标题，也不单凭改名开revision。small-lr BF16连续权重差分的受测非零率约1%，不是未舍入实数梯度天然稀疏定理。delta由idx/val、固定fused QKV/gate-up mapping、sorted offsets/LEB128编码；base-version匹配，先stage再batch-safe scatter-add并提升epoch，lease/hash约束结果接受。无损indices/传输不独立证明任意BF16差分再加回bit-exact；原稿未给post-reconstruction tensor bit comparison，只采用协议与受测payload机制，不签无条件bit-exact/noqualityloss。800steps是lr1e-6稀疏率profile，系统run仅7optimizersteps，rollout group512。Ubuntu24.04.1/CUDA12.6/FSDP2/vLLM，Qwen3 4/8/14B，2/4/6H100 trainer +4/8/12A100 actors，US–Canada native500Mbps–1Gbps；IdealSingleDC通过替换trace网络cost估算，非actualRDMA实验。稀疏抽取~5s，4.71→2.90s传输与生成overlap，不是零成本。cost对照GPU类型/块粒度不同且省略egress，hardwarecapacitymatching为作者估算。标准必要证据够；当前Ch36 1085–1087及1822真实承载该publication branch/base/partialvisibility/lease/fallback，拟已有覆盖，不复制bit-exact普遍保证。

## 第六批准入与必要证据

root实际完整题摘校准：11166、11171、11201、11236、11244有具体机制/反侧；11217一次core§4.3确认inverse accuracy/confidence transfer与data/scale反侧后窄5准入通过。11167仅样本/形状可视化无新增机制或评价盲区、11176活动预测应用、11180综述排除。11181一次core安全段全为既有引用；11199 storedrubric/judge/userloop、11241 majority伪标签+课程组合、11170 verificationprompt component且budget变动，均未建立新条件，root实核一次core后EX通过。完整题摘仍定位inventory.json；一次core缓存[V3_BATCH6_DECISION_CORE.txt](./V3_BATCH6_DECISION_CORE.txt)，不用新平行账本。

11166 [Small Updates exact-v1](https://arxiv.org/html/2602.11166v1) §3.1–3.2/A/G L95–113/161–243/299–314/385–390实际读。三instruct模型3B/7B与LoRA/PiSSA/DoRA同r32/alpha64/attention qkvo，AdamW2e-5/b64/1epoch/BF16；8A6000或API。TriviaQA/NQ闭卷、SQuAD给passage，2500train/500val/~2000test（NQ1805），GPT5mini judge/少量拒答排除，judge人类校准、sampling温度/次数、repeat/CI ND。detector分离提高但accuracy只有小增，不等事实知识因果；PredEntropy和AUPR有反退，whiteprobe不一致。模型各自median阈值定义danger，不能签固定风险gate或跨模型calibration；probe按val选层再test，PCA/linear separability≠epistemic机制证明。只采不应以任务accuracy替代检测可分性、也不反向以AUROC授安全；局部诊断仅报告，不制造新通用principle。

11171 [Language-aided BO exact-v1](https://arxiv.org/html/2602.11171v1) §3/§4 Tables2–7/A/B/C L108–125/165–218/242–312/413–433/533–552实际读。冻结Qwen2-7B最后token embedding3584，经domainprompt+可学token与projection映射GP；marginal likelihood联学kernel/projection/token，Matern5/2+EI，45000离散候选非45000实际train。10%random subset代理，30iterations同design space；LoRA任务模型7/13B等，seq1024/1epoch/2A10080。rank等参数改变FLOPs，Table5 NOMAD180h与ours24h预算矛盾，不签equal-wallclock；subset相关不授argmax/ranking保序，A9 MATH10%r=.6578，不普遍可靠。componentablation支持本例learnedmapping与token收益，跨family配置明显失效，seed/CI/precision/evaluator版本ND。原增量是离散LLM表征→可调连续GP接口，非成熟BO本身；仅报告这套HPO配方及proxy条件，不泛化搜索最优或通用迁移。

11201 [NLDD exact-v1](https://arxiv.org/html/2602.11201v1) §3–5/Table1–2/limits/A3/A5/A6/Table6 L106–267/339–392/435–446实际读。single-step反事实后截断其余steps，token/log-PPL筛选；clean-correct与|LDclean|>=1e-6条件、100/task、3模型6.7/8/9B、greedy/BF16/HF、GSM首tokenmargin，seed42/BCa10000。NLDD分母抵消globalS，不授softcap架构无条件可比；截断混合弱step依赖与早前步骤已够，不是内部利用的唯一因果证明。linear step-probe可读栈深不等最终答案正确，train/test同chain隔离ND；GemmaDyck Table1accuracy0但A6全部conditionclean-correct+Table6NLDD非空构成中心协议冲突，Table1 prose还对调Llama/DeepSeek PrOnto数。horizon并非统一70–85%，多为边界100%，无实际runtime剪枝验收。保留设计反证准入，不删除或降分藏冲突；mapping-gap/causal-pruning中心主张暂缓，不进Books，需原clean-correct筛选count与样本/统一accuracy定义或勘误重开。

11217 [Magic Correlations exact-v1](https://arxiv.org/html/2602.11217v1) §3–4.3/B2/C3.1 L175–239/285–337/446–481/626–630实际读。240M/1B各9data mixtures，20benchmark，选中答案probability均值；PT→SFT Pearson跨mixture不是individual calibration，category alignment跨benchmark均值不等样本概率校准。accuracy transfer增强而confidence减弱，FineWebEdu/NLI方向跨scale反转支持不能单用PT指标选后训练。正文PT12B/52B与Table2 b256×4096×200k不一致，SFT正文5epochs但table1B10，scale兼预算/LR变化不授architecture因果。BF16，hardware/seed/CI ND；窄5仅报告该predictor反侧，不授‘fingerprint’个体稳定或数据过滤通用收益。

11236 [ABot-M0 exact-v1](https://arxiv.org/html/2602.11236v1) §3.1–3.2/§6.1/§6.3 Table7 L191–235/303–305/379–402实际读。预测clean A但输入noisy A_tau，velocity=(Ahat-A_tau)/(1-tau)，训练等价weighted action MSE；仍迭代ODE denoising，非显式物理可行manifold投影，tau=1处理ND不抄普遍约束证明。Qwen3VL4B+.16B DiT，6Mtrajectory FASTpretrain/3Doptional，224image/100ksteps/b1024/LR1e-5，默认4steps/chunk16。匹配backbone/expert去3D的AML对照在RoboCasa chunk30 62.8vs45.7，chunk10 72.4vs69.3，长chunk仍质量下降，4vs10step非单调。hardware/dtype/episodes/seed/CI/latency ND；总体98.6不单归AML。可支持x0式action参数化局部长chunk取舍，仅报告，不签免迭代/物理安全/真实机器人普遍转移。

11244 [REVEAL exact-v1](https://arxiv.org/html/2602.11244v1) §3–5/Table6/§10Table11/§11Table12 L144–178/183–285/560–596实际深入读。humanverified错premise、shuffled/blank同prompt对照、NextQA互补遮挡（audioremoved/4倍frames），区分taskaccuracy与temporal integration；5humanannotators，NextQA-T196/S183，Gemini24fps/GPT75frames/OSS64frames。OSSblank10s vsclosed33s，不跨family排榜。遮挡视频包含全部pixel不等模型采到全部；Table11七mask变体各25videos仍非inputcoverage证明。四象限sequential-mosaic n100全图对照/跨边界文字与multiobject，Gemini40/Qwen32B6/Qwen7B4/LLaVA2/human84，支持有限整合诊断；未披露各模型实际四帧coverage/temperature/GPU/repeatCI，不能签‘strictlyarchitectural’或frame-independent编码是唯一因果。camera prompt用5视频迭代，annotation残余偏差/生成judge、2D synthetic不授真实3D普遍结论。反证深入支持与反侧够；仅报告诊断，longterm机制因果不足，不复制架构必败宣传。

第六批原日期（UTC秒精度）：11166 Submitted2026-01-17T21:39:24Z/Updated-v1Feb13T01:00:19Z/Created02:47:23Z；11171 Jan19T08:48:03Z/01:00:28Z/02:47:30Z；11201 Feb04T21:55:57Z/01:01:17Z/02:48:13Z；11217 Feb11T09:46:40Z/01:01:45Z/02:48:35Z；11236 Feb11T16:47:01Z/01:02:37Z/02:49:02Z；11244 Feb11T17:39:14Z/01:03:00Z/02:49:15Z。Updated/Created后三字段均2026-02-13；原prefix11实际定点read，官方schedule/batch的推定区间起点09BJT，上界分别10:47:24、10:47:31、10:48:14、10:48:36、10:49:03、10:49:16BJT（不含），不是精确首次公开clock。仅manuscriptSubmitted日期不是早公开证据。

Gaia2 11964官方Meta ARE页2025-09-22日期+同摘要机制/matchingauthors与HF2025-09-22公开页实际root实核，确认早公开，窗外关闭，不评分，不按本批arXiv重新作新首次事件。缓存[V3_GAIA2_PRIOR_PUBLICATION.txt](./V3_GAIA2_PRIOR_PUBLICATION.txt)保留本日发现原依据；不读旧全文/修订全史。PAM11521 MICRO2025早公开矛盾未解决，first-public终态日期隔离，不把program no-match当不存在证据。

## 第七个有限主题片段

原title查漏限定Agent/tool/memory、模型表示/推理、WorldModel与生成分支，完整题摘实际13，inventory身份11213/11243/11247/11291/11304/11348/11351/11361/11364/11388/11389/11395/11409。root实际完整读题摘校准：6potential11213（flat surrogate+离散trigger跨分布transfer/stealth条件）、11243（structure组织≠recall且prompt依赖反侧）、11361（paraphrase top1 mismatch定位→criticaltoken替换+parallel一致性）、11388（frozen SAE/oracle active-manifold certificate条件）、11389（objectmask改变observability/prediction分支）、11395（highnoise PCA+later learnedRFM离线跨noise复用）。尚非证据/Books通过，不签真值/架构因果/普遍证书。

11304 once exact-v1§6–7 L243–294支持窄潜在盲区：Table7 fabricated<6%/Table8cite>85%仍Table9 source-reconciliation/staleness/missing-risk，structured error≠holistic score，干预弱model regress；不是crypto应用指标自动准入。11348 once§2.2 L142–160/§3.6 L243–247支持middle-stage noise跨4family更敏感的潜在新条件；proxy生成冻结/solvability只是评价方法，不能签固有架构和任意任务保持可解。两项必要核验继续。

4EX经root题摘校准：11247 weightedmean不积累、成熟CUSUM类比/pattern聚合无新有效条件；11291 logical+visual hierarchical输出泛述无新coupling条件；11364 noise-reconstruct+NLI/conf融合/thermodynamic类比不建立新truth成立条件；11409成熟surprisal/repetition/coherence+tail/MAX组合未具体新失效边界。11351 once §4.2 L128–160 teacher behavior SFT+连续user询问penalty/未成功且turn预算未用满penalty，成熟rewardshaping组合没有新增informationgain正确性/成立边界，拟EX，缓存[V3_11351_DECISION_CORE.txt](./V3_11351_DECISION_CORE.txt)，root待最终core核，不扩全附件。

MiniMax [M2.5官方core](https://www.minimax.io/news/minimax-m25) L118–127：Forge中间层/async/tree merging40×未披露新dependency算法或可比配置，CISPO沿用，processreward泛述，EX。2026.2.12时区未核但不影响EX；不继续追发布日期，不单凭新benchmark/厂商宣称评分采用。目录历史缺段仍保留，不能以EX取消来源限制。

11530 [Pascal exact-v1](https://arxiv.org/html/2602.11530v1) §II-D/§III/§IV algorithms1–2/§V-A–D/§VII L106–326实际已读。reasoning+prefill计入time-to-first-answer，不同于engine prefill；answer阶段threshold QoE允许pacer缓存遮住有限preemption。高/低优先队列各RR，reasoning KV>5000tokens可demote，不是reasoning永不抢占。transition token触发placement/migration，选SLO通过且低reasoningcount，若destination无memory而source有则不迁移；两队列quantum500。八实例H10096GB/100Gbps是profile-based模拟，单实例对实际Xeon8558/H100/vLLM0.6.1/PyTorch2.4/CUDA12.1验证E2E MAPE1.62%，TTFT12.6%、TPOT6.49%；trace length来自o4-mini而cost模型是R1DistillQwen32B，非真实cluster/model输出质量验收。QoE最终只测first-answer后TPOT，TTFT单列，与§III TTFAT设置不同；tail bins按样本数切max/P90/P95/P99，不能统称P99。Migrations p99 .14/.25s是模拟，不授任意链路可忽略。adaptive反侧NonAdaptive SLO7.45% vs.69%，memory-free/no-migration仍可能transition blocking27.39s；reasoning-heavy短answer workload对RR gain缩小且部分TTFT增加，有限capacity无法永远SLO。standard支持与直接反侧足够；Ch56初检有reasoning/answer budget与slice切换，但尚未见这一QoE/preemption/phase-boundary queue分支，需完整具体owner对照再决定是否长期差额。

## 第七批必要证据与实际写回同步

B6六项必要原文支持/直接反侧已由root实际独立核通过：11166/11171/11217/11236/11244仅报告，11201保留中心争议暂缓，不删候选。11351决定core §4.2已root实际核，EX通过。三Books新增 actual POST 通过：12021 MODEL-LONG-CONTEXT Ch22正文485/487与末注1288；12029 INFER-PD-DISAGREGATION Ch55正文64/66与末注672；11530 INFER-SCHEDULING Ch56正文223/225与末注1949。均两段支持、直接反側、原owner差额先由root PRE核，实际正文/邻接/末注非作者POST核，窄锁释放；连此前11246/11902共5实际整合，不代日级验收。

11213 [STAB exact-v1](https://arxiv.org/html/2602.11213v1) §3.1–3.5、§4.1–4.4/Table3–4实际必要深入：public surrogate可投毒训练集/不知victim参数，5% poison、SAM+Gumbel软identifier分布与MMD一致/多样性，PLBART-base/CodeT5-small在Python3数据、methodname/summarization和9迁移组合；Table4两组件移除退步，Table3检测仍非零而非隐身。SAM flatness→distribution-general trigger是解释而非定理，软MMD不证明作用域/语义保全，非现代decoder LLM代码执行风险实测。surrogate2enc2dec、100优化iteration、rho.02、tau1、lambda.1、victim15epochs早停；硬件、精度、seed数/误差±定义Not Disclosed，未运行投毒/实现。6=2+2+2，安全反侧深入。仅报告：条件性code-model防御失效证据，不建立新的通用防御或生产安全保证。

11243 [StructMemEval exact-v1](https://arxiv.org/html/2602.11243v1) §3–4实际必要标准：73 synthetic scenarios/544queries，树/状态/净额任务，输出EM或judge而非内部结构直接验证；Gemini2.5/3Pro不同任务换backbone，retrieval top15/10/5，默认Mem-agent/Mem0+hints比较。hint增益大于两memory框架差额、count选Gemini3因2.5幻觉、反复updates生成spurious memories；额外context/工具/维护预算没有matched总成本，hint救回与“错误仅源于组织”的归因不严格。5=2+1+2；仅报告：具体评价反侧，不授复杂memory必胜或hint因果纯隔离；硬件/precision/repeats/CI Not Disclosed。

11361 [PPCV exact-v1](https://arxiv.org/html/2602.11361v1) §3.1–3.2 Eq1–6、§4/Table1–4、§5实际必要标准：原greedy trace teacher-force到多个同模型paraphrase，top1 mismatch的概率差max选一个位置，top10替代token跨原题+paraphrase续采后按answer一致性选。保持语义是prompt要求不是证明；一致性不是真值，Table1 Mistral GSM8K56.58低于Phi56.60，extra样本预算大致匹配不等tokens/墙钟完全相同。A100/vLLM、最长4096、math4/ARC3paraphrases、lambda2，SC48samples、其他4–8×5–8steps；GSM8K/SVAMP局部6–8×CoT延迟，不能采免费verification。相似权公式分母exp(-lambda*n)与描述冲突，不采用精确weight公式；可采局部token敏感性启发式。6=2+2+2；仅报告：局部decoder策略及成本取舍，不授自动正确性或新的可部署控制门；precision/CI Not Disclosed。

11388 [SSD exact-v1](https://arxiv.org/html/2602.11388v1) §3–4.9/Thm3、§5/Table1–3实际必要深入：模型与SAE需先于独立IID评估样本冻结，有限class是全部大小P mask，bound包括restricted empirical loss、dense/proxy gap、population pool mismatch eta与union penalty，不解释训练选择为何泛化；§4.8明确fixed-M直接Hoeffding更紧。§4.9忽略empirical eta估计罚项，不签实验数即完整证书；Table1实际P几乎m而非少量全球语义features。GPT2-small/Gemma2B，layer6/12，seq32，TopK64、batch16、alpha.5、delta.05、6250cal/70000eval；OOD提高risk/mismatch且gap下降，不能由proxy重构好推出质量。§5.3原encoder非固定TopK的k统计，Table3code Gemma64.32>60.31却caption称shiftleft；k>500是提议不是实现/calibrated gate。7=3+1+3。仅报告：限定posthoc分解与失效反证，不采用稀疏性自动证书、安全门、70B外推；硬件/precision/seed Not Disclosed。

11389 [Causal-JEPA exact-v1](https://arxiv.org/html/2602.11389v1) §4、§5/Table2/4/6、§6actual必要标准且formal子命题深入：冻结object encoder、整段对象history mask保留首identityanchor，history重构+future latent预测，部署只完整history向前预测。maskedcompletion是遮观测不是do-world干预、Remark1不授causalidentification；SAVi mask4全部反退，与VideoSAUR不同，PushT原DINO91.33>CJ88.67，slotonly60.67说明表示压缩不够。L40s同settings3seeds/50trajectoriesplanning timing不能授实机器人SLO。formal distribution-minimal neighborhood不必conditional-mean-minimal（方差差可均值相等），strictMSE-necessity/corollary attention与bidirectional→forward transfer不采用；保留实际mask机制与局部结果。6=2+2+2；仅报告：特定预训练slot/合成交互模型分支，不授真实因果结构恢复/普遍高效worldmodel。precision及完整CI Not Disclosed。

11395 [NA-RFM exact-v1](https://arxiv.org/html/2602.11395v1) §3/Alg1、§4/Table2–5、§5实际标准：early高噪PCA class-minus-global denoiser，late低噪forward activations训练RFM/AGOP方向跨time复用；高噪方向不可靠与noise-level退步是具体条件。Alg1RFMguidedstep实际两次UNetforward，§3.4“仅vector算术/无训练”不等额外执行为零（离线RFM5iter/16k及PCA）；独立evalclassifier仍共享标注人口来源，非人评/真值证明。100stepDDIM eta0，A10016sampleCIFAR测时，ImageNet4class256each/时batch4；Table2NA-RFM FID41.4比RFM40.3差、FemaleNonBlond86.4<92.2、Bird14.1%与两species<4%，不给通用OOD保证。6=2+2+2；仅报告：旧UNet条件guidance的具体时域分支，不证明新基础模型普遍rule；precision/seeds/CI Not Disclosed。

11304 [CryptoAnalystBench exact-v1](https://arxiv.org/html/2602.11304v1) §4–7/Table4–9实际标准：live多工具长文多axisrubric高分/引用覆盖高仍漏时间界、来源冲突与风险上下文，human只one selectedmodel subset kappa约.35–.42；固定prompt/tools单response各model、taxonomy classifier93.45未给独立split/误差/数量，改善prompt强模型赢弱模型退。5=2+1+2；仅报告：specific多工具评估盲区，不授生产correctness或金融结论。当前v1Updated原2026-03-26异常而Created2026-02-13仍须原完整batch依据，不把后更新当首公开；保留原字段，不重审旧revision。

11348 [AgentNoiseBench exact-v1](https://arxiv.org/html/2602.11348v1) §2–3/§3.6、§5必要标准：o3代理优化后冻结noise-generator，user/tool九类扰动；数学solvability指标不证明各例实际可解性检验。25%scenario抽样/多跳500，24model或mode，4trials mean±std（不等四独立训练seed），API硬件/precision Not Disclosed。middle最敏感是Fig6四family局部关联，early/middle/late精确定义/长度匹配未披露，不签固有因果定律；50trajectories/6scenario entropy不是原因隔离，Table1Search DeepSeekV3 toolnoise.22>.21反侧保留。5=2+1+2；仅报告：扰动位置与基线排名反侧，SGA逐步judge不等trajectory真值/真实执行失效保证。

B7八项日期raw来自datacite doi-prefix-2602-11-page-01.json.gz实际完整dates+created。Submitted分别11213 Feb11T08:26:47Z、11243 17:32:23、11304 19:29:31、11348 20:33:10、11361 20:48:52、11388 21:45:18、11389 21:47:26、11395 21:58:26；v1UpdatedFeb13T01:01:39/01:02:59/（11304异常Mar26T11:00:03）/01:07:51/01:08:34/01:10:30/01:10:34/01:10:47；CreatedFeb13T02:48:30/02:49:13/02:50:41/02:51:43/02:52:01/02:52:40/02:52:41/02:52:50Z。仅以同官方Feb13announcementbatch/UTC09BJT起点到Created秒bucket上界+1s推可公开完整区间，不授Submitted/Updated精确public秒。11304先定点恢复batchidentity（普通待办）再列确定分母。11389/11395 currentmetadata题名与exactv1有所更名，以exactv1原题采用，不扩修订全史。

GradLoc 官方新增窗内family，具体准入拟2+2+2=6，root待core校准；[原文缓存](./V3_GRADLOC_OFFICIAL.md)已有actual完整core与字段。默认en publicAt1770971763（16:36:03BJT）与zh1770971794（16:36:34）均窗内，31s语言版差异不合成单秒。global→microbatch→rank→token先microbatch避免MlogW重复，actual总O(M+logN)；adaptive阈只IID等方差Gaussian下sqrt scaling、唯一异常theorem不授实际DFS相关多异常。新TypeB token+sequence ratio≈1仍层spike，global scalar抑健康层，LayerClip按层/handle历史CA/EMA。clip统计含当前norm可污染阈，alpha/EMA系数未披露；根本cause仅假说，经验Qwen3-4B/lr2e-6/b128/8rollout/max32768/chunk4096/不同clip组合，硬件、seed、metric/CI ND，2spikedcostcases不签长期摊销零开销。Ch33无此具体spike localization/LayerClip正文，Ch28待具体局部optimizer覆盖比较后决定，不因新名强造差额。

## 最终处置同步（2026-10-04过程快照，已被后段日期纠正覆盖）

七批共91份完整题摘已root实际独立准入/代表EX及一次core核完，不是628库存全筛；root实际必要源核完B6六项、B7八项，支持与直接反侧足够，不扩全部references/附件。11351 §4.2已EX通过。GradLoc官方核心实际核、原2+2+2=6准入和Ch28 849–880/883–891具体owner比较仅报告已通过：IS≈1仍spike反侧保留，未披露阈与TypeB根因不强造长期gap。

冻结50个确定落窗家族：49 arXiv+GradLoc；49必要证据限定完成、1 NLDD中心人口争议终态暂缓。Books 5实际整合（Ch5/34/22/55/56）、2具体已有覆盖（11185 Ch28、11456 Ch36）、42仅报告、1暂缓。5实际POST已通过，三新增末注已同步，窄锁均释放；不冒充实现/复现或日级通过。

Crypto11304有限官方cs.AI/cs.IR list web两入口与定点curl未恢复唯一公告原页；原Created不是独立public上界、Submitted只可能公告下界、异常v1Updated2026-03-26T11:00:03Z尚未闭合。旧monotone_identifier_batch_reconciliation不是官方batch，不能用邻号授本窗。当前精确日期终态隔离，不评分、不计50分母、不用于本窗正面证据/Books；只需官方此ID批次页或精确v1首次公开可核完整区间，不扩前后revision。11157/OpenReview与PAM2025早公开矛盾、FERRET日期/当时正文、机构历史目录缺段继续按README§5终态保留，不记零事件或无遗漏。

Hunyuan GradLoc实际官方singlefamily原字段/正文已恢复；en publicAt1770971763与zh1770971794保留31秒语言差异，皆本窗。不能再笼统请求已到正文，但“全部”目标历史列表仍缺，恢复需对应窗口列表/API，不用单篇代目录Coverage。

README现已按50逐项候选表/原source小标题展开六部分，V3 validator初次通过。最终整日非作者验收及完成态静态检查尚待同步；未stage/commit/push，不改月索引/LS/其他日。

## 日期共因纠正后的当前终态（覆盖以上50分母快照）

root最终实际日期复核发现：20项Submitted早于Wed14EST=2026-02-11T19:00:00Z，正常Updated/Created无法排除更早公告；旧official-arxiv-first-announcement-reconciliation仅registry映射、monthlyarchive首page与schedule，不是逐ID官方本日batch。上文“官方batch支持本窗下界”对这20项的工作推定撤去，不能以邻号/同月/元数据更新时间继续授落窗。

20个精确身份：2602.11162v1、2602.11166v1、2602.11169v1、2602.11171v1、2602.11174v1、2602.11184v1、2602.11185v1、2602.11192v1、2602.11201v1、2602.11202v1、2602.11210v1、2602.11212v1、2602.11213v1、2602.11217v1、2602.11220v1、2602.11224v1、2602.11236v1、2602.11243v1、2602.11244v1、2602.11246v1。各完整原Submitted/Updated/Created在上文原日期表及B6/B7段保留；需官方新公告批次或作者/发布方可核首次公开完整区间，材料回来只重开各日期。11246已最多一次官方cs.LG目标月页恢复CacheMiss，停止；理论定义/上下界必要证据仍有效，不删两段独立理论，也不计本日正面候选或本日整合。

29晚Submitted家族均在Wed14EST后且Thu14EST前；官方availability identifier-assignment原HTML4617–4618/可读页L175–176明示最终identifier/DOI在announcement才分配且不能提前提供。故schedule最早Thu20EST/Fri09BJT下界与同精确v1官方已分配DOI Created秒bucket上界组合构成有限半开工作区间；非单独Created或精确09公开秒。Crypto11304虽晚Submitted，v1Updated异常仍独立日期隔离。GradLoc两语言版publicAt保留。

最终确定30=29arXiv+GradLoc；30必要证据限定完成，4本日实际整合（11902 Ch34、12021 Ch22、12029 Ch55、11530 Ch56）、1具体已有覆盖（11456 Ch36）、25Only。11185 Existing与11246理论整合是证据有效/日期未归属的保留产物，不计本日；NLDD中心争议也在日期保留集合，不授本窗正面采用。Ch5仅末注478补未确认本日窗/独立核验/日期重开边界，不改正文183/185；root实际tiny POST通过，锁释放。

本日README已同步六部分/30表/20精确日期请求，后续只最终整日验收、完成态与限定静态检查；无新论文队列，不重读全附件或全来源。

最终机械日期核：重新从DataCite prefix11/12原gzip逐ID取29晚Submitted家族的dates/dateType/dateInformation=v1和created，29项各只有一个v1Submitted，全部严格晚于2026-02-11T19:00:00Z且不晚于2026-02-12T19:00:00Z，Updated(v1)/Created均2026-02-13，未套同月/邻号。原字段仍在既有日期表/B7段，不新增平行账本。GradLoc报告原标题已与官方publicDetail title“Stabilizing RLVR via Token-level Gradient Diagnosis and Layerwise Clipping”一致。当前V3 validator、3份自写Markdown/24本地文件引用/30候选计数以及限定cached/unstaged diff-check通过；仅整日语义验收与完成态同步剩余。

最终完成态（2026-10-04T22:30:49+08:00）：root实际分段顺读六部分、30确定候选/4整合1已有25Only、20早Submitted日期隔离与其余精确终态、29逐ID raw日期及四处本日Books POST，整日语义验收通过。Ch5独立理论不计本日，末注日期边界tiny POST保持。普通可执行研究待办0；README开头/§1/§5/§6已同步完成/通过，外部终态仍不用于正面证据、Books或无遗漏断言。完成态V3/自写Markdown引用及本日五Books限定cached/unstaged diff-check实际通过；不stage/commit/push，不改其他日或月路由，本日作者结束。
