# 2603.09022 — MEMO exact-v1

本日SUP_EXACT_BATCH4/ADMISSION_BATCH4及独核AB/date夹证复用，2026-03-11公开/current无撤回；[exact-v1](https://arxiv.org/html/2603.09022v1)§3–5/Table2–4与Appendix10实际读。2+2+2=6，context-policy population与负迁移深入；不将TrueSkill/反思成熟性本身计新增贡献。

冻结模型、不更新weights；N8×5generations×50games=2000，TrueSkill μ−κσ/κ1选prompt，same-base对手、asymmetric交换角色。Memory对insights add/edit/remove、允许冲突、sample子集注入；是生成候选而非事实审核。Replay环境seed/完整prefix保留invalidmoves，inversefrequency/β采样低频失败，不是现实rollback。§4 GPT4omini/Qwen2.5 7B temp1，prompt3独立run，但RL只训练一policy、最佳checkpoint再3组test；38kRL与2kprompt不等全搜索成本对齐。heldout3opponents各50games只是此population泛化。

Table2 GPT MEMO49.5±6.4%RSE高于base25.1/44.9，但QwenMEMO44.3低于unstablebaseline45.0、GPTBriscola42.7低于ToT45.1；Table3 Kuhn memory+tournament57.2高于all55.6，不支持各组件唯一必要/全模型普胜。Table4 Briscola→SimpleTak−7.1、Grok Briscola−8/Kuhn−6直接负迁移。Appendix10约90,575对其它优化器的成本仅OUTPUT token，不含全部input/selfplay/reflection/RL训练/失败预算，不能称总API便宜。固定seed回放不消除LLM采样噪声；完整API价格、硬件/精度、tail/SLO ND或外部服务N/A，未运行artifact。

具体NoChange提案：唯一主owner AGENT-PROMPT，Ch74生命周期109–145实际读，包含候选variance/重复采样/heldout选择/所有优化采样预算/跨模型受限与proxy冻结；Ch77失败反思138–152及heldoutSkill1138–1155实际读，只作跨owner核覆盖，Ch75开篇读。采用长期命题仅contextpolicy选择不等权重更新、采样噪声与数据选择分责、生成memory是pending、迁移需heldout/成本全账。已有这些具体局部足够；TrueSkill保守评分和本游戏回放配方未推广长期必需机制，故不为方法名写段。无PRE/无Books写入，reviewer本轮实际打开必要exact-v1及具体owner局部，Source/date/6分与NoChange通过，不授DAY。
