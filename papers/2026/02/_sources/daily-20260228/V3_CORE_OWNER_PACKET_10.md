# 第十包：AB7已校准六项必要原v1与实际owner

本包仅针对具名潜力，不扩大613宽库存/228命名切片，不重跑AB发现校准。作者已实际读下列关键blocks与具体owner；root独立PRE/窄lease尚未授，未改Books、未计safe。全文身份为各ID原v1，机械位置见同目录V3_BLOCKS_<ID>.md。原文获取与当前官方abs轻量状态见V3_FETCH_AB7_NECESSARY_A.json（2026-10-05T18:51Z）。当前comments：22689 ICLR2026 accepted，22697页表图数，22710 NeurIPS2026 review，22716 CVPR2026；其余未给comment。只核状态信号，不默认比较revision。

六原v1均于02/26 UTC提交，晚于02/25 19:00Z截点；官方公告政策所给公开下界为02/27 09:00+08，同ID registered为身份公开上界，不是技术来源或arXiv首公告。registered UTC原值依次：22689 02/27 02:52:19、22697 :30、22700 :34、22710 :48、22716 :56、22718 :59。各上界加1秒转+08后，全区间落本窗。原字段见V3_THEME_METADATA.json，原v1 Submitted不等于public；后续会议状态不另计本窗新事件。

## 22689 MoFit — 2+1+3=6，Ch72缺失caption下的成员signal构造

实际原30–46/48–70/72–104/140–155/183–189/222–234。标准重构比较会把未知caption误配混入MIA；这条分支先在固定noise/time优化image perturbation的unconditional噪声预测，再以VLM初始化caption优化连续condition embedding，但将其应用回原始query image，故意保留surrogate与原图的错配。直接在原图优化condition会同时拟合member/holdout、冲淡信号，是具体控制；caption-free不等VLM-free或普通生成API黑箱。Cond/uncond及辅助误差经median/IQR缩放，已知member/holdout仍用于阈值校准，不提供训练记录或授权真值。

SD1.4 Pokemon416/417、COCO与Flickr各约2500/2500有限fine-tune，后两者150K步过拟合；LAION-mi原对照都近chance，后以431个verified-memorized members替换，不能外推普通成员分布或把MIA等同记忆证明。Table3虽ASR77.61，AUC71.03仍低PFAMI78.15/GTCLiD77.83、低FPR检出也非全胜；LoRA分支AUC54.35/TPR0是直接限制，不签隐私安全。单RTX4090、数百至千次优化约7–9分钟/image，caption初始化、embedding优化和ground-truth校准均付费；色彩/复杂度造成部分FP，JPEG/blur控制不是所有变换鲁棒证书。无需读医疗应用/全部攻击代码。

实际Ch72 279–307已有loss/entropy控制可识别性、matched controls、Unknown与provenance，但没有**图像条件优化到surrogate后故意与原图错配，以及普通caption优化会同时削弱两类signal的反侧**。拟membership小节一段，采用white-box接口和overfit条件，而非高ASR；保阈值、人口、费用/LoRA失效与provenance/canary/Unknown回退。请求PLATFORM-SECURITY窄lease。

## 22697 InteractCS-RL — 2+1+3=6，Ch33逐轮混合credit与成本反馈

实际原50–70/82–83/95–108；截断62–70及95–97已补。终局用户模拟器satisfaction与GenPRM每轮0/.5/1原则分数混合，再减lambda×costly-action indicator；本条trajectory的全部turn rewards做均值/方差归一，不是同prompt多completion group。增量PID以avg cost减目标delta为error，累计到lambda后clip；PID本身是成熟复用，增量在于明确的session/turn信号与软cost multiplier如何共同改变多轮训练，不能把它叫token因果credit或安全controller。

Qwen2.5 7/14B、用户模拟/judge均Qwen32B、G4/B128/Tmax15、8A100训练/2H20评分为作者条件。标称V-rate<30，而7B测得30.8±1.4/34.6±1.9，故不是硬预算；14B27.5/28.7也只所测人口。去PID和固定lambda有cost/utility取舍，固定项utility更低支持反馈分支，但不能签精确constrained-optimal。SFT与领域迁移部分退步、同源模拟器/judge权限有限；persona bank、roleplay、process scoring与PID校准成本都需分账，未披露精度/全部steps/真实客服验证。必要方法/控制/反侧足即止。

实际Ch33 245–267和1483–1531已有过程verifier、context/group/turn支持与核baseline，缺**在session/turn混合目标中以观测cost反馈更新软multiplier，且归一的人口不是标准GRPO group**。拟该逐轮credit附近单段，保模拟反馈、违反目标的测量与固定权重/可靠outcome回退。请求TRAIN-GRPO窄lease，不修改历史22817等邻接。

## 22700 IMMACULATE — 2+2+3=7，Ch72 discrete-path replay与受限完整性审计

实际原38–57/63–87/103–137/145–183/258–263，只读依赖的rationality假设不遍历全部证明。服务先commit模型/精度身份及离散token/采样或MoE route决策，事后抽样challenge由FP reference强制重放已commit离散路径，避免微小数值差改变控制分支；LDD比较相应logits分布差。声明BF16时换FP8才是合同precision substitution，不把FP8本身叫恶意。随机抽样的检出依赖受攻击比例、不可预知challenge与匹配数值噪声人口；3000审计、1%随机率对10%attack得到95%至少命中，但允许3次误报后的至少4hit只有约30%，不可合并为同一保证。

重要反侧：原145–150实际VC评测是**Intel TDX enclave内FP32 Transformers**，不是已验证无trusted-hardware的密码学实现；协议设想与实验trust boundary必须分开，不授端到端GPU fidelity/任意adaptive adversary证书。RTX6000 Pro96GB、TP2、LLaMA70/Qwen32与两MoE有限任务；FP32 CPU重放数百倍慢，极小抽样fraction的摊销取决请求规模。EVT极低FP尾概率估计不是有限样本观测证明，logging最大1.0%不写全低于1；token-overreport无独立实测。固定计算预算下rational highest-quality attacker假设不覆盖可识别audit/选择性攻击。未核完整crypto/code artifact。

实际Ch72 1122–1135已经以IMMACULATE具体承载request-bound commitment、TEE边界、抽样预算及未公开artifact限制，但未解释**commit离散路径以隔离数值/control-flow差、LDD仅判声明的precision合同，以及实际TEE实验≠无TEE协议证明**。拟只改/扩该已有短段，不新造同名gap；若root认定现有覆盖足可Existing，不为论文名强写。请求PLATFORM-SECURITY第二窄位置。

## 22710 Same Words, Different Judgments — 2+1+3=6，Ch66 preference的模态测量身份

实际原31–50/52–77/106–111。100个PRISM matched-content成对回答分别文本/TTS固定Kokoro voice呈现给独立人群，25个从长度差top10%抽样，75随机；安全/发音过滤与重录使其不是所有prompts随机样本。46audio/48text有效rater、每人20比较、每样本约8–10rater；slider与A/Tie/B、呈现counterbalance、历史仍文本。ICC2,1约.333/.295，而聚合ICC约.821/.788，不证明单rater标签高可靠。跨模态winner仅53/100、无总体固定shift，却prompt×modality随机斜率显著，故**相同文字不能直接沿用每题preference标签**，不是所有prompt方向反转或一个模态更好。

文本长度偏好系数4.92、audio3.52，两者都正，interaction p=.045不能说语音无length bias。两模态同样recency bias；音频约136s/题vs文本79s。binary原nominal-alpha near0还混入A/B counterbalance标签方向，不能照录成所有偏好无共识。GPT4o与GPT4oAudioPreview synthetic评分改变模型和模态，非纯modal因果对照。单voice/English-US/TTS、安全过滤、独立cohort限制不认证audio-native prosody或真实安全评价；额外聆听/重录与rater校准付费。

实际Ch66 2659–2695已有rater方差/个体-vs人群分布、聚合与rubric权限，但没有**matched文字在TTS呈现后每题winner可失配，聚合可靠不能保证跨模态迁移**。拟该measurement链一段，保匹配population/voice/presentation、single-vsaggregate分母、语音仍length bias与原modal-specific标注回退。请求PLATFORM-EVALUATION-SYSTEM窄lease。

## 22716 SoPE — 2+1+3=6，Ch13坐标分解与频段预算

实际原41–59/62–78/82–83。保token序列index t，并将point coordinates转r/theta/phi；将RoPE pairs按t:r:theta:phi=24:2:3:3分配，混合linear/log/periodic频率通道。t是序列index不是观测时钟；主文未明确定义所有transform，不能补精确有符号log配置。相位差依坐标差，不等Euclidean距离/旋转平移等变或坐标奇点/wrap自动处理，球坐标只是需验收的几何prior。

Sonata+Qwen2.5 .5B/2层MLP、4H20、室内3benchmark与SpatialLM固定对照。uniform1:1:1:1 layout63.0/59低于base63.9/60.7，24比例66.1/63.2，去mix65.4/61.4；Cartesian加mix也改善，不能把全部收益唯一归球坐标。频段/比例搜索、坐标规范和训练成本仍在，精度/完整epochs/seeds ND。MASt3R-SLAM scene graph/机器人规划示例不是controlled实机成功率、安全或普遍泛化验证；无需扩机器人artifact。

实际Ch13 150–198有RoPE相对位移、结构多轴/null对照与连续二维身份，但缺**3D坐标选择和序列/空间频段预算共同改变几何prior，均分甚至退步**。拟连续二维交接附近单段，不改encoding主推导；保origin/axis/wrap数值责任（明确工程条件非论文已验证协议）、token index≠clock、负控制与Cartesian/原RoPE回退。请求MODEL-POSITION-ENCODING窄lease。

## 22718 RLHFless — 2+2+3=7，Ch33同步rollout的预算/长尾分支

实际原49–93/94–101/103–139；首轮90后截断已完整补。重复训练prompt使用历史response长度EWMA ranking，将相近长度分到同actor，让短actor早退出；估错时按完成比例tau触发局部cut/migrate到仍有空槽actor，不像全局同时切。用profiled TPOT+候选actor数的normalized latency/GPUtime权衡和weight/KV传输约束选count；改变generation资源而非G/sample人口。历史排名可靠/有可用迁入槽/传输可隐藏是新可行性条件，成熟serverless和prefill去重不单独加分。

两AWS g6e.48xlarge共16L40S、Qwen2.5 3/7B、PPO/GRPO/GSM8K等、prompt1024/response2048、3epochs平均step、VERL0.3.1.dev/vLLM.8.3/CUDA12.8/NCCL2.27；完整batch/precision/SLO ND。Cost为GPU×second proxy，Docker/Ray自建serverless不是完整公云函数billing。prewarm历史调用+最短step/缓冲是原97实现，不免warm residency/startup/profile/Redis/NCCL费用。控制有trace-replay baseline以保持生成content、oracle只是完美预测；tau小增加迁移，<=.5成本不再降因无可用槽，latecut可有时延outlier，fixed-normalization权重不能跨workload普用。70B/20×8H100是Vidur模拟，不授真实规模收益/生产TCO。

局部文字冲突独立隔离：原64声称unique prefixes D(L)随L增大下降，但对aX/aY样本D(1)=1、D(2)=2；故不采用该单调搜索/保证充分prefill算法。无需整项D，已独立支持的ranking+runtime纠错+actorcount条件继续采用，不自修code。均衡分配的general最优、无质量变化也未由作者证明。

实际Ch33 1245–1294已有rollout服务/长尾、policy freshness和完整group-ready调度，缺**固定同prompt重访历史ranking让同长actor早退出、局部迁移和GPUtime-actorcount选择，以及warm费/槽依赖**。拟Rollout变服务小节一段，不新增独立serverless章/不改algorithm identity。保同步完整G、policy/KV一致性交给既有admission链，失配回固定actor/无迁移。请求TRAIN-GRPO第二窄位置。

2026-10-06 fresh执行者 `feb28_close_oct06`（非原prepared作者）局部复核及实际落实：22697：原必要blocks50–70/95–97与actual owner独核；Ch33正文1509/完整1499–1523/own2958 root非写入者actual POST通过；22718：原必要blocks49–93/119–132与actual owner独核；Ch33正文1293/完整1287–1305/own2960 root非写入者actual POST通过；22710：原必要blocks31–38/56–61/65–68及采用相关prepared控制/反侧与actual owner独核；Ch66正文2725/完整2711–2739/own5671 root非写入者actual POST通过。未变身份/精确v1/采用命题复用，费用、直接反侧/错误子保证及旧路径回退近文；不授全附件、实现复现或日级完成。 22689另发现原作者MoFit README与ICLR2026同题forum KUXLrSXYPv；notes API403、forum challenge（V3_FETCH_22689_FAMILY.json），arXiv事件区间不认证家族first-public。原技术必要审阅仍有效，缺原note pdate/本窗实质新事件，现日期终态隔离，不进确定候选或Books；未写该段。

2026-10-06 fresh执行者 `feb28_close_oct06`（非原prepared作者）本项落实：22700：2+2+3=7，commit离散路径/continuous reference重放与TDX/检出分母；必要原v1/直接反侧与actual owner独核，Ch72正文1145/自身4282及完整邻接root非写入者actual POST通过。保原有效身份/精确版/采用命题，必要原段见本项；作者已实际顺读，费用、人口、错误子保证和原路径回退近正文，窄锁释放；不授全附件/实现复现或日级。
