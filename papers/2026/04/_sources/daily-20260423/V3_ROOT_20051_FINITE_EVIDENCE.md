# 2604.20051v1 — 预训练文本自博弈生成 rubric 的有界证据

Primary：[arXiv exact-v1 HTML](https://arxiv.org/html/2604.20051v1)，实际读 §3.1–3.2、§4、§5.1–5.5、Appendix J；对应[作者代码入口](https://github.com/HCY123902/POP)仅识别存在，未复现实验。HTML 的 `21 Apr 2026` 不能单独视作首次公开；本窗日期归属待官方公告/邻界核对。

**准入问题：**无人工/更强 teacher 负责开放式任务奖励时，单模型自出题、自答、自评分通常有自我确认和模式收缩风险。论文让同一 `Qwen-2.5-7B` policy 读取相关预训练段落，生成 question/reference answer、多个 candidate answer 与分项 weighted rubric，再依据 rubric 给 0/1/2 分，只选同题最高/最低两端答案并控制长度差，形成 DPO pair。它把原来仅做语言模型训练的文档用作*自生成奖励的条件信息*；但文档/参考答案/rubric/评分仍由同一模型链路产生，不是外部真值。这条条件分支在 `TRAIN-RLHF`／后训练 reward identity 中值得核验，而不是由于 health QA 应用而入选。

**工作评分，待独立：**Design Delta 2 + System Reach 1 + Durability 2 = **5**。新增的是自博弈无强 teacher 时的 *grounding passage + extreme-pair selection* 组合及其适用边界，非一般性“模型能自证对错”。只在单模型规模、三个任务域及作者 budget 下观察；不因多项本地指标提升抬分。

**机制和有限结果：**生成 rubric 时可把文档中的 gold label 抽取为某些 criterion，其他开放式 criterion 只是依文档描写；分项权重归一加权，格式/无效评价的回答被滤除，长度差超过 100 words 或同分 pair 被丢弃。DPO 只用端点 pair，因此作者的全局排序与较强模型评分 Spearman 约 0.34 仍很弱，而端点 pair 按较强模型排序约 85% 同向；**85% 不是真实人类正确率或所有候选排序保证**。主实验对照是自身基线与“同语料继续预训练”，未同预算对照人工 rubric/强 teacher 的完整方案。Qwen-2.5-7B 与 Qwen-2.5-7B-Instruct 在 health QA、创作和指令遵循上有局部改善，但后者 HealthBench500 差异较小，OOD 中一些指标略降。作者披露单节点 32 CPU/192GB RAM/1×A100 80GB；模型、数据、judge 和任务预算不构成通用训练 ROI 结论。

**反证与 trade-off：**外部文档引入检索/语料选择偏差、过时事实、版权与更多生成/评分调用；同一 policy 的 question/rubric/grade 共偏差仍可能奖励熟悉而非正确答案。只选 extremes 降低误排序暴露，但丢弃中间样本、缩小偏好覆盖，不能推 PPO/GRPO 全排序同样有效。论文 Appendix J 承认合成集规模受成本限制且需足够强的 reference model；其“减少 reward hacking/mode collapse”是机制主张和有限消融，不是形式安全证明。固定人工 rubric、外部 verifier 或强 teacher 在高风险/真实答案可得时继续合理。

**Books 比较：**[Ch33](../../../../../books/part-04-training-system/33-grpo.md) 当前已写外部 evidence-derived rubric 的 provenance、bootstrap 及自我确认风险，并有 policy 不可见 passage + 冻结 judge 的 GRPO 分支。本文的“同一 policy 从预训练文本自出题/答/评分，仅选择端点做 DPO”是一个*不同 supervision/credit 分支*；是否形成必须写入的窄缺口，须让非作者按 Ch31–33 相邻内容裁决，不能只因方法名称不同就追加。若只证明 Ch33 现有分权原则的受限应用，应判 `已有覆盖`；若补足无 teacher 时的可行/失败边界，再作流畅小幅整合。当前不写 Books。

本记录只是 root source review；**日期、非作者准入/Books 比较、来源/冻结候选和整日 Gate 均开放**。
