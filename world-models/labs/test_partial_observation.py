import unittest

from partial_observation import demonstrate
from tiny_world import step


class PartialObservationTests(unittest.TestCase):
    def test_same_observation_different_future(self):
        left, right = demonstrate()['cases']
        self.assertEqual(left['current_position'], right['current_position'])
        self.assertEqual(left['action'], right['action'])
        self.assertNotEqual(left['target_next_position'], right['target_next_position'])

    def test_point_prediction_lower_bound(self):
        result = demonstrate()
        self.assertEqual(result['best_single_observation_point_prediction'], 0)
        self.assertAlmostEqual(result['single_observation_mse'], 0.81)
        self.assertEqual(result['history_mse'], 0)

    def test_worked_rollout(self):
        first = step((1, 0), -1)
        second = step(first, -1)
        self.assertAlmostEqual(second[0], 0.42)
        self.assertAlmostEqual(second[1], -0.38)
        self.assertAlmostEqual(step(first, 0)[0], 0.62)

    def test_worked_shift_error(self):
        prediction = step(step((0, 1), 0), 0)
        truth = step(step((0, 1), 0, damping=0.5), 0, damping=0.5)
        mse = sum((p - t) ** 2 for p, t in zip(prediction, truth)) / 2
        self.assertAlmostEqual(mse, 0.6176)


if __name__ == '__main__':
    unittest.main()
