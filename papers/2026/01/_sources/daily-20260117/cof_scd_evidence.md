# CoF / SCD：必要差额待 root 核

两项6=2+2+2此前root实际决定性方法准入；本批评价与actual owner核准备。未核代码或复现。正常公告/Submitted cohort且无先行正文条件下，以Jan16 01Z为公开下界，registered秒字段给排他上界，不把Submitted/Updated当公开。

## 10061 CoF-T2I

exact `2601.10061v1-primary.txt` actual §2.1–2.2 L94–121，§3.1 L251–257，Table3/4/5+§3.3 L342–460，C2 L941–957、Table7 L958–985和D限制已读。最小新接口：三帧progressive target以各帧单独进入Wan VAE初始一帧window编码，联合latent flow生成全三帧，只decode末帧。**纠正早期准入简记“防未来泄漏”**：native VAE本来causal，原文直接论据是过去draft与后帧经 temporal compression耦合/隐含motion，非原稿证明未来信息泄漏；联合p(Z1:3|prompt)没有逐帧commit/AR或内部推理因果保证。

Table3同设置/步数 target-only .81、continuousVAE .83、独立VAE .86（Wanbase .55），足够支持受限 codec/中间监督差额但不是全部headline增量。C2连续codec须pad三帧成五帧(F1,F2,F3,F3,F3)，故同时改latent layout/序列长度，不能把.03唯一归因抽象“独立性”或证明必要性。Table4帧间均值.56/.79/.86非因果rollout，Table7Spatiotemporal中间7.317→末7.287反退，不能说所有子任务单调。训练Wan2.1T2V14B、64K合成chain、1800steps/B64/LR1e−5/WD1e−2/1024平方、freezeVAE/updateDiT；多generator/judge/反向合成不作为真trace，B2称Qwen3VL7B（模型名口径不据此造身份）。硬件/精度/seed/采样步数/CFG/端到端耗时及完整数据构造预算未披露；同step不等同同token/FLOPs。

actualowner `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24 L206–213已latentartifact/global/local分责，L407–421 TMD拥有外步/内步非AR；没有“联合三帧中间监督+单帧codec隔离draft耦合/terminaldecode”分支。拟Ch24 latent-generation分责段后两短段：中间state目标/codec边界→共同denoise/末帧输出，保连续VAE/paddedbaseline混杂/局部反退/成本/原T2I或视频路径退路。不在Ch23重写codec知识，不借reasoning名称给分。

日期raw：SubmittedJan15T04:33:06Z、UpdatedJan16T01:20:20Z、createdJan16T02:46:14Z/registered02:46:15Z；条件BJTJan16[09:00:00,10:46:16)。

## 10114 Scheduled Checkpoint Distillation

exact `2601.10114v1-primary.txt` actual §5.2 L149–160、§6 L161–188、§7.1 L189–207、Table1 L208–292及§7.2–7.5L293–311。旧fixedbestteacher/fixedcheckpointorder→每次选minKL(bestTeacher||checkpoint)+KL(currentStudent||checkpoint)；AW为sigmoid(log固定studentSFTloss/所选teachercheckpointloss)，混KL与goldCE。**AW的student anchor固定，不是当前训练student在线loss**；KL代risk差/最佳teacher距离是heuristic，不采risk证书。§4 SFS优势> TFS劣势只是分解恒等，不计理论新增/普遍学生超teacher。

同基础CDinfra/optimizer每Treset/N×Tsteps，Llama3.1 8Bteacher→Llama3.2 3Bstudent，max512/B8/AdamW(.9,.95)/clip1/cosine10%warmup/T2epochs/N按教师epochs等分、A80080GB；LR在TD gridsearch再共享，精度/seed/总GPU时/每次scheduleprobe和teacherpool驻留成本未披露。student取bestcheckpoint，未交代独立选取population，不授无选择偏差。Table1平均CD .739→SCD.742→AW.763，但JMMLU SCD.474低CD.482、RRTNM .538低CD.585，AW CRADE .807低SCD.819；AW PubmedQA.766仍低teacher.792，平均.763仍低teacher.773。有限NRNER超teacher不是domain通用定律；没有AW-only完整factorial，不能将全部收益独立归因AW。领域数据测试一般distill机制，不收临床成果。

actualowner `TRAIN-SFT` Ch29 L244–258有teacher容量/target选择/P-ALIGN/发布teacher校准，但没有保存teacher SFT轨迹后动态挑checkpoint并用固定studentSFT anchor分配gold/teacher权重。拟P-ALIGN后/teacher发布校准前两段，不改Ch35checkpoint存储owner：teacher目标identity+probe/schedule+lossmix为监督构造的条件分支；保持gold/局部counter/额外state与budget/固定teacher普通KD退路。

日期raw：SubmittedJan15T06:46:01Z、UpdatedJan16T01:24:25Z、created/registeredJan16T02:47:32Z；条件BJTJan16[09:00:00,10:47:33)。
