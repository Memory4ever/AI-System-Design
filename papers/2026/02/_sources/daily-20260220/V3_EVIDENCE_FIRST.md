# 02/20 首批原始日期与必要证据（继续中）

## 日期范围（不能当作公告点）

首8 live DataCite JSON（V3_DATACITE_*.json）与精确v1 abs匹配论文身份。原Submitted v1均在2026-02-17T19:00Z后、2026-02-18T19:00Z前；按 arXiv [availability](https://info.arxiv.org/help/availability.html) Tuesday14–Wednesday14 ET的最早Wednesday20 ET即本窗09:00，下界不排除 moderation延迟。上界使用同ID的 arXiv-issued DOI **Registered** 字段，而不把 DataCite Created 定义为正文公开：availability 明确正文随 announcement 公开、ID/DOI不能预先提供；[arXiv DOI说明](https://blog.arxiv.org/2022/02/17/new-arxiv-articles-are-now-automatically-assigned-dois/)说明新论文DOI预期在announcement之后24h内取得。这是用实际注册事件作“announcement已发生”的上界推定，不把预期24h作为硬时限，不授精确公告时刻，且Updated/scheduled_match均不作为归属证据。采用范围统一从2026-02-19T09:00:00+08:00至各Registered+1秒的半开界（包住原字段秒精度）：

15945 10:34:35；16052 10:37:07；16246 10:41:41；16313 10:43:15；16444 10:46:20；16520 10:48:13；16603 10:50:21；16708 10:52:58。均在2026-02-19，不伪造其他首公开时刻。16708原始v1题名为Policy Compiler for Secure Agentic Systems，旧inventory/当前DataCite改题名不是exact v1题名。这里只限定 arXiv 首公开事件；已有更早公开artifact/thesis时仍须独立去重，不被注册事件搬入本窗。

## 必要当前事件说明轻检查

2026-10-05实际取得首8官方current abs（`V3_CURRENT_ABS_2602.<ID>.html`），并实际读各title、完整AB、Comments（有则）、当前version与submission history的本页字段，没有在这些当前页面观察到withdrawal/correction/erratum标记。16246当前v3、16313当前v2、16444当前v2、16708当前v3的版本号本身不证重要修订；未为“无标记”遍历旧版本或全部历史。PCAS当前改名FORGE与v1机制身份不同，本日报仍只采用已核v1，不回填后来assume/guarantee contract。15945 AB16类taxonomy不等于§6.3四个受控攻击数量。

## 2602.16052v1 MoE-Spec

实际读exact-v1 §3.1–3.3、§4.1–4.6、§6、AppendixA/B/C必要段（非所有附件）。router权重按整棵drafttree求和、每层top-B名单；truncation把漏出名单专家贡献置零，甚至只走residual；substitution在名单内重取top-k并重新算约束权重。两者修改验证target，不是仅优化draft，因此不能声称保持原target distribution。§4.1注3进一步承认EAGLE tree q=1在T=1已有distribution shift，作者说各方法继承相同比较路径；任务质量近似不等于exactness。

评价：OLMoE1B-7B、Qwen3-30B-A3B、Mixtral8x7B；math/code/summarization5任务，每benchmark80样本、maxgeneration1024、FP16、A10080GB，1/1/2GPU、single-request；T=1均5seeds；63token树。budget在候选集合中挑速度最大且质量在EAGLE1SD内的点，是测试任务质量容忍条件，不是分布等价证明。AppendixC batchedMoE一致应用于AR/EAGLE/budget，不把1.4–1.5x实现收益归专家budget。§4.4低budget static失效，router优于固定但oracle须跑所有专家不可用于真实加速。§6选budget部署相关，2–3%selection代价、小tree抵不过开销，多request复用专家可缩小边际收益，sigmoidrouting未实证；不授普遍10–30%或productionSLO。

Books：INFER-SPECULATIVE-DECODING，root 已实际核必要原段与 owner 差额、授窄锁；已写现有 Expert Budget 论证内两段及末注，root 非作者实际正文/完整前后/末注 POST 通过、锁释放。不是全章脏diff归于本日，未核实现或复现。

## 2602.16603v1 FlowPrefill

实际读§3、§4、§5.1–5.2、§6.1–6.5关键评价/成本反侧。operator边界检查是轻信号，不把每operator变调度round；arrival/completion触发排序、S-EDF slack可行性与SLO batching，executionpool只执行submit/preempt/resume。TP rank同步iterationcounter防暂停错位通信deadlock。单operatorruntime仍是blocking下界，极长输入须与chunk共存而非取代chunk；没有kernel中途抢占。

评价：vLLM0.11.2，8xA80080GB NVLink200GB/s，Llama3-8B/70B、Qwen2.5-14B为1/4/2-wayTP，QwenTrace仅长度/arrival，随机token填充、singleturn化。TTFTgoodput是90%attainment可维持requestrate，text/image/search/file按任务给不同SLO。1P1D DistServe原FCFS比值不是机制单独增益；EDF+CP2K/8K更强控制中最多2.0x/4.5x。§6.3控制S-EDF/EDF/D-EDF与batchbudget；§6.4operator-v-layer blocking实测3.5–4.2x降低、低于4.5ms属于此配置，不授硬实时保证；predictor离线tokenlength polynomial依赖PD隔离，未给跨模型负载泛化保证。§6.5singleSLO500ShareGPT/Poisson<2K对照throughput相当；极长输入中间chunk合理；colocationGPU减半且TTFT目标放宽3x、不同TBT约束不可直接混同主结果。precision/maxoutput/concurrency具体未披露处保留Not Disclosed；未复现代码。

Books：INFER-SCHEDULING；两粒度原则已有具体覆盖，但原成本段缺 TP 同步 counter 与单 operator 不可中止边界。root 实际必要原段/owner PRE 后授窄锁；已在原段融入轻检查/arrival-completion 完整调度区别、TP同步及operator下界并窄同步原末注。root 非作者实际正文/完整前后/末注 POST 通过、锁释放；不复制宣传倍数，不授日级完成。
