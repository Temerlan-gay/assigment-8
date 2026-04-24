import unittest
import hw


class TestHW(unittest.TestCase):

    def test_count_unique_elements(self):
        self.assertEqual(hw.count_unique_elements([1, 1, 2, 3]), 3)

    def test_reverse(self):
        self.assertEqual(hw.reverse_list([1, 2, 3]), [3, 2, 1])

    def test_sum(self):
        self.assertEqual(hw.sum_values([1, 2, 3]), 6)


if __name__ == "__main__":
    unittest.main()