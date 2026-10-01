"""CPU teaching experiments; finite categorical policies, not an LLM trainer."""

import argparse
import json
import math
import random
from pathlib import Path


def softmax(logits):
    exps = [math.exp(x - max(logits)) for x in logits]
    return [x / sum(exps) for x in exps]


def expected_gradient(logits, rewards):
    probs = softmax(logits)
    baseline = sum(p * r for p, r in zip(probs, rewards))
    return [p * (r - baseline) for p, r in zip(probs, rewards)]


def group_advantages(rewards):
    mean = sum(rewards) / len(rewards)
    std = math.sqrt(sum((r - mean) ** 2 for r in rewards) / len(rewards))
    return [(r - mean) / (std + 1e-8) for r in rewards]


def rloo_advantages(rewards):
    if len(rewards) < 2:
        raise ValueError("RLOO requires at least two samples")
    return [r - (sum(rewards) - r) / (len(rewards) - 1) for r in rewards]


def clipped_term(ratio, advantage, epsilon=0.2):
    clipped = min(1 + epsilon, max(1 - epsilon, ratio))
    return min(ratio * advantage, clipped * advantage)


def dpo_loss(policy, reference, chosen, rejected, beta=0.1):
    margin = beta * (math.log(policy[chosen] / reference[chosen])
                     - math.log(policy[rejected] / reference[rejected]))
    return max(0, -margin) + math.log1p(math.exp(-abs(margin)))


def measure(logits, rewards):
    p = softmax(logits)
    return {
        "probabilities": p,
        "reward": sum(a * b for a, b in zip(p, rewards)),
        "true_success": p[0] + p[1],
        "entropy_nats": -sum(x * math.log(x) for x in p),
        "kl_to_initial": sum(x * math.log(x / 0.25) for x in p),
    }


def train(rewards, sampled=False, seed=7, steps=200, batch_size=64):
    logits = [0.0] * 4
    rng = random.Random(seed)
    history = []
    for step in range(steps + 1):
        if step in (0, 1, 10, 50, 200):
            history.append({"step": step, **measure(logits, rewards)})
        if step == steps:
            break
        p = softmax(logits)
        if sampled:
            # Exact state-only baseline is available only in this tiny example.
            baseline = sum(a * b for a, b in zip(p, rewards))
            actions = rng.choices(range(4), weights=p, k=batch_size)
            grad = [sum((rewards[a] - baseline) * ((a == j) - p[j])
                        for a in actions) / batch_size for j in range(4)]
        else:
            grad = expected_gradient(logits, rewards)
        logits = [z + 0.2 * g for z, g in zip(logits, grad)]
    return history


def verify():
    # A finite-difference check validates the gradient independently of the update.
    z, rewards, eps = [0.1, -0.3, 0.5, 0.0], [1, 1, 0, 0], 1e-6
    gradient = expected_gradient(z, rewards)
    for j in range(4):
        plus, minus = z[:], z[:]
        plus[j] += eps
        minus[j] -= eps
        numerical = (measure(plus, rewards)["reward"]
                     - measure(minus, rewards)["reward"]) / (2 * eps)
        assert abs(numerical - gradient[j]) < 1e-8
    assert group_advantages([1, 1, 1, 1]) == [0.0] * 4
    assert group_advantages([0, 0, 0, 0]) == [0.0] * 4
    assert abs(sum(group_advantages([1, 1, 0, 0]))) < 1e-8
    expected_rloo = [2 / 3, 2 / 3, -2 / 3, -2 / 3]
    assert all(abs(a - b) < 1e-8 for a, b in
               zip(rloo_advantages([1, 1, 0, 0]), expected_rloo))
    assert abs(clipped_term(1.5, 1) - 1.2) < 1e-8
    assert abs(clipped_term(0.5, -1) + 0.8) < 1e-8
    reference = [0.25] * 4
    assert abs(dpo_loss(reference, reference, 1, 0) - math.log(2)) < 1e-8
    assert abs(dpo_loss([0.1, 0.4, 0.3, 0.2], reference, 1, 0)
               - math.log1p(math.exp(-0.1 * math.log(4)))) < 1e-8
    good, hacked = train([1, 1, 0, 0]), train([0, 0, 1, 0])
    assert good[-1]["true_success"] > good[0]["true_success"]
    assert hacked[-1]["reward"] > hacked[0]["reward"]
    assert hacked[-1]["true_success"] < hacked[0]["true_success"]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    verify()
    result = {
        "kind": "actual_cpu_execution_of_teaching_model",
        "task": "Choose among four fixed maze routes; no per-cell navigation is trained here.",
        "answers": ["A: detour reaches exit", "B: short route reaches exit", "C: circles until timeout", "D: times out away from exit"],
        "settings": {"learning_rate": 0.2, "steps": 200, "batch_size": 64,
                     "initial_logits": [0, 0, 0, 0], "seeds": [7, 17, 27]},
        "correct_reward_exact": train([1, 1, 0, 0]),
        "wrong_reward_exact": train([0, 0, 1, 0]),
        "sampled_reinforce": {str(s): train([1, 1, 0, 0], sampled=True, seed=s)
                              for s in (7, 17, 27)},
        "grpo_group": {"reward": [1, 1, 0, 0],
                       "advantage": group_advantages([1, 1, 0, 0]),
                       "all_equal": group_advantages([1, 1, 1, 1])},
        "rloo_group": {"reward": [1, 1, 0, 0],
                       "advantage": rloo_advantages([1, 1, 0, 0])},
        "ppo_clip": {"positive_A_ratio_1.5": clipped_term(1.5, 1),
                     "negative_A_ratio_0.5": clipped_term(0.5, -1)},
        "dpo": {"chosen": "B", "rejected": "A",
                "example_policy": [0.1, 0.4, 0.3, 0.2],
                "initial_loss": dpo_loss([0.25] * 4, [0.25] * 4, 1, 0),
                "improved_margin_loss": dpo_loss([0.1, 0.4, 0.3, 0.2], [0.25] * 4, 1, 0)},
        "checks": "finite_difference_gradient_and_mechanism_assertions_passed",
    }
    payload = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload + "\n", encoding="utf-8")
    for name in ("correct_reward_exact", "wrong_reward_exact"):
        for row in result[name]:
            print(name, row["step"], "reward=%.4f" % row["reward"],
                  "true_success=%.4f" % row["true_success"],
                  "p=" + str([round(x, 4) for x in row["probabilities"]]))
    print("All mechanism checks passed; no LLM or GPU training was performed.")


if __name__ == "__main__":
    main()
