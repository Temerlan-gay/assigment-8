import unittest
from hw_bonus import *


class TestBonus(unittest.TestCase):

    def test_longest_consecutive(self):
        self.assertEqual(longest_consecutive([100, 4, 200, 1, 3, 2]), 4)

    def test_find_missing(self):
        self.assertEqual(find_missing([1, 2, 4]), 3)

    def test_find_duplicate(self):
        self.assertEqual(find_duplicate([1, 3, 4, 2, 2]), 2)

    def test_group_anagrams(self):
        self.assertIn(["bat"], group_anagrams(["bat"]))


if __name__ == "__main__":
    unittest.main()