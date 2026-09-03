#!/usr/bin/env bash
set -euo pipefail

repo_root="/Users/apple/Documents/Work/PycharmProject/AI-System-Design"
# Full DataCite records are large enough that 1,000-row responses repeatedly
# hit the request timeout.  Keep the abandoned large-page attempt separate and
# use a stable 250-row page size for the canonical content snapshot.
out_dir="${repo_root}/papers/2026/08/_sources/arxiv-owner-replay-20260903/datacite-content-p250"
mkdir -p "${out_dir}"

fetch_day() {
  local day="$1"
  local page=1
  while true; do
    local output="${out_dir}/${day}-page-$(printf '%02d' "${page}").json"
    if [[ ! -s "${output}" ]]; then
      curl --get --fail --location --silent --show-error \
        --retry 6 --retry-all-errors --retry-delay 3 --max-time 180 \
        --data-urlencode "query=created:[${day} TO ${day}]" \
        --data-urlencode "prefix=10.48550" \
        --data-urlencode "page[size]=250" \
        --data-urlencode "page[number]=${page}" \
        --output "${output}.tmp" \
        "https://api.datacite.org/dois"
      mv "${output}.tmp" "${output}"
    fi

    local page_count
    page_count="$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1])).get("meta",{}).get("totalPages",1))' "${output}")"
    if (( page >= page_count )); then
      break
    fi
    page=$((page + 1))
  done
}

export -f fetch_day
export out_dir

python3 - <<'PY' | xargs -n 1 -P 6 bash -c 'fetch_day "$0"'
from datetime import date, timedelta

current = date(2026, 7, 30)
end = date(2026, 9, 2)
while current <= end:
    print(current.isoformat())
    current += timedelta(days=1)
PY
