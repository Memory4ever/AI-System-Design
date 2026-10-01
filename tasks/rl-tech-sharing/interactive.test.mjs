import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { expectedStep, sampledStep, groupStats, groupCases, clippedTerm } from './interactive.mjs';

const near = (a, b, tolerance = 1e-10) => assert.ok(Math.abs(a - b) < tolerance, `${a} != ${b}`);
const expected = expectedStep([0, 0, 0, 0], [1, 1, 0, 0], 0.2);
assert.deepEqual(expected.gradient, [0.125, 0.125, -0.125, -0.125]);
near(expected.after[0] + expected.after[1], 0.5124973964842103);
const recorded = JSON.parse(readFileSync(new URL('./examples/results.json', import.meta.url)));
expected.after.forEach((p, i) => near(p, recorded.correct_reward_exact[1].probabilities[i]));
const sampled = sampledStep([0, 0, 0, 0], 0, 1, 0.2);
assert.deepEqual(sampled.gradient, [0.75, -0.25, -0.25, -0.25]);
assert.deepEqual(sampledStep([0, 0, 0, 0], 0, 0, 0.2).after, [.25, .25, .25, .25]);
near(sampled.after.reduce((a, b) => a + b), 1);
const stats = groupStats([1, 1, 0, 0]);
near(stats.mean, 0.5); near(stats.std, 0.5);
stats.advantage.forEach((a, i) => near(a, i < 2 ? 1 : -1, 1e-7));
assert.deepEqual(groupStats([1, 1, 1, 1]).advantage, [0, 0, 0, 0]);
for (const key of ['mixed', 'all-one', 'all-zero']) {
  const {answerIds, rewards} = groupCases[key];
  assert.deepEqual(rewards, answerIds.map(id => id < 2 ? 1 : 0), `${key} must score the displayed answers correctly`);
}
assert.deepEqual(groupCases.wrong.answerIds, groupCases.mixed.answerIds);
assert.equal(groupCases.wrong.rewards.filter((r, i) => r !== groupCases.mixed.rewards[i]).length, 1);
const wrong = groupStats([1, 0, 0, 0]);
near(wrong.advantage[0], Math.sqrt(3), 1e-7);
near(wrong.advantage[1], -1 / Math.sqrt(3), 1e-7);
near(clippedTerm(1.5, 1), 1.2);
near(clippedTerm(0.5, -1), -0.8);
near(clippedTerm(0.5, 1), 0.5);
near(clippedTerm(1.5, -1), -1.5);
assert.equal(recorded.dpo.chosen, 'B');
assert.equal(recorded.dpo.rejected, 'A');
near(recorded.dpo.example_policy[0] + recorded.dpo.example_policy[1], 0.5);
// A relative preference can improve while both successful candidates lose probability.
const pairLoss=(chosen,rejected)=>Math.log1p(Math.exp(-.1*Math.log(chosen/rejected)));
assert.ok(pairLoss(.3,.05)<pairLoss(.4,.2));
assert.ok(.3+.05<.4+.2);
console.log('Animation math agrees with the CPU example; sample, group and clipping checks passed.');
