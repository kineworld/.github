"""Exact state-aliasing demonstration; no training, network, or file writes."""
import json

from tiny_world import step


def demonstrate():
    cases = []
    for velocity in (-1.0, 1.0):
        current = 0.0
        previous = current - velocity
        target = step((current, velocity), 0.0)[0]
        recovered_velocity = current - previous
        history_prediction = step((current, recovered_velocity), 0.0)[0]
        cases.append({
            'previous_position': previous,
            'current_position': current,
            'action': 0.0,
            'target_next_position': target,
            'history_prediction': history_prediction,
        })
    best_point = sum(c['target_next_position'] for c in cases) / len(cases)
    return {
        'kind': 'educational_constructed_counterexample_not_model_benchmark',
        'cases': cases,
        'best_single_observation_point_prediction': best_point,
        'single_observation_mse': sum(
            (best_point - c['target_next_position']) ** 2 for c in cases
        ) / len(cases),
        'history_mse': sum(
            (c['history_prediction'] - c['target_next_position']) ** 2
            for c in cases
        ) / len(cases),
        'assumptions': [
            'Two equally weighted cases; exact positions and unit time step.',
            'Known simulator coefficients and position update; no parameter learning.',
            'Two frames are sufficient here, not in arbitrary real-world video.',
        ],
    }


if __name__ == '__main__':
    print(json.dumps(demonstrate(), indent=2, allow_nan=False))
