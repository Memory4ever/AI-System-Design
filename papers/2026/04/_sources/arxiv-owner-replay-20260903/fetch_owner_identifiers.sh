#!/usr/bin/env bash
set -euo pipefail

repo_root="/Users/apple/Documents/Work/PycharmProject/AI-System-Design"

fetch_one() {
  local day="$1"
  local set_name="$2"
  local month="${day:5:2}"
  local out_dir="${repo_root}/papers/2026/${month}/_sources/arxiv-owner-replay-20260903/oai-list-identifiers"
  local out_file="${out_dir}/${day}-${set_name}.xml"
  mkdir -p "${out_dir}"
  if [[ -s "${out_file}" ]]; then
    return 0
  fi
  curl --fail --location --silent --show-error \
    --retry 6 --retry-all-errors --retry-delay 3 --max-time 180 \
    --output "${out_file}.tmp" \
    "https://oaipmh.arxiv.org/oai?verb=ListIdentifiers&from=${day}&until=${day}&set=${set_name}&metadataPrefix=arXivRaw"
  mv "${out_file}.tmp" "${out_file}"
}

export -f fetch_one
export repo_root

python3 - <<'PY' | xargs -n 2 -P 3 bash -c 'fetch_one "$0" "$1"'
from datetime import date, timedelta

current = date(2026, 4, 1)
end = date(2026, 5, 31)
while current <= end:
    for set_name in ("cs", "stat", "eess"):
        print(current.isoformat(), set_name)
    current += timedelta(days=1)
PY
