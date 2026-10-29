# Sep20 必要core有界补读

作者Meitner。补窗Sep19完整BJT自然日；P为准入潜力而非日期/Evidence通过。只围绕安全、负面或决定准入的事实读核心，不遍历附件。原件`SUP_CORE_<id>.raw/request.json`均保留；HTML失败保留后PDFfallback，不以摘要替正文。

| exact v1 | 实际读到 | 实际增量/反侧与P理由 | 未读/未采用边界 |
| --- | --- | --- | --- |
| 15114 | HTML404；PDF p4–10 Method/Table1/Fig2–3/discussion | P：固定首句四条件minimal pair，混合效应含test-item；C2语法错误与C3语用异常差异不显著，C4语义异常较高，surprisal不能独有归因语法 | 不显著不等正式等价；四模型局部，不授所有LLM无语法能力；非全PDF/所有附录 |
| 15159 | §3/4.3/5.1/5.3/5.4/7 | P：instruction与5poisoned docs联合GA优化，非只改instruction；医学DPR另finetune，其他未调，top-k变化连同clean accuracy改变。Table4 top3 ACA61.90/top20 90.47；Table1 ACA60.32不足支持无损 | static RAG/知识库可写+prompt采用的威胁权限；自然性自动judge问yes为坏却称higher better的定义冲突，未人核；现有三检测有26.67/33.33%检出，未来建议非验证防御；未读全部GA/附录实现 |
| 15206 | §3.1/4/5/AppendixF | P：paired StereoSet 4212校准+偏差gradient/Hessian，4bit/group128，attention out与FFN down修正；Mistral ALL Cooc88.03反而高于FP84.33/GPTQSS82.34，不能所有metric统一改善 | OPT/Mistral/英语短句/单A10080GB；量化时间OPT6.7B7.98→10.40、Mistral8.07→10.59分钟，非免费；无多语言/长文本/部署公平保证；未读全部证明 |
| 15293 | §3/4/5含Table3/5/6，截断中段已再定点读 | P：最终answer与10维reasoning rubric分开，Cosmos final较好不等reasoning较好；视频/8frames/middle改变输入信息，不仅模型排名 | Qwen生成QA/trails后人工删约12%；50题3volunteers不能等全面reasoning faithful/真实robot safety；固定judge+另一judge近似不等oracle正确；8frames/长视频32，4096tokens受closest limit |
| 15335 | §3.3/4/5/Limitations | P：German fact-consistent词替换，3677原claims约25.3%留，6API各3次，judgmental词负效应比政治方向更稳定；objectivity prompt不稳定消除影响 | political annotation低一致/annotator偏向；拒答o4-mini21.2/24.5%、Maverick objective92%剔除，非模型普遍政治立场因果；无全语言外推/全附录复核 |
| 15336 | §3/4.1 | P：4process标准/逆序/label-shuffle、text/log与strict prompt对照；strict将text知识回归27→13/log20→10但不消失，结构log也非免疫 | behavioral footprint相对3groundtruth最相似，不是formal conformance/绝对正确；ProMoAI固定activity vocabulary、手工描述生成；未读所有模型明细/附件 |
| 15339 | §3.2–3.4/6 | P：sBERT仅question信息也AUC>.70，domain/type refinement降低但保留shortcut；须重考虑hidden-state hallucination predictor等于self-awareness | AUROC贡献相减只是近似，假设小sBERT知识与主模型独立/问题信息同等并非证明，不能将差值等于因果self-awareness；只知识回忆，不授reasoning/longform；未读SCAO全实验 |
| 15151/15154/15557 | Cicero独核§4及实际后批core记录 | 分层复用同日实际核心；15151 FX方向模型特异，15154 pseudo-SFT与GRPO独立/联合失效条件，15557 OOD格式proxy reward hacking反侧均P | 不授原标签真情绪变化/临床事实reward/隐藏think因果；本人不将复用称新全文深审 |
| 16244 | §3.1–3.5/4/Table2–3，同日Cicero§3，current history/comments已轻读 | P：PQC adapter不是仅综述；PennyLane经典模拟4090，100Alpaca生成/1000步loss，SoRA BLEU正文2.67/表.67及ratio.09/.10冲突 | 无量子硬件加速/足够训练匹配/端到端收益；仅决定准入；current仅v1，所读页未见W，不授全站修订史 |

| 15435 | §3.1/4方法设置与Table4–6/5；主结果中段已定点补读，Cicero§8实际§4.2完整 | P：一致性冲突触发跨模型attribute query，最高3迭代，最后仍按trace判断；转移攻击而非ORCA自适应攻击，JPEG下mPlug CHAIR18.50→20.70反降，约33倍慢 | Cover recall metric主动省略，3个旧LVLM+4辅模型增加预算，非单模块因果或无代价防御；一致但共同错仍未解；不扩全附录 |
| 15711 | §3/4.1/4.3 | P：CLIP冻结主干的双stream adapter及测试labelled fewshot feature-bank；CDFA86.0→联合91.6，未见generator1000fake+1000real无更新86.6/89.4加fewshot再+2.1/+2.7 | 测试额外labels与cache成本不能同零样本baseline等同；§3noise/spatial变量s/n对调，非临床安全/全新生成器免疫；未读所有dataset/raw图片/实现 |
| 15932 | §3/4.1/4.2/6.2 | P：bounded loss、iid两级Markov反馈channel+task-specific loss/index link给codebook-mixture Bayes/minimax下界；认知/表达min只是上界不一定联合可达 | 不自动实证human容量/真实RLHF风险，需验证每任务Assump2、报告残余rho；未读PAC-Bayes全部证明/附录，不授普遍安全不可能定理 |
| 16072 | §4/6.3–6.4/TableII/7 | P：相同task内instruction swap负例与跨层FS投票；模拟直迁real recall.3188/F1.456差，real-head训练recall.6957/F1.730才恢复 | 3head等权+VLM权2，二阶段专门监督不是泛zero-shot可靠；离线轨迹检测非online safety shield，未读全real数据/实现 |
| 16088 | §4含Theorem4.1–4.2/6/Limitations | P：oracle语义class将生成RS化，image noise/text固定；二类flip、iid采样且同epsilon误差模型才有q→p公式，不是任意平均error<.5即保语义安全 | Gemma2-9B oracle未实证所有条件，prompt7无法certify；LLaVA1.6 sigma.5 alpha.001/4A10040GB，100sample2.8s/1000约38s；并不保证文字扰动/多类/现实attack；其余证明未全读 |
| 15356 | §3/4.3/Limitations；结果中段已定点补读，Cicero§8实际§4.3完整 | P：31binary tabular+285 masked proxy，201分位数XGB按dataset分组5fold；score variance可筛task但有明显outlier，4o与小模型不同 | tokenprob API/固定prompt、公开数据潜在memorization、proxy任务不独立；threshold提高selective AUC不保未知域calibration；未读全附录 |
| 15482 | §3/4.1/4.4/5 | P：四TCGA癌类50kpatch/5non-overlap batches RSA；相同DINO训练范式不保证表示相近，stain-normalization slide-specific减少5.5–20.5%也减少disease-specific | batch range不是全institutions置信/因果；训练data/规模/architecture不同，RSA不等下游accuracy/隐私保证；未读所有spectral及附录 |
| 15980 | §3.2–3.3/4.3 | P：AF比较most/least relevance扰动error归一差；FE.93可能AF-.01，同ASR/FE也AF.49 vs.32，常规指标不能独有归因解释有效 | 相对原prediction非groundtruth correctness；黑mask/Gaussian/FGSM条件，分母0未在所读定义处理；非对所有explainability给faithfulness保证/全图片复核 |
| 15803 | §2/3/4.2–4.3 | P：brand-feature替代用CLIP相异与语义双score，w过低换brand/过高失去连贯；cache减call需warmup重复bias | 220人工prompts/4T2I/Gemini2.5Pro，DALL-E过滤强被排除，human N未披露；自身BNS也由VLM judge，front-door条件未验证，Eq2非直接因果识别保证；未读所有图数字 |
| 15968 | §3.3–3.4/4.2 | P：closed-loop failure replay的人类takeover动作与模型失败pair训练，Bench2Drive SR/DS增加但efficiency/comfort不全胜 | 不是实车安全；Eq3已sigmoid Eq4再sigmoid且未标准reference log-ratio，保留实现未核冲突；无explicit reward不等免reward hacking；未扩appendix/代码 |
| 16058 | §4.3/5.3/6 | P：noisy/OOD视觉控制与pretrained DistilBERT只last-layer VQVAE避免所有层random插入扰乱；5seed GLUE STSB/QQP差异不全显著 | 非all-task保证/认知意识证明；CIFAR-C/Tiny-C/syntheticshapes不是adversarial security；未读全资源调度实验/附录 |
| 19364 | §2及AppendixA方法首/后段（survey长段未全读） | P：400ChatGPT+400Gemini US四群体field、13prompts与API/sock-puppet；field更异质，Profile又过度异质；514MMLU模拟有变但没有field全benchmark | memory/custom instructions真实体验混杂，4benchmark问题purposive非random，模型UI/API对齐靠作者声明，不能把全差异因果归于personalization/把10runs当800全MMLU |
| 19371 | §3.1/4.1–4.2/4.4–4.5/Limitations | P：137M–3B从零、58/75/100B固定budget内频次10–10000，过量infusion留存下降；collapse点由拟合外推，tokens增大阈值后移 | 28,108triple MC perplexity非自由回忆；exactsurface过滤未去paraphrase，10/100模板结果规模特异，无3B以上大模型普遍law/生产knowledge安全保证 |
| 25534 | §3.2/4/5.1/AppendixA.4 | P：policy自身rubricGRM省外部评分，弱grader给Qwen.288/GPT4.1给.147；同GPT4.1外评self.500>baseline.446局部 | GPT5.462来自外部发布不是本研究matchedbudget；movingreward不可直接对比，longer response改善completeness但communication变差，physician MF1是rubric grading非临床能力；未读全部training/图复现 |

| 15759 | §2/3.1/6.1/7 | P：group-aware Bayes classifier，Gaussian类/群的moment/prior约束给exact fairness；Bios Llama2-7B moment steering是近似实际应用 | 多类Prop3.2为充分条件，二类univariate Prop3.3才iff；finite-sample预算/近似保证未来工作，非现实公平无代价，未读所有proof/joyfulgeneration |
| 19368 | §4.2/5.1/5.3/A.1 | P：verify-while-draft复用pipeline而非等draft后verify，低acceptance/长draft的EESD退化反侧；exit-head结构改变acceptance与负载平衡 | batch1/max512、多GPUworkers/蒸馏早退头，AR质量仅称理论未实测；alpha0等AR忽略通信/imbalance，非任意资源无退化；未读全执行图/代码 |
| 19369 | §3.3/4.3–4.4 | P：Korean-first schema/value白名单与有限replan，single-chain95.6%但multi-chain33.8%、missingparams66.6低于76.8；role separation成立条件而非单leaderboard | 总TSR+0.4pp作者承认不显著；4360tokens9.1s不胜GPT4mini3747/7.9，也不胜Qwen8B6.1s，API cache推测未控制；未读全dataset/实现 |

| 15602 | §4.1–4.3/Table2/5 | P：Qwen2.5VL7B 32frames总体39.4→64frames38.6，AvgRS39.5→38.5；reasoning主要帮助RC/HD而非fine temporal任务 | closed APIs因budget1FPS而open各VideoMME采样，不全模型公平排名；同backboneRL还改变训练，不唯一归因推理本身；无全部domain外推 |
| 15419 | §3.2–3.3/4/Table1–2 | P：268/50%/100%嵌套train、4checkpoint300epochs，早峰空串/negated诊断，dummy precision.62/recall1可近似早峰；大PegasusX较差，继续训练可后期恢复但10%未验证 | 4A40/hyperparameters已披露但batch不统一，模型参数§3 272/568M与§4 257/512M冲突；double-descent/530epochs预测为conjecture，非普遍模型规模反证/临床质量 |
| 15957 | §2.4/4.2/4.4 | P：6tasks/8patients每prompt10次、accuracy exactgold/Dice；工具选择全对仍参数窗口和长response解释失败 | 单机构/小样本、人工error分类无完整uncertainty；未核MCP权限实现/全部日志、真实诊断generative/reasoning未测；结构输出无format error不等语义可靠 |
| 16256 | HTML404→PDF p3–6 §3.1–3.5/4/Table3–4 | P：5000YouTube混码评论/三annotators、TFIDF树89.71vsBERT79.7/RoBERTa76.6局部结果，英文BERT-base-uncased/3epochs可能不适低资源 | §3.5称所有10fold不partition，§4却Transformerheld-out test；可比协议冲突且TFIDF fit-before-fold未澄清，std称报告表未列；不授树普遍优/同预算公平因果/无leak，未读全九页 |

决定准入N由Cicero实际必要core分层复用其§7：15366/15479/15490/15566/15596/15635/16006/22688/25203/19365/15984均P，读到位置及具体反侧以其本日唯一note为准，不称本人重读全篇。15695状态R不扩大方法；16054wholeW排除。明确P但date未证停止进一步全文；MiMo Books实际一段+自身SF整合及Cicero§10非writerPOST已通过，普通仅完整六部分DAY/完成态FINAL，本表不自授日级通过。
