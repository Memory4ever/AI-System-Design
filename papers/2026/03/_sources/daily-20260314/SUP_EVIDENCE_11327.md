# 11327 MR-Search：必要 Source 与 actual Ch33 NC

mar14_supplement；精确[2603.11327v1](https://arxiv.org/html/2603.11327v1)，SUP_NECESSARY_11327.raw，GET200/355081B/2026-10-09T15:33:41.965218UTC见SUP_CORE_CREDIT_JUDGE_MANIFEST_RESULT.json。九作者/题名DOI、完整题摘/Preprint说明与v1/v2当前history已实际读；仅v1为采用版本，晚v2本身不证明重要事件，未识别具名先稿或撤回/勘误说明。官方Mar13日级夹证的owning/findable/URL/arxiv.content与Wed21:40:26UTC v1、registered见SUP_DATE_SECOND.md/本ID raw，有效official ID非预分配/日程原证复用；提交/注册单独非first-public。非作者单项仍待实际核。

单episode终局信用忽略跨次探索→同题meta-episode保reflection历史、各episode可核答案return并按同轮RLOO及未来折扣合成→需分别定义训练sampling/credit单位与测试context adaptation，不把终局成功当所有reflection真值。**2+1+2=5标准完成**：新增训练单位与return安排是重要post-training机制，作用范围仍局限搜索policy组件；不把RLOO/PPO成熟理论、无critic或反思模块名称加分。

## 实际必要原证

实际§3.1–3.4 Eq1–10/Alg1全部、§4.1–4.4 Tables1–3/Fig3–5文字及直接Limitations，A.1.3配置；没有读case全集、所有曲线或代码。每同题采G独立meta episodes，内部N次search/reflection依赖此前完整context；每次答案由同gold verifier打分。Eq7仅同n其他meta-episode回报作LOO baseline，Eq8对未来折扣return，Eq9 clipped/token-broadcast并mask工具输出；同turn不保证同history/state，baseline独立于当前action的受限性质不授完整clipped/长度权重无偏或token因果。Eq5 N+1/Alg1 N、Eq8 N上界及Eq9记法存在索引不齐，本轮不还原唯一码路径。

§3.4 Eq10 mask的是对应episode即时reward，再累加未来credit；prose称exploration不贡献gradient不作为采用结论。具体两episode m0=0/m1=1时A0仍有gamma*rtilde1，mask reward不等零掉前轮policy gradient。也不能把其余反思token自身评分与答案verifier混同。§4.4前两exploration/后两exploitation改总轮数，Table3 exploration的NQ48.3低于50.2、step-level48.6及Musique16.3低于22.1，shortcontextBamboogle47.2高于45.2但平均未等效，不说全部变体逐任务更优。

2018Wikipedia/E5 top3、NQ+HotpotQA训练、ASearcher90/10，Qwen2.5-3B/7B；EM normalized/最后有效答案，主要MR默认turn3。A1.3 AdamW1e−6/300steps、group5、训练8K/16Kcontext、各episode3/5toolcalls、temp1训练/greedy评价；8H10080G训练+2H100 retriever，precision/生产concurrency/deadline及完整搜索/训练token成本未披露本轮可核值。三次run shade不等三独立训练seed认证。相同retriever返回数/步骤数不等总tokens、反思轮或完整费用匹配，更多search calls不能称免费process reward；没有longform/多异构工具/frontier训练验证。不核实现/复现。

## Actual owner 与具体已有覆盖

ROADMAP `TRAIN-GRPO`；实际顺读Ch33 870–888跨步骤/episode→重复试验→压缩conditioning→Measurement完整邻接，1593–1623 Hierarchy→history identity→同history即时分支→Turn Index→其他trajectory baseline完整局部、2298–2320conditioning/action-token credit；Ch32/34入口实际核。现有870–882承载同任务多episode、reset/retained history、测试冻结参数、reward/credit身份与多次试验全预算；1593–1623承载按history/behavior/group冻结条件、同轮号不证same state、可靠return/critic退路、other-trajectory return baseline与陈旧支持边界；2308局部已分开action/token信用和同reward广播。不是只凭同主题授NC。

本稿可采用的训练单位/跨次context适应和credit/预算边界已有上述具体正文承载；同n RLOO折扣是该接口局部配置，没有已证新可行性条件需另写长期段落。**标准完成/已有覆盖/Books新写0**，保留可选mask的原文/公式差异，不采用零gradient或全clipped无偏保证。root实际必要Source/完整owner/NC独核PASS，见本日独核文件“11327 / 12246”节；不授DAY。
