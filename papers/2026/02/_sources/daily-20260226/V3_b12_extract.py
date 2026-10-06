import pathlib
ROOT=pathlib.Path(__file__).resolve().parent
PROJECT=ROOT.parents[4]
keys={
 '20751':['S2.SS2.SSS2.p1.2','S2.SS2.SSS3.p2.1','S2.SS3.p1.1','S3.SS1.p4.1','S3.SS2.p6.1'],
 '20759':['S4.SS2.p3.1','S4.SS3.p5.1','S5.SS2.SSS0.Px5.p3.1'],
 '20770':['S3.SS3.p1.1','S4.SS1.p4.1','S4.SS1.p5.1','S5.SS1.p4.1'],
 '20791':['S3.Thmtheorem1.p1.1','S4.p3.1','S5.p3.1'],
 '20794':['S3.SS2.p1.1','S3.SS2.p2.3','S4.SS4.p3.1'],
 '20796':['S3.p2.1','S4.p8.4','S5.SS1.p2.1','S5.SS3.p3.1'],
}
out=['# B12 — 六项最小必要原证与actual owner（未授终态）','']
for short,ids in keys.items():
 lines=(ROOT/('V3_PARA_2602.'+short+'.txt')).read_text().splitlines()
 out+=['## 2602.'+short+'v1','https://arxiv.org/html/2602.'+short+'v1；原HTML paragraph身份保留：','']
 for line in lines:
  if line.partition(' | ')[0] in ids:out += [line,'']
for short,ranges in [('20751',[(1488,1520)]),('20794',[(2284,2345)])]:
 lines=(ROOT/('V3_CORE_2602.'+short+'.txt')).read_text().splitlines()
 for lo,hi in ranges:out+=['### 原txt '+short+' L%d–%d'%(lo,hi),'\n'.join(lines[lo-1:hi]),'']
for path,ranges in [
 ('books/part-04-training-system/31-rlhf.md',[(540,545),(214,218)]),
 ('books/part-06-ai-infrastructure/66-evaluation-system.md',[(3557,3557),(1791,1795)]),
 ('books/part-04-training-system/28-pretraining.md',[(1478,1489)]),
 ('books/part-03-multimodal-world-models/23-multimodal-representation.md',[(105,107)]),
 ('books/part-04-training-system/29-sft.md',[(854,858)]),
]:
 lines=(PROJECT/path).read_text().splitlines()
 out+=['## Actual owner '+path,'']
 for lo,hi in ranges:out+=['### 原文件L%d–%d'%(lo,hi),'\n'.join(lines[lo-1:hi]),'']
(ROOT/'V3_B12_CORE_OWNER_PACKET.md').write_text('\n'.join(out)+'\n')
print('words',len(' '.join(out).split()))
for short,ids in keys.items():
 lines=(ROOT/('V3_PARA_2602.'+short+'.txt')).read_text().splitlines()
 found={line.partition(' | ')[0] for line in lines}
 print(short,'missing',set(ids)-found)
