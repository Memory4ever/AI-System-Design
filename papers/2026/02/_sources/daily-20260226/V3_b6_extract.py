import pathlib,re,html

ROOT=pathlib.Path(__file__).resolve().parent
patterns={
 '20555':['Here.*unknown target function','Then with probability','several promising directions'],
 '20566':['direct end-to-end ranking','Since dropping tokens','online pruning shows','apply spatial adaptive weighting'],
 '20574':['GATES relies on agreement','canonical GATES setup','GATES and Tutor-Trajectory SFT achieve near-identical','single model instance','require at least'],
 '20577':['We observe that.*strikes the optimal','classification problems','restrict the unmasking candidate set','random embeddings'],
}
packet=[]
for short,keys in patterns.items():
 raw=(ROOT/('V3_CORE_2602.'+short+'.raw')).read_text()
 packet+=['## 2602.'+short+'v1','', '原文精确HTML：https://arxiv.org/html/2602.'+short+'v1；下方为该精确原源实际paragraph机械抽取，非作者摘要。','']
 for q in re.findall(r'<p\b[^>]*>(.*?)</p>',raw,re.S):
  q=re.sub(r'<math\b[^>]*alttext="([^"]*)".*?</math>',lambda m:' '+html.unescape(m.group(1))+' ',q,flags=re.S)
  s=html.unescape(re.sub('<[^>]*>','',q)).strip()
  if len(s)<5000 and any(re.search(k,s,re.I) for k in keys):packet += [s,'']
(ROOT/'V3_B6_CORE_PACKET.md').write_text('\n'.join(packet))
print('Exact core packet paragraphs:',len(packet))
