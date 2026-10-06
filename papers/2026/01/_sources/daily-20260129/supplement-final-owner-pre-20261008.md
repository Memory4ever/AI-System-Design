# Jan29 — last two scoped title-omission candidates

准入、必要Source、owner PRE及实际写后POST均由root非作者通过；19792为2+1+2=5，19115不重复评分，重要机制事件受影响内容深入。精确日期材料见supplement-dates：v1 Jan27提交只供发现/公告下界，created均Jan28仅作已访问上界；结合已有官方schedule边界，不把提交或created作实际公开时刻。没有用v2后发内容。

## 2601.19792v1 LVLMs and Humans Ground Differently

精确原件supplement-primary-19792，必要§4.1–4.5(text254–450)、Table1/§5(text451–650)、§6/Limitations(text650–850附近；按节定位优先)，web原件supplement-final-deciding/core也含行号。共同task/角色固定四轮、同对象每轮重排，HH/HA/AH/AA共89pairs×4round=356dialogs。GPT5.2 reasoningnone，3-part prompt含pragmaticnorm+JSON/CoT scaffold；完整humanfilteredparticipant条件非随机population。accuracy=正确放basket，effort=word/turn，lexicaloverlap=LLM提取RE后的proxy。AA高初始accuracy却后轮下降，word/turn不降低、overlap始终高；HH提高accuracy并缩短。不由词汇复用证明conceptualpact；不由此局部实验宣称LVLM全无commonground/Turingtest失败/physicalrisk。后续每condition仅最多2次，小量reasoninglevel有阶段恢复，异构partialexception；未全面repair分析，英语单对象/全factorial单model，closedmodel/历史保留scaffold影响。原稿AH数量22pairs而叙述“16pairs”不一致，taskdistractor4而caption6不一致，不采用精确分组效应或机制唯一归因；只采用评价接口与观察模式。

Ch82 actual L18–33有singlebaseline/coordinationtax，L60–95不同topology/communicationmetrics，L270角色solvevsaggregate profile，但未具体承载“相同partner跨回合成功与effort/词汇适应联合测量，高lexicaloverlap可能只是冗长复制”的交互证据。Ch81/83 opener分别durableworkflow/协议标准化，不争owner。拟Ch82单Agentbaseline比较段后、信息上界段前两段：

若部署对象是持续合作的partner，还应把初次成功与共同约定的形成分开测量：保持伙伴、角色和对象身份，跨回合重排任务，联合记录准确率、用词/轮次费用及指称表达的复用与缩短。词汇重合高可能只是完整复制冗长描述；如果后续既不省交流又更易出错，就不能仅凭高初始分数或确认次数宣布共享语义已经稳定。<!-- source-family:SF-2026-ARXIV-2601-19792 -->

[受限referential任务](https://arxiv.org/html/2601.19792v1)把human/AI director与matcher作四种配对，观察到AI配对的初始准确与后续适应可分离；它没有证明所有LVLM缺共同基础，也没有测真实physical安全。英语单对象、特定GPT5.2/scaffold、有限follow-up与词汇提取proxy限制归因，人工招募、持续对话、分析和重复校准均付费。伙伴或任务改变时应重建这份交互证据；约定不稳或交流税过高时，保留显式object IDs、typed handoff、固定workflow与独立结果核验，不由话多或词汇重合替伙伴批准完成。

## 2601.19115v1 FBSDiff++

无HTML，必要PDF已下载supplement-19115v1.pdf（33pages），提取原件supplement-primary-19115(JSON.pages)。仅实际读p3版本新增、p7–9§3.2/Alg2/3/Fig2–5、p18–19受影响ablation/metrics、p20–22Tables1–6，不全附件。旧2024FBSDiff2408.00998+officialrepo仅去重身份，不作当窗新项；本项是同一FBSDiff家族的新机制事件，不因另论文名增加家族。恢复时定点rg核papers/books的2408.00998、FBSDiff和2601.19115，除本日拟文记录未发现既存候选或采用链；没有既有有效审阅可重复计数。本新扩展arxivJan28可访问，无旧++公开信号发现；不以v1 Jan27提交作公开日期。

从1000-stepinversion+50-stepreconstruction+50target改50inversion+50target，反序缓存inversionstates直接作guidance取消reconstruction；不是equivalent reverse/no loss。将i+j绝对2D三角mask改先w再h连续1D-DCT替换，每轴百分比阈值按size归一；percentile不认证两个空间相同语义、全分辨率或strictpreservation。局部mask仍decode能跨区域影响，styleSTP固定一次spatialtransform也不授semantic disentangle。p21Table3 20samples相近proxy支持50vs1000recipe，Table4分辨率只四点512²/512×1024/1024×512/2048²（20samples），Table2保留强度与CLIP明显tradeoff。p22Table5总85.2s→9.6s是该inversionbudget/路径差别，未披露timingGPU/precision/batch/concurrency/SLO，不采普遍8.9x。p19LAIONMini每任务800images×2人工prompts，DINOselfsim/LPIPS/AdaIN/CLIP/aesthetic都是proxy，尚未证明无损编辑/严格背景不变。

Ch24 L177–183已有subspace leakage和TPBlend两接口，L187 graphdiffsourceprompt与inversion、L1738跨segment依赖，未具体承载inversioncache替reconstructionguidance和peraxisrelativeband接口。拟在TPBlend费用段后、逐帧reference编辑段前两段：

Reference guidance 也不必重新运行一条source reconstruction trajectory：可反序读取已缓存的inversion states，在target采样早段逐步替换指定频带，再释放约束完成生成。需要适配长宽和分辨率时，各轴按长度归一的相对频率阈值，比固定二维坐标门槛更明确地声明控制范围；连续沿宽、沿高替换改变了控制算子，不是原二维mask的语义等价转换，也不保证频带恰好对应纯style或content。<!-- source-family:SF-2026-ARXIV-2601-19115 -->

[FBSDiff++ 的有限 SD1.5 对照](https://arxiv.org/pdf/2601.19115v1)支持取消 reconstruction 后减少 inversion 预算的局部分支；只测有限尺寸与 proxy 质量，保留强度又与 text fidelity 交换。缓存、DCT、inversion/target 步数、图像 decoder 与预处理都计成本，表中 50 vs 1000 步的总时间不成为通用 8.9 倍或 SLO。局部 latent mask 不能自签原像素严格不变，尺寸/编辑/保真未通过时，保留高精度 inversion、source reconstruction、显式 inpainting 与原频率控制，并独立验收未编辑区域和目标完成。
