import json,pathlib,sys
root=pathlib.Path(__file__).resolve().parent
rows=json.loads((root/'inventory.json').read_text())['identities']
if sys.argv[1]=='names':
    words=['language','llm','transformer','moe','inference','training','reinforcement','distill','agent','multimodal','generative','diffusion','world model','vision-language','vla','checkpoint','kernel']
    selected=[r for r in rows if any(w in r['title'].lower() for w in words)]
else:
    ids=set(sys.argv[1].split(','));selected=[r for r in rows if r['arxiv_id'].split('.')[1] in ids]
lines=['# 本窗主题查漏题摘','', '原始本窗库存只恢复题名/题摘，不继承旧候选、日期、评分或验收；宽库存479非队列。关键词只命名线索，逐项人工贡献筛选。','']
for r in selected:lines.extend(['## '+r['arxiv_id']+' '+r['title'],'',r['abstract'],''])
(root/sys.argv[2]).write_text('\n'.join(lines)+'\n')
print(len(selected))
