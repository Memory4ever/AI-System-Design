# 2603.08806 — TDAD exact-v1

本日SUP_EXACT_BATCH4/ADMISSION_BATCH4及独核AB/date夹证复用，2026-03-11公开/current无撤回；[v1](https://arxiv.org/html/2603.08806v1)§3–6/§8、§4.1–4.3/Table4/Appendix1必要操作定义actual读。2+2+2=6，hidden/mutation安全与回归信号深入；不借pytest成熟性加分。

YAML tools/policy/priority/decisiontree/respondschema→TestSmith造tests、PromptSmith据visiblefails迭代prompt/tool-description→一次respond/mocktrace断言。MutationSmith后置仅看artifact/intents不见tests；activationprobe必须检出行为改变，5次未activate排除，87%激活，不是全部mutations覆盖。v1/v2 hiddenINV/DIR对单trial固定，生产hiddenfail改visible意味着未来应换新heldout，不会永远独立。v2只用v2tests从v1prompt起，编译后才验v1invariants/SURS，非形式语义compiler或preproduction guarantee。

四Spec10–14decisionnodes，同Sonnet4.5充所有roles、默认temp、无seeds/个案retry，Dockerpytest/mockfixtures仍不冻结LLM采样。24trials=4spec×2version×3；Table4v1成功11/12、v2仅7/12，HPR97.3/77.7与SURS97.2条件在18个成功run，失败6个不能从denominator消失。Expensev2只有1次成功且无CI；v1仍survive HALLUCINATE_NUMBERS/SKIP_RUNBOOK_LOOKUP，v2MS100仅activated有效mutants，不能证明全错误空间。v2fail2为spec-conflicting tests、3为budget，test oracle也可错。30–60min/spec与45.15美元仅成功run不等总失败/开发/评估账；无anti-gaming组件独立ablation/DSPy matchedbaseline/其它model/50+node系统。未运行artifact，全部代码/附录不强制。

owner AGENT-PROMPT，actual Ch74Lifecycle109–145/typedrules146–175/PromptInjection94–109、Ch73/75开篇。已有prompt版本、regression/canary/rollback与抽取非行为，未具体拆“可见生成测试→hidden更新→mutation激活分母→成功条件编译”测量权。逐字PRE插“修改一个词也可能改变行为，因此需要offline regression…”段后、repository instruction semantic-binding前：

> 自动把 policy specification 编成 Prompt 与测试时，测试 oracle 也进入待验 artifact：可见失败能驱动改写，却可能让生成器只满足当前断言；hidden cases 与行为 mutation 应在候选冻结后另行检查。Mutation 必须确实改变目标行为，未激活或被排除的项不能混入 mutation score，编译失败的 run 也不能从成功率与预算中消失。[有限编译实验](https://arxiv.org/html/2603.08806v1#S5)中的测试通过与高分只覆盖所选 specification、mock tool 和成功编译人口，不授部署安全。发现 hidden failure 后可把它提升为 regression，但下一轮须更新独立 held-out，保存 spec/test/prompt/model/tool revision 与失败账。生成、验证、mutation 和重复调用均付费；测试相互冲突、oracle 不可信或预算耗尽时保留人工审阅、原 Prompt 与 canary/rollback，不由测试生成器同时宣布规则正确和外部 effect 可提交。

reviewer已实际打开必要v1及具体owner局部，Source/date/6分与逐字PRE通过；root授Ch74指定单段及本人末注窄锁，已按逐字拟文＋对应SF marker写入Lifecycle旧regression完整段后、repository instruction semantic块前。作者实际完整邻接及自身末注顺读，锁释放，root非writer实际顺读Ch74 108–144完整邻接及301本人注，actualPOST PASS。必要Source与Books整合完成，未核artifact/复现，不授日级Gate。
