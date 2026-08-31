#!/usr/bin/env python3
"""Freeze exact-v1 primary bodies for the retained 2026-05-07 families."""
from __future__ import annotations
import hashlib, json, subprocess, time
from pathlib import Path

R=Path(__file__).resolve().parent
D=json.loads((R/'screening-ledger-final.json').read_text())
BODY=R/'exact-v1-bodies'; BODY.mkdir(exist_ok=True)
manifest=[]
for x in (z for z in D['identities'] if z['screening_status']=='retained'):
    aid=x['arxiv_id']; target=BODY/f'{aid}v1.html'
    # export.arxiv is substantially more stable for bulk provenance freezing.
    # PDF is exact-v1 even when the HTML renderer is absent.
    target=BODY/f'{aid}v1.pdf'; url=f'https://export.arxiv.org/pdf/{aid}v1'
    if not target.exists() or target.stat().st_size < 2000:
        target.unlink(missing_ok=True)
        subprocess.run(['curl','-L','--retry','1','--max-time','45','-A','Mozilla/5.0','-sS',url,'-o',str(target)],check=False)
    ok=target.exists() and target.stat().st_size >= 2000
    manifest.append({'arxiv_id':aid,'source_family_id':x['source_family_id'],'exact_v1_url':url,'local_body':str(target.relative_to(R)) if ok else None,'retrieved_at':'2026-08-31T00:00:00+08:00','bytes':target.stat().st_size if ok else 0,'sha256':hashlib.sha256(target.read_bytes()).hexdigest() if ok else None,'access_status':'body_frozen' if ok else 'blocked'})
    time.sleep(.15)
(R/'evidence-provenance-manifest.json').write_text(json.dumps({'schema':'evidence-provenance-v2.1','report_date':'2026-05-07','items':manifest},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'total':len(manifest),'body_frozen':sum(x['access_status']=='body_frozen' for x in manifest),'blocked':sum(x['access_status']=='blocked' for x in manifest)}))
