# 2026-10-06：两家族必要证据与停止范围

窗口UTC 2026-10-05T01:00:00Z～2026-10-06T01:00:00Z。作者oct06_daily实际阅读以下原PR core、精确实现和关键反侧；root非作者独核指定core/采用命题，不是全库审计。均未运行实现或复现实验。

## C01 / SF-2026-UNIRL-20261005

本日是main合入公开实现事件，不是bug首次披露。原[窗内commit API](https://api.github.com/repos/Tencent-Hunyuan/UniRL/commits?since=2026-10-05T01%3A00%3A00Z&until=2026-10-06T01%3A00%3A00Z&per_page=100)8项；合入时间以PR merged_at核。#547=2026-10-05T03:05:03Z；#528=03:34:23Z；#403=09:09:20Z。#403 commit committer秒值09:09:19Z不覆盖PR公开字段。三核心2+2+2=6按家族一次计分，正确性纠错深入。

### #547：正确layout不能由平静ratio签字

[#547](https://github.com/Tencent-Hunyuan/UniRL/pull/547)问题/validation与[0a82feb exact diff](https://github.com/Tencent-Hunyuan/UniRL/commit/0a82feb2240f8b3b2964ec95f4e60215f827b3cc)：`unirl/rollout/engine/vllm_omni/pipelines/bagel/pipeline.py`的`_prompt_text/_source_image/_is_batchable_t2i`三helper从batch `.prompts[0]`改single `.prompt`。先前forward已unwrap，图像helper返回None使it2i不注入KV context，走上游fixed980 SigLIP/采样VAE posterior/source尺寸canvas；trainer replay走Navit/mean posterior等不同序列。512输入偶然与512输出尺寸匹配，不认证其他source尺寸。

作者controlled运行：BAGEL-7B-MoT LoRA，16prompts×8samples，512×512，rollout/trainer一个8×H20节点、EditScore-8B另一个节点，vLLM/vLLM-Omni0.28.0。旧recipe old_logp_source=replay使trainer自比；显式rollout概率比较时旧worker/train KV长度5938/2263，而ratio均值约0.999972；改后三helper2263/2263且ratio约0.999984。比率平静不是conditioning一致的充分证据。首batch generation49.18→36.78秒、reward2.80→4.62及后续reward只属改变conditioning后的作者对照，不是同分布机制净提速/普遍质量增益。实际执行batch/concurrency、文本输入长度、采样步数、其他精度与SLO为Not Disclosed；16×8是采样组成，不推并发128。

采用边界：先绑定源图/预处理/latent采样/KV layout/canvas及old概率来源，再解释ratio。已有Ch33版本、group和view身份原则仍有效，但此前无该实现反侧；已融入`TRAIN-GRPO`「版本窗口与Draft复用仍须保护Trajectory Identity」L1382一段及末注。没有声称后续layoutguard已在本窗完整交付，也未沿版本史扩审。

### #528：逻辑sleep、物理释放与wake组合峰分别验收

[#528](https://github.com/Tencent-Hunyuan/UniRL/pull/528)Summary/memory-saver validation/wake窗口/R sizing limitations与[54cc7b6 exact](https://github.com/Tencent-Hunyuan/UniRL/commit/54cc7b69698332b7c1b167b174263fe02ce81ea7)：实际读`unirl/config/validation.py`、`sglang/config.py/engine.py/backends/http.py`、`harness/protocol.py/tool_agent.py`、`trainer/agentic.py`和相关README。

- saver缺失时SGLang安装Noop TorchMemorySaverAdapter，release返回成功仍不释放。配置验证Agentic严格raise、AR在实际sleep场景warn；启用saver和CPU weights backup须重新核wake空间，并支付host副本和迁移成本。
- 作者Qwen3-4B fp32/2×H20约97.9GiB，srt0.5.19、torch2.13cu130：saver off fraction.3无释放71–73GiB；on .3三轮2完成1OOM；.4三轮完成；.45两完成；.6一次在wake达约95GiB OOM。wake先于backend offload、缓存allocator保留block不能自然被resume复用，不能由rollout峰推出全步可行。只用这条有限反侧，不将.4设成全负载默认最优。该memory对照实际有效输入/输出长度、执行batch/concurrency及SLO为Not Disclosed，不将后述另一Agent评测的320 trajectories混作这里的并发或长度。
- `context_length`唯一config owner传server并clamp max_new_tokens；input≥context_length−6失败。最终generation截断或后续context超限为overflow，首turn之前为failed；overflow仍可像completed评分。实际trainer先计算advantages，再在opt-in `mask_overflow_loss`时跳过该trajectory生成训练parts：保留组baseline，只删除梯度。它改变estimator，不等价于先删样本重算baseline，也未获无偏证明，默认mask false。
- observation只按字符上限clip，不能代token预算；HTTP nonretryable4xx不再重试（408/409/425/429例外）。有限40rollouts HotpotQA-hard320trajectories/localWiki的R≈.05是该KV-offload场景，不认证普适tier判定或Agent总质量。

采用：`TRAIN-DISTRIBUTED-TRAINING` Ch36「Training Memory Contract必须覆盖组合峰值」L1779窄段，补充sleep API≠HBM已释放与wake-before-offload验收。Ch36已有overlap状态lifetime/组合峰与backend全局state，不替代；overflow、字符clip/R常数留报告，不扩owner。

### #403及其余有限事件

[#403](https://github.com/Tencent-Hunyuan/UniRL/pull/403)原body仍描述较早bf16/mode未设置，必须区别最终[94e8f26](https://github.com/Tencent-Hunyuan/UniRL/commit/94e8f26b8768a3695b5985c2fa072e07d9dbfa0d)。实际`examples/diffusion/minimax_h3/minimax_h3_t2va_trainside.yaml`最终header明确旧两seed+0.00234/step不是当前config；L70附近master_dtype fp32、cast_forward_inputs false，reward ImageBind mode all；algorithm old_logp_source replay。不能将旧曲线转授最后recipe有效性。

原两seed各45rollouts的256×384 canvas、10 SDE steps/group16/lr1e-4/1update，与旧768×768/3steps/group4/lr3e-4/2update同时改变多个knob；FlowGRPO/NFT与eta共线，不能因跨objective比较认定eta导致plateau。ImageBind audio_video+CLAP没有prompt→video项且embedding alignment不评分artifact；NFT sibling黑/静音collapse仍可能涨reward。最终改mode all/precision后须新验，旧slope和p值不采用为新收益。此事件纠正recipe事实与归因，只有报告，不增加书稿配方清单。

#542 [fd87af1](https://github.com/Tencent-Hunyuan/UniRL/commit/fd87af1605315a6d58c9116dd6f1afca4ab7f251)实际5 README/YAML，GenEval detector paths明确非空、download_models必须目录、v2.28.2；GenEval2配置dataset缺条目failclosed/allow_fallback与local缺list得0不能混同。无新API或数据格式，作为部署/评价辅助边界仅报告。root另读维护者纠偏core。#560唯一版本guard为局部兼容辅助；#553仅bump0.2无release；#532/#531内部README/agent写作规则范围排除。这里没有将普通8commit全部默认长期owner。

## C02 / SF-2026-QWEN-CODE-025

[release v0.25.0](https://github.com/QwenLM/qwen-code/releases/tag/v0.25.0) API published_at `2026-10-05T09:44:40Z`；精确tag→commit `6788c035698a0ada471c958d1e789e96c6cddd9b`。2+2+2=6，实际发布/权限纠错深入相关部分，非全release审计。SDK/desktop同CLI包装不增家族。

### 默认恢复是带平台条件的交付事实，不是恢复保证

[#13211](https://github.com/QwenLM/qwen-code/pull/13211)mergedOct3属于窗外实现背景。实际精确tag [application.yml](https://github.com/QwenLM/qwen-code/blob/6788c035698a0ada471c958d1e789e96c6cddd9b/packages/sdk-java/managed-agent-server/src/main/resources/application.yml) L79–115：embedded broker enabled默认false；L100 durable-local-process true、L101 trusted-local-reboot-recovery true；operator/verified-workspace recovery false。这是启用broker后的默认选择，不能写所有Qwen Code自动开启broker。

原core要求Linux machine-id/boot-id、owner UID/0700且无symlink或workspace包含的state目录；nonLinux/缺失malformed identity fail startup；static provisioner需显式关闭trusted reboot recovery。持久记录不认证当前head的物理reboot，LOST-on-reboot wedge仍open；portable synthetic identity测试/Mac测试不替Linux精确head物理验收。独立recovery scheduler避免阻塞单线程pump只是实现边界，不是故障完备/恰一次保证。release“No known breaking changes”不能掩盖这些平台/启动迁移条件。

### #13406：native不适用先拒绝，上游最终参数仍只判一次

[#13406](https://github.com/QwenLM/qwen-code/pull/13406)merged_at `2026-10-05T07:26:00Z`，精确 [ed88833](https://github.com/QwenLM/qwen-code/commit/ed8883320d09c469d132f95e447eddc467805209)。精确tag [Session.ts](https://github.com/QwenLM/qwen-code/blob/6788c035698a0ada471c958d1e789e96c6cddd9b/packages/cli/src/acp-integration/session/Session.ts) L14045附近：agent-host native-only confinement guard以上游undefined构造，permissionChecked:false，拒绝EXECUTION_DENIED/not_started先于permission RPC/hooks；L15167附近最终getToolInvocationGuard以invocation.params、permissionChecked:true、session/cwd调用。hook改写后仍检查最终对象，不能把early allow缓存到effect，也不双调用stateful upstream。

实际原Session tests包含outside deny无permission RPC、inside hooks改写后upstream仅一次/拒绝不执行、inside后继续并只persist一次final。作者controlled-provider macOS Host/WebShell有限E2E，旧baseline本来没有outside文件内容泄漏，旧bug是无意义permission RPC顺序，不能描述为已证实的旧泄漏漏洞；未提供Linux/Windows/realmodel对应验收或完整生产安全证明。

最终Books仅报告：当前Ch84 Primitive Effect/Resume/current-head及Ch72 actual-effect独立授权承载一般职责；本次采用的主要是0.25平台/default配置与局部实现回归，不把generic owner论点变成Linux reboot保证，也不为版本事实制造Books diff。昨日13064/13069同family既有事件只定点去重，不再次评分。

## 实际审阅停止

支持与关键反侧已足够：C01三核心和两Books窄差额；C02两core及精确stable配置。未审全PR讨论、所有release fixes、全库、default revision diff或proof附件；不以未运行optional代码保留普通待办。必要正文/日期皆可取得的两正式候选无外部Evidence hold；arXiv等另见来源缺口，不用于这两家族正面论证。
