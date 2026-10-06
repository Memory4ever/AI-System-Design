# 11975 HomeSafe：root 必要 Source 与 Ch26 PRE 提案

只补03-14的Mar13自然日，日期/准入复用本日独核，不改变旧候选。root实际读取exact-v1 `SUP_NECESSARY_11975.raw` 的§3.1–3.3（B30–42）、§4全部Eq1–4（B48–65）、§5.1.2–3（B70–85）、§5.4–5（B122–132）及D.1–3（B274–286）。支持与直接失败证据已足，不读取旧修订/无关附件，不认证代码、真机实验复现。

增量是持续快观察→黄灯异步慢查→红灯优先的告警消费接口，以及预测时刻、PNR前截止与实际停机时刻不能合为一个指标；不是泛称fast/slow。原稿slow用trigger-centered window，而§5.5另称仅最近两frame，实际可见观测/非阻塞recipe未统一，不补造生产执行。438条合成/仿真危险视频；HDR分母全是hazard，EWP只统计intent至impact、并非全部在PNR前deadline，普通安全人口FPR未由该分母证明。10FPS/2秒window/1.5秒stride的共同测试与1/5FPS adaptive策略并非已证同一完整runtime。模型/解析/传输/执行费用缺完整硬件和尾延迟合同。

直接反证：D.1慢查最终halt5.78s晚于PNR3.9s；D.2红灯4.12s晚于PNR4.0s；D.3FastBrain2.33s先识别、但engineering latency1.56s使实际停机3.89s晚于impact2.60s。§5.4平均3.10s和平均2.39s提前偏置不能抵消逐episode的deadlinemiss。中心“保障物理安全/latency compensation ensures alerts”不采用，有限接口和分母教训可以独立成立。

actual Ch26完整Safety envelope930–988、Evaluation ladder1020–1054、fastslow415–417已读：已有monitor仅告警/controller提交、异步预测年龄与完整physical evidence；缺的是异步risk alarm仲裁及alarm timestamp不等真实stop时间的具体现象。唯一owner `MULTIMODAL-EMBODIED-VLA`，Ch25预测与Ch66一般证据只handoff，不新增重复机制。提案2+2+2=6；实际安全接口/评价差额触发局部深入，不借厂商身份或bench规模加分。待非准备者Source/评分/actualowner/PRE核验，不授Books或DAY。

## 两段 PRE（拟Safety envelope监控列表后、原Critical-phase Dreaming前）

独立监视器也要在自己的内部区分反应与解释：快分支持续读当前观察，在风险含糊时提议异步慢查；等待慢结果期间，新的高风险信号仍可优先升级告警。慢查处理的是某次触发所绑定的观察窗口，不是自动更新到当前环境的事实；系统应另行验收结果对应的时刻、适用状态与超时处理，不能让旧的“安全”判断撤销更新后的危险告警。这个接口用持续快观察保留反应能力，却增加调用、窗口驻留、仲裁及陈旧结果的成本；原有确定性监视、可信低层控制器与人工接管仍是失配时的退路。

但“识别到了危险”还不是“在来得及干预时停止”。评价应分别记录可见风险开始、不可逆边界、干预截止、告警发出与实际停止，并保留未检出及非危险曝光的分母。[受限双分支监视研究](https://arxiv.org/html/2603.11975v1)中，危险识别可早于冲击，工程延迟仍使实际停止晚于冲击；仅在危险视频上统计的 detection rate 也不能证明普通运行中的 false-alarm rate。其按意图至冲击计的有效告警与不可逆边界前的干预是不同事件，平均提前偏置不能逐次抵消尾延迟。合成/仿真视频、观察窗口及实施披露尚不能认证在线物理安全；deadline 无法满足时应缩短链路、使用已验证的本地监视与控制或保守停机，而不是让较高检测分数授予安全继续权。<!-- source-family:SF-2026-ARXIV-2603-11975 -->
