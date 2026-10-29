# Priority Mask 2603.15803：必要机制、反侧与受限 PRE

作者 resume_mar18；仅03-19补03/18自然日。2+1+2=5给标注span条件的biased masking/互补同批训练接口；涉及中心数学说法与知识差额作必要深入。[exact-v1](https://arxiv.org/html/2603.15803v1)§2.1–2.2/§3.1–3.4.4/Tables1–2/§4实际读；current abs仅v1/Ongoing work，无已见具体撤回/纠错，不以submitted当公开，日级夹证按本批限定复用。不遍references/代码，不冒图3/4全部点实际视觉核或复现。

## 支持与关键反侧

GPT4o读取instruction+target answer，离线按code controlflow/pivots、math操作/结果提取span，映射binary C；这不是实际测出的Shannon信息密度或正确推理oracle。AST/confidence/learned extractor是未来工作。p_prior=min(w p_base,1)、p_other=p_base，解平均mask概率等于sigma，只约束第一view的期望总量，不是每个实例恰好mask该比例。随后同mini-batch加入M及1−M，两view在每位置的平均遮罩为1/2；互补view的比例1−sigma，不能写两view都保持sigma或默认原ELBO timestep/weight已忠实不变。完整loss weighting/第二view时间身份未披露，数学保证不采用。

§3.4.1声称w与1/w诱导分布期望isomorphic不一般成立：未触clamp，rho=.25、sigma=.5时w=2给priority/base=.8/.4，反mask=.2/.6；w=.5给.285714/.571429、反mask=.714286/.428571，非同一mask pair分布。59.19与59.22局部接近不证明恒等或所有w对称。此处反例限定作者强命题，不否认两view作为可训练proposal存在。Soft比hard某些任务更好，但“保localanchors避免梯度陡峭/contextcollapse”只是解释，无gradient/collapse测量支持唯一因果，亦不证明真实逻辑/语法两能力被精确解耦。

LLaDA2.0-mini/dFactory/seq2048/globalbatch16/block32/sigma[.3,.8]/EOS可mask，测试max512/T32；450k OPC-SFT-Stage2+GSM8k一epoch，抽取子集与未抽取shuffle。正文通常10–30%与mainCode10%/Math50%分清，抽取teacher与prompt/mapping/失败处理、LR/optimizer、exact model/framework版、hardware/precision、trainingsteps、seed/repeat/CI、完整I/O/batch/concurrency/SLO ND。Baseline450k同内容有用，但同计算宣称未完整交代双view/teacher费用与baseline也否complement；不能以同样原始条数签等token/训练预算。

Table1 original58.10、uniform55.32、priority59.19平均；mainMBPP54<56.8、GSM73.92<original86.58，训练域/原模型不同目标不可只报+3.87全优。T2 code20%soft MBPP49.6<hard50，非每task全面更好；100%code HE更好而MATH低于10%，更多teacher先验不单调。没有独立teacher-span vs随机等长度span对照或全部budget匹配，annotation最低成本/不可或缺/普遍最优不采用。可支持受限训练接口与质量局部比较，不授contextcollapse因果或生产提速。

## actual owner 与待裁边界

实际Ch24 545–606完整objective/commit→reverse route→corruption/token time→locality预算→条件采样/AR迁移；Ch23/25首18行已读。soleMULTIMODAL-GENERATIVE-PARADIGMS，577–579确有locality但不承载annotation-span概率倾斜/互补view的身份与budget限制；不假NC，也不借高层mask主题排除。拟locality两段后/局部条件重采样前一段，但root/非preparer须先裁该受限mechanism可否与中心强证明精确隔离，尚未授锁/未写。不将“数学对称证明未立”改成普通没有实验。

### 受限一段逐字 PRE（待裁，不预支采用）

预测预算也可以围绕离线标注的关键 span 重分配，而不是只按 token 距离选择位置。一条[受限训练分支](https://arxiv.org/html/2603.15803v1)先由 teacher 从指令与答案提议关键区域，提高这些位置的遮罩概率，再在同批加入原 mask 的互补 view，让两份训练视图分别提供不同可见条件；标注不是信息密度或推理正确性的真值，双 view 也不是把两类能力精确拆开。第一 view 的期望总遮罩率约束不自动延伸到互补 view，其时间与 loss 权重、原数据和 teacher 版本必须单独冻结并计入预算；局部质量改善没有证明 reciprocal bias 对称、原 ELBO 不变或避免 context collapse 的唯一因果。更强标注比例与硬遮罩均可能反退，须在同数据、同训练费用与独立任务切片上验收；标注错位、域偏差或成本不合算时，均匀/混合 mask 与既有 locality 分支继续成立，不由逻辑关键字批准完整生成质量。<!-- source-family:SF-2026-ARXIV-2603-15803 -->

### 静态来源注（随采用裁决，不预支写入）

- `SF-2026-ARXIV-2603-15803` — [Priority Mask exact-v1](https://arxiv.org/html/2603.15803v1)必要§2–4/Tables1–2；仅teacher-span概率倾斜/互补view训练接口。总遮罩率、view时间/loss权重、teacher/全训练费与任务反侧近文，不采reciprocal symmetry/原ELBO不变、精确能力解耦或contextcollapse因果保证；未核全部图像点/代码或复现。

## 非准备者 Source/PRE 与窄锁

root实际exact-v1 §2.1/2.2、§3.1–3.4.4/Tables1–2/§4及actualCh24 545–615完整objective→corruption→locality→重采样、Ch23/25交接，独算rho=.25/sigma=.5/w2与w.5反例、两view均值.5，核T1 MBPP/GSM与T2 math反退和双view/teacher未匹配费用。限定Source/PRE正式通过，只将“两次更新分别读取”修为“两份训练视图分别提供”，不改变同mini-batch身份；授Ch24 locality后唯一一段与静态注窄锁，未actualPOST先不计整合安全。根源数学强命题不采，与受限接口精确隔离。

## 实际写后复核

root非writer实际顺读Ch24 560–600完整locality→关键span→条件重采样交接，新增581与本人静态末注2451逐字回对通过的PRE，核训练预算、双view、数学/因果隔离及旧分支；该家族正文和本人注共两处。限定diff检查通过，静态注不循环添加人员状态。实际POST通过，Ch24窄锁释放；本项可记受限整合，不授本日DAY。
