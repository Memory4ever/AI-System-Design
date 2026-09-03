#!/usr/bin/env python3
"""Dependency-free GDN/GDN-2 recurrence reference.

This file implements only the equations needed for correctness experiments. It
does not copy or approximate the official GPU kernels and must not be used for
performance claims.
"""

import json
import math
from typing import Dict, List, Sequence


Vector = List[float]
Matrix = List[List[float]]


def zeros(rows: int, columns: int) -> Matrix:
    return [[0.0 for _ in range(columns)] for _ in range(rows)]


def _shape(state: Sequence[Sequence[float]]) -> tuple:
    rows = len(state)
    columns = len(state[0]) if rows else 0
    if any(len(row) != columns for row in state):
        raise ValueError("state must be rectangular")
    return rows, columns


def _validate(
    state: Sequence[Sequence[float]],
    key: Sequence[float],
    value: Sequence[float],
) -> None:
    d_key, d_value = _shape(state)
    if len(key) != d_key:
        raise ValueError("key dimension must match state rows")
    if len(value) != d_value:
        raise ValueError("value dimension must match state columns")


def read(state: Sequence[Sequence[float]], query: Sequence[float]) -> Vector:
    d_key, d_value = _shape(state)
    if len(query) != d_key:
        raise ValueError("query dimension must match state rows")
    return [
        sum(state[key_index][value_index] * query[key_index] for key_index in range(d_key))
        for value_index in range(d_value)
    ]


def gdn_step(
    state: Sequence[Sequence[float]],
    key: Sequence[float],
    value: Sequence[float],
    alpha: float,
    beta: float,
) -> Matrix:
    """Apply Eq. 6 from Gated DeltaNet-2 using [d_key, d_value] state."""

    _validate(state, key, value)
    if not 0.0 <= alpha <= 1.0:
        raise ValueError("alpha must be in [0, 1]")
    if not 0.0 <= beta <= 1.0:
        raise ValueError("beta must be in [0, 1] for this reference")

    d_key, d_value = _shape(state)
    decayed = [[alpha * state[i][j] for j in range(d_value)] for i in range(d_key)]
    old_value = [
        sum(key[i] * decayed[i][j] for i in range(d_key))
        for j in range(d_value)
    ]
    return [
        [
            decayed[i][j] - beta * key[i] * old_value[j] + beta * key[i] * value[j]
            for j in range(d_value)
        ]
        for i in range(d_key)
    ]


def gdn2_step(
    state: Sequence[Sequence[float]],
    key: Sequence[float],
    value: Sequence[float],
    decay: Sequence[float],
    erase_gate: Sequence[float],
    write_gate: Sequence[float],
) -> Matrix:
    """Apply Gated Delta Rule-2 Eq. 29 with state shape [d_key, d_value]."""

    _validate(state, key, value)
    d_key, d_value = _shape(state)
    if len(decay) != d_key or len(erase_gate) != d_key:
        raise ValueError("decay and erase_gate must have d_key elements")
    if len(write_gate) != d_value:
        raise ValueError("write_gate must have d_value elements")
    for name, values in (
        ("decay", decay),
        ("erase_gate", erase_gate),
        ("write_gate", write_gate),
    ):
        if any(not 0.0 <= item <= 1.0 for item in values):
            raise ValueError(f"{name} values must be in [0, 1]")

    decayed = [[decay[i] * state[i][j] for j in range(d_value)] for i in range(d_key)]
    erase_key = [erase_gate[i] * key[i] for i in range(d_key)]
    old_value = [
        sum(erase_key[i] * decayed[i][j] for i in range(d_key))
        for j in range(d_value)
    ]
    new_value = [write_gate[j] * value[j] for j in range(d_value)]
    return [
        [decayed[i][j] - key[i] * old_value[j] + key[i] * new_value[j] for j in range(d_value)]
        for i in range(d_key)
    ]


def max_abs_difference(left: Sequence[Sequence[float]], right: Sequence[Sequence[float]]) -> float:
    if _shape(left) != _shape(right):
        raise ValueError("matrix shapes must match")
    return max(
        (abs(a - b) for left_row, right_row in zip(left, right) for a, b in zip(left_row, right_row)),
        default=0.0,
    )


def frobenius_delta(before: Sequence[Sequence[float]], after: Sequence[Sequence[float]]) -> float:
    if _shape(before) != _shape(after):
        raise ValueError("matrix shapes must match")
    return math.sqrt(
        sum((a - b) ** 2 for before_row, after_row in zip(before, after) for a, b in zip(before_row, after_row))
    )


def run_scenarios() -> Dict[str, object]:
    initial = [[1.0, 0.5], [-0.25, 0.75]]
    key = [0.6, 0.8]
    value = [0.4, -0.2]
    alpha = 0.9
    beta = 0.35
    gdn = gdn_step(initial, key, value, alpha, beta)
    reduced_gdn2 = gdn2_step(
        initial,
        key,
        value,
        [alpha, alpha],
        [beta, beta],
        [beta, beta],
    )

    state = zeros(2, 2)
    key_a, value_a = [1.0, 0.0], [1.0, 0.0]
    key_b, value_b = [0.0, 1.0], [0.0, 1.0]
    state = gdn_step(state, key_a, value_a, alpha=1.0, beta=1.0)
    after_first_write = [row[:] for row in state]
    repeated = gdn_step(state, key_a, value_a, alpha=1.0, beta=1.0)
    state = gdn_step(repeated, key_b, value_b, alpha=1.0, beta=1.0)

    correlated_key = [0.8, 0.6]
    correlated_read = read(state, correlated_key)
    correlated_write_state = gdn_step(
        after_first_write,
        correlated_key,
        value_b,
        alpha=1.0,
        beta=1.0,
    )

    reset_state = gdn_step(
        after_first_write,
        key_b,
        value_b,
        alpha=0.0,
        beta=1.0,
    )

    erase_only = gdn2_step(
        [[1.0, 0.0], [0.0, 1.0]],
        key_a,
        value_b,
        decay=[1.0, 1.0],
        erase_gate=[1.0, 1.0],
        write_gate=[0.0, 0.0],
    )
    write_without_erase = gdn2_step(
        [[1.0, 0.0], [0.0, 1.0]],
        key_a,
        value_b,
        decay=[1.0, 1.0],
        erase_gate=[0.0, 0.0],
        write_gate=[1.0, 1.0],
    )

    return {
        "gdn2_reduces_to_gdn_max_abs_error": max_abs_difference(gdn, reduced_gdn2),
        "repeat_same_association_state_delta": frobenius_delta(after_first_write, repeated),
        "orthogonal_key_a_read": read(state, key_a),
        "orthogonal_key_b_read": read(state, key_b),
        "correlated_query_mixed_read": correlated_read,
        "original_key_after_correlated_write": read(correlated_write_state, key_a),
        "original_key_after_explicit_reset": read(reset_state, key_a),
        "new_key_after_explicit_reset": read(reset_state, key_b),
        "gdn2_erase_only_state": erase_only,
        "gdn2_write_without_erase_state": write_without_erase,
        "state_elements_independent_of_sequence_length": 4,
    }


def main() -> None:
    results = run_scenarios()
    if results["gdn2_reduces_to_gdn_max_abs_error"] > 1e-12:
        raise AssertionError("GDN-2 reduction check failed")
    if results["repeat_same_association_state_delta"] > 1e-12:
        raise AssertionError("repeated association should not change unit-strength Delta state")
    print(json.dumps(results, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
