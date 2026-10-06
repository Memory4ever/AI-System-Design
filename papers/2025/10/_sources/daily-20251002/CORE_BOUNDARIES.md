# 2025-10-02 必要安全/反侧有限core

全部是精确v1 HTML，原件/机械提取分别为 `core-<ID>v1.raw` / `.text.txt`。已下载不等已读；下表记录实际有限阅读位置与判断。未获日期准入或独立校准，不授正面Evidence完成、不写Books。停止于足以避免错误排除或宣传外推的命题，不遍历全附件。

| 身份 | 实际位置 | 有限判断与关键限制 |
| --- | --- | --- |
| 2510.00490v1 GGUF BFA | §3.1～3.2 threat/deployment | 需远程执行、物理bit mapping与高频memory access；正文的pagemap/kernel module依赖和“无root”宣传有张力。不能当任意云租户可遥控LLM单bit的生产证明。 |
| 2510.00494v1 latent System1/2 | §3～4.1与4.3.1～5 | GPT-2 124M/Qwen3 0.6B、8×A100 80GB、40B/8B tokens；same data+latent budget但不parameter-matched。三pass不等原工作单pass。近似single-model表现和latent冗余是局部设计反侧，不推翻所有latent reasoning。 |
| 2510.00496v1 Agent-ScanKit | §5.1 | 18 GUI models、跨mobile/web/desktop；部分采样只原先100% step准确例，官方prompt/inference配置。扰动下降不能直接分解全部模型的“memorization比reasoning多”的因果量。 |
| 2510.00565v1 Priming | §4～4.1、6.1 | intervention threat和no-intervention attack分开；100 JBB behaviors、GPT-4o judge；三MDLM、BeaverTails/DeBERTaV3、2500steps。肯定token中间态威胁存在研究潜力，不把可改内部态攻击当黑盒API全可达。 |
| 2510.00626v1 irrelevant audio | §2.2～2.3 | 三文本benchmark、六LALM；5秒silence/noise、FSD50K；多数greedy，但Voxtral温度0.2/top-p0.95。accuracy之外用双向prediction influence rate，静音不是零影响；只限这些输入与模型。 |
| 2510.00628v1 audio order | §3.1 | MMAU test-mini、MMAR/MMLU，TTS题目/选项，过滤>180s和非四选项；强制correct answer四个位置。是受控位置偏差，不能推成所有spoken任务24%下降。 |
| 2510.00635v1 ReFlux | §5.1～5.2 | FLUX.1-dev、Euler28步、1000 attack优化步、H20 96GB batch1；白盒更新text相关参数，I2P自动detectors。概念擦除在指定攻击下可失效，不是任意user prompt无条件绕过所有服务。 |
| 2510.00761v1 optimizer/unlearning | 评价定义及§7 | MUSE ICLM/Llama2 7B保留/遗忘不同指标；ZO无tampering时较弱但tampering下较强，FO-ZO混合。不能只留robustness宣传、删掉原始forgetting代价。 |
| 2510.00778v1 DIA | §4.1及采样步敏感段 | PIE700图、9子任务，SD1.4，PGD epsilon0.05，DIA20轮/基线60轮，10步inversion；CLIP辅以PSNR/LPIPS/SSIM。是输入免疫/保护；并非新恶意攻防无限能力，更多采样步降低保护强度。 |
| 2510.00829v1 REAL-MT | Experimental Settings/controlled-noise | Qwen2.5 7/14B、Qwen3 8B，greedy，tokens4096/32768，H80080GB batch40。synthetic noise+idiom资源分层，reasoning noisy-context误信的局部反证；资源层和模型差异不自动完全因果控制。 |
| 2510.00857v1 ManagerBench | Limitations | 合成多选scenario、人类仅校准subset，无法允许agent提第三条安全路径，prompt nudge改变目标，非zero temperature。是目标/安全取舍评价盲区，不能外推真实经理行为概率。 |
| 2510.00938v1 RECAP | §4.1 | 错误CoT prefill与常规unsafe prompt分开；StrongREJECT/WildJailbreak/Fortress，另XSTest/benign Fortress测overrefusal，GPT4o judge。训练恢复不等所有adaptive攻击安全保证。 |
| 2510.01070v1 secret elicitation | §6 | 人工SFT单run secret模型、single rollout审计，human/LLM多轮probe可能找到secrets；未表明复杂pretrain/RL自然secret同样可恢复。保留模型审计方法潜力，不称能力上界。 |
| 2510.01088v1 SIRL | §5.1 | Qwen2.5 3/7B、Llama3.2 3B/3.1 8B，PKU-SafeRLHF unlabeled prompt，20 JailbreakBench、rule+LLM judge，8A100/verl；内生entropy reward并非天然可靠安全标准。 |
| 2510.01157v1 SpeechLLM backdoor | §4～5.3 | poisoned encoder/connector/LoRA的freeze/train与propagation分开；LibriSpeech/CREMA-D/VoxCeleb2，ASR trigger要重复；不同任务5～10%有效poison率，clean质量与trigger AER分开。只有攻击者可污染训练材料的特定模块化威胁。 |

以上只为日期隔离材料保留必要安全/反侧边界，没有实验复现、代码执行或部署验收。root需独立核这些项是否遗漏重要信号及日期隔离是否足够。
