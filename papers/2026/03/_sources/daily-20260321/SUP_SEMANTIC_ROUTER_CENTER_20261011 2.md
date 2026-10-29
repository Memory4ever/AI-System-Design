# SemanticRouter18174：必要原证与中心隔离提案

准备者resume_mar18，仅03-21补BJT03/20；本日准入/官方日级夹证复用，未独核、未计safe或DAY。当前候选拟2+2+2=6，评分对象是连续ML信号进入编译策略时co-fire/selection语义的新增解释，不给传统防火墙、priority/硬授权等成熟原则新分。不是因负面、没有benchmark或产物规模排除。

## 必要 exact-v1 与直接反侧

[原HTML](https://arxiv.org/html/2603.18174v1)必要§2.2–3.2/4.1–4.3/5–7/Table1，§8语义授权外推与10–11实际读。没有追旧相关work、代码或后版本。

- §2.2–2.3每signal score越threshold转Boolean，routes按priority first-match；同query math=.52/science=.89都过.5而math获胜，是原机制例子，不是实测概率/错路由率。§3分crisp、geometry、classifier，再区分结构shadow/redundancy与分布co-fire/calibration。
- Theorem1把球帽有无交集称co-firing probability可判定；实际角距小于两阈值角和只判空间交集，不能无输入人口P(x)推non-trivial概率。类别名单互斥亦不证实际score激活互斥；神经classifier一般“undecidable”未有正式计算问题/归约，缺分布与不可判定不等，三层普遍定理不采用。
- 核心Theorem2称θ>1/k、τ→0可任意输入至多一个激活；proof还声称有限τ由Σp=1就至多一个超过1/k。明确反例k=3、θ=.4、p=(.49,.49,.02)，Σp=1而两个超过θ；这些p可由有限logits=τlogp产生。τ→0时两个相等最大logits的极限(.5,.5,0)仍两fire，故“任何输入”也不能删除ties。严格>阈值.5可保证至多一个但允许全不fire；explicit argmax+tie/default/reject规则是另外的消费机制，不等原threshold配方已证。没有用修复后一般原理替原中心claim写书。
- §6.3由siblings sum1推architecture不可能coactivate同样缺threshold与tie条件。§6.4 numerical example softmax([.52,.89,.31]/.1)写(.24,.72,.04)；实际稳定计算约(.02406,.97300,.00295)，唯一science结果相同但不能照精确数字校准temperature。这只定点算术，不扩全库实现。
- §5 category overlap/NOT guard提示、SIGNAL_GROUP metadata/default、TEST query→route和TIER提供作者公开接口事实；auto-NOT改变原优先匹配可见规则，不证最佳语义。§7/Table1区分implemented compiler constructs与future FDD/typecomposition/coherenthead；runtime normalization只config，parse/compile/decompile roundtrip不证明classifier正确/权限安全。无co-fire率、任务品质、真实分布、temperature sweep、批量/并发/硬件/完整成本或seedCI实测；Not Disclosed，而不是以缺实验作EX理由。
- §8将softmax_exclusive外推语义RBAC防privilege escalation和gateway/data governance统一正确，依赖上述中心互斥桥，且互斥路由不等已核授权；未知输入可迫选而不得提升trusted principal。§10原文承认online realpopulation co-fire monitor是future，未由table implemented授生产/部署保障。

## Actual owner 与提案处置

sole `PLATFORM-GATEWAY`，实际Ch62 94–127 identity/semantic候选/授权分责，148–188完整typed evidence→learned router→hardeligible边界；Ch61/63开篇。现文确有hard-filter-first/可信证明不等分类器，但没有连续score多阈值co-fire与编译保证接口，不假称完全NC。潜在具体差额不改变中心公式失效：本次拟**中心争议终态隔离**，不写Books，不虚NC、不降分/EX，不用旧一般硬授权原则绕过争议制造diff。

仅一次必要请求：相同原family的修订定义/证明或作者原协议，明确finiteτ、多阈值及ties/no-fire/default的consumer条件，且将球帽交集与真实输入概率区分；如还主张语义RBAC安全，须有独立授权合同而非分类互斥替代。收到后只重开Theorems1–2/§6.3/§8及该owner差额，不追作者全史或全production实现。在此之前原公开compiler接口可作有限上下文，但不支撑正面formal conflict-free、概率/安全Evidence或Coverage。等待非准备者独核该中心处置，不预支safe/DAY。

## root 非准备者独核：中心隔离有限通过

root实际读exact-v1必要§2.2–4.3/5–7/Table1、8.1–8.2及10–11；实际Ch62完整94–127/148–188和ROADMAP唯一owner回对。反例k3、θ.4、有限softmax(.49,.49,.02)确实双fire；相同最大logits在零温极限亦不变成唯一1，球帽非空不取得真实人口概率。正文没有将threshold改成explicit argmax，因此不能沿作者中心保证认证互斥或RBAC安全。implemented与config/future区分和未给实际co-fire率保持，缺benchmark不是排除依据。正式有限PASS：2+2+2=6不改、中心争议终态隔离，不写Books/不假NC；请求及定点重开范围足够，不扩其他论文或代码。不授DAY。
