# 02/19 首批必要证据与采用边界

本文件是实际核心审阅笔记，不承接旧 receipt 的判断。日期依据：同一 DOI 的 [原始 DataCite 字段](V3_DATACITE_DATE_BOUNDS.json)；[arXiv 官方 availability](https://info.arxiv.org/help/availability.html) 说明标识符/DOI 在公告时赋予，Monday 14:00～Tuesday 14:00 ET 提交最早 Tuesday 20:00 ET 公告。六篇各自 Submitted v1 > 02/16 19:00Z 且 ≤ 02/17 19:00Z，上界为各自 DOI Created/Registered（均 02/18 02:35～02:39Z），共同限定完全落入本窗；不采用 Updated、相邻 ID 或月列表倒推。候选数尚未最终确定，97 日期成立不表示97准入。

## 2602.15156v1 Panini

采用精确 [v1 HTML](https://arxiv.org/html/2602.15156v1)，本地 [原文](V3-exact-v1/2602.15156v1.html)。实际读 §2、§3～4、§6 与 Appendix G/Table19。

反复读原始 chunk 在写入便宜、查询少时合理；本篇新增的读法是一次分解查询，实体 BM25 与 QA dense 双索引取候选，cross-encoder 重排，答案实体实例化下一跳，几何均分链分数的 beam search，而非每跳调用 LLM；仅把链上 QA 对送给 answer model。GSW 表示本身来自作者既有工作，不把它全部当本篇首创。改变的选择是将每次多跳证据提炼迁到一次写入+有界链检索，不是模型权重持续更新。

Table2 的同 HippoRAG2 切片、默认 GPT-4o-mini answer、GPT-4.1-mini 写入、GPT-4o 分解、Qwen3-8B embedding、Voyage reranker 下，均值 F1 56.06 对 HippoRAG2 53.3；不是“5–7个百分点普遍提高”。Table3 的平均319.79对普通chunk705.27只计 answer-context tokens，不是所有成本下降2–30倍。Appendix G 中 MuSiQue 11656passages 写入100.1min/$48.02，read3.3s/query，对dense1.9min/1.3s；证明存在写入与读取预算交换，不证明单次端到端更快。Platinum 按可用证据标注可答/不可答且统一N/A prompt，答题与拒答分账；不能把拒答率当总体可靠性。

§6 明示未实现 latent-link caching/experience-driven reconciliation，开放模型抽取会缺 verb/QA 边；entity reconciliation、事实密集QA及语料增长实验不覆盖任意叙事/多模态记忆。拟评分2+2+2=6（跨写/读），必要证据已读；Books 尚待实际 owner 比较及 root 复核，不授完成。

## 2602.15197v1 OpaqueToolsBench / ToolObserver

采用精确 [v1 HTML](https://arxiv.org/html/2602.15197v1)，本地 [核心原文](V3-exact-v1/2602.15197v1.html)。下载曾到时，主体 §3～5.2/§7 已完整取得并实际阅读；未据此称附录完整。实际机制：从真实多步任务轨迹学习工具行为，而非孤立合成单工具试探；offline batch editor 借训练 gold/结果生成局部描述再 consensus merge，online 仅执行反馈迭代（不使用gold），描述不再改变时早停。

§3 分 documentation opacity 与 intrinsic opacity，BFCL匿名工具、Chess阶段/强度工具和固定BrowseComp+分域检索分别测试 schema、状态依赖与序列依赖。Table2 GPT-5 匿名名 execution accuracy0→0.80，对P2P0.44，但gold0.95；工具已知参数时0.82→0.83，收益不普遍。§5.1 token3.5–7.5倍优势绑定 BFCL online 探索总I/O，不能套用于offline或所有任务。Table4 BrowseComp GPT-5 FullSearch21.8→22.1且调用9.3→9.5，不能照录“显著恢复差额”。GPT-5-mini domains EasyTool7.1胜TO3.2；作者称随机异常却未给足独立重复，本轮保留反例。Table4题注写Qwen0.6B而行是GPT5两型，Table6正文与行有错置，本轮不采用那两组数值解释。

新增命题是工具执行反馈的学习单元须覆盖跨调用状态依赖；不证明生成文档正确、安全、授权或生产适用。拟2+1+2=5（工具调用组件），标准必要证据已读；Books待owner实际比较。

## 2602.15200v1 COMPOT

采用精确 [v1 HTML](https://arxiv.org/html/2602.15200v1)，[本地原文](V3-exact-v1/2602.15200v1.html)。实际读 §3 Eq4～11、§4 Tables1～9、§5；未核代码或复现。

单一SVD子空间与无约束字典重优化都有合理用途。本篇在 activation-whitened 空间约束字典正交，固定字典时 hard threshold 系数有解析解，固定系数时薄SVD Procrustes 更新；原文 Eq7 非联合凸，主实验交替20轮，消融到100/300轮。因此“eliminating iterative optimization”只可解释为消除单步迭代 pursuit/逐原子更新，不能说整个压缩一次闭式完成。原空间归一化矩阵的全局奇异值池分配预算，与重建whitening的谱分开，设过低/过度压缩guards。

Table3 固定CR、256×1024 RefinedWeb校准、normalized lm-eval0.4.8 下，与SVD-LLM/CoSpaDi的质量比较较可比。Table5 SVD-LLMv2复现缺项/偏差，Dobi-SVD主表未含remapping，不能把所有表概括成普遍获胜；不同protocol不能合并。Eq11显式计16bit字典/非零系数/1bit mask，4bitGPTQ组合Table7绑定Llama7B、2.8GB权重预算、WikiText PPL；不证明runtime加速。§5 Gram正定与校准代表性是限制，缺真实kernel端到端执行。本篇拟2+1+2=5；标准证据已读，Books待owner实际比较。

## 2602.15222v1 Automatically Finding Reward Model Biases

采用精确 [v1 HTML](https://arxiv.org/html/2602.15222v1)，[本地核心原文](V3-exact-v1/2602.15222v1.html)。实际读 §2.1～2.3、§3.1～3.4、§5。摘要准入不等于结果普遍成立。

预定义长度/格式偏置检查容易漏未知属性；本篇从采样响应和reward提出自然语言属性，按RM偏好与Sonnet4.5反偏好的Pareto目标保留并变异，而非只做flat best-of-N。反事实响应由三provider rewriter最小修改，validation Bonferroni，独立test偏置集后用partial-conjunction；Table1 17个待验属性只有10个双侧显著。属性相关变化仍不能完全拆开，judge不是human truth。

§3.3 固定提出候选总数比较depth5/branch4、depth3/branch8、depth1，单次完整运行、六topic有结果，支持受限观察而非进化搜索定律。§3.4合成注入recall只检3个regex属性，n=10 Wilson CI很宽，presence中间比例更易发现；不保证未知偏置召回。仅Skywork-V2族、20手写synthetic topics，发现RM偏置不证明下游policy已学会偏置。新增是发现-验证分开且按prompt子分布审计，不是已有偏置列表扩充。拟2+1+2=5，标准必要证据已读；Books待owner比较。

## 2602.15318v1 Sparrow

采用精确 [v1 HTML](https://arxiv.org/html/2602.15318v1)，[本地原文](V3-exact-v1/2602.15318v1.html)。实际读 §2～4 Tables2～6 与§6。

直接让小draft消费长visual KV可保留原始细节，但容量与attention稀释会让接受率/速度崩溃。原文替代分支在draft推理只消费已融合视觉的text hidden states/window，视觉计算留给target；训练保留target中层visual bridge，并MTP递归预测降低teacher/student分布差。Table6 25k visual时，MTP+IVSB无VATA接受长度1.21，完整4.37；局部消融支持为何训练用视觉而推理不重读全部visual。

LLaVA-OneVision7B、L20、25k visual、四video tasks、dynamic tree30-4-8，Table2 temp0平均DSR2.82而ESR1.93；temp1 DSR2.04、ESR1.59。Qwen2.5VL7B Table3不同13～17k输入；A800 tree48-5-10结果不能和L20直合。Table5 prefill占比13.8%→38.7%，spec不优化prefill；‘real-time’不授固定SLO、batch/concurrency泛化。作者称lossless而不测quality，是标准target verification假设下的输出保障主张，不是本轮实现核验。拟2+2+2=6；标准证据已读，Books待owner比较。

## 2602.15323v1 Robust Signatures Watermark

3+2+3=8，安全归因contract必要深入已读，root非作者必要源/PRE/实际Ch72正文L179/181与完整邻接/末注POST均通过，窄锁已释放。不因密码学方向漏排，不据此授日级Gate。

已实际读 §1.1 定义/假设、Remark1.6及§2.1～2.3：普通soundness仅防key-independent误报，unforgeability还允许观察watermarked outputs/verification，限制有效检测文本须接近其观察过的某输出；robust recoverability保证列表包含原substring，却不防列表伪项，需单独unforgeable recovery。构造将前块签名藏进下一块；PPH保留约定距离判定+差分恢复，与strong UF-CMA签名组合。Hamming every-block-close、block对齐/足够长文本、末块loss、highentropy以及secret/public不同密码假设，不等语义改写/插删或法律所有权保证。精确§6.4实例与必要反侧已在下文实际完成。

已恢复完整HTML并实际读§6.1 Theorem6.1/Algorithm9～11与两方向证明、§6.4 Corollary6.6/6.7、§2.3反侧。算法在任意输入的2n substring上解藏于后块的前块签名；Theorem6.1鲁棒性保证有2n近似子串可检测，而不可伪造仅保证有n近似子串，不能推检测整篇均来自模型。§6.2更长chain分支也需末块loss。

secret实例还需ideal PRC（subexponential LPN假设）、强签名/CRHF以及高熵；public实例需random oracle/highentropy，error-rate为subconstant且每块首ell bits不得修改，不能照录“可公开验证且常数比例任意改写鲁棒”。§2.3承认Hamming不覆盖广泛改写，GapEdit只future；unforgeability归约本身不依赖embedding entropy，但具备鲁棒/undetectable实例仍有条件。生产部署、现实参数开销与语义编辑未验，未运行代码；这里采用证明责任的差异与条件化分支，不授全局安全/所有权。

实际owner Ch72 已读 L165～235水印/取证段、L2935～2965组合改写及key归属段，以及Ch71出口、Ch73开头。原L177和L2954只说水印sensor≠authentication并与签名交叉，未解释soundness/unforgeability/recoverability三种对手与证明方向。经root源/owner PRE授窄锁，已在原L177之后融入两段条件化差额，保留旧sensor建议；root实际再次核PPH精确wording与邻接/末注POST通过，窄锁释放。

Books实际段落采用：普通低误报/鲁棒检测在key-independent输入和有限改写测试中可用作sensor；一旦攻击者可观察模型输出/验证，就需单独声明不可伪造保证，检测通过至少要对应某个观察过的输出片段。恢复原substring的存在与恢复列表不含伪项又是两方向责任，不能仅凭recall或‘可恢复’标签合并。先为前块构造保留约定距离判定的摘要，再签名并嵌进后块；代价是块长、嵌入容量、验证扫描与恢复状态。该分支仅在明确Hamming/block predicate与密码假设成立时成立，不覆盖semantic paraphrase、插删、短片段或法律归属；未知编辑继续回退签名origin record、provenance与人工裁决。实际Ch72 L179/181及末注已通过root POST；保留相邻generator/decoder生命周期限制，未授日级。
