# 2604.26622v1 → Ch77 非作者实际写后复核

- 审阅对象仅为 root 已写的 `books/part-07-agent/77-memory.md` 视觉压缩后两段（现约 472–479 行）及前后交接；不代表 04/30 日期、来源或整日 Gate。作者未写这两段。
- 原文：官方 [exact-v1 §4 Eq. (5)–(15)、§6 Tables 3/6/7、Limitations](https://arxiv.org/html/2604.26622v1)。式 (5) 的存储单元同时含渲染图、verbatim text segments 与 metadata；SoM 模型输出 `(image, segment)` 索引，式 (10) 从日志取回已选文字。低清命中后的高清图由原日志重新渲染，并非从缩略图无损反演。
- 实际正文从“只存图像”的感知/OCR 风险自然转入“视觉定位 + 原文日志确定性回读”的条件路径，下一节仍回到长视觉流的 entity identity。它没有将图像、已选片段相同、片段相关和答案真值混为一谈。原文日志拥有 revision、授权及删除状态是工程验收推论，正文未称作者已验证其安全实现。
- 负边界保留：Table 3 动态 Step SR 46.1% 低于静态高清 46.5%；Table 6 的 100% faithfulness 仅指选中后与日志文字一致；Table 7 在 Mind2Web 条件下文本注入 3980→596 token/step，但磁盘 18KB→1.47MB/episode、检索延迟 0.3→1.7s/step。正文没有写成无限历史可扫或端到端总成本必降。
- **裁决：实际机制正文、上下交接、source-family body marker 写后 PASS。** 审阅期间发现章末 `Review notes` 暂缺具名记录，已通知共享章写入者；root 随后补上 `SF-2026-ARXIV-2604-26622` exact-v1、实验负边界与非作者写后状态。我复读新增记录，与正文/原文相符；本次单篇可记实际 Integrate，但不据此将日报标 Complete。
