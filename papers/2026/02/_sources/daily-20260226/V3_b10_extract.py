import pathlib,re,html
ROOT=pathlib.Path(__file__).resolve().parent
PROJECT=ROOT.parents[4]
patterns={
 '20720':['Assuming a grey-box adversary','ASR degradation does not exceed','Due to the high costs of API','We set the default number of iterations','3,691 benign agent trajectories'],
 '20722':['First-In-First-Out','three most recent steps','stored for calculating','All comparative experiments were run','assembled training batch size frequently','31% of the samples'],
 '20727':['rows of.*treated as individual','equal divisions from vector','0.5% compared to LoRA','except on MATH','parameter-free'],
}
packet=['# B10 — 必要原证＋actual owner（3项，非整日验收）','']
for short,keys in patterns.items():
 raw=(ROOT/('V3_CORE_2602.'+short+'.raw')).read_text()
 packet+=['## 2602.'+short+'v1','https://arxiv.org/html/2602.'+short+'v1；原HTML paragraph机械摘段：','']
 for q in re.findall(r'<p\b[^>]*>(.*?)</p>',raw,re.S):
  q=re.sub(r'<math\b[^>]*alttext="([^"]*)".*?</math>',lambda m:' '+html.unescape(m.group(1))+' ',q,flags=re.S)
  s=html.unescape(re.sub('<[^>]*>','',q)).strip()
  if len(s)<6500 and any(re.search(k,s,re.I) for k in keys):packet += [s,'']
for short,ranges in [('20720',[(1556,1603)]),('20722',[(2320,2407)]),('20727',[(561,716),(718,824),(1714,1764)])]:
 lines=(ROOT/('V3_CORE_2602.'+short+'.txt')).read_text().splitlines()
 for lo,hi in ranges:packet+=['### '+short+' 原正文txt L%d–%d'%(lo,hi),'\n'.join(lines[lo-1:hi]),'']
for path,ranges in [
 ('books/part-06-ai-infrastructure/72-security.md',[(684,695),(2855,2862)]),
 ('books/part-04-training-system/31-rlhf.md',[(680,688)]),
 ('books/part-04-training-system/30-lora.md',[(191,195),(203,207),(213,231)]),
]:
 lines=(PROJECT/path).read_text().splitlines()
 packet+=['## Actual owner '+path,'']
 for lo,hi in ranges:packet+=['### 原文件L%d–%d'%(lo,hi),'\n'.join(lines[lo-1:hi]),'']
(ROOT/'V3_B10_CORE_OWNER_PACKET.md').write_text('\n'.join(packet))
print('words:',len(' '.join(packet).split()))
