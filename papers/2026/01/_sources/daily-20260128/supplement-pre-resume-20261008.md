# Jan28 恢复后最小 Books 拟文（逐批状态见下）

## 最新层级（恢复后的实际结果）

新增61已到必要证据/具体Books安全终态：35整合48段16owner、11已有覆盖、9仅报告、6中心争议；全部35实际正文/完整邻接/自身末注 POST与状态轻核已由非作者通过，窄锁释放。下文旧待Source/待Books/待锁/PRE仅拟文为历史阶段；未变有效Source/PRE/POST复用，不代表当前普通队列。原64保护，最终六部分已融入README，V3进行态通过，最终DAY尚待。

本包只请求下列具体差额；原件为同目录 `supplement-core-<ID>-20261008.json` exact-v1 HTML，作者与 `resume_20260128_audit` 已实际读必要位置，未核代码或复现。root 授各 owner 窄锁及字面 PRE 后才写入；本文件不是 POST 或 DAY。

18730/18731/18734 三段已按本包写入并实际 POST 通过，锁释放；后续18722/18760只拟文，尚未写入。后一批复用 root 实际必要原证及反侧，作者实际读其具名包并比较当前 Ch31 724–746/773–823 两段完整邻接，不声称另一次全附件 Source。

## 18722 → TRAIN-RLHF / Ch31（待新窄锁）

实际比较 Ch31「RLHF、RLAIF 与 Verifiable Reward」773–823：现有文已分反馈来源与最终verifier，尚无仅judge读取特权reference、batch ordinal反馈与objectives分责。拟在反馈来源基本边界后插一段：

反馈者也可以取得 student 不可见的训练期信息：让 judge 读取参考语言的解答，在目标语言 rollout 之间做成对比较，再把同题候选的胜率转成相对 reward；student 仍只从目标语言问题生成。这不同于把参考答案直接拼入 student，也不同于答案、格式或语言识别器的二值验证。Reference 来源、翻译、judge 与 rollout batch 应共同保存，胜率依赖候选集合，交换展示顺序后平均也不能消除循环偏好或共同错误。[受限多语训练对照](https://arxiv.org/html/2601.18722v1)中特权 judge 对某些两答案均正确切片反而更弱，不构成逐步真值；八候选带来二次成对调用，少数据不等全训练降本。参考或 judge 资格不可靠时，保留 objective verifier、独立过程审核和原无特权反馈，而不由相对排序替答案正确性签证。<!-- source-family:SF-2026-ARXIV-2601-18722 -->

## 18760 → TRAIN-RLHF / Ch31（待新窄锁）

实际比较 Ch31「Human feedback 不等于统一人类价值」724–746：现有文已有population/rubric/agreement，尚未分contextual理由与general values两流排序和原则批准。拟在“特定feedback process”判断后插一段：

从人的反馈提取原则时，当前任务中的偏好理由与脱离具体任务表达的一般价值应作为两条来源流：前者能解释这次比较，却可能看不见已被满足或罕见风险的原则；后者补充更宽目标，却不自动反映同一人群的具体选择。可以分别生成、聚类并按偏好预测或多样性/共识代理排序，合成 candidate constitution，但来源人口、任务条件、聚类与排序版本应保留，stakeholder discussion 与 ratification 才决定是否批准。[受限两流实验](https://arxiv.org/html/2601.18760v1)用不同数据人口，局部人类偏好和小安全切片不能认证组合因果或民主合法性。模型误读理由、代表性缺失和冲突观点压缩仍需处理，生成、标注与讨论也计费；来源不匹配或批准缺位时，回直接征询、窄域显式原则与独立审核，不把聚类后的高分候选冒充共同意愿。<!-- source-family:SF-2026-ARXIV-2601-18760 -->

## 18730 → AGENT-REFLECTION / Ch80

实际比较 Ch80「Feedback 来源决定价值」同模型相关错误与版本保留论证；Ch79 交接把执行验收交给观察，Ch81 开篇把事实状态留给 runtime。已有文未说明选择性自评门会因 policy 微调而失灵。拟插在同模型 feedback 边界附近一段：

反思也可以只在自评低于阈值时触发，而不是每次都重写：先把原则放入生成条件，再让同一模型逐项打分，任一项未达门限才合并批评并修订。这节省部分无条件修订，却把漏检变成新的停止失效路径；评分者与被评分 policy 相关，微调后仅在回答中提及原则就可能骗过自评门，让本应修订的回答直接停止。原回答、自评分、是否触发及修订后的独立判据应分开保存；一次 revision 还可能引入新违反。[受限 constitution 实验](https://arxiv.org/html/2601.18730v1)的较少 token 同时伴随比对照更高的 violation，不能签发同安全效果下的降本或部署安全证书。无可靠独立反馈时，保留完整规则检查、无自评门的受限修订或升级人工，而不让高 self-score 认证合规。<!-- source-family:SF-2026-ARXIV-2601-18730 -->

## 18731 → TRAIN-RLHF / Ch31

实际比较 Ch31 198–220 preference-profile 与低秩 reward basis/jury/时间状态；已有文分开 basis 与治理，尚无用户 support/query 元学习适配及困难用户失效分界。拟插低秩 basis 两段之后一段：

低秩分解还可以支持少样本个体适配，而不把每位用户都变成独立的大模型：共享 reward basis 与初始混合权重，用该用户的 support pairs 只更新低维权重，再以分离的 query pairs 更新共享 basis 和初始化。Query loss 可以提高难适配用户在 outer 更新中的权重，但它是当前模型的损失，不是用户价值真值或逐人最坏风险保证。[受限 meta-reward 实验](https://arxiv.org/html/2601.18731v1)中最难一成用户仍可低于随机准确率，重加权也只有有限增量；少量显式静态偏好不验证漂移、隐式噪声或下游 policy。应绑定 user/support/query 身份，分别计共享训练、个体适配与标注成本；低维参数少不认证全链费用更低。用户信号不足、query 支持失配或困难切片不稳时，回退固定 basis、独立窄域 reward 或请求澄清。<!-- source-family:SF-2026-ARXIV-2601-18731 -->

## 18734 → TRAIN-SFT / Ch29

实际比较 Ch29 330–378 on-policy teacher/self-target/future-label/feedback-prediction；同模型改采样已覆盖，但同 checkpoint 以额外 reference solution 形成 on-policy privileged 分布与固定 initial teacher 的权限/版本分账尚无。拟在 self-target 分布段后、future-label 段前一段：

同模型产生 target 也不必是无外部监督：student 在只有问题的条件下生成 rollout，teacher 在同一已访问 prefix 上额外读取 reference solution，再提供 detached 的词表分布或采样 token 的 log-probability correction。新增信息而非模型名字决定监督权限，teacher checkpoint、privileged context 与 student rollout 应各自绑定版本；[受限 on-policy self-distillation 实验](https://arxiv.org/html/2601.18734v1)实际固定 initial teacher，不能推成持续同步当前 policy 的自教。参考答案也不保证弱 teacher 能生成可靠指导；full-vocabulary 信号增加 logits 和峰值内存，少 rollout/较短输出下的 generated-token 降幅不等端到端训练降本，部分小模型或任务仍反退。teacher 能力或 reference 质量不足时，保留独立教师、verified targets 或既有 policy-gradient 路径，不把特权上下文蒸馏认证为零外部信息的自我纠错。<!-- source-family:SF-2026-ARXIV-2601-18734 -->
