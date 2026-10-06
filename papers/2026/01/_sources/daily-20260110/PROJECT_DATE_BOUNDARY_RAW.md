# Jan10 可见原项目日期查漏

仅定点原论文所示GDPO/RoboVIP项目入口，查可见早于本窗的发布或修订信号；当前README不是历史完整证据，不扩commit史或全站。原返回中的代码段未用于声称实现审计或复现。

GitHub - NVlabs/GDPO: Official implementation of GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization · GitHub (https://github.com/NVlabs/GDPO)
citeturn26882view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://github.com/NVlabs/GDPO","lineno":260}); Total lines: 379
L99:     * AVAILABLE ADD-ONS
L100:       * cite10†GitHub Advanced SecurityEnterprise-grade security features L101:       * cite57†Copilot for BusinessEnterprise-grade AI features L102:       * cite58†Premium SupportEnterprise-grade 24/7 support L103: 
L113: You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. Dismiss alert
L114: 
L115: cite61†NVlabs / cite62†GDPO Public
L116: 
L117:   * cite63†Notifications You must be signed in to change notification settings
L118:   * cite63†Fork 38 L119:   * cite63†Star L120:   * cite62†Code L121:   * cite64†Issues 5 L122:   * cite65†Pull requests 1 L123:   * cite66†Actions L124:   * cite67†Projects L125:   * cite68†Security and quality 0 L126:   * cite69†Insights L127: 
L128: Additional navigation options
L129: 
L130: main
L131: 
L132: cite70†Branches cite71†Tags L133: 
L134: [Input: Go to file]
L135: 
L136: Go to file
L137: 
L138: Code
L139: 
L140: Open more actions menu
L141: ## Latest commit
L142: 
L143: 
L144: 
L145: ## History
L146: 
L147: 31 Commits
L148: ## Folders and files
L149: 
L150: Name  | Name  | Last commit message  | Last commit date
L151: --- | --- | --- | ---
L152: cite72†.github/workflows | cite72†.github/workflows |    |
L153: cite73†imgs | cite73†imgs |    |
L154: cite74†nemo_rl-GDPO | cite74†nemo_rl-GDPO |    |
L155: cite75†trl-GDPO | cite75†trl-GDPO |    |
L156: cite76†verl-GDPO | cite76†verl-GDPO |    |
L157: cite77†LICENSE | cite77†LICENSE |    |
L158: cite78†README.md | cite78†README.md |    |
L159: cite79†third_party_dependency.LICENSE | cite79†third_party_dependency.LICENSE |    |
L160: ## Repository files navigation
L161: 
L162:   *   * cite80†README L163:   * cite80†Apache-2.0 license L164: 
L165: More items
L166: 
L167: # GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization [ICML2026]
L168: 
L169: #
L170: 
L171: 🤗 cite81†Hugging Face Page†huggingface.co |    📄 cite82†Paper†arxiv.org |    📜 cite83†Page†nvlabs.github.io L172: #
L173: 
L174: GDPO is a reinforcement learning optimization method designed for multi-reward training. While existing approaches commonly apply Group Relative Policy Optimization (GRPO) in multi-reward settings, we show that this leads to reward advantages collapse, reducing training signal resolution and causing unstable or failed convergence.
L175: GDPO resolves this issue by decoupling reward normalization across individual rewards, preserving their relative differences and enabling more faithful preference optimization. Across tool calling, math reasoning, and code generation tasks, GDPO consistently surpasses GRPO in both training convergence and downstream evaluation performance.
L176: 
L177: In this repo, we provide implementation of GDPO based on cite84†VERL at cite85†verl-GDPO , cite86†TRL at cite87†trl-GDPO , and cite88†Nemo-RL at cite89†nemo_rl-GDPO .
L178: We also include easy-to-use, slurm-free training scripts that enable the community to quickly validate GDPO’s effectiveness over GRPO on tool calling and math reasoning tasks. Each run can be completed in approximately 1 hour on a single node with 8×A100 GPUs, or around 2.5 hours on a single A100 GPU.
L179: ## 💥 Open Source Integration 💥
L180: 
L181: GDPO is now supported in the following RL-training libraries:
L182: 
L183:   * cite86†TRL 🔥🔥 cite90†Example here !!
L184:   * cite91†Ms-swift 🔥🔥 cite92†Example here !!
L185:   * cite93†Axolotl 🔥🔥 cite94†Example here†docs.axolotl.ai !!
L186:   * cite88†NeMo RL 🔥🔥 cite95†Example here !!
L187:   * cite96†Verl 🔥🔥 cite97†Example here !!
L188: 
L189: ## 🚀 Run GDPO with verl to improve two-reward RL training for tool calling.
L190: #
L191: 
L192: Here we compare GDPO with GRPO on the tool calling task, specifically, the model trained to learn how to incorporate external tools into the reasoning trajectory to solve a user task following the output format of
L193: 
L194:     `**Output Format**
L195:     <think> Your thoughts and reasoning </think>
L196:     <tool_call>
L197:     {json_string}
L198:     ...
L199:     </tool_call>
L200:     <response> AI's final response </response>
L201:     `
L202: The training set consists of 4k samples. Each training instance contains a question and its corresponding ground-truth tool calls. The training involves two rewards:
L203:   * Format Reward: A binary reward (0 or 1) checks whether the model output satisfies the required structure and contains all necessary fields in the correct order.
L204:   * Correctness Reward: The correctness reward ∈ [−3, 3] evaluates the model-generated tool calls against the ground-truth calls using three metrics: tool name matching, parameter name matching, and parameter content matching.
L205: We train Qwen2.5-1.5B-Instruct with GDPO and GRPO using verl for 100 steps. Check cite85†verl-GDPO for detailed implementation of GDPO based on VERL and how to reprodcue the above result.
L206: ## 🚀 Run GDPO with TRL to improve three-reward RL training for math reasoning.
L207: #
L208: 
L209: We compare GDPO and GRPO in their ability to incentivize the model’s reasoning capabilities (i.e., achieving the “aha” moment). Specifically, the model is trained to first produce detailed reasoning steps and then output the final answer in a prescribed format when solving user queries.
L210: 
L211:     `Output Format:
L212:     <think>Your thoughts and reasoning</think>
L213:     <answer>Final answer in integer format</answer>
L214:     `
L215: Training is conducted on the GSM8K dataset, where each example consists of a math problem paired with its ground-truth answer. The RL training incorporates three reward signals:
L216: 
L217:   * Format Reward: A binary reward (0 or 1) indicating whether the model output follows the required structure and includes all necessary tags in the correct order.
L218: 
L219:   * Correctness Reward: A binary reward (0 or 1) that verifies whether the final answer enclosed within `<answer></answer>` matches the ground-truth solution.
L220:   * Integer Reward: A binary reward (0 or 1) that checks whether the final answer inside `<answer></answer>` is an integer, encouraging integer-only outputs.
L221: 
L222: We train Qwen2.5-1.5B-Instruct with GDPO and GRPO using trl for 1 epoch. Check cite87†trl-GDPO for detailed implementation of GDPO based on TRL and how to reprodcue the above result.
L223: ## ⚙️ GDPO is a straighforward drop-in replacement for GRPO
L224: 
L225: ### trl modification
L226: #### Original trl GRPO Implementation
L227: 
L228:         # line 1254 in trl-GDPO/trl-0.18.0-gdpo/trl/trainer/grpo_trainer.py
L229:         # Gather the reward per function: this part is crucial, because the rewards are normalized per group and the
L230:         # completions may be distributed across processes
L231:         rewards_per_func = gather(rewards_per_func)
L232:         rewards = (rewards_per_func * self.reward_weights.to(device).unsqueeze(0)).nansum(dim=1)
L233: 
L234:         # Compute grouped-wise rewards
L235:         mean_grouped_rewards = rewards.view(-1, self.num_generations).mean(dim=1)
L236:         std_grouped_rewards = rewards.view(-1, self.num_generations).std(dim=1)
L237:         is_std_zero = torch.isclose(std_grouped_rewards, torch.zeros_like(std_grouped_rewards))
L238: 
L239:         # Normalize the rewards to compute the advantages
L240:         mean_grouped_rewards = mean_grouped_rewards.repeat_interleave(self.num_generations, dim=0)
L241:         std_grouped_rewards = std_grouped_rewards.repeat_interleave(self.num_generations, dim=0)
L242:         advantages = rewards - mean_grouped_rewards
L243:         if self.scale_rewards:
L244:             advantages = advantages / (std_grouped_rewards + 1e-4)
L245: #### trl GDPO Implementation
L246: 
L247:         # line 1222 in trl-GDPO/trl-0.18.0-gdpo/trl/trainer/grpo_trainer.py
L248:         # Gather the reward per function: this part is crucial, because the rewards are normalized per group and the
L249:         # completions may be distributed across processes
L250:         rewards_per_func = gather(rewards_per_func)
L251:         ## Make sure every reward contain no nan value
L252:         rewards_per_func_filter = torch.nan_to_num(rewards_per_func)
L253: 
L254:         all_reward_advantage = []
L255:         ## Calculate the mean and std of each reward group-wise separately
L256:         for i in range(len(self.reward_weights)):
L257:             reward_i = rewards_per_func_filter[:,i]
L258:             each_reward_mean_grouped = reward_i.view(-1, self.num_generations).mean(dim=1)
L259:             each_reward_std_grouped = reward_i.view(-1, self.num_generations).std(dim=1)
L260: 
L261:             each_reward_mean_grouped = each_reward_mean_grouped.repeat_interleave(self.num_generations, dim=0)
L262:             each_reward_std_grouped = each_reward_std_grouped.repeat_interleave(self.num_generations, dim=0)
L263:             each_reward_advantage = reward_i - each_reward_mean_grouped
L264:             each_reward_advantage = each_reward_advantage / (each_reward_std_grouped + 1e-4)
L265:             all_reward_advantage.append(each_reward_advantage)
L266: 
L267:         combined_reward_advantage = torch.stack(all_reward_advantage, dim=1)
L268:         pre_bn_advantages = (combined_reward_advantage * self.reward_weights.to(device).unsqueeze(0)).nansum(dim=1)
L269: 
L270:         ## compute batch-wise mean and std
L271:         bn_advantages_mean = pre_bn_advantages.mean()
L272:         bn_advantages_std = pre_bn_advantages.std()
L273: 
L274:         advantages = (pre_bn_advantages - bn_advantages_mean) / (bn_advantages_std + 1e-4)
L275: ### verl modification
L276: #### Original verl GRPO Implementation
L277: 
L278:         ## line 148 in verl-GDPO/verl/trainer/ppo/ray_trainer.py
L279:         elif adv_estimator == 'grpo':
L280:             token_level_rewards = data.batch['token_level_rewards']
L281:             index = data.non_tensor_batch['uid']
L282:             responses = data.batch['responses']
L283:             response_length = responses.size(-1)
L284:             attention_mask = data.batch['attention_mask']
L285:             response_mask = attention_mask[:, -response_length:]
L286:             advantages, returns = core_algos.compute_grpo_outcome_advantage(token_level_rewards=token_level_rewards,
L287:                                                                             eos_mask=response_mask,
L288:                                                                             index=index)
L289:             data.batch['advantages'] = advantages
L290:             data.batch['returns'] = returns
L291: #### verl GDPO Implementation
L292: 
L293:         ## line 175 in verl-GDPO/verl/trainer/ppo/ray_trainer.py
L294:         token_level_scores_correctness = data.batch['token_level_scores_correctness']
L295:         token_level_scores_format = data.batch['token_level_scores_format']
L296: 
L297:         # shared variables
L298:         index = data.non_tensor_batch['uid']
L299:         responses = data.batch['responses']
L300:         response_length = responses.size(-1)
L301:         attention_mask = data.batch['attention_mask']
L302:         response_mask = attention_mask[:, -response_length:]
L303: 
L304:         ## handle correctness first
L305:         correctness_normalized_score, _ = core_algos.compute_grpo_outcome_advantage(token_level_rewards=token_level_scores_correctness,
L306:                                                                         eos_mask=response_mask,
L307:                                                                         index=index)
L308: 
L309:         ## handle format now
L310:         format_normalized_score, _ = core_algos.compute_grpo_outcome_advantage(token_level_rewards=token_level_scores_format,
L311:                                                                         eos_mask=response_mask,
L312:                                                                         index=index)
L313: 
L314:         new_advantage = correctness_normalized_score + format_normalized_score
L315: 
L316:         advantages = masked_whiten(new_advantage, response_mask) * response_mask
L317:         data.batch['advantages'] = advantages
L318:         data.batch['returns'] = advantages
L319: ## 📝 Citation
L320: If you find GDPO useful, please star and cite it:
L321: 
L322:     @misc{liu2026gdpogrouprewarddecouplednormalization,
L323:           title={GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization},
L324:           author={Shih-Yang Liu and Xin Dong and Ximing Lu and Shizhe Diao and Peter Belcak and Mingjie Liu and Min-Hung Chen and Hongxu Yin and Yu-Chiang Frank Wang and Kwang-Ting Cheng and Yejin Choi and Jan Kautz and Pavlo Molchanov},
L325:           year={2026},
L326:           eprint={2601.05242},
L327:           archivePrefix={arXiv},
L328:           primaryClass={cs.CL},
L329:           url={https://arxiv.org/abs/2601.05242},
L330:     }
L331: ## 📜 Licenses
L332: 
L333: Copyright © 2026, NVIDIA Corporation. All rights reserved.
L334: 
L335: This work is made available under the NVIDIA Source Code License-NC. Click cite77†here to view a copy of this license.
L336: 
L337: ## About
L338: 
L339: Official implementation of GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization
L340: 
L341: ### Topics
L342: 
L343: cite98†agentic-ai cite99†grpo cite100†llm cite101†reasoning cite102†rl cite103†trl cite104†verl L344: 
L345: ### Resources
L346: 
L347: cite105†Readme L348: 
L349: cite106†Apache-2.0 license L350: 
L351: cite107†Activity L352: 
L353: cite108†Custom properties L354: ### Stars
L355: 
L356: 510 stars
L357: 
L358: ### Watchers
L359: 
L360: 7 watching
L361: 
L362: ### Forks
L363: 
L364: cite109†38 forks L365: 
L366: cite110†Report repository L367: 
L368: ## Releases
L369: 
L370: ## Packages
L371: 
L372: ## Used by
L373: 
L374: ## Contributors
L375: 
L376: ## Languages
L377: 
L378: You can’t perform that action at this time.
--------------------------------------------------------------------------------
RoboVIP (https://robovip.github.io/RoboVIP/)
citeturn26882view1 [wordlim: 200] Crawled: 6 days ago; Content type: text/html; Source: open({"ref_id":"https://robovip.github.io/RoboVIP/","lineno":null}); Total lines: 181

