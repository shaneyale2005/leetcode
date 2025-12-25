import unittest

# 导入你要测试的排序算法
from bubble_sort import bubble_sort



class TestSorting(unittest.TestCase):

    def check_sort(self, sort_func):
        """通用排序测试"""
        test_cases = [
            ([5, 3, 8, 4, 2], [2, 3, 4, 5, 8]),
            ([], []),
            ([1], [1]),
            ([1, 2, 3, 4], [1, 2, 3, 4]),
            ([4, 3, 2, 1], [1, 2, 3, 4]),
            ([3, 1, 2, 1], [1, 1, 2, 3]),
        ]

        for nums, expected in test_cases:
            data = nums.copy()
            sort_func(data)
            self.assertEqual(data, expected)

    def test_bubble_sort(self):
        self.check_sort(bubble_sort)


if __name__ == "__main__":
    unittest.main()
