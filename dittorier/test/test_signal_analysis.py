__author__ = 'alberto'

import unittest

from dittorier.signal.fourier import basic_operations


class TestSelectors(unittest.TestCase):
    def setUp(self):
        # Test signals
        self.signal_a = [1, 2, 3, 4, 5]
        self.signal_b = [0.4, 0.4, 0.2, 0.4]
        # Interpolated signal a by factor of 2 and step function
        self.interpolated_signal_a_by_step = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        # Interpolated signal a by factor of 2 and zero function
        self.interpolated_signal_a_by_zero = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
        # Decimated signal a by factor of 2
        self.decimated_signal_a_by_two = [1, 3, 5]

    def test_operation_interpolate_zero(self):
        self.assertEqual(basic_operations.interpolate(self.signal_a, 2, filter='zero'),
                         self.interpolated_signal_a_by_zero)

    def test_operation_interpolate_step(self):
        self.assertEqual(basic_operations.interpolate(self.signal_a, 2, filter='step'),
                         self.interpolated_signal_a_by_step)

    def test_operation_decimate(self):
        self.assertEqual(basic_operations.decimate(self.signal_a, 2), self.decimated_signal_a_by_two)