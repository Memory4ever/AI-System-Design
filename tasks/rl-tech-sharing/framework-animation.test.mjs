import assert from 'node:assert/strict';
import { frameworkScenes, frameworkFrame, frameworkMarkup } from './framework-animation.mjs';

assert.deepEqual(Object.keys(frameworkScenes), ['shared', 'handoff', 'async']);
for (const [key, scene] of Object.entries(frameworkScenes)) {
  assert.ok(scene.frames.length >= 4);
  scene.frames.forEach((_, index) => {
    const frame = frameworkFrame(key, index);
    assert.equal(frame.lanes.length, 2);
    assert.ok(frame.title && frame.takeaway);
    for (const lane of frame.lanes) {
      assert.equal(lane.nodes.length, 5);
      assert.ok(lane.active >= 0 && lane.active < 5);
      assert.ok(lane.detail);
    }
    assert.ok(frame.ready >= 0 && frame.ready <= 8);
    if (frame.updated) assert.equal(frame.ready, 8, 'never update the fixed eight-answer batch early');
  });
  assert.deepEqual(frameworkFrame(key, -1), frameworkFrame(key, 0));
  assert.deepEqual(frameworkFrame(key, 100), frameworkFrame(key, scene.frames.length - 1));
}
assert.throws(() => frameworkFrame('unknown', 0));
const shared = frameworkScenes.shared.frames;
assert.deepEqual(shared.map(frame => frame.lanes[0].active), [0, 1, 2, 3, 4]);
assert.ok(shared.at(-1).updated);
assert.equal(frameworkScenes.shared.label, '采样与权重');
assert.match(shared[0].lanes[1].detail, /连续批处理/);
assert.match(shared[2].lanes[1].detail, /v7/);
assert.match(shared[3].lanes[1].detail, /暂停/);
assert.match(shared[4].lanes[1].detail, /KV/);
const asyncFrames = frameworkScenes.async.frames;
assert.equal(asyncFrames[1].ready, 8);
assert.equal(asyncFrames[1].updated, false);
assert.match(asyncFrames[1].title, /v8.*没完成/);
assert.match(frameworkScenes.async.batchStates[4][1], /v8.*v9/);
assert.match(frameworkScenes.async.boundary, /verl.*异步/);
assert.match(frameworkScenes.handoff.boundary, /互补/);
const timelines = frameworkScenes.async.timelines;
assert.equal(timelines.length, 2);
for (const rows of timelines) {
  assert.equal(rows.length, 2, 'generation and training have separate resource tracks');
  for (const row of rows) assert.equal(row.cells.length, asyncFrames.length);
  assert.equal(rows[1].cells[0][1], 'wait', 'no training before the fixed batch is complete');
}
assert.deepEqual(timelines[0].map(row => row.cells[1][1]), ['wait', 'train']);
assert.deepEqual(timelines[1].map(row => row.cells[1][1]), ['rollout', 'train']);
assert.match(timelines[1][0].cells[1][0], /第2批 v7/);
assert.match(timelines[0][0].cells[3][0], /第2批 v8/);
assert.match(frameworkFrame('async', 4).title, /v8.*v9/);
assert.match(frameworkFrame('async', 4, 'retry').title, /仍要等/);
assert.match(frameworkFrame('async', 4, 'retry').lanes[1].detail, /不参与第二次更新/);
assert.equal(frameworkScenes.async.retry.trainerCells[4][1], 'wait');
assert.match(frameworkScenes.async.retry.batchStates[4][1], /重.*中/);
for (let index=0; index<3; index++) assert.deepEqual(frameworkFrame('async', index, 'retry'), frameworkFrame('async', index));
assert.doesNotMatch(JSON.stringify(frameworkScenes.async), /A\+B|\bC\b/);
assert.match(frameworkMarkup({}), /role="tablist"/);
assert.match(frameworkMarkup({}), /aria-label="播放"/);
console.log('Framework animation: frame structure, fixed batch, group boundaries and comparison scope pass');
