# SimE：actual增量最低关闭提案

准备者mar14_supplement，仅03-14补Mar13 BJT。root11完整题摘准入及七exact-v1身份/日级日期独核有效复用，不重审latestv3或倒灌新版本。精确v1 SUP_SOURCE_REM11_11211.raw GET200467249B/2026-10-10T03:22:50.970816Z，完整AB/作者及必要§III Eq1–11/B29–98、TableIII完整各行/B118–128和§IV-C B141–143、附录B320–327/D347–353实读，不声称全图像/全附录/代码。

原更多adapter连接通常扩大优化可达空间→同block Atten/MLP/All组合在increment配置下有非单调结果→仅改局部配置/训练身份，准入窄P保留。**拟1+1+2=4最低关闭/仅报告Books0，非EX/NC。** Design1来自当前adapter连接位置/组合消融，不给既有CLIP/AdaptFormer、参数空间集合包含时sup不降的成熟命题或大backbone更好加分；Reach1限定CLIP-CIL组件，Durability2受限可复用配置评价。没有新重要优化条件或跨任务动态不变量可采用。

必须区分“increment steps”与每步更新模型：实际仅task1训adapter+classifier20epoch，随后composite original/adapted image features全冻结，只用新类prototype扩classifier；不是每新任务重新微调后连续遗忘机制。TableIII 10/20steps下多分支低于Atten单分支，50steps下三分支Last75.16高于73.88，局部负侧不等普遍更多adapter有害。§IV-C以distribution-shift/overfitting解释并未做单独因果隔离；frozen后不同class划分/firsttask与读出仍改变评价，不把文中自然语义“larger incremental stages”认证为单位越大越好。

Theorem1明确须嵌套参数空间只保证sup，Theorem2存在不同loc实际解反退不是本优化器收敛或nonlinear correlation定律；无须遍历证明附录为成熟集合论补贡献。TableI †换ViT-L/14/LAION2B与主ViT-B16不能混合成matched方法优势，no old-image replay不等零state（仍存prototype/原始+适配特征、classifier与adapter）。训练参数不是总GPU/FLOPs/SLO；不采用主文thousands与TableIII1.19M矛盾的压低成本口径，不推lifelong/scalable/全部安全。身份/date/duplicate无必要具名早稿信号，沿已独核Mar13 arXiv事件；只需要非准备者actual以上原证/最低理由复核，无owner/PRE/POST或Books写需求。
