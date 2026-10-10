"""Read-only exact identity recovery; metadata dates are not first-public claims."""
import concurrent.futures
import json
import sys
import urllib.request


def recover(paper_id):
    url = 'https://api.datacite.org/dois/10.48550/arXiv.' + paper_id
    try:
        data = json.load(urllib.request.urlopen(url, timeout=35))['data']['attributes']
        keys = ['doi', 'titles', 'dates', 'created', 'registered', 'published', 'state', 'relatedIdentifiers', 'url']
        return dict(query_url=url, **{key: data.get(key) for key in keys})
    except Exception as error:
        return {'url': url, 'error': str(error)}


with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
    for result in pool.map(recover, sys.argv[1:]):
        print(json.dumps(result, ensure_ascii=False))
