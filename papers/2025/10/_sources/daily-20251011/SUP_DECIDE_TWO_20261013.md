# SECOND两个局部N：实际最低决定域

作者Kierkegaard；root指出准入事实未清后仅实际读下述精确v1方法/评价/反侧，不重22AB或全稿。原件均curl200/exit0：07629为230922bytes、07869为152265；[Clinical原件](SUP_DECIDE_07629_V1_20261013.raw)、[U0原件](SUP_DECIDE_07869_V1_20261013.raw)。此包是作者N→窄P提案，须root实际非作者核；不评分/授当窗公开日、正式Evidence、Books或医疗/physical安全保证。

## 07629：只保留候选覆盖与验证人口条件

实际[精确v1](https://arxiv.org/html/2510.07629v1)§3.1–3.3/4.2/5.3 Tables4–5及Limitations。tree billableleaf/同parent siblings/同grandparent cousins，与index无向graph1/2-hop外链分别扩展；contextualrevision由LLM在candidate descriptions/codes选argmax，不是formaltrue verifier。标准exact/F1与prefix1/2/fuzzy ancestry测量不同，不用near-miss接近认证可用代码。

决定事实是原**standalone verification候选由gold seed扩展，因此gold总在集内/上界100%**，而full pipeline由model-predictedseed扩展，即使oracle也只能召回候选集合内gold。T4合并所有关系扩大集合后description-only82.2%，低于单cousins90.3%；candidate覆盖/干扰项/费用不能从不同集合accuracy只读一种收益。T5 Oracle最高67.3F1不是validator低于100%，而是前段coverage缺失；Sonnet3.5v1原55.6→verification55.5，正文“allmodels reliablyimprove”不成立，fine-tunedHaiku只56.9→57.6不能借原baseline大幅度归因验证。

作者窄P提案：新增数据/clinical任务本身不作贡献；只保原研究实际暴露**gold-expanded conditional selection与predicted-expanded end-to-end恢复的不同资格，以及扩展更广也会损selection**，应改变对“verificationaccuracy=管线可靠性/更多candidate普遍更好”的采用判断。成熟tree/LLMcombo不独享分数，也不将局部text-labelmetric升为真实临床正确性。207notes/67finetune/Outpatient限定及模型/描述prompt/CoT不普胜、全部费用保留；无需再读全部图/附录。

## 07869：只保留视觉人口、动作接口与训练辅助消费者条件

实际[精确v1](https://arxiv.org/html/2510.07869v1)III-C Eq1–8、IV-A/B TablesII–III及V。主体GR00T N1.5继承原actionloss；视觉/语言→VLM，pressure/IMU/DVL和动作→diffusiontransformer经cross-attention消费VLM，不把“多源融合”名称单独当新算子。thruster PWM与jointangles结合动作，target world→robot relativepose只用作traininggroundtruth；这是可检查action/target身份，不授坐标转换即泛化因果。

CAP从双目VLM token 经Conv/MASK、channelattention、pool/MLP预测target，MSEtargetloss与原actionloss联合。**CAP只作训练辅助，推理可disable**，而非把在线新感知模块与0额外latency拼成一个recipe；groundtruth制备/5000steps/batch1024预付仍在。IV-A20tasks×5trajectory/35Kframes的GR00Tbase、USIMFT、U0均分别做mono/bino，未适配base平均actionerror mono0.2435/bino0.2451、USIMFT0.0791/0.0619、U0.0730/0.0593：新增bino不自动惠及原预训练人口，域适配改变收益资格；CAP相对FT mono/bino收益不同，多个任务action或targeterror也反退，不能采“bino consistentlybetter”。IV-B非grasp七任务×10次/每模型、grasp五×5为simulation，80%成功与robot-targetdistance减少21.2%是不同consumer/指标，不能合成真实抓取或流体安全。

作者窄P提案：不以水下新dataset/成熟ConvAttention/robot-frame变换单独准入；保留**未适配vs域适配对单双目输入的相反资格、CAP监督分支可训练后退出部署但不消全部成本**这一具体设计/对照条件。matchedFT与相同mono/bino的必要反侧已读，真实fieldvalidation原V明确futurework，绝不当已验证。没有读全部simulation生成附件/源码或复现，也无Books提案/锁。

以上两个准入提案prepared即交root，不等其它7N/Source全；当前root路由54/132、78待验（Sep27单项新family暂恢复），本lane已通过dInfer/77/首12不受影响，禁止从数字变化重研。
