#!/usr/bin/env bash
set -euo pipefail

stage="${STAGE:?STAGE is required}"
profile="${PROFILE:?PROFILE is required}"
artifact_root="${ARTIFACT_ROOT:-${PWD}/artifacts}"

cleanup() {
  if [[ "${ray_started:-0}" == "1" ]]; then
    ray stop --force >/dev/null 2>&1 || true
  fi
}
trap cleanup EXIT

case "${stage}" in
  ppo|rloo|grpo)
    gpu_count="${GPU_COUNT:?GPU_COUNT is required for online stages}"
    ray start --head --node-ip-address=0.0.0.0 --num-gpus="${gpu_count}"
    export RAY_ADDRESS="http://127.0.0.1:8265"
    ray_started=1
    ;;
esac

python3 scripts/run_stage.py \
  --stage "${stage}" \
  --profile "${profile}" \
  --artifact-root "${artifact_root}" \
  --execute
