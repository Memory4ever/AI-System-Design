import assert from 'node:assert/strict';
import { scorerTrace, mechanismFrames, mechanismNames } from './mechanisms.mjs';

assert.deepEqual(Object.keys(mechanismNames),['sampling','credit','rm','dpo','repair']);
for(const id of ['clip','groups','weights','truncation'])assert.throws(()=>mechanismFrames(id),/Unknown mechanism/);
const scores=scorerTrace();
assert.ok(scores.at(-1).loss<scores[0].loss);
assert.ok(scores.at(-1).preferredProbability>.5);
assert.ok(scores.at(-1).short>scores.at(-1).long);
for(const id of Object.keys(mechanismNames)) {
  const frames=mechanismFrames(id);
  assert.ok(frames.length>=3,id);
  for(const frame of frames) {
    assert.ok(frame.title && frame.caption && frame.boundary,id);
    assert.ok(frame.move>=0 && frame.move<=frame.path.steps.length,id);
    assert.ok(frame.rows.every(row=>row.length===3),id);
    assert.ok(!JSON.stringify(frame).includes('NaN'),id);
  }
}
const credit=mechanismFrames('credit');
assert.deepEqual(credit.at(-1).returns.map(n=>Number(n.toFixed(2))),[.92,.94,.96,.98]);
const sampling=mechanismFrames('sampling');
assert.equal(sampling[0].version,0);assert.equal(sampling.at(-2).version,0);assert.equal(sampling.at(-1).version,1);
assert.deepEqual(sampling.at(-1).path.steps.map(s=>s.a),sampling[0].path.steps.map(s=>s.a));
assert.notDeepEqual(sampling.at(-1).probabilities,sampling.at(-2).probabilities);
const dpo=mechanismFrames('dpo');
assert.ok(dpo.at(-1).loss<dpo[0].loss);assert.ok(dpo.at(-1).success<dpo[0].success);
const repair=mechanismFrames('repair');
assert.equal(repair[1].fingerprint,repair[2].fingerprint,'editing a reward cannot undo parameters');
assert.equal(repair[0].fingerprint,repair.at(-1).fingerprint,'full restore returns this toy to its initial state');
console.log('Mechanism calculations and animation state contracts passed');
