# Discrete Feynman–Kac Correctors 10403 — 必要证据与owner差额

2+2+2=6。新增命题仅 frozen masked diffusion 的 inference target→rate/weight/resampling 接口，不把CTMC/FK/SMC成熟基础计新贡献；该具体owner缺口必要深入。exactv1 primary `2601.10403v1-primary.txt`；未核artifact/复现，未采用完整收敛证明/精确有限粒子宣称。

实际§2 L116–169、§3.1–3.3 L170–231、Alg1 L232–253：annealed/product/reward-tilted marginal target要求同时改off-diagonal rate与g-weight，不是只改denoiser token logits。Alg1 finite dt Cat(delta+Bdt)→logweight加gdt→SNIS重采样并reset1/K，合法概率仍依赖rate/step；learned posterior ratio、finite粒子/时间离散近似不可授target exactness。product每条件forward，rewardtilt需所有可转移states reward，替代difference reward仅futurework。这里理论只辨明目标/算法对象，不采用未独立核完整proof。

关键语言评价§4.2 L291–303和D.2 L1404–1418、D.3 L1443–1465：LLaDA8B-Instruct，code A100L/128token，HumanEval与sanitizedMBPP各10prompt调M={2,4,8}/beta={3,5,10,20}/remask，最终M4、HEbeta10/MBPP20、random；余154/417题，5seed SE，accuracy以最长无syntaxerror片段解析并sanitize后testcases，不授完整repo/任意输出。HE33.78±.97 vs argmax30.74±.76/naive30.49±.49；MBPP31±.40 vs argmax30.28±.87/naive29.24±1.07，局部差额非全面优越。naive就是M1、无resampling，M4增加population/cost，非matched totalbudget。precision/concurrency/fullwalltime/latency及base denoise-step完整配置未披露，不补实现。

Amortizedlinearregression单A100、128token、5subset/5particles由固定数据量网格选；posterior product依赖uniformprior且LM真实posterior未校准，parseable不等参数正确，curatedTableA3仍有严重错误；SMC收益非随samples无界增加，FigA1阈值8。storyPPL不能当constrainttruth。不采用protein应用成果（AI4Science暂缓），只保通用rate/reweight接口；奖励评价全states与多forward、粒子退化/样本多样性及realcost应独立验收，预算/ratio/schedule/quality不可靠回原sampler或固定guidance。

当前owner `MULTIMODAL-GENERATIVE-PARADIGMS` Ch24实际L971–979 reverse-target身份/CTMC rate×direction/λdt合法性，与L981–985 training tilt-matching：现有具体正文未承载 frozen模型 inference marginal tilt 同时修改rate与weight/多粒子resample，training局部target不可冒此接口。拟L979后、training tilt前两短段，分清score/rate proposal、sampler近似/费用、target density非事实/质量acceptance；Ch20是AR token温度非该owner。root核必要精确原段与owner后才窄写，不扩全proof/附件。
