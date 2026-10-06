import pathlib,re,html
ROOT=pathlib.Path(__file__).resolve().parent
PROJECT=ROOT.parents[4]
patterns={
 '20558':['A critical design choice','Attribution of Improvement','Removing the length reward','industrial-scale dataset','two-stage pipeline introduces additional training cost'],
 '20580':['1750 detections','For each instance of PI','Phone numbers have a much lower','prefix length','Annotating personal information is time-consuming'],
}
packet=[]
for short,keys in patterns.items():
 raw=(ROOT/('V3_CORE_2602.'+short+'.raw')).read_text()
 packet+=['## 2602.'+short+'v1','','https://arxiv.org/html/2602.'+short+'v1；精确HTML原paragraph机械摘段：','']
 for q in re.findall(r'<p\b[^>]*>(.*?)</p>',raw,re.S):
  q=re.sub(r'<math\b[^>]*alttext="([^"]*)".*?</math>',lambda m:' '+html.unescape(m.group(1))+' ',q,flags=re.S)
  s=html.unescape(re.sub('<[^>]*>','',q)).strip()
  if len(s)<6000 and any(re.search(k,s,re.I) for k in keys):packet += [s,'']
for path,ranges in [
 ('books/part-07-agent/75-context.md',[(194,201),(247,253),(263,275)]),
 ('books/part-06-ai-infrastructure/72-security.md',[(47,49),(279,285),(295,295)]),
]:
 lines=(PROJECT/path).read_text().splitlines()
 packet+=['## Actual owner '+path,'']
 for lo,hi in ranges:
  packet+=['### 原文件L%d–%d'%(lo,hi),'\n'.join(lines[lo-1:hi]),'']
(ROOT/'V3_B7_CORE_OWNER_PACKET.md').write_text('\n'.join(packet))
print('words:',len(' '.join(packet).split()))
