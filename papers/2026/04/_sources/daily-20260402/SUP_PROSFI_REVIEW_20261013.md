# PRoSFI `2603.29500v1`：formal scaffold 与 reasoning witness 分责

实际已读必要v1 §4 [方法](SUP_PROSFI_DECIDER_20261013.json)、§3/5.2 [oracle与主Table2](SUP_PROSFI_EVAL_ORACLE_20261013.json)、仅§5.1/5.3/5.4/5.6 [评价](SUP_PROSFI_EVAL_20261013.json)。拟真实 `2+1+2=5`；不是把完整formal-verification原则作为本文新贡献。准入/Source/Books待root，不预授。

## 实际机制与条件

直接产生全Lean script对小模型难且可打断rollout；本文让7B输出id/dependencies/conclusion/rule scaffold，每step依赖少于5，并要求末step为target/answer候选。生成整个rollout后才formal验证，可batch/async分责；不从设计接口推出已实测异步throughput。全部step/answer正确最高reward1，answer对但部分step未验为.3，format对但answer错.1，其他0。每step提取的formal命题验证不自动覆盖全部自然语言trace，§3自己明确RewardHit≠Soundness；actuallogicalpremise/自然语言对应仍需独立验收。

## 必要评价与反側

ProverQA去掉Uncertain后769train，Qwen2.5-7B-Instruct/GRPO，LR3e-7/B64/8responses/max5120/KL.001/clip-higher、960iters约14h；8×Hopper GPUs、Debian12/CUDA12.4/PyTorch2.6/vLLM.8.3/Verl.4.0，GPU型号/memory、precision、完整CPU verifier预算与independent training seeds Not Disclosed。ProverQA-Extra128为Qwen32B生成故事，test每题16responses平均，不将16responses当16trainingseeds或开放domainOOD。

§5.3说direct-Lean保持reward/training只改output，但自己声称accuracy与soundness皆低于Outcome，Table2只Extra符合；Hard direct92.29/33.11高于Outcome91.31/21.97。不能抄该无条件否定。Table2 PRoSFI Hard92.97/GPTSound76.07，Extra91.94/56.10支持此受限格式/奖励分支的作者评价；GPT-OSS-120B Soundness为judge proxy非真实proof coverage/独立人验。RewardHit与GPTSound correlation不认证formal propositions涵盖所有NL推理或绝无错步。

停止在真实接口与局部protocol/主反側：不扫prompt、全部proof、GPTjudge附件或代码；未复现。若Source通过，再按TRAIN-RLHF具体owner正文比较生产者/验证者/semantic witness差额，不能由形式验证主题自动整合或NC。日期仅normal复合门和当前official轻量事件点，不使用Submitted/created单字段。
