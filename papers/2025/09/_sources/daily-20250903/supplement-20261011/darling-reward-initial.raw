import os
import asyncio
import functools
from typing import Dict, List, Optional, Tuple

import httpx
import torch
from transformers import AutoTokenizer
import math

# ──────────────────────────────────────────────────────────────────────────────
# CONFIG – adjust HOSTNAME if needed
# ──────────────────────────────────────────────────────────────────────────────
HOSTNAME    = os.environ["VLLM_SERVER_HOSTNAME"] 
NUM_SERVERS  = 8
SERVER_CFGS  = [
    {"url": f"http://{HOSTNAME}:{8000+i}", "model": f"similarity_gpu_{i}"}
    for i in range(NUM_SERVERS)
]

THRESHOLD = 0.5        # decision boundary: “similar” if prob > 0.45
MAX_LEN   = 4096                   # token budget for CLS + s1 + SEP + s2 + SEP

# ──────────────────────────────────────────────────────────────────────────────
# LIGHTWEIGHT CACHES
# ──────────────────────────────────────────────────────────────────────────────
@functools.cache
def get_tokenizer():
    tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-Embedding-4B")
    if tokenizer.cls_token_id is None:
        tokenizer.cls_token_id = 151644
    if tokenizer.sep_token_id is None:
        tokenizer.sep_token_id = 151645
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        tokenizer.pad_token_id = tokenizer.eos_token_id
    return tokenizer  
                               
@functools.lru_cache(maxsize=None)
def get_client(base_url: str) -> httpx.AsyncClient:
    """Get a new HTTP client for the given URL."""
    return httpx.AsyncClient(base_url=base_url, timeout=600)

# ──────────────────────────────────────────────────────────────────────────────
# VERY CHEAP LOCAL CHECK FOR TINY ANSWERS
# ──────────────────────────────────────────────────────────────────────────────
def maybe_test_equality(r0: str, r1: str) -> Optional[bool]:
    """If both responses ≤5 tokens, decide by exact unigram overlap."""
    u0, u1 = r0.strip().lower().split(), r1.strip().lower().split()
    max_len = max(len(u0), len(u1))
    if max_len <= 5:
        return len(set(u0) & set(u1)) * 2 >= max_len
    return None

# ──────────────────────────────────────────────────────────────────────────────
# TOKENISE TWO SENTENCES INTO  CLS sentence1 SEP sentence2 SEP
# ──────────────────────────────────────────────────────────────────────────────
def build_input_ids(s1: str, s2: str, tokenize=True) -> List[int]:
    tok = get_tokenizer()
    cls, sep = tok.cls_token_id, tok.sep_token_id

    # Reserve space: CLS + SEP + SEP = 3
    # Simple split: truncate each sentence to half of (MAX_LEN-3)
    half = (MAX_LEN - 3) // 2
    if tokenize:
        ids1 = tok.encode(s1, truncation=True, max_length=half, add_special_tokens=False)
        ids2 = tok.encode(s2, truncation=True, max_length=half, add_special_tokens=False)
    
        return [cls] + ids1 + [sep] + ids2 + [sep]
    else: # no tokenization, just split by whitespace
        ids1 = s1.split()[:half]
        ids2 = s2.split()[:half]
        return tok.cls_token + " " + " ".join(ids1) + " " + tok.sep_token + " " + " ".join(ids2) + " " + tok.sep_token
    
# ──────────────────────────────────────────────────────────────────────────────
# REMOTE SIMILARITY SCORE VIA /v1/embeddings
# ──────────────────────────────────────────────────────────────────────────────
async def remote_similarity_prob(s1: str, s2: str, cfg: Dict) -> float:
    """Return P(similar) from the remote classifier."""
    payload = {
        "model": cfg["model"],
        "input": [build_input_ids(s1, s2, tokenize=False)],
    }

    
    max_retries = 3
    retry_delay = 1.0  # Initial delay in seconds
    
    for attempt in range(max_retries):
        try:
            # Get a client - may be cached or new
            client = get_client(cfg["url"])
            
            try:
                resp = await client.post("/classify", json=payload)
                resp.raise_for_status()
                
                #print(resp.json())  # Debugging output
                prob = resp.json()["data"][0]["probs"]
                #print(f"payload: {payload}")  # Debugging output
                #print(f"Logits: {logits}")  # Debugging output
                return prob[-1]
                
            except (httpx.HTTPError, httpx.TimeoutException, httpx.ConnectError, 
                    httpx.ReadError, RuntimeError) as e:
                # If we get a connection error or the "TCPTransport closed" runtime error
                if "TCPTransport closed" in str(e) or isinstance(e, (httpx.ConnectError, httpx.ReadError)):
                    # Clear the cache entry for this URL and create a new client
                    get_client.cache_clear()
                    if attempt < max_retries - 1:  # Not the last attempt
                        continue  # Try again with a new client
                
                # For other errors, follow normal retry logic
                if attempt == max_retries - 1:
                    raise
                    
                wait_time = retry_delay * (2 ** attempt)
                print(f"Request failed (attempt {attempt+1}/{max_retries}): {str(e)}. Retrying in {wait_time:.2f}s...")
                await asyncio.sleep(wait_time)
                
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            wait_time = retry_delay * (2 ** attempt)
            print(f"Unexpected error (attempt {attempt+1}/{max_retries}): {str(e)}. Retrying in {wait_time:.2f}s...")
            await asyncio.sleep(wait_time)

# ──────────────────────────────────────────────────────────────────────────────
# EQUIVALENCE PREDICATE
# ──────────────────────────────────────────────────────────────────────────────
async def equivalence_check(
    prompt: str,
    r0: str,
    r1: str,
    cfg: Dict,
) -> bool:
    eq = maybe_test_equality(r0, r1)
    if eq is not None:
        return eq
    prob_sim = await remote_similarity_prob(r0, r1, cfg)
    #print(f"Comparing:\n  {r0}\n  {r1}\n  -> P(similar) = {prob_sim:.4f}")

    return prob_sim > THRESHOLD

# ──────────────────────────────────────────────────────────────────────────────
# UNION-FIND PARTITIONING FOR ONE UID, RUN ON A GIVEN SERVER
# ──────────────────────────────────────────────────────────────────────────────
async def process_uid_partition(
    uid: str,
    responses: List[str],
    indices: List[int],
    prompt: str,
    cfg: Dict,
) -> Tuple[str, List[List[int]]]:
    n = len(responses)
    parent = list(range(n))

    def find(x):               # path-compressed
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        pa, pb = find(a), find(b)
        if pa != pb:
            parent[pa] = pb

    # Launch all pairwise checks concurrently
    async def check(i, j):
        same = await equivalence_check(prompt, responses[i], responses[j], cfg)
        return i, j, same

    tasks = [check(i, j) for i in range(n) for j in range(i + 1, n)]
    for i, j, same in await asyncio.gather(*tasks):
        if same:
            union(i, j)

    # Gather partitions
    groups: Dict[int, List[int]] = {}
    for k in range(n):
        root = find(k)
        groups.setdefault(root, []).append(indices[k])

    return uid, list(groups.values())

# ──────────────────────────────────────────────────────────────────────────────
# ASYNC FAN-OUT ACROSS UID BLOCKS & SERVERS
# ──────────────────────────────────────────────────────────────────────────────
async def partition_async(
    solution_str: List[str],
    uid: List[str],
    prompts: List[str],
) -> Dict[str, List[List[int]]]:
    # bucket answers by uid
    by_uid_resp, by_uid_idx, by_uid_prompt = {}, {}, {}
    for idx, (ans, u, prm) in enumerate(zip(solution_str, uid, prompts)):
        by_uid_resp.setdefault(u, []).append(ans)
        by_uid_idx.setdefault(u, []).append(idx)
        by_uid_prompt.setdefault(u, prm)

    # create one task per uid, round-robin across servers
    tasks = []
    for n, (u, resps) in enumerate(by_uid_resp.items()):
        cfg = SERVER_CFGS[n % NUM_SERVERS]
        tasks.append(
            asyncio.create_task(
                process_uid_partition(
                    u, resps, by_uid_idx[u], by_uid_prompt[u], cfg
                )
            )
        )

    results = await asyncio.gather(*tasks)
    return {u: parts for u, parts in results}

# ──────────────────────────────────────────────────────────────────────────────
# SYNC WRAPPER –  REWARD = distinct_count / TOTAL_RESPONSES
# ──────────────────────────────────────────────────────────────────────────────
def partition(**kwargs) -> List[float]:
    solution_str: List[str] = kwargs.get("solution_str", [])
    uid          : List[str] = kwargs.get("uid")
    prompts      : List[str] = kwargs.get("prompts", [])

    if uid is None:
        raise ValueError("uid is required for partition reward function")

    # async partitioning
    uid_parts = asyncio.run(partition_async(solution_str, uid, prompts))

    # map uid → list of indices (for totals)
    uid_to_indices: Dict[str, List[int]] = {}
    for i, u in enumerate(uid):
        uid_to_indices.setdefault(u, []).append(i)

    # raw distinct counts
    rewards = [0] * len(solution_str)
    for u, parts in uid_parts.items():
        # Use total responses for this specific UID (not all responses)
        total_for_uid = len(uid_to_indices[u])
        
        for grp in parts:
            # Calculate distinctness within this UID group
            distinct = total_for_uid - len(grp)
            
            for idx in grp:
                # Normalize by total responses for this UID minus one (to avoid self-counting)
                rewards[idx] = distinct / (total_for_uid - 1)
    
    # if zero reward to 0.1
    rewards = [max(r, 0.1) for r in rewards]

    return rewards

def partition_sigmoid(**kwargs) -> List[float]:
    """Sigmoid-based partitioning reward function."""
    rewards = partition(**kwargs)
    return [1 / (1 + math.exp(-r)) for r in rewards]

async def process_uid_partition_correct(
    uid: str,
    responses: List[str],
    indices: List[int],
    correctness: List[bool],
    prompt: str,
    cfg: Dict,
) -> Tuple[str, List[List[int]]]:
    """Partition only correct responses and assign rewards accordingly."""
    n = len(responses)
    
    # Filter to only correct responses
    correct_mask = [correctness[i] for i in range(n)]
    correct_indices = [i for i in range(n) if correct_mask[i]]
    correct_responses = [responses[i] for i in correct_indices]
    
    if len(correct_responses) <= 1:
        # If 0 or 1 correct responses, no partitioning needed
        # Return each response as its own partition
        return uid, [[indices[i]] for i in range(n)]
    
    # Set up union-find for correct responses only
    correct_n = len(correct_responses)
    parent = list(range(correct_n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        pa, pb = find(a), find(b)
        if pa != pb:
            parent[pa] = pb

    # Launch pairwise checks for correct responses only
    async def check(i, j):
        same = await equivalence_check(prompt, correct_responses[i], correct_responses[j], cfg)
        return i, j, same

    tasks = [check(i, j) for i in range(correct_n) for j in range(i + 1, correct_n)]
    for i, j, same in await asyncio.gather(*tasks):
        if same:
            union(i, j)

    # Gather partitions of correct responses
    correct_groups: Dict[int, List[int]] = {}
    for k in range(correct_n):
        root = find(k)
        # Map back to original indices
        original_idx = indices[correct_indices[k]]
        correct_groups.setdefault(root, []).append(original_idx)

    # Add incorrect responses as singleton partitions
    all_partitions = list(correct_groups.values())
    for i in range(n):
        if not correct_mask[i]:
            all_partitions.append([indices[i]])

    return uid, all_partitions

async def partition_correct_async(
    solution_str: List[str],
    uid: List[str],
    prompts: List[str],
    correctness: List[bool],
) -> Dict[str, List[List[int]]]:
    """Async partitioning considering only correct responses."""
    # bucket answers by uid
    by_uid_resp, by_uid_idx, by_uid_prompt, by_uid_correct = {}, {}, {}, {}
    for idx, (ans, u, prm, corr) in enumerate(zip(solution_str, uid, prompts, correctness)):
        by_uid_resp.setdefault(u, []).append(ans)
        by_uid_idx.setdefault(u, []).append(idx)
        by_uid_prompt.setdefault(u, prm)
        by_uid_correct.setdefault(u, []).append(corr)

    # create one task per uid, round-robin across servers
    tasks = []
    for n, (u, resps) in enumerate(by_uid_resp.items()):
        cfg = SERVER_CFGS[n % NUM_SERVERS]
        tasks.append(
            asyncio.create_task(
                process_uid_partition_correct(
                    u, resps, by_uid_idx[u], by_uid_correct[u], by_uid_prompt[u], cfg
                )
            )
        )

    results = await asyncio.gather(*tasks)
    return {u: parts for u, parts in results}

def partition_correct(**kwargs) -> List[float]:
    """Partition reward function that only considers correct responses for diversity."""
    solution_str: List[str] = kwargs.get("solution_str", [])
    uid: List[str] = kwargs.get("uid")
    prompts: List[str] = kwargs.get("prompts", [])
    correctness: List[bool] = kwargs.get("correctness")

    if uid is None:
        raise ValueError("uid is required for partition reward function")
    if correctness is None:
        raise ValueError("correctness is required for partition_correct reward function")

    # async partitioning considering only correct responses
    uid_parts = asyncio.run(partition_correct_async(solution_str, uid, prompts, correctness))

    # map uid → list of indices (for totals)
    uid_to_indices: Dict[str, List[int]] = {}
    uid_to_correct_count: Dict[str, int] = {}
    
    for i, (u, corr) in enumerate(zip(uid, correctness)):
        uid_to_indices.setdefault(u, []).append(i)
        if corr:
            uid_to_correct_count[u] = uid_to_correct_count.get(u, 0) + 1

    # Calculate rewards
    rewards = [0.0] * len(solution_str)
    
    for u, parts in uid_parts.items():
        correct_count = uid_to_correct_count.get(u, 0)
        
        if correct_count <= 1:
            # If 0 or 1 correct responses, give minimal reward to all
            for idx in uid_to_indices[u]:
                rewards[idx] = 0.1
            continue
            
        for grp in parts:
            # Only calculate diversity for correct responses
            if any(correctness[idx] for idx in grp):
                # This partition contains correct response(s)
                distinct = correct_count - len([idx for idx in grp if correctness[idx]])
                for idx in grp:
                    if correctness[idx]:  # Only reward correct responses
                        rewards[idx] = distinct / (correct_count - 1)
                    else:
                        rewards[idx] = 0.1  # Minimal reward for incorrect
            else:
                # This partition contains only incorrect responses
                for idx in grp:
                    rewards[idx] = 0.1

    # Ensure minimum reward
    rewards = [max(r, 0.1) for r in rewards]
    return rewards

import asyncio
from typing import Dict, List, Tuple

# Mock implementation for testing without actual API calls
async def mock_partition_async(solution_str, uid, prompts):
    """Mock version that simulates the partitioning without API calls"""
    
    return await partition_async(solution_str, uid, prompts)

def test_partition():
    """Test the reward function with mock partitioning"""
    # Two prompts with three responses each (2 similar, 1 distinct per prompt)
    print("Testing partition reward function with mock data...")
    solution_str = [
        # UID1 - Capital of France (responses 0-2)
        "The capital of France is Paris.",
        "Paris is the capital of France.",
        "France's capital city is known for the Eiffel Tower, located in Paris.",
        
        # UID2 - Programming joke (responses 3-5)
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "I would tell you a joke about programming, but it only works on my machine."
    ]
    
    uid = ["uid1", "uid1", "uid1", "uid2", "uid2", "uid2"]
    prompts = [
        "What is the capital of France?", 
        "What is the capital of France?", 
        "What is the capital of France?", 
        "Write a short joke about programming.", 
        "Write a short joke about programming.", 
        "Write a short joke about programming."
    ]

    solution_str_math = [
        "8 times 7 = 56",
        "7 times 8 = 56",
        "8*10 - 8*3 = 56 (distributive property)",
        "15 - 6 = 9",
        "9 + 6 = 15",
        "Count down from 15: 14, 13, 12, 11, 10, 9 (6 subtracted), 9 apples left."
    ]   

    uid_math = ["uid1", "uid1", "uid1", "uid2", "uid2", "uid2"]
    prompts_math = [
        "What is the value of 8 times 7?",
        "What is the value of 8 times 7?",
        "What is the value of 8 times 7?",
        "If you have 15 apples and give away 6, how many do you have left?",
        "If you have 15 apples and give away 6, how many do you have left?",
        "If you have 15 apples and give away 6, how many do you have left?"
    ]
    
    solution_str = solution_str_math  # Use math prompts for testing
    uid = uid_math  # Use math UIDs for testing
    prompts = prompts_math  # Use math prompts for testing
    # Calculate rewards using our mock partition
    rewards = [0] * len(solution_str)
    
    # Mock the partitioning results
    uid_parts = asyncio.run(mock_partition_async(solution_str, uid, prompts))
    
    # Map uid → list of indices
    uid_to_indices = {}
    for i, u in enumerate(uid):
        uid_to_indices.setdefault(u, []).append(i)
    
    # Calculate rewards
    for u, parts in uid_parts.items():
        total_for_uid = len(uid_to_indices[u])
        for grp in parts:
            distinct = total_for_uid - len(grp)
            for idx in grp:
                rewards[idx] = distinct / total_for_uid
    
    # Print results
    for i, response in enumerate(solution_str):
        print(f"Response {i}: {response}")
        print(f"  → Reward: {rewards[i]:.4f}")
    print("Rewards:", rewards)
    
    
if __name__ == "__main__":
    test_partition()
