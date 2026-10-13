# 03-18 补03-17 必要证据与 Books 提案（进行中）

精确版本均 v1；日期夹证口径经非作者核验：Submitted仅给最早常规公告日、官方arxiv.content/findable注册给已有公开上界，同BJT03/17才能推断首arXiv日，不冒充精确公告时刻。MoDA/ClawWorm不进入此确定池。首次8项ID/同稿标题对2026 Daily README定点去重无有效同事件采用；03/17旧线索不是已完成判断，MoDA03/16保留不搬。

## 14591 FlashHead — 2+1+2=5；采样语义差额定点深入

[exact-v1](https://arxiv.org/html/2603.14591v1)，实际§3.1–3.3、§4.1–4.5、§5、AppendixC/D/D.1；原件SUP_METHOD_A/B/D。离线等容量spherical k-means使C2T变成dense index，centroid scoring→选p簇→候选token高精度projection。Llama3.2-1B词表128256、c8016/p512，离线1000iterations约4h单A40；training-free仅不fine-tune，不等零准备费用。

Greedy是受限制候选最大值：相同hidden/KV的XNLI top1为97%，不是全vocab exact argmax。随机路径以centroid概率无放回抽簇再在所选tokensoftmax；AppendixD明确边缘分布q(t|h)=E_S[q(t|h,S)]，这保持全词表非零机会，不证明等于dense softmax。此区分是本报告推断而非作者自称exact；不能把fullsupport/相似task均值写成原分布保证。概率任务100条子集、10000probe集合MC，没采到token以当前最小非零概率clip；不可把其loglikelihood数与精确dense计算混为相同协议。5独立clustering重复支持局部鲁棒，不给统计等价结论。

GPU测量：RTX3500Ada、vLLM、batch1、100prompts+10warmup、每128输出tokens，BF16或W4A16。基准Llama1B的head1.94→0.40ms(4.85x)而全模型BF167.69→6.15ms(1.25x)、INT43.60→2.06ms(1.75x)。输入长/并发/SLO Not Disclosed；FGD仅CPUfloat32未进入GPU/probability对照。不同模型head收益递减，8B BF16 OOM，§5把largebatch/server扩展列未来方向。未核artifact/复现。

Books比较：MODEL-SAMPLING Ch20现正文19–64定义dense目标、102–139定义截尾并renorm、157–190固定processor/RNG，尚未区分随机候选检索的全support与dense目标分布。Ch19末handoff仍KV语义、Ch21首handoff返回MLP组织，无冲突。拟在Ch20“一个固定logits例子”之前补最小两段（只采样语义，不接管Ch12projection计算）：

> 上面的完整 softmax 是目标分布，不要求每种实现都先形成完整 logits。若为了减小词表头的读取量，先按簇抽取一个候选集合，再只对集合内 token 归一化，就必须区分“每个 token 都有机会入选”与“仍按原分布抽样”。令 S 为随机候选集合，最终边缘分布是 q(t\|h)=E_S[q(t\|h,S)]；全词表非零支持并不单独保证它等于 dense softmax。Greedy 检索遗漏最高分 token，或随机集合改变归一化分母，都会改变 next-token 的决策语义。
>
> 这是一条以离线簇索引、候选读取与近似误差换资源的分支，不是 top-k/top-p 的等价实现。受限词表头实验只在已披露模型、batch1 RTX3500Ada条件下显示任务均值与端到端延迟取舍；head加速不能代替完整模型收益，概率任务的Monte-Carlo估计与零概率修补也不是精确likelihood。需要原分布、严格复现、罕见token覆盖或大batch吞吐时，应保留dense路径，或另作分布误差与实际成本验收。

当前仅 Source/逐字PRE提案，尚未获锁、未写书、不授POST/DAY。

## 14633 When Scanners Lie — 3+2+2=7；设计反证深入

[exact-v1](https://arxiv.org/html/2603.14633v1)，实际§4.1/4.2、§5.1、§6、§8、AppendixA.1/A.2人类验证/成本反侧；SUP_METHOD_C0/D。固定attack-response，只换static/Grok4.1judge计算样本disagreement，D>tau=.05只触发增强检查，不证明任何一方正确。Garak0.13.2、25attack、MistralSmall8B/CommandA111B/GPT5mini、temperature0、3runs、每category至多100、max512。名义约23K pairs与附录每scan最多1800并不严密同分母，故不推更精确总量/生产率。

增强层GPT5.2不看前两个标签；所谓89%对72%是与该verifier的一致，而非独立groundtruth全样本accuracy。200样本人工由第一作者单标、同attackrubric，93%一致/kappa.85、10FP/4FN，不能排共享rubric偏差。22/25类别越阈、6类别D>.5只证明该配置测量不稳定；4类别static更好。majority .881反低于Grok .893，17类别替换达到.899后全替换回.893，不能宣传所有dynamic更好。作者费用按AzureGrok4.1token价格估算，latentinjection近47.4%input；图caption基础$14.38与正文$14.86不一致，不采用精确统一base费用。硬件/precision/SLO Not Disclosed，不把verifier换名当真实独立性/安全保证。

拟采用边界：ASR是attack/response/evaluator三者共同测量产物；先以同一response配对差异作稳定性诊断，再用独立标签与成本选择局部升级，保留static有优势切片。现owner PLATFORM-EVALUATION-SYSTEM Ch66已有EvaluationIdentity/per-verifier outcomes/aggregation/strongverifier分权，需定点比较其正文是否已承载“固定response的evaluator替换diagnostic”差额，尚未申请锁或写入。

## 首批其余普通待审

15031 AttnRes拟2+2+3=7，exactHTML转换缺正文，已取21页exactPDF并实读§2/3/4；Ch17现431–455已有depth-history/blocksummary/statecost主命题，后续评价与具体差额未定。15202 LMetric拟2+2+2=6、15340 DOS拟2+1+2=5、15401 SWE-Skills拟3+2+2=7、15530DUET/15589LEXI拟2+2+2=6；核心精确HTML可得，普通评价/owner比较未完成。分数按拟采用新增命题而非主题映射给出，独核前不授Evidence完成。
