import os
import time
import json
import torch
from transformers import AutoTokenizer, AutoModelForMaskedLM
from pynvml import *
from tqdm import tqdm

# ------------------------------
# Settings
# ------------------------------
model_name = "bert-base-uncased"
cache_dir = "./.hfCache"
repeat_count = 1000
num_trials = 20
device_index = 0
output_file = f"16_full.json"

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
# Load model & tokenizer
# ------------------------------
tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir)
model = AutoModelForMaskedLM.from_pretrained(model_name, cache_dir=cache_dir, torch_dtype = torch.float16).cuda()
model.eval()

# Example input
prompt = "The capital of France is"*10 
seq_len = 8
tokens = tokenizer.tokenize(prompt)
stud = tokens[:seq_len]
prompt = tokenizer.convert_tokens_to_string(stud)
inputs = tokenizer(prompt, return_tensors="pt", max_length=seq_len, padding="max_length", truncation=True).to(model.device)

print(inputs)

# ------------------------------
# Measure full forward pass
# ------------------------------
def measure_model_energy(model, inputs, repeat_count, num_trials, label="FullModel"):
    energy_usages = []
    for trial in tqdm(range(num_trials), desc=label):
        with torch.no_grad():
            time.sleep(0.5)
            start_energy = get_gpu_energy_mj()
            for _ in range(repeat_count):
                _ = model(**inputs)
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

results = {"full_model": measure_model_energy(model, inputs, repeat_count, num_trials)}

# ------------------------------
# Save results
# ------------------------------
with open(output_file, "w") as f:
    json.dump(results, f, indent=4)

print(f"\nFull-model energy results saved to {output_file}")

# Shutdown NVML
nvmlShutdown()
