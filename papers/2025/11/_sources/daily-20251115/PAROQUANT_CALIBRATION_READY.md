# 11/15新增方向：ParoQuant

作者Planck；不重复首批三方向或Language Drift。精确[2511.10645v1](https://arxiv.org/html/2511.10645v1)，[实际原HTML](raw-paroquant-v1.html)及request；完整题摘在第三批XML已经读。最新[Ohm校准](FIRST_INDEPENDENT_REVIEW.md)通过准入/6分，日期采用[DATE_RECOVERY](DATE_RECOVERY.md)BJT [Nov14 09:00,Nov15 03:05:54)，原注册上界请求已否定，不能继续引用。必要后续Evidence见[新包](PAROQUANT_EVIDENCE_READY.md)，不单凭提交/DataCite赋日。

旧约束：weight-only PTQ的scaling便宜但跨通道outlier处理有限，任意rotation虽可降低量化误差却要在线矩阵计算。v1实际增量是可优化且互不重叠的Givens通道对rotation、channel-wise scaling与对应kernel协同，尝试用有限参数/独立数据访问降低在线变换代价；需要重新考虑的是精度与实际在线变换成本的联合选择，不是“正交变换是等价的”这一成熟事实。拟2+2+2=6，owner路由`INFER-TENSORRT-LLM` Ch49的量化表示/校准/产物链，不因方法名没有出现就认长期缺口。

当前只读身份、完整题摘与决定准入所需§2.2/3/4开头（web原页L90–112），不把这一准备冒称标准Evidence完成。§3的前10%通道对接近全rotation是LLaMA3-8B第一层k_proj局部实验，不能授所有层/模型最稀疏等效；Qwen3-4B AWQ MMLU-Pro下降也不单独证明长度导致误差累积。核心4.1–4.3、Table1/2与§5.2/A.4最低必要核仍是普通审阅：数值精度与group size/校准样本、channel pairing优化、online inverse开销及同硬件decode对照，不能只采2.4%和<10%宣称普遍优势。

请root独立核新增准入/拟分与上述日期范围，允许按可比反侧收窄；批准后只读支撑该命题的机制/评价，不遍历无关附件，不直接写共享Books。
