"""Retrieve named exact-v1 manuscripts and current signal pages, not whole categories."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).parent

def fetch(job):
    paper,kind=job
    url=f'https://arxiv.org/html/2606.{paper}v1' if kind=='HTML' else f'https://arxiv.org/abs/2606.{paper}'
    path=ROOT/f'SUP_RAW_{kind}_{paper}_20261026.raw'
    if path.exists() and path.stat().st_size>5000:
        return paper,kind,'already saved',path.stat().st_size
    result=subprocess.run(['curl','-L','--max-time','60','-sS',url,'-o',str(path),'-w','%{http_code}'],capture_output=True,text=True)
    return paper,kind,result.returncode,result.stdout,path.stat().st_size if path.exists() else 0,result.stderr[:100]

if __name__=='__main__':
    papers=[arg for arg in sys.argv[1:] if arg!='--abs-only']
    kinds=('ABS',) if '--abs-only' in sys.argv else ('ABS','HTML')
    jobs=[(paper,kind) for paper in papers for kind in kinds]
    with ThreadPoolExecutor(max_workers=10) as pool:
        for future in as_completed([pool.submit(fetch,job) for job in jobs]):
            print(future.result(),flush=True)
