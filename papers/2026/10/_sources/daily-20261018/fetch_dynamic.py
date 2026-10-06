"""Fetch two bounded official directory endpoints, retaining raw responses."""
import concurrent.futures
import datetime
import json
import pathlib
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent

def hunyuan(lang):
    url = 'https://api.hunyuan.tencent.com/api/blog/publicList'
    payload = {'renderType': 0, 'pageNum': 1, 'pageSize': 20}
    headers = {'Content-Type': 'application/json', 'Origin': 'https://hunyuan.tencent.com', 'Referer': 'https://hunyuan.tencent.com/research', 'Accept-Language': lang, 'User-Agent': 'Mozilla/5.0'}
    record = {'url': url, 'payload': payload, 'language': lang, 'checked': datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        request = urllib.request.Request(url, data=json.dumps(payload).encode(), headers=headers)
        with urllib.request.urlopen(request, timeout=20) as response:
            raw = response.read().decode()
            record['status'] = response.status
        (ROOT / ('hunyuan_' + lang + '.raw.json')).write_text(raw)
        data = json.loads(raw)['data']
        record['totalNum'] = data['totalNum']
        record['rows'] = [{k: row.get(k) for k in ('id', 'title', 'publicAt', 'publishedAt', 'displayPublishTime')} for row in data['list']]
    except Exception as error:
        record['error'] = str(error)
    return record

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        result = list(pool.map(hunyuan, ['zh', 'en']))
    (ROOT / 'hunyuan_directory.json').write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(json.dumps(result, ensure_ascii=False, indent=2))
