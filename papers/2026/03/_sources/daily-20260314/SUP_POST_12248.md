# 12248 actual 非写入者 POST

复核者 mar14_supplement；Books 写入者 root。仅 03-14 补充 Mar13 BJT；不授 DAY。

## 实际检查与原证

真实顺读当前 Ch29 47–119：schema/拒答配对/ChunkFT → 完整条件最大似然与 masked token 数学 → Logits 解释 → root 新94/96两段 → Concept Tokens/ER-CE/多语校准/人票及 nuisance 表示分支。首输出末端截断后实际补读103–119，未以截断算全部邻接。实际读1253–1266结论与本人1257末注/相邻旧注；不是只看marker。Ch28/30入口及Ch33具体baseline交接复用未变化的必要PRE。

回对 exact-v1 原件：§2.1 条件均值/feature richness（本次B30–53），E Eq89–94完整与F nested-prefix/mask全段（本次B423–446），完整Table6/直接H1反侧（本次B497–505）；此前有效必要§2–4/Alg1/G成本协议复用。不重复全D证明、所有H图、代码/复现。

## 结果：PASS

新段明确 sequence-mean feature 目标不等 teacher-forced CE、frozen representation 不取得真值权限，完整分布连接保留足够丰富feature条件，有限feature/短rollout/reference人口仍可能漏模式。E特定pairwise奖励的其他reward含当前sample，普通去条目仍依赖；正文实际同时排除其他项中的该贡献、按剩余样本重新归一并限定同prefix条件独立 n>2，符合Eq93的n−2定义域。不认证印刷Eq94三行完全相等、也不声称n=2不存在任何其他baseline。

正文保留同批whitening/偏置/std或clip不能继承固定feature无偏，Ch33通用PG/baseline仍唯一owner。Nested短续写只看自己的prefix/采样历史，不能读其他续写或未来gold，不作全部署人口匹配。冻结feature、rollout/统计/参考与调参付费，Table6真实反退与per-step比SFT慢没有抹去；verified CE/outcome/originalcheckpoint并存回退，原CE数学/ConceptToken和其他分支未被覆盖。

末注精确版本/评分5/有限feature、n>2及归一/whitening/反侧与正文和原证一致，目前仍待POST，交root仅更新自身note并释放。没有写Books，没有核代码/全证明/复现实验或授生产性能/完整语义真值。
