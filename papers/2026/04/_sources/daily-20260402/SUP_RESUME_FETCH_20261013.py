"""Bounded exact-version evidence recovery for the already discovered Apr 2 set."""
import argparse
import concurrent.futures
import datetime
import html.parser
import json
import pathlib
import urllib.request


class Sections(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.active = []
        self.parts = {}
        self.all_text = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'section':
            identity = attrs.get('id') if 'ltx_section' in attrs.get('class', '').split() else None
            self.active.append(identity)
            if identity:
                self.parts[identity] = []

    def handle_endtag(self, tag):
        if tag == 'section' and self.active:
            self.active.pop()

    def handle_data(self, data):
        self.all_text.append(data)
        for identity in self.active:
            if identity:
                self.parts[identity].append(data)


def fetch(identity, destination):
    url = 'https://arxiv.org/html/' + identity
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    request = urllib.request.Request(url, headers={'User-Agent': 'AI-System-Design bounded research'})
    record = {'url': url, 'checked_at': now, 'event_scope': 'existing April 1 supplement hit only'}
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            raw = response.read()
            record.update(status=response.status, response_url=response.url)
        stem = 'SUP_RESUME_CORE_' + identity.replace('.', '-') + '_20261013'
        (destination / (stem + '.raw')).write_bytes(raw)
        parser = Sections()
        parser.feed(raw.decode('utf-8'))
        body = {'id': identity, 'url': url, 'sections': {key: ' '.join(' '.join(value).split()) for key, value in parser.parts.items()}, 'prefix': ' '.join(' '.join(parser.all_text).split())[:3500]}
        (destination / (stem + '.json')).write_text(json.dumps(body, ensure_ascii=False, indent=2))
        (destination / (stem + '.request.json')).write_text(json.dumps(record, ensure_ascii=False, indent=2))
        return {'id': identity, 'status': record['status'], 'sections': list(body['sections']), 'bytes': len(raw)}
    except Exception as error:
        return {'id': identity, 'error': str(error), 'url': url}


def metadata(identity, destination):
    identity = identity.removesuffix('v1')
    stem = 'SUP_RESUME_DATE_' + identity.replace('.', '-') + '_20261013'
    record = {'id': identity, 'checked_at': datetime.datetime.now(datetime.timezone.utc).isoformat()}
    for kind, url in [('abs', 'https://arxiv.org/abs/' + identity), ('doi', 'https://api.datacite.org/dois/10.48550/arxiv.' + identity)]:
        try:
            with urllib.request.urlopen(url, timeout=45) as response:
                raw = response.read()
                record[kind + '_response'] = {'url': response.url, 'status': response.status}
            (destination / (stem + '-' + kind + '.raw')).write_bytes(raw)
            if kind == 'abs':
                parser = Sections()
                parser.feed(raw.decode('utf-8'))
                record['current_abs_text'] = ' '.join(' '.join(parser.all_text).split())
            else:
                data = json.loads(raw)['data']
                record['owned_client'] = data.get('relationships', {}).get('client')
                record['doi_attributes'] = {key: data['attributes'].get(key) for key in ['doi', 'state', 'registered', 'created', 'published', 'publisher', 'url', 'dates']}
        except Exception as error:
            record[kind + '_error'] = str(error)
    (destination / (stem + '.json')).write_text(json.dumps(record, ensure_ascii=False, indent=2))
    return {'id': identity, 'abs': record.get('abs_response', record.get('abs_error')), 'doi': record.get('doi_response', record.get('doi_error'))}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('ids', nargs='+')
    parser.add_argument('--metadata', action='store_true')
    args = parser.parse_args()
    destination = pathlib.Path(__file__).resolve().parent
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        action = metadata if args.metadata else fetch
        for result in executor.map(lambda identity: action(identity, destination), args.ids):
            print(json.dumps(result, ensure_ascii=False))
