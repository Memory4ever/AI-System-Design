# Grading Style 18765：必要原证与具体已有覆盖提案

root 准备，仅03-21补BJT03-20；待非准备者独核，不自授Source/NC/DAY。本篇标题、完整v1摘要的新增配对评价信号已本日独立准入校准。

## 身份和最低必要证据

[exact-v1正文](https://arxiv.org/html/2603.18765v1)、[官方身份/历史](https://arxiv.org/abs/2603.18765v1)。当前v1提交03-19，不当公开日；实际[DataCite](https://api.datacite.org/dois/10.48550/arXiv.2603.18765)created03-20T02:20:27Z/registered02:20:28Z/statefindable，v1Submitted03-19T11:20:07Z、Updated03-20T00:51:40Z、Available2026-03；与本日有限官方公告批次支持BJT03-20的日级arXiv归属，不证明别处从未先发。未见当前官方撤回/勘误信号；不核全部作者历史。

实际读v1 §3.1–3.4、§4/Tables1–2/4.5、§5.1–5.4与§6直接限制；其中早期截断的144–192重新实际读完整。不核数据/代码/复现，也不遍历引用教育机构。

原正确内容可因表达风格改变judge分数→同一base答案造grammar/informal/non-native三种变体，在相同content-only评分提示下测paired delta→重考虑风格忽略指令是否已经让judge成为稳定内容仪器。拟2+1+2=5；仅judge单测量组件的新增有限反证，不把跨三领域等同跨生命周期，不授普遍教育公平结论。

- §3：60题，math/programming/essay各20；每题base与三变体，共180perturbed＋60base。两模型各240、共480次评分，Llama3.3-70B/Groq T0、Qwen2.5-72B/HF API T.01；JSON1–10＋理由，groundtruth作者自己标7–10。样本/统计单位是原题，不是独立180人群；只有作者声明内容保持，未给外部盲评的一致性及独立学生人口。
- §3.4/4：18 model×subject×perturbation paired t比较，未披露多重比较校正/独立重复/区间；六essay切片显著，另Qwen math非母语p.017，不授“数学完全公平”。T2 Qwen essay grammar d.64与正文“uniformly >.8”不一致；不采全面大效应/显著比例作普遍结论。人类相关性math近0受7–10高分/输出顶格限制，低偏差不证明准确。
- §5：固定一种含反偏指令的prompt仍有差异，支持“这份提示未充分消除所测差异”，没有无指令/多缓解对照，不支持所有prompt mitigation无用、偏差只能由深层weights产生或组织/语料造成差异。两个不同provider、model revision身份不精确，不将跨模型差别唯一归因训练文化。
- §6承认synthetic人口、两模型、每域20题、作者groundtruth、扰动未按真实写作分布校准；人工标签本身不等独立事实真值。hardware/precision/inputoutput长度/batch/concurrency/SLO与总费用未披露；无需因局部效应删除该反证，也不能照录可部署量级。

## 实际唯一 owner 与具体 NC

`PLATFORM-EVALUATION-SYSTEM` / Ch66，root实际读365–415、522–545、1915–1952及2766–2805；65/67交接复用本日已实际内容。

- 1927–1934 `Judge 的输入扰动必须保留 Clean Twin` 已逐item冻结clean/noisy、扰动族/强度/实际edit/provider、方向；明确meaning-preserving只是前提需抽检、稳定不等正确、少模板/小sample限制、失败退人工/verifier/独立evaluator。这实际承载本文配对表面风格测试，不只主题相似。
- 2766–2798 scorer表已有style/shared blindspots，并要求judge/model/prompt/sampling/rubric固定与关键slice人工/可执行校准；不是靠更强模型或一条反偏prompt制造groundtruth。
- 530以后已有prompt variants与分variant spread、原始item/pair人口/多重比较及construct效度；本文小合成任务分叉未建立需另设owner的新算法，不为每个教育slice加重复正文。

建议**具体已有覆盖**：把本文有限任务分叉、提示未充分消偏、equivalence/作者标签/多重比较与provider限制保留Daily，不改Books；这不是因审阅费时、访问受阻或已有标题缩池，证据仍保留。不新增书稿未证的“weights层偏差/数学无偏/教育发布安全”，待非准备者核此NC后计安全处置，无实际写入所以无POST。

## 非准备者最低充分审阅：正式有限 Source / 日期 / 具体 NC PASS

resume_mar18 独立 fresh 本21合同/路线/停点，实际 official v1完整AB/currentheader/history，无先稿会议信号或现页撤回/纠错字段；实际 DataCite created03/20T02:20:27Z、registered28Z/statefindable、v1Submitted03/19T11:20:07Z、Updated03/20T00:51:40Z、Available2026-03，与官方本批次夹证只支持BJT03/20 arXiv事件的限定归属，不证明其他原发不存在。

实际 v1 §3.1–3.4/L88–119、§4/T1–2/L120–169、§5.1–5.4/L170–185与§6/L189–192；60原题/180变体/480调用、两provider与T0/.01、作者7–10评分及仅内容保持声明准确。Qwenmath非母语p.017与grammaressayd.64支持保留跨域反侧/措辞冲突，单反偏prompt不证明全部缓解失效或weights层因果。未检代码/数据/复现或无关引用机构。

actual Ch66 1915–1952中CleanTwin完整段、2766–2805 scorer表与固定judge/prompt/sampling/rubric/独立slice校准完整论证、522–545原题/paired/多重比较及promptidentity，均实际读回；前次工具中间截断的2766–2805已重新完整回读，Ch65/67开篇本日身份不变有效复用。现文具体承载逐原题clean/noisy配对、meaningpreserving需抽检/稳定不等正确、style盲点与独立校准，而非只主题相似。两模型小合成切片未提出未覆盖的新通用scorer算法，root拟2+1+2=5和具体NC成立。**必要Source/日期/actual具体NC正式有限PASS**，不造Books差额或POST，不采普遍教育公平/数学无偏/零费用，单篇可安全归并，非最终DAY。
