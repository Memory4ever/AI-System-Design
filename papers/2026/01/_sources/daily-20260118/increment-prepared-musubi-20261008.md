# Musubi Jan17 localized compatibility and target-scope release

有界四主题日期补检在fork README发现Jan17两条具体release，回原maintainer kohya-ss/musubi-tuner PR851/852；fork与后期HF上传仅发现身份，不采用其日期或技术权威。不扩Musubi普通PR/其它框架。两事件同一工具family，不是两篇基础模型论文或Hunyuan/Qwen厂商发布。

待root准入校准：原有通用LoRA格式/所有target生成约束→PR851修Z-Image参数名转Diffusers消费、PR852允许移除原图target但保condition与更新output数协议→不能由‘LoRA已训练/目标图集合’默认下游adapter被应用或需重复生成原图。局部具体新增接口而非借LoRA原理、架构名称与未经matched的速度。拟1Design+1Reach+2Durability=4 OnlyReport；兼容纠错影响范围必要深审，但不新增Books通用机制/不冒exactExisting。

原件：increment-musubi-prcore-20261008.json PR851 conversationL177–255、PR852 authorL165–227（‘Without’两句有表述混淆不采为对照）；increment-musubi-files-20261008.json官方API两PR各4changedfiles（包括doc/Japanese duplicates，不假称8独立mechanisms）。完整必要patch已实际读：851 convert_lora.py +121–133，在attention.to/feed.forward路径分支替换to.q/k/v/out→to_q/k/v/out与feed.forward→feed_forward，docs改成Diffusers consumer并声明旧script可能在nunchaku失效，既有converter继续可用。没有跑ComfyUI/nunchaku、无匹配全loader/version/quality矩阵，故只支持名字映射及维护者局部兼容声明，不保证所有weight有效、输出质量或普遍consumer兼容。

852 qwen_image_train_network.py assert只layered，call_dit noisy_model_input切掉第一target并num_layers−1，随后保持control拼接；latents/noise同步切片，非删除conditioning。docs§training明确quality impact unknown，inference输出层数参数须按训练是否移除适配（文档有N−1规则但本报告不用作执行recipe），不是mask原图loss且仍计算同完整target。缓存不是唯一consumer：提交由cache移到training。本次没有公开匹配step/quality/runtime/hardware总费用experiment，作者缩时/省memory只定性，不能授质量保持、通用加速或用附近VRAM1024/B1表当该flag消融。

日期：increment-musubi-prdates-20261008.json为本次官方API实际字段转存，851 createdJan17T01:29Z/merged01:34Z、852 created02:05Z/merged07:21Z，均BJTJan17；exactmergeSHA8510864929/852f021c78，files patchhead851eed0d95/8523bcaaba，head与merge身份分开。PR当前closed且merged，不是撤回；当前必要PR/patchdoc没有可见撤回或纠错标记，不遍历完整后续版本。正式采用仅本窗两个release接口变化，不重计Jan11基础Layered支持或Z-Image模型首次公开。候选/评分/证据还待非作者决定；原0候选不动，无Books锁/写入。
