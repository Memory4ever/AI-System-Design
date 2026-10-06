import pathlib,re,html
ROOT=pathlib.Path(__file__).resolve().parent
PROJECT=ROOT.parents[4]
patterns={
 '20696':['Synchronized Dual-Sequence','Crucially, this single selected token','amateur correction','performance follows an inverted','necessitates dual forward','Under the negative prompt'],
 '20708':['We first compute the generation-normalized','To construct a comprehensive representation','In this formulation','We utilize two widely used datasets','Values are reported with standard deviations','Compared to filtering'],
 '20715':['high variance during non-interaction','objective upweights data','For each task, we collect 60','same 40 human interventions','Shaded regions indicate','does not yet exist'],
}
packet=['# B9 — 必要原证＋实际owner（3项，非整日验收）','']
for short,keys in patterns.items():
 raw=(ROOT/('V3_CORE_2602.'+short+'.raw')).read_text()
 packet+=['## 2602.'+short+'v1','https://arxiv.org/html/2602.'+short+'v1；精确HTML原paragraph机械摘段：','']
 for q in re.findall(r'<p\b[^>]*>(.*?)</p>',raw,re.S):
  q=re.sub(r'<math\b[^>]*alttext="([^"]*)".*?</math>',lambda m:' '+html.unescape(m.group(1))+' ',q,flags=re.S)
  s=html.unescape(re.sub('<[^>]*>','',q)).strip()
  if len(s)<6500 and any(re.search(k,s,re.I) for k in keys):packet += [s,'']
for short,ranges in [('20696',[(1193,1283)]),('20708',[(1310,1450),(1765,1818)]),('20715',[(555,590),(676,762),(1612,1684)])]:
 lines=(ROOT/('V3_CORE_2602.'+short+'.txt')).read_text().splitlines()
 for lo,hi in ranges:packet+=['### '+short+' 原正文txt L%d–%d'%(lo,hi),'\n'.join(lines[lo-1:hi]),'']
for path,ranges in [
 ('books/part-02-model/20-sampling.md',[(145,168)]),
 ('books/part-06-ai-infrastructure/72-security.md',[(2257,2270)]),
 ('books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md',[(657,678)]),
]:
 lines=(PROJECT/path).read_text().splitlines()
 packet+=['## Actual owner '+path,'']
 for lo,hi in ranges:packet+=['### 原文件L%d–%d'%(lo,hi),'\n'.join(lines[lo-1:hi]),'']
(ROOT/'V3_B9_CORE_OWNER_PACKET.md').write_text('\n'.join(packet))
print('words:',len(' '.join(packet).split()))
