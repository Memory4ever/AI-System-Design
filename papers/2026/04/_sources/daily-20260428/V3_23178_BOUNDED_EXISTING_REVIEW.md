# 2604.23178v1 Judging the Judges：有限 Source→Owner 判断（作者侧）

此页只核[官方 exact-v1](https://arxiv.org/html/2604.23178v1) §3–5 的必要机制与实际 Ch66；不是本日日期或非作者 Gate。论文在 5 个 judge、225 受控 pair、MT-Bench 同 400 题和 LLMBar 约 200 题上比较 9 个 mitigation 配方。受控同内容 Markdown/plain STYLE 偏向在五模型中较高，但作者 §5.5 承认可读性混杂；LENGTH expansion 与 truncation 控制又表明“偏短”不能直接叫一概长度歧视。MT-Bench 的 Claude S8/S5 两组多重校正后显著；GPT-4o、Llama、Gemini Flash 大多仅方向性，LLMBar 上 position swap 反使五模型结果退步。对未知任务默认 CoT、成本估算和“style 在一切部署压倒 position”均不是受控通则。

Ch66 [Judge Ranking / calibration](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 已将 position、style、自偏好、展示顺序、固定输入/输出预算、人工校准与版本化 scorer identity 分开；Scorer 小节也保留方法对 task/rubric 的依赖。此稿的具体新增证据是**同一协议下先量哪一种 bias 与 position sensitivity 在当前模型/任务主导，再按预算选择 mitigation**，但它没有给出现有合同以外的新状态 owner、验收权限或跨模型保证。作者暂建议贡献准入后作 `5=2+1+2` 标准、窄 Existing Coverage Ch66，不为一个策略表追加算法段；受测数值作 Review 证据而非部署默认值。若非作者找到本章缺少“策略选择的测量先于 mitigator”这一独立长期职责，再只重开该窄点。

v1 `Updated=2026-04-28T00:23:30Z` 仅是本窗截止前字段；正式归属仍须公告槽、连续 ID/邻界与更早公开反证联合核，不能直接记作首次公开时间。本页不改工作上限、正式候选分母或 Books。
