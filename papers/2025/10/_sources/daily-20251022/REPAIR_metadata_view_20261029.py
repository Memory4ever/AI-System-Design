"""Read only named identity metadata from this day's finite discovery originals."""
import json
import sys
from pathlib import Path

root = Path(__file__).parent
records = {}
for path in root.glob('REPAIR_VALID_REGISTERED_*_P1_20261029.json'):
    for row in json.loads(path.read_text())['data']:
        records[row['id'].split('arxiv.')[-1]] = row['attributes']
for key in sys.argv[1:]:
    key = key if '.' in key else '2510.' + key
    row = records[key]
    print('\nID', key, row.get('titles'))
    for description in row.get('descriptions', []):
        print(description['descriptionType'], description['description'])
