# Apr20 三项实际正文写后复核

复核者 root，非日报作者和本批写者。实际顺读 Ch24 AR/RAE-AR→partial-prefix search→edit-history 的交接，Ch28 sign geometry→随机sign→可行域的交接，Ch72 SkillPoisoning 的 admission→真实 effect 验收交接；复用 apr02 已核且未变的[必要原文与 owner 记录](./V3_APR02_SOTO_SIGN_SKILL_INDEPENDENT.md)。三项实际写后通过，未复现实验，不代替全日 Gate。

- `2604.15453`：真实两段以已训练 coarse-to-fine 表示解释 partial reconstruction 可供 verifier 搜索的条件，不把所有一维序列称语义有序；detokenizer/branch/verifier 成本、NFE≠wall-clock、内部 verifier 改善与外部质量退步及 grid/BoN 共存均保留。未采用 AppendixB 一般界或所有模态保证。
- `2604.15416`：真实两段正确区分 `E[sign(v+G·U)]=v/G` 与 raw gradient 无偏，momentum、历史包络及理论/实践分责明确；FP8 对照保留 BF16 master/nonlinear、具体梯度/state 格式，不泛化所有 AdamW 失败。采样/尺度/随机恢复状态与回退就近解释，和原 sign 几何不冲突。
- `2604.15415`：真实两段区分主动安装公开有害功能与隐蔽 payload，平台内容 policy 不由用户同意自动授予；200自然语言skills、无脚本执行、plan≠effect、judge/policy版本、误拒绝及低风险轻审路径均保留。未作法律裁决或现实事故率保证。

正文均在 Review notes 前，删除项目名称后仍构成完整条件推理。Review notes 可以最小同步写后通过，实验未复现不变；其余候选普通待办继续。
