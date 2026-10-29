# Multi-LiveCodeBench

Official repository for the paper "Multi-LCB: Extending LiveCodeBench to Multiple Programming Languages"

<p align="center">
    <a href="https://anonymous.4open.science/r/Multi-LiveCodeBench-C627/">🏠 Home Page</a> •
    <a href="https://multi-lcb.github.io/multi-lcb-page/">🏆 Leaderboard</a> •
    <a href="https://huggingface.co/livecodebench/">💻 Data </a> •
    <a href="https://github.com/LiveCodeBench/LiveCodeBench">💬 LiveCodeBench</a>
</p>

Rigorouse NLP PLP code benchmark based on problems for competitive programming. Supports evaluation on 12 programming languages: 
- c++,
- c#
- python
- java
- rust
- go
- typescript
- javascript
- ruby
- kotlin
- scala
- php

The project is an extension of the LiveCodeBench. You may find more information about the benchmark and its design in the original repository:<br> 
- <a href="https://github.com/LiveCodeBench/LiveCodeBench"> What is LiveCodeBench</a>

# Installation

Install requirements using `conda`. All necessary compilers and dependencies listed in `requirements.txt`. Note that `pyproject.toml` is provided, but we don't build against it.

```bash
conda create -n multi_lcb_env python=3.11
conda activate multi_lcb_env
conda install --file requirements.txt 
```

Test that all compilers setted up correctly by running tests

```bash
# note that some tests will have status 'skipped'
pytest test/tests_plangs

# alternatively run all tests to check for any other missing depencies
pytest test
```

Project was developed and tested on:
```
Ubuntu 22.04.5
conda 25.7.0
GPU NVIDIA H100 80Gb
```

Additionally you may need to set up server environment for sglang/vllm. This is our most preferred way to inference models.
```bash
conda create -n sglang_env python=3.11

# install nvcc (if needed)
conda install nvidia/label/cuda-12.9.0::cuda
which nvcc # check that nvcc works

pip install "sglang[all]==0.5.1" "torch==2.8" "flashinfer_python==0.2.11.post3" 

# fix for pynvml deprecation warning message
pip uninstall pynvml
pip install nvidia-ml-py
```

# Running

1. Start SGlang/VLLM as a separate process. 
2. Run Multi-LCB with async sglang/vllm client


Launch Sglang/VLLM server.
```bash
conda activate sglang_env

MODEL_TAG="Qwen/Qwen2.5-Coder-3B-Instruct"

python3 -m sglang.launch_server \
    --model-path "$MODEL_TAG" \
    --host 0.0.0.0 \
    --port 5000 \
    --dp 8 \
    --tp-size 1 \
    --context-length 32768 \
    --max-running-requests 100 \
    --nnodes 1
```

Next continue with Multi-LCB evaluation:<br>
Args:
* `cot_code_execution` - Turn on reasoning if needed (reco to use `N`=1 for the first cot run)
* `batch_size` - vllm/sglang async queue depth (client side)
* `continue_existing` - Continue with existing generations
* `continue_existing_eval` - Continue with exisiting evaluations
* `num_process_evaluate` - Low values will increase time for evaluation. High values may result in tests failing due to TimeoutErrors. 
* `eval_restarts` - every generated code will be evaluated several times if it execution fail due to TimeOutErrors. We recommend to restart all evaluations with TimeOutErrors at least 3 times. Each restart we decrease number of cpu threads to give more resources for failed tasks.
* `plangs` - Comma separated list of programming languages to evaluate. Or you can use `"all"`. If multiple GPU nodes available running different sets of languages on each node will speed up generation/evaluation. 

```bash
conda activate multi_lcb_env

# SGlang/VLLM server host and port
export OPENAI_BASE_URL=http://localhost:5000/v1
export OPENAI_KEY=dummy

# sglang model name
MODEL_TAG="Qwen/Qwen2.5-Coder-3B-Instruct"

start_date="2024-07-01" # most used cutoff date

temp=0.2 # default LCB 
top_p=0.95 # default LCB 
num=10 # default LCB 

# --batch_size=50  (client async queue depth)
# --cot_code_execution (turn on reasoning, better use with n=1)
python -m lcb_runner.runner.main \
    --model "VLLMAsync" \
    --local_model_path ${MODEL_TAG} \
    --max_tokens 30000 \
    --continue_existing \
    --max_seq_length 32768 \
    --evaluate \
    --temperature ${temp} \
    --top_p ${top_p} \
    --n ${num} \
    --start_date $start_date \
    --batch_size 50 \
    --plangs "all" \
    --cot_code_execution
```

# Post Evaluation Stats collection

If you aleady made generations and evaluations on the whole dataset you may want to filter stats only for specific part of the dataset. Usually you will want to filter problems based on date or platform. This can be done using following script:

```bash
conda activate multi_lcb_env

# Use the same parameters that were used for generation and evaluation
MODEL_TAG="Qwen/Qwen2.5-Coder-3B-Instruct"
temp=0.2 
top_p=0.95
num=10

python -m lcb_runner.evaluation.compute_scores \
    --eval_all_file "leetcode_scores.csv" \
    --model "VLLMAsync" \
    --local_model_path ${MODEL_TAG} \
    --cot_code_execution \
    --temperature ${temp} \
    --top_p ${top_p} \
    --n ${num} \
    --start_date "2024-10-01" \
    --end_date "2025-05-01" \
    --platform "leetcode"
```


## Details on Evaluation
... TBD


## Adding Support for Custom Models
... TBD


