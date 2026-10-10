# 12166 LatentGeo：实际delta最低关闭提案

mar14_supplement，Mar13BJT补查；精确v1 `SUP_NECESSARY_12166.raw/txt` GET200/611868B/2026-10-09T16:01:56.189368UTC。完整题摘与当前官方说明有效复用`SUP_ABS_12166.txt`；official ID日级日期已root实际核六项及正常公告规则夹证PASS，`SUP_DATE_FOURTH.md`/`SUP_DATE_12166.raw`，不以Submitted/注册字段单独作first-public。当前未识别具名撤回/重要勘误/先稿信号，不遍历全部版本。

实际读§3.1–3.4完整Eq1–13/B37–99、§4.1/4.2主要评价与Table3全部行/B148–180，包括输入扰动机制study；未遍历全部数学benchmark、补充曲线或代码。plan→K10 latent boundary/pad token hidden states→answer；target为辅助图像经frozenViT/pool/**共同训练**projector得到的representation。cos+MSE不授几何truth；两流visual+plan与plan-only各对同target，stop-gradient只有consistency一支，不冻结LLM/projector或强制teacher稳定。Stage3删visual alignment但仍latent-token CE，不授已可执行辅助构造或无幻觉保证。

RL继承PPO-style/dual clip、reference KL与GDPO逐component group-normalization后batchwhiten，广播全response，并加format/一个latent segment/length/repetition奖励。它改变局部训练/rollout配置，单segment形式奖励不是辅助构造质量。Eq13 EMA latent reward对应正的exp logitbias和b_min floor，有限最大r_lat=.5不推出偏置最终归零；“自动衰减避免最终bias”和“严格防重复”不作已证保证。biased sampler与policy ratio的具体分布核对未披露，本轮不核代码/补造修正。

Table3 full34.6/text26.7、w/o stage2 13.1、w/o stage3 23.1、noRL32.1/GRPO26.7/GDPO26.1是受限训练recipe对照，去阶段改变目标/训练量，后两同时换训练组件；表无单独no-bias行，不将差额唯一归因decodingbias。四题input-superpixel saliency不直接干预latent，也不能认证latent编码正确辅助几何或因果faithful。accuracy整体提高仍有Circ. full24.6低于text30/noRL27.3等反侧。4A800/5+2+5SFT epochs/RL1/K10、answer parser/LM fallback±2%数值容差有限，未认证matched全训练tokens/hardware wallclock、precision/onlineconcurrency/SLO，未复现。

拟 **1+1+2=4，已关闭/仅报告、Books0**：原文实际新增是task-specific latent监督/两流curriculum与采样bias配置；已有视觉latent对齐、auxiliary scaffold、component-normalization成熟原则不重复加分，未给新构造有效性/独立latent验证或同质量预算可行界。不是因数学任务/小模型/Books已有覆盖或审阅成本排除，保留窄P后真实局部贡献，不倒推EX。实际Ch23 1198–1225 latent canvas/特权双流接口只作范围校准，不以“主题已覆盖”决定分数；此4分不需要泛化NC或新增书稿。待非作者必要原件/评分与日期实核，不正式计候选/不授DAY。
