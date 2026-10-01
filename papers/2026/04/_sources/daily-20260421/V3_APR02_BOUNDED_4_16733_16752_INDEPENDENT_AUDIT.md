# Apr21 四项有限非作者复核：16733～16752

审阅者：apr02。访问日期：2026-09-27。范围仅作者 `V3_BATCH_16733_16752.md` 的四项必要 exact-v1 命题、反证与实际 Books owner；未重扫来源或原始题摘库存，未修改作者 Report、笔记或共享 Books，未复现实验。本文件不是日级 Gate；作者的公告批次组合推断仍交日期 Gate，未把 submitted/Updated 字段作为首发时刻。

## 2604.16733v1 AW4RE：6 分标准，仅报告 PASS

实际读取[官方 HTML v1](https://arxiv.org/html/2604.16733v1) §3–5、Eq6–12 与评价定义；对读 Ch25 `Memory 架构为何从静态 cache 演进` 及相邻相机检索/生成历史段。同时间保留动静态证据、跨时间只取 static-mask，再投影补全，是受限观察代理而非物理 transition；有机制贡献，不能因未入 Books 写成无贡献。支持区质量与 T-LPIPS 不证明未知区真值或 policy 收益。当前章已承载证据状态、相机检索与 stale-state 责任，这个局部配方尚不要求改变长期判断；仅报告合理，不冒称整个实现已覆盖。2+2+2=6；未采用串联模块表达为完整概率证明或实时 SLO。

## 2604.16734v1 Sequential Prefill：5 分标准，仅报告 PASS

实际读取[官方 HTML v1](https://arxiv.org/html/2604.16734v1) Alg1、§3–4、Table1–2；对读 Ch45 逻辑 KV 不含 workspace 的容量定义及压缩/物理分配 owner 段。Alg1 先 append 再 evict，故 KV 瞬态 M+b，不能声称全程硬上限 M。A100、block256 的 Qwen2.5-VL-7B 小预算平均54.46对完整65.52，有明显有损反例；InternVL14B 的 Table2 68.95与63.26差值也不等标出的7.73。保留少物化 KV 与额外顺序延迟的取舍，不采普遍 minimal-loss、峰值估算或生产并发保证。2+1+2=5；局部配方仅报告，不以一般容量原则假称算法完整已有。

## 2604.16745v1 CATIS：6 分纠错深入，窄争议 PASS

实际读取[官方 HTML v1](https://arxiv.org/html/2604.16745v1) §3.1 Eq1/Assumption1/Proposition1、§3.3–4 机制、§5 与 AppendixJ/K 的必要吞吐行；对读 Ch23 预算、结构保护与代理重要性段。取 ε(l)=c∈(0,1)，满足非减假设，但 Eq1 得 Δ(l)=lcrδ，仅线性，故该假设单独不能推出普遍超线性/固有 collapse。额外 α>0 反馈分支与有限经验不因此失效；pairwise/unary 扰动总量到排序风险还需规范化与 margin 条件。2+2+2=6 深入只隔离中心普遍保证，保留 z-score、CLS 趋势与 protect/merge/evict 机制。VideoMAE/A100/batch4/10warmup/50timed 的 CATIS76.2vid/s低于ToMe87.1和ToFu88.5；不能把图像 batch64 的局部吞吐外推为通用零开销。PDF未独立成功读取，不声称 PDF/实现已验证；不写 Books 定理。

## 2604.16752v1 SSTA-32：5 分标准，仅报告 PASS

实际读取[官方 HTML v1](https://arxiv.org/html/2604.16752v1) §3–6 与局限/消融；对读 Ch66 Evaluation Identity 及 decision-rule/input-estimate/actual-decision 分账正文。32条最小对照的 typed deferral 有有限诊断价值，但同会话包含 gold specification、关键词评分与首动作不构成隔离部署或执行成功。Action-only 同分不能推出内部自知；删除类别同时改变允许动作集，不独立证明四维普遍必要性。2+1+2=5 标准仅报告，不把整个 benchmark 当算法已覆盖，也不采可靠控制保证。

## 交接

四项必要 source→owner 裁决通过：3 个标准仅报告、1 个中心理论窄争议；无新增 Books 写入请求。未检查全附件、版本史、实现代码或全部外部目录；结果不能代替作者窗口、完整分母、独立日级 Gate。Apr17 的普通 Books 待办不因本复核变成外部受阻或完成。
