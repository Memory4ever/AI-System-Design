# 2025-11-11 第二局部校准ready

作者Noether。第一小包Omnilingual/OpenAI不重复。新18篇原exact-v1完整题摘及贡献/处置逐项见[ORDINARY_SCREENING](./ORDINARY_SCREENING.md)，原分组AB链接均可回核。未授日期、准入通过、Evidence Gate或Books；普通20个题摘及来源尾项仍由作者继续，不等待root。

root可先核以下affected-core，不必等待全日：

- UTF-8 Plumbing原v1 PDF身份COLM2025已核。Theorem2只说明含不合法byte token的vocabulary允许不合法序列，不证明必然每次生成；Theorem3/§5说明逐片replacement/drop与整串解码不交换，保留raw bytes和codepoint commit边界才能避免不可逆丢失，Algorithm1是局部fix且有内在限制。[原定理/流式core](./nov11-critical-stop.txt)、[mitigation范围](./nov11-critical-find.txt)。COLM论坛challenge、API受阻停止，submitted Nov5不是public。
- CIA原v1§3.3/3.4、§4.1与§7：GCG最大化snippet连续entropy；aligned结果需要mismatched SFT、raw template。500 prompts、InfiniGram 50-token exact/near match及diversity>=0.1，Llama真实训练语料未全部已知。§7明确white-box与可改权重/模板权限；高entropy不是充分泄露条件，不写ChatGPT/Gemini已攻破或生产泄露概率。[威胁/评价core](./nov11-critical-details.txt)、[限制](./nov11-critical-identity.txt)。
- DRAGON原v1§intro机制及CoT/detector消融：negative scorer+similarity confidence、guard动态CoT，不改base weights。TOFU/WMDP检测和拒答改善不能证明训练数据已从参数删除；不把无retain data说成无任何训练（guard/scorer训练仍在）。[机制](./nov11-critical-identity.txt)、[原消融](./nov11-critical-details.txt)。原OpenReview链接带分号Cachemiss后纠正forum一次，MUGen论坛challenge；不扫描会议全表，不授日期。
- Licensing Oracle原v1 PDF正文题名已核，web索引却题为Teaching a Language Model to Speak the Language of Tools，隔离这一索引。§3.1/3.2明确GLiNER/谓词mapping→triple、SHACL和知识图licensed后emit，§6.3明确graph coverage、语义/时间歧义、multi-hop未处理。可保留局部验证/拒答成本方向，但原必要充分/全正确声明不成立为本报告保证；不能因成熟validation原则就自动否定局部新证据。[方法](./nov11-critical-find.txt)、[限制](./nov11-source-final-details.txt)。
- Edits Decay官方v2 withdrawal原声明已经实际取得[HTML](./edit-v2.html)：技术性manuscript record错误涉及作者顺序、状态、未发表。历史v1链不采用、不评分，v2撤回版本排除；不能因为撤回记录就断言当前重新上传v3/v4全实验无效，也不能用当前254配置/2026结论替代历史232配置。

准入方向：KV跨模态状态、抽象ICL负证据、优化/entropy、任务PTQ、token/step路由与理论可行性均按局部增量，不按算法名缺位制造Booksgap。source/current/raw日期不足的潜力仍完整保留，最小日期重开统一见普通记录，不形成全附件/全owner队列。
