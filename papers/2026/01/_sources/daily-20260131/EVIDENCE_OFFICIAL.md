# 既有官方信号的必要核证与终态边界

## Kimi CLI v1.4 / PR810

当前处置：root已实际核release时间、exact-tag受影响源分支和Ch72上下文，仅报告正式确认通过；下面“拟”保留原提案措辞，不是当前待审阅，不授日级完成。

[Release v1.4](https://github.com/MoonshotAI/kimi-cli/releases/tag/1.4)官方元数据 published_at=2026-01-30T11:37:26Z（北京时间19:37:26）落窗；tag b1af1633646129441fc0cd6d5ff375bcd68281ee。2+2+2=6，root实际决定核心准入并核必要影响分支，强制安全/兼容性深入只读受影响OAuth credential路径。

keyring backend移到portable文件，源PR声称startup migration/no reauth；精确tag load_tokens先读file，旧ref才读keyring，save成功才delete旧key。反侧：_migrate_ref无论load_tokens内部save是否成功仍返回file-ref、并持久化default config，后续读取因此可能不再走旧keyring。_save_to_file先write再chmod，_ensure_private_file抑制OSError，600是尝试不是权限保证。这些只是静态分支条件，不是生产必然丢失、攻击或实际复现；未触碰本机凭据。精确source CORE_KIMI_V14_PR810.txt，release原元数据 RELEASE_META.txt。

Books拟仅报告：PLATFORM-SECURITY Ch72实际 L118–120区分credential storage、holder/request binding、生命周期/撤销，迁移不能从“portable”或文件存在自签成功。当前版本错误路径不产生新通用授权机制，保留此实例和恢复边界，不声称原文或Books已实现transactional migration，不强制新增diff。运行时、平台文件权限/锁与异常注入结果 Not Disclosed；SLO/benchmark不适用于此静态兼容性核证。

## OpenAI custom-actions model selector — 日期终态保留

[官方 Enterprise/Edu release notes](https://help.openai.com/en/articles/10128477-chatgpt-enterprise-and-edu-release-notes)的 January30,2026 段已实际读：selector增加 GPT-5.2 Instant/Thinking，o-series/Pro不支持，workspace admin仍控制availability。这个短core只说明兼容集合，不披露新tool execution机制、安全或性能；日期无时区/秒，不足确认整段落入本日09→09窗。Research/News有界入口、RSS与exact-date补检不能恢复精确时区，故终态隔离，不评分/确定候选、不进入Books、不支持零命中。

重开只需该更新原始发布时间含时区，或官方确认的公开范围完全落窗；再在同一selector/compatibility命题上判投入，不重扫所有release。ChatGPT visual UI与应用webinar等已按范围关闭，不能借其日期定位本项。

## Tencent KsanaDiT v0.2.2 — 身份/日期/必要核心终态保留

[官方CHANGELOG](https://github.com/Tencent/KsanaDiT/blob/main/CHANGELOG.md) v0.2.2 - 2026-01-30段只列Sage-SLA/Turbo Diffusion、Qwen-Image attention op、Pinned Memory Manager/OOM(!166)线索。没有公开时区/秒、对应精确revision、pinning机制的实际变化/负侧，不能从Added/OOM标签给准入或完整覆盖。

有限恢复已到停止：目标release/tag v0.2.2 API404，GitHub release/tag和PR166直接打开cache miss；exact KsanaDiT+PinnedMemoryManager/v0.2.2检索恢复了官方changelog但未恢复必要core/时间，!166不擅改成已实际GitHub PR。此前不匹配搜索结果未采用，不扩大Tencent组织目录。终态隔离该具体信号，不作为候选/Books或“本窗无事件”的证据。

重开需官方公开的target tag/release时间含时区、!166或相同变化的精确源代码/说明，以及pinning新增机制或可比正确性/资源条件。若仅恢复普通pinning组合/工程维护则贡献关闭；未知事实不转全文附件队列。
