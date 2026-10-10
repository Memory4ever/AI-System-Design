# Linear Interpretability exact-v1 必要证据（作者审阅，独立 Source 待 root）

身份2602.09783v1；公开2026-02-11同日包络root已核。拟贡献：将方向可读视作训练偶然现象→线性接口、已假设特征可读与共享/稀疏条件下的不变分量论证＋非线性readout反例→需区分结构条件、整个表示与可读特征分量；2+1+2=5。中心理论主张有直接冲突，按合同定点深入，不以低分绕开。

原件linearcore.json §3 L148–276；linearevalproof.json §4/5 L276–342和A.1/A.2/B.1 L419–524；linearproof2.json §5.2–6 L342–375、B.2/B.4 L538–611。 https://arxiv.org/html/2602.09783v1 。不开展全附录证明修复；支持/反侧已足。

Definition3.4已假设φᵀWh=g(f)跨context线性可读，A.1才构造f相关分量；不由architecture单独推出所有语义线性。A.2把K个代表均值的span≤K−1推全相关子空间，未约束类内零空间；linear separable也不需centroid affinely independent。B.1只直观dim+interference成本比较，没给全representation objective下唯一/普遍optimal。B.2 LN有固定变换方向，但η/σ(h)可混杂线性读出，并非完全数值保真。

主Theorem3.13写整个h_t∝d_f；B.4实际保留h_t=λd_f+η且仅dominant单特征、η小才近似∝，与正文严格命题不同，不采用严格selfreference或普遍architecture necessity。2层moddivision p97非线性MLPhead~95%、独立linearprobe~20%仅部分未形成Fourier种子，其他种子线性probe仍成功。八小分类任务/四模型T2取每法最佳单head（selection边界），不是全head平均/通用因果faithfulness；SAE训练无class token但implicit instance并不排除feature知识。小GPT2与情感/卡通准确率弱、Apple69/65.7不等于全语义保证，训练seed/CI/headselection heldout/hardware/precision成本 Not Disclosed。

拟仅报告或争议隔离主要保证；若长期知识仅保留『条件读出与整体表示不能等同』须实际owner现有正文比较，不据争议生成书稿。独立 Source/PRE 尚未授。
