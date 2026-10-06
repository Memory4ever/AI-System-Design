# Qwen3-Omni Books 实际 POST

复核者：James，非本次 Books 写入者；写入者 root。结论：通过。仅验收本家族实际写入，不授 22 日 DAY，没有修改 Books。

实际顺读 Ch24 630–690 的完整 speech 交错→新增两段（670/672）→ARIA→时间层级论证，1772–1780 的实际 Review notes（本家族首条及相邻条）；Ch23 260–300 的 acoustic codebook、时间位置/conditioning 责任，Ch25 1–40 的生成/预测/行动条件状态区分。不是只读 root 描述或正文标记。

原源实际核对：本日具名 ae5dbf9 PDF §2.4–2.5、Table1–2、p7 RTF 定义及 §5.2 全部 Tables13–15；精确 Qwen2.5-Omni v1 §2.4 完整 streaming 小节与 Fig4 文字。沿用此前已核的本日 Blog 完整 Architecture 与原配置发布日期，不把后续报告反推为首发已公开的全部细节。PDF/HTML 已保留本日目录，未核实现、未复现或试听。

- 第一段准确区分 Talker 跨时间帧主码 AR、MTP 同帧固定步 AR 与只读左上下文 Code2Wav。没有把 MTP 写成未来多帧独立并行，或把因果 renderer 写成取消全部顺序依赖。旧 DiT/BigVGAN 原文是有限右视野的逐块流式输出，不是整句离线；正文保留质量/等待取舍。
- 第二段没有把 RTF<1 当在线首包或 tail SLO。Table2 音频首包 234→1172ms、视频547→2284ms（1→6并发）与“largely unaffected”宣传叙述的反侧在本日证据记录中保留，正文采用实际表格方向。主码、残余码、codec/buffer 费用未消失。
- Tables13–15 的质量证据主要是有限 text-to-speech：中文 WER 1.07 不胜 CosyVoice3 0.71，德语 WER 0.777 不胜 ElevenLabs 0.572，多项跨语种指标也退步；正文没有普遍音质/稳定性优势。没有同模型、同训练预算的 renderer 单因素对照，正文明确不唯一归因因果 ConvNet；未披露硬件/precision/长度/SLO 不被填造。
- 声学退步、codec 不匹配或预算不足的旧分支回退，以及已播放音频不可回滚，是限定的工程判断，不冒充厂商实测结果。与前文 reasoning 可见性、后文 ARIA 提交节奏/时间层级自然衔接，没有接管 Ch23 表示或 Ch25 world-state 真值。
- 实际末注给本日 Blog、具名 v1 必要位置和旧 v1，明确晚版本补证、非普遍收益、未实现/复现；没有隐藏日期/证据权限差额。

FSF 另见 FSF_BOOKS_POST.md：当前首段 CCL 触发与 safety-case material update 对象仍须 root 窄修。两项不能合并自动通过；实际 Books 2 的完成同步暂不授。22 日另有七项风险/反侧必要 core 普通待办，由作者继续，不借本 POST 自授作者 ready 或 DAY。
