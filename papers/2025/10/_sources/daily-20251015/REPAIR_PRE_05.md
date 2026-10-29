# PRE05：参数适配、表示与条件的六个精确增量

writer已整体消费reader R10–13首次必要，不第二Methods。各项仅以下原稿/独立marker/本人note，请唯一reader整体核；实际目标owner/完整直接两侧已读，未写Books。

## I12 / 11598 / TRAIN-LORA Ch30 / 2+1+2=5

文件 `books/part-04-training-system/30-lora.md`，原`## Merge 与动态 Adapter 是两种资产策略`之后、完整GIFT段之前；前侧为PrivatePEFT完整两段与semantic marker，不改它们。

拟正文全文：

部署的shared adapter也可以由多次局部适配来训练，而不在运行时路由多个任务adapter：每轮从shared状态复制task adapter，在support上更新，再用不重叠query估计梯度，以first-order跨任务平均更新shared状态，最终只部署后者。[MeTA-LoRA的受限分支](https://arxiv.org/html/2510.11598v1#S3)因此分开临时任务参数、query评价与最终合并资产；detach内循环不等完整二阶元梯度，任务内适配过也不保证shared参数消除负迁移。独特样本少可能伴随千轮重复前反向，更多样本或更大模型也非逐任务单调更好；复制/局部更新、query求值、跨任务训练与最终回归全计费。Support/query泄漏、任务分布或净质量失配时，保留普通joint LoRA、目标任务adapter与独立held-out验证，不由few-shot或一个shared发布物批准零额外训练和通用迁移。

<!-- source-family:SF-2025-ARXIV-2510-11598 -->

拟本人Review note：

- `SF-2025-ARXIV-2510-11598`：Popper，Daily2025-10-15补Oct14；整体消费Epicurus R10首次必要§3/Alg1/Eq2–6/§4/T1–6/A2T7，2+1+2=5。只临时task/query/shared部署三状态；保first-order近似、任务/样本反退及重复训练全费，未第二Methods/代码/复现。PRE/SAVE/fullselfread/solePOST仅本日canonical实际层。

## I13 / 11696 / TRAIN-LORA Ch30 / 2+2+2=6

同文件，完整“Quantized base 不代表所有计算都以 4-bit 执行”原段后、完整“若希望进一步压低激活驻留”原段前。

拟正文全文：

量化基座还可能同时改变rollout探索，而不只是压低存储：冻结低位base并训练LoRA时，静态量化误差是一份固定扰动；另在RMSNorm scale注入随阶段变化的噪声，才形成动态行为分布。[QeRL的受限方法](https://arxiv.org/html/2510.11696v1#S3)中的噪声通过共享输入产生相关的乘性权重扰动，不是各矩阵独立加Gaussian，也不由entropy升高证明唯一探索因果或无偏策略更新。Base量化布局、adapter、noise law/时钟和真实rollout概率应共同绑定；这是消费资格要求，原文层名与附录映射未闭处不补成全层recipe。部分任务加噪会反退，单H100短程小batch计时不能拼成长回答或全部8卡训练的净加速，NVFP4名称也不认证H100原生FP4算术。校准、全部rollout/噪声求值、LoRA更新与独立质量回归均费；数值、探索或净预算失配时，保留无动态噪声的QLoRA、较高精度与原已验采样，不由低位存储批准免费探索和全尺度稳定。

<!-- source-family:SF-2025-ARXIV-2510-11696 -->

拟本人Review note：

- `SF-2025-ARXIV-2510-11696`：Popper，Daily2025-10-15补Oct14；整体消费Epicurus R12首次必要§3/Eq3–10/§4/T1–3/AppG/K，2+2+2=6。仅quantbase/adapter/关联动态noise的训练身份；保层名张力、AQN反退/短程计时与全费，不授独立加噪/精确PG/普遍速度。未第二Methods/代码/复现；PRE/SAVE/自读/solePOST只本日canonical真实层。

## I14 / 11509 / MULTIMODAL-REPRESENTATION Ch23 / 2+1+2=5

文件 `books/part-03-multimodal-world-models/23-multimodal-representation.md`，完整“若一段视觉 token 与动作 token 相差 200 ms”段后、完整TCAS段之前。

拟正文全文：

比较同场景的前后观察时，还可以在语言decoder之前先组织差异：两份点云经共享encoder后，对所选特征投影并作加/乘融合，让固定长度的状态同时携带原观察与变化线索，而不直接拼两倍语言tokens。[Situat3DChange的受限接口](https://arxiv.org/html/2510.11509v1#S4)减少的是decoder输入位置，不是双观察编码、融合或监督制备费用；共同坐标、ego/allocentric参照与对象对应仍须保存，表示差异不等真实动作意图。自动扩写QA和少量人核不使全部空间标签成为事实，原文重复运行口径也有冲突；部分2D任务更好、混入新数据后局部方向任务反退，不能宣三维表示统一占优。配准/标注、双路编码、全部训练与独立空间回归计费；微小变化、参照或质量失配时，保留两份原观察、显式坐标与较完整token接口，不由固定token数或平均QA分批准完整环境状态和物理控制。

<!-- source-family:SF-2025-ARXIV-2510-11509 -->

拟本人Review note：

- `SF-2025-ARXIV-2510-11509`：Popper，Daily2025-10-15补Oct14；完整消费Epicurus R11首次必要§3–5/AppC/D2/E1，2+1+2=5。只双观察差异在decoder前融合与参照身份；保run/seed冲突、QA标签/切片反退和全费，不采无成本/完整3D状态或安全。未第二Methods/全图/实现/复现；PRE/SAVE/完整自读/solePOST据本日canonical实际层。

## I15 / 11693 / MULTIMODAL-REPRESENTATION Ch23 / 2+2+2=6

同文件，完整“比较两模态的几何间隔时，先拆开均值位置与配对关系”段（SF-2026-ARXIV-2604-00279）后、完整“对齐目标也可以来自人的关系判断”段前。

拟正文全文：

共享空间的适配还可只更新语言decoder，而不重新训练模态producer：冻结视觉encoder/projector，在文本对比目标上训练decoder的LoRA，再重接原多模态输入，必要时加入少量跨模态配对。[LCO的受限分支](https://arxiv.org/html/2510.11693v1#S3)借用预训练对齐，却不保证小增量自动保住原生成或全部模态；producer冻结也不使consumer读出的语义坐标不变。文本/图文任务有分项反退，低分辨率OCR监督甚至可损生成，不能把较好的生成能力或几何结构升级成普遍representation scaling law；依赖假设的经验上界更不证明真实能力单调。预训练、合成/配对、LoRA与全部模态编码和新旧任务回归均费。模态输入、decoder坐标或质量失配时，保留原联合模型、可信跨模态配对适配与独立消费者，不由一份embedding均值批准无损重新接合。

<!-- source-family:SF-2025-ARXIV-2510-11693 -->

拟本人Review note：

- `SF-2025-ARXIV-2510-11693`：Popper，Daily2025-10-15补Oct14；完整消费Epicurus R12首次必要§3/4.1–4.2/T1/5.2–5.3/Limitations，2+2+2=6。只冻结模态producer/decoder对比适配及重接资格；中心point-mass KL/上界/scaling law不采用，保生成/模态反退与全费。未第二Methods/代码/复现；PRE/SAVE/自读/solePOST只本日canonical真实层。

## I16 / 11538 / MULTIMODAL-GENERATIVE-PARADIGMS Ch24 / 2+1+2=5

文件 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`，完整aggregator–predictor原段（SF-2026-ARXIV-2610-29854）后、完整“对自适应提交的diffusion模型，输出token数相同”段前。

拟正文全文：

生成干预也可以用有目的的退化分支作差，而不另训无条件模型：在选定block将少量大激活维置零，继续运行剩余层得到detail-deficient预测，再以原输出与退化输出的差调节guidance，并可另接CFG。[Detail Guidance的受限对照](https://arxiv.org/html/2510.11538v1#S4)把内部破坏变成采样控制，仍不证明这些通道只拥有细节或语义严格不变；选层、选维与scale依赖模型。CFG与DG叠加时两份scale也可能一起改变，代理美学/偏好提升不能单独认证prompt遵循，局部语义指标仍会退步。激活诊断、退化分支前向、全部CFG/采样与独立细节/语义回归都计费，training-free不等推理免费。内部结构、语义或净质量预算失配时，保留原denoiser、普通CFG及较小guidance，不由大激活排名批准永久删维和通用质量改善。

<!-- source-family:SF-2025-ARXIV-2510-11538 -->

拟本人Review note：

- `SF-2025-ARXIV-2510-11538`：Popper，Daily2025-10-15补Oct14；完整消费Epicurus R11首次必要§4.2–4.3/§5/T1–2/AppF/T4–5，2+1+2=5。仅degraded分支差分guidance；保选层/scale、CFG共同干预、语义proxy反退与全费，不授独立因果/语义不变/免费。未第二Methods/图像素/实现/复现；PRE/SAVE/fullselfread/solePOST只本日canonical真实层。

## I17 / 11588 / TRAIN-SFT Ch29 / 2+2+2=6

文件 `books/part-04-training-system/29-sft.md`。完整“因此 SFT data schema 是模型接口的一部分”段后、完整“拒绝示范还可能同时奖励与风险无关的措辞”段之前。

拟正文全文：

把长policy移入参数时，监督人口还应按义务类型拆开：事实记忆、行为要求与简单/复杂条件不必都用同一种QA扩写，可先安排相应继续预训，再用指令示范连接实际任务；policy ID只作回忆/路由cue，不取得授权。[一项受限policy内化研究](https://arxiv.org/html/2510.11588v1#S3)显示referral、替代和override仍弱，更多SFT甚至会损某些规则，不能从较短输入宣布动态规则已可靠执行。训练时的规则版本与来源、合成类别/预算、CPT/SFT阶段和外置当前override应分别保存；撤销、有效期和优先级仍交可信运行时，不由旧权重自行裁定。全部teacher/合成、继续训练、SFT与新旧规则回归都计费，context压缩不是生命周期净省费。规则更新、条件覆盖或独立遵从失配时，保留原显式policy上下文、检索及确定性门禁，不用参数记住规则替代最新权限与执行验收。

<!-- source-family:SF-2025-ARXIV-2510-11588 -->

拟本人Review note：

- `SF-2025-ARXIV-2510-11588`：Popper，Daily2025-10-15补Oct14；完整消费Epicurus R13与旧必要反侧，exact-v1 §2.2/3/4/T3–5/AppD/M，2+2+2=6。仅policy类别化训练人口/CPT-SFT与运行时override交接；保数据额外量、referral/override反退及全费，不采动态撤销已实现/输入压缩净省费。未第二Methods/代码/复现；PRE/SAVE/自读/solePOST只本日canonical真实层。
