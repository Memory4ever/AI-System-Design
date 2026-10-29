"""Preserve the independent reader's existing primary response, without GET."""

import argparse
import datetime as dt
import hashlib
import json
from pathlib import Path

BASE = Path(__file__).parent
SOURCE = Path('/var/folders/0s/d7zssqw15m35sw2bkgln8_yc0000gn/T/zeno-sep12-forms-exaajvbe')
EXPECTED = {
    '2509.08182': 'dd521e99a810d732403ac1e9b7ba07baaec7da64692c2ce706f2f97d791428fd',
    '2509.08401': '67e402a1eb58729a6c175c3166b4d6fcec9ea654568982f0471329a853d74afa',
    '2509.08215': '8c95a8af51d1a518c961ff70cb600327176d58f29fe6acd0cc1e49579e421143',
    '2509.08283': '8e56d0ad0cf8f4a4e954b34acc5913eb495edc44862494637de3dd88d13d3283',
    '2509.08381': '900b58a784449d2b89ea8216d587b0cf379a454649e6d6cbe27518bbc4917326',
}

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('ids', nargs='+', choices=EXPECTED)
for identity in parser.parse_args().ids:
    extension = '.pdf' if identity in ('2509.08215', '2509.08381') else '.raw'
    source = SOURCE / (identity + extension)
    raw = source.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != EXPECTED[identity]:
        raise ValueError('Reader response hash mismatch: ' + identity)
    target = BASE / ('FORMS_READER_' + identity + '_20261021' + extension)
    if target.exists():
        if target.read_bytes() != raw:
            raise ValueError('Existing primary response differs')
        print(identity, 'verified existing', len(raw), digest)
        continue
    with target.open('xb') as stream:
        stream.write(raw)
    request_path = Path(str(source) + '.request.json') if extension == '.pdf' else source.with_suffix('.request.json')
    request = json.loads(request_path.read_text())
    record = {'copied_at': dt.datetime.now(dt.timezone.utc).isoformat(),
              'original_path': str(source), 'reader_request': request,
              'bytes': len(raw), 'sha256': digest,
              'purpose': 'Author one non-preparer adoption; reuse reader first GET, no network'}
    with target.with_suffix('.provenance.json').open('x') as stream:
        json.dump(record, stream, ensure_ascii=False, indent=2)
        stream.write('\n')
    print(identity, len(raw), digest)
    if extension == '.pdf':
        for suffix in ('.raw', '.request.json'):
            failed = SOURCE / (identity + suffix)
            destination = BASE / ('FORMS_READER_HTML404_' + identity + '_20261021' + suffix)
            with destination.open('xb') as stream:
                stream.write(failed.read_bytes())
