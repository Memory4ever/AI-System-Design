# 已准入五项的匹配证据与 Books 提案

本日作者的精确 v1 标准审阅；原文选择段见同目录 CORE_STANDARD_<id>v1.txt。不声称实现核验或复现实验，非作者仍需独立核。日期用 DATES.md 对应 submitted-batch 下界与各自 DataCite 创建上界，不伪造首次公开秒。

## FineInstructions — 2601.22146

采用命题：在相同文档和训练 token（含chat template、余量rollover）下，将文档转换成匹配真实查询类型的 instruction-answer objective，改变训练接口而不是单纯增文档。2+2+2=6。§3.1–3.4实际包含查询模板、BGE-M3两轮compatibility训练、global+5 Gaussian局部pool、0.865匹配threshold、3B实例化、至少80% answer excerpt及FlowJudge≥4过滤。§4.1–4.3对照是在同文档与token预算下；不同原生格式/dataloader、teacher和过滤仍共同变化，不能把Table1全部收益归于模板多样性。IPT23B四epoch与Nemotron300B一epoch分开，不能合并为同训练预算跨corpus。1.8B Lingua/Llama3 tokenizer、8H100，precision、真实数据生成全成本、并发/SLO未披露；SLO不适用离线训练。

§5 Table1 IPT standard→FI MixEval17.8→31.7/Hard14→19.2，Nemotron24→33/17.1→21.8。MixEval2024-08-11、MTBench101单轮用GPT5mini judge、AlpacaEval用GPT4Turbo长度校正；不是独立人类真值。§6.3复杂模板匹配/实例化失败、长输出使logprob短选择题评分失配。§6.2提到judging ablation但未核具体表，不使用其精确增益。

Books拟仅报告：Ch27实际正文150–185已承载format vs内容、teacher/lineage及matched-token patch验收；本篇提供一种局部可复现生成recipe，未能单独证明哪项模板/过滤选择是长期必要条件。不声称Ch27已有具体FineInstructions算法。需root核这一窄采用边界。

## Shepherding — 2601.22132

采用命题：将strong model调用从二元路由改为partial-prefix hint预算，且小模型可承担剩余生成；2+2+2=6。§2.2–2.3/§3定义teacher输出0–90%候选prefix、classifier+log(1+n)hint回归、长hint转全路由；teacher错/全部hint失败样本被过滤，不能赋一般纠错能力。hint长度质量非单调，训练supervision的最小值是oracle，不是可部署精确知道的需求。reactive先3次SLM生成取共识，最终结果7trials/majority需与额外资源一并解释。

§4.1–4.4 Llama3.2 3B本地RTX5090、Groq Llama3.3 70B历史input/output价格；本地SLM费用假定0，不是完整资源成本。GSM776/CNK2147/HumanEval164/MBPP500；policy在GSM训练，code不另FT。Table1 GSM reactive89.1%/$0.034 vs ABC94.9%/$0.048，不是相同精确质量；§4.3约束90%teacher质量时比较各自有限operating points，不证明完整Pareto。HumanEval76.2%相同点成本0.013 vs0.019；MBPPreactive67.2%与ABC67.8%也有差。CNK局部每次SLM384.62ms，reactive3响应1163.48ms+policy7.32ms；所谓159×只decision阶段，不含remote/network/end-to-end。precision、并发、完整SLO未披露。

Books拟仅报告：Ch70实际45–135已要求cost_to_quality目标、所有推理工作与measured/resource账本；本篇可作为partial-hint operating point实验，不把零本地成本模型或有限阈值提升成稳定部署选型规则。不称现有书已有hint算法。

## Value-Based Pre-Training with Downstream Feedback — 2601.22108（精确v1原题名）

采用命题：labels只产生detached downstream gradient，designer改变当前unlabeled self-supervised target，learner不直接更新于feedback labels；2+2+2=6。§3.1–3.3 topK softtarget混合与HVP alignment、部分参数scope控制二阶成本；不采用§3.4/附录理论界为本次证明。

§4/A.1 Qwen1.5 .5/4/7B、NuminaMath-CoT answer-only、1024seq、AdamW cosine/warmup、bf16；五LR选择双方best，固定learner-step/tokens而非总wallclock。GSM1024训练例只供designer；vision feedback512ADE+512NYU。§4.5 random gradient、uniform topK smoothing/selfdistill，4B GSM54.31/54.58/57.61 vs value58.98，decontam57.5 vs56.7。Table2 .5B MMLU38.08→35.01、7B OMEGA1.52→1.50、OxfordHard .0867→.0820，不能照作者aggregate说没有损伤。单H100 Table3 throughput45782→38491、step.7157→.8513、peak15.71→16.38GB；具体代表size/长训/E2E未在所读段明确，不外推。SLO不适用离线训练。

Books拟已有覆盖：TRAIN-PRETRAINING / Ch28正文155–168实际写downstream detached→candidate target gradient→alignment→learner only unlabeled，并明确非无条件unsupervised、feedback/designer/approx身份和general能力代价；不是仅参考列表命中。无需新增diff。

## MetricAnything — 2601.22054

采用命题：不同metric sensor/data先进入depth+validity mask，再用稀疏pixel/depth prompt的共同中间域接口，让metric约束可跨采样布局；2+1+2=5。§3.1–3.2 PDSA/GMDR沿用既有prior depth，conditioned DPT约5%参数、共享ViT；20M来源/相机规模不是本次评分。real损失去top20%噪声区域，synthetic MAE+SSI-MAGE。不采用prompt-free student/VLA/MLLM全部后续链。

§4.1.1 Table1三未见dataset四prompt类型，只支持局部稀疏prompt迁移，不是所有格最强：NYU16×PromptDA1.75优于ours1.86；NYUExtreme PriorDA2.01优于2.08。§5.6 Hypersim500→64000point AbsRel .043→.031，同时224→308ms，是density-quality-cost局部取舍。§6.1三camera24Hz/128-beamLiDAR10Hz、无motion compensation仅可视证据，不证明安全或定量时序鲁棒性。§7.1声明源dataset完全不同、ScanNet单exception；§7.2 144H200100ksteps/warm10k，backbone1e-6/head1e-5。§5.3单帧H200FP32 native1536² teacher285ms vsDepthPro246ms，不能照文字称无延迟增加；concurrency/SLO未披露。§8中心投影camera假设，非nonpinhole通用。

Books拟仅报告：现有Ch23具有单位/坐标/calibration/time/provenance接口；本次commonprompt的具体recipe及density取舍仅在深度任务核验，尚不足将其提升为跨模态普适新范式。不称已有正文覆盖此算法。

## Leviathan — 2601.22040

采用命题：词表输入不必保留每token独立宽row，可由id组合codebook+非线性generator生成embedding，将释放预算重新配置body；2+1+2=5。§3确定性base59³三索引/177entries→128D→dense/LN/sigmoid→32-knot rank1/M8 Bspline→residual输入，输出仍untied densehead。固定tokenizer/token流、AdamW/JAXFlax、PileUncopyrighted512seq×512batch；iso-body tiedDense vs untiedgenerator/head有归因混杂。iso-param例109M6layer vs108.5M52layer不是isoFLOP。

§4.4–4.5 sampleefficiency/fittedDenseequivalent只属于四Dense拟合和局部scratch规模；不采用未核irreducibleb迁移为定律。§6 iso-body吞吐降51%(60M)→23%(410M)，iso-param降48–71%主要深度串行；词表几何由id任意顺序，不保证语义近邻。具体hardware/precision/runtime版本/concurrency未在采用段披露，SLO不适用训练。可将generator当新的预算分支，不能称无成本替代lookup。

Books实际整合：Ch12原正文185–219只有线性factorized E×P及秩/投影/共享head边界，root独立核认为非线性共享id→生成输入表示构成具体长期接口缺口。获PRE唯一窄锁后，作者重读Books必要上下文与Ch11/12/13交接，只在factorization之后补正文227/229两段及末注367；root实际POST通过，词表输出头指代修正后实际回核通过，锁释放。未扩其他机制，未stage/commit/push。其余四项的必要证据与具体Books决定也经root实际通过：FineInstructions/Shepherding/MetricAnything仅报告，VPretraining Ch28实际已有覆盖；单批通过不授日级完成。
