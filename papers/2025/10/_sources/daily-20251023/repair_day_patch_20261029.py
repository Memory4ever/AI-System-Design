"""Render this day's manually authored report reconciliation as an apply_patch input."""
import json
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPORT = ROOT.parent.parent / '23' / 'README.md'
BOOKS = '../../../../books/'

OWNERS = {
    5: ('WORLDVIEW-REPRESENTATION', 'part-01-worldview/05-what-neural-networks-learn.md'),
    14: ('MODEL-SELF-ATTENTION', 'part-02-model/14-self-attention.md'),
    15: ('MODEL-MULTI-HEAD-ATTENTION', 'part-02-model/15-multi-head-attention.md'),
    23: ('MULTIMODAL-REPRESENTATION', 'part-03-multimodal-world-models/23-multimodal-representation.md'),
    24: ('MULTIMODAL-GENERATIVE-PARADIGMS', 'part-03-multimodal-world-models/24-multimodal-generative-paradigms.md'),
    25: ('MULTIMODAL-WORLD-MODELS', 'part-03-multimodal-world-models/25-multimodal-world-models.md'),
    26: ('MULTIMODAL-EMBODIED-VLA', 'part-03-multimodal-world-models/26-multimodal-embodied-vla.md'),
    27: ('TRAIN-DATA', 'part-04-training-system/27-data.md'),
    29: ('TRAIN-SFT', 'part-04-training-system/29-sft.md'),
    30: ('TRAIN-LORA', 'part-04-training-system/30-lora.md'),
    33: ('TRAIN-GRPO', 'part-04-training-system/33-grpo.md'),
    36: ('TRAIN-DISTRIBUTED-TRAINING', 'part-04-training-system/36-distributed-training.md'),
    45: ('INFER-KV-CACHE', 'part-05-inference-system/45-why-kv-cache-speeds-up.md'),
    49: ('INFER-TENSORRT-LLM', 'part-05-inference-system/49-tensorrt-llm.md'),
    56: ('INFER-SCHEDULING', 'part-05-inference-system/56-inference-scheduling.md'),
    66: ('PLATFORM-EVALUATION-SYSTEM', 'part-06-ai-infrastructure/66-evaluation-system.md'),
    72: ('PLATFORM-SECURITY', 'part-06-ai-infrastructure/72-security.md'),
    75: ('AGENT-CONTEXT', 'part-07-agent/75-context.md'),
    76: ('AGENT-RAG', 'part-07-agent/76-rag.md'),
    81: ('AGENT-WORKFLOW', 'part-07-agent/81-workflow.md'),
    82: ('AGENT-MULTI-AGENT', 'part-07-agent/82-multi-agent.md'),
}

# Each tuple is an authored contribution, actual owner decision, and evidence judgment.
ENTRIES = [
('18003', '审稿警告与接受gate可以分离，校准accept率不等辨识真实性', 66, '已有覆盖',
 '精确v1 §3.1–3.5/4.1–4.2/5.1–5.2：单pass reviewer无运行或联网证据，三模型同提供商不能据角色数假设错误独立；rate matching/isotonic拟人类接受率而非真伪。50真实+50合成人口中，ReD增加警告仍可能提高接受，DetOnly高召回付高FP；AI生成不等造假，GPT5 concern judge也非事实真值。保警告未约束决策这一局部反侧，不采集中界为fabrication检出证书。',
 'Self-report、Behavior Probe与Deployment Outcome段已把自述、实际决策及外部effect分验；Ch81计算guard是交接，不需重复改书。'),
('18032', 'verbal feedback改变通信边与聚合，但不等参数RL或最优图', 82, '已有覆盖',
 '精确v1 §3.3–3.6/4.1：以初始utility构边，reflect/act增删并乘性调整edge，最终保peer和majority。训练正确性反馈不能变成线上oracle；每任务三训练点、100评价/三run、不同API模型并非等token单agent比较，全部边访问/反思/聚合计费。只采任务反馈可改变拓扑这一受限机制，不授全局最优或更密图更好。',
 '实际动态mutation/peer evidence-ledger连续块已允许改边、插critic及串行副作用，明确版本迁移、authority transfer、race/replay/rollback与探索预算；R32实际核。'),
('18085', '轮换单人示范与各自buffer使伙伴policy共同适应，区别固定阶段支持', 26, '整合',
 '精确v1 III/IV Alg1、V/VI/VII：每episode一成员接受人示范，其他当前policy执行，各buffer做BC。VMAS四任务10seed和三HeRo+机器人只支撑有限协作；中心相机/ArUCo与mock LiDAR不等分散感知，零介入navigation高方差且p=.0773，不授普遍显著sim2real或安全。人工示范、更新、标定与纠错全计费，共适应带来非平稳伙伴分布，无联合最优/收敛证明。',
 '原顺序模仿段已有单人/伙伴人口，故撤旧A3广义缺口；只在其后新增固定伙伴分阶段与episode轮换/各buffer共同适应的采集分支。修订完整PRE R28后实际保存，不把已有原则重复计新贡献。'),
('18087', 'AR提出主题/长度计划，再隔离span异步去噪并同步cache', 24, '整合',
 '精确v1 §4.1–4.4及R19评价：AR计划与隔离span内双向生成分开，同步后才共享内容/cache；格式合法不证明语义独立，未定span的KV不能当稳定prefix。最长span的steps ratio不是总NFE或墙时倍数。Dream7B/四H200与AlpacaEval只给质量/均值时延取舍，密交互版本更慢却可能质量更好；教师标注、padding、全部denoise及cache重建计费。',
 '现固定block-size与视频长度expert没有该语义计划接口，已在固定block-size段后补异步隔离/同步、失准及顺序块/AR回退，不授等质量SLO。'),
('18091', '像素熵先于encoder构变长patch，并承担packing与dense回映接口', 23, '整合',
 '精确v1 §3.1–3.3/4.1–4.2/4.4/B：quadtree熵阈值决定patch尺度，resize及高分辨率残差补充后进ViT，packing mask隔图，dense任务回映网格。这不同encoder后删token，但像素熵非问题语义，简单背景也可能重要。8A100分类/8A6000 dense及单GPU推理，重实现layer merge禁weighted attention，不能泛比所有后端或授无损；packing/rearrange/细节补充均计费。',
 '在codec选择后仍解码RGB的段后新增encoder前可变patch与dense-consumer分责，保原跨帧feature分支与失配回退。'),
('18113', '低受骗率可能来自不行动，安全与任务完成须固定分母分验', 66, '已有覆盖',
 '精确v1 III/IV/V/VI/VII：四自建站14pattern、32任务/88情景、六agent各三run，用action trace及录像分DC/DF/EC/EF。50随机EF定性支持early-exit/interaction paralysis，不是全人口因果；UI变化同时改变可识别性。低DPSR不等防御通过，tailored prompt仅两scenario仍受骗；API/backend版本与生产base-rate未闭，不采通用安全排名。',
 '实际Response Rate、条件质量与无条件质量段已排除原样返回/不行动抬高质量，并分别验response、真实goal与effect；R32实际核，不增重复书稿。'),
('18114', '连续latent/token双channel加噪，可联合或先latent后token采样', 24, '整合',
 '精确v1名Latent Discrete Diffusion Models，仅continuous latent，后版discrete机制不倒填。§3.1–3.2及R19 §2.3/3.2/5：FUJI联合/SEQ先latent后token，内部仍factorized；理想factorized NELBO界不自动等实际忽略端点/调权loss的tight likelihood。unit norm防latent幅度规避目标，latent额外64steps须计总NFE；LM1B短文本外部PPL/entropy不是任务质量或真实似然证书。',
 '现AE→latent prior→decoder并未承载双channel共同去噪；在其完整限制段及原binding后新增联合/先后采样、全费与单channel/AR回退，未改codec owner。'),
('18117', '异步teacher扩demo pool与当前student回答是两个消费时点', 75, '整合',
 '精确v1 §4–5/A.4.1：entropy先决定检索ICL，仍不确定则异步teacher供后来请求，三次一致/跨模态匹配只proxy，不能追认当前答案已纠正。4–12B VLM/3shot与CodeCarbon/EcoLogits估费，SigLIP替各baseline encoder并非旧CLIP同配置；pool漂移、教师重复、检索/prefill及驻留全计，不称更新学生权重或实测全碳/SLO。',
 '现CIRCLE固定demo重标不含跨request写入。其后新增示例source/版本/可见次序/写入失效与当前回答分责，保后续Semantic Policy完整解释块，不授pool为原始authority。'),
('18121', '无参数core-attention按query shard重批，逻辑池与同GPU角色分开', 36, '整合',
 '精确v1 §4–6/8：CA-task为query shard加完整context K/V，CPU profiler/greedy按FLOPs与bytes调度，block128；in-place server在同GPU切CA与其余层，非物理独立空闲池或任意KV子块。Llama8B/34B、DGX H200 TP8、每配置30batch及合成长度；WLB-ideal重实现未含deferred execution，不是原系统等条件全胜。短任务通信可能暴露，模型忽略resident KV而高估bytes，precision/CUDA/完整profile Not Disclosed，不授无通信/1.35x普适。',
 '在原负载/搬运权衡段后新增query-token粒度与逻辑池/in-place角色、完整KV及通信覆盖条件，未取代TP/PP/CP或补未来fault tolerance。'),
('18123', '消息声明经receiver frame/本地perception消费，不靠平均风险授安全', 72, '整合',
 '精确v1 §4.1–4.2及R13 §5：语义/位置/时序检查字段max后跨agent/层平均，可能稀释单高风险，majority也可共同错。CARLA32个预设critical场景、四辆LangCoop车辆/200m模拟通信，等所有LLM输出后推进的ET是simulator time，不是真车wall-time截止；本地感知遮挡及坐标变换不是物理真值。只采消息到sensor消费的边界，不授身份协议或驾驶安全。',
 '在开放协议限制后补receiver frame与本地/多源perception消费、遮挡/共同错误和全部等待费；坐标推导仍归Ch26，未形成第二owner。'),
('18131', '静态constitution与触发后动态测试权限不同，未触发不等无漏洞', 72, '已有覆盖',
 '精确v1 §3.3/4/5.1–5.3，R13：先LLM筛查后对已flag项动态测试并融合，unseen风险category不等任意OOD。F1混benign MBPP/特定red集，非生产base-rate precision；生成测试不触发不能认证无漏洞，最终LLM融合非形式证明，工具/模型/测试全费。',
 'R20实际coding防御正文已把规范、模型flag、测试及未知输入分开，测试为有限witness而非完整安全证书；只采该局部新验证，不为BlueCode名称再增机制。'),
('18135', 'world-model候选修订与真实执行后观察分责，视觉质量不等控制效用', 25, '已有覆盖',
 '精确v1 §2–4：proposal→候选rollout→revision/score→只执行选段再观察，统一API不证明text/viewpoint/lowlevel因果等效。Habitat四类/RLBench四任务各50，proposal/base/revision及more-data一epoch预算混杂；panorama分辨率损失与manipulation有限收益保留。视频质量、候选scaling不授接触/控制或无限收益，所有WM/修订/后训练和执行计费。',
 'Imagined rollout与Open-loop imagination vs closed-loop correction已明确planner利用model漏洞、执行首项后真实observe重规划；本稿是局部验证，不把WM改名统一物理simulator。'),
('18148', '规则读出与activation干预仍不等真实行为机制', 5, '已有覆盖',
 '精确v1 §3/4/5/A.2：query-key/output-value交互提出skipgram等规则，只搜top100×100且忽略多feature/MLP。top激活正样本对随机零值负样本偏好recall，正文100/两split与附录150/三split不合并；无正预测时precision定1。GPT2-small首层prepend干预只支持该操作读数，不证明下游行为唯一因果；SAE/搜索/干预计费。',
 'Ch5实际信息可读、局部规则与activation干预/留出行为阶梯已承载三种权限，保本稿样本冲突及反例而不增加普遍faithfulness结论。'),
('18165', '跨步confidence决定重开与回退，局部进度不证明终止', 24, '已有覆盖',
 '精确v1 §4/5/6.3/C：历史unmask confidence均值作阈值，旧token下降可remask；正文单调叙事与c>=tau方向不直接相符，不抄作recipe。至少remask1可撤进度，无形式终止/target分布无损证明。LLaDA8B/A6000/长度256/block128/T0，五greedy运行非独立种子；质量/步数仅该人口，回退及总求值计费。',
 '实际“用跨步分布不稳定性分配Revision Budget”已把永久lock/可撤状态、阈值震荡、cache失效及总费拆开，Saber为代理实例，不重复写入。'),
('18179', '粗verifier增量选择协作/竞争及不同peer消费，区别只选worker', 82, '整合',
 '精确v1 A.1/Eq7/A.5.3支持按历史PR增量与探索选动作：协作吸收上轮高PR轨迹，竞争请历史高PR peer批评；不等state-conditioned价值已估计或有经典UCB保证。R4实际关键反侧：退化/对抗PRM曲线与状态探索仍未来，强QWQ被majority稀释，有限数值任务与跨provider默认超参不隔离全预算。全部模型/轮次/聚合计费，不授20%普适鲁棒。',
 '已有peer selector只选交给谁，新增本轮吸收proposal或请批评及各peer消费；R15完整PRE→W7真实SAVE/全自读→R18磁盘POST通过，窄位已释放，不行政重存。'),
('18204', '指南/代码slice双载荷检索与draft多facet分责，SecurePass是同sample交集', 76, '整合',
 '精确v1 §2.1–2.2支持漏洞修复/CWE归纳与PDG双向slice，draft诊断多facet/RRF消费；slice可能丢依赖，派生指南不授规范真值。R12 §3.1/3.5/B.3：CodeGuard+94场景的SecurePass@k要求同sample功能与CodeQL同时过，不认证未知CWE/全输入；Semgrep反馈非独立truth，API/本地A800混合不统一推时延，多轮draft/诊断为主要费。',
 '现MoM摘要/关系树没有安全指南与因果代码slice双载荷，故在完整MoM段/原marker后新增，保原文回读与payload角色，安全规范仍归Ch72。'),
('18291', 'photometric一致性可改善而metric深度变差，proxy不能认证真值', 25, '已有覆盖',
 '精确v1 §3.2–3.3/4/5.3/7.2–7.3/9/11：已知pose以backwarp指导latent及positive scale/shift，正则约束逐步梯度。深度优化可提高photometric同时恶化AbsRel，specular/illumination/尺度和scene限制保留；A6000约7s/768不含prep，不授实时或任意相机真值。',
 'Ch25几何生成后修订RGB-DN与Projective 4D Predictive State实际已有内部一致性/真实米制观测分验，本次局部新反证支撑该边界；不声称正文已有完整GeoDiff算法。'),
('18313', '联合panorama预测给自己规划打分不是独立道路安全证据', 25, '已有覆盖',
 '精确v1 §3/4：RGB/semantic/depth共VAE/PDiT，预测occupancy再造碰撞/边界/速度reward；联合误差相关，自己预测给自己评分非独立物理真值。Plücker/intrinsics归一不授任意metric相机。48A800/11.22B/batch48/NuScenes，planner主要150场景自身world，backbone/训练预算混杂，不把想象改善当真实道路闭环；生成/occupancy/reward全费。',
 'Projective 4D与Imagined rollout已限定联合分支、learned reward和想象成功无真实提交权限，保本稿局部接口，不因panorama/occupancy新增重复论证。'),
('18314', '攻击日志派生策略库并反哺后续生产，动态库改变测试人口', 72, '整合',
 '精确v1 §3.2–3.5及R12 §3.6/4：成功log转可检索策略继续evolve。Mind2Web240train/600test与baseline200口径冲突，不合并；ASR是10次内目标action triplet命中的pass@10，非单次真实损失率。测试期间库继续增长，不是冻结IID测试；移Strategist同时移evolution/library不能唯一归因。未提供或执行payload，库维护/全部调用计费。',
 '现archive只保存/评覆盖、固定style bank只分预算，新增日志→派生策略→增长库→后续producer接口，置于archive后、固定风格bank前，保版本/人口及回退。'),
('18315', '表征读数改善可以与任务表现脱钩，softmax前QK不等注意概率', 5, '已有覆盖',
 '精确v1 §4–6：475个小Transformer/PPO/H100，6/8元素枚举、维2–128与1/2/10M步；accuracy是correct swap比例。order metric用softmax前QK/sqrt，更高维readout继续改善而行为较早平，成功子集与未收敛人口分开。相关几何与probe无表征因果干预，不授真实环境world model或通用内部算法；训练/枚举/解释全费。',
 '实际cosine/CKA/probe与行为连续论证已明确几何、指定读出和实际使用不同验收，保局部反证，不因标题World Model改归Ch25。'),
('18337', 'generalist/domain expert交互hidden成为action条件，不需逐token文字推理', 26, '整合',
 '精确v1 §3/4与R30定点Reasoning Output：冻结generalist/运动expert以global/local mask交互，单forward双向token-wise hidden交action DiT，非逐token文字。主配14B组合，1B仅局部时延，300sim×3与50pick/place+200bussing，不同预训练/finetune预算未唯一隔离mask。运动hidden非物理真值，幻觉可传播；双主干、动作生成/controller全费，不授原能力全保或无增参加速。',
 '现mediator/action-query与raw/query双条件不含双主干运动hidden接口，在Mediator限制后新增该分支，保controller执行权、预算/质量验收与原路径回退。'),
('18353', '轨迹ranking surrogate仍有在线负样本与两模型成本，不等真实终态目标', 24, '已有覆盖',
 '精确v1 §3.1–3.4及R19：expert正/当前policy负的ranking，周期同步概率模型、threshold margin；无需成对人工负样本不等消灭online policy负例。理想density/trajectory下界与forward专家近似不证明实际收敛或terminal objective恒等；测试选点与online数据预算限制收益归因，proxy仍可hacking，双模型/训练/选择全计费。',
 '实际生成后训练的轨迹概率、反馈与信用分配段已承载在线discriminator/局部surrogate及全费，本次是局部参数化，不增另一份“无负样本”recipe。'),
('18358', 'member轴共享投影/MLP与head轴冗余不同，函数/校准须分别验收', 15, '整合',
 '精确v1 §4.2–4.3/5：同base剪heads造成员，grouped投影保流、平均共享MLP；不是独立模型原函数严格等价，单forward也有member activation/工作。ViT-B/ImageNet-CIFAR/OpenOOD、BERT/SST2，BERT DE(D)共享pretrain并非独立预训练，图像accuracy有反退；BF16局部计时不授全硬件收益。Taylor/UQ用不同信息，剪枝/恢复/校准全费，不从noise假设推普适robust。',
 '在head冗余总结后新增member分组与共享函数/uncertainty分责，保原动态head预算分支；不能以head越多自动等ensemble越独立。'),
('18383', 'teacher工具集合、答案与执行三reward分开，集合匹配不等全trace模仿', 33, '整合',
 '精确v1 §3.3/4.1/5.2/限制是strict tool-set exact match，不能以后版柔性F1替换；同集合不约束顺序/参数/副作用，执行成功非语义正确。Qwen3-235B teacher、四student，数学Python训练/RAG与BFCL-v4 OOD仍有任务反退；经gold核验的teacher答案作参考，采样/工具/验证/RL全费。仅保监督粒度选择，不授通用工具最优。',
 '现query参照/outcome不含工具集合粒度，在ChatR1原段/marker后补三reward权限及可信outcome/verified trace回退，唯一owner为TRAIN-GRPO而非重复一般SFT。'),
('18457', '冻结视觉prior并不冻结codec或保障全部生成consumer质量', 23, '已有覆盖',
 '精确v1 §3及R19：VFM多层feature经可训投影为Gaussian latent，decoder分scale注style/spatial并ToRGB监督，多loss/对抗训练仍有费。VFM冻结不等codec不训/无信息损，干净CKNNA不预测所有生成；teacher/codec配置与latent压缩混杂，重构和语义proxy不独授下游生成更好。',
 '实际连续codec/PAE与三consumer段已有冻结prior补细节、扰动decoded一致性仅proxy、重构/语义/生成分别验收，保本稿局部新验证，不为新tokenizer名重写。'),
('18476', '有限hypothesis的entropy是模型内集中度，不是真实人心校准', 82, '已有覆盖',
 '精确v1 §3.2–5：3–5意图假设/GPT4o likelihood更新belief，entropy转confidence后选择澄清/追目标。Qwen2.5-7B policy与partner/judge/IM/LHM共享GPT4o，90/14场景未披具体多seed次数；oracle固定轨迹而本法探索更多，超过oracle不证明真实intent信息上界。全部额外模型/历史费计入，不把无参数更新写成免费或一般ToM真实性。',
 'Behavioral belief不等authenticated identity已把有限history预测、身份和外部规则分开，latent标签不认证真实多意图，具体覆盖成立。'),
('18477', 'LLM DAG去冗余不接管加密/DP executor或语义与隐私验收', 81, '已有覆盖',
 '精确v1 III/IV：已知FA skeleton到粗细prompt DAG跨subquery复用，encryption/DP在backend；uniform schema/每client一记录、semi-honest假设不因LLM自动保持。GPT4/T0、20合成query/两schema、operation count非加密吞吐/网络或privacy budget组合，少DP节点可能改相关性；无optimizer完成率仍100%，不能说其提高完成。',
 'Plan-execute实际段已有cache/dependency-aware优化不得跳precondition/effect或误批并发，故只作受限实例，不新增隐私机制或安全保证。'),
('18480', 'batch/长度/总求值可改变DLM比较，后续撤回史须按版本隔离', 24, '已有覆盖',
 '精确v1 §3/4.2/5/6由R6实际核：单A80080/FP16/同SDPA，GSM8K100例0/5shot，强制输出64–2048、batch1–64；跨checkpoint非同质量Pareto，固定EOS后继续非自然有效token/SLO。大batch反转不是所有DLM永慢，roofline非kernel profile。R25核v2撤回以重划相关工作/原创、v3恢复；v1只提示newer version withdrawn，未宣布全部v1实验失效。v2不入选/评分，v3不倒填本日；5分仅受限实验反侧，不给成熟roofline/batch原则原创分。',
 'Parallel Progress与Active Compute两连续段已分低QPS token并行、高QPS跨request参数摊销和总K/质量运行点；R16实际覆盖，未因后版行政改书。'),
('18483', 'GUI观察支持、动作接口与指导人口共同变化，asking效果不能混成纯能力', 66, '已有覆盖',
 '精确v1 §4/5/7：DC原图/pixel-key与TA的YOLO约400标注/task、OCR及语义bbox共同变化；ask只episode前一次，hint每turn注入，非中途多次主动搜寻。RTX4070Ti/1920×1080/0.5s延迟、八trial、10invalid终止，0DC不证理论不能玩；asking自选/跨trial历史非纯因果，标注、视觉、输入/模型全计费。',
 'R20实际Ch66观察support/动作执行/指导信息的分责已承载局部采用，不把新benchmark场景改写成普遍agent能力量尺。'),
('18488', 'benchmark修复改变接受域与人口，强模型共同失败只给审查线索', 66, '已有覆盖',
 '精确v1 §2.1/3：point→bbox改变接受域，强模型全失败是heuristic，LLM改label加随机人审不证全量错标。GA“均bbox”与ablation原point口径冲突不合并；3B/2400 curated与旧31k训练不同，不能独归质量胜数量。bbox包含非真实effect，任务修改/难度人口及数据审查费用保留，不授生产通过。',
 'R20实际Ch66已分支持域、候选错误筛查与真实任务/effect；局部修复验证不需再造同主题书稿。'),
('18491', '搜索器/归一化/预算定义的potential不能当算法内在可调性标量', 66, '仅报告',
 '精确v1 §3/4/5：逻辑改写+Bayes调参量尺依probe/normalization/权重/当前搜索器与预算。Claude3.7、Bayes0/10/20及reflection1/2/3，ABR/调度/CartPole；纯LLM约60%情景无显著收益、加Bayes仍约20%，state与搜索预算不同不支持简单算法永更可调。局部WiFi/Dashjs不是生产验收，不能改黑盒内部逻辑。',
 'R32实际Observed Capability/Elicitation Ceiling已分自然行为、给定监督预算最好行为与识别上限；有限实现未形成新普适量尺，保局部评价但不为场景流程改书。'),
('18525', '共享父权重bits可省副本，但BF16近似与KV/acceptance另须证明', 49, '已有覆盖',
 '精确v1 III–V由R10实际核：FP16指数重映与per-tensor scale不自动逐bit恢复原模型，BF16小指数round近似；同部分weight bits不证draft/target hidden/KV一致，缺修复/rollback及完整exact rejection，不能借一般投机定理补recipe。28nm/500MHz综合与功耗模拟非流片/GPU服务，五模型×三任务非15模型，batch/SLO Not Disclosed；decoder/scale/控制费不免费。',
 '实际Ch49父表示/各档kernel质量与FPGA dataflow已分责，target acceptance仍Ch48。只采表示/硬件消费方案，不授lossless或2.07x部署保证。'),
('18541', '完整trigger缺席不等组成token无监督，KD不自动清除teacher风险', 72, '整合',
 '精确v1 §4.2及R13 §4.1/5/限制：前提是可植入teacher并预期下游域/语言重叠，完整组合少见但组成token可自然出现。Llama8B→3B同词表主配与另几family只界定所测边界；ASR有trigger/FTR无trigger分验，三个普通任务非完整隐蔽性认证，防御未研究。未实施毒化/提供payload，不称任何蒸馏必传或KD消毒。',
 '在量化后门原段/marker后新增完整与组成监督两粒度，保teacher/数据人口、学生能力及全费；不改可组合Prompt后邻接或授通用防御。'),
('18544', '周期decode quota不保证最大token gap，优先级收益须按人口验收', 56, '已有覆盖',
 '精确v1 IV/Alg1–3/V：utility×TPOT选择与1s cycle decode-mask是平均quota，不证相邻token间隔上界。TTFT不等号/Alg3索引与ceil-floor未闭，不抄硬SLO recipe；高优先获益牺牲non-real-time，高load仍低。ChatGLM2-6B/4060Ti16GB、TPOT100/120/250ms、0.1–7到达/7:3比例，precision/engine版本/完整输出和区间 Not Disclosed，不采35x全类保证。',
 'SLO-aware Admission与Iteration Scheduling实际已有累计期限/逐token间隔及quota-debt/墙时等待分开，局部新反侧不需重复算法段。'),
('18563', 'gate严格度与冗余同时变化，跨策略方差不证明信任的因果方向', 72, '已有覆盖',
 '精确v1 III/IV/VI-B由R13核：tau同时改MNI gate与输出冗余，OER依任务MNI+rule/classifier，误差未闭。AD为跨三个tau加权方差而非斜率，不能证明单调或“信任必降安全”。19合成场景/1488链、无network/tools/跨run memory，API版本/多seed未披；telemetry因果验证仍未来，只保暴露/策略敏感度分账。',
 'R20实际Ch72已把任务必要aggregate、敏感集合、接收权限与输出暴露分开，具体覆盖而非凭security主题；不授跨framework安全排名。'),
('18583', '跨模态cross-covariance与各边缘支持统计不能互代', 27, '整合',
 '精确v1 §3/4：冻结encoder局部线性contrastive内层化cross-covariance，实际Frobenius替unbounded trace并加边缘feature/online encoder更新。局部条件不自动等真实InfoNCE全局最优，未读完整C不采强保证。Flickr30k/COCO、NFNet/BERT，旧基线冻结text而本法可训，收益不独归单loss；real特征、合成与online维护/下游训练全计费。',
 '实际joint geometry/分边缘目标未显式承载配对cross-covariance双约束，故在其限制段/原binding后新增，保非逐pair/高阶完备与坐标随encoder变。'),
('18586', '工具停等KV按生命周期迁移，空间预留与关键路径分配另验收', 56, '整合',
 '精确v1 §3–7/Alg1–2：DAG事件/估时与EWMA预测空隙，覆盖双向传输才offload，预取前分轮预留，copy完成才释放源GPU块。priority公式/配额clamp未闭，不授公平/最优SLO recipe。Qwen14B/A10080与32B/H200140、CPU swap100GB/Poisson，工具调用及持续时间因模型不稳定而模拟，非真实工具分布；block利用率非kernel利用率，全部迁移/allocator/预留费计，不采47%/16.9普适。',
 '在停等资源段后新增未共享KV的copy完成/释放、预测回迁及reserved/shared空间consumer，R24→W12→R27实际POST通过；不把预测当deadline保证。'),
('18596', 'reward precision/NPV提高可以付出abstain coverage，step与终态分开', 66, '已有覆盖',
 '精确v1 §2/3/4/5：272轨迹/346关键step人工标注，排无成功/8+成功和>25步，成功轨迹仍可有bad step。UPE全正/全负同意否则abstain，precision/NPV改善付coverage/采样费，未在真实RL loop验证。specialist32B低于base也混prompt/严格度，截图可能不显示file size；标签/模拟概率非真实effect或因果。',
 'R20实际Ch66过程/终态、选择性coverage与独立effect/script验收已承载采用范围，不为reward benchmark新增重复论证。'),
('18638', '受限LSA重参数化与优化可达性分开；固定结构hardness归约存争议', 14, '暂缓',
 '精确v1 §2.3–4及C.4/C.14由R14核：无softmax单head、二状态Markov/固定p/infinite prompt，扩展X凸最优不等原(b,A)可达或SGD可解，更深实验可变坏。中心NP-hard归约自加任意D(r)/冻结变量/不等式，未证仍在Eq8固定对称乘积映射且hard实例来自该population最优X，广义bilinear hard不推出结构子类hard。5分与合法工程域保留，强定理不作正面。',
 'Ch14受限ICL/kernel/TD构造已分全局minimum与训练可达；不声称已有该全部实现。Books只暂缓争议强命题，需合法结构保留归约才重开，不把普通未读改H。'),
('18680', 'Gaussian NLL工程代理与真实conditional MI不同，连续entropy界有尺度反例', 29, '暂缓',
 '精确v1 §3/4.1/A.1由R14核：多teacher Gaussian conditional kernel/NLL平均不等学到真实MI。T~Uniform[0,.1]、S常数、Y=1[T>.05]时teacher无误/student错半，h(T|S)=ln(.1)，所写1-exp(-h)=-9不能上界.5；缩放embedding改变NLL而不改Bayes分类。有限文本工程域保留，不扩Science应用，不授任意连续任务理论保证。',
 'Ch29表示MSE/行为及Visual Information Gain/CIG已有代理likelihood非客观MI边界；强bound暂缓、不进Books正面，需离散/连续测度假设与尺度有效界澄清才重开。'),
('18716', 'spatial/semantic head分预算与刷新需保持原位置和质量，不授无损KV', 45, '已有覆盖',
 '精确v1 §3/4：按窗口外mass分类local/window-sink与semantic heavy-hitter/recent，CFG KV-MSE差为相关线索非语义因果。Janus1/7B、24²grid/384²、CFG5、A10080/batch至256、GenEval553/DPG1065；大batch吞吐非单请求SLO，峰值memory非全参数免费。head阈值/网格变化须重测，追踪/刷新计费，丢KV不保target分布。',
 '实际Ch45跨层角色/head-aware/KVCompose已区分head、原位置、索引刷新与未来有效性，局部图像验证不需重写机制或把layout授identity保证。'),
('18725', '句级伪domain与centroid adapter路由是代理，分域不必普遍更好', 30, '已有覆盖',
 '精确v1 §4–6：bartMNLI句级伪标→r16 domain LoRA，embedding centroid cosine路由。general/wiki-news全域baseline更强，标签/数据/容量共同变化；NLLB600M/两A10080、英→爱尔兰语高质量数据，未测webcrawl/反向/其他任务或全部时延。伪标/centroid/路由维护全计，不授域越细越优或普遍胜fullFT。',
 '实际输入相关adapter库及MCIT/ProtoAda已分伪domain/prototype、选择、encoder统计人口及行为验收，冻结centroid不冻结竞争；保局部替代，不重复改书。'),
('18744', '继承buffer上的预测/生成扩展给延迟质量取舍，hop一次不等frame一次', 24, '已有覆盖',
 '精确v1 III-B/IV/VI/VII：buffer机制明确继承[1]，本次仅新Data Prediction/生成扩展。不同年龄frame不同noise，每hop一次NN但frame累计多步；DSM固定(B−1)与DP可调d延迟分开。16k/STFT510/hop256/K128、EARS+WHAMv2/A100训练，原DB匹配条件可更差，DP/g32加参数且d0逊SEMamba；时延公式疑点与未读BC-UNet不授lookahead保证。',
 '实际wavefront/统一成本模型已分暂定latent交错、每对象总求值/驻留与级联，局部音频延迟质量反侧具体覆盖；不称首次buffer发明或无等待。'),
('18795', 'LLM embedding到CLIP两阶段兼容仍需各consumer回归，不等旧能力无损', 23, '已有覆盖',
 '精确v1 §3及R19：离线LLM embedding经MLP投原CLIP text空间，以instance/pair-distance继承，再InfoNCE调vision/projection并EMA regularize。非在线训练全部LLM或数值空间恒等；分类/检索取舍保留，62.5vs74.5不能叫无损旧知识，text提取/EMA/双loss与producer-consumer版本维护全费。',
 '实际连续图文encoder兼容/对齐段已有旧软关系teacher、scale职责及各consumer验收；新两阶段为局部替代，不再造普适无损recipe。'),
('18798', 'gold反馈反思是训练特权，不能给线上开放搜索自证权限', 33, '已有覆盖',
 '精确v1 §2/3：rejection保groundtruth一致反馈/成功trace，RL answer_submit后可获gold F1再继续，按次数折扣/长度惩罚。训练Wiki限域而推理live Google/Jina，九集各512+Bamboogle125/LLM judge，12prompt×8trajectory/至30turn/100step/60A800h；小模型重复坏JSON、预算/工具人口限制归因。自家reader摘要非原网页，全部搜索/采样/判分计费，不反投current数字。',
 'Ch33实际ChatR1参照改写段已有human/teacher训练参照不取得部署真实意图/faithfulness权限；本次新验证可用，不授线上oracle或重复书稿。'),
('18810', '守恒、函数等价不变性与指定干预faithfulness是三项独立义务', 5, '整合',
 '精确v1 §3.1–3.2/4.1由R14实际算术核：f=x1x2x3两括号等分relevance为(6,6,12)/(12,6,6)，总24而zero-LOO=(24,24,24)。只反驳该rule三义务互推，不一刀切所有LRP；真实softmax不能任意重括号，CP-LRP同时改softmax/bilinear split不能独归一个因果。BERT/MNIST的zero/mask LOO也非人类语义真值，解释与干预成本计入。',
 '现relevance patching只说守恒非faithfulness，新增函数等价与zero-LOO的可复算区别，接在完整旧段/marker后，保Jacobian lens后邻接。'),
('18821', 'RAG可答资格与solver失败难度分账，文档一致不等开放问题唯一真值', 27, '已有覆盖',
 '精确v1 §3/4.1/4.4/E：同policy proposer/solver，预置答案集经文档RAG solver/LLM judge过滤，再各自训练；不是无任何监督。E5/Wiki2018 top3、七QA各500/Bamboogle125/Qwen32B judge、prompt4096/output8192，Temptations非唯一例直接反驳可答即唯一。噪声doc4优于7仅消融，judge/题池/双角色rollout/RAG全费，不授任意现实正确。',
 '实际Policy-relative Sweet Spot与Verifier-backed Synthetic Curriculum双重权威已分来源资格、可解性、当前难度/solver和独立verifier；保局部资格机制，不重复改书。'),
('18825', '跨层virtual可达不等dense单层函数，理论/密度阈值须绑结构条件', 14, '已有覆盖',
 '精确v1 §3/4/A.1–A.3由R14核：uniform prior/正交prototype/各向同性Gaussian/给定class权重等限制，不能直接授feature-dependent softmax。cluster虚节点两层可达不证任意dense数值函数等价；全部expert加权非Top-k稀疏算力。1/(3dh)是实现空间常数非普适wall-time分界，partition/index全计，不外推LLM serving或test-label oracle。',
 '实际跨层补全可达与block-skip执行段已分感受野、内容路由和数值/硬件成本，采用局部mask/执行思路，不搬受限定理为通用LLM保证。'),
]

class Title(HTMLParser):
    def __init__(self):
        super().__init__()
        self.active = False
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.active = True

    def handle_endtag(self, tag):
        if tag == 'title':
            self.active = False

    def handle_data(self, data):
        if self.active:
            self.parts.append(data)


def title(short):
    fixes = {
        '18091': 'Accelerating Vision Transformers with Adaptive Patch Sizes',
        '18113': 'Investigating the Impact of Dark Patterns on LLM-Based Web Agents',
        '18121': 'Efficient Long-context Language Model Training by Core Attention Disaggregation',
        '18179': 'Adaptive Coopetition: Leveraging Coarse Verifier Signals for Resilient Multi-Agent LLM Reasoning',
        '18476': 'Probabilistic Modeling of Intentions in Socially Intelligent LLM Agents',
        '18480': 'How Efficient Are Diffusion Language Models? A Critical Examination of Efficiency Evaluation Practices',
        '18525': 'From Quarter to All: Accelerating Speculative LLM Decoding via Floating-Point Exponent Remapping and Parameter Sharing',
    }
    if short in fixes:
        return fixes[short]
    parser = Title()
    parser.feed((ROOT / f'REPAIR_2510.{short}v1_20261029.html').read_text())
    return ' '.join(''.join(parser.parts).split())


def render():
    old = REPORT.read_text()
    baseline = (ROOT / 'baseline-before-repair-20261029.md').read_text()
    # The baseline also contains the already-valid Seed3D extension; preserve it intact.
    old_evidence = old.split('## 4. 证据与知识整合\n\n', 1)[1].split('\n## 5.', 1)[0]
    assert len(re.findall(r'^### \[', old_evidence, re.M)) == 1, 'One-time reconciliation already applied; edit the report in place.'
    original_block = '\n\n'.join(old_evidence.split('\n\n')[:2])
    assert len(original_block) == 217
    assert original_block in baseline
    seed_row = next(line for line in baseline.splitlines() if line.startswith('| [Seed3D'))
    assert seed_row in old
    source_table = old.split('| 来源 | 检查范围与依据 | 结果 | 缺口 |', 1)[1].split('\n\n按需', 1)[0]
    rows = source_table.splitlines()
    rows = [line for line in rows if not line.startswith('| SRC-ARXIV |')]
    rows.append('| SRC-ARXIV | 旧四窄主题35题摘及五Submitted主题67出现/63唯一/新增57题摘按本日有效层复用；本轮同主题registered自然日五查询24/47/31/3/0，各page1/totalPages1/无next，105出现/103唯一，与旧93交AdCo1；全部题名导航，含糊项全AB，按具体潜力读必要域 | 已检查 | 此为有限主题发现而非全学科召回；旧五错误client字段0不授覆盖。精确v1联合界与当前事件说明另核，七跨日资格保留，不以created或Submitted定日 |')
    rows.append('| SRC-OPENREVIEW | Topoformer同题同作者早稿信号触发项目/作者出版页及具名Paper/forum，API2一次403，止该身份恢复 | 受阻 | 作者出版页May10,2024足以排本次first事件，历史全文未取得，不授2025逐字无修订；无具名重要差额，不扩会议全站 |')
    header = old.split('## 1.', 1)[0]
    header = re.sub(r'\*\*检查时间：\*\* .*', '**检查时间：** 2026-10-29T16:06:03+08:00', header)
    intro = '''## 1. 结论

本次仅补BJT 2025-10-22。保留旧Seed3D整行/日期/5分、原小时窗和连续旧§4，不借其他日报候选。旧35题摘局部纠正后32P3C、Submitted发现新增57题摘44P13C及MiMo一项按本日有效层复用；旧93身份的v1日门已逐项恢复：77同日界中仅AdCo落本窗、另76窗外，16跨日界也均可排本窗（9最早界晚于目标、7最晚界早于目标）。因此撤销旧“76全体日期H”；此结论仅v1公告，不抹机构介绍、artifact或具名重要revision。

旧Submitted切片不完整，本轮补同主题registered自然日差额：五个有效查询105出现/103唯一，与旧93仅交AdCo，102新导航身份，不是102当窗论文。标题先限定范围、含糊项全AB，原53P加四C最小重开为57潜力；七项联合界跨目标、Topoformer具体早稿、Food4All精确v1普通应用各自剥离后，**48个新增正式家族，加原Seed3D共49**。撤回18515/18551不入选/不评分；不把导航列表变全量Methods配额。查询/分页/停止与逐项理由见[SCREEN](../_sources/daily-20251023/REPAIR_SCREEN_20261029.md)和[本日canonical](../_sources/daily-20251023/REPAIR_20261029.md)。

49家族采用命题所需证据已按支持/关键直接反侧互斥读足，均保局部配置与反证，未核代码、复现实验、部署或生产能力。Books处置为18整合（原Seed3D1及本轮新增17）、28具体已有覆盖、Crucible1仅报告、LSA/多teacher MI两强子命题争议暂缓。新增17均为实际长期差额，不因模型名/章节数增分；已有覆盖由实际正文论证校准，非主题映射。最新十四处真实SAVE/全自读已由R33磁盘actualPOST通过并释放窄位；此稿仍进行中，日级DAY/完成SAVE/FINAL尚未发生。

主要变化是输入patch/latent/动作hidden等消费接口、工具停等KV/无参数core-attention的状态与调度分责，以及工具集合reward、在线demo pool、策略库/安全slice等证据生产与消费边界。两理论子争议不作正面定理，七跨日资格及机构历史缺段不授Coverage/Evidence/Books或“无遗漏”；DLM后续撤回/恢复按精确版本披露，不把v2撤回外推成v1实验全失效，也不倒填v3原创声明。

## 2. 来源覆盖

十四每日源只复用本日实际原件与停止层，不重抓全机构历史。入口/原始请求见[FETCH](../_sources/daily-20251023/FETCH.json)、[恢复请求](../_sources/daily-20251023/RECOVERY_FETCH.json)、[原筛选](../_sources/daily-20251023/SCREENING.md)、[Source](../_sources/daily-20251023/SUP_SOURCES_20261015.md)、[旧窄arxiv](../_sources/daily-20251023/SUP_ARXIV_20261015.md)。本轮registered五份VALID原件、KNOWN_COMPLETE、POTENTIAL_FULL三小批和REOPENED_FULL保实际字段与身份；错误client字段五个0及80s全字段请求失败保真，但不授发现完成。修正正控出现AdCo；sparse发现不替完整client关系/唯一v1日门。

Hunyuan仅本日本身中文All原件，zh/page1/size200/renderType0实际code0、total11/list11、11个lang均zh；R2完整核三发布时间字段。它涵盖当前中文列表，不是EN9/default，也不因已知size100模板重复请求；全2026不能证明2025零事件。按需仅已有候选必要原文与Topoformer身份触发OpenReview，不扫描每周来源/会议全站。

| 来源 | 检查范围与依据 | 结果 | 缺口 |'''
    date = '''

新增48行的公开日期均仅指**精确arxiv v1公告**：适用2025官方ET截止/公告与公告前不分配最终ID规则给最早界，精确DOI/唯一v1、DataCite `arxiv.content`、findable及`registered`给最晚界，整个无冲突区间均落BJT22才准入。`created`仅记录创建，不是登记或公开日；Submitted/ID月份/后版日期均不独断。原字段/算术见[KNOWN bounds](../_sources/daily-20251023/REPAIR_KNOWN_BOUNDS_20261029.json)、[POTENTIAL bounds](../_sources/daily-20251023/REPAIR_POTENTIAL_BOUNDS_20261029.json)、[REOPENED bounds](../_sources/daily-20251023/REPAIR_REOPENED_BOUNDS_20261029.json)，适用[2025官方原件](../_sources/daily-20251023/READER_ARXIV_AVAILABILITY_20250106.md)及[DataCite定义](https://support.datacite.org/docs/what-is-the-difference-between-the-created-and-registered-date-in-the-datacite-rest-api)。联合界不证明全球first或历史逐字内容；已知早稿/撤回信号另核，不无限排所有假想渠道。

Seed3D旧行仅官方PAPER目录Oct22研究介绍事件，BLOG另Oct23、arxiv v1后到，原5分不改。新48精确v1与全部当前官方事件页的comments/history已实际轻查；普通版本号/会议标签不自动证明重要差额。撤回18515实验失效、18551被旧论文supersede、Topo早稿及Food4All v1/current差额均有具名处置。所有未披露的完整engine版本、precision、分布/并发/SLO/置信区间保持Not Disclosed，不以缺字段补造成全局比较。
'''
    table = ['## 3. 候选与判断', '', '| 材料 | 公开时间 | 项目贡献与评分 | 审阅结果 | Books决定 |', '| --- | --- | --- | --- | --- |', seed_row]
    evidence = []
    score6 = {'18085', '18121', '18135', '18313', '18525', '18586', '18821'}
    for short, contribution, chapter, decision, proof, comparison in ENTRIES:
        label = title(short)
        url = f'https://arxiv.org/html/2510.{short}v1'
        node, path = OWNERS[chapter]
        link = f'[Ch{chapter}]({BOOKS}{path})'
        score = '2 + 2 + 2 = 6' if short in score6 else '2 + 1 + 2 = 5'
        depth = '争议' if decision == '暂缓' else ('深入完成' if decision == '整合' or short in {'18113','18131','18525','18563','18480','18810','18825'} else '标准完成')
        book = f'{decision}：`{node}`，{link}'
        if decision == '暂缓':
            book += '；仅强子命题见§5'
        elif decision == '仅报告':
            book += '；量尺受搜索器/预算限定，未形成新长期机制'
        table.append(f'| [{label}]({url}) | 2025-10-22 | {contribution}；{score} | {depth} | {book} |')
        evidence.extend([f'### [{label}]({url})', '', proof, '', f'**Books：{decision}。** {comparison} 唯一归属`{node}`，具体正文见{link}。', ''])
    assert len(ENTRIES) == len({e[0] for e in ENTRIES}) == 48
    tail = '''## 5. 缺口与下一步

普通可执行项：整日六节DAY、writer真实完成SAVE/全稿自读QA及sole reader actualFINAL。研究/owner与必要Books实际POST均已补足，不因一批结束称本日完成；后续只按实际到达反馈修正，不重有效必要层。

本窗已隔离的**七项日期资格**（不进确定候选/评分/Books）：[17917 unlearning](https://arxiv.org/abs/2510.17917v1)、[17925 SpecAgent](https://arxiv.org/abs/2510.17925v1)、[17853 CiteGuard](https://arxiv.org/abs/2510.17853v1)、[17862 FCV](https://arxiv.org/abs/2510.17862v1)、[17858 shortcut flow](https://arxiv.org/abs/2510.17858v1)、[17845 MATagent](https://arxiv.org/abs/2510.17845v1)、[17919 ParaVul](https://arxiv.org/abs/2510.17919v1)。最早公告界分别BJT21/21/16/16/16/14/21，registered最晚界均BJT22，整个区间未落同一天，不能截取22或用created代替。R17/R21已按具名ID/题名有限查询、官方abs/current及作者项目入口恢复，未得更窄原始公告；当前外部资格不足，不因日期H抹FCV已读安全反侧或ParaVul机制。重开只需对应官方公开批次/明确日期的原始公告或无冲突更窄界，不要秒级证明，不发无限泛检索。

**两项强子命题争议**：[18638 LSA](https://arxiv.org/html/2510.18638v1)需证明Eq8固定映射/Markov population约束内合法hard归约；[18680 多teacher](https://arxiv.org/html/2510.18680v1)需澄清离散/连续测度、尺度与有效Bayes界。R14反例及R32实际owner比较已读足，保重参数化/工程代理的有限事实，不把争议强定理用于正面Books或能力保证；这不是普通研究未做，取得作者合法修正才重开对应依赖，不重全部Methods。

来源历史外部缺段按§2隔离：OpenAI Research、Google pubs/DM、Meta、Qwen历史/冲突字段、Moonshot组织/目标历史、Hunyuan2025、Zai历史、MiMo Blog/current事件、MiniMax独立Agent历史。需要相应当时目录/原文或官方事件日期才定点重开。旧93 v1分层已解除旧76整池H；PathFormer current v1/Advanced日期冲突、JaiLIP/SEC/RADAR/MiMo具体后版提交字段按旧原件保留，但版本号不证明重要修订，亦不授同family所有artifact/revision窗外或零事件，不新造全family逐版全文队列。

Topoformer同题同作者出版页明示May10,2024，足以排本次first；OpenReview历史全文未得，不声称2025逐字无差额，没有具名重要差额不继续双全文。Food4All精确v1由R20读§3/5后仅成熟应用组合C，不以后版诊断机制倒填；18515/18551官方撤回是排除而非访问H。上述保留项不支持正面Coverage/Evidence/Books、“无遗漏”或性能/安全保证；未来材料只重开受影响家族/真实日期，不创建其他日报。旧CURRENT_STOP/旧独核保历史角色，不继承其秒级要求或旧完成声明。

## 6. 复核

复核者：Chandrasekhar `01a1863b-2866-7d12-82f0-3935bd387acb`，非writer Locke。

结论：未通过（完整日级DAY/完成SAVE后actualFINAL尚待实际发生；非研究失败或外部H）。

[本日sole reader独核](../_sources/daily-20251023/REPAIR_REVIEW_20261029.md)R1–R33为已成分批层：R2适用2025规则/本日中文All；R3–R7正控纠错/有限发现/首六日门准入；R9旧93原件逐项独立重算零差异；R11八C全AB中四具体重开、其余18C未称逐篇独核；R12–R14安全/撤回/早稿与四理论关键直接反侧；R17/R21七跨界有限恢复；R19五生成关键反侧；R20九owner和Food v1改判；R22其余潜力全AB校准及C范围分层，不把这些校准冒充全部Methods二读。R23接合writer实际补足域，R25处理DLM撤回/恢复。未改变的旧六v1/十二必要反侧与Seed实际链复用，不借其他日期候选。

Books完整PRE/实际保存链：AdCo R15→W7→R18 actualPOST，TokenCake/CAD R24→W12→R27 actualPOST；B四/R2BC修订/C五/D四分别R26/R28/R30/R31完整PRE→W15真实SAVE/完整新增与两完整邻接/本人注自读→R33全部十四份磁盘actualPOST通过，全部窄位已释放。R16/R20/R29/R32实际正文已校准28具体已有覆盖、Crucible仅报告与两理论子争议。所有授权只到各单段/独立marker/本人注，不锁全章或root第三批准，不重存已完成段。

writer当前六节稿待V3、引用、冻结及限定diff检查，再交整日DAY；机器只查格式/可判定一致性，不代语义复核。共享main的并发dirty/staged保护，不改State/共享索引，不stage/unstage/commit/push，不声称全仓clean。历史root独核仅旧层有效，不能代本轮sole reader日级验收。
'''
    common = '''
下列新增48项的精确证据位置、模型/负载/硬件、未披露字段、作者结果/本人的推断及未采用主张，详见[实际必要证据](../_sources/daily-20251023/REPAIR_EVIDENCE_20261029.md)与[sole reader关键反侧](../_sources/daily-20251023/REPAIR_REVIEW_20261029.md)。正文已有覆盖的逐项实际论证见[Books比较](../_sources/daily-20251023/REPAIR_BOOKS_20261029.md)，后到R29/R32校准优先于该过程稿旧“待比较”文字。支持/直接反侧合用到拟采用命题即停，下载不等阅读，作者结果不等复现。整合项完整稿/邻接/本人注见本日PRE文件，采用状态以实际POST为准。

'''
    new = header + intro + '\n'.join(rows) + '\n\n' + '\n'.join(table) + date + '\n## 4. 证据与知识整合\n\n' + old_evidence + '\n' + common + '\n'.join(evidence) + '\n' + tail
    assert seed_row in new and original_block in new
    assert old.split('**窗口：** ', 1)[1].splitlines()[0] == new.split('**窗口：** ', 1)[1].splitlines()[0]
    print('*** Begin Patch\n*** Update File: ' + str(REPORT))
    print('@@')
    for line in old.splitlines():
        print('-' + line)
    for line in new.splitlines():
        print('+' + line)
    print('*** End Patch')


if __name__ == '__main__':
    render()
