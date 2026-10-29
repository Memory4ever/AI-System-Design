"""Bounded source retrieval for Jun15 BJT supplement; raw downloads are not review."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import subprocess
import json
from urllib.parse import urlencode

ROOT = Path(__file__).parent
URLS = {
    'OPENAI_RSS':'https://openai.com/news/rss.xml',
    'ANTHROPIC':'https://www.anthropic.com/research',
    'ANTHROPIC_HISTORY':'https://www.anthropic.com/listing/research/default/2',
    'DEEPMIND_RESEARCH':'https://deepmind.google/research/',
    'DEEPMIND_BLOG':'https://deepmind.google/blog/page/2/',
    'DEEPMIND_CONSCIOUSNESS':'https://deepmind.google/research/publications/248131/',
    'QWEN_EN':'https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=en-US',
    'QWEN_ZH':'https://qwen.ai/api/v2/article/retrieval?type=qwen_ai&language=zh-CN',
    'DEEPSEEK':'https://api-docs.deepseek.com/updates',
    'MOONSHOT_BLOG':'https://platform.kimi.com/blog',
    'MOONSHOT_REPOS':'https://api.github.com/orgs/MoonshotAI/repos?per_page=100&sort=updated',
    'HUNYUAN':'https://hunyuan.tencent.com/research',
    'ZAI':'https://www.zhipuai.cn/zh/research',
    'SEED':'https://seed.bytedance.com/en/public_papers',
    'ERNIE':'https://ernie.baidu.com/blog/zh/',
    'MIMO':'https://mimo.xiaomi.com/',
    'MIMO_BUNDLE':'https://cdn.cnbj1.fds.api.mi-img.com/aife/mimo-blog-fe/doc_build/static/js/4752.2908c99e.js',
    'MIMO_MODEL':'https://mimo.mi.com/docs/en-US/updates/model',
    'MINIMAX':'https://www.minimax.io/blog',
    'ARXIV_RULES':'https://info.arxiv.org/help/availability.html',
    'ARXIV_CL':'https://arxiv.org/list/cs.CL/2026-06',
    'ARXIV_LG':'https://arxiv.org/list/cs.LG/2026-06',
}
DATE = 'registered:[2026-06-14T16:00:00Z TO 2026-06-15T15:59:59Z]'
for key, terms in {
    'DATACITE_LM':'(titles.title:("language model" OR "language models" OR LLM OR LLMs OR transformer OR transformers OR "mixture of experts" OR MoE OR RLVR OR RLHF OR GRPO OR attention OR tokenizer OR pretraining OR "post-training"))',
    'DATACITE_SYSTEM':'(titles.title:(GPU OR GPUs OR kernel OR kernels OR collective OR inference OR serving OR quantization OR "distributed training" OR "tensor parallel" OR "pipeline parallel" OR "KV cache"))',
    'DATACITE_AGENT':'(titles.title:(agent OR agents OR agentic OR reasoning OR RAG OR retrieval OR memory OR "tool use"))',
    'DATACITE_MULTI':'(titles.title:(multimodal OR "vision-language" OR "world model" OR "world models" OR "video generation" OR "image generation" OR diffusion OR VLA OR "foundation model" OR "foundation models"))',
}.items():
    URLS[key] = 'https://api.datacite.org/dois?' + urlencode({'client-id':'arxiv.content','query':DATE+' AND '+terms,'page[size]':1000})

def fetch(item):
    key, url = item
    path = ROOT / ('SUP_RAW_'+key+'_20261026.raw')
    cmd=['curl','-L','--max-time','120','--retry','1','-sS',url,'-o',str(path),'-w','%{http_code}']
    p=subprocess.run(cmd,capture_output=True,text=True)
    return {'key':key,'url':url,'returncode':p.returncode,'status':p.stdout,'bytes':path.stat().st_size if path.exists() else 0,'error':p.stderr[:200]}

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=10) as pool:
        for future in as_completed([pool.submit(fetch,item) for item in URLS.items()]):
            print(json.dumps(future.result(),ensure_ascii=False),flush=True)
