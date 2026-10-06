# 2025-11-19：首批11项必要证据与采用边界

作者Dalton；2026-10-04续跑。root已实际校准11份完整exact-v1题摘，不等于日期、Evidence或Books通过。以下是实际定点方法/对照/限制审阅，不是新的发现池；11项首公开仍待有限恢复，未加入正式报告的确定当窗候选。评分沿用校准包，不因审阅困难、反证或Books覆盖降分。未运行代码、复现实验或写共享Books。

完整题摘、准入理由及各项评分见 [ADMISSION_CALIBRATION.md](./ADMISSION_CALIBRATION.md)；日期原字段见其中指定的DataCite及STEP OAI raw。当前官方abs轻检在 [ABS01](./WEB_CURRENT_ABS_01.txt)、[ABS02](./WEB_CURRENT_ABS_02.txt)、[ABS03](./WEB_CURRENT_ABS_03.txt)：未见明确withdrawn/retraction标记，但下列实质版本/渲染差异已经处理，不能以“无标记”忽略。只核当前事件页，不遍历版本史。

## STEP — 2511.13091v1

[精确正文](https://arxiv.org/html/2511.13091v1) §5–7；raw [CORE04](./WEB_CORE_04.txt)、[CORE05](./WEB_CORE_05.txt)、[CORE08](./WEB_CORE_08.txt)。平滑成功率控制重采样且保留每任务一份；只使用成功轨迹，所有步骤共享成功率加权优势，不能称真实逐步信用。step augmentation的reward是与参考动作匹配，不是环境执行验证。

UI-Tars-DPO-7B、OSWorld/AndroidWorld；GiGRPO是去掉state clustering的变体，历史缩短也影响成本。OSWorld消融full23.8、去sampling21.7、去augmentation23.0、两者去除21.4；按表而非正文笔误。16 GPU/两节点的训练步时T-GRPO45.67、GiGRPO24.59、STEP26.25分钟，不是STEP端到端8.5倍，也不快于GiGRPO。评价含训练任务；GPU型号/精度/长度Not Disclosed。可保留有界采样分配分支，不采用严格held-out泛化或失败正确前缀已被利用。标准所需支持/反侧已足；日期与`TRAIN-GRPO`具体正文比较未完成。

## SoCE — 2511.13254v1

[精确18页PDF](https://arxiv.org/pdf/2511.13254v1) 方法/对照及§7.1；raw [CORE03](./WEB_CORE_03.txt)、[CORE04](./WEB_CORE_04.txt)、[CORE05](./WEB_CORE_05.txt)。局部命题是同基座对齐checkpoint的低相关类别expert选择与非均匀平均，不能泛化到异构架构/任意训练阶段。uniform-all、selected-uniform、weighted有比较，但BFCL/MGSM的leaderboard分数实际参与选择，独立dev划分只是假设/未来要求，不能认定测试独立的泛化收益；FLORES/长上下文改善有限。

HTML v1出现2026页脚/表值差异，当前abs有2026 v2；不混入v1值。局部下载PDF只取得1,968,883/3,227,258字节且超时，不作为有效完整PDF；已实际读的web精确PDF才支持上述判断。停止无关benchmark附件；首公开待定、`TRAIN-CHECKPOINT` owner差额待比，不把soup名称缺位当缺口。

## Brittleness — 2511.12728v1

[精确正文](https://arxiv.org/html/2511.12728v1) §3/4.1–4.5及限制；raw [CORE08](./WEB_CORE_08.txt)、[CORE16](./WEB_CORE_16.txt)、[CORE19](./WEB_CORE_19.txt)。22集合、三类query、语义/排列与四类提示构成受控网格，七instruct模型每个约871万query；yes/no解析把双/无答案记错。平均98.615%，不能写成普遍不会集合推理；等价排列/措辞的失败模式因模型而异，基本稳定性探针有局部价值，不证明内部“理解”机制。

全部模型皆完美的NL1模板不存在，不等于多数query失败。硬件/精度/batch/temperature在所读必要段Not Disclosed；不为追这些值扩全文。当前v1无明确纠错信号。标准局部失效命题读足；首公开及`PLATFORM-EVALUATION-SYSTEM`具体正文差额仍待，不授Books已有覆盖。

## Donors — 2511.13368v1

[精确正文](https://arxiv.org/html/2511.13368v1) §3/4及A.1；raw [CORE08](./WEB_CORE_08.txt)、[CORE09](./WEB_CORE_09.txt)、[CORE16](./WEB_CORE_16.txt)。七个Llama/Qwen小模型、单source-task-language LoRA三epochs，再排除训练匹配格评估迁移矩阵；v1匹配任务跨语言+1.63pp，两个off-task均负，整体-0.75pp，仅这一recipe/配置成立。A.1披露FP16、rank32/alpha64、无prompt masking、LR5e-5、GH200；不能把预训练基线adjustment的低R²当因果识别。

**实质修订信号**：[当前官方abs](https://arxiv.org/abs/2511.13368) v3（2026-09-11）改为11语言/四benchmark净正迁移；与v1配置/负均值不同。已定点核v3 §3/4.1及A.2，raw [METHOD](./WEB_DONORS_V3_METHOD.txt)、[TARGETED20](./WEB_TARGETED_20.txt)：新增Gemma、共同ID对齐及disjoint train/test、三seed/最低validation loss checkpoint，BF16且MC只监督answer（v1 FP16/不mask）。这是实质协议差异；未取得将v1明确认定为错误的官方说明，不能宣称作者撤回v1，但也不能拿v1外推PEFT普遍负迁移或用v3回填。必要中心反侧已核到能决定版本隔离处，停止其它v3消融/附件。首公开待定，不正面采用、不写Books；精确重开只需v1公开边界或明确影响旧结果的官方纠错。

## KAN forgetting — 2511.12828v1

[精确正文](https://arxiv.org/html/2511.12828v1) 局部支撑条件、视觉/编辑实验及AppG；raw [CORE06](./WEB_CORE_06.txt)、[CORE07](./WEB_CORE_07.txt)、[CORE17](./WEB_CORE_17.txt)。保留局部样条不保证抗遗忘的负侧：TinyImageNet中MLP更好，KAN-LoRA也非统一优胜；未证明capacity完全匹配，维度代理不是直接流形测量。

**理论争议定点**：AppG从`d_j<=D`写`r^(d_i+d_j)<=r^(d_i+D)`，对`0<r<1`方向相反；固定r下“小指数更可忽略”的解释亦不能照录。这是作者核算出的具体疑点，不宣称已审计/推翻全部理论。维度遗忘率及该推论不采用；实验局部负证据不因此按小模型或理论错误整体排除。root可直接核AppG原式；若采用理论，只在更正证明或明确r/测度假设后重开。首公开待定；`MODEL-FFN`/模型学习链仅作路由，不造长期缺口。

## Uni-MoE — 2511.12609v1

[精确正文](https://arxiv.org/html/2511.12609v1) §2.3.2/4.5；raw [CORE10](./WEB_CORE_10.txt)、[CORE12](./WEB_CORE_12.txt)、[CORE18](./WEB_CORE_18.txt)。shared always-on+routed+zero-output null，top-p累计概率阈值0.7使激活k可变；null是跳过输出，不是删参数/知识unlearning。梯度估计复用既有Grin-MoE，不能计成本次新算法。

激活比例分析不是固定质量的wall-clock/SLO对照；跨modal encoder/DiT/TTS成本不可把LLM激活参数直接代替。未取得isolated null/variable-k消融，不采用独立性能归因；设计分支本身可有界保留。算法实现未运行，85套评价不是待全文队列。当前v2为窗外修订且无明确撤回；日期待定，`MODEL-MOE`差额待实际正文比较。

## WebCoach — 2511.12997v1

[精确正文](https://arxiv.org/html/2511.12997v1) §2–4；raw [CORE02](./WEB_CORE_02.txt)、[CORE03](./WEB_CORE_03.txt)、[CORE04](./WEB_CORE_04.txt)。实际hook是zero-shot Qwen3-8B Coach消费当前状态摘要与top5 episode检索，以intervene boolean决定在下一action前同步注入system advice；actor无梯度更新，coach DPO未执行。完整episode才持久化。

同actor643 live WebVoyager任务：38B成功率.473→.614，但时长215→395.4秒；7B .328→.311为负。动态跨session顺序/网站变化及选择性vs总注入未完全控制；HNSW检索9ms不是全链成本，38B vs4o不是机理证据。可采用“该同步选择hook在此配置有正/负与延迟取舍”，不采用memory组合本身新增、普遍加速或38B优势归因。当前v2不混用；日期待定，`AGENT-MEMORY`具体差额待比。

## Visual Room — 2511.12928v1

[精确正文](https://arxiv.org/html/2511.12928v1) §3/4及AppE；raw [CORE12](./WEB_CORE_12.txt)、[CORE14](./WEB_CORE_14.txt)、[CORE18](./WEB_CORE_18.txt)。350图/2100问题、17任务、10模型zero-shot三次平均。感知全对样本子集上的认知变化是条件筛选，不是干预；平均变化小且存在负值，不能证明认知不依赖感知。MC与caption混合评价也不能直接等同能力百分点。

AppE保留前序感知问题的串联prompt使多数配置改善，且有Gemini2.0Flash反侧；不能与主表2.5模型混用。只采用评估协议/问题依赖对“seeing vs understanding”解释的局部边界，不采用Chinese-Room哲学普遍结论。精确API版本/预算等Not Disclosed；不扩AppC全部指标。日期待定；`MULTIMODAL-REPRESENTATION`/`PLATFORM-EVALUATION-SYSTEM`路由而非已有覆盖判断。

## NAND PIM — 2511.12860v1

[精确正文](https://arxiv.org/html/2511.12860v1) III-B/C、IV/V；raw [CORE12](./WEB_CORE_12.txt)、[CORE14](./WEB_CORE_14.txt)、[CORE18](./WEB_CORE_18.txt)、[CORE19](./WEB_CORE_19.txt)。小plane降低RC却损密度；H-tree在die内RPU累计部分结果以减outbound traffic。64同尺寸plane三MVM对shared bus模拟平均减时46%；大小plane对照匹配active-BL吞吐，不代表已制成硬件。

W8A8静态QLC与动态SLC-KV/INT16 RPU分工；NeuroSim/3D-FPIM/SimpleSSD模型与实测4090基线不是同类测量。single-batch、输入/输出1K；初始KV写入120ms的OPT30B实例需较长输出摊销，不能称TTFT同倍加速。32年寿命依赖三天retention/50倍耐久假设，是projection；面积亦工艺缩放估算。采用有界容量/RC/累加路径设计，不授生产能力。当前abs ICCD2025提示需有限publisher首公开恢复；日期待定，`INFER-GPU-MEMORY` owner差额待比。

## Length bias — 2511.12573v1

[精确正文](https://arxiv.org/html/2511.12573v1) §3–5及AppI；raw [CORE10](./WEB_CORE_10.txt)、[CORE13](./WEB_CORE_13.txt)、[CORE15](./WEB_CORE_15.txt)。方法依赖“固定内容变长度/固定长度变内容”的有效改写；GPT4o-mini扩增和偏好翻转构造去长度数据。分类器标签是augmentation类型，不是独立人工语义gold，512截断也不能证明内容不变；relabel不自动等于真实人类偏好。

同OpenLlama3B骨架对照仍有额外数据预算；CDA_HRO的长度相关性下降但CDA_LoRA分支未降，不推广所有架构或分支。只采用受假设约束的反事实数据设计与局部结果，因果识别/普遍质量收益未证实。当前v1无明确纠错。标准有界命题支持/反侧足；日期和`TRAIN-RLHF`实际owner差额未完成。

## Live-SWE — 2511.13646v1

[精确正文](https://arxiv.org/html/2511.13646v1) §2–4/消融；raw [CORE13](./WEB_CORE_13.txt)、[CORE14](./WEB_CORE_14.txt)、[CORE16](./WEB_CORE_16.txt)、[CORE17](./WEB_CORE_17.txt)。实际是在既有bash中创建/修改脚本，每次反馈后附reflection；agent loop本身未改，任意scaffold演化属future work。Sonnet4.5-0929、temp0、250step/$3、one patch不等于无test-time compute。

Verified500的75.4 vs70.6来自同backend但baseline复用，成本.68 vs.56美元；50问题消融full76、去tool62、去reflect64无重复CI。Nano44→14、Mini60→58，不能普遍鼓励在线造工具；也未验证授权/沙箱保证。当前v2/v3的77.4不能回填v1。只采用有界在线脚本/反思分支及模型依赖反侧；首公开待定，`AGENT-REFLECTION`/`AGENT-TOOL-CALLING`实际差额待比。

## 有限停止与下一步

1. 上述局部证据已经读到能支持/收窄准入命题处，不再因日期不确定扩大全文队列。Donors影响中心结论的v3局部检查已完成版本隔离判断；日期未确认且不正面采用者只保留最小请求，不把未读全文/未比较Books统一列普通待办。真正日期确认项才继续适用标准/深入与owner判断。
2. 11项日期恢复复用原字段，不把Submitted、registered、当前findable或推定schedule当精确首公开。仅搜索该11项官方公告/作者首公开或publisher原始版本边界；有完全落窗上下界即可采用，仍无必要材料时逐项隔离并精确重开，不授零命中/窗外。
3. Gemini已有独立 [单项包](./GEMINI_SINGLE_REVIEW.md)，限定Evidence/OnlyReport已实际 [非作者通过](./GEMINI_INDEPENDENT_REVIEW.md)。本笔记不代表其余11项日级ready，不授确定当窗候选或Books长期结论。
