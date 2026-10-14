# Oct11 必要隐私反侧小包

作者Kierkegaard；只2025-10-10补窗的新首12必要读层。不是公开日、正式评分、完整Evidence或Books授予；root独核仍普通。没有书锁或写入。

最新真实权限：root§16已实际核07452上述必要方法/threat/metrics/privacy budget及07567同v1前日§17局部readback，必要反侧通过，不重研究。下述07709新增必要层尚待独核。

## 07452：精确v1实际局部

原件[2510.07452v1 HTML](https://arxiv.org/html/2510.07452v1)，本日本人保存`SUP_PRIVACY_07452_V1_20261013.raw`，HTTP200/exit0、265585保存bytes。实际结构化完整读取§3.1、3.3–3.7、4.1、4.3–4.6、§5与Limitations；未读全references/无关附录，未执行实现。

最小机制是对每种PII的clean/corrupt配对做EAP-IG，再以95/99 percentile选边、取类型间高分边交集，以zero/mean ablation减少输出；不是证明所有PII沿唯一可删除通路，也不是参数不可逆遗忘。发现输入从私有数据每类型选1000 spans，corrupt仍是同类型替代。既有窄P可保留，但必要隐私采用只能是特定发现人口与攻击下的干预/效用取舍。

§4采用ECHR的name/location/race与FLAIR标注（正文引述约86%准确）；GPT2三尺寸、Llama3.2-1B、Qwen3-0.6B/1.7B，长度512、batch8、4epochs、1–4H100。攻击为empty prompt、top-k40、10000×256 token，并称约four million tokens，两口径并不相等；base预采50000 queries/约13M token并排除其中已出现PII。该排除使测量对象是所定义fine-tuning增量，不是部署总泄露。三次攻击重复不是训练/电路发现全部重复；verbatim输出与FLAIR匹配，不覆盖定向提示、语义变体、未知PII或更强adaptive攻击。Utility仅ECHR test perplexity，不授全任务能力保留。

§5明确Patch-DP可能低recall而高precision：GPT2-Large一例约80 precision/约1 recall。因而“少漏”不等“泄露不可信”，不能只摘低召回或摘要65%/0.01%来保证安全。该节随后实用建议称Patch-DP precision/recall均≤1%，与上述例子不一致；Llama precision的60%→0.5亦未齐单位，不补作者数值。DP组合有模型相关效用反退，Qwen3-1.7B效用不保，ε4/1较差的选择背景保留。

更关键的是§5 Privacy budget considerations：电路识别再分析私有训练数据，作者明确未计入训练时ε；不能将整体机制当作不访问私有数据的DP postprocessing或声称继承完整原保证。正文建议独立数据发现再patch是条件性重开路径，未在当前实验证明该数据独立性/预算核算。Limitations承认PII类型有限、大模型电路发现未做且资源/时间重。保留窄P，不借安全反侧降分或抹潜力；任何以后正面采用必须绑定攻击、标注、数据依赖及precision/recall不同分母。

## 07567：同一精确v1必要安全层有限复用

首12精确v1身份/完整题摘已经本日root§10实际核。本次仅定点实际读回前日本人非作者独核`daily-20251010/SUP_INDEPENDENT_20261013.md`§17的07567对应原§4/5、6.1/6.3/6.4/8必要局部，不继承前日材料池、公开日、Source或Books权限，不重全稿。

可复用反侧：forget/retain共享image，external encoder/classifier触发最低attention visual tokens的输入干预；base不改、guard可移除，因此是行为输入guard而非不可逆参数删除。400合成人脸/fake bios、8K QA并预先full memorization fine-tuning限定人口；APE仅测试的paraphrase/keyword，Min-K不是真实训练成员truth。尚无image variants、移除guard或任意extraction保证；single-run、不同GPU/RAM与per-epoch费用不可当完整同预算。外部guard/encoder有训练，不称zero external training。只有这段必要反侧和同identity采用范围复用，root可局部读回，无全Source/日门授予。

## 07709：模型判安全与实际轨迹分责，必要局部已准备

本日[2510.07709v1 HTML](https://arxiv.org/html/2510.07709v1)HTTP200/exit0、保存140472bytes于SUP_SAFETY_07709_V1_20261013.raw。实际§3.1/3.2、4.1/4.2/4.4/4.5、Tables1/2与AppA.3必要反例；未读全部taxonomy/对话附件、未运行仿真。root§10准入P有效不重题摘。

1000 social scenarios由GPT5生成unsafe逐时计划/重写safe，21categories/192subcategories；Pexels关键词取首图、CLIP ViT-L14 336px以soft.30重搜最多三次/hard.35选最高，未达null交manual，最后human verification。这是构造计划/图匹配标注过程，不是证明真实危险/所有动作物理合法。multimodal context可误导local planner，AppA.3已明确把rooftop-edge坐姿判safe；judge纠正的单例不签全部场景。

每50steps进行风险识别→替代提案→另LLM judge，再把改稿写memory；每10steps日志。unsafe-to-safe conversion计计划动作被改且模型判safe，不是执行轨迹的injury/collision或人类真实行为反事实。Table2/§4.4展示早先judge警告被planner的social/fun goal覆盖，直到约400steps才改rooftop跳跃；不是enforcement barrier保证每个被判unsafe动作在执行前禁止。社交对话/acceptance ratio与safe替代传播是另分母，不当因果safety率。

600steps×60s、晚7到早5、默认5agent；GPT4o-mini/Claude3.5Sonnet/Qwen-VL2BInstruct及text-embedding3-small。Figure7正文三者unsafe均未清零（7.5→2.3、9→5、10→5），Qwen约450steps才下降；Figure8是8场景×5agent，不让全部1000dataset变完整性能验证人口，55/75/98等不能代统一安全保证。baseline无multimodal每run$2–3，启用perception+revision/judge$5–8，费用口径联合变化不隔离视觉或单模块收益，也未给完整物理执行/端到端SLO/全部重复置信。可保留P只评价者、改稿时间、传播和执行安全不同消费对象的必要测量边界，非部署安全/伤害防止证明。
