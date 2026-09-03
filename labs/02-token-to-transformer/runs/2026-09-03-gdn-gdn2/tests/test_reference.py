import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from reference import (  # noqa: E402
    frobenius_delta,
    gdn2_step,
    gdn_step,
    max_abs_difference,
    read,
    zeros,
)


class GatedDeltaReferenceTest(unittest.TestCase):
    def test_gdn2_reduces_to_gdn(self):
        state = [[1.0, 0.5], [-0.25, 0.75]]
        key = [0.6, 0.8]
        value = [0.4, -0.2]
        alpha, beta = 0.9, 0.35

        expected = gdn_step(state, key, value, alpha, beta)
        actual = gdn2_step(
            state,
            key,
            value,
            decay=[alpha, alpha],
            erase_gate=[beta, beta],
            write_gate=[beta, beta],
        )

        self.assertLessEqual(max_abs_difference(expected, actual), 1e-12)

    def test_gdn2_noop_gates_preserve_state(self):
        state = [[1.0, 2.0], [3.0, 4.0]]
        actual = gdn2_step(
            state,
            key=[1.0, 0.0],
            value=[9.0, 9.0],
            decay=[1.0, 1.0],
            erase_gate=[0.0, 0.0],
            write_gate=[0.0, 0.0],
        )
        self.assertEqual(actual, state)

    def test_repeated_exact_association_has_zero_delta(self):
        initial = zeros(2, 2)
        first = gdn_step(initial, [1.0, 0.0], [0.25, 0.75], 1.0, 1.0)
        second = gdn_step(first, [1.0, 0.0], [0.25, 0.75], 1.0, 1.0)
        self.assertLessEqual(frobenius_delta(first, second), 1e-12)

    def test_orthogonal_keys_do_not_interfere_at_capacity(self):
        state = zeros(2, 2)
        state = gdn_step(state, [1.0, 0.0], [1.0, 0.0], 1.0, 1.0)
        state = gdn_step(state, [0.0, 1.0], [0.0, 1.0], 1.0, 1.0)
        self.assertEqual(read(state, [1.0, 0.0]), [1.0, 0.0])
        self.assertEqual(read(state, [0.0, 1.0]), [0.0, 1.0])

    def test_correlated_query_reads_a_superposition(self):
        state = [[1.0, 0.0], [0.0, 1.0]]
        self.assertEqual(read(state, [0.8, 0.6]), [0.8, 0.6])

    def test_correlated_key_write_damages_prior_association(self):
        state = gdn_step(zeros(2, 2), [1.0, 0.0], [1.0, 0.0], 1.0, 1.0)
        state = gdn_step(state, [0.8, 0.6], [0.0, 1.0], 1.0, 1.0)
        self.assertEqual(read(state, [1.0, 0.0]), [0.3599999999999999, 0.8])

    def test_explicit_reset_removes_prior_request_state(self):
        state = gdn_step(zeros(2, 2), [1.0, 0.0], [1.0, 0.0], 1.0, 1.0)
        state = gdn_step(state, [0.0, 1.0], [0.0, 1.0], 0.0, 1.0)
        self.assertEqual(read(state, [1.0, 0.0]), [0.0, 0.0])
        self.assertEqual(read(state, [0.0, 1.0]), [0.0, 1.0])

    def test_gdn2_can_separate_erase_and_write_strength(self):
        state = [[1.0, 0.0], [0.0, 1.0]]
        erase_only = gdn2_step(
            state,
            key=[1.0, 0.0],
            value=[0.0, 1.0],
            decay=[1.0, 1.0],
            erase_gate=[1.0, 1.0],
            write_gate=[0.0, 0.0],
        )
        write_without_erase = gdn2_step(
            state,
            key=[1.0, 0.0],
            value=[0.0, 1.0],
            decay=[1.0, 1.0],
            erase_gate=[0.0, 0.0],
            write_gate=[1.0, 1.0],
        )
        self.assertEqual(erase_only, [[0.0, 0.0], [0.0, 1.0]])
        self.assertEqual(write_without_erase, [[1.0, 1.0], [0.0, 1.0]])


if __name__ == "__main__":
    unittest.main()
