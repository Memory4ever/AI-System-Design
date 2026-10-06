# 02/20 第二十六有限证据包：Dense teacher target 与 graphon边界

## 2602.15971v1 — B-DENSE: Branching For Dense Ensemble Network Learning

2+2+2=6，Ch24拟parallel auxiliary-state监督接口差额深入，待rootPRE。当前exact-v1 abs题名Learning，官方v1 HTML及11页v1 PDF封面题名SupervisionEfficiency；PDF仍印2602.15971v1，方法/评价对应，不借后版效率改名新增机制，不据题名字串单独作外部hold。原链接[exact-v1 PDF](https://arxiv.org/pdf/2602.15971v1)已实际打开对应方法；V3_REVIEW_2602.15971v1.html §3.1:130–135、§3.2:138–169、Alg4:183–195、§4:199–264、必要weight tuning A1:375–385。事件页无可见撤回/勘误。日期桥lower2026-02-19T09:00+08，Registered2026-02-19T02:35:11Z+1秒upper10:35:12+08。

Student最终层重复teacher weights，输出K*C channels分别监督同输入对应teacher K个中间状态；共享backbone，weighted branch loss，推理只用终点通道。它是平行辅助读出监督，不是推理逐branch更新、并非自动生成连续曲线/精确积分。§3.2 piecewisequadrature只是解释，noise预测器不普遍就是PFODEvelocity，不采用为全理论正确或路径证书；finite targets不能约束全连续轨迹。训练teacher state存储/额外head梯度/weights选择仍付费，“~.01% FLOPs/近free”不采用全pipeline保证。

PD DDPM/CIFAR32 teacher1024→128、K2、每轮50kupdates/batch128/AdamW2e−4/L4约4–5h；SFD EDM CIFAR32/ImageNet64、K4/NFE2/A10044min/3h，作者设置声称同原hyperparams，但weights在CIFAR2-step Optuna再选，不授等总调参budget。FID50k，未披露repeatedseed/CI、precision/inferbatch/concurrency/tailSLO。CIFAR2step4.53→4.40小幅；ImageNet2step10.25→9.57但3/4/5step6.35→6.54/4.99→5.97/4.33→5.91反退；A1又baseline10.57不混口径。teacher artifacts继承，large latent/video/3D尚future，不将qualitygain作全面优势或容量根因已排除。

Actual Ch24:509–515已分distribution/组合一致及左右时间map，未承载同输入平行多头teacher-state auxiliary监督而只交付终点head的设计。拟在组合一致段后1段，把辅助监督/交付状态与真实trajectory分开，绑定teacher/schedule/branchweight/head选择，费用及多步反侧近文；回退原endpoint蒸馏、减少branch或保多步。请求Ch24单段+自身末注锁，尚未写。

## 2602.16196v1 — Graphon Mean-Field Subsampling for Cooperative Heterogeneous Multi-Agent Reinforcement Learning

2+1+2=5，中心理论桥接争议需深入定点核；拟暂缓，不写Books，待root独核。V3_REVIEW_2602.16196v1.html实际§2–3:99–190、Alg1–2:197–230、§4–5:232–284、直接限制288、匹配evalA4:1014–1055、C3:1180–1197。日期桥lower09:00、Registered02:40:30Z+1秒upper10:40:31+08；exact-v1无可见撤回/勘误。原源角色仅形式分析/作者toy，不执行代码。

Graphon rownormalized权重iid有放回κ邻居，状态/动作joint histogram z及状态marginal g；有限S/A、bounded reward、reward/transition Lipschitz、generative simulator。κ只在固定|S||A|下poly，指数κ^(|S||A|)且全n在线loop/graphweight维护，不是任意LLMteam零成本scale。§3:172–174 max over compatible z明确只是upperbound、不可由单agent控制，但随后greedy action真实team近优需要可实现policy闭合，不能由contraction直接推。

更直接核心反例针对Theorem5.1/C3：原式只用TV(g_z,g_zhat)，即使joint action不同而当前state marginal相同，右边也是0。符合Assumptions3.4–3.7的简单环境：S=A={0,1}、r(s,a,g)=g(1)、P(s'=a|s,a,g)=1、γ>0、全1 graphon。当前neighbors均state0，joint z对action0/1各半；κ=1抽到(0,0)概率1/2。两者g=δ0，TV0；从Q0=0，Q1=g(1)，第二次backup的下一邻域state由邻居当前action决定，full Q2=γ/2，sampled Q2=0。状态marginal的即时相等不控制future g，因此该全t零差命题失败，§5后续rate依赖桥隔离，不称采样均值无偏/固定operatorcontraction都错误。若作者另有不公开的surrogate action过程，仍需给出同版J_n/J_κ完整定义与closing assumption，不能替补。

A4仅25agents/5×5fixedpositions/3state3action/H100、IntelCPU1TiBRAM、30seed、κ1–24/MC50/offlineexhaustive250iter/gamma.95。实测为可控离散robot proxy不是LLM现实协作；A4:1039把joint histogram缩成statehistogram并说即时reward/transitions只依赖g即可，但action→neighborfuture正是未处理接口，不由局部score关闭上述反例。实际Ch82:344–357区分offline策略population/onlinebelief与有限payoff，不用同主题书写取代争议。终态重开需同版修正版state-action stability/realizable decentralized policy证明及采用的surrogate实现；当前sampling/局部toy仅报告，不支持近优/安全/通用population性能保证。

## 停点

两项必要证据准备待rootPRE/处置；普通剩余不伪装external。16375下一项method/eval已读，owner在生成式检索identifier成本分支，仍待提交其具体差额。无stage/commit/push。

## 独立处置追加（2026-10-05）

15971 root必要PRE与Ch24 body511/505–519完整邻接/自身末注2077实际POST通过，锁释放；16196限定Theorem5.1/C3 state-only稳定性→近优依赖争议隔离root实际独核通过，保固定operator及局部toy；不授日级。
