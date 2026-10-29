"""Recover prior tracked evidence after case-insensitive filename aliasing.

Retain both byte-identical Git originals and fresh fetched versions. This only
targets this author's known overwritten source files, not unrelated changes.
"""
import hashlib
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent
REPO = ROOT.parents[4]
new_dir = ROOT / 'resume-check'
old_dir = ROOT / 'original-before-resume'
new_dir.mkdir(exist_ok=True)
old_dir.mkdir(exist_ok=True)
names = ['ANTHROPIC.txt','DEEPMIND.raw','DEEPMIND.txt','DEEPSEEK.txt',
         'ERNIE.txt','HUNYUAN.txt','KIMI.txt','META.raw','META.txt','MIMO.txt',
         'MINIMAX.raw','MINIMAX.txt','QWEN.txt','SEED.txt','ZAI.raw','ZAI.txt',
         'fetch-results.json']
records = []
for name in names:
    file = ROOT / name
    relative = file.relative_to(REPO).as_posix()
    old = subprocess.check_output(['git','show','HEAD:'+relative],cwd=REPO)
    fresh = file.read_bytes()
    (new_dir/name).write_bytes(fresh)
    (old_dir/name).write_bytes(old)
    file.write_bytes(old)
    assert file.read_bytes() == old
    records.append({'file':name,'git_original_sha256':hashlib.sha256(old).hexdigest(),
                    'fresh_sha256':hashlib.sha256(fresh).hexdigest(),
                    'restored_exactly':True})
(ROOT/'case-alias-recovery.json').write_text(json.dumps(records,indent=2))
print('Restored',len(records),'tracked source files exactly; originals and fresh requests both retained.')
