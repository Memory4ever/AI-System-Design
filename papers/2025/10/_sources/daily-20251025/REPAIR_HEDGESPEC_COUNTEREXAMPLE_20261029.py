"""Exact finite calculation of the printed v1 Theorem 3 estimator, not GPU reproduction."""
from fractions import Fraction as F

p_first = {'A': F(1, 2), 'B': F(1, 2)}
q_first = {'A': F(9, 10), 'B': F(1, 10)}
p_second = {'A': {'C': F(1, 2), 'D': F(1, 2)}, 'B': {'C': F(9, 10), 'D': F(1, 10)}}
q_second = {'A': {'C': F(1, 2), 'D': F(1, 2)}, 'B': {'C': F(1, 10), 'D': F(9, 10)}}
gamma_first = sum(min(p_first[x], q_first[x]) for x in p_first)
gamma_second = {x: sum(min(p_second[x][y], q_second[x][y]) for y in p_second[x]) for x in p_first}
both_accepted = sum(min(p_first[x], q_first[x]) * gamma_second[x] for x in p_first)
actual = 1 + gamma_first + both_accepted
printed_estimator_mean = sum(p_first[x] * (1 + gamma_first + gamma_first * gamma_second[x]) for x in p_first)
assert actual == F(53, 25)
assert printed_estimator_mean == F(49, 25)
assert actual != printed_estimator_mean
print('gamma1:', gamma_first, 'gamma2:', gamma_second)
print('actual expected output length including correction/bonus:', actual, float(actual))
print('mean printed estimator over target trajectories:', printed_estimator_mean, float(printed_estimator_mean))
print('difference:', actual - printed_estimator_mean)
