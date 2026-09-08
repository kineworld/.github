"""CPU-only educational system identification + MPC. Python standard library.

No neural network, image input, download, or company benchmark claim.
Run from any directory: python tiny_world.py --seed 7
"""
import argparse
import itertools
import json
import math
import random
import statistics


def step(state, action, damping=0.9, gain=0.2):
    x, velocity = state
    next_v = damping * velocity + gain * action
    return x + next_v, next_v


def collect(seed, episodes=40, length=25):
    rng = random.Random(seed)
    rows = []
    for _ in range(episodes):
        state = (rng.uniform(-2, 2), rng.uniform(-1, 1))
        for _ in range(length):
            action = rng.uniform(-1, 1)
            target = step(state, action)
            rows.append((state[1], action, target[1]))
            state = target
    return rows


def fit(rows):
    # Solve the 2x2 least-squares normal equations for v_next = d*v + g*a.
    vv = sum(v * v for v, a, y in rows)
    aa = sum(a * a for v, a, y in rows)
    va = sum(v * a for v, a, y in rows)
    vy = sum(v * y for v, a, y in rows)
    ay = sum(a * y for v, a, y in rows)
    det = vv * aa - va * va
    if abs(det) < 1e-12:
        raise ValueError('Insufficiently varied data to identify both coefficients')
    return (vy * aa - ay * va) / det, (ay * vv - vy * va) / det


def prediction_errors(model, seed, test_damping):
    rng = random.Random(seed)
    errors = {1: [], 5: [], 20: []}
    baseline = []
    for _ in range(100):
        real = (rng.uniform(-2, 2), rng.uniform(-1, 1))
        predicted = real
        for horizon in range(1, 21):
            action = rng.uniform(-1, 1)
            old = real
            real = step(real, action, test_damping)
            predicted = step(predicted, action, *model)
            if horizon == 1:
                baseline.append(sum((real[i] - old[i]) ** 2 for i in (0, 1)) / 2)
            if horizon in errors:
                errors[horizon].append(sum((real[i] - predicted[i]) ** 2 for i in (0, 1)) / 2)
    return {'state_mse': {str(k): statistics.mean(v) for k, v in errors.items()},
            'one_step_persistence_mse': statistics.mean(baseline), 'independent_starts': 100}


def plan(state, model, horizon=4):
    best = (math.inf, 0)
    for actions in itertools.product((-1, 0, 1), repeat=horizon):
        imagined, cost = state, 0
        for action in actions:
            imagined = step(imagined, action, *model)
            cost += imagined[0] ** 2 + 0.1 * imagined[1] ** 2 + 0.01 * action ** 2
        if cost < best[0]:
            best = cost, actions[0]
    return best[1]


def control(model, seed, test_damping, episodes=20):
    rng = random.Random(seed)
    starts = [(rng.choice((-1, 1)) * rng.uniform(1, 2), rng.uniform(-0.2, 0.2)) for _ in range(episodes)]
    results = {}
    for name in ('zero_action', 'learned_mpc', 'oracle_mpc'):
        costs, distances, successes = [], [], 0
        for start in starts:
            state, cost = start, 0
            for _ in range(30):
                action = 0 if name == 'zero_action' else plan(state, model if name == 'learned_mpc' else (test_damping, 0.2))
                state = step(state, action, test_damping)
                cost += state[0] ** 2 + 0.1 * state[1] ** 2 + 0.01 * action ** 2
            costs.append(cost)
            distances.append(abs(state[0]))
            successes += abs(state[0]) < 0.25 and abs(state[1]) < 0.15
        results[name] = {'mean_cost': statistics.mean(costs), 'mean_final_distance': statistics.mean(distances),
                         'successes': successes, 'episodes': episodes}
    return results


def run(seed=7, test_damping=0.5):
    if not math.isfinite(test_damping) or not 0 <= test_damping <= 1:
        raise ValueError('test_damping must be finite and between 0 and 1')
    model = fit(collect(seed))
    return {'kind': 'educational_synthetic_experiment_not_product_evidence', 'seed': seed,
            'training': {'damping': 0.9, 'gain': 0.2, 'episodes': 40, 'transitions': 1000},
            'learned': {'damping': model[0], 'gain': model[1]},
            'in_distribution': prediction_errors(model, seed + 1000, 0.9),
            'shifted': {'test_damping': test_damping, **prediction_errors(model, seed + 1000, test_damping)},
            'control_shifted': control(model, seed + 2000, test_damping),
            'limits': ['fully observed linear noiseless simulator', 'structure and position update are supplied',
                       'no visual encoder or hidden-state learning', 'oracle knows test physics',
                       'fixed short-horizon planner, not optimal control', 'single seed is not a research conclusion']}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seed', type=int, default=7)
    parser.add_argument('--test-damping', type=float, default=0.5)
    args = parser.parse_args()
    print(json.dumps(run(args.seed, args.test_damping), indent=2, allow_nan=False))
