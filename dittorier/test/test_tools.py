__author__ = 'alberto'

import unittest

from dittorier.tools import utils


class TestTools(unittest.TestCase):
    def setUp(self):
        # Test signals
        self.signal_a = [1, 2, 3, 4, 5]
        # Signal split in pieces of 2
        self.signal_a_split_pieces_2 = [[1, 2], [3, 4], [5]]
        """
        Signal split in pieces of 2 with index
        Considering the next case:
        new_array = Array('i',6)
        [1,2,3,4,5,6] => [[0,1,2],[2,3,4],[4,5,6]]
        This will be useful for using multiprocessing pool
        and working with larger signals and then joining all the work.
        """
        self.signal_a_split_pieces_2_with_index = [[0, 1, 2], [2, 3, 4], [4, 5]]

    def test_operation_interpolate_zero(self):
        self.assertEqual(utils.chunks(self.signal_a, 2),
                         self.signal_a_split_pieces_2)

    def test_operation_interpolate_step(self):
        self.assertEqual(utils.chunks_with_index(self.signal_a, 2),
                         self.signal_a_split_pieces_2_with_index)

    def test_will_fail(self):
        self.assertEqual(True, True)