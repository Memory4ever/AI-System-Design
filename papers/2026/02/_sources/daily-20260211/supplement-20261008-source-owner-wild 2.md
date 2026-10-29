# WildReward08829：必要Source/owner/PRE请求

WildReward: Learning Reward Models from In-the-Wild Human Interactions，精确2602.08829v1；2+2+2=6，自然followup→筛后ordinal反馈监督与RM的具体观测/目标接口深入。root完整AB/日期已通过；wild-core.json完整§2/3/Limitations实际读，wild-direct.txt必要A/B L245–268。无实现/复现，不读无关prompt图附件。

§2从WildChat4.8M取history/query/response/followup。先10k classifier、200manual样本：82%neutral/17%negative/1%positive，neutral86%新request/14%relevantfollowup，未披露每class完整manual人口/CI。gpt-oss120b分五类，neutral默认，relevantengagement视positive是观测假设而非quality真值；相邻两turn同topic cosine>.6/MiniLM、20例90%支持为implicit mining依据，新增12,310约+29%；572拒绝负反馈纠偏由同classifier做refusal validation，不独立safety gold。去remainingneutral后186k四类，ordinal BCE对三个y>k，reward1+ΣP(y>k)是固定1…4编码的期望等级，不是真实cardinalutility或天然calibration；未证明所有三个head概率有序约束。

AppendixA只EN/CN、text/noexternaltool、去外部context、>20turn、query<5words/response<10words；feedback可观察与筛选人口不同，不能批准所有部署反馈。Qwen3-4/8B一epoch/H100/TRL/batch512/lr1e-5/seq4096；precision/GPU数/重复CI/全classifier+data+policybudget/SLO未披露。RewardBench8B86<INF95.1、Judge66<INF70.2，非全winner/8B全优4B（PPEHuman4B61.6 vs8B62.5但仅切片）。T2去refusal SRF90.4→28.5，SRP72→97反侧；去feedbackminingSRF68.3/SRP77.5，也改变data人口，非固定同样本label单因素因果。更广user10x同size实验未完全控制user人口topic/feedback，不能claim diversity唯因果。

§3.4 Platt fit50%/eval50% RMNormal，ECE2.76vs8.81只是该pair population/bin校准；chosen−rejected signedmargin在gold方向定义，Fig4用margin>.2筛后87%/约50%coverage，不能直接授线上未知chosen身份的confidencefilter。§3.5 WildChatheldout5000→negative downsample→1000双作者去噪（任一flag剔除）→948同pipelinebinary labels，AUC只分此筛后正负人口，不识别跨query绝对utility或通用threshold。§3.6 DPO20kprompt difficulty去1/5，60%subjective/20%math/20%commonsense；offline4response、online8不是预算matched，当前policy对分布影响是解释。OnlineWild average62.6vsArmo60.4而MMLU48.9<50.3；offline MATH48.6<49.6/Arena55.4<55.7。H100/verl/batch64/8rollout/lr5e-7/seq4096；gpt4omini-20240718judge、IFEval四类平均不可当strict only。无PPO/GRPO RL验证，不以OnlineDPO命名推一般RL稳定。

actual TRAIN-RLHF Ch31 101–125已有pairwise目标/ordinaltrajectory/LMgrade marginal与rating强度，但缺自然followup不是显式annotation、保neutralunknown与正当refusal负反馈policy分责，和三个阈值classifier→期望ordinalgrade读取的接口。Ch30/32开头交接actual重读，Ch34在线pair形成分责已核，可复用。唯一owner Ch31，拟在现有LM-grade ordinal段后加一段。尚未root Source/PRE/锁，不写Books。

等级监督还可以来自真实对话的后续反馈，而非预先要求用户给一对答案排序。一个有界路径先区分显式拒绝、错误纠正、积极参与和明确满意，保留无明确信号的unknown；再为各等级阈值学习“是否高于该级”的概率，以固定编码的期望等级读出reward。这把反馈来源与reward目标分开，却不能把相关追问自动当正确性、没有反馈当负面，或把对正当拒绝的不满当应被优化掉的行为。相邻turn回填与拒绝核验均是版本化观测规则，须保标签出处、筛选人口和独立安全/任务效标；有序类别也不识别真实数值间隔或跨query效用。采集、分类、人工校准与在线候选生成都付费，有限onlineDPO收益不证明所有RL或等预算优越；反馈稀疏、筛选漂移或阈值未校准时，保留明确unknown、可信人工偏好与独立行为检查，不让用户参与度接管安全授权。

拟链接exact-v1#S2；自身末注保原生反馈人口、refusal/SRP反侧与ordinal/校准分母、online/offline预算。请求root必要Source与actual owner/PRE后授窄锁。
