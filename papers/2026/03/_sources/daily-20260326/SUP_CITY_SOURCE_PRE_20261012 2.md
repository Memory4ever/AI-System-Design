# 3DCity-LLM necessarySource / sole Ch23两PRE

2026-10-12，[2603.23447v1](https://arxiv.org/html/2603.23447v1)，原2+1+2=5/date25不改。actual必要§3.2–3.3/§4/Eq1–6、§5.1–5.2/T4–5、§5.4/T8–10、§5.6–5.7/T11–12、§6限制；未读全部task表/图片点值/code或复现。明确支持target/neighborhood/global条件支持的接口，而非城市应用本身。

## 采用接口与直接反侧

Target用topviewCLIP/Uni3Dshape/nameBERT（无name置零）；neighbor按target3D距离KNN、relativepos调权shape，再与neighbornames**分别concat**（Eq3是保K个加权向量不是平均单vector）；globaltopview+全部Mnames另projector。每一路保token粒度与不同context范围；taskparserobject/relationship读三路且人工选择target，scene任务没有target、object/relationship零向量而读global。不是自动targetgrounding、同一完整jointscene给所有问题、也不是从局部邻域推出全局对象完备图。几何来自实例分割/点云/坐标，name是外部语义annotation，attentionweight非真实关系概率；接口确定输入支持而非回答/规划许可。

3.2既有instancemask/landmarks→BEV IDs及coordinates/distances模板，VLM生成1.2M多任务QA/persona，multipleVLMcrosscheck是validator意见非独立truth（ChatGPT5引用GPT4paper身份不推已核版本/私有参数）。评价同样GPT/Qwen/DeepSeek看answer/reference/evidence平均logicality/reliability，correlation.5–.8不证明消除共享偏差或稳定真值；privacy去个人数据/提示避免PII不是正式匿名保证。T4 relationshipROUGE34.61<CityVLM35.52，T5 citywiseall64.49<64.70/multihop51.23<52.26，T8加shape微增是局部support，T9/10加name改善可来自标签已供答案信息，不授geometry更正确/唯一机制归因。消融没有分别证明manualtarget→automatic或jointthree支全部必要性。未披露独立城市/QA划分详细与seed/区间，不由1.2M认证泛化。

LLaVA1.5-7B/LoRA8/dropout.05/bf16/maxseq512/B8/accum10/AdamW5e-4/ZeRO2/singleA100，两stage10/24h；targetK/M/C具体部署大小、inferprecision/B/length/concurrency/runtimegate/fallback/SLO ND。T12mean7.40/13.69/14.54s因人口不同非三支相同workload netaccelerator；encoder/segmentation/pointcloudprojection/KNN/BERT/name制备/QA与双stage/LLMjudge/推理均计费。只用任务支持分路，不用平均text/judge评可读地图、真实距离/道路规划安全或普遍低费。

## actual Ch23差额 / 锚

actual Ch23完整1125–1205 Native3D/referenceidentity/pointcloudpool→OpenVoxel实例ID/caption与partloss→partialbinding/null→nativegeometry→track/TRACE/reconstruction；1311–1326交接及Ch24/25开篇有效层。OpenVoxel由instancegroup提供读取身份却没有target对象流/relativepos邻域流/global名词流分别project与scene任务置零的明确support合同；partialbinding拥有对应资格不是分路范围。sole MULTIMODAL-REPRESENTATION Ch23，不复制城市data/benchmark为Ch27/66新owner。

拟OpenVoxel原第二完整段末“而不是由 group ID 取得几何真值权限。”之后、下一“已有对象字典也不要求…”partialbinding原段之前，两PRE+本人静态注；保原group/part与nullbound路径，不新增收纳标题。未独核/锁/实际写/POST。

## 两逐字PRE

实例身份明确之后，读取范围还可以随问题粒度分路，而不是把局部与整场景压成一份相同条件。一个受限分支分别保存目标对象的外观/形状/名称、由目标相对位置加权的邻居形状与名称，以及全局视图和地标名称，再各自映射给语言消费者。对象和关系问题仍先由人选择目标；整场景问题则把对象与邻域条件置零，只读取全局支。这样明确哪些局部证据参与当前回答，却不构成自动 grounding 或完整关系图，名称、分割、坐标和邻域选择的来源仍须保留。<!-- source-family:SF-2026-ARXIV-2603-23447 -->

任务分路可以降低无关条件干扰，也会遗漏超出邻域的关系或让名称先验替代几何证据。局部特征消融、文本相似度和多模型评语不独立认证真实空间关系，部分跨场景与多跳结果仍退步；人工目标支持也不能直接搬到开放自动检索。分割/投影、形状与名称编码、邻域计算、任务解析、QA制备与适配/读取全都付费，不同问题平均时间不是同负载的净加速或 SLO。目标、名称或坐标失配，或问题需要更完整场景时，保留全图/点云、较宽邻域、原实例字典与专用几何工具，允许 Unknown，不由分路回答批准定位、世界状态或行动规划。

## 自身静态证据注PRE

- `SF-2026-ARXIV-2603-23447` — [3DCity-LLM exact-v1](https://arxiv.org/html/2603.23447v1)必要§3.2–4/Eq1–6、§5/T4–5/T8–12与§6；仅target/relativepos邻域/global分路支持、人工target与scene置零接口。保名称/分割/坐标资格、judge非truth/质量反退/人口未披露、平均时间非净SLO与制备编码训练全费；不授自动grounding、空间/隐私真值或规划安全，未核code/全部图/task表或复现。
