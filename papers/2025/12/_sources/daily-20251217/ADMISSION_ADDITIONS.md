# 新发现的具体增量（待主线程定点校准）

实际读取2026-10-02。下列有潜在准入依据，均未因日期或阅读费时降分/删除；未确认first-public的不计确定当窗候选、不写Books。仓库commit时间不是public时间。

- [FlashFuser 2512.12949v1](https://arxiv.org/abs/2512.12949v1)：单SM scratchpad限制FFN等fusion → DSM跨SM通信抽象+分层dataflow/cost pruning → 可在片上扩fusion而须计通信代价；请校准是否足够构成INFER-TENSORRT-LLM机制增量。完整v1题摘已读，H100作者数字未完成归因，first-public待恢复。
- [UIFormer 2512.13438v1](https://arxiv.org/abs/2512.13438v1)：UI压缩缺Boolean完备性oracle → 受限DSL、结构分解与正确性/效率reward合成转换程序 → 压缩不能只按token验收；待校准AGENT-CONTEXT/TOOL owner边界。
- [Code scaling 2512.13472v1](https://arxiv.org/abs/2512.13472v1)：统一token scaling忽略语言交互 → 语言比例/配对翻译与协同效应预算对照 → 数据预算应随语种饱和与交互而非均分；待校准TRAIN-DATA/ PRETRAINING。
- [VGCO 2512.13860v1](https://arxiv.org/abs/2512.13860v1)：人类工具说明与调用失败不匹配 → 失败评价驱动state/action特定层级编辑及verification → 离线文档优化需绑定失败与验证，不由文字合理性验收；待校准AGENT-TOOL-CALLING。
- [HyperVL 2512.14052v1](https://arxiv.org/abs/2512.14052v1)：端侧高分辨率ViT成本 → 动态resolution预测+多尺度一致学习共用LLM → 切换视觉支路必须同时验收表示与资源；待校准MULTIMODAL-REPRESENTATION。
- [CTVP 2512.13821v1](https://arxiv.org/abs/2512.13821v1)：执行不可信代码有风险 → 对语义等价变换的预测trace作一致性验证及信息论主张 → 预测trace不应默认等于真实execution证据；安全/反证信号保留，必要理论假设若可归窗须深入审，不以摘要“provably”采用。
- [PerfCoder 2512.14018v1](https://arxiv.org/abs/2512.14018v1)：代码性能缺可解释训练监督 → 优化轨迹SFT+runtime reward与planner反馈 → 性能监督与正确性/测量可比需分开；待校准机制是否超过任务recipe。
- [gpu_ext 2512.12615v1](https://arxiv.org/abs/2512.12615v1)：设备策略固化/跨租户边界 → host/device verified eBPF hook → 可扩policy但须保留verification与资源authority；待校准PLATFORM-GPU-SCHEDULER/SECURITY边界。
- [Janus 2512.13525v1](https://arxiv.org/abs/2512.13525v1)：MoE attention/expert并置资源比例固定 → 分离GPU集群、自适应two-phase通信与独立expert placement → 两侧容量可独立扩而增加传输调度成本；待校准分离系统增量，禁止采用当前v4的4.7×替v1。
- [EARS 2512.13194v1](https://arxiv.org/abs/2512.13194v1)：严格speculative accept受低置信target限制 → uncertainty适应的rejection tolerance → 需显式在质量与acceptance之间取舍，不能声称保持exact target distribution；待校准Ch48近似分支。
- [SPON 2512.12744](https://arxiv.org/abs/2512.12744)：activation稀疏化可使hidden-state塌缩 → input-independent anchors与distribution matching且可吸收bias → 需要保留表示退化机制；当前题摘已读，精确v1仍需恢复，不能采用较晚摘要变化。
- [PIEP 2512.12801](https://arxiv.org/abs/2512.12801)：多GPU能耗测量受通信非确定性及采样成本影响 → 能耗估计/测量成本模型 → 需区分测量扰动与训练收益；完整题摘已读，方法/first-public待核。
- [MiMo-V2-Flash历史release commit](https://github.com/XiaomiMiMo/MiMo-V2-Flash/tree/65f0e73804b030611b74235ddad9dc4ad1a6a586)：历史README已有routing replay使rollout/train选同expert、prefix cache存KV+routing及MOPD → 需分开数值routing一致与policy一致；不是从2026 arXiv报告倒推，公开事件仍缺有权字段。
- [HY-WorldPlay历史README](https://github.com/Tencent-Hunyuan/HY-WorldPlay/tree/82d43dae3670e085cdf886505d44c79cbc729bc6)：有限memory与few-step蒸馏引起长期漂移 → context reconstitution/temporal reframing和teacher-student memory alignment → 蒸馏需约束历史condition，而非仅逐帧损失；README声称Dec17无时区，commit在Dec16UTC不证明公开，未据当前后来训练代码宣称2025已开源。
- [HunyuanVideo1.5修订9304589](https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5/commit/93045891eb2c352cec06a1c6838cc30008840cad)：all_gather backward由只取local chunk改为SUM reduce_scatter → 分布式梯度累积语义改变，不是普通版本标签；正确性信号必须保留并定点审相关原语。该patch已读，需校准其public revision归属，不能用commit时刻自动确定本日。

## 追加精确v1题摘（同样未授公开日期）

- [M-GRPO 2512.13070v1](https://arxiv.org/abs/2512.13070v1)：长程self-supervised RL collapse不能靠更多rollout根治→momentum target与IQR低entropy过滤→须分离稳定目标与多样性保护；潜在TRAIN-GRPO增量。
- [RPO 2512.13240v1](https://arxiv.org/abs/2512.13240v1)：同policy正负response错误相近→外部hint-conditioned reflection构造更强contrastive pairs→更大margin是否仍on-policy须核假设；潜在TRAIN-DPO增量。
- [Textual Gradients 2512.13598v1](https://arxiv.org/abs/2512.13598v1)：prompt优化收益常以gradient类比解释→实验/case study挑战类比→效果存在不证明该解释；设计反证保留，归AGENT-PROMPT，不因局部实验排除。
- [SWR 2512.13921v1](https://arxiv.org/abs/2512.13921v1)：递归计算与跨warp通信冲突→分层recurrence分解与hardware-aligned jagged windows→截断状态/计算代价须共同解释；潜在MODEL-LONG-CONTEXT机制。
- [Effective depth 2512.14064v1](https://arxiv.org/abs/2512.14064v1)：更多depth/long-CoT常被推定每token更深→Qwen家族及难度对照未见有效深度比例提升→需核proxy定义才挑战深度利用结论；潜在模型层次评价证据。
- [SDAR-VL 2512.14068v1](https://arxiv.org/abs/2512.14068v1)：block diffusion训练不稳定→异步block noise、mask ratio无偏归一化、渐进Beta curriculum→objective normalization与corruption schedule共同约束；潜在Ch24生成训练机制。
- [UniSparse 2512.14082v1](https://arxiv.org/abs/2512.14082v1)：稀疏attention迁移与质量折中→composite tokens的多粒度压缩+block selection→selection统计与kernel执行需分离；潜在MODEL-SELF-ATTENTION/INFER-PREFILL。
- [Efficient-DLM 2512.14067v1](https://arxiv.org/abs/2512.14067v1)：AR迁移到全双向attention及均匀mask破坏预训练/测试条件→block-causal持续预训与position-dependent mask→migration需保留跨block条件、非原AR分布保证；潜在Ch24。
- [RADAR 2512.14069v1](https://arxiv.org/abs/2512.14069v1)：固定draft调用数浪费计算→offline RL学MDP动态draft tree预算→只改变proposal预算，仍需target verifier与端到端配置；潜在Ch48。
- [Membership inference 2512.13352v1](https://arxiv.org/abs/2512.13352v1)：独立MIA benchmark未必代表提取pipeline→把多个MIA放入生成/筛选闭环比较→需核具体反向结果才判定评价增量，不先照录“实用性”；准入事实尚需定点正文，不是已入选。
- [AutoTool 2512.13278v1](https://arxiv.org/abs/2512.13278v1)：固定tool inventory限制适应→trajectory stabilization与KL-regularized Plackett-Luce ranking分阶段优化→新tool generalization需分开selection与任务结果；只拟采用非AI-for-Science的机制与切片。
- [FROC 2512.13337v1](https://arxiv.org/abs/2512.13337v1)：forgetting/utility双风险难选择→conformal-style预算与配置可行域→需要核风险聚合和交换性条件，风险score不自动是删除影响的事实概率；潜在模型生命周期/评价增量。
- [SkipCat 2512.13494v1](https://arxiv.org/abs/2512.13494v1)：单独低rank分解需大幅降rank才省资源→同input矩阵共享projection并skip部分block→固定预算可保留更多有效rank，需算实际访存；潜在FFN/低rank执行分支。
- [RecTok 2512.13421v1](https://arxiv.org/abs/2512.13421v1)：高维tokenizer语义增强仍损生成→VFM语义蒸馏进入forward flow trajectory并masked reconstruction→要区分latent容量与训练路径语义；潜在Ch24机制。

负侧已读：Memory in the Age of AI Agents完整v1题摘主要分类/框架/前沿清单，未给修正设计的新增对照或失效证据，按综述不足准入关闭；BlossomRec完整v1题摘只支持推荐兴趣长短两种sparse pattern+gate的任务收益，未建立基础模型泛化或新的稀疏系统机制，按当前可支持范围关闭，不据此否定一般attention理论价值。

SIGMA决定准入的补读已执行：[2512.13488v1 HTML](https://arxiv.org/html/2512.13488v1) §3.1–3.5、§4.1–4.3完整必要段。具体增量不是MFU数字，而是跨栈numerical validation不仅比较forward，还比较gradient和10步optimizer累积差异；否则forward接近可掩盖router/qk-layernorm累计误差。另把unknown fault online隔离和offline签名生成/历史验证分开；有平台机制准入潜力。Table6的94.45%是Effective Utilization（非闲置加速器时占比），不是MFU；Table10的MFU轨迹从9.86%起，累积recipe同时改变global batch和model层数，两种指标均不作各机制独立因果；MoE layer norm valley仅有限模型观测，不能声称稳定训练必要定理。first-public未授，暂缓本日采用，不评分以免把条件排期作确定事件。

## 日期终态保留的统一边界

以上具名潜在贡献未获得实际个体first-public；官方advanced只支持announced年/月，日列表400、历史catchup有限失败及OAI语义已由root定点验证。保存每项identity、精确版本与贡献，不按常规提交排期授归属。重开条件：官方历史new公告、保留的个体RSS pubDate/announced_date_first含日及官方时区依据，或可证明首次正文完全落窗的作者原始公开记录。仅重开取得证据的身份与真实归属日，不全月扩扫。仓库三项需其公开release/push事件字段或同事件官方公告的首发约束；commit时间本身不足。未评分、不入Books、不证明零事件或覆盖通过。

Membership-inference题摘未具体给差异结果，保留为宽线索，不擅自称通过准入或已审证据；公开归属若恢复，再围绕其pipeline与独立benchmark差异定点补读。它不是已入选候选被删掉。

## 相关题名闭合对照

2026-10-02本轮重新逐项对照14条具体系统入口及46条ML语义compute入口，不把其余宽库存变成新队列。以下精确v1完整题摘均已取得，新增潜力保留：

- [MEP GPU kernel 2512.22147v1](https://arxiv.org/abs/2512.22147v1)：完整application编译/运行贵→抽取hotspot并自动补成Minimal Executable Program做repair/performance-pattern继承→reintegration仍须原application验证；不是只数字优化。v1字段实际Dec15提交，较大ID不授晚公开或本日归属。潜在INFER-TENSORRT-LLM执行/验证增量。
- [SocialNav-MoE 2512.14757v1](https://arxiv.org/abs/2512.14757v1)：小VLM实时控制中hard/character reward不足→SSR semantic similarity与router/encoder配置比较→语义reward是否有更好决策取舍可定点核验。保留局部Embodied/RFT潜力，不因是navigation自动排除；不采用摘要的实时/低功耗保证。
- [Resource allocation 2512.12816v1](https://arxiv.org/abs/2512.12816v1)：客户端不能重训、概念老化与预算共同限制→DMRL/IMRL下更新策略差异及通信约束部署调度→固定定期更新可能理论上次优；保留PLATFORM-MODEL-REGISTRY模型更新/成本边界潜力，需核假设，不外推LLM训练。
- [FIN-bench-v2 2512.13330v1](https://arxiv.org/abs/2512.13330v1)：翻译benchmark不保证稳定模型排序→2.15B训练曲线按monotonicity/SNR/nonrandom/model-order consistency筛任务→评价任务必须验证信号稳定，不仅扩语言条目；保留PLATFORM-EVALUATION-SYSTEM潜力。
- [Graph adaptation 2512.13149v1](https://arxiv.org/abs/2512.13149v1)：独立样本式transfer解释忽略node dependency→Markov依赖假设下conditional-shift/generalization界与decorrelation→保留表示迁移理论条件的潜力，不能当任意Transformer去相关定理。
- [KCI 2512.14000v1](https://arxiv.org/abs/2512.14000v1)：conditional-independence test的功效/Type-I错误无法单纯归模型质量→conditional mean embedding估计误差、conditioning kernel取舍→保留评价/统计推断条件的潜力，不以通用kernel词扩扫物理/统计库存。
- [SonicMoE 2512.14080v1](https://arxiv.org/abs/2512.14080v1)：IO/tile-aware重排与通信/计算overlap改变expert执行成本，保留MoE kernel潜力；[DTop-p 2512.13996v1](https://arxiv.org/abs/2512.13996v1)：PI controller控制目标稀疏率，保留动态expert计算预算/控制稳定性潜力。两者精确v1提交实际Dec16，不授12/17公开。

具体close：

- 2512.12731v1完整题摘仅在symmetry/Gaussianity postulates下导出传统spline regression核与正则；未连接本项目模型能力、训练优化或执行主线的具体设计，不因出现ML/kernel入选。
- 2512.13238v1完整题摘的Wizard-of-Oz采集与15k VQA只给egocentric assistance新数据/任务难度，未给改变模型/系统判断的盲区比较结果；不是任何新数据均不收。
- 2512.13515v1完整题摘是SQL迁移的fine-tune+syntax mapping+SME feedback流程，未给超越任务recipe的执行机制/成立边界；按当前披露关闭。
- 2512.17948v1精确标题为Physicists Joke，完整题摘是1966幽默文集复原，不是模型研究；现搜索标题/摘要可能受v2影响，保留身份纠正。
- 2512.13396v1完整题摘的LoRA四信息单元+flow selection/pruning只证明推荐scenario-task收益，未新增foundation机制/系统边界；2512.13632v1是病理口吃分类的clinical retrieval+Jaccard metric/gate，当前无基础模型机制关系；2512.12868v1只研究MedQA临床诊断，当前暂缓切片，不能借evaluation owner引入科学应用。
- 2601.04213标题明确是LLM交互教学可视化；2512.14045标题明确是二进制ML分析中的function-inlining安全，不是本项目大模型编译/执行；其余确定医学、农业、天文、地质、照明、无线等领域应用按标题关闭。关闭只指本项目准入，不判断学术价值。

两项普通定点阅读已补完：

- [2512.12595v1 PDF](https://arxiv.org/pdf/2512.12595v1) §3/3.1–3.3 pp2–4、§5–7 pp4–7：noise-aware只写噪声检查/可疑样本重复测量平均，rectified flow仍是已有线性noise-data路径，bidirectional与hybrid只给组合轮廓，未定义相对旧机制的新增可核验操作或成立条件。§6.2声称移除组件收益但未给对应protocol/表；本次明确关闭的是“新增机制”准入事实仍不成立，不是因为数字不够好/日期失败而降分。模型和基准版本、noise检测/remeasure规则均未具体披露，数字不采用。
- [2512.13352v1 PDF](https://arxiv.org/pdf/2512.13352v1) §IV pp3–6、§V pp7–9与§VI起点p9：题摘未给具体反向结果，正文已恢复。生成+ranking中的多种MIA相比likelihood只边际改善，Min-K%++/lowercase明显退步；后续threshold确认阶段S-ReCaLL有更大差异，故standalone membership、候选排序、真正泄漏确认不能互相替代。15k扩展集和model-less BoW用于检查简单分布伪影，ensemble须目标分布的ground-truth标签、现实攻击不一定可得；k重复fine-tuning注入手机数字的设计保留受限语料/模型范围。这是具体PLATFORM-EVALUATION-SYSTEM/SECURITY潜力，保留而不降分；日期仍隔离，不采用为本窗安全证明，不宣称已完成全部深审。

本轮相关题名普通准入判断/定点正文待办0。上述新增潜力仍需root准入校准，不凭作者记录授日级通过。真正first-public缺口采用统一精确重开条件，已知有效证据不删除。
