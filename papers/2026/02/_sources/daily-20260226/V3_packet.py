import json, pathlib, sys, gzip
ROOT=pathlib.Path(__file__).resolve().parent
ids=sys.argv[1].split(',')
inventory=json.loads((ROOT/'inventory.json').read_text())['identities']
records={r['arxiv_id']:r for r in inventory}
packet=[]
for short in ids:
    identity=short if short.startswith('2602.') else '2602.'+short
    r=records[identity]
    packet += ['## '+identity+' '+r['title'],'','恢复来源：本日本地原始 identity/完整题摘；不继承旧评分、候选、日期或验收。', '', r['abstract'],'']
(ROOT/sys.argv[2]).write_text('\n'.join(packet))
