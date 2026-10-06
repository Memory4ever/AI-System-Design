# Anthropic：2026-10-08 官方事件

检查：2026-10-09 13:06 BJT；作者 supplement_20260312，本轮只处理 Live 10-09。

## 来源与准入

[Research](https://www.anthropic.com/research) Publications 当前首两项均为 Oct8，下一项 Oct1，停止于该相邻旧日期；不展开旧文章。作者实际读两项官方正文，root 已独立读并校准。

- [The missing map of the sky](https://www.anthropic.com/research/the-missing-map-of-the-sky)：官方正文日期 Oct8。原有跨波段 inpainting、并行 survey 校准用于天文制图，没有新增通用模型/系统机制；AI for Science 暂缓。已读 Building / Trial and error 必要说明；两轮 agent 没发现 glow 只是具名案例，不由此判定独立复核普遍无效。具体 EX，不评分、不转入 Books。
- [Launching an opt-in vulnerability-finding service for open-source software](https://www.anthropic.com/research/launching-opt-in-vuln-finding-service-for-open-source)：官方正文日期 Oct8。人工 triage 限制报告吞吐 → opt-in 接收未人工核验输出、维护者另行验证 → 应拆开发现、报告接收与修复授权。准入校准由 root 实际通过；拟 3+2+3=8，深入核受影响安全发布合同，不采用普遍模型性能。

## 必要证据实际读范围

作者实际读 launch 全部核心正文（web 15–37），及 [OSS Scanner FAQ](https://red.anthropic.com/oss-scanner/) 全部 17–94；没有执行 scanner、构建容器、复现安全效果或审可选代码。

Launch：未经人工 triage 的报告可错；reproducer、可行时 bisection、可用时 patch 是不同证据。97 个 high/critical、48 项目选择人口中85达CVD、11重复、1invalid，88%不是所有 raw findings precision/recall；29k candidate/6k manual不是确证率。Threat-model误解及severity膨胀保留。

FAQ：注册需人工确认 core maintainer；依赖安装/build 可以联网，agent audit 在禁网沙箱中运行。未验证报告当前不启动90天CVD时钟；以后人工验证可从通知验证之日起计90天。退出后恢复标准CVD。维护者可提供scope/severity/去重指引，缺失时scanner自行猜测；报告交付格式与扫描频率可变。上述均为厂商披露合同，不是隔离或修复效果的独立验证。

## 唯一 owner 与逐字 PRE（实际写后通过）

实际读 Ch72 850–916完整局部（Security Agent trace→变换/CGIF→repository-first→containment），Ch71/73开篇；既有验证/授权原则不覆盖未triage接收的双路径。拟唯一 PLATFORM-SECURITY，在CGIF完整段后/repository-first前插一段：

人工核验仍适合没有能力自行消化大量安全报告的维护者，但它也限制发现结果的交付速度；有验证资源的维护者可以另选一条受限路径，明确同意接收尚未人工 triage 的模型报告，再自行重放、核对 threat model、去重和决定修复。这里的 opt-in 只授权接收报告，不把模型 finding 升级为已确认漏洞，也不授权 candidate patch 自动合入或上线。报告应保存可重放输入、可行时的引入版本定位和可用时的候选补丁，并分别记录各自证据状态；未验证报告的交付不应自动启动与人工验证报告相同的公开披露时钟。OSS Scanner 的公开合同将这两条路径并存，并允许退出后恢复标准 CVD；这一选择把验证工作和误报消化成本部分转给维护者，不能用选定 high/critical 样本的通过比例认证全部输出、严重性或漏报率。<!-- source-family:SF-2026-ANTHROPIC-OSS-SCANNER-20261008 -->

实际状态：root必要Source/逐字PRE通过后授窄写；作者写Ch72新871与本人3246末注、实际完整邻接顺读。root非writer实际读新正文、860–882完整局部与本人末注，POST通过/锁释放。仅采用opt-in未triage接收与人验CVD分责，不授模型准确率、实现/隔离验证或生产自动修复，非日级验收。
