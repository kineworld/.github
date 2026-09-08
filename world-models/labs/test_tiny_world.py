import unittest
from tiny_world import collect, fit, prediction_errors, run, step


class TinyWorldTests(unittest.TestCase):
    def test_known_transition(self):
        self.assertEqual(step((0, 1), 0), (0.9, 0.9))

    def test_identifies_parameters_across_seeds(self):
        for seed in (0, 7, 42):
            damping, gain = fit(collect(seed))
            self.assertAlmostEqual(damping, 0.9, places=10)
            self.assertAlmostEqual(gain, 0.2, places=10)

    def test_shift_is_not_hidden_by_teacher_forcing(self):
        model = fit(collect(7))
        iid = prediction_errors(model, 1007, 0.9)
        shifted = prediction_errors(model, 1007, 0.5)
        self.assertLess(iid['state_mse']['20'], 1e-20)
        self.assertGreater(shifted['state_mse']['20'], 0.001)

    def test_singular_data_rejected(self):
        with self.assertRaises(ValueError):
            fit([(0, 0, 0)] * 5)

    def test_invalid_physics_rejected(self):
        for damping in (-1, 2, float('nan')):
            with self.assertRaises(ValueError):
                run(test_damping=damping)


if __name__ == '__main__':
    unittest.main()
