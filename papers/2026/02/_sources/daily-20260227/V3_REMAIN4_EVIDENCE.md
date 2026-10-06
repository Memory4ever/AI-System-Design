# 四项有限证据后的具体已有覆盖比较

四项必要原源/关键反侧及实际owner承载段已root非作者实际核验，21950/21811/21697/21595均具体Existing通过，无Books写入。均未运行artifact/复现实验；不因finite/in-domain本身改EX、不因没有论文名增Books段。下列保留写前比较，不再待PRE。

## 21950 MEDSYN: Benchmarking Multi-EviDence SYNthesis in Complex Clinical Cases for Multimodal Large Language Models（原风险EX改IN）— 2+2+2=6

[exact-v1](https://arxiv.org/html/2602.21950v1)，V3_BLOCKS_2602.21950.md blocks27–34/52–60/Table4。英语FDx多选同题，RemoveText三模型+.50～7.04pp，length-matchedRandomText+.75～4.78pp，支持“更多连贯文本可干扰该视觉证据选择”；random控制tokenbudget，不证明attention变化为causal解释。DDx生成覆盖率/GPT5judge0–5与FDx多选accuracy不是同一任务/人口，不把两个分数差授统一calibration。专家摘要与rawimage不同信息预算、每种CE给text或visual而非同时，文本摘要更强不证明同信息跨modal差额或全视觉不足。模型7B有限、并未全部matched更大骨干，medical部署结论不采用；hardware/precision/seed/全部token与费用NotDisclosed，图文两条接口不独立truth。

拟Existing MULTIMODAL-REPRESENTATION Ch23 actual107（完整99–115）已用semantically matchedinput与text-only/swap诊断将稳定、实际模态依赖和accuracy分开；actual564–582另将task contribution与sample-specific reliability分责、污染模态拖累与static/late/single fallback分开。该Remove/Random结果是这项已写判断的具体负面验证，不新增新的融合或authority接口。报告保真实controlled比较和RAPT非因果，不按医学暂缓EX、不为新benchmark造差额。

## 21811 DexRepNet++: Learning Dexterous Robotic Manipulation with Geometric and Spatial Hand-Object Representations — 2+1+2=5

[exact-v1](https://arxiv.org/html/2602.21811v1)，blocks51–71/147–153/196–219。Localcontact Surf最近点距离/normal与掌心Occ、22jointPointNet局部patch共同输入；global pGlo为预训PointNet整体shape。Samepolicy BC150epoch/DAPG600iter、10seeds，较高variance variants20runs；40trainobjects，ablation是10GRABunseen+30 3DNet，不冒充全部5355unseen同ablation分母。RTX3090约42GPUh，100evaltraj/object，objectlift30±5cm不是通用接触安全。

实际215 Occ+Surf加pGlo比不加下降约20%unseen、DexRep+pGlo也弱于DexRep；支持该population/encoder的额外globalfeature干扰，不证明全部globalrepresentation有害或local唯一causal。Global与local encoder/pretrain/容量未全面matched，extraencoder/residency/training costs不等免费；longerruns是否追回作者217承认未知。tSNE相近不认证语义因果，CI不重叠不是一般化p-value规则。

拟Existing MULTIMODAL-REPRESENTATION Ch23 actual95–101（多层summary/readout的完整因果链）：更大summary/aggregation需额外缓存、容量/预算，pooling可丢局部定位；细空间任务保patch-level接口，不同任务/预算选择producer与consumer，matchedbudget再验。该localcontact任务明确验证“全局aggregation不能代理task-relevant local cues”的已有表示责任，不给Ch26另写模型recipe；Ch26 actual17–25/37已有contact/geometry/controller与physicaltruth分权，有限feature反侧不授权安全。

## 21697 EditFlow: Benchmarking and Optimizing Code Edit Recommendation Systems via Reconstruction of Developer Flows — 2+2+2=6

[exact-v1](https://arxiv.org/html/2602.21697v1)，blocks76/83–97/120/158–176/210。评测Keep由任意已完成prefix的graph successor定义，但实现只与last h_n作≺/∼筛选；root/作者据该接口作条件性推断：若合法依赖h_(n−2)而与h_n无关，候选会被错拒，这不是作者承认的实测case。图one-hop也不是完备所有topologicallegal下一步。Break以不在最终commit的hunk定义，不能把等功能替代edit判真实错误；commit参考与开发者认知、可执行性分别验收。Digitaltwin大量graph为同模型自动infer，25人注图支持有限反侧而非真实humantrajectory/cognitiveflow truth。作者跨protocol平均recall−7.09%不套给每人口；人注Table6三模型recall分别45.95→45.41、38.92→36.76、15.68→14.05，均反退。增1.71s/6.58ktokens/$.03是作者总体perquery平均，非每配置固定费用，不证明2s所有人不可感或长期工作效率。

拟Existing PLATFORM-EVALUATION-SYSTEM Ch66 actual419–436：真实过程trace/affordance/effect receipt与finaloutcome分开；开放合法替代路径存在verifier false reject，scorer接受集合与state-transition合法集合需同时冻结，proxy不达标不等任务失败。该flowlabel的两个acceptanceset冲突是既有oracle审计原则的具体例证，不增加新通用controller。AGENT-PLANNING Ch79 actual201–203已有历史precedence只作候选prior、局部边不能保全局依赖/executor合法，未把ranking代功能授权。报告保last-only错拒/commit参考限制，不为新flow术语整合段。

## 21595 SPOC: Safety-aware planning under partial observability and physical constraints — 2+1+2=5

[exact-v1](https://arxiv.org/html/2602.21595v1)，blocks15–22/29/31为root/作者必要core已核。AI2THOR单臂13actions，FO全scene vsPO只能nav到已观察/必须find；holdingobject前提影响交互，pour必须持source。25hazard+5nonhazard×5设置，GC按online动作/状态/短后续3step检查，CSR任意违规0与GSRsubgoal分开，联合要求两者100；explicit/implicit提示的信息不同不能归纯reasoning，sampledguard不覆盖真实连续物理safety。Gpt5mini3runs的FO/PO/IPC有限比较支持环境可观测/约束验收差异，未披露完整wallclock/APIbudget/precision，不采用普遍防护。

拟Existing PLATFORM-EVALUATION-SYSTEM Ch66 actual419–436的process-compliance/finaloutcome分账、原始environmentreceipt、scorer接受集与alternate-path false reject，及actual684（完整682–687）goal存在量词vsprocess每时点量词已具体覆盖本项评价盲区。AGENT-PLANNING Ch79 actual49–61已分不可得/可查询未查询/已实际context三种信息状态；Ch26actual1344持续automaton与1430precondition placement不代physicaltruth。SPOC不是只加hazard菜单，保潜力准入与有限负面证据；当前完整评价/观测边界已有覆盖，不制造Books段。
