# 10505 VeriEnv：clone状态、SDK verifier与训练人口的Source/PRE

仅Mar12 BJT补充自然日；完整exact-v1 AB、非作者准入与第二批日级夹证有效复用，不重跑日期。官方 https://arxiv.org/html/2603.10505v1；SUP_CORE_10505.raw/txt与SUP_CORE_LAST_SECOND_MANIFEST_RESULT.json保存GET200、307182bytes、UTC2026-10-09T16:26:01.296624。作者实际完整§3.1–3.4、§4.1–4.2、§5.1–5.3、§6–8/Tables1–5；A.1.1–1.2/A.2–A.3具体实现流程、B.1–B.3标注合同、Table7全部相关前段example实际读。图仅正文/caption，不授像素曲线数值；不读全部website截图/完整生成prompt或引用全文，无代码/复现。

## 实际新增命题与最低投入

真实网站探索有副作用/难reset且外部答案未必可核→screenshots重建可执行(C代码,D数据库,P受控SDK)，由SDK构造任务前提与terminal checker→训练仅收所定义checker的成功轨迹。这把环境生成、随机初始化、验证器及训练acceptance人口接成具体接口，不借成熟sandbox/程序判分或RFT本身计增量。拟2+2+2=6：新状态/训练admission接口2、environment创建与evaluator权限/训练数据两侧分责2、可复用reset/语义/transfer资格2。安全/设计接口触发必要深入，已完成；拟受限Ch66两段，未授Source/PRE/POST/正式。

## 方法与反侧

§3.1 GPT5.2/Cursor coding agent从Mind2Web screenshots重建(C,D,P)，本地文件/terminal及Playwright debugging产出start/reset脚本；作者明确不完美等同原站，只拟保功能结构。截图不证明原后台语义/数据、真实账户或外部效应完整复刻。§3.2 task=自然语言+SDK validation program；生成器先模拟查询验证可行性，再生成terminal binary rule，示例must_include可能只查回答子串。§3.3 agent仅browser，validator受控SDK查内部状态，按成功reward筛轨迹做rejection fine-tuning；没有当前RL训练结果，§6.2 RL是未来方向。固定checker确定可复算，不自动真实任务oracle。

§3.4 149网站7400tasks；人审四CS graduate，两个subset各15items、每subset双标，不能称独立60cases或全7400gold。功能90%/实际正文90.3%，visual4.7，task executability90%，**judge correctness76%**，meanκ.61仅同伴一致。主要错误reset未保populate随机seed，checker原答案随DB变；作者说重跑validation可修，但未报告全池修后分母/独立复核。必须绑定reset seed、DB版本及reference生成时间，不能照录保证任务正确或“无人工监督”=无需人工校准。

Table7 example含must_include“2”、名字/价格子串与fuzzy numerical matcher；真实语义、路径/effect和答对文本不是同义。checker可能误收/误拒，任务/裁判都由同LLM/SDK产生仍有common-mode。§8声称external network disabled、SDK不含payment/authentication/PII，内部状态只validator可见；这仅作者协议声明，非实际sandbox artifact认证。正文/A.3/B.2仍含signup/login/session修复及Table7 bestbuy Sign in，范围口径需说明（可能指模拟登录与真实认证区分），不擅改成已验证无任何认证功能，也不推作者实际越权。

## 对照、预算与外部效度

§4.1 97网站训练，明确排除目标test网站重叠但原exact列表未披露；136candidate→97为39构建失败的条件人口，与总149library不能直接一一同分母。GPT5.2/Cursor每站平均83.5min/$3.6含debug/taskgen，非完整policy采样训练/部署费用、非每站上界；A.1.2 LR1e-5/twoepochs/10%warmup/maxseq8000/ZeRO3/GA2/twoA40，缺batch/precision/seed/匹配轨迹总token/budget。A.1.1其他codingCLI早退/模型多模态能力缺失仅作者观察，不授通用框架或模型结论。

WebArena-Lite五Docker站；Mind2Web-Online300原tasks因blocked过滤到220，**采用WebJudge7B模型评trajectory**，不能称外部评价也全部SDK确定checker。Proprietary带星结果来自既有paper，非本轮统一复跑/相同人口。T4 Qwen total7.88→13.94、GitLab13.89→12.50退；Llama3.03→12.73差9.70，正文写9.09有口径冲突，保表/文原值不补修。T5 Qwen13.18→20.45但Hard11.63→6.98退，Llama11.36→24.55且略高ADP24.09，不授所有slice/显著或纯validator因果。

§4.2把WebArena站当真实service代理，只在clones训练；原测试站本已sandboxed，3类别/几个phases正文曲线不等真实商业站无gap。§5.1只有限环境份额范围升趋势，未给统一训练token/trajectory预算、独立CI/全部artifact；环境更多可能同时改变训练量/人口，不授普遍scaling law。§5.2 39failed多server/taskgen缺、port/CORS；Docker隔离为建议而非全站实现已核。§5.3 PAE比较同时改任务来源、环境与judge，非只程序checker的因果。§6 dummyPDF/video占位可能减少真实业务语义，测试必须声明omissions；§8 misuse/IP/ToS与真实部署仍待独立安全，不由受控训练提升授生产权限。

## actual owner与具体差额

唯一PLATFORM-EVALUATION-SYSTEM [Ch66](../../../../../books/part-06-ai-infrastructure/66-evaluation-system.md)，ROADMAP精确ID已核。实际完整287–310 harness/environment，包括刚落SpecOps两段；1364–1392 simulator→DynamicReference完整；4500–4525 ConstraintGraph合法解/模拟效度完整。现文已讲component分责、resolved spec、live reference不能自签真值、模拟不能代真实，**未具体承载从screenshots生成(C,D,P)并让task factory/SDK oracle绑定populate/reset状态后产训练acceptance人口**。不重复一般verifier/permission原则。Ch31只消费监督信号，真实tool effect由Ch78接交（Ch65为KAI、Ch67为Monitoring，不冒充工具/数据owner），不开第二owner；SpecOps真实有限setup API联改目标而非本项重建新backend，不能当同接口。

拟放Ch66 SpecOps两段之后、Git对象身份段之前两段，连着上游测试spec再解释可执行环境的另一受限生成分支，保持后面访问边界链。请求root两段窄锁，作者不写Books；需独立Source/actual owner/逐字PRE先核。

### 逐字PRE

真实网站不能安全反复探索、也难恢复同一状态时，可把截图重建为应用代码、数据库和受控内部SDK组成的训练环境，再让task factory用SDK检查前提、生成terminal checker；被训Agent仍只走browser，SDK只供validator事后取证。成功轨迹筛选因而消费的是“当前clone状态下该checker接受”的人口，不是原网站真值或所有合法行为。生成代码、populate seed、reset前后DB、任务与reference/checker须共同绑定；reset后数据改变却沿用旧答案，会让确定性的程序稳定地产出错误奖励。环境重建与oracle生成可以扩训练面，但共同生成者、占位媒体和规则遗漏不能被可执行性消除。

[VeriEnv的有限必要原证](https://arxiv.org/html/2603.10505v1)中，人审judge correctness只有76%，外部Mind2Web评价又采用模型judge；克隆可运行、任务可执行、checker正确和真实站泛化须分账。97训练网站、39构建失败和过滤后的220评测任务不授全站覆盖，部分任务slice退步；平均构建费用还不含完整采样、训练、oracle复核与部署。测试者不应由自身checker判分签发真实服务权限，原站语义、seed/DB或checker不能独立核时隔离任务/Unknown，保留固定回归、独立环境效果与人工校准；高副作用真实调用仍需原权限和部署验证，而不是用合成环境的pass替代安全。<!-- source-family:SF-2026-ARXIV-2603-10505 -->

## 精确停点

6分必要Source/actual owner/两段PRE ready，送非作者实际原源与owner裁；未formal/未写Books/未POST，不等其他日期/全pool完成。强deterministic可靠、无人工、全gap小、普遍环境scaling/纯组件因果及真实部署安全不采用，普通缺artifact不伪造外部终态。
