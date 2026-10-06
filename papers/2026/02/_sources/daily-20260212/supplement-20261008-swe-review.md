# 2602.09447v1 必要审阅（作者准备，独立 Source 尚待）

精确身份：[SWE-AGI](https://arxiv.org/html/2602.09447v1)，root已通过AB潜在贡献与Feb11包络。评分2+2+2=6；读§2–3核心/关键T3/T6–7/结论反侧，原件swecore/swebehavior/swefind。不遍历22任务附录或完整日志。

拟采用：bugfix/function完成不是从authoritative spec构造长期多模块系统的等价测量。任务固定publicAPI/scaffold，public tests约10%、submission可重复得到hidden pass/fail，测量spec→implementation缺口；22任务6easy8medium8hard，不是证明AGI/生产就绪。MoonBit新生态减污染的设计理由有据，但没有pretraining overlap审计或受控其它语言实验，不授clean guarantee/语言普效。

关键评价§3.1 L188–220：不同CLI与tool policies、5.3 xhigh vs5.2 high；无统一token/wallclock预算，tokens排cached/reasoning费漏计，价格估算不得总交付费；42h单项快照与其它自然停止异质。任务pass=compile+全hidden过，test pass=public+private整体且未拆，反复hidden feedback可适应但没有heldout second suite，不将其当一次盲测或全标准correctness。runtime/memory未评分，不授functional pass即生产性能、安全、可维护性。

§3.2/T3 19/22vs17/22只是本协议作者观测，无多seed/CI，不归因单模型新增机制。easy全过不外推复杂系统，near-miss高testpass不等完整任务成功；比较ranking非新增长期命题。§3.3 T6–7 L327–372 Read含ls/find/help/artifact等启发式bucket、不含内在reasoning且front-end granularity不同；hard Read份额41.4%–64.6%不是真实时间/认知成本，更非read行为导致失败的因果证明。可保留multi-module code理解维护活动增加的局部signal及测量边界，不采用普遍“reading是central瓶颈”或最佳策略因果。硬件/precision、上下文/truncation策略、重复采样 Not Disclosed。

Source后owner拟PLATFORM-EVALUATION-SYSTEM（workload/预算/observable proxy边界），须实际现有正文才能定已有覆盖/差额；不为新22任务/数字独立造Books段。
