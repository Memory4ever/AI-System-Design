# 2603.09616v1 必要证据及采用界限

作者 supplement_20260312；公开日夹证 2026-03-11（SUP_EXACT_FIRST / SUP_ARXIV_AVAILABILITY），原报告无该家族。完整v1题摘、当前唯一v1无撤回/纠错标记已读；官方HTML https://arxiv.org/html/2603.09616v1 实际§3、§4.1–4.7、§5.1–5.5、AppendixB/C完成必要审阅。评分2+1+3=6，针对ALiBi因果反侧额外深入，不由工时或处置降分。

## 实际方法与支持

§3.1用BOS mass与attention entropy识别BLOOM头，§3.2目标QKV Xavier重初始化、output projection置零、非目标gradient mask冻结、仅训练目标参数。§3.3单RTX5070Ti/16GB、bf16、AdamW5e-5、batch1/accum8、seq512。§3.4 BLOOM1b7两遍，分别108与39头；不是任意模型免训练删除无效头。

Table2 healthy242→341→379是按其BOS质量阈值的诊断容量，不是通用任务效用；trainingPPL16.99→15.10同时12条heldoutPPL21.45→28.76。Table3 C4验证50文本/4024token：C4 surgery29.30vsstock32.42，但curated74.11；支持训练分布特化的局部观察，不能证明无能力损失。§4.2相同手术/两语料108头均恢复，而语料多维混杂未隔离；不能把functional redistribution相关性作原因证明。§4.3 frozen头BOS mass也漂移，支持冻结参数不冻结输入activation的共享残差通道推断。

§4.6 H5额外重初的一次seed/一个column transient训练PPL12.70，随后overfit；不采用25%通用质量提升、预训练局部极小或gradient绝不可逃出的数学结论。§4.7 50prompts/150completions temperature0.7/topp0.92/max100，未blindhuman/statistical；curated出现HTML与语言漂移。§5.5仅1b7完整手术、BLOOM跨尺度只诊断、ALiBi外未测、阈值固定。AppendixC C4seed42，Pass1/2无显式seed，11development iterations不是预注册独立重复评估。代码与checkpoint链接存在，但本轮未执行/复现/实现审计。

## 中心因果冲突，精确隔离

§1.1称upperhead指数的ALiBi slopes更陡并导致BOScollapse；所写公式m_h=2^(-8(h+1)/H)与AppendixB Table10却从H0=.7071降到H15=.0039，所列距离100 penalty从-70.71降至-.39，不支持该“更陡”归因。§4.5相同headindex跨层共享dimension slice不等于语义坐标不变。BOS与距离相对符号/完整logit被content支配也未由这组描述控制。因此本次不采用ALiBi斜率因果、global-local-minimum或“所有sink头都非冗余”，保留公式/表与正文冲突，重开仅需作者更正或能独立证明slope mapping及受控sink因果的证据，不请求全部附件。

## 具体owner比较与建议（未写Books）

MODEL-MULTI-HEAD-ATTENTION Ch15当前“Head怎样分化，又为什么会冗余”已在125行保留可分化≠H份独立能力、剪枝局部质量和生产执行门，126–127附近Scalpel是activationcomponent干预，不是QKV/output重新初始化+短训分支。新差额是“可剪”之外的恢复选择，且结构诊断与heldout效用分账；建议该节剪枝段后两段窄整合，保留旧pruning在预算/质量成立时合理，不在Ch13重复斜率病因。

拟新增内容：BOS集中只证明一个诊断模式，移除该head对当前任务影响小不证明它永远没有可训练容量；资源允许时可选择定点重初始化QKV、output置零后短训并冻结其余参数，作为pruning/gating之外的替代分支。冻结权重不冻结共享残差输入，因而必须连同未改头的行为复核。

代价/失效近文：新增训练与校准/阈值/语料预算；head health恢复不等最终能力，局部BLOOM1b7证据出现heldoutPPL和生成漂移，单seedH5瞬时训练loss不签发通用收益；斜率归因冲突不写入。若质量/预算不能满足，保留原头、原pruning/gating和已验执行。正式采用待非作者Source/PRE及root实际写后。
