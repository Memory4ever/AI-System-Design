import pathlib
ROOT=pathlib.Path(__file__).resolve().parent
PROJECT=ROOT.parents[4]
keys={
 '20799':['S2.SS2.SSS1.p1.1','S2.SS2.SSS1.p2.1','S2.SS3.SSS1.p5.1','S4.SS4.p3.1'],
 '20800':['S3.SS1.p10.1','S4.SS1.p4.1','S4.SS2.p4.1','S5.p1.1'],
 '20813':['S4.SS0.SSS0.Px1.p3.1','S5.SS0.SSS0.Px2.p2.1','S5.SS0.SSS0.Px3.p2.1','S7.SS0.SSS0.Px3.p1.1'],
 '20816':['S2.p3.1','S2.p5.1','S3.SS2.SSS2.p3.1','S3.SS2.SSS4.p1.1','A2.p2.1'],
 '20878':['S3.p5.1','S5.p5.1','S5.T2.3.1'],
 '20880':['S3.SS3.p3.1','S4.SS1.p5.1','S4.SS1.p5.2','S4.SS1.p6.1','S5.SS1.SSS0.Px1.p3.1','A4.I1.i2.p1.1'],
}
out=['# B13 — 六项最小必要原证与actual owner（未授终态）','']
for short,ids in keys.items():
 lines=(ROOT/('V3_PARA_2602.'+short+'.txt')).read_text().splitlines()
 found={line.partition(' | ')[0] for line in lines}
 assert not set(ids)-found,(short,set(ids)-found)
 out+=['## 2602.'+short+'v1','https://arxiv.org/html/2602.'+short+'v1；原HTML paragraph身份保留：','']
 for line in lines:
  if line.partition(' | ')[0] in ids:out += [line,'']
lines=(ROOT/'V3_PDF_2602.20799v1.txt').read_text().splitlines()
out+=['### 20799 exact-v1 PDF p14 Table4, extraction L743–750','\n'.join(lines[742:750]),'']
lines=(ROOT/'V3_CORE_2602.20816.txt').read_text().splitlines()
for lo,hi in [(656,704),(1973,2102)]:
 out+=['### 20816 原txt L%d–%d'%(lo,hi),'\n'.join(lines[lo-1:hi]),'']
for path,ranges in [
 ('books/part-04-training-system/27-data.md',[(327,330),(788,790)]),
 ('books/part-06-ai-infrastructure/66-evaluation-system.md',[(128,130),(293,299),(998,1000),(3671,3673)]),
 ('books/part-04-training-system/29-sft.md',[(246,250)]),
 ('books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md',[(232,236)]),
]:
 lines=(PROJECT/path).read_text().splitlines()
 out+=['## Actual owner '+path,'']
 for lo,hi in ranges:out+=['### 原文件L%d–%d'%(lo,hi),'\n'.join(lines[lo-1:hi]),'']
(ROOT/'V3_B13_CORE_OWNER_PACKET.md').write_text('\n'.join(out)+'\n')
print('words',len(' '.join(out).split()))
