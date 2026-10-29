import fs from 'node:fs';
const root = 'papers/2026/04';
const day = `${root}/08/README.md`;
const own = `${root}/_sources/daily-20260408`;
const sup = fs.readFileSync(`${own}/SUP_REVIEW_20261014.md`, 'utf8');
const legacy = fs.readFileSync(`${root}/_sources/daily-20260407/v3-reopen-notes.md`, 'utf8');
const oldReport = fs.readFileSync(`${root}/07/README.md`, 'utf8');
const current = fs.readFileSync(day, 'utf8');
const roadmap = fs.readFileSync('ROADMAP.md', 'utf8');
const nodes = new Map([...roadmap.matchAll(/\| `([^`]+)` \| Ch(\d+) \| `([^`]+)`/g)].map(m => [+m[2], [m[1], m[3]]]));
const records = [];
function add(id, score, ch, disposition, contribution, noteLine = null, deep = true) {
  let title, url;
  const oldRow = oldReport.split('\n').find(l => l.startsWith('| [') && l.includes(`2604.${id}v1`));
  if (oldRow) [title,url] = oldRow.match(/^\| \[([^\]]+)\]\(([^)]+)\)/).slice(1);
  else {
    const raw = fs.readFileSync(`${own}/SUP_${id}_20261014.raw`, 'utf8');
    const m = raw.match(/<meta name="citation_title" content="([^"]+)"/);
    if (!m) throw Error(`title ${id}`);
    title = m[1].replaceAll('&amp;', '&').replaceAll('&quot;', '"').replaceAll('&#39;', "'");
    url = `https://arxiv.org/html/2604.${id}v1`;
  }
  const node = nodes.get(ch);
  if (!node) throw Error(`node ${ch}`);
  const body = sup.split('\n').find(l => l.endsWith(`<!-- source-family:SF-2026-ARXIV-2604-${id} -->`));
  let evidence;
  if (noteLine) evidence = noteLine === 'GEN' ? legacy.split('\n').slice(54,61).join('\n\n') : legacy.split('\n')[noteLine-1];
  else {
    const block = sup.split(/\n(?=### )/).find(b => new RegExp(`^### ${id}\\b`).test(b));
    if (!block) throw Error(`Source ${id}`);
    evidence = block.slice(block.indexOf('\n')+1).trim();
  }
  evidence = evidence.split(/拟(?:\*\*|2\+|Ch|owner|采用|整合|5分|争议|\s*\*\*2)/)[0].trim();
  // Preserve the primary-support portion, never carry the old day's adoption/date conclusion.
  evidence = evidence.split(/。(?:日期|自身|尚待|Books 对读)/)[0];
  const review = disposition === '暂缓' ? '争议' : deep ? '深入完成' : '标准完成';
  records.push({id, score, ch, disposition, contribution, title, url, node, body, evidence, review, noteLine});
}
add('03240','2+1+2=5',76,'整合','固定初检→子集专用Gram adapter/set margin→集合packing选择');
add('03279','1+2+2=5',66,'已有覆盖','局部PCC近1仍音质下降→precision与outcome双面验收',null,false);
add('03298','2+2+2=6',54,'整合','受限NPU block可逆exponent表示与依赖解耦→resident/解码取舍');
add('03307','2+1+2=5',23,'暂缓','训练grounding蒸馏与推理slot producer存在中心冲突→不授serving接口');
add('03314','2+1+2=5',30,'整合','paired modality生成低秩middle map→静态与动态adapter分账');
add('03436','2+1+2=5',5,'整合','decoder可分解性critic正则→geometry proxy与真概念分账');
add('03388','2+2+2=6',66,'整合','一次backbone＋Bayesian last-head MC→posterior scope/成本取舍');
add('03540','2+2+2=6',26,'整合','单步动作generator＋stored latent conditional PPO→joint与执行prefix credit');
add('04384','2+1+2=5',14,'整合','weight与输入logits谱不同→低effective rank不授压缩保证');
add('04440','2+1+2=5',28,'整合','训练DCT坐标每forward重构dense→参数节省与物化费用分账');
add('04493','2+1+2=5',49,'整合','显式sign×rank-one magnitude＋稀疏残差→非低秩执行/metadata费用');
add('04491','2+1+2=5',24,'整合','保FM＋self-lookahead velocity正则→非endpoint flowmap或一步保证');
add('04734','2+1+2=5',76,'整合','teacher score-spectrum采样→hard-only窄标签人口反侧');
add('04646','2+2+2=6',24,'整合','同t按divergence代理选附近state→不同temporal solver且改distribution');
add('04579','2+1+2=5',23,'整合','token-grid context经FiLM调SSM→有限connector消费而非全decoder保证');
add('04746','2+1+2=5',24,'整合','partial instruction/global请求与draft/local指令双判→未完成不等错误');
add('04757','2+2+2=6',72,'整合','受限keyless honest-transcript反例→passive审计排除边界');
add('04834','2+2+2=6',23,'整合','recent-N event窗口截至RGB exposure→variable freshness与fusion费用');
add('04902','2+2+2=6',14,'已有覆盖','early agreement与可解码trace不等正确/必要真实过程');
add('04917','2+2+2=6',27,'已有覆盖','typed reward＋mixture局部negative-transfer→条件人口/质量分账',null,false);
// Latest valid necessary evidence locations; these are route pointers, not old completion labels.
add('04202','2+2+2=6',66,'已有覆盖','动态GT/belief revision与workspace outcome分评',294,false);
add('04230','2+1+2=5',21,'仅报告','MFG proxy/phase非普遍→只保受限routing诊断',295,false);
add('04247','2+2+2=6',77,'已有覆盖','LLM reduce非结合律→bounded fan-in/context version',299,false);
add('04253','2+2+2=6',49,'已有覆盖','shape/buffer/placement联合→模拟与真实硬件分责',376,false);
add('04261','3+2+2=7',31,'整合','frozen本地偏好reward vectors→中央PPO而非fedavg',300);
add('04323','2+2+2=6',66,'已有覆盖','Skill loaded/selected/retrieved/adapted分层真实controlpath',301,false);
add('04335','2+2+2=6',56,'整合','两deadline＋step VideoState恢复共置→总命中与video尾分账','GEN');
add('04399','2+2+2=6',66,'整合','recoverable subtask聚合→非step hardAND/终局叙述',302);
add('04410','2+1+2=5',34,'整合','混合density bounded ratio→非参数梯度/偏好真值保证',333);
add('04426','2+2+2=6',72,'整合','MITM/PCAP network-effect sensor→host盲区/已泄露不可撤',303);
add('04451','2+2+2=6',24,'整合','跨request分时段/区域features reuse→近prompt非KV等价',377);
add('04522','2+2+2=6',72,'已有覆盖','issuer单key provenance≠named-agent亲签/即时离线撤销',344);
add('04532','2+1+2=5',66,'已有覆盖','judge语言改变需求判定→solver与evaluator身份分开',335,false);
add('04561','2+2+2=6',72,'已有覆盖','goal reframing局部反证→叙述不授dispatch/effect权限',336);
add('04745','2+2+3=7',70,'整合','execution-idle与deep idle分母→驻留节能/尾成本',337);
add('04750','2+2+2=6',49,'已有覆盖','硬件/parallel plan联合DSE→模型误差与thermal限制',338,false);
add('04759','2+2+2=6',72,'已有覆盖','self-state/harness持久毒化→load/activation再admission',339);
add('04783','2+2+2=6',72,'已有覆盖','TFHE PBS精度/batch/转换→隐私执行边界非LLM实测',343);
add('04847','2+2+2=6',66,'已有覆盖','duplex tool/content四时刻→首响应不代真实完成',373,false);
add('04855','2+2+2=6',33,'整合','chosen-prefix control与logit observation分轴',416);
add('04872','2+2+2=6',81,'已有覆盖','synthetic spec/evaluator先可执行→cheap训练非测试SLO',375,false);
add('04894','2+1+2=5',33,'整合','binary group成功率两符号advantage modulation',353);
add('04913','2+2+3=7',25,'整合','delta history与spatial anchor不同consumer→BoM非概率校准',351);
add('04921','2+2+2=6',45,'已有覆盖','preRoPE统计/模型校准身份/cadence→递归反退',352,false);
add('04347','2+1+2=5',81,'仅报告','有限evaluation预算recipe比较→非通用autoresearch支配',371,false);
add('04373','2+2+2=6',77,'已有覆盖','derived lesson/late construction→相关性非当前utility',400,false);
add('04207','2+1+2=5',66,'已有覆盖','任务条件视觉sensor/entropy迁移反退→无truth权',414);
add('04356','2+2+2=6',21,'整合','permutation合并artifact＋逐层校准→非runtime裁route',407);
add('04461','2+2+2=6',72,'已有覆盖','student-release DP不保护teacher/API所见prompt',408);
add('04580','2+2+2=6',81,'已有覆盖','code/test共同fitness→独立contract/hidden oracle',415);
add('04648','2+2+2=6',31,'已有覆盖','frozen RM-feature OOD penalty→受限pool soft-risk选择',392,false);
add('04767','2+1+2=5',33,'整合','MC/cloze/open课程改变可达reward→原任务迁移另验',393);
add('04385','2+1+3=6',14,'已有覆盖','低DLA gate可必要→多位置因果控制不由读出贡献认证',403);
add('04418','2+2+3=7',66,'整合','AO verdict×真实correctness四cell→verifiability非accuracy',360);
add('04701','2+1+2=5',49,'整合','integer body/aux重组替FP旁路→fakequant非NPUkernel',506);
add('04722','2+1+2=5',45,'暂缓','自适应KV controller时间单位/packed测量中心冲突',507);
add('04281','2+1+2=5',28,'整合','width selector horizon/regime可翻转→function保留非轨迹',513);
add('04743','2+1+2=5',66,'已有覆盖','conditioned failure probe/steering proxy→独立outcome',514);
add('04863','2+1+2=5',66,'整合','ADS空间compactness与CGC语义alignment双轴',527);
add('04238','2+1+2=5',81,'已有覆盖','compiler finite oracle/零cost calls→contract与budget shape',534,false);
add('04523','2+1+2=5',49,'整合','LUT容量/索引/host转换/分层reuse联合费用',535);
if (records.length !== 61 || new Set(records.map(r=>r.id)).size !== 61) throw Error('61 distinct');
const book = r => `[Ch${r.ch}](../../../../${r.node[1].replace(/^books\//,'Books/')})`;
const adopted = new Set(['04261','04335','04745']);
const nc = {
  '03279':'Ch66“数值mismatch的判定必须连接baseline、机制与结果owner”以reference/tolerance/operator/shape/precision/downstream outcome双面验收；不把PCC近1当感知质量。',
  '04902':'Ch14“可解码不等于单点拥有因果控制权”已分probe、单/多位置transplant、必要/充分与原生读出；Ch66 failure direction持有独立intervention/control survival。',
  '04917':'Ch27数据mixture人口/组合非可加及recipe匹配，Ch33 reward channel/format/content/heldout分账已承载typed reward与受限transfer边界。',
  '04202':'Ch66动态phase、关系回归、Outcome Witness及belief/action/outcome分别持有时变truth、真实workspace与分层分母。',
  '04323':'Ch66 Skill真实controlpath分别验loaded→selection→retrieval→adaptation及no-Skill反侧。',
  '04532':'Ch66 pairwise envelope与agreement测量身份保artifact/solver、judge/template/language/scale/pooling不同对象。',
  '04847':'Ch66 duplex合同分别持有响应时钟、内容、turn/interrupt与工具真实outcome；mock API不签生产SLO。',
  '04743':'Ch66 failure direction分label读出、独立correction/outcome与control survival；steered probe不是真实错误率。',
  '04522':'Ch72 delegation完整论点持有issuer授权hop与principal签名区别、scope/expiry/replay/effect责任。',
  '04561':'Ch72 goal alignment/组合授权持有目标叙述不授dispatch/effect权限；局部单模型反证不成为普遍taxon。',
  '04759':'Ch72 self-state与harness backdoor持有跨run load/trigger admission与write lineage，不乘成人为stage自然发生率。',
  '04461':'Ch72 DP被保护/发布对象与private prediction分账、明文可见边界已承载student发布不保护teacher/API prompt。',
  '04783':'Ch72隐私执行协议/非线性转换持有PBS精度/batch/转换合同；单block投影不等LLM/SLO。',
  '04247':'Ch77“并行经验汇总需要Bounded Fan-in与Context Version”两段持有worker局部证据/curator提交、parent version/冲突及同源错误。',
  '04373':'Ch77“从原始轨迹到派生策略”及“Query-conditioned Late Construction”持有lesson来源/适用条件与当前utility再验，不把历史成功或检索相关性当执行权。',
  '04253':'Ch49 Chiplet Pool与Execution Plan联合演化、Typed System IR、跨算子buffer/ordering与cost-model分责持有形状/存储/放置联合设计，非silicon实证。',
  '04750':'Ch49 Chiplet Pool与Execution Plan联合演化和Typed System IR持有硬件/并行计划共同搜索、模型误差/热设计/实际runtime回退。',
  '04207':'Ch66 attention sensor、length deconfounding与模型/任务slice校准持有受限风险信号无truth权；不称本篇entropy训练recipe已在书中逐机制实现。',
  '04872':'Ch81 Synthetic Environment两段先验结构、语义、可行性和真实canary，持有合成环境可执行契约及generator/verifier共同偏差。',
  '04921':'Ch45 Pre-RoPE Calibration与Workload-semantic Selection完整两路线已有model/calibration revision、update cadence及physical block/FullKV回退。',
  '04580':'Ch81先编译contract/Evaluator-driven search已分candidate/test共同错误、独立holdout/权威与谱系，Ch66 budget surface分width/depth。',
  '04238':'Ch81可执行contract/Evaluator-driven search持有finite oracle/heldout与晋级责任，Ch66“Search排名必须覆盖预算形状”分width/depth/frontier与真实成本。',
  '04385':'Ch14 probe与多位置transplant/causal tracing持有可读、必要/充分与分布式carrier边界，不以DLA小断言无控制。',
  '04648':'Ch31 frozen realized-pool soft-risk selector与Ch66 representation/detector/校准分责持有受限选择风险；不声称frozen RM prediction-error训练recipe已逐机制实现，更不授概率真值。'
};
const rows = records.map(r=>`| [${r.title}](${r.url}) | 2026-04-07 | ${r.contribution}；${r.score} | ${r.review} | ${r.disposition}：${r.node[0]} ${book(r)}${adopted.has(r.id)?'，复用既有真实正文/POST，不计本轮新写':''}${r.disposition==='暂缓'?'；见§5精确重开':''}${r.disposition==='仅报告'?'；局部诊断/预算比较不改变长期机制':''} |`).join('\n');
const sections = records.map(r=>{
  let ev = r.evidence;
  if (!ev || ev.startsWith('##') || ev.startsWith('- **04013') || ev.startsWith('- **03571')) throw Error(`wrong Source route ${r.id}/${r.noteLine}`);
  const refs = r.noteLine ? `[既有精确必要Source](../_sources/daily-20260407/v3-reopen-notes.md)（按ID定位${r.noteLine==='GEN'?'GenServe必要方法/配置/反側':`最新有效段，原记录定位${r.noteLine}`}）` : `[本日必要Source与逐批独核](../_sources/daily-20260408/SUP_REVIEW_20261014.md)`;
  let decision;
  if(r.disposition==='整合') decision = adopted.has(r.id) ? `本日恢复决定为整合：${r.node[0]} ${book(r)}。既有真实正文与有效Source/非作者POST一致，本轮reader实际当前完整局部对读复用；不再写同义段或加fresh计数。` : `本日整合：${r.node[0]} ${book(r)}。当前owner/完整邻接逐字PRE后，已在原论证内实际写入受限差额，非作者实际正文、完整旧邻接与来源注POST通过；原分支与失配回退保留，不授实现/复现或生产保证。\n\n${r.body}`;
  else if(r.disposition==='已有覆盖') decision = `已有覆盖：${r.node[0]} ${book(r)}。${nc[r.id]} 非作者已实际读当前承载正文/完整相关局部，此决定不是主题相似或仅Review note匹配，不新增同义书稿。`;
  else if(r.disposition==='仅报告') decision = `仅报告：${r.id==='04230'?'MFG/phase只作所测checkpoint的routing诊断，cluster baseline更好与dormant phase不授统一训练控制':'1500evaluation预算比较仍有工具/session/API与sampling混杂，KotH/Autoresearch局部反胜，不授统一Agent架构支配'}；证据保留，不新增长期算法或Books机制。`;
  else decision = `争议/暂缓：${r.node[0]} ${book(r)}。中心矛盾双方均保留，不作正面Evidence或Books，具体缺少的原始澄清及定点重开见§5；不是普通未读，也不以降分或删反侧关闭。`;
  return `### [${r.title}](${r.url})\n\n${r.contribution}；评分${r.score}，审阅${r.review}。精确v1身份和公开日由本家族AB/DOI、官方first-announcement赋号规则、相邻批次/OAI及月列表组合支持Apr07自然日；单Submitted/Updated/created不定义首发。${refs}保留必要位置、评价合同与未证明范围。\n\n${ev}\n\n${decision}\n`;
});
const heading3 = current.indexOf('## 3. 候选与判断');
const heading4 = current.indexOf('## 4. 证据与知识整合');
const heading5 = current.indexOf('## 5. 缺口与下一步');
if (heading3 < 0 || heading4<0 || heading5<0 || current.includes('本次自然日补充61项')) throw Error('one-time merge bounds');
const mode=process.argv[2];
const insert=mode==='rows'?rows+'\n\n':sections.slice(+process.argv[2],+process.argv[3]).join('\n')+'\n';
const anchor=mode==='rows'?'## 4. 证据与知识整合':'## 5. 缺口与下一步';
process.stdout.write('*** Begin Patch\n*** Update File: '+day+'\n@@\n'+insert.split('\n').map(l=>'+'+l).join('\n')+'\n '+anchor+'\n*** End Patch\n');
