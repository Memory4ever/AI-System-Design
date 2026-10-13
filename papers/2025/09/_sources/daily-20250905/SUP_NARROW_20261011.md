# Sep05必要局部与采用边界

作者实际读取记录，非独立签字。所有ID为2509.*v1；HTML段号由本日inspect.py定位，PDF为物理页。正文原件为SUP_core-ID_20261011.raw（03518为SUP_lie-core），PDF为SUP_pdf-ID_20261011.raw；ICPAD先稿PDF为SUP_icpad-old-pdf及SUP_icpad-v1-pdf。这里是贡献决定/安全反侧，不是日期未知材料的候选Evidence完成，不授全文、复现或Books。

## 首批必要局部

| ID | 实际必要位置与判断边界 |
| --- | --- |
| 03498 OneCAT | §3/3.1段20–51：三路模态FFN/shared QKV与next-scale接口；段27输出需detokenizer，作者repo --vae_path一致，不采整套VAE-free/无teacher。 |
| 03501 Strefer | 段14–24、106–118：dense时空监督；masklet/occlusion/pseudo-label与hallucination、模块成本和foreground bias保留。项目/CVF只年/月级，不能授Sep04日证。 |
| 03505 LimiX | 段12–31：feature/sample轴与CCMM context/query，作者News明确Sep03 paper available；OLD，不把Aug29模型release或2026v2当同事件。 |
| 03518 lying | §3–6段13–79：提示规定说谎目标、PCA/dummy-token控制与steering任务代价；不授意识、通用欺骗因果或安全保证。 |
| 03992 DK | 段33–46、120–127、137–158：离散条件与forward估计；连续极限原文formal非严格证明，强收缩/小噪声失败及每步二阶导数成本，不采窗外v2。 |
| 04259 RL's Razor | 段25–87、95–105、123–126：同prompt/Pareto与on-policy分布条件；oracle-SFT可胜RL，BF16稀疏在float32消失。有限binary reward/convex假设，神经策略非e-flat未必精确KL最小，作者尚缺KL→遗忘mechanistic account及frontier验证；P不授通用因果或RL普遍优势，不称整套理论/附录全核。 |
| 03680 Lux | 段24–48、72–79：nonaligned token/channel接口与dual-tonemap；部分HDR真值缺失，迭代采样非实时。 |
| 04338 FE2E | 段15–46、58–63、85–91、132–138：editor先验、一致速度/BF16量化；附录同LoRA/优化/数据且一denoise-step对照，不授整模型cost-free。 |
| 03837 BEV | 段37–47、51–65：坐标/time消融；含future目标与ego-only信息不对称，不授现实在线/安全。 |
| 03643 CEHR | 段24–52、97–104：ATT/TD/TTE时间目标；scalar collision非高维embedding证明，full FT对linear probe不等可比临床部署。 |
| 03975 Vessel | 段14–23、34–51、54–60：低注量/任务权重反侧；June2024 exact DOI与作者机构2024同家族OLD，不授出版社403全文已读。 |
| 04076 robot | 段35–59：batch任一成功/短轨迹偏置、hard subset与无pointcloud反侧；无碰撞loss，固定20s PRM不证明所有方法公平或安全。 |
| 04193 DUDE | 段30–54、67–79：frozen SD分离/渐进neighbor对齐；OfficeHome/PACS反转，不授真实因果解耦。 |
| 03475 PnP | 段0–9必要intro：理论由既有文献支撑，本稿组织不构成新证明；EX不因survey体裁。 |
| 03883 motion | 段3–13：五阶段/十任务/200论文组织未有本稿原始反侧或形成条件；EX。 |
| 03487 SafeProtein | 必要方法/评价及限制、段49–62：本阶段科学应用EX；有限评价不授实际biosafety保证，不传播攻击操作。 |
| 03479 text game | 精确PDF六页必要§3–5：既有worldmodel/PG模块未给可辨新机制/controlled协议，EX，不因HTML404。 |
| 04245 synthetic HF | PDF p5/6/8/9/10必要隐私段：MIA/AIA/NNAA的有限均值/零匹配不证明全部类别隐私；EX，质疑本身不是原文新增贡献。 |
| 10518 HKM | 历史v1段19–59曾读；当前abs明确整篇withdrawn/重大错误，v2不可用是撤回非故障；不入选/评分/Books。恢复须官方有效修正版及具名修复，不靠旧PDF仍可下载。 |

04535 ICPAD双方精确PDF p1/p3共同方法与AAAI官方Apr11发表实际读；OLD身份有效，无Sep04具名重要修订。其余首批P完整题摘已校准但未声称必要全文/Evidence完成，日证恢复后按所需命题投入。

## 第二批决定局部

| ID | 作者实际必要位置及最终窄处置 |
| --- | --- |
| 03122 | 段15–36、42–56：editing指纹与FSFT subspace正则，lambda非单调/冻结模块仍破坏传输；类似输入误报不支持ownership特异性或防盗保证，P。 |
| 03531 | 段23–51、81–107：entity-token/span-max与linear/LoRA检测；NotSupported和InsufficientInformation合并标签，搜索/标注噪声，跨模型监测额外forward成本，LoRA分布改变与attempt下降，原文明确部署不足。P，不授claim级/高风险安全。 |
| 03616 | 段17–41、49–88：多bias梯度与SBA避免train/test shift混杂；依赖已知group标签且纠缠残留，正文provable invariance措辞未被当定理验收。P，不授未知bias或所有公平。 |
| 03419 | 段24–61、76–104：reference/rubric有益且诱发六类偏置，dimension缓解仍误报；未验证工具/多模态和通用修复。P，风险/真值准确率不由ASR混算。 |
| 03526 | 段21–37、65–68：相同多speaker合成数据，SFT独立labels对group最佳/最差relational objective；四voice/500指令embedding一致性非真值，teacher答案与过滤、不同任务目标优劣反转保留。P，不授任意voice或RL普遍优势。 |
| 03162 | 段15–27、49–59、69–72：原生/翻译STEM各100题两人仅评自然度/术语，同题5→4选项与文化子集；P翻译外部有效性/协议条件。自然度非答案正确，文化/难度未因果分离，官方考试整体通过率不作直接benchmark对照。 |
| 03433 | §3必要MCDB段47–60及段95–109、119–122，段100–101截断后补读：按模态贡献比抑制主导梯度，adapter/SPR组合与gamma反侧；P训练权重/组合收益条件，额外成本/subject差异/跨域未验证，不采用脑科学成果或在线保证。 |
| 03525 | HTML404后PDF实际p6–8/10–11/15–18/28–29：同输入/prompt与validation选配置下token-label vs classifier-head出现模型相关反转，P输出接口/适应条件。tokenization仅likely未消融证明；n71、ASR、API top5剩余质量估单token及资源差异，不采临床/概率校准/小模型普遍优势。 |
| 03529 | 段72–98：标准层次Transformer/CLS及NT-Xent、UMAP和Tesla cosine例；未给新的模型形成条件/控制，金融forecast仍未来，EX。 |
| 03527 | 段22–30、39–42、56–59：graph/text RAG+LoRA/4bit及摘要JSON组合；无受控hallucination证据，结论承认不准和实际建议限制。EX，不采用消除幻觉保证，也不倒造负面P。 |

Anscombe实际独核所有新67题摘及上述受影响局部，三项EX→P具名修正见唯一SUP_INDEPENDENT_20261011.md §11。作者与非作者所读范围分开：不授所有附件、全部定理或全部原实验验收。
