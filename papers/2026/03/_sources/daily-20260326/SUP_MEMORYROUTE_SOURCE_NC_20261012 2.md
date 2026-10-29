# MemoryRoute necessary Source / actual NoChange

作者supp_mar26_fresh，仅03-25增量。2603.23013v1，2+1+2=5与本日日期已独校；不因Books覆盖排除贡献、降分或不审。当前拟具体已有覆盖，待非作者必要独核。

实际[exact-v1](https://arxiv.org/html/2603.23013v1) III-A–D/Eq1、IV-A–E、V-A–E/TablesI–V、VI limitations及成本投影边界已读。拟采命题仅为：记忆是否提供真实支持与confidence是否让小模型被选中是两件事；检索质量、消费资格和最终QA分别验收。所谓logprob floor线性变换不是校准正确率；raw高confidence可在无个性事实时仍接受错误。两轨保存turn pairs/timestamp/userpartition再retrieve→inject→cheap probe→escalate，回写仍需provenance与治理，system-context注入不授原对话事实权。论文关于“错误记忆一定降低confidence”的解释不能作为保证。

LoCoMo仅conversation26/19sessions/214turns/152QA，warm一次预装steady-state不是在线累积能力证据；single MI300X192GB，Qwen3VL8B BF16/32K vs235B22BactiveMoE AWQ/16K，非公平同precision同context规模定律。TII cold96.1%在8B/warm100%说明该τ .50下路由变化很少，而QA有差异；§V-C 301明确warm probe截断context使16K输入vsmemory-only103K，2×2不是每个条件相同输入长度的完全归因实验。TI temporal warm10.3低于cold8B14.1、fullcontext大模型43.9高于warm30.5，不能写memory普胜规模。摘要+15.0与30.5−15.4=15.1不扩大精确宣传。LongMemEval底库500但管线只100分层QA，TV multi-session/assistant反退，hybrid增加打分/索引费。不把publisher baseline混协议比较、tokenF1当语义真值。

EffCost按总参数量乘input+4output，是估算，尤其MoE22Bactive/不同量化不按总P直接测实际能耗/墙钟；后段美元价投影不是本次实付或当前费率。缺硬件利用、servingbatch/concurrency/TTFT/latency/SLO及memory编码/索引/维护全生命周期费，不授96%净省费/Pareto最优、warm随时间必然收敛。未核artifact/复现。

## actual owner coverage

sole AGENT-MEMORY Ch77，实际完整174–224 memory-quality/规范双经验→受约束读取→sparse/dense cascade→explicit-field disambiguation→非对称索引→skillrouter→score/ACL/provenance→增量投递与费用；1667–1688 hiddenchannel→评分/模态路由/写权限分离→proceduralgraph与projection开头；Ch76/78开篇交接已读。现188–191真实正文明确router只拥有执行计划、margin非事实置信、错skip漏证据及强制fallback；193–217保存完整source/条件与tenant权限，不授similarity真实性；1672–1676明确模型自评分不保证可信，独立核验/事实状态与selection分离。该批局部实验为这条已承载判断的具体反证验证，不新增足够独立的长期控制链；因此已有覆盖/NoChange，不造正文或来源注diff，也不将这篇笼统称低价值/组合即EX。

后续若取得改变上述控制选择的新事实，如matched context/端到端总费用且可信度校准可复查，只定点重开对应采用命题；当前没有访问受阻或中心可靠性正面采用。待reader独立实际Source→具体owner覆盖通过后Report同步标准完成/已有覆盖，非DAY。
