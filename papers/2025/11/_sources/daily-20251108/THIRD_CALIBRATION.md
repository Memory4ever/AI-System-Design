# 2025-11-08 新增必要反侧小包

作者Noether。只交新增实际证据，不重复首批题摘；不授日期、日级或Books完成。08普通工作继续，不等待07。

## Block Rotation exact-v1：格式条件与反侧

[原v1](https://arxiv.org/html/2511.04214v1)，[实际HTML](./blockrotation-v1.html)，已读§3.1/3.2、表1、§4.1–4.3核心，不声称全附件已审。

- §3.1：A800上以microsoft/microxcaling模拟MX格式；模型Llama2 7B/13B、Llama3 8B、Llama3.2 1B/3B、Mistral7B；WikiText2 PPL与五项zero-shot准确率。不是B200实测吞吐。
- 比较区分QuaRot+RTN与QuaRot+GPTQ，表1 Llama2-7B的MXFP4 RTN PPL7.08/Avg57.26，QuaRot13.09/50.32，QuaRot+GPTQ6.29/58.35。因而不能概括全部旋转都崩溃：组合补偿实际缓解，其他模型收益不一致。
- §4.1–4.3：32值E2M1共享E8M0 PoT尺度；全局正交旋转保持L2能量，却把能量转入原小值块、抬高常规块尺度；多块累计误差可能超过减少少数outlier的收益。块内旋转对齐32通道组，限制跨块能量迁移。这是量化格式/变换兼容条件，不是成熟outlier原则改名。
- 原§3.2 prose把GPTQ PPL13.35写为3.35的例子与表1不一致；采用表1，不采用该错误数值或无损宣传。保留为中央数值反侧。

owner仅定位INFER-TENSORRT-LLM通用量化校准段，未读现有论点并认定新缺口；日期未核，不请求整合。最小date重开是该精确v1官方公告或可信首次公開上下界完全落窗，submitted Nov6不够。

## REMIND exact-v1：访问条件与评价边界

[原v1](https://arxiv.org/html/2511.04228v1)，[实际HTML](./remind-v1.html)。已读§3、算法1/2、§4及§5.1、表1相关反侧。

- 模型loss在原句/扰动句上的统计输入分类器；gradient特征由外部text encoder计算，不等于要求target梯度。只有自然语言输出、没有loss/log-prob的API不能据此声称支持。
- §5.1明确有至多1000个带标签validation样本作校准；MUSE/TOFU/WMDP，Llama3-8B-Instruct/Llama2-7B-Chat/Zephyr7B；GPT2 tokenizer用于跨模型扰动。WMDP无holdout，作者使用test替代，不能当独立未训练组天然等价。
- 表1 RF multiclass AUC原句82.84、rephrased74.2571；低FPR结果也下降。局部分类改善不是遗忘彻底、安全或法规合规证明。embedding近邻替换语义保持是作者方法假设，不由算法本身保证。

潜在PLATFORM-EVALUATION-SYSTEM增量是forget核验从单点到邻域的诊断及访问/校准边界；未建立因果证明“任何平坦邻域均已忘”。日期未核隔离；不因该命题未采用继续全部实验附件。

## Guardrail reverse engineering exact-v1：代理与不可识别性

[原v1](https://arxiv.org/html/2511.04215v1)，[实际HTML](./guardrail-v1.html)。已读§3.2、§4.1–4.3、§5.1–5.3和$85关联段。

- 威胁观察是整系统最终purified response；§4把victim评分prompt反馈当reward，并以GRPO更新Llama3.1-8B surrogate，divergence样本用于mutation/crossover。不能仅由最终输出区分base模型alignment和外部guard贡献；“真实隐藏规则已全部恢复”不是这些观察可保证的结论。
- §5.1 jailbreak3600/400、injection4200/800 train/test；LoRA rank32、lr2e-5、batch8/accum4；4×RTX A6000训练。victim写ChatGPT/DeepSeek/Qwen3而未锁定API精确版本，作者原配置不当现在服务保证。
- §5.2 RuleMR来自九伦理/哲学维度单选value benchmark；这是代理偏好一致性，不是隐藏policy源码、coverage或攻击ASR。表2 accuracy/F1是区分benign/malicious任务，不能转述为绕过率。
- $85关联ChatGPT injection600次训练迭代的LP_GPT=1；LP公式是toxic-score差值比，1不表示全规则恢复或全API成本。同一victim也充当训练reward/部分evaluator，独立LlamaGuard/ShieldGemma结果不消除全部混杂。

保留潜在PLATFORM-SECURITY黑盒行为可提取性命题并收窄；不采“商业guard普遍被攻破”。日期未核，不请求Books。root请局部校准上述代理/反证解读，而非重读全文。

## 本次完成的来源尾项

- [Anthropic native](./anthropic-native.html)真实Next flight解析172个去重post身份；`publishedOn`邻接Nov4 16:00:49.850Z/Nov12 18:19Z跨过本窗，无内嵌本窗post。不授官网外绝无漏项。
- [MiMo原HTML](./mimo-current.html) `blog-more`已内嵌第9–15项，data-expanded=false/aria-hidden=true；More不是新分页。日期未披露的Blog仍历史保留，不授2025零研究。
- [MiniMax原技术页](./minimax-techblog-current.txt)仅2026-05-13 Agent Team；旧历史缺段隔离，不读2026正文冒充08。
- 六篇当前abs原HTML已实际取得并检查comments/history/摘要旁轻量信号，均仅v1且未见withdraw/erratum/correction标记；不遍历版本史。
- 旧arXiv `/list/cs.CL/2511` native404明确Invalid Year2511，本日dated-route native400；据实际错误修正为`/list/cs.CL/2025-11?skip=175&show=50`成功200。只浏览50标题，停止，不取all1527；月标题不能证明首次公開时刻。[原50标题](./arxiv-month-corrected-native.html)含ThaiOCRBench corrected Table2信号，仍须定点核影响范围，不能无视。

本包只请求局部校准。其余未读/必要日期与有界补检新标题仍按CURRENT_STOP推进；没有Books修改。
