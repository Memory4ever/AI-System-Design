# 04/22 TS-Attn 非作者写后复核

root，2026-09-28。仅针对 `SF-2026-ARXIV-2604-19473` 已实写的 Ch24 机制正文与证据区，不代表 04/22 整日 Gate。

[exact-v1](https://arxiv.org/html/2604.19473v1) §3.2–3.4/§4.1–4.4 与 Ch24 旧运动条件段→新多事件偏置段→Plan/Generate/Validate handoff 对读。正文保留完整 prompt、仅对早期 cross-attention 做 frame×subject/event 局部偏置；明确 subject attention 只是区域代理、事件分段及多主体可能错、不能推物理真值。后段给旧短段/无偏置路径的共存与调度/计时成本，未把作者GPT-4o judge得分或单A100比较外推生产SLO。章末 Review note 把受限模型、帧数、分段调用及未披露配置留在证据区，正文后无新的机制正文。`git diff --check -- books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md` PASS。实际写后 PASS；未复现实验。
