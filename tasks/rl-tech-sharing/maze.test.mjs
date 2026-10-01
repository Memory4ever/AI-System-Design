import assert from 'node:assert/strict';
import { MazeTrainer, maze, route, policy, evaluate, objective, groupAdvantages, mazeScene } from './maze.mjs';

const near = (a, b, eps = 1e-6) => assert.ok(Math.abs(a-b) < eps, `${a} != ${b}`);
const initial = new MazeTrainer('ppo');
const short = route('RRRR');
const long = route('DDRRRRUU');
const demoScene=mazeScene(short,0,-1,short);
assert.equal((demoScene.match(/data-demo-step=/g)||[]).length,4,'all demonstration steps must exist before playback');
assert.ok(demoScene.includes('给定示范'));
assert.ok(demoScene.includes('data-demo-route'));
assert.ok(!mazeScene(short,0).includes('data-demo-route'),'other modes and evaluation have no demonstration overlay');
assert.equal(short.success, true);
assert.equal(long.success, true);
assert.throws(() => route('U'), /wall/);
near(short.total, .92);
near(long.total, .84);
short.steps.forEach((step,i)=>near(step.returns,[.92,.94,.96,.98][i]));
assert.deepEqual(groupAdvantages([1,1,1,1]), [0,0,0,0]);
for (const s of maze.cells) near(policy(initial.logits, s).reduce((a,b)=>a+b), 1);
assert.ok(evaluate(initial.logits).success > 0);
assert.ok(evaluate(initial.logits).success < 1);

// Analytical gradients are checked independently against the loss, not against animation output.
for (const mode of ['sft','ppo','grpo','dpo']) {
  const trainer = new MazeTrainer(mode);
  const batch = trainer.prepare();
  const {loss, gradient} = objective(trainer.logits, batch);
  assert.ok(Number.isFinite(loss));
  for (const s of maze.cells) for (let a=0;a<4;a++) {
    const old=trainer.logits[s][a], h=1e-5;
    trainer.logits[s][a]=old+h;const plus=objective(trainer.logits,batch).loss;
    trainer.logits[s][a]=old-h;const minus=objective(trainer.logits,batch).loss;
    trainer.logits[s][a]=old;
    near((plus-minus)/(2*h), gradient[s][a]);
  }
  const before=JSON.stringify(trainer.logits);
  trainer.update(batch);
  assert.notEqual(JSON.stringify(trainer.logits),before);
  assert.equal(trainer.history.length,2);
  for(let i=0;i<39;i++) trainer.update(trainer.prepare());
  assert.ok(trainer.history.every(p=>Number.isFinite(p.loss??0) && p.success>=0 && p.success<=1));
  const twin=new MazeTrainer(mode);
  for(let i=0;i<40;i++)twin.update(twin.prepare());
  assert.deepEqual(trainer.history,twin.history,'fixed seeds must reproduce the actual run');
  console.log(mode, trainer.history[0], trainer.history.at(-1));
}

// Reward changes cannot silently change an offline demonstration or preference label.
for (const mode of ['sft','dpo']) {
  const good=new MazeTrainer(mode,'exit'), bad=new MazeTrainer(mode,'steps');
  good.update(good.prepare());bad.update(bad.prepare());
  assert.deepEqual(good.logits,bad.logits);
}
const frozen=new MazeTrainer('ppo');
const snapshot=JSON.stringify(frozen.logits);
const pending=frozen.prepare();
assert.equal(JSON.stringify(frozen.logits),snapshot,'rollout must not update the policy');
assert.equal(frozen.history.length,1);
frozen.update(pending);
assert.throws(()=>frozen.update(pending),/version/,'old batches must not be reused as a new iteration');

// Clipping is a flat objective branch, not a hard clamp on the action probability.
const clipped=new MazeTrainer('ppo'),clipBatch=clipped.prepare();
for(const path of clipBatch.paths)for(const step of path.steps)step.advantage=1;
clipped.logits[maze.start][1]=3;
const check=objective(clipped.logits,clipBatch),h=1e-5;
clipped.logits[maze.start][1]+=h;const plus=objective(clipped.logits,clipBatch).loss;
clipped.logits[maze.start][1]-=2*h;const minus=objective(clipped.logits,clipBatch).loss;
near((plus-minus)/(2*h),check.gradient[maze.start][1]);
for(const mode of ['ppo','grpo']) {
  const bad=new MazeTrainer(mode,'steps');
  for(let i=0;i<40;i++)bad.update(bad.prepare());
  assert.ok(bad.history.at(-1).reward>bad.history[0].reward);
  assert.ok(bad.history.at(-1).success<bad.history[0].success);
}
console.log('Maze: routes, reward, gradients, reproducibility and learning boundaries passed.');
