import os
import time
import json
import torch
from transformers import AutoModelForMaskedLM
from pynvml import *
from tqdm import tqdm

# ------------------------------
# Settings
# ------------------------------
model_name = "bert-base-uncased"
cache_dir = "./.hfCache"
activations_file = "activations.pt"   # saved from save_activations_bert.py
repeat_count = 10000
num_trials = 20
device_index = 0
output_file = f"32_parts.json"

# ------------------------------
# NVML Init
# ------------------------------
os.environ["CUDA_VISIBLE_DEVICES"] = str(device_index)
nvmlInit()
handle = nvmlDeviceGetHandleByIndex(device_index)

def get_gpu_energy_mj():
    try:
        return nvmlDeviceGetTotalEnergyConsumption(handle)  # millijoules since boot
    except Exception as e:
        print(f"NVML Error: {e}")
        return 0

# ------------------------------
# Load activations
# ------------------------------
data = torch.load(activations_file)
layer_idx = int(data["layer_idx"])
embeddings_in = torch.cat(data["embeddings"], dim=0).cuda()
attn_in = torch.cat(data["attn_in"], dim=0).cuda()
mlp_in = torch.cat(data["mlp_in"], dim=0).cuda()
mlm_head_in = torch.cat(data["mlm_head_in"], dim=0).cuda()

# Add batch dimension if needed
if embeddings_in.dim() == 2: embeddings_in = embeddings_in.unsqueeze(0)
if attn_in.dim() == 2: attn_in = attn_in.unsqueeze(0)
if mlp_in.dim() == 2: mlp_in = mlp_in.unsqueeze(0)
if mlm_head_in.dim() == 2: mlm_head_in = mlm_head_in.unsqueeze(0)

# ------------------------------
# Load model
# ------------------------------
model = AutoModelForMaskedLM.from_pretrained(model_name, cache_dir=cache_dir, torch_dtype=torch.float16).cuda()
model.eval()
dtype = model.dtype

# Select target layer
chosen_layer = model.bert.encoder.layer[layer_idx]

# ------------------------------
# Helper to measure one module
# ------------------------------
def measure_energy(module, inputs, repeat_count, num_trials, label):
    energy_usages = []
    for trial in tqdm(range(num_trials), desc=label):
        with torch.no_grad():
            time.sleep(0.5)
            start_energy = get_gpu_energy_mj()
            for _ in range(repeat_count):
                _ = module(*inputs) if isinstance(inputs, tuple) else module(inputs)
            end_energy = get_gpu_energy_mj()
        energy_used_per_call_mJ = (end_energy - start_energy) / repeat_count
        energy_usages.append(energy_used_per_call_mJ)
    vals = torch.tensor(energy_usages, dtype=torch.float64)
    return {
        "all_trials": [round(x, 6) for x in energy_usages],
        "average_mJ": round(vals.mean().item(), 6),
        "variance_mJ2": round(vals.var(unbiased=False).item(), 6),
        "std_dev_mJ": round(vals.std(unbiased=False).item(), 6),
    }

# ------------------------------
# Measure components
# ------------------------------
results = {}

# 1. Embeddings
results["embeddings"] = measure_energy(
    module=model.bert.embeddings,
    inputs=(torch.randint(0, model.config.vocab_size, (embeddings_in.size(0), embeddings_in.size(1)), device="cuda"),),
    repeat_count=repeat_count,
    num_trials=num_trials,
    label="Embeddings"
)

# 2. Attention
results["encoder.attention"] = measure_energy(
    module=chosen_layer.attention,
    inputs=attn_in,
    repeat_count=repeat_count,
    num_trials=num_trials,
    label="Attention"
)

# 3. Intermediate (MLP first dense)
results["encoder.intermediate"] = measure_energy(
    module=chosen_layer.intermediate,
    inputs=mlp_in,
    repeat_count=repeat_count,
    num_trials=num_trials,
    label="Intermediate"
)

# 4. Output block (dense + residual + layernorm)
intermediate_out = chosen_layer.intermediate.dense(mlp_in)
results["encoder.output"] = measure_energy(
    module=chosen_layer.output,
    inputs=(intermediate_out, mlp_in),
    repeat_count=repeat_count,
    num_trials=num_trials,
    label="Output"
)

# 5. CLS Head
results["cls"] = measure_energy(
    module=model.cls,
    inputs=mlm_head_in,
    repeat_count=repeat_count,
    num_trials=num_trials,
    label="CLS Head"
)

# ------------------------------
# Save results
# ------------------------------
with open(output_file, "w") as f:
    json.dump(results, f, indent=4)

print(f"\nResults saved to {output_file}")

# Shutdown NVML
nvmlShutdown()
