#!/usr/bin/env bash
set -euo pipefail

repo_root="/Users/apple/Documents/Work/PycharmProject/AI-System-Design"

fetch_day() {
  local day="$1"
  local month="${day:5:2}"
  local out_dir="${repo_root}/papers/2026/${month}/_sources/arxiv-owner-replay-20260903/datacite-created"
  mkdir -p "${out_dir}"
  local page=1
  while true; do
    local out_file="${out_dir}/${day}-page-$(printf '%02d' "${page}").json"
    if [[ ! -s "${out_file}" ]]; then
      curl --get --fail --location --silent --show-error \
        --retry 6 --retry-all-errors --retry-delay 3 --max-time 240 \
        --data-urlencode "query=created:[${day} TO ${day}]" \
        --data-urlencode "prefix=10.48550" \
        --data-urlencode "page[size]=1000" \
        --data-urlencode "page[number]=${page}" \
        --data-urlencode "fields[dois]=doi,created,updated" \
        --output "${out_file}.tmp" \
        "https://api.datacite.org/dois"
      mv "${out_file}.tmp" "${out_file}"
    fi
    local page_count
    page_count="$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1])).get("meta",{}).get("totalPages",1))' "${out_file}")"
    if (( page >= page_count )); then
      break
    fi
    page=$((page + 1))
  done
}

export -f fetch_day
export repo_root

python3 - <<'PY' | xargs -n 1 -P 3 bash -c 'fetch_day "$0"'
from datetime import date, timedelta

current = date(2026, 4, 1)
end = date(2026, 5, 31)
while current <= end:
    print(current.isoformat())
    current += timedelta(days=1)
PY
