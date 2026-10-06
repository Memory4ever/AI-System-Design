# 2025-09-20 source/core 差额与 ready 路由

作者Tesla；2026-10-06T14:35:53+08:00。本日独立重读适用合同与路由；未变化的53份精确v1题摘初筛复用原记录，只补以下来源和必要反侧，不扩全文队列。

## Source

[实际请求](./20-narrow-recovery-requests.json)逐请求保留UTC时间、20秒上限与HTTP/字节，原响应未覆盖。

- Seed type1/year2025，原token0缺列表后实际执行20/40/60/80；20仅SwiftSpec（2506.11309），PublishDate1749657600000=2025-06-11T16:00Z/06-12北京时间；40/60缺列表，80 has_more=false/next空停止，total94始终未得到完整正文目录。原`seed-paper-page-{20,40,60,80}-recovery.raw`。Blog原type2跨下界停点不变。
- MiMo本日runtime及官方8557/6159 chunks实际200，完整读15项Blog题名/描述。组件初始8、More同数组余7，无待执行网络页；数组无date，历史缺口保留。原`mimo-runtime-recovery.raw`、`mimo-blog-bundle-recovery.raw`、`mimo-blog-component-recovery.raw`。

## 必要 Core

### [红队 2509.15478v1](https://arxiv.org/pdf/2509.15478v1)

HTML不可用后取得[精确v1 PDF](./2509.15478v1-safety.pdf)。实际读§3–5、§6/8限制及Appendix D.1/TableD1，视觉核PDF页5/Table4与页19/TableD1。May–June2025 API、英美语境，prompt成对但可重提，重提预算未量化。Table4总体文本.35、多模态.31，Qwen方向相反；不能授模态普遍优劣。17人评分并非独立prompt样本，模型间alpha差异大。§4.3的ASR口径与评级计数关系未说明；D.1 Pixtral系数4.27、TableD1为4.67，保留差异，不合并或判失实。只保留局部安全评价边界，未复现统计/实现，不作生产安全率。网页截图入口失败后使用本地PDF渲染核两页，不虚称网页截图成功。

### [It Depends 2509.16107v1](https://arxiv.org/html/2509.16107v1)

实际读§3.1–3.6、§4.1–4.3、全部Limitations及Appendix D英文全排列消融。ClearRef52/SharedRef227、8个ConceptNet关系，机器翻译五语言；一个simplification后缀。Clarification总计正确，hedge提到至少一实体可正确，Answer Attempt须全positive；correct与direct response不是同一目标。GPT-4.1-mini judge只与一作者500条英文标注核一致，非其他语言人核。DPO1388对、单次训练，SharedRef正确率升高主要伴随clarification/hedge迁移，不能当问题已被直接解决。英文全排列降低某些平均正确率、主simplification负侧仍在。保留局部澄清/目标口径潜力，非一般简化提示必然有害，未采用或复现。

### [REAMS 2509.16241v1](https://arxiv.org/html/2509.16241v1)：撤回旧关闭

完整重读v1题摘，实际补Algorithm1/Figure2、§4.1–4.5、§7/Table2、§9限制。CodeLlama13B初代码人工执行，与预先正确答案比较后，只对失败题生成Llama3.1-8B推理再送CodeLlama；Figure2称迭代至正确、Algorithm1只列一次额外阶段，次数预算未统一。推理模型8bit与人工执行已披露，但运行硬件、输入输出长度、重试总成本及统一基线预算未披露。90.15%混合265题整体与Table2 MATH89.96%不是同分母，不合并；不能用oracle失败选择及人工判定的收益证明无oracle自主求解、解释忠实或正式证明能力。

旧关闭仅“成熟program synthesis组合无具体边界”撤回：原流程揭示正确性oracle/重试资源与报告能力混杂的具体评价边界，恢复为贡献潜力，交root校准最小命题；缺原公开日期，不评分、不进正式行或Books。

### 其余关闭

本轮完整重读15560、15896、15839的精确v1完整题摘。15896另定点读§5实体混淆/说服/风格安全信号及§6机制提案：实际反侧归属于Chiang/Lee、Xu、Wu等2024研究，本稿新增的是心理解释框架/未来方向，未给本次新模型机制或新评价对照，不授其所引研究已审。维持此版本贡献关闭，不否定原安全现象。15560观点无可核新机制/条件对照，15839专门物理科学benchmark按ROADMAP暂缓；维持原范围/贡献理由。其余5明确领域标题未扩读。

## Ready 路由

53精确v1现50潜力/3关闭，另MiMo先发潜力及5领域标题。正式确认家族0；必要安全/反侧core如上，未读全部53正文。日期仍外部隔离；本日owner整合提案0、实际Books0，未授已有覆盖。

FIRST exact packet：[FIRST_BATCH.md](./FIRST_BATCH.md)加本差额；来源：[FETCH.md](./FETCH.md)加本日原请求记录。root普通待办为FIRST校准（含REAMS新最小边界与全部必要安全负侧）、Google本次再阐述事件差额、最终六部分DAY。只有日期恢复或具体校准返修才继续对应必要证据/实际owner，无53篇全文队列。作者侧材料ready，日报仍进行中。
