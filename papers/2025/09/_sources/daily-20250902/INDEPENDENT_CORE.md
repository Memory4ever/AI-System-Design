# 02 非作者必要 core 与 DARLING 局部校准

复核者 sept12_15_author；按当前合同独立加载本日窗口，不继承其他日报。作者 Aristotle/root 的有效首批准入复用；本记录不是最终DAY或正面Evidence。

DARLING：实际完整读 `meta-diversity-original.raw` 的官方摘要，learned partition function提供超出词面差异的语义多样性信号，并与quality reward在线联合优化，有明确目标/信号替代。最小潜力准入通过，当前19=14潜力/5关闭。五benchmark/pass@k和探索因果仍作者声明，未核方法/预算/判别器；官方Sep2日期无精度/时区，不能授完全落窗，也不能用后来的arXiv提交否定更早官网。保持日期hold。

## 五项原文独立核查

- TConstFormer：实际读精确v1原HTML §2.1、§4.1–4.3、§5.1–5.2、§8。cache miss明确包括每次历史窗口滑动后首token，成本C1*N+C0且固定Wog周期重算，固定超参下周期平均含C1*N/Wog；cache-hit O(1)或固定KV不证明全周期O(1)/全历史恒定存储。41M与精确检索无定论限制保留，不以小模型关闭。HTML页头自动日期2026不作原公开证明；abs v1身份/唯一历史现已定点官方轻量核。
- Unlearning：实际读v1 §2.2–2.3、§4.1–4.3、§5.2–7。1:1仅98 retain每epoch，cyclic/MELU遍历1801且重复forget，等4epoch不是等曝光/计算。脚注100epoch 1:1 DPO能到FE .79/MU .78，不能宣称无法忘记。MELU entity pairing真实，但一般集随机配；同族生成、仅LoRA输出评价与实体可分假设不授base-weight删除/抗提取/隐私证明。未读memorization附录或全部算法表图。
- Safe-LLaVA：实际读v1 §3–3.1.1、§4.1–4.3/表2–3文本、§5、Appendix B/E–E.1。保护分数是1-mean(B)，97.1被叙述误称leakage rate不能反向采；GPT/Gemini分数明显不同，自动judge不等人工真值。baseline与处理组数据差异设置真实；一般视觉任务只是语义保持代理，无逐样本faithfulness或无害问题误拒直接测量。短回答减少披露是作者明确替代解释，不能授零泄露/全面安全。未读图中全部prompt、性能像素/统计附录。
- Two Causes：实际读v1 §2–3.3、§4/§5.1–5.4、Appendix C/D。VCD在局部POPE任务少false-negative而多false-positive，分账而非总分推统一改善。top25% attention centroid等面积方区、轻度增强后hidden差分steering是真实机制；定位attention不证明已正确编码语义，yes/no干预不排他证明两类根因。centroid消融adversarial退化、head比例过大降分、Appendix D不直接针对fabrication suppression保留。未读SID完整代数推导或全部图像。
- BAI：实际读v1 §3–4.1、§4.5–4.7、§5–6。stage1多SFT均权、stage2base比例确真实，但§4.5.1负侧对照允许base+reasoning两者，不称所有必须两步。Seed-MoE/PPO配置与1600/3000步比较保留；长度/RM轨迹是初始化条件的局部反证，不证明reward hacking根因或通用消除。§4.7明说training-policy对sampling-policy，不倒写固定SFT reference KL。未核全部seed/曲线像素/运行。

五必要风险/理论原件足够支持禁止强采用及保留最小潜力，未作五篇完整Evidence，不把日期hold送全文队列。当前官方精确v1 abs轻量检查见 `INDEPENDENT_CORE_IDENTITY_WEB.json`；未见新撤回标记，版本变化本身不扩审。无Books实际写入，不授已有覆盖。该记录为局部证据停点，最终有限来源、题摘与日级终态以同日README §6为准。
