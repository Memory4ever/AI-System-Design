# 2604.24983v1：白盒 embedding 修改与文本界面不能混称

作者侧必要证据审阅；无攻击复现、不转述有害目标或可操作 payload，不代替独立/日期/日级 Gate。[官方 exact-v1](https://arxiv.org/html/2604.24983v1) *Adaptive Prompt Embedding Optimization for LLM Jailbreaking*。本日 arXiv 公告窄批链暂支持 v1 在北京时间 04/29 08:00 公告，页眉投稿日期不是首公开时刻；更早同家族例外待独立核。

§3–4 的威胁模型要求对本地 open-weight 模型的 tokenizer、embedding layer、forward 和 embedding gradient 有访问；Algorithm 1 返回改写后的连续 `E*`，而式 (2) 的 nearest-token projection 只是**文字报告/可见性**检查，不是把修改后 token 再作为攻击输入。若把投影得到的原文本发给普通 text-only API，模型通常会重新 lookup 原 `E`，论文没有证明仍有该攻击效果。因此“可见字符串未变”只说明本地白盒注入可以绕过文本层的表面比较，不能写成普通用户无权限文本消息的不可见攻击。对同模型开放自定义 `inputs_embeds`/soft-prompt 的服务，则 continuous channel 属独立不可信 artifact，要按实际暴露接口审计。

§5–6 Table 2 以 520 AdvBench、320 HarmBench text-test 行、四个 3B–7B 本地模型，与 nanoGCG/SPT/BEAST 共享最终 decoding 和两 judge 的计分口径；PEO 在所测八个 model×benchmark 格的 ASR-Judge 高于三 baseline。ASR-Judge 要 GPT-5.4 与 Claude Opus 4.6 都判 harmful，API 失败留分母且算未成功；这是**两个模型裁判的共同判断**，不是独立无误 truth。ASR-Match 与 ASR-Judge 在 Qwen3 AdvBench 等格方向不同，支持勿用关键词代替语义判别，却不证明 judge 无系统共错。§5.3 每 pass 100 optimization iterations、最多四 pass，未给完整同 hardware/同 wall-time 对照；不能仅凭迭代少宣称生产攻击成本优势。论文未评估 text-only remote endpoint 的等价可达性或实际部署防御。

`SECURITY` [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md) 已在白盒 activation 段（约 681–688）明确“直接修改内部连续状态”与“普通离散 prompt 可达性”非蕴含，并在可热插拔 prompt/soft prompt artifact 段（约 765）与 graph continuous conditioning 段（约 778）规定输入资产/权限分账。这些具体命题承载本篇真正可迁移判断；不用另建两个 owner，也不把单篇算法全部称为已覆盖。作者拟 `Design Delta 2 + System Reach 1 + Durability 2 = 5`，Standard，`No Change — Existing Coverage`；需非作者实际 source→Ch72 核确认。原在 106 工作题摘的额外潜在线索，不改变 `64+41+1` 工作账，尚未正式冻结候选。
