# OctoBench / VIST2：必要原源及具体owner待root核

## 10343 OctoBench — 2+2+2=6，评价gap必要深入；拟Existing

actual v1 §3.1–3.3 L187–325、§4.1/主Table2–3、§4.3.4/limits546–564、A/B854–873、D1056–1062。34repo环境/ClaudeCode2.0.69/Kilo.10.2/Droid.42.2；72人工seed→217expand，另32singleconflict。GPT5.1 16reference轨迹→checklist union/dedup/human–LMreview，20%spot与stratified双人audit>95%，audit量/分层数未披露，不能把rubric全当oracle。Trajectory proxy log/normalize/truncate，仅当前轨迹evidenced和已触发conditional判适用；skill类别特例always要求expectedskill。ISR=全activechecks合取，CSR=每instance check均值再平均，非全check加权分母。Task outcome另轴，不能从CSR85%推全部合同兑现；未触发项目不计分可能被strategicavoid，作者limits已承认。

8models×3scaffold/每instance三运行；T1其他provider/scaffolddefault，timeout通常30min，longoutput截断/hiddenreasonavailable与否影响证据。三judge均值/std是judge变化不是独立运行CI；stable rank不证明groundtruth/objectivity/无偏，turn长与难度混杂不授contextfatiguecausal。Conflict只观察sourceschosen，无预设priorityoracle，不能当违反真实授权。rawtrace未默认release，precision/GPU/e2ecost/prompttokenbudget ND；16reference+checklist+三judge费用不能抹掉。

actual `PLATFORM-EVALUATION-SYSTEM` Ch66 L2619–2628已具体拥有冻结必要taskrubric、actual environment evidence+active集合/conditionalprocess分母与未知处理、不能见失败后删要求、process/outcome/sideeffect分别验；L2630–2644 criterionverdict/evidence/missingstate vsglobalrank，L2478 ranking≠construct。该长期机制可采用范围已实质承载；本次repo/scaffold/localrates仅报告不冒现有实验。拟6深入完成Existing请root终裁，不为增diff重复正文。

## 10378 VIST2 — 2+2+2=6，decode压缩表示consumer gap深入

actual v1 §2–3 L87–143、§4.1 L145–149/§4.3 L335–344、Table3PPL308–332/Table6数学705–717、§4.4/未来729–744、Table8 976–1020、B1039–1051及D1054–1056。旧text-as-image只prefill仍让生成历史textKV增长；本接口按chunk生成currenttext后render/VE→visualmemory，后续text只读取previousvisual和当前chunk，不读pasttext。position按previousvisualcount+currentlocaloffset；sparse mask/training必须与consumer同版，不认定lossless/cachebitwise。视觉producer与decode KV实际layout/eviction不同责任，原文未核可执行cache迁移源码。

captionwarmaligner→OCRcurriculum视觉encoder/aligner→OLM新mask适配LLM→interleavedSFT，OCRwarmup可读旧text而OLM仅visualhistory，不能称全部stage无oldtextaccess。SigLIP2+Qwen3 .6/4/8B/8H200，Table8 AdamW/WD1e-4/warm.01/cosine/1epoch/PTLR5e-4SFT1e-5/8BSFT B8accum/max8192。10MSFT合成长CoT+答案一起压，density/char/readback仍有loss；precision/seed/E2E含render/VEwallclock/servingbatchconcurrency未披露。

主headline3xTTFT/77%memory/74%FLOPs不能当吞吐：§4.4明确与Glyph吞吐相当且prefillcompression较低，figure硬件/输入/输出预算细节不足不造统一数字。Table3 8BArxiv/Gutenberg2.22/1.90劣Qwen2.15/1.88，Wikipedia1.62优1.65；Table6 GSM/MATH/AQUA受测有退，不能“全部不损”。写作评估所谓GPT4PPL计算未给API/logprob实现，单PPL不验证groundedwriting。trainingloss消融不等完整samebudget任务因果，staticchunk/density适配未验不授普遍codec。

actual `MULTIMODAL-REPRESENTATION` Ch23 L386–390具体已有光学有损transport/rendererencoder/原文readbackauthority，但只讲input，不承载generatedcompletedchunk→visualmemory与latertextconsumer只读visualhistory的长期接口。拟此分支后两段，currenttext可读/pastvisual责任、codec/mask/position/cacheversion与成本反侧相邻；Ch45不复制表示机制，仅已有KV分责。需root必要原源/owner核后授Ch23窄锁，未核implementation不授真实cachefree/吞吐保证。

两个normalSubmitted+正常公告条件的register秒精度上界完全落窗；具体日期原字段见jan17_all_date_fields.json，报告逐项ISO范围，无Submitted=public。
