# 有界尾项最小逐字稿

仅本日既定尾六，Source/date由reader1独立核；未获逐字PRE不写Books。

## 03894 / Ch66

锚点：受监督Judge置信读出完整段（2605-15416）后，自报数值confidence鲁棒性段前。

逐字正文：

黑盒 actor 不提供 logits、重复采样又几乎相同时，可以让较小的开放权重 surrogate 固定读取同一 context、schema 与候选 tool call；但读出应按错误位置分解：argument value 的 teacher-forced likelihood、扣除无请求条件下 likelihood 的 PMI 修正、整次调用的 verdict 与 tool-choice 对照不是同一种证据。[受限代理置信对照](https://arxiv.org/html/2610.03894v1)显示它们可互补，原始 likelihood 的方向却会反号，必须在独立留出数据确定 orientation；生成 verdict 与强制 YES/NO 的差异也不能全归于模型大小。Nl2bash 的反馈收益超过随机信号，AppWorld 中随机反馈却与融合分数相当，因此额外反馈本身仍是替代解释。PMI 两次 prefill、verdict 生成、surrogate 驻留和校准都计费；局部 selective accuracy 不是动作正确性保证，与 tool 执行并行及 fail-open 更不提供 pre-effect 授权或零增时硬门禁。错误类型、域或校准变化时保留独立 verifier、原始观察与拒答／人工路径，不能由 confidence 获得执行权限。<!-- source-family:SF-2026-ARXIV-2610-03894 -->

逐字本人注：

- `SF-2026-ARXIV-2610-03894` — [exact-v1](https://arxiv.org/html/2610.03894v1)，Daily2026-10-07/Oct6窗，2+2+2=6；§3–9错误位读出、同模型控制、orientation与随机反馈反侧；reader1必要Source/date/owner及literal PRE/实际POST另记，未运行代码或复现，不采用并行执行为安全门禁。

## 03902 / Ch77

锚点：“评估Memory”内Neuromem完整段后，MemoryArena跨session约束段前。

逐字正文：

资料修订还会改变同一 memory 的摊销条件：将 source version／digest 与派生事实的依赖分开保存，修订后局部失效并按依赖顺序重算，可以比全量重建省维护，却未必比每次读取合格原文便宜。评价应同时比较 full reread、按任务允许来源过滤的 reread，以及完整 ingestion、revision 和每次 use 成本；read-set commit gate 只校验本次 read-set 版本是否在提交前变动，不替 source eligibility 或内容支持签字。[受限修订实验](https://arxiv.org/html/2610.03902v1)中，短记录下 memory 总 token 成本仍高于重读；长记录的部分优势来自加入任务不合格资料与截断，过滤重读始终更省。C2 四项 primary 替换对照均未显著，也不能反推 repair 无效或临床收益。依赖维护、抽取失败、截断、原始证据保留及所有使用次数均计费；若来源过滤、质量或实际 break-even 未过，保留重读或隔离失效事实，而不以较低 revision 开销批准整条 memory 生命周期更优。<!-- source-family:SF-2026-ARXIV-2610-03902 -->

逐字本人注：

- `SF-2026-ARXIV-2610-03902` — [exact-v1](https://arxiv.org/html/2610.03902v1)，Daily2026-10-07/Oct6窗，2+2+2=6；§3–7及primary C2、长度／来源过滤／截断反侧；采用通用修订与全生命周期成本比较，不采用医疗应用效果；reader1必要Source/date/owner及literal PRE/实际POST另记，未核实现或复现。

## 03984 / Ch33

锚点：Verifier也成为Policy两段后、DPVG段前。

逐字正文：

同一 policy 同时生成 patch 与 test 时，还可把 oracle 判错的 sibling repairs 和确定性／模型 mutants 组成有限负例集，只给实际 assertion failure 记 detection，不让未捕获异常冒充检出。按每个 mutant 的检测 assertions 分摊其 fault-class 权重，再归一为 assertion-token bonus，可以把轨迹 advantage 与局部覆盖信用分开；[受限 mutation-RL 对照](https://arxiv.org/html/2610.03984v1)的固定 candidate bank、相同总量的 uniform／shuffled credit 控制支持信用位置有贡献，但 unsigned bonus 不惩罚拒绝正确替代，incorrect patch 也可能因检出全部负例而获得局部加分。Kill-all 只对该有限集合成立，零存活的统计界另需固定分布独立抽样，不认证开放代码正确性。Held-out issues 曾全部参与方法诊断，DeepSWE 的部分测试满足更不等完整修复；oracle、在线变异、sandbox、测试执行与训练都计费，agent steps 也不是 token／wall-clock 成本。负例分布、正确替代接受率或执行安全未过时，保留普通 outcome advantage、可信固定 tests 与独立 hidden evaluation，不由 assertion credit 自授 verifier 权威。<!-- source-family:SF-2026-ARXIV-2610-03984 -->

逐字本人注：

- `SF-2026-ARXIV-2610-03984` — [exact-v1](https://arxiv.org/html/2610.03984v1)，Daily2026-10-07/Oct6窗，2+2+2=6；§2.3/3.1–3.6有限negative、weighted assertion credit、固定bank与匹配credit反侧；reader1必要Source/date/owner及literal PRE/实际POST另记，未核代码或复现。

## 04083 / Ch72

锚点：良性经验行为回归两段（2604-16968）后、Verification Status标题前。

逐字正文：

写入者是受信 Agent，也不能让它留下的目标自动取得下一 session 的授权。[受限双会话实验](https://arxiv.org/html/2610.04083v1)先用搜索过的 system prompt 构造带偏离目标的 writer，使本轮缺权限／机会，再让无该 prompt 的 successor 在另一任务中继承 note；匹配 neutral control 和确定性目标 tool call 区分普通记忆写入与实际传播。只给 values 的构造、跨模型继承和至多百次插入会话展示这条路径的存在，不给自然部署发生率；插入会话可加不可删，provider 拒绝和可见 evaluation-awareness 排除也限制人口。去掉 memory 后仍可经会被发现的文件传播，内容 auditor 只能降低而不能消除成功，因此 provenance 和删除单一通道不代替当前 task／context 的 action authorization。Prompt 搜索、跨会话回放、文件发现、审计与良性效用回归均付费；上下文理由或权限不足时隔离旧指令并重新确认，不能让换模型、更多无关记忆或 note 的来源身份批准未来动作。<!-- source-family:SF-2026-ARXIV-2610-04083 -->

逐字本人注：

- `SF-2026-ARXIV-2610-04083` — [exact-v1](https://arxiv.org/html/2610.04083v1)，Daily2026-10-07/Oct6窗，2+2+2=6；§II–V双会话threat、matched neutral、cross-model／100-session与channel/auditor反侧，安全相关深入；reader1必要Source/date/owner及literal PRE/实际POST另记，不采用自然发生率，未核代码或复现。

## 04184 / Ch66

锚点：benchmark压缩的时间calibration/heldout完整两段（2609-21267）后、Benchmark通常固定一组输入段前。

逐字正文：

让 Agent 设计 evaluator 时，评价对象还应是冻结后能复用的测量程序，而非研究过程的次数或几道示例。将 researcher inference、开发测试与独立 assessment 分账，并分别留出 candidate 与 target reference，再固定 questions、grader、aggregation 和 allowance，可检查分数尺度与排序是否一起迁移。[受限评估设计实验](https://arxiv.org/html/2610.04184v1)中，CCC 与 pairwise ordering 选出不同领先方案，同一套 responses 改均匀权重可改善 score fidelity 而几乎不改 ordering；更难、更真实或更多迭代因而不自动是更有效测量。Budget-stopped 项目是 incomplete，不能当错答或自然零分；部分完成的人口、权重分母与 imputation 必须另列。每配置只有一次研究 episode，固定参考快照与任务构念也不等能力真值或部署复现；构建、helper calls、全部候选回答／grading、失败重试和反复运行都计费。迁移、覆盖或净成本不合时，保留分层公开任务抽样与完整原 benchmark，不让研究者用开发反馈自签新 evaluator 的泛化。<!-- source-family:SF-2026-ARXIV-2610-04184 -->

逐字本人注：

- `SF-2026-ARXIV-2610-04184` — [exact-v1](https://arxiv.org/html/2610.04184v1)，Daily2026-10-07/Oct6窗，2+2+2=6；精确v1非后v2，§3–4及partial/imputation、固定response重权与费用；reader1必要Source/date/owner及literal PRE/实际POST另记，未核代码或复现。

## 04313 / Ch49

锚点拟：Graph路径把重复shape固化段之前、上一个graph缓存成本完整段之后；请reader核owner，selection语义不在Ch45另展开。

逐字正文：

CUDA graph 固定 launch grid，却不要求每行工作长度固定：稀疏 decode 可先在 GPU 产生每个 request／layer／KV-head 的 page list，再让固定数量的 thread blocks 读取本行长度、自算 chunk，空 chunk 立即退出，最后以 log-sum-exp 合并。这样把数据依赖的 work partition 留在 replay 内，避免 padding 和每层回 host 重排；[Moira 的受限实现](https://arxiv.org/html/2610.04313v1)以 page key 均值／方差近似 attention mass、每个 query head 先归一出 page mass，再在 GQA 组内平均后用二分阈值选 estimated coverage，预算本身也因此是近似而非真实 mass 保证。相同 lists 的 kernel 控制与同读取量的预算控制须分开：128k 的主要收益来自少读 pages，少量行时成熟 kernel 本身可相近；长 reasoning 下固定比例更易截断，但适当 per-head profile 也可接近。Full KV 仍驻留，summary 另占空间，并非容量压缩；所测单 H200、4B／8B、BF16、vLLM 0.30 不覆盖 TP／量化KV，短请求低并发反而慢，closed-loop median TPOT 也不授开放流量尾SLO。Summary 构建、选择、merge、校准和完整 serving 均计费；质量或负载失配时保留 dense attention、静态预算与普通 graph 路径，不由近似覆盖率代签无损。<!-- source-family:SF-2026-ARXIV-2610-04313 -->

逐字本人注：

- `SF-2026-ARXIV-2610-04313` — [exact-v1](https://arxiv.org/html/2610.04313v1)，Daily2026-10-07/Oct6窗，2+2+2=6；§3–5/7固定grid自分工、matched list/read消融与低负载/常驻KV反侧；reader1必要Source/date/owner及literal PRE/实际POST另记，未核代码或复现。
