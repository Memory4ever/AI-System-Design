import pathlib,re,html

ROOT=pathlib.Path(__file__).resolve().parent
patterns={
 '20450':['Terraform.*hierarchical selection takes inspiration','This running sum is used','Our results illustrate that IQR','One exception.*scenario','we illustrate the accuracy of Terraform'],
 '20981':['we opt to mask tokens','Selected important tokens.*high similarity','We observe that the model with a temporal routing','We ablate on having the structure of models with tokens','minimal impact on overall performance'],
 '21092':['experimental setup','The Graph Transformer model has therefore learned','In barbell experiments','important distinction.*computational','For each graph, we consider two different variations'],
 '21078':['simply averaging the local proxies','dynamically maintain a global category prior','does not overlap','directly including them sometimes leads','set-based supervision is not as precise'],
}
packet=[]
for short,keys in patterns.items():
 raw=(ROOT/('V3_CORE_2602.'+short+'.raw')).read_text()
 packet+=['## 2602.'+short+'v1','','原文精确HTML：https://arxiv.org/html/2602.'+short+'v1；机械抽取的原始paragraph（不以作者摘要代原文）。','']
 for q in re.findall(r'<p\b[^>]*>(.*?)</p>',raw,re.S):
  q=re.sub(r'<math\b[^>]*alttext="([^"]*)".*?</math>',lambda m:' '+html.unescape(m.group(1))+' ',q,flags=re.S)
  s=html.unescape(re.sub('<[^>]*>','',q)).strip()
  if len(s)<6500 and any(re.search(k,s,re.I) for k in keys):packet += [s,'']
(ROOT/'V3_CROSS_ONCE_CORE_PACKET.md').write_text('\n'.join(packet))
print('words:',len(' '.join(packet).split()))
