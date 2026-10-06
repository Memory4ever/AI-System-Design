# AB3 四项必要证据与受限 Books 提案

当前终裁：root已实际三项缓存必要方法/评价及HRA官方必要方法/配置/限制，四项OnlyReport通过。10187/10214保持5标准，10229设计反证与10313安全必要深入；无新Books。Geo Table2作者解释与0.6B强β数值相反须保留，不能采所有scale偏好结论。以下原提案保留，标题/待核词不覆盖本段终裁。

作者实际核心方法/评价/直接反侧；root准入已通过，以下终处置待root必要核，未称已写Books。精确v1，无artifact运行/复现，沿现有材料复用，不扩全部附录。

## 10187 HOMURA — 5 标准，拟 OnlyReport

实际§3.2.1 Eq6–8/quality rewards、§4.1/Table3、§4.3/Table4/Limitations，缓存2601.10187v1-decisive.txt。语言别syllable区间及短句仅lower-bound放宽改变奖励粒度；soft exponential不保证真实spoken deadline。Eq8 outside取max-distance而非最近边界，不修成smooth penalty。语义来自backtranslation/embedding与teacher rubric，不是真值。Qwen3-8B三次平均、BoN/后编辑与token费用分账；tokens非wallclock，硬件/precision未披露。极端压缩[.3,.4]反弹及语义损失只限Zh–En，不采用跨语信息密度极限定律。

Ch33 L64–72已有reward代理/质量与预算分责，不冒该精确实验已覆盖；本日具体syllable配方及局部回弹不足确认一个新长期reward知识缺口，真实时长/韵律尚未直接测量。拟仅报告局部选择证据，无新Books。并非因小模型/translation任务排除；候选保留。

## 10214 DepthDirector — 5 标准，拟 OnlyReport

实际§3.1–3.5、§4.1–4.3/condition ablation，缓存2601.10214v1-decisive.txt。source-video frameconcat作appearance条件；warped depth/mask channelconcat投影后加noisy latent作view条件，不把两消费者合写warped RGB。relative depth按inverse-depth scale/shift对齐、mesh遮挡；Wan2.2 TI2V5B冻结+LoRA32并不保持原函数，source帧翻倍tokens。UE5 synthetic multi-view训练，8 A100四天576×1024×81；50steps约4min为作者局部视频配置，precision及完整前处理成本未披露。200 Koala片段、MegaSaM/ArcFace/VBench/GIM/CLIP均代理；比warping略牺牲camera精度，移除source损facial motion，换小backbone同时改分辨率/容量不能纯归因。

Ch24 L168–178已有外部scaffold与生成条件/读取分责，但不是本实验exact Existing。局部camera re-rendering条件与派生depth、synthetic支持域不足确认长期3D理解/物理控制缺口，拟OnlyReport保留appearance/geometry接口与精度反侧；不授physical truth或function preservation。

## 10229 GeoSteer — 5 设计反证必要深入，拟 OnlyReport/待root差额裁决

实际Eq6–22、setup/Table1–2与direct β反侧，缓存2601.10229v1-decisive.txt。teacher gpt-oss20B正负CoT与prefix充分性打分监督VAE/regressor；逐token hidden→latent后使用Jacobian转置pullback并Euclidean归一，不是inverse-metric natural gradient或faithfulness证书。Qwen3 .6/1.7/4/8B，GSM8k four-shot样例从test随机选，不能当严格heldout；.6B强β退步、4B近flat；GPT4o CoT偏好非正确性真值。teacher/VAE训练和逐步额外gradient、hardware/precision与E2E延迟未披露。

Ch20 L277–287固定subspace与request条件库在prefill后静态复用，确不等同逐token nonlinear score pullback；不声称精确已有覆盖。我的受限提案为OnlyReport：验证的是局部learned-quality steering可行性与力度反侧，未建立更稳定/更忠实/成本合算的通用替代成立条件；若root认为“per-token learned score pullback”本身已经支持长期接口差额，定点裁决该命题，不由recipe未写自动授gap。当前不写Books。

## 10313 HRA — 5 安全必要深入，拟 OnlyReport

实际III-C–F（含Eq9符号错位）、IV-A/B直接transfer、IV-D/E预算/消融与V-B。必要精确源 https://arxiv.org/html/2601.10313v1 。local/global UAP与estimated-future梯度/离散text trigger为受限新增，ScMix作者称新但IV-A明确归ETU，不计其原创，不修Eq9。CLIP/ALBEF/TCL/BLIP，Flickr30K训练转MSCOCO/RefCOCO+；image12/255、text1、100PGD、batch16，cross-resolution resize。跨模型迁移退化仍明显，单模态baseline不隔离multimodal增益；消融拆FM/LUE/ScMix与text/image。L40s future-step训练费用上升（时间单位原表未明确），precision/全训练与统计不确定性未披露；uniformword可被人感知、低预算transfer受限。

Ch72 L748附近已有组件访问权、同目标跨输入通用扰动≠任意目标/decoder迁移的安全边界；不冒HRA局部配方exact覆盖。本日有限surrogate attack与预算消融不足授普遍防御/安全认证或长期通用攻击保证，拟OnlyReport；保留模型/任务/预算与ScMix归属冲突，未因security/negative拒绝候选。
