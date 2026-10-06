# Sep26 三具名准入与必要 Source 包

最新：root本日§10–12已经实际通过三个家族的必要Source/评分/Books层（5/5/6），README六节已同步原1＋新3＝4、原整合1/已有覆盖2/仅报告1、新写0。§3误报Eq5/7/8符号已纠正，仅loss命名不清；下文“待root”是早期准备时点，当前普通只完整DAY/完成态同步QA/实际FINAL。历史PDF明确partial、父稿有限角色已核，不再机械追原bytes或重复下载，不写Books/State/index/scripts。

作者Kierkegaard；交root独核，未预签。仅补Sep25完整自然日，原GDPval/14源/49原件层有效；本次恢复入口见[SUP_SCOPE](SUP_SCOPE_20261013.md)，root实际日期/题摘/两Blog主体读域见[本日独核§9](SUP_INDEPENDENT_20261011.md#9-root新增具名漏项与日期门窄恢复)。旧Cicero读层与root新读层分开。

## 1. Wayfinding：已准备单篇

[官方研究披露](https://research.google/blog/towards-better-health-conversations-research-insights-on-a-wayfinding-ai-agent-based-on-gemini/)，Mike Schaekermann/Rory Sayres，公开日期原样2025-09-25。date-only不要求TZ/时刻；不决定所链论文first。旧正文必要域可复用；本人本次实际在线顺读L98–154设计、评价与结论，未看图像/下载论文/执行原型。

准入P：一次给完整答案或先问完再答各有交互代价 → 每轮最多三澄清问与当前best-effort回答并存、分栏更新 → 信息未齐时不必把澄清和提供有用信息做成互斥阶段。具体项目增量是交互与临时回答消费协议，不是医疗领域指标或通用“应澄清”原则。评分提案2+1+2=5；reach仅单一人机协作流程，不借Gemini/健康名词增加。

标准必要Source：官方Design L118–128、随机研究L129–146及结论L147–154。130名美国非医护成年人within-subject，顺序随机；四混合研究163总人口不合并成130随机试验。基线Gemini2.5Flash，要求至少3分钟，测六维体验与偏好；不是诊疗准确性、安全或因果解释认证。UI和prompt同时变，不能单独归因双栏；症状原因问题更长交互不是自动低成本。未披露端到端token/费用/SLO，不采宣传或精确图中倍率。透明解释只是生成说明，不授faithfulness；每轮临时回答不能绕过实际高风险action授权。

Books初步：唯一`AGENT-WORKFLOW` Ch81。实际读现正文L257–276的每轮ask/assume admission、用户回答绑定/中断预算和安全门；已有澄清门不等Wayfinding“每轮临时回答并存”UI已写。暂只报告受测交互设计与体验证据，未发现必须据其改变现硬门禁的结论；可以No Change/仅报告，不把主题接近记为“已有覆盖全部双栏机制”。如root认为该并存协议构成长期gap，再给窄提案/锁；当前没有授权写书。

## 2. LMSYS GB200 PartII：已准备单篇

[SGLang Team官方稿](https://www.lmsys.org/blog/2025-09-25-gb200-part-2/)，原公开日期2025-09-25，不造时刻/论文first。本次实际读本日保存[lmsys主体](lmsys.html.text.json)及官方L31–87；旧有效Methods/Experiments/Accuracy/Future读层与root§9匹配复用。没有执行code、下载未公开CuTe补丁或复现。

准入P：既有大EP与较高precision布局在旧硬件条件下合理 → 低精度同时改KV容量/dispatch字节，较小EP+host-prefetch可在减通信收益超过计算减速时胜出 → kernel、dtype与拓扑改变后需联合重选scale而非固定“越多GPU越好”。具体配置边界，评分提案2+1+2=5，不因多个成熟模块提高reach或Headline倍率。

必要Source为Methods L41–56和评价/反侧L59–84：GB200NVL72，DeepSeekV3/R1；标准BF16attention/FP8MoE与FP8attention/NVFP4MoE、可选outputprojection；q_b_proj另用FP8。decode48ranks、prefill高精4/低精2；2k/4kISL分别KV近满batch1408/768。旧baseline直接复制，不同硬件、precision、EP、kernel/策略、routing平衡及batch均混杂。局部kernel与端到端吞吐分开，不采3.8x/4.8x普遍因果，也不从一次准确性图授全部质量。早期CuTe依赖未公开修复，运行/完整成本/SLO未核，MTP仅future。

Books提案No Change/已有覆盖：唯一`INFER-TENSORRT-LLM` Ch49实际L215–231已绑定model/precision/KV/layout/topology/kernel/revision；L268–270已有硬件依赖最佳DP/EP与full-cost/fallback；L310–335已有phase-specific placement、profiling、prefetch、host带宽/迁移成本和静态回退。当前具体边界由这些正文承载，不需要在Ch51重复硬件报告；本篇平台/early-access参数留报告，不授独立TMA内存正确性规则或新kernel实现证书。未写Books，无锁/POST义务。

## 3. Lumina：准入包已准备，必要 Source 当前读域

原日期事件复用root§9及Oct10§19：Alpha-VLLM News2025-09-25 TechnicalReport披露；Sep10checkpoint/inference、Oct06训练代码分别保留。拟列日期2025-09-25官方研究披露，非arXiv首次/全网首发。root已经实际完整v1题摘及current单v1身份核验，不重该AB。本人取得[exact-v1 HTML](https://arxiv.org/html/2510.06308v1)，[本日原件](SUP_LUMINA_v1_20261013.raw)，curl HTTP200/exit0、size_download627445（传输口径，不冒savedbody同字节）；命令`curl --location --compressed --silent --show-error --connect-timeout 7 --max-time 20 --output <本日原件> --write-out '%{http_code} %{size_download} %{url_effective}' https://arxiv.org/html/2510.06308v1`。

准入P/评分提案2+2+2=6：图文统一masked目标不必共享运行时揭示/停止规则 → 图像全局并行、文本block-sequential并在完成block见answer结束符时停止 → 同一checkpoint/目标仍应按模态保存sampler、stop与成本身份。reach是图文模型与执行边界，不是“omni”泛模态能力；视频/音频只是未来。

当前本人实际必要§3.1–3.3/4.1–4.4/5相关数据、§7.1–7.2及§8：image16×16codec省序列却欠语义；joint词表不消codec/输出type；Eq2 tilde预测记号与Eq3 clean目标不能据此补精确joint/recipe。已解码image置信度设负无穷/remask描述有歧义，不自修top-k规则。文本block结束符只减少冗余块，不授真实流式commit；max-logit仅近似cache代理，复用旧KV和logits，warmup/periodicrefresh付费，不授exactARcache。StageIV自己问答自评分存在共偏；Eq7/8均为loglikelihood，Eq5外负号一致；正文把它们称loss有命名不清，不判符号错误或中心配方冲突，也不由文字自行补可执行RL实现。scratch消融省pretrain并只256/SFT，不证明原体系必须LLaDA。§7当前局部A800/步数/ML-Cache倍速不倒证September；显存增加、理解速度收益较弱及low-level任务差反侧保留。未读全§6或全部附件，不称完整standard已验。

Ch24现masked L514–528、typed统一输出L1156–1180、模态性能分账L1332–1347、双向cacheL1478–1487实际覆盖拟采用的三个语义；初步No Change可行，待必要评价采用层与root独核，不请求虚假gap锁。正在仅查Technical-Report.pdf有限historical路径，非机械相同bytes门：截至Sep26/per_page3实际API返回一条Sep26 UpdateTechnicalReport；不把commit时刻推翻官方Sep25披露。只识别原artifact可采用域，不扫全history/月份。

## 当前普通余项

Lumina必要历史artifact/评价限定；root三项准入/评分与最终Source/Books独核；README六节窄整合、actualDAY/完成态FINAL。Wayfinding/LMSYS日期hold旧理由已纠正，正文无明确TZ矛盾；其他arXivsubmitted未知不连带放宽。没有新发现或全源队列，不stage/commit/push、不写State/index/scripts/Books。

## 4. 最新实际独核与 Lumina 评价/历史角色

root已实际保存本日独核§10–11：Wayfinding date/窄P/5分/标准Source/Ch81仅报告通过；LMSYS date/窄P/5分/必要Source/Ch49具体已有覆盖No Change通过。两项正式可同步，不重原Blog或Books邻接；没有写书、锁或POST义务。Lumina date/准入与v1§3.1–3.3已root实际读，以下是尚待root核的作者新增必要采用层，未冒whole-v1。

本人已实际补v1§6.1.1 GenEval原解释/Table3、§6.3理解原解释/Table10、§7.1原方法/费用和Fig12 caption、§7.2消融、§8限制。停止于上述直接支持拟采用命题的范围，不遍历其余四T2I榜/所有I2I附件。比较不同family的参数、数据、codec与sampler预算不能隔离统一目标本身收益；不用榜首/SOTA授范式普胜。Table3颜色存在局部退步；正文FLUX.1[Dev]82%与该Table3实际66%不一致，保留冲突，本文不采用该比较量或替作者改数。Table10 MME-P低于Janus-Pro/BLIP3-o/BAGEL，MMBench低于BAGEL，“统一”不能授每指标最好。StageIV同源理解器的评分不等独立质量验收，GenEval样式数据不能自动认证跨分布。只采用实际存在的图文统一目标、模态sampler/停止分责与近似cache设计，不采用具体性能量。

§7.1 T2I64steps，理解block256/128steps；Fig12 caption T2I的Lumina-mGPT2.0分辨率768、Emu3为720，其余1024，理解均1024tokens。不是匹配分辨率或质量的端到端对照；理解的block×step削弱速度优势。ML-Cache同设置采样对照同时多付驻留内存（作者该图像例38.9→45.9GB），不保证allquality或servinggoodput。Precision/batch/concurrency/完整codec及服务SLO在该采用层未完整披露；A800局部配置/倍率均不倒证Sep25。未查看Fig12像素或运行code，因此不采用图中未文字披露的逐点数值。

历史artifact有界实际结果：[PDF路径历史API](SUP_LUMINA_pdf_history_20261013.raw)截至Sep26/per_page3只一条`8b270d4c0eb1cd24c53eaae951c515f1bce4eb95`，Sep26T03:15:31Z UpdateTechnicalReport；[精确commit](SUP_LUMINA_pdf_commit_20261013.raw)文件状态added，不能把message“Update”当已证明旧PDF。此commit时刻为artifact入库角色，不能推翻News Sep25研究披露；不把Sep26PDF入库改成Sep25同bytes。实际GET其raw_url，HTTP200但curl exit28/44.409s，仅486235/29757201bytes，保存为[明确partial](SUP_LUMINA_report_8b270d_20261013.pdf.partial)，不是取得/读取完整报告；同原件web备用Cache miss。请求均`--location --compressed --silent --show-error --connect-timeout7`，API max20s/200exit0 size_download903和1047，PDF max45s；下载count仅该口径，不新增指纹账本或冒零命中。

本次原日期门仍来自作者明确研究发布，当前v1只作为2026-10-13恢复时的精确技术解释，不声称September报告逐字、完整训练recipe/性能不变。历史PDF可用于以后核原性能/细节，但拟采用命题不需要相同bytes证明，也不为这项缺口机械阻断明确原披露。正在仅恢复该commit的父README来确认同期公开核心描述，非全history/absence-proof；其余旧49原件不动。

Lumina最终Books提案No Change/已有覆盖：Ch24 actual masked L514–528承担masked目标/同轮marginal边界，typed L1156–1180承担joint输出的codec/schema/评价分责；L1332–1347分别承担文本prefix/stop与图像whole-sample不同性能合同，L1478–1487明确双向cache近似与full-refresh回退。这些正文真实承载本次最小采用命题；不是主题相似或把全Self-GRPO/ML-Cache宣称都授已有覆盖。图文运行参数与受限局部结果留报告；没有新的永久缺口需要重复写入或跨Ch23/33/45添三份note，当前不请求Books锁。此Source/评价/NoChange准备好供root独核；准备的范围不等已核，普通余项只该剩余核验、报告同步与真实DAY/FINAL。

父artifact已实际有限恢复：[0261379 README](SUP_LUMINA_readme_0261379_20261013.raw)，200/exit0 size_download4630；[父commit](SUP_LUMINA_parent_commit_20261013.raw)，200/exit0 size_download1889，committer2025-09-25T15:38:17Z（BJT25日23:38）。README仍明确TechnicalReport ComingSoon/unchecked，News至Sep20，但已写统一离散图文、图像全局/文本block采样与不同step成本，以及ML-Cache三参数/精度–质量取舍。它支持September同期已披露核心分责，不支持已取得Sep25 PDF。该稿理解speed配置block256/128steps与quickstart block32/gen_length128是不同用途，不拼同一benchmark合同。父页尚未更新报告与Sep26 PDF added是真实artifact时间差，不把当前News Sep25日期、此保存状态和现在v1强行合成同bytes/version；也不能由一份README未更新证明别处没发布。上述所有请求已结束，没有第二次完整PDF下载；partial保留不计完整取得或读取。
