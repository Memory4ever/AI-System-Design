# Nov22 四个训练消费最小域

作者Noether；承接[LEARNING15](SUP_ARXIV_LEARNING15_20261015.md)四M。只读下列精确v1必要接口/限制，未读全图/全实验/代码，不预独核或日期。

## SlsReuse 17262v1：M→窄P

[原HTML](https://arxiv.org/html/2511.17262v1) §3.2/3.3 Algorithm1原L119–210实际读：LLM分别取intent/platform/cloud-service/language四元组；某属性query=None跳过，完整覆盖/superset候选保留，partial则按Jaccard distance与缺覆盖的Pareto集合保留，再以SentenceBERT intent cosine排topK。这比“prompt+检索”具体，改变硬约束不完整时如何避免全空或不兼容推荐；不是retrieval分数替运行兼容性。LLM抽取误差和逐属性prune顺序可能漏候选，不授可执行/平台语义正确或91.2%。潜力已清，不扩110query/全部函数。

## ReVul-CoT 17027v1：M→具体C

[原HTML](https://arxiv.org/html/2511.17027v1) §3.1–3.4、§4.2和Threats必要域（原L174–231/269–272/451–458）实际读：CodeBERT与description CoSENT各cosine加权，topK带severity/CVSS/CWE知识作few-shot CoT分类，未给区别已有双路RAG/CoT的新增执行机制或一般成立边界。所读贡献为领域severity数据/组合与指标，不因安全任务自动准入。NVD有CVSS原评分等字段，输入信息权限与test同源需分开；weak zero-shot不能排training/label污染，公开CVE不能推未披露漏洞，CoT不是解释真值。没有采用MCC/通用防御，未指控泄露已发生，未声明全split已核；足以作当前具体C，不扩12070条/全部比较/日期。

## AUV 16900v1：M→受限P

[原HTML](https://arxiv.org/html/2511.16900v1) §III-C Eq21–30/Algorithm1及§IV必要LLM消费者与结尾限制（原L195–270/366–377）实际读。LLM从预定义函数库按任务语义选f_j，训练constraint violation可触发switch；learned critic softplus保正，actor约束用old/new当前state动作值差与reward；算法先Q挑diffusion候选，再在update步施LAC，不能说每个实际动作先经过严格Lyapunov证书。Eq30近似关系/函数switch没有独立充分稳定性保证，单state positivity不等完整Lyapunov条件；plots/系数不同曲线不识别LLM为唯一原因。保留语义外环选择/critic消费的明确接口潜力，不授exponential stability、真实海试安全、全形式证明或图像全部已读，不扩全部仿真。

## FLARE 16450v1：M→P

[原HTML](https://arxiv.org/html/2511.16450v1) §II-B–D/III及限制（原L77–151/185–189）实际读。四向filter在发/收task data与result做量化/反量化，aggregation/local train回原dtype不意味着信息无损；container按dict单item序列化，file按chunk读，改变“线路分块但仍预分配整object”的峰值额外内存条件。最大item仍可能约1GB，file传输缓冲不等训练总内存或自动zero-copy。非IID多轮累积误差、端到端带宽开销/operational resilience未评，secure aggregation/DP兼容性不授。保留实际通信/重组接口潜力，不采14%/无损收敛或deployment ready。

LEARNING15当前由10P4M1C→**13P2C，M0**。SDA/SHAP/COPYCHECK必要受影响域另行具体处理，非这四M重复；新增current及其余已观察标题/date/six普通工作继续。

后续已实际读Ohm§12，15168v2原C凭具体TableII/错绑原证局部恢复P，见LEARNING15末；不重该有效最小域。当前合并为**14P1C/M0**，上句13P2C是该单身份更正前阶段，不控制终态；17027具体C及本包其他决定不变。

已实际消费Ohm§13/root转达的ReVul分区澄清：原声明knowledge80%、validation10%、test10%，retrieval只用knowledge80%。该明确分区保留，不说完全没有split；但不等预训练、重复、时间/项目泄漏均排除。原“未声明全split已核”只限制作者阅读权限，不撤销原文明确分区或请求重读四Methods。14P1C及四门3P1C现已真实独核通过，后续只按此层归并。
