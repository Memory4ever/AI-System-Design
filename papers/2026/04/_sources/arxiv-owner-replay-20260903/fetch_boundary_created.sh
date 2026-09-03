#!/usr/bin/env bash
set -euo pipefail

repo_root="/Users/apple/Documents/Work/PycharmProject/AI-System-Design"

fetch_day() {
  local day="$1"
  local owner_month="$2"
  local out_dir="${repo_root}/papers/2026/${owner_month}/_sources/arxiv-owner-replay-20260903/boundary-created"
  mkdir -p "${out_dir}"
  local page=1
  while true; do
    local output="${out_dir}/${day}-page-$(printf '%02d' "${page}").json"
    if [[ ! -s "${output}" ]]; then
      curl --get --fail --location --silent --show-error \
        --retry 4 --retry-all-errors --retry-delay 2 --max-time 90 \
        --data-urlencode "query=created:[${day} TO ${day}]" \
        --data-urlencode "prefix=10.48550" \
        --data-urlencode "page[size]=1000" \
        --data-urlencode "page[number]=${page}" \
        --data-urlencode "fields[dois]=doi,created,updated" \
        --output "${output}.tmp" "https://api.datacite.org/dois"
      mv "${output}.tmp" "${output}"
    fi
    local pages
    pages="$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1])).get("meta",{}).get("totalPages",1))' "${output}")"
    if (( page >= pages )); then break; fi
    page=$((page + 1))
  done
}

fetch_day 2026-03-30 04
fetch_day 2026-03-31 04
fetch_day 2026-06-01 05
fetch_day 2026-06-02 05
fetch_day 2026-06-03 05
