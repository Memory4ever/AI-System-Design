# Ablate and Rescue 2603.14833v1：纠正无依据旧日期门后必要审阅

本轮只恢复已有具名项，不新增发现。原停点称“具体先稿信号”，但当前本日记录未提供其原稿 URL/公开日期；作者确认未持有，不能把模型 artifact 先公开等同于论文全文先公开。实际官方 abs/history 为 03/16 v1 submitted，既存 DataCite arxiv.content/findable registered 上界 BJT03/17；按同批日级夹证作日期复核，不追小时。最终日期裁决待 reader，不先计候选。

root 实际 https://arxiv.org/html/2603.14833v1 §3.1–3.4/§4.1–4.3/Table1/§5：先缓存并冻结 unperturbed mixing matrices，再成对 zero stream、分别恢复一个 stream，比较 baseline token distribution 的 KL 及恢复比例。高 CKA 的流仍出现不对称恢复；干预增加可辨识功能使用关系，不证明任意自然路由下可删流。781M 单模型、Dolma、AdamW/Muon；CounterFact21,919 中仅65过 knowledge check，因而选择 distribution KL，不得把该分布恢复当事实正确率。训练tokens、完整预算/hardware/precision/并发/SLO未披露，不采用普遍裁剪或能力保真。CKA一般可逆线性不变性措辞不成立，不进入正文，不依赖其数学保证作功能干预判断。评分2+1+2=5，具体干预资格/相似性误用边界深入；未核 artifact 或复现。

实际 owner Ch17 403/424已有层替换与交换分责，439–500有 residual、多流及mHC carry约束，但尚未把 stream pair ablation、single rescue 与冻结mixer评价条件解释为独立实验接口。唯一 MODEL-TRANSFORMER-LAYER；在mHC carry完整段后/正交约束段前两段，衔接“几何守恒不等功能保留”。不复制 Ch66 通用因果评测。

## 逐字 PRE

> 几何约束之外，多个流是否真能互换，还需要功能干预。表示相似只说明观测到的坐标关系；一个受限实验先缓存原轨迹并冻结混合矩阵，再同时清零两条流、分别恢复其中一条，以原模型输出分布的 KL 变化衡量恢复程度。相似的流仍可呈现不对称恢复，因而不能由高相似度直接授予删流或合流。这里冻结 mixer 是实验条件，避免把恢复效果与路由重新适应混在一起，不是推理部署应永久冻结原路由的建议。

> 恢复分布也不等于恢复正确答案：受测小模型知识检验通过率很低，分布距离更适合观测干预影响，却不能证明事实能力、任意任务或剪枝后质量。缓存原 activation、成对干预与受控恢复增加评测费用，删除后重新训练的自然轨迹还须独立验收。干预人口、路由条件或 evaluator 不匹配时，保留全部 stream、任务级回归及已训练的标准 residual；跨流几何、表示相似和功能使用是互补证据，不互相签发保证。<!-- source-family:SF-2026-ARXIV-2603-14833 -->

必要 Source、日期、具体 owner 与两段 PRE 待非准备者独核；未写Books、不授DAY。末注只保存上述证据边界与真实写后身份。
