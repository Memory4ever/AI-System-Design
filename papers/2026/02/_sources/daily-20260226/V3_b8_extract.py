import pathlib,re,html
ROOT=pathlib.Path(__file__).resolve().parent
PROJECT=ROOT.parents[4]
patterns={
 '20659':['previous belief state.*pre-pended','static throughout task execution','We ablate key components','25 real-world trials','all inference measurements performed'],
 '20662':['memory content as a simple combinational logic function','sharing resources with the KV Cache','We measure the overall system performance','primary cost of supporting longer contexts','synthesized.*gates|non-monotonic behavior'],
 '20666':['This split process provides','SMART iteratively performs bottom-up merging','slightly inferior results','diversity naturally decreasing','For sampling, we use the DDIM'],
}
packet=[]
for short,keys in patterns.items():
 raw=(ROOT/('V3_CORE_2602.'+short+'.raw')).read_text()
 packet+=['## 2602.'+short+'v1','','https://arxiv.org/html/2602.'+short+'v1；精确HTML原paragraph机械摘段（非摘要）：','']
 for q in re.findall(r'<p\b[^>]*>(.*?)</p>',raw,re.S):
  q=re.sub(r'<math\b[^>]*alttext="([^"]*)".*?</math>',lambda m:' '+html.unescape(m.group(1))+' ',q,flags=re.S)
  s=html.unescape(re.sub('<[^>]*>','',q)).strip()
  if len(s)<5500 and any(re.search(k,s,re.I) for k in keys):packet += [s,'']
for path,ranges in [
 ('books/part-03-multimodal-world-models/25-multimodal-world-models.md',[(402,417),(421,438),(245,264)]),
 ('books/part-05-inference-system/49-tensorrt-llm.md',[(55,69)]),
 ('books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md',[(33,59)]),
]:
 lines=(PROJECT/path).read_text().splitlines()
 packet+=['## Actual owner '+path,'']
 for lo,hi in ranges:packet+=['### 原文件L%d–%d'%(lo,hi),'\n'.join(lines[lo-1:hi]),'']
(ROOT/'V3_B8_CORE_OWNER_PACKET.md').write_text('\n'.join(packet))
print('words:',len(' '.join(packet).split()))
