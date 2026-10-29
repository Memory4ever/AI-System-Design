# W2T15990：必要原证、实际差额与受限 PRE

仅本19既有具名家族；resume_mar17准备，非日报作者。实际重载AGENTS/研究合同/Report合同/统一prompt/ROADMAP、来源使用/每日/arXiv主题与本日README/STOP/LS路由，Books背景及相关交接。2+2+2=6保持，具体owner差额与表示唯一性反侧触发必要深入。日期复用SUP_LATER_METADATA_MISSING5中arxiv.content findable夹证（created/registered 2026-03-18T02:21:42Z）；v1 Submitted03/16T23:01Z不是公开时刻。当前[官方事件页](https://arxiv.org/abs/2603.15990)只显示v1，无已见撤回/具体纠错信号；不全版本或全站考古。

## 必要 Source 与边界

实际[exact-v1 HTML](https://arxiv.org/html/2603.15990v1)§3/Eq1–2/Prop3.1–3.2、§4/Eq3–7、§5.1–5.4/Tables1–5及直接limits、A.1–2必要证明和remark、B.1–3/Tables6/8/Alg1及C.2/Table9。不拟合所有图、不遍全附件、不复现实验。QR代数、学习consumer与关键反侧已足够，停止原证扩读。

同一更新BA=(BG)(G⁻¹A)允许非正交GL(r)因子变化，raw factor flatten/cosine不是更新矩阵等价性的可靠表示。B=QB RB、Aᵀ=QA RA后，小core M=RB RAᵀ的SVD可lift为BA的一个精确SVD，保非零奇异值与奇异子空间，复杂度O((dout+din)r²+r³)；不需要物化dense delta。这个代数成立，但不等于每条奇异向量坐标都唯一。

Prop3.1说固定sign/order即可相同；§3和A.1同时承认重根子空间旋转，A.2末remark声称相同routine/backend/order/sign数值输出一致。独立反例：ΔW=I₂、Σ=(1,1)，U=V=I₂或U=V=R(30°)都得到同一I₂；R列为(√3/2,1/2)、(−1/2,√3/2)，每列最大绝对坐标均为正，排序及这种符号规则没有消除旋转。实际数值R Rᵀ≈diag(.9999999999999999,.9999999999999999)。同矩阵/同奇异子空间不推出逐rank U/V相等；近重根还受数值扰动，零奇异方向与padding亦须独立约定。此反例不否定精确SVD、简单非零谱的受限方向表示或有限预测实验。

只为该决定性桥定点核官方artifact：论文链接[官方repo](https://github.com/xiaolonghan2000/Weight2Token)README的regression入口；`llm/regression/perf_prediction_pipeline.py`实际import `common.w2t_utils.canonical_svd_features`与wrapper；[helper](https://github.com/xiaolonghan2000/Weight2Token/blob/main/llm/common/w2t_utils.py)实际函数只做两QR、小SVD、lift，以及U列最大绝对坐标取正并同步V符号，未在此函数见退化子空间basis固定化。raw helper一次cachemiss、单次curl连接失败后exact blob可读，不称repo不可用；main观察不是已锁实验commit，未核完整pipeline/全部code/运行。代码只是支持窄函数观察，不能冒充原实验实现全验。Eq5正常化σpool在rank Transformer之后，单凭pool零权重也不能证明删除零padding不影响其他token；本文不宣称已发现all-zero执行bug。

§4把每个位置的u/v经独立projector融合，log(1+σ)经MLP作scale/shift，rank Transformer及σ-weighted pooling后加入layer/module embedding，再position Transformer+attention pooling获得checkpoint embedding。它是带监督学习的representation，不是SVD自行读出能力。预测时只看权重，不抹掉训练adapters、构建checkpoint标签和encoder训练所消费的数据与原模型evaluation。

## 有限评价与直接反侧

全部主要adapter rank8/q-v；视觉SD1.4、512²/batch1，语言Llama3.2-3B/context512。8:1:1按checkpoint名字切分而非跨未知任务/任意base OOD；正文声明五独立encoder runs，Tables1–3未给置信区间。CelebA一identity/21图一LoRA共10177，CUB一image一LoRA11788，GoEmotions一训练样本一LoRA20000；ARC10000全数据超参trial的held-out test accuracy成为回归标签。有限ARC测试MAE .32%、RMSE .67%、Pearson98.98%、Spearman95.35%支持该人口预测信号，不授每adapter质量保证或未见任务普遍性。

Retrieval用已在ARC-Easy质量预测训练的encoder，不作检索专门训练；gallery1296、query600，四任务×六shot配置×25queries。相关性是task identity相同，非实际性能/安全或最佳可部署adapter。T3平均NDCG65.71高于GLNet43.97，但GSM8K24.97低于RawCos33.41。SD1.4→1.5的同rank邻近架构transfer不代表任意base/layout/rank。T8各encoder参数量不同，B.3训练batch/warmup也不同，不能唯一归因于canonicalization或称相同总compute。

T4测float32分解局部时间与因子cosine，不是端到端checkpoint分析/预测或serving SLO；不把近1的cosine当退化空间唯一性证明，也不按两列median之比争论未披露聚合方式。T9“relative cost”只按query-shot数/256定义，未包含训练全部gallery/encoder、原模型labels、分解/cache/index与验证全费；64→128的Hit@1/NDCG实际下降，预算增加不单调。必要主表计时的完整hardware/shape组合、全链费用与不确定性在所读范围Not Disclosed；不授93×端到端降本。作者limits承认固定base/layout与standalone adapters，未覆盖merged/composed/dynamic组合；本次也不授intent、安全或生成内容认证。

## actual owner / 具体差额

sole `TRAIN-LORA` Ch30实际178–238完整相关链（被输出截断的211已另次定点补读）：191–193已有QR小core谱压缩及矩阵误差非任务质量，201–209有effective-rank/optimizer gauge与紧fiber，211开始局部后验。尚未承载“训练后方向/幅度按位置token化，checkpoint-level监督预测/检索作为consumer，表示等价与预测权限分开”的接口。不能把既有QR原理写成本文原创，也不能仅按LoRA主题NC。

Ch59实际88–120已拥有base/rank/module/runtime资产身份，以及weight-only主方向risk sensor的threshold/abstention和统计分类非行为权威，但没有此完整低秩方向token与质量/任务检索consumer；Registry仅交接版本化资产，不新增第二owner。Ch29实际1230–1244交接SFT→参数化→偏好，以及Ch31实际1–42的偏好监督交接已对齐。建议Ch30现209后/211前单段，接同权重多因子自由度，随后仍回到几何不确定性；不动旧有效谱压缩或后验段。

## 逐字 PRE（未授写，待 root 非准备者裁）

同一权重的多种因子表示，还会影响训练后怎样比较adapter，而不只影响优化。一个[受限weight-to-token分支](https://arxiv.org/html/2603.15990v1)先从低秩因子恢复更新的奇异方向与幅度，再将每个位置的方向和幅度编码成token，经rank与layer/module两层聚合，用checkpoint级监督学习属性、质量或检索表示。小core分解保留的是更新矩阵的谱；非零奇异值互异且符号固定时，可避开raw因子的坐标自由度，但重根的子空间旋转、零方向与数值约定不能只靠排序和符号消除，未锁定这些条件时不批准唯一canonical token。表示相同也不等于换基座后行为相同，实际base、缩放、target modules与特征版本仍须绑定。有限质量预测只覆盖所测checkpoint人口，按task identity检索也不证明选中了能力最佳或安全的adapter；离线adapter/标签构建、encoder训练、分解、索引与独立行为回归均计费。谱条件、域外校准或检索质量不稳时，应保留普通LoRA、来源明确的固定adapter及加载后的直接评价，而不是让weight embedding替代发布验收。<!-- source-family:SF-2026-ARXIV-2603-15990 -->

静态注：`SF-2026-ARXIV-2603-15990` — [exact-v1](https://arxiv.org/html/2603.15990v1)§3–5/Eq1–7/Tables1–5、A.1–2/B.1–3/Tables6/8/Alg1与C.2/Table9；官方main只定点canonical helper，不冒实验commit或完整实现。仅训练后checkpoint-token consumer及简单谱/监督人口边界，不采重根唯一方向、普遍能力/安全或端到端速度保证；未核artifact执行或复现。

## root 非准备者 Source / actual owner / PRE

root独立实际读取exact-v1完整题摘、§3/Prop3.1–3.2/Eq1–2、§4/Eq3–7、§5.1–5.4/Tables1–5/Limitations、A.1–2必要证明、B.1–3/Tables6/8/Algorithm1及C.2/Table9；支持与直接反侧足够，停止扩读。实际顺读Ch30 178–239的谱压缩、optimizer gauge、局部后验及Ch59 84–121的资产/sensor边界，Ch29结尾与Ch31入口交接。2+2+2=6保持。I₂重根旋转反例成立，排序/符号不授唯一方向；PRE明确只给简单非零谱、学习consumer与监督人口，未把SVD代数变成能力/安全或成本证明。原§4低秩方向token、两层聚合与checkpoint监督具有独立具体差额，不是既有压缩原理再命名。Source、soleTRAIN-LORA具体差额及上面逐字一段PRE通过，可采用该有限接口。root本次未独立核官方main helper，作者的具名局部artifact观察仍只属于其记录，不授root完整实现核验。仅授resume_mar17 Ch30原209后/后验段前这一段及静态自身注窄写，实际非writer POST仍待，未计safe或DAY。

## root 非writer实际 POST

root实际顺读Ch30 195–224完整placement/optimizer gauge→新211→局部后验/共享邻接，以及960–972静态本人971和相邻源注；新211与上述逐字PRE一致，family仅正文及本人注两处。回对root已独立读取的必要v1，简单非零谱与退化旋转、监督人口、task-identity检索不授最佳能力/安全、完整离线费用和保留直接评价均准确。静态注实际采用范围和作者具名main局部观察限制保留，不冒实验commit/完整实现或复现。限定diffcheck通过；一次nonwriter实际POST PASS，root接纳释放Ch30窄锁，可计本项有限整合，不授全日DAY。

## 一次精确重开请求及当前停止

只请求一次：与实验对应的artifact commit及重复/零/近重根的basis固定化、mask/padding与缩放语义，等价因子在有限精度下逐token/最终embedding的最小trace或对退化子空间不依赖basis的表示；独立新task/base/rank与主动扰动评价，以及同标签人口/质量约束的adapter构建、label evaluation、encoder/index/验证总预算和不确定性。可由受限证明、勘误或最小可检artifact替代，仅重开未采唯一性/外推/成本主张。准备有限PRE不授其通过，争议不能用降分/EX/假NC消除；root裁是否此受限interface足以独立采用。当前未写Books、未POST、未计安全或DAY；不扩发现或下一日。
