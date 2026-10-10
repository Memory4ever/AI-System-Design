# TRM 08498：必要证据、中心隔离与 owner 差额

精确2602.08498v1；root完整AB与本批Feb10BJT公开上下界通过。拟采用是可见trace的DAG评价接口，不是“thinking truth”或理论保最优：2+2+2=6，中心冲突与具体差额受影响深入。原件 `supplement-20261008-trm-core.json` 完整§3/4/5/6；`supplement-20261008-trm-direct.json` 为官方v1必要A/F/G.1–3/H原文（JSON string，jq -r . 可恢复带原L行号文本）。没有运行artifact/复现，不遍历其余证明。

## 实际方法与评价边界

§4：双换行+语料高频prefix分step；顺序构造有向依赖，parent attachment pool只含current main branch与代表branch endpoints，不是全history或唯一真实依赖。连续chain合并supernodes，macro摘要带结构tag，micro取dominant path；四维efficiency/effectiveness由LLM判并再聚合。每pair两个顺序各三次，保consistent/non-tied labels；六次一致仅描述筛后人口，不是独立真实正确性或所有pair可靠。Macro压缩与dominant path会丢信息，原始trace/分步器/候选parent pool/路径选择/摘要与judge identity必须保留。

§5/F/G：64k prompts采verified-correct traces形成约103k train/1.5k validation，Llama3.1-8B BT value head。正文“rule-based verifier”与F L768/772所述DeepSeekV3.2做verification/结构/preference的分工口径不完全一致，训练correct标签仅作者核验，不能认独立ground truth。Validation88.6%把ties判错；PromptOnly78.6%，其排除ties93%是另一分母。BoN用Qwen3-8B/GPT-OSS-20B，N1/2/4/8/16、T.6/p.95、5 repetitions；TRM只看reasoning，PRM看reasoning+final，输入资格不同。44.7→64的19.3pp绑定N16，不是同总搜索费用。

RL用GRPO r_v[(1−α)+α sigmoid(r_t)]，α.2；correctness gate使wrong reward仍0，同时重排correct人口。300steps/8samples/temp1/lr5e-7/global512/mini128/clip.3，General-Verifier math。Table2不是全部切片胜：Qwen1.5B Olympiad37.3<ReasonFlux37.5、Qwen7B MATH83.0<83.6/BBEH9.2<9.5、Llama AIME24 8.1<8.8/MATH53.8<55。Table3 GPU-hours49×4对Verifier44×4尚不含TRM自身约20h/preferenceannotation；hardware/precision/servingSLO未披露。采用局部测量/奖励分支，不授普遍更便宜或内部reasoning因果。

## 必要中心冲突（只隔离实际保证）

§5.1“optimal policy invariance”的直接A L527–572：L535 Φ(s_t)=I(final r_v=1)TRM(s_t) 依赖future终局，并不是共享prefix的state-only potential。L543–550保留非零terminal γ^T TRM(final)，又与主文无γ^T式不一致；没有终止potential置零或吸收续程补偿。不能直接把无限horizon潜势定理授给该有限终局奖励。

最小反例：单prompt有两条同长且都verified correct的response，r_v均1，而sigmoid(r_t)分别.25/.75。原r_v下二者策略都optimal；α>0的新reward严格偏好后一条，故“every optimal ... and vice versa”的最优策略集合不保持。只隔离实际终局recipe的保最优与其所依赖保证；不否认一般potential定理、不修证明、不向NPG其余附件扩队。重开需官方state/terminal条件与实际reward一致推导，或撤回该保证。DAG评价/实证可以独立受限成立。

## actual owner 与最小 PRE 请求

PLATFORM-EVALUATION-SYSTEM Ch66实际918–947 final→trajectory/cycle及2837–2865 narrative→actions→outcome分层承载“轨迹不能代正确性”，未承载对可见reasoning分step、构DAG，再分macro branching/merge与dominant-path micro评分这一测量接口。TRAIN-RLHF Ch31 actual537–570的Reward DAG是criteria graph，不能当本文trace dependency graph已经覆盖；Process Reward1087–1098是(K,N)concentration，也不是结构评价。Ch65/67交接已实际读，可复用。唯一owner拟Ch66，不在Ch31复制训练recipe。

拟在Ch66 final→trajectory开头的lucky-pass段后添加一段；中心保证不进Books。尚未root必要Source/PRE、未获Ch66锁、未写。

最终答对也不说明可见推理轨迹的组织是否合理。一条测量分支把trace按版本化规则分step，用有界parent候选构成DAG，再分别比较包含branch/merge的macro摘要与支持最终结论的dominant-path micro内容；全局探索组织与局部推进不必压成同一个终局分数。这个图是评价者从可见文本提出的依赖假设，不是内部计算或真实因果链，摘要与路径选择也可能漏掉决定性证据。交换pair顺序、多次judge并筛一致非tie标签可以限定训练人口，却不能认证事实真值或未筛人口可靠；应保留原trace、分步器、parent pool、摘要/路径与judge版本，并由独立任务verifier继续负责正确性。构图、重复标注、reward训练及搜索都付费，局部质量切片仍可能退步；依赖/标签失准或预算不足时回读原trace、用原process/outcome评价或人工审查，不让结构偏好接管发布判断。

拟链接exact-v1#S4；末注保中心reward隔离、correct-only人口/信息资格、制备成本及反侧。请求root实际必要原文与owner差额/PRE，获锁后才写。
