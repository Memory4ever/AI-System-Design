import pathlib
ROOT=pathlib.Path(__file__).resolve().parent
PROJECT=ROOT.parents[4]
keys={
 '20903':['S3.SS2.SSS1.p1.1','S3.SS2.SSS1.Px2.p1.2','S4.SS2.SSS1.p4.1','A7.SS1.p1.1'],
 '20911':['S3.SS2.SSS0.Px2.p2.1','S3.SS2.SSS0.Px3.p3.1','S4.SS4.SSS0.Px3.p1.1'],
 '20913':['S3.SS2.p2.1','S3.SS2.p3.2','S6.SS2.p2.1','A2.SS3.SSS0.Px2.p1.1','A4.p1.1'],
 '20924':['S4.SS2.p2.1','S7.SS1.p2.1','S7.SS1.p5.1','S9.p4.1'],
 '20926':['S3.SS2.SSS2.p3.1','S3.SS3.p2.1','S4.SS4.p1.1','S4.SS4.p3.1'],
}
out=['# B14 — 六项最小必要原证与actual owner（未授终态）','']
for short,ids in keys.items():
 lines=(ROOT/('V3_PARA_2602.'+short+'.txt')).read_text().splitlines()
 found={line.partition(' | ')[0] for line in lines}
 assert not set(ids)-found,(short,set(ids)-found)
 out+=['## 2602.'+short+'v1','https://arxiv.org/html/2602.'+short+'v1；paragraph身份保留：','']
 for line in lines:
  if line.partition(' | ')[0] in ids:out += [line,'']
lines=(ROOT/'V3_PDF_2602.20904v1.txt').read_text().splitlines()
out+=['## 2602.20904v1','HTML为空转换壳，精确PDF https://arxiv.org/pdf/2602.20904v1 定点机械摘录。','']
for lo,hi in [(220,241),(413,425),(810,833),(880,906),(1258,1266)]:
 out+=['### PDF extraction L%d–%d'%(lo,hi),'\n'.join(lines[lo-1:hi]),'']
for path,ranges in [
 ('books/part-04-training-system/31-rlhf.md',[(255,257)]),
 ('books/part-01-worldview/05-what-neural-networks-learn.md',[(304,311)]),
 ('books/part-04-training-system/30-lora.md',[(595,597),(603,607)]),
 ('books/part-07-agent/75-context.md',[(391,397)]),
 ('books/part-06-ai-infrastructure/66-evaluation-system.md',[(47,49),(108,110)]),
 ('books/part-07-agent/76-rag.md',[(281,283),(805,810)]),
]:
 lines=(PROJECT/path).read_text().splitlines()
 out+=['## Actual owner '+path,'']
 for lo,hi in ranges:out+=['### 原文件L%d–%d'%(lo,hi),'\n'.join(lines[lo-1:hi]),'']
(ROOT/'V3_B14_CORE_OWNER_PACKET.md').write_text('\n'.join(out)+'\n')
print('words',len(' '.join(out).split()))
