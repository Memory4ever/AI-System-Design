# ILVR 精确证据与条件性 Books 草案

2026-10-02T18:03:46+08:00；作者 Plato。**暂缓采用：缺首公开归属及非作者证据检查。不是整合完成。**

## 原始证据

[ILVR v1](https://arxiv.org/html/2512.05665v1) 实际读 §3.1 Eq1–2、§3.2、§3.3、§4.1、Tables1–3、Figure4 与限制。

- K 个 latent pad 的隐藏态反馈下一 embedding，绕过词表；helper images 是训练监督，不是每步推理再次取图。推理中间态由模型生成，不能叫新环境 observation。
- EMA teacher=.999；冻结视觉 encoder 的局部 patch 分组，结合文字 intent 与前一 latent query 选择 top-K 视觉目标。先 CE+cosine alignment，再去 teacher 做 CE latent relaxation。
- Qwen2.5-VL-7B、AdamW1e-5、seed42，K8、L784、lambda1；COMT/VSP15epochs，10k Zebra2epochs。开放回答用 Qwen72B judge。这些限定不能写普遍能力证明。
- Table3 Stage1 OOD：Direct31.5、Pooling32.4、Interleaving34.8；缺 Interleave+Pooling 完整因子交叉，不足逐组件因果拆解。Figure4 K8 优于 K12，latent capacity 非单调。
- 必要节未披露端到端 latency、hardware、precision、batch、concurrency、SLO：Not Disclosed。避免反复像素编码是设计动机，不是已核生产加速；judge 偏差和固定 seed 保留。

## 唯一 Owner 与实际对读

Owner `MULTIMODAL-REPRESENTATION`，Ch23，`books/part-03-multimodal-world-models/23-multimodal-representation.md`，当前约868行：“文字与辅助图像写入统一 canvas，再压缩为连续 latent reasoning state”，后接 codec/token budget、可检查性和高风险外部验收。此段实际覆盖 canvas 压缩，但没有动态 hidden-state feedback、按 intent 选 teacher target 与 teacher-free relaxation，不能报 ILVR 整体已有覆盖。

相邻 Ch24 14–38 行拥有生成 factorization/状态修正/commit，不应接管视觉监督机制。Ch25 327–338 行明确 imagined UI 是 branch-local，真实 observation 才推进 authoritative state；ILVR latent 不改此边界。Ch23 约445行真实 crop 重编码与约511行检索 latent 也不能充当本机制已有覆盖。

## 局部替换草案（由 root 协调，不在本轮写书）

目标：保留 Ch23 上述 canvas 段，将其后接一段机制分支，而非覆盖原方案：

> 视觉中间态也可以不先渲染成辅助图像再压缩，而让 decoder 在文字之间生成少量连续 latent，并将上一隐藏态作为下一步输入。这把成本从重复像素编码转向 latent 生成与监督选择。训练时可用冻结视觉 encoder 的辅助图像 patch 作目标，由文字意图和前一 latent 查询选取相关 cue，再从联合对齐损失过渡到无 teacher 的语言目标；推理时不因此取得新的环境证据。静态图像压缩仍适合信息固定且需要可读中间图像的场景，动态 latent 更依赖监督目标、latent budget 与检查边界。有限视觉推理实验提示预算存在非单调收益，但没有证明端到端加速、跨负载泛化或连续状态可解释。高风险判断仍须回到可读 trace、外部 observation 与独立结果验收。

这个草案的 ILVR 特定事实需待日期与 root 精确证据核验后再落实；现阶段仅供 owner 协调，不能成为 Books 正面证据。

## GLM/AutoGLM 的不同边界

GLM-V 历史 e111410 README 已读 native multimodal function calling，不能用较旧 GLM4.5V 报告替代。Ch78 38–90行已有 tool identity/version、typed input/output、authorization 和 proposal→execution 的实际段落；它承载执行合同，不承载视觉输入/返回的编码设计。新增表示分支不一律降“仅报告”，但本次缺公开时间和可归因技术正文，Books 暂缓而非新增未经证实 asset 身份/权限机制。AutoGLM 当前 README 的确认/接管与 Ch78 合同主题有关，却不是精确历史实现证据；保持独立缺口。
