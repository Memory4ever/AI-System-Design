# 12/09 实际来源停点

2026-10-02T19:01:02+08:00定点补核：Seed paper/Blog两类2025官方API各实际18条、total94/45、next20，逐项日期检查和本窗邻接已恢复；Pink Slime出版PDF与精确v1的攻击、重放与评价对读已执行，按旧公开论文后续归档关闭。具体原始字段、位置与边界见[TARGETED_REPAIR](./TARGETED_REPAIR.md)，撤销与这两项冲突的旧隔离；不改非作者§6结论。

作者 Plato；窗口 [2025-12-08T09:00:00+08:00, 2025-12-09T09:00:00+08:00)。检查 2026-10-02T17:23:41+08:00 起，17:41:05 更新。当前是执行记录，不是覆盖验收。

## 入口与搜索边界

十四每日源均按注册表原始入口打开。实际读到的段及未决自包含在 [README 第二节](../../09/README.md)。本文件补充可复查查询，不另要求 JSON/指纹。

- OpenAI、Anthropic：官方域限定 `after:2025-12-07 before:2025-12-10` 研究检索；结果出现窗外材料，不把搜索结果时间标签当正文公开时间。
- DeepMind、Google Research、Meta、Qwen：官方域与 `December 8, 2025`/`2025-12-08` 日期检索；Meta 发现 publications page=4，显示 12/12 和 12/01 相邻项；其余历史全覆盖尚未恢复。
- DeepSeek、Kimi、Hunyuan、ZAI、Seed、ERNIE、MiMo、MiniMax：官方域/实际官方 GitHub 入口与 `2025-12-08` 定点搜索。DeepSeek 搜索触发 SGLang issue 14691；ZAI 发现 GLM-4.6V、AutoGLM。辅助结果中的无关 gist、科学材料及后续 HunyuanWorld 报告不扩扫、不当窗采用。
- arXiv advanced：`date-date_type=announced_date_first`、日期 2025-12-08～2025-12-09、`large language model` 和 `transformer`；分别 Cache miss；本地入口 25 秒超时，浏览器超时，简单主题入口 HTTP 429，export API 返回 `Rate exceeded.`。日粒度字段有效性尚未恢复，因此不据空响应声明零。
- 官方列表补检：`https://arxiv.org/list/cs.CL/2025-12?skip=100&show=100` 定点 167–200；`skip=200&show=100` 定点 201–218；`cs.DC/2025-12?skip=0&show=100` 定点 25–40。月份目录仅恢复身份及相关主题，不形成窗口事件分母，不逐项审无关题目。误取较晚页及当前 pastweek 未作本日候选证据。

## 已实际读完整题摘的增补

- [2512.05858v1](https://arxiv.org/abs/2512.05858v1)：六模型、GPQA Diamond/MMLU-Pro，expert personas 对事实准确率无一致收益，低能力 persona 常下降；反证仅适用于准确率而非语气用途。潜在 owner `AGENT-PROMPT`，不是普通负侧。v1 提交 2025-12-05T16:35:18Z，公开未授；尚无性能采用或评分。
- [2512.05501v1](https://arxiv.org/abs/2512.05501v1)：本地东南亚安全规范与英语/机器翻译评价存在可能盲区，题摘提出八语言安全样本和 guardrail 差异。应核本地语境、标注和对照，而非凭数据集规模准入。v1 提交 2025-12-05T07:57:57Z，公开未授。
- [2512.05959v1](https://arxiv.org/abs/2512.05959v1)：多语/文化视觉 QA 的检索对小模型有益、对大模型可退化，潜在修正“更多检索必然更好”；须核受控索引、模型规模与检索条件。v1 提交 2025-12-05T18:55:58Z，公开未授，不按提交截点推定公告。
- [2512.05464v1](https://arxiv.org/abs/2512.05464v1)：自生成数据、自奖励 GRPO 的 Collective Agency 目标，是否只有换规范目标/既有流程组合需定点补读。v1 提交 2025-12-05T06:46:00Z，未排除、未准入。

## GLM 官方精确历史内容

通过 GitHub 官方 API 按 README 路径、`since=2025-12-08T01:00:00Z&until=2025-12-09T01:00:00Z` 查询，返回三次更新：11:27:07Z、11:28:10Z、12:17:52Z。已读取最早 [e111410 历史 README](https://github.com/zai-org/GLM-V/blob/e111410bc94b90fe19703ec89e07919b6cbbc49b/README.md) 全文，明确项目 news `2025/12/08`、106B-A12B/9B、训练上下文 128k、native multimodal function calling。commit 时间是内容版本时间，不替代公众发布时间。

历史 Model Overview 区分视觉直接进入工具参数、视觉返回进入推理，以及交错检索输出；Remaining Issues 明示纯文本能力、过度/重复思考及计数/个体识别限制。暂不采用宣传的 SOTA，没有提取未核评价图数字。所链论文 2507.01006 指 4.5V/4.1V，不是 4.6V 新报告。可能的 owner 为 `AGENT-TOOL-CALLING`，需对读 Ch78 与 Ch77/79，并与 Ch23 分清内容表示/执行契约责任。

[AutoGLM 官方说明](https://autoglm.z.ai/blog/?embed=0)全文已读：标注 December 8, 2025，叙述虚拟手机隔离、回放/干预与开源模型/推理工具链；MobileRL/ComputerRL/AgentRL 属回顾，不能都作本次新增。需恢复对应开源 artifact，判断真实执行/权限机制差异，不能仅凭“可私有部署”认定隐私保证或所有权边界已解决。当前准入事实与日期均未闭合。

## 下一步

继续 README 第五节的可执行项；首批主线程反馈已落实在 README，未改变未核日期、未评分和未审证据的状态。日期调查不阻塞其他来源推进。
