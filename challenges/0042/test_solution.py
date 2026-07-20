import unittest
from solution import Solution


class TestTrap(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)

    def test_example_2(self):
        self.assertEqual(self.solution.trap([4, 2, 0, 3, 2, 5]), 9)

    def test_no_water_ascending(self):
        self.assertEqual(self.solution.trap([1, 2, 3, 4, 5]), 0)

    def test_no_water_descending(self):
        self.assertEqual(self.solution.trap([5, 4, 3, 2, 1]), 0)

    def test_flat_ground(self):
        self.assertEqual(self.solution.trap([0, 0, 0, 0]), 0)

    def test_single_bar(self):
        self.assertEqual(self.solution.trap([5]), 0)

    def test_two_bars(self):
        self.assertEqual(self.solution.trap([5, 2]), 0)

    def test_empty(self):
        self.assertEqual(self.solution.trap([]), 0)

    def test_single_valley(self):
        self.assertEqual(self.solution.trap([3, 0, 3]), 3)

    def test_v_shape(self):
        self.assertEqual(self.solution.trap([5, 4, 1, 2]), 1)


if __name__ == "__main__":
    unittest.main()
