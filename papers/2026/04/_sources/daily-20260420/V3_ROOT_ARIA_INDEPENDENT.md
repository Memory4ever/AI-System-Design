# 04/20 Qwen3.5-Omni ARIA 有限非作者采用核验

复核者：root；仅对 `2604.15804v1` ARIA 最窄命题、Ch24 实际邻接与拟写 literal 裁决，不签整个 04/20 Daily Gate。实际核[官方 HTML v1](https://arxiv.org/html/2604.15804v1) §2.4–2.5 和 Table2，以及 Ch24 原 speech/reasoning token 交错与 Thinker→performer 段。

结论：**最窄 source→owner 与拟写两段 PASS，可在 Ch24 既有交错段后实施，尚不是实际整合。** 论文明确比较旧 dual-track 与 ARIA 单流，把输出前缀的累计 speech/text token 比率约束在 item-level global ratio 内；这里的新约束是两种 tokenizer 编码率不同时的可提交顺序，不是已有 token type 交错或后文部署 pipeline 的同义重复。拟文保留旧 fixed-chunk/dual-track 分支，且把在线未知全局比例的获取作为未披露前提，没有把训练构造直接说成已具生产硬保证。

Table2 是作者内部设置下 theoretical first-packet latency，Flash A/V 1并发235/426ms、8并发352/1625ms；Plus 435/651→955/1980ms。它没有 ARIA 单独消融，不能把这些数字归 ARIA、也不能推任意语言或生产 p95/SLO。图表中的 Thinker/Talker TTFT/TTFC 与总体首包也不是相同指标；拟文未混用。40M小时 AuT 训练/6.25Hz 与输入视频时间身份属另一机制，不应写作 ARIA 成效。实际写入后须重新读改动段及相邻两段再给写后结论。
