# 四项必要证据与当前owner判断 — 待root核

所有exactv1，未核artifact/复现；必要源缓存同ID `v1-primary.txt`。准入已通过，不按Books/workload改分。

## 10460 Contextual StereoSet — 2+1+2=5，具体控制差额深入，拟Ch66

实际§4–5 L159–186：同三选项/内容不改，hash(probeid)固定选项排列，context维度location/year/style/observer交叉360，budget72+两baseline。构念明确是“多数人觉得typical”的stereotype selection，不授内在belief/歧视行为或地理真实文化；English地点mention测prompt sensitivity。item bootstrap、permodel六primarycontrast BH-FDR，非context副本当独立人口。§6.1–6.3 L187–308：fullgrid50items、T0/.7/1六model；budget完整4229items八models；有效parse≥99% inclusion条件，coverage须与行为分账。语言本土synthetic的SS≈0可能capability不足，不证明少bias；translatedHindi/Chinese contrasts BH后无显著。Table5 L435–490给局部不同cue方向，不外推allmodels/alltasks causal规律。vignette L128–141明确exploratory/non-audit。模型API/precision/runtime/e2ecost未披露，360/74倍调用和translation审核不能省。

原提取器在Table9中间L743截断，不是官方HTML缺失；同exact raw有完整footer，移除script/style block后无全局skip的提取器已恢复64341字符到footer，另存`2601.10460v1-primary-recovered.txt`保旧证据定位。实际新增核§11 L870–879：StereoSet label非groundtruth/ambiguity，Englishmention非真实culture，alignment与pretrain相关机制未归因，validlabel条件分母，APIerror/parsemissing而非refusal，authorrequest artifact不可授已复现。Ch66实际L404–410现有semantic-equivalent prompt spread与polarity label mapping，不包含固定内容/typicality构念下context factorial+paired contrasts；拟framing极性后两短段，context并不都target-preserving、低SS不授公平、item分母/语言能力/成本与固定baseline退路近正文。非新增benchmark规模/新地区名称计分。

## 10496 Exposure-aware bug/fix — 2+2+2=6，测量接口差额深入，拟Ch66

实际§3.1–3.7 L110–193、§5.1 L461–471/§5.3 L482–490、§6.1 L505–516：16899Java单语句pairs，Stackv2portrait为candidatecorpus signal，不是每model真实训练记录；3/7/15BStarCoder2、Mellum4B及SmolLM3的额外数据/分词支持不同，不授size/trainingcausality。50char ngram/stride50、padding99、badness≥.9给四proxy exposure cohorts，Bloomreported.1%collision/striding/context/partialmatch和其他corpus未知都保留。作者L156 padding覆盖公式未采用（右侧可超过实际sample长度）；短变体共享context/variant归属须另核，不能把portrait hit认证bug/fix真membership或memorization。

Likelihood metric配对相同prefix，仅varianttokens，方向/length不同；并列实际decode：maxprefix2048、5独立completion、T.8/topP.95/max64，exactstring分fix-only/bug-only/mix/neither四互斥人口。Neithermatch不是正确、fixlikelihood高不是已交付fix、no-FIM/fullproject未知。RQ1equalXOR1109/arm属balanceddiagnostic非原deploypop；min/maxprob与Gini/arithmetic方向受exposure条件改变、decode更常逐字bug只是所测Java/proxycorpus关系，不授causal传播/production漏洞率。两A40 48GB/AMD EPYC9334/256GB；precision/concurrency/e2ecost/CI未披露，不凭literalcode相同认证可运行。

当前Ch66 L484–486真正具体区分corpusprovenance与outputmemorization sensor，但未承载bug/fix四jointcorpuscohort与likelihood-vs-realdecode四结果接口。拟此后两短段，把membershipproxy、conditionalpairscore和固定5draw outcome分责，slice/预算/target语义及unknown/fullproject回退近正文，不采用作者paddinglemma或总bug率。

## 10497 MergeTune — 2+1+2=5，标准完成，拟OnlyReport

实际§4 L114–154/Eq5–9、Alg1 L1950–1986、§5.2–5.3 L1310附近、A1 L1919–1940及Tables9–11 L2560–2630。两条endpoint→w的pathloss目标，预训练数据缺失时假设grad≈0/H≈muI退成L2anchor，downstream真实loss+interpolatedpathloss，非实际估计Hessian/真实pretrainloss保持证书；低有限点损失/高accuracy不是全path无lossbarrier或全knowledge保留。prompt设置w=T(p)为derivedclassifier，不自动全模型parameterconnectivity；adapter结构差异仅merge linearheads/保encoder。有限CoOp/KgCoOp/MMA/PromptKD16shot/11dataset，新增continuedtraining同recipe但额外epochs，3090mixedprecision；alpha5约3x/10约5x/15约7x相对KgCoOp成本不是freeposthocmerge。Table11beta0降低base但novel73.61略高full73.60，Table10endpointloss独立提高HM却novel74.26→73.60；averageHM提升不授逐slice无forget。参数继承为何因果不成立，n=5/10离散loss和λ/β局部控制只支持CLIP配方。

Ch29实际L825–835保护gradient/optimizercommit及base生成proxy≠旧真实function，Ch30 parametermerge L270附近已有矩阵/behavior差别；长期“参数代理不认证旧function/质量和费用回归”的边界已有，但本论文具体双endpointloss只是局部继续训练recipe，无新的已验证普遍机制，拟OnlyReport而非假称已有本实验/全path。若root认为确需长期gap，应先实际指定唯一owner和窄采用命题，不借LMC成熟原则加分。

## 10416 LLMdoctor — 2+2+2=6，中心配置争议拟NoBooks终态

实际§4.1 L124–142：同patient两behaviorprompt的绝对logprob差→均值norm/tanh→sparsitythreshold→继承response preference符号，不授token因果/独立reward真值。§4.2 L143–180/Eq6–12：SubTB的F=Q(prefix)V(prefix)对所有subtrajectories匹配概率积，Q只被称“positive weighting derivedfromtokenrewards”，未给带正负r到Q的具体map；V需进入log但正值parameterization/terminalboundary未定义。不能自补指数/累积Q或授flowconservation/diversityproof。§4.3 L182–195：patient/doctor两全vocabprob product，多objective可调β只算控制接口，不授安全priority或相同tokenizer自动成立。

实际§5.1–5.7 L197–333、F L789–837：LLaMA7BSFT/Tulu7/13/70、doctor7B、HH112k/12.5k但main300randomprompt/GP4ojudge；Table2 full61 vs noSubTB53.15/noValue58.23/noSparse56.58/noFlow52.76局部wins半tie，不是事实或害处保证。基准不同预算16RS/10ARGS/segment16×8等未matchede2e；通用LoRA16/.32/drop.05、AdamW5e−6/3epoch/B64accum4，与F2DPO1epoch5e−4版本不同，不合并统一训练预算。hardware/precision/e2elatency ND。NoSubTB把局部proxy变不同目标，胜率不修复未定义Q。

当前中心TFPO具体目标不能依据公开正文完整构造，已作有限sameprimary定点Q/implementation定位，不把optionalcode缺失阻塞可支持的promptdiff/product局部事实。拟Disputed安全终态NoBooks，不采用中心TFPO机制/理论或已验证rewardidentity；重开需作者提供Q正值map、V正值/terminalboundary和与实际设置对应的更新公式/官方实现。非普通未读Blocked、非改4分删池，现有Ch20tokencontrol/Ch34preference与Ch33credit不补造新source。
