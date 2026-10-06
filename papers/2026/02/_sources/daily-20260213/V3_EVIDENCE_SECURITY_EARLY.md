# 02/13 早期安全必要证据（作者判断，待非作者 Source/Books 复核）

精确版本均 v1。下列为受影响深入，不是全文/实现复现。日期仍待本日公开范围整体复核；不继承其他日期结论。

## 2602.10134 — Reverse-Engineering Model Editing

6=2+2+2，安全反侧深入。§3.2–4：攻击者已有 pre/post weights、编辑算法/配置、协方差估计及含真实 subject/relation 的候选 pool。ΔW·C 的右奇异子空间用于候选 key 排序，再用 pre/post next-token entropy drop 排 relation。不是无候选开放世界恢复，也未直接评测 object 恢复。只采用白盒差分是新 observer 的机制；不采用 exact-recovery 定理，故不展开全 Appendix E。

D.1 L496–517：从每个数据集前2000条采样 N=1/10/50/100，subject pool 同前2000条，1000去重/补齐 prompts 含目标，5独立 runs；JS gray-box 对照用相同 pre/post logits，weight-access 权限本身不同。§4 Table2 的 zsRE prompt top1 可仅 .04–.13，不等于所有编辑高成功恢复；semantic similarity 不是原值匹配。§5/Table3 decoy 改更新几何会付 generalization/specificity 成本，未证明 privacy。硬件/精度 Not Disclosed（所用必要方法/配置未载），没有性能或生产承诺。

拟 PLATFORM-SECURITY/Ch72 差额：现337–369已枚举 secret substrate/observer、unlearning suppression 与 MoE trace，但没有 pre/post editor update 的 key-subspace 观察面。窄段接 unlearning：发布前后 checkpoint 或 delta 也需注册 observer；行为 suppression 不签发 confidentiality。只给该 locate-then-edit/候选池人口，不写普遍“编辑必泄漏”或 decoy 安全保证。

原证：V3_EVIDENCE_10134_INITIAL.txt L100–198/253–264、10134_TAIL.txt L220–309、10134_CONFIG.txt L496–544。

## 2602.10139 — Privacy Layer for Screen-based Agents

6=2+2+2，安全接口深入。§3–4把 XML/OCR 同步隐去，session mapping、本地 screenshot opaque overlay、virtual text 与 proxy(str) 本地还原，gatekeeper 对必要性/最小化做 learned 判定。实体别名实际是 SHA256(v||type) 前5位 BASE36，没有 salt；不能授匿名化/抗字典/无碰撞保证。跨模态 whitelist 放行已见于 prompt 的同名 PII 也不是隐私证明。空间 index/bounds 校验不保证 UI freshness；本地 learned gatekeeper 不获得确定性授权。

AndroidLab Pixel7Pro emulator 138任务/9apps，XML/SoM 与 GPT4o/Gemini3Flash；PrivScreen500 screens/1000 synthetic PII，UITars7B 等。Table7 与正文成功率数字冲突，保留冲突，不选较好数：GPT4o SoM 表48.55→49.28而 prose36.23→32.61；Gemini XML 表48.91→52.17而 prose34.78→39.86。Table8 UITars任务效用80→61（DualTAP67）且泄漏LR18.1仍非零。CPU OCR + RTX4090 NER 本地预处理约1.770秒/图不是全系统SLO；CPU型号/precision Not Disclosed。中心普遍 privacy/utility 保证不采用；受限接口机制可独立采用，待 root 判断。

拟 Ch72 差额：300–325 已有 span/关系本地 sanitization、opaque placeholders consistency restoration 与 KG local grounding，但没有远端代理仅见虚拟屏幕/alias、真实动作值仅由 local proxy 消费的控制分离。窄加该接口并强调 deterministic unsalted 短 alias 未提供 privacy，all-modal 漏检/截图/坐标一致性与 utility 代价；不改原 formal-DP 边界。

原证：V3_EVIDENCE_10139_INITIAL.txt L100–259、10139_TAIL.txt L258–353、V3_EVIDENCE_SECURITY_FINAL_0.txt 10139 L289–329/354–409。

## 2602.10153 — Code Comments in AI Control

6=2+2+2，安全监测反侧深入。APPS499 selected tasks；U=o4-mini、T=4.1-nano，backdoor须过已知测试但在 exploit input 错，perfect audit 假设。benign 98th percentile 为名义2% audit threshold；攻击分布可超过2%，不能当真实固定总预算。comment/no-comment 下红蓝双方均适配，effort仅 informal matched；5 monitor outputs 平均分。正常 comments 降 benign suspicion，也能让攻击解释获得 halo；真正结果是 calibration/分离与 audit/defer 决策一起变，不是 explanations 永远真实或普遍增加安全。7 monitors 不是各自独立 red-team optimization；strongest/weakest U形仅推测。§5明确未研究借 comments jailbreak monitor。

拟 Ch72差额：824–842已有低信任内容经 Agent echo 到 monitor、parser fail-unknown，但未承载完整 benign comments 改阈值后真实 backdoor separability 的评价分账。Ch66 582 format scorer paired intervention 已覆盖一般注释格式偏差，不替安全 audit/defer 合同；唯一 owner 仍 Ch72。窄加 comments 作为 untrusted explanatory view，code/test evidence 独立，冻结 benign threshold、attack distribution、audit oracle/error 与 defer utility；不删 comments 或假设 perfect audit 可部署。

原证：V3_EVIDENCE_10153_INITIAL.txt L100–259、10153_TAIL.txt L267–313。

## 2602.10161 — Omni-Safety / OmniSteer

6=2+2+2，跨模态安全深入。context/payload 分配到不同模态与单模态重复不同，测试的是重构组合；t-SNE/cos 不能证明 semantic/MI 完全控制。harm-safe 均值方向、多模态 SVD uncentered 主能量方向，再由 per-layer两层 adapter 预测 strength，hinge+L1 控拒答/误拒；不是已识别唯一 causal refusal direction。static strength0.1 虽 RSR99.8但BAR46.2（baseline95.2），强 tradeoff；trained hooks有额外计算，不是零 overhead。

A/B配置：8×A10080GB、3独立runs平均；analysis无system prompt，§3.3/5.4用default prompt；generation max256，temperature0.9/0.7/0.7。adapter bottleneck128、LR1e-3/1e-3/5e-4、不同层/阈值；precision/batch/epoch Not Disclosed。三模型数据集结果不是所有 omni-model安全；Table3的 Qwen accuracy40.43→42.47 与“小于2%”措辞不严格一致，不授普遍无质量损失。AppC ablation adapter提高BAR但不同指标可退；不全扩 Appendix F。

拟 Ch72差额：521–568 目前output guards、训练模块化隔离/MoE routing/data filtering，缺跨模态 harm-safe direction 只作 activation sensor、adapter strength 同时控制 refuse/benign 的状态干预分支。窄加实验性分支与 cause非识别/quality成本/独立 effect policy，不将它升为确定性授权或系统安全证书。

原证：V3_EVIDENCE_10161_INITIAL.txt L100–169、10161_TAIL.txt L168–249、V3_EVIDENCE_SECURITY_FINAL_1.txt L249–268、10161_CONFIG.txt L415–489/504–522。
