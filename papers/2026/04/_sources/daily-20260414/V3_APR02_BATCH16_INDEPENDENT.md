# Apr14 第十六批四项有限非作者核验

复核者apr02，非本日作者/书稿写者。实际重读当前AGENTS、Research/Report合同与统一Prompt；仅以下四项必要官方v1、拟采用命题及相关当前正文，不扩附件、发表史、日期全日Gate或宽库存。没有写Books/作者README，没有复现实验；日期仍由作者组合证据归并。

## 10219 — 5分标准，仅报告：通过

实际读[官方v1](https://arxiv.org/html/2604.10219v1) IV-C Eq7–13、IV-D Eq14–17、V-A/C TablesII/III，并核III-D观察边界。HVAR用中层attention share和entropy pivot分配proxy reward；FRM另用transition词概率触发，插指令后生成、剥除外加指令并保留正确终值轨迹，两种触发不可混为一物。Qwen2.5-VL-7B的组件和同样本量筛选消融支持受限配方，但不是模型内部自知/幻觉唯一因果：奖励、筛选、额外采样与训练仍共同变化。仅报告不假称Books承载了完整recipe；不采用普遍grounding或零延迟保证。

## 10235 — 6分标准，已有覆盖：通过

实际读[官方v1](https://arxiv.org/html/2604.10235v1) §4.2–4.5 Eq3–12、§5.3 Table4及§5.4。Ch45当前“Pre-RoPE Calibration 与 Workload-semantic Selection 是两条正交路线”实际正文具体承载chunk shortlist、CPG call/control/return/assignment prior、chunk预算与保护span、再物理KV选择，不只是主题相同。60样本消融显示span保护强于纯预算调节；局部SGLang/Qwen32B端到端112–118秒不证明tail-SLO。补充采用边界：§4.4在保护token超过预算时仍截到预算，不能把hard protection描述为无限容量保留；不声称完整实现或全面胜出已复现。无必要新正文。

## 10261 — 6分标准，已有覆盖：通过

实际读[官方v1](https://arxiv.org/html/2604.10261v1) §3.3、§4.2–4.3、§5、§6.3–6.5。实际对读Ch66 Document Agent的retrieval/navigation/grounding/effort链及run diagnosis的opportunity set条件。Diamond汇合与tool链分账是有效受限评价，现正文已承载本次采用的诊断命题；不声称已经实现该benchmark。Linear与DAG任务平均长度、工具数同时变化，不能将PVR/RCR差别全部因果归于拓扑；PVR低仍可能合法shortcut，不能把未访问预定页面一概判失败。600秒、step budget、截断、模型/Agent组合都是协议条件，不采用纯模型能力排序。

## 10268 — 5分标准，仅报告：通过

实际读[官方v1](https://arxiv.org/html/2604.10268v1) §3.2 Eq7/Alg1、§3.3 Eq11–13/Alg2、§4.1–4.3。CFG0的training-resolution tiled inversion再混合原unconditional与dilated条件差，是高分辨率编辑受限分支。原文“initial steps”与Alg2的t≤τ方向表述不完全协调，采用时只记实际条件，不自行修算法。单RTX4090、SD2.1/SDXL1.0、150对、λ=.5及指标支持局部identity/quality工作点，未证明一般因果/跨范式优势；额外patch、kernel/guidance及显存成本保留。仅报告不伪称完全已有覆盖，亦不新增孤立机制摘要。

四项有限采用处置通过；这不是日期/来源整体验收或Books新增通过。
