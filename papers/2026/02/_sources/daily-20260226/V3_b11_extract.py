import pathlib,re,html
ROOT=pathlib.Path(__file__).resolve().parent
PROJECT=ROOT.parents[4]
patterns={
 '20732':['Relying solely on partial context selection','Our system manages the KV cache','To maximize GPU utilization','Specifically, we calculate the empirical distribution','Despite the baseline benefiting'],
 '20739':['This accumulative tool reward is added','Finally, even among valid and correct rollouts','To address these challenges, we adopt','Both.*trained for 700','Removing the accumulative tool reward leads','retaining the common standard deviation normalization','uses approximately 5K visual tokens'],
 '20743':['This phase extends standard GEPA','This feedback function is generated once','Sampling follows a round-robin','All methods are run under the same rollout budget','Third, although a key contribution','approximate API costs'],
}
packet=['# B11 — 必要原证与 actual owner（3项，未授终态）','']
for short,keys in patterns.items():
 raw=(ROOT/('V3_CORE_2602.'+short+'.raw')).read_text()
 packet += ['## 2602.'+short+'v1','https://arxiv.org/html/2602.'+short+'v1；原HTML paragraph机械摘段：','']
 for q in re.findall(r'<p\b[^>]*>(.*?)</p>',raw,re.S):
  q=re.sub(r'<math\b[^>]*alttext="([^"]*)".*?</math>',lambda m:' '+html.unescape(m.group(1))+' ',q,flags=re.S)
  s=html.unescape(re.sub('<[^>]*>','',q)).strip()
  if len(s)<6500 and any(re.search(k,s,re.I) for k in keys):packet += [s,'']
for short,ranges in [('20732',[(1226,1254),(1327,1394)]),('20739',[(774,812)]),('20743',[(739,765),(1562,1593)])]:
 lines=(ROOT/('V3_CORE_2602.'+short+'.txt')).read_text().splitlines()
 for lo,hi in ranges:packet += ['### '+short+' 原txt L%d–%d'%(lo,hi),'\n'.join(lines[lo-1:hi]),'']
for path,ranges in [
 ('books/part-05-inference-system/45-why-kv-cache-speeds-up.md',[(188,198)]),
 ('books/part-04-training-system/31-rlhf.md',[(949,955)]),
 ('books/part-04-training-system/33-grpo.md',[(104,132),(2172,2178),(2314,2316)]),
 ('books/part-06-ai-infrastructure/72-security.md',[(253,260)]),
]:
 lines=(PROJECT/path).read_text().splitlines()
 packet += ['## Actual owner '+path,'']
 for lo,hi in ranges:packet += ['### 原文件L%d–%d'%(lo,hi),'\n'.join(lines[lo-1:hi]),'']
(ROOT/'V3_B11_CORE_OWNER_PACKET.md').write_text('\n'.join(packet))
print('words:',len(' '.join(packet).split()))
