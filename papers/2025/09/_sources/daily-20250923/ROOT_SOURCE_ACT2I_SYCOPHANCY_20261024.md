# AcT2I / Pointing to a Llama：有限必要证据

Singer A227确认两项已有准入、日门和各5分，但未开始CORE/Methods/直接对照且无请求在途；root明确接受后首次捕获并首备。日期/评分/owner/README不转、不第三题摘。Singer唯一另一角色回以下原域实际采用后，Sartre仅角色复用。本包不预Books、准入再判或DAY完成。

## AcT2I — 2509.16141v1

[精确稿](https://arxiv.org/html/2509.16141v1)、[raw](ROOT_CORE_ACT2I_16141_20261024.raw)/[请求](ROOT_CORE_ACT2I_16141_20261024.request.json)：UTC2026-10-24T10:05:32.824560至10:05:33.792959，200/exit0，189103B/SHA256 `af70492ccc0be14084fe205758ee7f6bac0bb1355be7037b309574a7adba85dd`。

实际完整读§3/4/6、B/G/H、D2/D3/E2及其直接表6/F1–6/8文字caption；未图像素、全taxonomy/POS/fewshot/开源模型附录、代码或复现。主命题的评价盲点、干预、直接控制与关键反侧/全部费用足停，不以余附件为配额。

**首先纠正机制类别。** 25动物间动作×每动作5个独特配对=125prompt，各模型每prompt4seed，五公开T2I模型。三种干预让GPT4/4o补空间、情绪或时间姿势描述，再原模型生成；**完全training-free prompt enrichment，不是更新T2I参数/teacher-logit训练**。E2约42–47token，目标50–70，H承认又人工小调到含义清楚；长文本、额外细节与人工选择一起变，不能把收益独占归因LLM“知识蒸馏”或时间推理电路。静态图上的motion cues不证明真实时间演化/因果世界模型。

25MTurk评者、每图3人多数yes/no，验实体和动作是否符合，非美学分。原基线接受48/45/44/29/27%仅五模型×这125难例；稀有配对被主动过采样，entropy>.82不证明各轴独立、自然分布平衡或所有人类场景。125prompt仅25action/四图共享prompt和评者，不当2500独立语义任务；未给训练seed/完整不确定性/逐项可靠度，不能补显著性。表1 gorilla-dog行text却是duck，身份/实际prompt版本需保留，不默修或由此指控全部实验无效。

主结果时间/情绪扩写较受偏好，但部分aggressive/social原prompt更好，PixArt/Playground不能同样利用细节。274/365/891%等是细分类相对变化，未核图像素/完整原计数，不能写百分点/普遍倍数；偏好赢率、majority接受与absolute质量分开。十个人类关系“9/10改善”只作者质例叙述，不是同规模独立量化外推/无人体形变。

**指标反侧是更稳的长期命题。** CLIP text-image和DINOv2相似不一定读取动作关系。DINO参考还先用CLIP从AnimalKingdom选frame，参考选择/物种外观影响测量，不是独立真实动作oracle。D2仅一张cat-chasing-mouse图比较三个caption/参考：CLIP26.9>25.9>25.6，但DINO .257低于错误参考.286/.290；正文“正确在两指标都最高”不成立。该单例足以保排名反侧，不证明所有指标无效/严格相关为零，更不在未看图时认证三caption视觉真值。D3八prompt/每prompt十问的LLaVA pilot约70%总体/62%语义，仅小样本人类对齐，不授VLM统一替人或精确risk校准。

**费用与选择。** H称default且guidance/steps/resolution跨模型一致，却未给数值、precision/模型revision、总wallclock/并发SLO；单A100与四seed不作公平全部compute证明。GPT4o全125×三维375calls约$.20只是作者所述扩写API费，不含所有image生成/额外prompt编码、人工调整、25评者/复核和独立质量验收；免训练不免采样费。保原简短prompt和无需情绪叙事的精确布局，按用途核实体/角色/动作及新增细节有无偷换目标，不由通用相似度或更丰富描述批准真实关系/物理用途。

## Pointing to a Llama and Call it a Camel: On the Sycophancy of Multimodal Large Language Models — 2509.16149v1

[精确稿](https://arxiv.org/html/2509.16149v1)、[raw](ROOT_CORE_POINTING_16149_20261024.raw)/[请求](ROOT_CORE_POINTING_16149_20261024.request.json)：UTC2026-10-24T10:05:33.911040至10:05:34.521629，200/exit0，219258B/SHA256 `6ef7e62bcc843a6548aefca02718cdbbcd7bf741bf6f9fd887f240c26016740a`。

root实际完整读§3–6/8、表1–9、A1/A2和实际表10–13（附录段落只引用表，另按真实id读取），未所有示例图像素/A3自由输出、代码或训练复现。支持双侧取舍和实际监督/部署路径已足，不扩所有VLM版本或音视频未做实验。

**不是只让模型坚持原答案。** Vanilla SFT用错误用户意见配正确答案，降低被误导flip，却也降低起初答错时接受正确反馈的能力。SRT仍是SFT：从COCO/GQA/ChartQA/DocVQA/OCRVQA/GeoQA+/AI2D/CLEVR QA造约30K一轮/两轮对话，GPT4o-mini产误导/纠正与image-textualization→reflection→summary轨迹。二轮第一答可能错，因此不对第一答算loss；训练目标是后续视觉检查与修订，而非强化错误首答。自产描述/反思仍可错，不是额外真实观察或已核忠实内部推理；只给同格式prompt与经过训练是不同干预。

**评价权限。** MME11子集、七意见case；flip只测相对Case0改变，须再分初始正确被误导的sycophancy rate（越低越好）与初始错误被纠正的correction rate（越高越好）。这两者条件分母依model/适配后首答而变，不能直接当同一固定错误人口/相同机会的转移概率。七case/每图双题共享图像，不当独立任务七倍；sum的overall不等每项真值/安全。二轮表11模板与表1显式correct/wrong answer的设置须按实际协议保留，不补成完全自然用户反馈。

§3/6.2“视觉比文本更迎合”对照给text description直接包含GT属性，改变了答案可见性/抽取难度；不是只变modality的等信息控制。降resolution也同时丢识别证据，不能独占归因latent confidence。T7 attention比例下降是伴随测量且总tokens/意见输入改变，不是训练数据失衡或注意力导致迎合的因果证明；不能把文字更低flip解释为读出了真实模型置信。

**必须保留双侧反退。** T5 Qwen原correction34.39%/syc13%→vanilla6.18%/.55%→SRT28.86%/3.47%。SRT比vanilla更愿纠正，但correction仍低原模型、syc又高于vanilla；不存在双轴全胜。LLaVA同样41.73/19.34→2.17/.55→25.2/6.61。Qwen Case0 1846.5→SRT1827.4、Case1 2024.7→1877.4亦退，不因overall高覆盖掉。T6 15K overall12992.3高30K12969.6、23K更低，不授数据量单调。T8直接prompt correction60.04%更高却syc35.10%更差；T9去reflection correction10.22%更差、syc1.56%却更低于full3.47，移除阶段还改变训练target/长度，不能识别纯推理机制或最佳Pareto边界。

**预算/部署边界。** Qwen2-VL-7B/LLaVA1.5-7B、lr1e-5/globalb64/3epoch、4A10080GB约4h，eval temp0/default其余；precision/完整trainable范围、seedCI、全部teacher/token预算/独立污染审计未披。1200items单A10080GB无CoT2m9s、CoT7m39s约3.56倍总时间，只作者批次口径，不是TTFT/并发尾SLO/每请求上界；加长输入输出/反思均付费。全QA来源/纠正标签核对、teacher生成、三阶段目标训练/全部数据量尝试、图像编码/描述/反思与独立正确/错误反馈回归均计费。音视频扩展为future，不授通用防迎合、安全或真实世界因果理解。误导/有效纠正须分别测，无法可靠核视觉/反馈时保原图、可靠QA/拒答或人工确认，不让“更自信/更坚持”替事实审定。

当前两原件请求均已结束。以上为有限必要首备与精确反侧；原评分/日期保持，待唯一另一角色实际采用，不自行判NC/I或DAY。
