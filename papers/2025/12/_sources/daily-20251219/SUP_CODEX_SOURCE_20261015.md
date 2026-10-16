# Dec19 Codex 单篇 Source / owner / PRE

## 1. 身份、日期、准入

Boyle实际打开[官方release](https://openai.com/index/introducing-gpt-5-2-codex/)，December18,2025及today release字段；Newton§3已实际同日核验。新增Dec18自然日解除旧日精度门；不代授其它GPT5.2事件或未来API发布时间。实际再打开[22页原addendum](https://cdn.openai.com/pdf/ac7c37ae-7f4c-4442-b741-2eabdeaf77e0/oai_5_2_Codex.pdf)，cover同日，§3产品风险、§4/§4.2、Table4及§5.1.2必要边界；复用原Feynman已核相同版本/命题层，不扩无关bio或全部附件。

准入：仅静态要求保护用户改动，未覆盖执行中外生编辑→作者披露RL rollout里user model制造冲突、按不revert给正奖励→考虑把部署中的外生状态变化纳入训练访问分布。拟2+1+2=5，贡献是训练环境/奖励接口局部条件，不是发布产品的整体能力，因安全/具体owner缺口深入受影响域。请Newton先校准贡献/分数与必要Source；不以其API使用方式为研究目标。

## 2. 机制与反侧

§4.2明确模拟编辑在rollout期间发生，不是只在初始prompt说明；奖励不回退用户变化。没有披露user model身份、冲突采样分布、奖励权重/计算实现或训练预算。Table4四代模型avoidance为0.66/0.70/0.75/0.76，不能据此识别本干预单独收益，也非零数据丢失保证。§3 sandbox/network属于产品权限，不等训练行为保证；§5.1.2各测试盲区与内部High判定不能化成所有真实攻击/风险安全。当前release/core未见具名勘误；不按版本名预设无未来修订。未核实现/复现，硬件/precision/完整rollout成本及SLO Not Disclosed。

## 3. actual owner与锚点

已读ROADMAP及Ch31当前§后训练分支的本质差异是StateDistribution完整三段与后续hint/prefix分支；现有body讨论policy访问状态/teacher/revision与staleness，但未承载外生用户并发编辑的训练环境注入。唯一TRAIN-RLHF Ch31，不将runtime权限交Ch31或重复写Workflow。拟插在该节原“扩大状态覆盖能修复静态数据看不到的错误……”段及其source-family marker之后、“事后反馈还可以改变教师评分时的条件……”段之前。一自然段+本人末note，保持Draft，不改marker/他注/其它owner。另实际读Ch30 LoRA开篇参数表示/目标分责和Ch32 PPO开篇轨迹/advantage/clipping交接，本段未改变更新算法或adapter owner；未授锁不写。

## 4. 逐字PRE

训练访问分布还可能遗漏执行中的外生变化：初始仓库正确，不代表Agent写入时用户没有继续编辑。一个受限分支在RL rollout期间让模拟用户制造冲突编辑，并对保留用户改动而非回退给予正奖励，把“与后来状态共存”放进反馈环境，而不只写成初始提示。[官方训练披露](https://cdn.openai.com/pdf/ac7c37ae-7f4c-4442-b741-2eabdeaf77e0/oai_5_2_Codex.pdf)只明确这一接口，没有给冲突分布、奖励权重或同模型移除干预的消融；跨代avoidance分数不能单独识别该训练的效果，更不保证不丢数据。模拟编辑、长rollout和独立冲突回归增加成本，模拟用户也可能漏掉真实并发方式。部署仍需真实版本/冲突检查和外部写入权限；分布失配或保护失败时，停止破坏性动作、保留现有改动并请求协调，而不由训练高分授予覆盖用户状态的权力。

本人末note逐字拟稿：

- `SF-2025-OPENAI-GPT52-CODEX`：Dec19补Dec18；[原addendum](https://cdn.openai.com/pdf/ac7c37ae-7f4c-4442-b741-2eabdeaf77e0/oai_5_2_Codex.pdf)§4.2/Table4及必要§3/§5.1.2。Boyle拟2+1+2=5，限rollout外生冲突编辑与不revert奖励接口，保未披露冲突/奖励细节、跨代非干净因果及产品权限分责，不授零数据丢失/网络或cyber安全。必要Source与owner/PRE尚待Newton/root；未授书锁/写入/POST，不授DAY；未核artifact或复现。

## 5. 已发生Source/PRE批准与真实保存

Newton§6实际本包全部必要Source/2+1+2=5/唯一owner及逐字PRE通过；root ROOT_REVIEW§1实际读回批准本段+本人注窄锁。写前实时完整读925–941锚点及teacherhint两段、末本人拟追加处/前注；unstaged空、cached4add为已存在Alignment正文/注，完整读diff并保护，不操作index。实际按§4逐字保存一个自然段与本人末note，后顺读925–946完整state分布/扩大覆盖原段/marker/新增全文/完整hint两段及prefix交接，实际读末本人注/前注；两层限定diffcheck0。未改原段/marker/他注。Newton actualPOST、root实际读回/释放尚待，不因保存自签整合或DAY。

更新：Newton§8实际完整新增/两侧/本人note POST通过，root ROOT_REVIEW§2实际读回接纳并释放窄锁，直接协调已确认。本人只同步本人末注行政尾并实际读回，未动正文/他注；该行政差额交root读回，无需再Source/POST，不授DAY。
