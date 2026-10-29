# BrowseComp 受影响纠错证据（只读本次受影响范围）

实际取得并读取官方当前 Opus 4.6 / Sonnet 4.6 PDF 的 p2 changelog 全页；当前字节含后续版本，不声称3月原始快照。来源：[Opus](https://www-cdn.anthropic.com/6a5fa276ac68b9aeb0c8b6af5fa36326e0e166dd.pdf)，[Sonnet](https://www-cdn.anthropic.com/bbd8ef16d70b7a1665f14f306ee88b53f686aa75/Claude%20Sonnet%204.6%20System%20Card.pdf)。保留原始 [Opus PDF](SUP_CARD_OPUS.raw) / [Sonnet PDF](SUP_CARD_SONNET.raw)，抓取回执 [cards](SUP_FETCH_cards.json)。没有把同家族两卡重计成新模型事件，也未扩读全卡。

两页均明确本项纠错公开日期 March 6, 2026，足以进入用户授权的Mar06自然日补窗；不是假设00Z或Submitted。

| 受影响配置 | 旧分→修订分 | flagged处置 | 结论限制 |
| --- | --- | --- | --- |
| Opus highest single | 83.97%→83.73% | 新检出3题直接记错，未rerun；只reverify原最高分single配置 | 保守重记分，不是去泄漏后重跑能力估计 |
| Opus multi | 86.81%→86.57% | 11题更新blacklist后rerun，8/11仍correct | 与single是不同估计对象，不代表所有污染清除 |
| Sonnet highest single | 74.72%→74.01% | 新检出9题直接记错，未rerun；只reverify原最高分single配置 | 不是所有single配置的新完整比较 |
| Sonnet multi | 82.62%→82.07% | 11题更新blacklist后rerun，5/11仍correct | 只审此纠错，不扩其他能力/安全结论 |

Blog核心证据：[官方HTML文本](SUP_BROWSECOMP.txt) L15–35（普通泄漏9+主动识别/解密2；REPL与JSON镜像），L40–43（16失败尝试和访问限制），L45–54（query变持久URL及multi预算混杂），L57–59（纠错协议与限定缓解）。上限判断是runtime污染路径/分数合法性责任变化，不把multi的3.7倍观察归因为架构因果、不宣称模型被指令禁止却违规，也不凭URL blocklist签无污染证明。正文所称最有效阻挡包含BrowseComp变体的search result仅为本实验观察。

root已独立读官方core并确认准入3+2+3=8；Books具体差额仅提案交root，作者没有写共享Books。
