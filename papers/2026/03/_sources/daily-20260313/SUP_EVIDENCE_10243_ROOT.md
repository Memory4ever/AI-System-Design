# 10243 GR-SAP：必要证据与安全保留主张的采用边界

root；只补 Mar12 北京时间自然日，复用第二包的完整题摘准入及 `SUP_DATE2_10243.raw` 日级公开夹证，不使用提交日单独定窗。精确 [2603.10243v1](https://arxiv.org/html/2603.10243v1)，已实际打开 §2.1–2.3/Eq1–2、§3、§4、§5.1–5.5/Tables1–3，以及必要 Appendix B、C.2/C.4/C.5。缓存 `SUP_CORE_10243.raw/txt`，GET200，2026-10-09T14:19:27.829707+00:00。D.2 的标准差表在此次 HTML 缺数值，不采用显著性判断；未执行代码、复现实验或查看图像点值，不为读全部附录扩大队列。

## 实际增量与评分

原安全示教不公开，直接混其他机构数据又可能失配 → 用当前模型生成领域安全 query/response，经过滤及 guardrail 修订后与下游任务混合 → 需要判断这份 replay 到底恢复原 alignment 分布，还是仅改善有限 judge 下的行为。具体增量为模型自身生成且经修订的安全 replay，不把成熟混合训练、KL 链式分解或“安全不能自签”的原则重复计分。拟 **2+1+2=5**；因“可靠原分布代理/保留安全”的中心保证依赖未证前提，实际针对该主张深入，拟 **争议 / 暂缓，Books 新写0**，待独立复核。

## 方法与理论边界

§2/AppB 的联合分布 KL 分解成立：原 query–response 与合成 joint 的差异等于 query KL，加原 query 人口上的条件 response KL。它是恒等式，并不估计两项大小。原文把语义相似度当 query KL 小、把 LLM 表示能力当 residual 可忽略，未证明这种推出关系。Theorem2 引用先前结果、含 closed convex 参数集及多个 TV/KL 残差项；本稿没有建立引用界的适用前提、实际AdamW优化解与该界所需解的对应、以及过滤/修订后训练人口的残差桥梁，不能由该式批准真实模型安全 gap 小。非凸loss本身不证明参数集不闭凸（参数集仍可为整个欧氏空间），本次不作这种反驳。

§3 保留原 chat/system prompt，以38子域生成 query；C.2 用 Qwen2.5-0.5B PPL 去极端5%/95%、bge-small-en-v1.5/FAISS 对相似度>.85去重、与域词相似度<.5删 query。WildGuard temperature0 对 response 提议 unsafe 标签；排除分支删记录，修订分支让原模型在追加拒答提示下重写。阈值、guardrail、prompt与修订改变合成人口，不认证每个样本无害；实际修订后的 response 也不再就是理论式中原条件 `Pθ(y|x)`，不能将 raw-proxy 推导直接当实际训练分布的证明。

训练总人口 N 固定，比例 r 的 synthetic 与(1−r)任务样本混合；可行时synthetic safety examples按难/易各半选，unsafe 原响应低于10%只是在该模型原数据观察，并非部署安全界。C.4 DeepSpeed stage2、AdamW/cosine lr2e−6→1e−6、warmup .1；任务 N 为7168/9216/10240，train/inference max length1024，vLLM/temperature0。GPU、precision、完整batch/step预算和训练总费用必要处未披露，生成、过滤、guardrail、修订及 replay tokens 都计费，不能以混合比例小推免费安全保留。

## 评价、直接反侧与未证明

四模型 OLMo2-7B-SFT、Llama3-8B、Qwen2.5-7B、Mistral7B；五下游任务和四安全集，三次运行。HS 是相应 guardrail 标成 unsafe 的比例，不是真实无害概率；构造与评估使用同一 guardrail 家族可能共同漏错。只有 OLMo2 有公开的原 alignment corpus；C.5 的原基线为 CoCoNot/WildGuard/WildJailbreak 三子集，不认证其他三个模型原训练分布已恢复。

Table2 用**未经后处理** raw synthetic 测 MAUVE（query .455 / response .646），理由为避免后处理污染相似度；这又与实际经过过滤/修订的训练人口不同。更接近该 MAUVE 指标，不等 KL 残差上界小或 original distribution 被恢复。Table1 OLMo2 GR-SAP HS .50、原数据 .60 是有限测量，不证明等价；Mistral GR-SAP13.68仍高于AEGIS12.81，MedQA56.93→52.71、WinoGrande82.35→73.09，不能泛称所有方案/所有质量切片更好或效用损伤皆<1%。

Table3 的 query filters 累计、response exclusion/revision 是互斥分支：能支持局部修订和人口选择的结果，不唯一识别每个组件的独立因果。§5.5 r超过 .1 后HS呈U形，r=.3更差；Theorem2 中较大 λ 的首项更小，不能删掉真实负侧或推实际单调安全。U形观察本身不直接反驳一个宽松理论上界。D.2 本次转换缺标准差数值，不据缺表声称作者从未重复运行或证明显著。性能/安全可支持范围仅为这些模型、任务、数据制备与 evaluator 的描述结果。

## Actual owner 与本次处置

唯一机制 owner `TRAIN-SFT` / [Ch29](../../../../../books/part-04-training-system/29-sft.md)。实际顺读当前773–805 mixture、buffer replay与tool示教，801以后 scaffold-bound supervision，以及846–891 synthetic/verifier与safety distillation完整邻接；另读 Ch28/30 开篇交接。现文具体要求监督人口与teacher/verifier身份、独立回归及总费用，区分 soft risk/KL 与真实安全保证。它并未承载本稿的38子域/MAUVE实验，不能冒称新recipe已吸收；也不因主题已存在撤销候选。

本次不新写 Books：中心“原分布可靠代理/安全保留保证”仍有未证桥梁，保留正反侧与局部结果，正式提案为争议/暂缓 Books0，而不是访问受阻或全方法无效。若取得针对**实际后处理人口**的分布差异界或独立行为证据、guardrail 与人工/独立 evaluator 对照、完整安全–效用及预算条件，可只重开此主张与 Ch29 差额；不需要等待所有代码或重审成熟 KL 原理。独立复核尚未完成，不授正式单项或 DAY。
