import pathlib
ROOT=pathlib.Path(__file__).resolve().parent
PROJECT=ROOT.parents[4]
keys={
 '20937':['S4.SS1.p2.1','Thmassumption3.p1.1','A2.SS1.p2.1','A2.SS1.p3.1'],
 '20943':['S3.SS2.SSS0.Px2.p2.1','S3.SS2.SSS0.Px2.p2.3','S4.SS2.p2.1','S4.SS4.p3.1'],
 '20945':['S3.SS1.SSS0.Px1.p2.1','S3.SS2.SSS0.Px1.p2.1','S3.SS2.SSS0.Px4.p1.1','Sx1.SS0.SSS0.Px3.p1.1'],
 '20951':['S4.I2.i1.p1.1','S4.I2.i2.p1.1','S5.p3.1','A8.p2.1'],
 '20972':['S2.SS3.p3.1','S4.SS1.SSS0.Px1.p1.1','A4.SS0.SSS0.Px4.p1.1'],
 '20973':['S5.SS1.p2.1','S5.SS4.p1.1','S5.SS4.p2.1'],
 '20976':['S4.SS1.SSS0.Px2.p1.1','S6.SS0.SSS0.Px2.p1.1','S7.SS0.SSS0.Px2.p2.1','Sx1.p2.1'],
 '20980':['S3.SS3.SSS0.Px2.p1.1','S3.SS4.SSS0.Px1.p2.1','S4.SS3.p3.1','S4.SS3.p4.1'],
}
out=['# B15 — 八项最小必要原证与actual owner（未授终态）','']
for short,ids in keys.items():
 lines=(ROOT/('V3_PARA_2602.'+short+'.txt')).read_text().splitlines()
 found={line.partition(' | ')[0] for line in lines}
 assert not set(ids)-found,(short,set(ids)-found)
 out+=['## 2602.'+short+'v1','https://arxiv.org/html/2602.'+short+'v1；paragraph身份保留：','']
 for line in lines:
  if line.partition(' | ')[0] in ids:out += [line,'']
lines=(ROOT/'V3_CORE_2602.20937.txt').read_text().splitlines()
out+=['### 20937 C.2 原display formula TeX（L1295–1320内机械筛出）']
out += [s for s in lines[1294:1320] if '\\mathbf' in s]
out+=['']
lines=(ROOT/'V3_CORE_2602.20945.txt').read_text().splitlines()
out+=['### 20945 原Eq2 TeX（原txt L337）',lines[336],'']
for path,ranges in [
 ('books/part-04-training-system/28-pretraining.md',[(656,658)]),
 ('books/part-03-multimodal-world-models/25-multimodal-world-models.md',[(1001,1003),(1009,1009)]),
 ('books/part-04-training-system/31-rlhf.md',[(785,790)]),
 ('books/part-04-training-system/27-data.md',[(329,332),(240,248),(308,310),(800,810)]),
 ('books/part-06-ai-infrastructure/66-evaluation-system.md',[(132,134),(94,104),(3671,3673)]),
 ('books/part-03-multimodal-world-models/23-multimodal-representation.md',[(1046,1054)]),
]:
 lines=(PROJECT/path).read_text().splitlines()
 out+=['## Actual owner '+path,'']
 for lo,hi in ranges:out+=['### 原文件L%d–%d'%(lo,hi),'\n'.join(lines[lo-1:hi]),'']
(ROOT/'V3_B15_CORE_OWNER_PACKET.md').write_text('\n'.join(out)+'\n')
print('words',len(' '.join(out).split()))
