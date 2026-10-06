# Meta 必要正文与历史版本边界

检查：2026-10-02，Asia/Shanghai。官网事件页下载链接分别指向SAM文件 `601855122_2188196835043403_3490818288454227815_n.pdf` 与PE-AV文件 `597955303_843450318459451_4764117894355142100_n.pdf`；网页缓存失败，本机各一次40秒下载超时且未取得正文。有限替代已实际下载并阅读 [SAM 2512.18099v1](https://arxiv.org/pdf/2512.18099v1)（57页）与 [PE-AV 2512.19687v1](https://arxiv.org/pdf/2512.19687v1)（38页）。前者提交12/19、后者12/22；不默认为12/16事件的相同版本，不据此授12/17归属或Books采用。官方时刻交由日期sidecar恢复，本作者不重复请求。

## SAM Audio

实际必要位置：§3.1–3.4（p6–8），§5.2（p17–18），§5.3–5.4（p19），§7.3–7.4（p25–26），§7.8.1（p28），Appendix D.1–D.3（p55–56）。

- 在DAC-VAE连续latent中沿channel联合建模target/residual；25Hz帧对齐的visual/span条件拼入latent，text走cross-attention。span的active/silent状态及dummy/null条件与训练期随机drop使缺失条件可处理。它不是保证目标/残差波形严格加和的证明。
- 辅助AED embedding对齐只在pretraining使用。p55–56对比两个3B checkpoint的general SFX；不外推所有域。具体增量是“语义与时间定位监督如何接入分离生成”，不只是把三个接口并列。
- §7.3 ground-truth span消融关闭text baseline的预测span以隔离条件增量；span-only在持续声/音乐中退步，text+span在所测域更好。§7.4 predicted span的专业器乐切片也退步；不能把时间提示当唯一实例标识。
- SAJ训练用原混合音、分离输出和text，不需reference stem；人工三次独立评分且音量归一化，performance分为recall/precision/faithfulness/overall。§7.8对保留测试集与CLAP、SDR estimator、Gemini对比，报告Pearson/Spearman相关；相关性不是逐例正确性或分布外校准保证。人工OVR受比较上下文影响，不能跨表直接相减。

## PE-AV

实际必要位置：§2（p6–8），§3（p8–9），§4.3 Tables6–10（p12–13），§5.1/Fig12（p19），Appendix D.2/Table19（p27）。

- 全局audio/video/fused AV与三种caption分别投影；八种pretrain对比pair，stage2再增两种text-conditioned joint retrieval pair，并非十项都在相同阶段。帧级模型另训练local/global activity目标。
- Table6控制caption engine变体；Table7固定总训练样本改real/synthetic比例，1:10在本实验最好并非越多越好；Table8数据扩大也有局部及平均非单调（16M平均42.9、32M42.8），不照录“monotonic”成定律。Table10更多pair亦非每次严格改善。消融为base、100k步、batch800，不能和完整大模型收益混为单一因果量。
- Fig12提高local目标采样概率可改善边界指标，同时降低惩罚false-positive的指标；具体差异是“帧级何时”与“跨样本哪个事件”两种监督竞争。default0.7是所测任务折中，不是所有连续监测系统的最佳值。
- Appendix D.2按pair两端stack、各一次all_gather再split，减少collective调用；4pair/8node作者报告step-time改善，未披露足够硬件/精度等字段，不作配置无关性能保证。

## Books具体比较（未写书）

已读 `MULTIMODAL-REPRESENTATION` Ch23“对齐不是把向量拉近这么简单”及相邻“时间、空间与provenance必须进入状态”：现文具体解释全局对比不保证局部定位、多目标冲突和真实采集时钟≠可读时间token。此原则已有覆盖；PEA-Frame的local/global采样反向指标与上述联合pair训练不是主题相同即整项已覆盖。若历史版本/日期成立，可在该节全局/时空对齐段后加入局部与跨样本负例的具体取舍，而不另建owner。

SAM拟归 `MULTIMODAL-GENERATIVE-PARADIGMS`：现Ch24有条件生成、flow路径和draft/verify职责，但尚未据实际段落证明已覆盖target/residual联合flow与三类条件的消歧边界。日期及历史版本未解前均暂缓采用；必要正文已有可读替代，不能把“尚未阅读”包装成外部缺口。准确外部请求是官网12/16下载正文或官方证明其与上述v1必要命题一致。
