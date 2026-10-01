# GPT-5.5 System Card → Ch66 非作者有限复核

- 复核者 root；原日报作者 apr01。官方[公告](https://openai.com/index/introducing-gpt-5-5/)与[持续更新的 System Card](https://deploymentsafety.openai.com/gpt-5-5)同一家族；RSS 公布时刻 2026-04-23T11:00:00Z 落本窗。card §7.2/§7.2.1 已重开；当前页面注明 04/24 API safeguards 更新，不能倒填当窗原版全部措辞与后发结果。本核仅针对 04/23 即可支持的受限评价合同，不能认证整版 card 的历史不可变性。
- 原文给出固定真实 coding-agent 轨迹 prefix 的双模型重采样、隔离外部 side effect 的工具响应模拟、monitor 分级和人工复核。模拟器与原轨迹的辨别测试只检一种 realism，不证明未发生的外部行为或生产安全；已知分类的高 recall 不能替代删除类别描述后对未知错误的漏检测量。作者也明确说该研究是内部部署风险的额外信号，而非外部部署安全的直接度量。
- [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md) 的 Offline/Replay/Shadow 段已区分历史状态缺失、反事实与真实副作用；该章 simulator identity 与真实环境锚定段要求单独校验评测环境，detector 零命中/隐藏风险段要求独立抽查假阴性、不能以无告警证明安全。三段共同承载本家族可采用的**具体长期判断**。不称 Ch66 已重现 OpenAI 内部分层、样本选择、漏检率或所有 category-ablation 实现。保持 `已有覆盖`，不新增产品事实正文。
- 结论只对这一家族的 Existing 决定通过。OpenAI 历史 Research/Index 停点及不可变原版 card 全文仍是外部覆盖限制；04/24 其他候选和整日独立 Gate 尚未通过。
