# Apr23 三项必要处置独立核

复核者：`/root/apr20_resume`，非作者；2026-09-27。只核19749/19769/19775精确v1必要方法、直接反证及实际owner，不验收日期、全部来源或日级完成，不写共享Books。已经有效且未变的作者证据按当前位置复用，本次实际打开决定处置的原始段落。

## 2604.19749 — 标准5分，仅报告：通过

[正式v1](https://arxiv.org/html/2604.19749v1)：*The Tool-Overuse Illusion: Why Does LLM Prefer External Tools over Internal Knowledge?*。实际§4–6、Table2、Appendix B/E.1–E.3支持把无工具有限采样可用性、调用频度和收费reward分开。avg@1024不是精确知识边界，零正确样本不是内部永远不能回答；调用行为相关不识别“模型误感知”这一唯一原因。KDPO是同prompt少/多调用的偏好构造而非新DPO目标，Table2的Qwen3 AIME24 43.33→33.33和7B费用RL平均−1.1必须保留。线性utility分析只在其概率/费用模型下成立，零费时小正收益可使调用合理，不证明每种模型皆过用。

配置实际为64 Ascend910B（8节点）、7B每RL session约24h；local ReTool复现有轻微退步，checkpoint200。DAPO G16、2K/8K、T1/topP.6；E.2同时改G与temperature，不能隔离组大小。KDPO一epoch约6h、beta.05、batch256/GA4、4096，结果平均checkpoint20/40/60，不是独立seedCI。evaluation vLLM/Python sandbox、avg8、T1/topP1，precision/concurrency/SLO未披露；不扩展成搜索/写操作证明。

实际顺读Ch78:178–203 utility admission及643–660 Necessity/Execution两Gate：当前已具体承载收益/费用/失败面、授权不随utility跳过。有限新配方/数据值得报告，但无新增长期机制缺口，**2+1+2=5标准Only通过**；不称整套KDPO已Existing。

## 2604.19769 — 正确性歧义深入6分，窄暂缓：通过

[正式v1](https://arxiv.org/html/2604.19769v1)：*TTKV: Temporal-Tiered KV Cache for Long-Context LLM Inference*。实际§4.1–4.3/Algorithm1、§5.1–5.3/Tables1–7及官方HTML公式定点读取，确认Algorithm1第1/10行直接累加不同块的`Attn`输出。原文定义它为attention output，未在这条算法给共同normalizer/LSE。若采用常规块内softmax，两块各一个score0、value1得到2，联合结果1；这是印刷算法的条件反例，**不能证明未公开kernel也犯同错**。近期FIFO、K8/V4、Top-k选择及压缩/预取协议仍是有效机制描述，不随之普遍否定。

Table6无streaming的traffic47.5与8.1不同，不能把全部差归纯overlap；Table5 Avg.Lat列与p95 caption、Table7正文8B与caption70B未消歧。A100/RTX3090没有绑定各表GPU张数/weight放置；batch8、128token块、FP16/K8V4等有效配置保留，输出长度、并发、SLO及各表精确资源配置未披露。作者受限quality/traffic表保留，不把5.94×/76%/2×先作可靠设计保证。

实际Ch45:1144–1158混合格式livepage要求一次global online-softmax；已有效的prefix output/LSE机制不被替代。**2+2+2=6，因中央执行正确性歧义定点Deep与暂缓通过**，不是安全关键词自动Deep。重开只需exact-v1算法/必要kernel说明里的共同归一化、selector与计时范围、各表model/GPU/精度配置，不要求全版本/所有附件/全实验复现；不进入Books、不支持普遍效率或等价保证。

## 2604.19775 — 标准5分，仅报告：配置修正后通过

[正式v1](https://arxiv.org/html/2604.19775v1)：*From Actions to Understanding: Conformal Interpretability of Temporal Concepts in LLM Agents*。实际§3.2–3.3/§4.1–4.3/§5.1–5.2及Tables1–6：固定policy的Monte Carlo续写reward是成功倾向代理，双p值Eq4存在同时支持/同时不支持而不产生确定标签的情况。可交换性、固定NCM与类别校准条件必要；交集本身不证明概率严格下降，有限p值/tie不可当连续uniform。按保守≤界解释，不把reward类别误标界转移给后训probe、OOD任意分布或整轨迹安全。

发现作者notes把另一配置串入：**§5.1实际ScienceWorld 1443 training trajectories，60%（889）SFT，余40%平分calibration/probe；测试360 in-distribution和165 OOD**，不是8380/2500或作者RL。ALFWorld 2851中1710 SFT，剩余同样分calibration/probe。终局稀疏reward情况下F1最低.56；t3白盒RepE系数.025的提升1.1%，比较2.8/4.2/6.8不证明总成本matched/普遍胜出。hardware/precision/concurrency/SLO未披露。这里只研究一般Agent时间表示与探针，不因ScienceWorld名称重新引入AI for Science应用。

实际顺读Ch80:112–141 TrajectoryDriftSensor：方向相关、judge/calibration、白盒/跨模型失效及外部verifier/budget/effect authority已经分离。**2+1+2=5标准Only，通过条件为先纠正上述训练/测试配置**；当前新标签配方与有限实验留报告，不称算法整体Existing，也不新增Books。纠正已发root；未预支其实际修改完成。

以上结论仅是三项source→实际owner的有界非作者核；尚非Apr23日期/来源/日级Gate。没有Books写入，因此不存在本批write-after验收。
