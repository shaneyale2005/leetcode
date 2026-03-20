import unittest
import random
from collections import Counter

from sort import bubble_sort, selection_sort, insertion_sort, shell_sort, merge_sort

random.seed(42)


class TestSorting(unittest.TestCase):
    def assert_sorted(self, actual, expected, input_data):
        if len(actual) != len(expected):
            self.fail(
                f"Length mismatch: actual={len(actual)}, expected={len(expected)}, input={input_data}"
            )

        for i, (a, e) in enumerate(zip(actual, expected)):
            if isinstance(a, float) or isinstance(e, float):
                self.assertAlmostEqual(
                    a,
                    e,
                    places=10,
                    msg=f"Index {i} value mismatch: actual={a}, expected={e}, input={input_data}",
                )
            else:
                self.assertEqual(
                    a,
                    e,
                    msg=f"Index {i} value mismatch: actual={a}, expected={e}, input={input_data}",
                )

    def check_sort(self, sort_func, test_inputs):
        for i, nums in enumerate(test_inputs):
            with self.subTest(case_index=i, input=nums):
                data = nums.copy()
                expected = sorted(nums)
                sort_func(data)
                self.assert_sorted(data, expected, nums)

    # ==================== Boundary Cases ====================

    def test_empty_and_single_element(self):
        test_inputs = [
            [],
            [1],
            [0],
            [-1],
            [0.0],
            [float("inf")],
        ]
        self.check_sort(bubble_sort, test_inputs)

    def test_two_elements(self):
        test_inputs = [
            [1, 2],
            [2, 1],
            [1, 1],
            [0, 0],
            [-1, 1],
            [1, -1],
        ]
        self.check_sort(bubble_sort, test_inputs)

    # ==================== Positive Numbers ====================

    def test_positive_sorted(self):
        test_inputs = [
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            list(range(20)),
        ]
        self.check_sort(bubble_sort, test_inputs)

    def test_positive_reverse(self):
        test_inputs = [
            [5, 4, 3, 2, 1],
            [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
            list(range(20, 0, -1)),
        ]
        self.check_sort(bubble_sort, test_inputs)

    def test_positive_unsorted(self):
        test_inputs = [
            [1, 3, 2],
            [100, 1, 50],
            [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],
            [1, 3, 5, 2, 4, 6],
            [1, 10, 2, 9, 3, 8],
            [1, 2, 4, 8, 16, 32],
        ]
        self.check_sort(bubble_sort, test_inputs)

    # ==================== Negative Numbers ====================

    def test_negative_sorted(self):
        test_inputs = [
            [-3, -2, -1],
            [-10, -9, -8, -7, -6],
        ]
        self.check_sort(bubble_sort, test_inputs)

    def test_negative_reverse(self):
        test_inputs = [
            [-1, -2, -3],
            [-6, -7, -8, -9, -10],
            [-100, -200, -1],
        ]
        self.check_sort(bubble_sort, test_inputs)

    def test_mixed_sign(self):
        test_inputs = [
            [-1, 0, 1],
            [1, 0, -1],
            [-5, 5, 0],
            [0, -1, -5, 2, 4],
            [10, -10, 5, -5],
            [0, 0, -1, 1],
            [-1, -1, 2, 2],
            [1000, 0, -1000],
        ]
        self.check_sort(bubble_sort, test_inputs)

    # ==================== Duplicates ====================

    def test_duplicates(self):
        test_inputs = [
            [1, 1, 1, 1, 1],
            [1, 2, 1],
            [2, 1, 1],
            [1, 1, 2],
            [3, 3, 1, 1, 2, 2],
            [1, 2, 3, 1, 2, 3],
            [0, 0, 0, 1, 0],
            [5, 2, 9, 1, 5, 6],
            [1, 0, 0, 0, 1],
            [21, 12, 21, 12],
        ]
        self.check_sort(bubble_sort, test_inputs)

    def test_all_same(self):
        test_inputs = [
            [5, 5, 5, 5, 5, 5, 5],
            [0, 0, 0, 0, 0],
            [-1, -1, -1, -1],
            [100, 100, 100],
        ]
        self.check_sort(bubble_sort, test_inputs)

    # ==================== Floating Point ====================

    def test_floats(self):
        test_inputs = [
            [0.5, 0.2, 0.8],
            [1.1, 1.01, 1.001],
            [-0.5, 0.5, 0.0],
            [3.14, 2.71, 1.41],
            [10.0, 10, 9.9],
            [0.1 + 0.2, 0.3],
        ]
        self.check_sort(bubble_sort, test_inputs)

    def test_mixed_int_float(self):
        test_inputs = [
            [1, 2.5, 3],
            [1.5, 2, 2.5],
            [0, 0.1, 0.2, 1, 1.1],
        ]
        self.check_sort(bubble_sort, test_inputs)

    # ==================== Extreme Values ====================

    def test_extreme_values(self):
        test_inputs = [
            [1, -1, 0, 1000000, -1000000],
            [2**31 - 1, -(2**31), 0],
            [float("inf"), 1, -1, float("-inf")],
            [1e10, -1e10, 0, 1e-10],
        ]
        self.check_sort(bubble_sort, test_inputs)

    # ==================== Random Arrays ====================

    def test_random_small(self):
        test_inputs = [
            [random.randint(-50, 50) for _ in range(10)],
            [random.randint(-50, 50) for _ in range(15)],
            [random.randint(-50, 50) for _ in range(20)],
        ]
        self.check_sort(bubble_sort, test_inputs)

    def test_random_binary(self):
        test_inputs = [
            [random.randint(0, 1) for _ in range(20)],
            [random.randint(0, 1) for _ in range(30)],
        ]
        self.check_sort(bubble_sort, test_inputs)

    def test_random_positive(self):
        test_inputs = [
            [random.randint(1, 1000) for _ in range(8)],
            [random.randint(1, 100) for _ in range(15)],
        ]
        self.check_sort(bubble_sort, test_inputs)

    def test_random_large(self):
        test_inputs = [
            [random.randint(-1000, 1000) for _ in range(50)],
            [random.randint(-100, 100) for _ in range(100)],
        ]
        self.check_sort(bubble_sort, test_inputs)

    # ==================== Special Patterns ====================

    def test_alternating(self):
        test_inputs = [
            [1, -1, 1, -1, 1, -1],
            [1, 0, 1, 0, 1, 0],
            [10, 1, 10, 1, 10, 1],
        ]
        self.check_sort(bubble_sort, test_inputs)

    def test_nearly_sorted(self):
        test_inputs = [
            [1, 2, 3, 4, 6, 5],
            [1, 2, 4, 3, 5, 6],
            [2, 1, 3, 4, 5, 6],
        ]
        self.check_sort(bubble_sort, test_inputs)

    def test_nearly_reverse(self):
        test_inputs = [
            [5, 4, 3, 2, 1, 6],
            [6, 5, 4, 3, 1, 2],
        ]
        self.check_sort(bubble_sort, test_inputs)

    # ==================== In-Place Modification ====================

    def test_in_place_modification(self):
        original = [3, 1, 4, 1, 5, 9, 2, 6]
        data = original.copy()
        bubble_sort(data)
        self.assertEqual(data, sorted(original))


class TestSelectionSort(unittest.TestCase):
    def assert_sorted(self, actual, expected, input_data):
        if len(actual) != len(expected):
            self.fail(
                f"Length mismatch: actual={len(actual)}, expected={len(expected)}, input={input_data}"
            )

        for i, (a, e) in enumerate(zip(actual, expected)):
            if isinstance(a, float) or isinstance(e, float):
                self.assertAlmostEqual(
                    a,
                    e,
                    places=10,
                    msg=f"Index {i} value mismatch: actual={a}, expected={e}, input={input_data}",
                )
            else:
                self.assertEqual(
                    a,
                    e,
                    msg=f"Index {i} value mismatch: actual={a}, expected={e}, input={input_data}",
                )

    def check_sort(self, sort_func, test_inputs):
        for i, nums in enumerate(test_inputs):
            with self.subTest(case_index=i, input=nums):
                data = nums.copy()
                expected = sorted(nums)
                sort_func(data)
                self.assert_sorted(data, expected, nums)

    # ==================== Boundary Cases ====================

    def test_empty_and_single_element(self):
        test_inputs = [
            [],
            [1],
            [0],
            [-1],
            [0.0],
            [float("inf")],
        ]
        self.check_sort(selection_sort, test_inputs)

    def test_two_elements(self):
        test_inputs = [
            [1, 2],
            [2, 1],
            [1, 1],
            [0, 0],
            [-1, 1],
            [1, -1],
        ]
        self.check_sort(selection_sort, test_inputs)

    # ==================== Positive Numbers ====================

    def test_positive_sorted(self):
        test_inputs = [
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            list(range(20)),
        ]
        self.check_sort(selection_sort, test_inputs)

    def test_positive_reverse(self):
        test_inputs = [
            [5, 4, 3, 2, 1],
            [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
            list(range(20, 0, -1)),
        ]
        self.check_sort(selection_sort, test_inputs)

    def test_positive_unsorted(self):
        test_inputs = [
            [1, 3, 2],
            [100, 1, 50],
            [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],
            [1, 3, 5, 2, 4, 6],
            [1, 10, 2, 9, 3, 8],
            [1, 2, 4, 8, 16, 32],
        ]
        self.check_sort(selection_sort, test_inputs)

    # ==================== Negative Numbers ====================

    def test_negative_sorted(self):
        test_inputs = [
            [-3, -2, -1],
            [-10, -9, -8, -7, -6],
        ]
        self.check_sort(selection_sort, test_inputs)

    def test_negative_reverse(self):
        test_inputs = [
            [-1, -2, -3],
            [-6, -7, -8, -9, -10],
            [-100, -200, -1],
        ]
        self.check_sort(selection_sort, test_inputs)

    def test_mixed_sign(self):
        test_inputs = [
            [-1, 0, 1],
            [1, 0, -1],
            [-5, 5, 0],
            [0, -1, -5, 2, 4],
            [10, -10, 5, -5],
            [0, 0, -1, 1],
            [-1, -1, 2, 2],
            [1000, 0, -1000],
        ]
        self.check_sort(selection_sort, test_inputs)

    # ==================== Duplicates ====================

    def test_duplicates(self):
        test_inputs = [
            [1, 1, 1, 1, 1],
            [1, 2, 1],
            [2, 1, 1],
            [1, 1, 2],
            [3, 3, 1, 1, 2, 2],
            [1, 2, 3, 1, 2, 3],
            [0, 0, 0, 1, 0],
            [5, 2, 9, 1, 5, 6],
            [1, 0, 0, 0, 1],
            [21, 12, 21, 12],
        ]
        self.check_sort(selection_sort, test_inputs)

    def test_all_same(self):
        test_inputs = [
            [5, 5, 5, 5, 5, 5, 5],
            [0, 0, 0, 0, 0],
            [-1, -1, -1, -1],
            [100, 100, 100],
        ]
        self.check_sort(selection_sort, test_inputs)

    # ==================== Floating Point ====================

    def test_floats(self):
        test_inputs = [
            [0.5, 0.2, 0.8],
            [1.1, 1.01, 1.001],
            [-0.5, 0.5, 0.0],
            [3.14, 2.71, 1.41],
            [10.0, 10, 9.9],
            [0.1 + 0.2, 0.3],
        ]
        self.check_sort(selection_sort, test_inputs)

    def test_mixed_int_float(self):
        test_inputs = [
            [1, 2.5, 3],
            [1.5, 2, 2.5],
            [0, 0.1, 0.2, 1, 1.1],
        ]
        self.check_sort(selection_sort, test_inputs)

    # ==================== Extreme Values ====================

    def test_extreme_values(self):
        test_inputs = [
            [1, -1, 0, 1000000, -1000000],
            [2**31 - 1, -(2**31), 0],
            [float("inf"), 1, -1, float("-inf")],
            [1e10, -1e10, 0, 1e-10],
        ]
        self.check_sort(selection_sort, test_inputs)

    # ==================== Random Arrays ====================

    def test_random_small(self):
        test_inputs = [
            [random.randint(-50, 50) for _ in range(10)],
            [random.randint(-50, 50) for _ in range(15)],
            [random.randint(-50, 50) for _ in range(20)],
        ]
        self.check_sort(selection_sort, test_inputs)

    def test_random_binary(self):
        test_inputs = [
            [random.randint(0, 1) for _ in range(20)],
            [random.randint(0, 1) for _ in range(30)],
        ]
        self.check_sort(selection_sort, test_inputs)

    def test_random_positive(self):
        test_inputs = [
            [random.randint(1, 1000) for _ in range(8)],
            [random.randint(1, 100) for _ in range(15)],
        ]
        self.check_sort(selection_sort, test_inputs)

    def test_random_large(self):
        test_inputs = [
            [random.randint(-1000, 1000) for _ in range(50)],
            [random.randint(-100, 100) for _ in range(100)],
        ]
        self.check_sort(selection_sort, test_inputs)

    # ==================== Special Patterns ====================

    def test_alternating(self):
        test_inputs = [
            [1, -1, 1, -1, 1, -1],
            [1, 0, 1, 0, 1, 0],
            [10, 1, 10, 1, 10, 1],
        ]
        self.check_sort(selection_sort, test_inputs)

    def test_nearly_sorted(self):
        test_inputs = [
            [1, 2, 3, 4, 6, 5],
            [1, 2, 4, 3, 5, 6],
            [2, 1, 3, 4, 5, 6],
        ]
        self.check_sort(selection_sort, test_inputs)

    def test_nearly_reverse(self):
        test_inputs = [
            [5, 4, 3, 2, 1, 6],
            [6, 5, 4, 3, 1, 2],
        ]
        self.check_sort(selection_sort, test_inputs)

    # ==================== In-Place Modification ====================

    def test_in_place_modification(self):
        original = [3, 1, 4, 1, 5, 9, 2, 6]
        data = original.copy()
        selection_sort(data)
        self.assertEqual(data, sorted(original))


class TestInsertionSort(unittest.TestCase):
    def assert_matches_python_sort(self, nums):
        data = nums.copy()
        expected = sorted(nums)
        insertion_sort(data)
        self.assertEqual(data, expected, msg=f"input={nums}")

    def test_boundary_and_pattern_cases(self):
        test_inputs = [
            [],
            [42],
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
            [3, -1, 2, -1, 3, 0, 2, -5],
            [0, (2**31) - 1, -1, -(2**31), 42, (2**31) - 1, -(2**31)],
        ]
        for case in test_inputs:
            with self.subTest(input=case):
                self.assert_matches_python_sort(case)

    def test_preserves_multiset(self):
        nums = [5, 1, 5, 2, 9, 2, 2, -7, -7, 0]
        before = Counter(nums)
        insertion_sort(nums)
        after = Counter(nums)
        self.assertEqual(before, after)
        self.assertEqual(nums, sorted(nums))

    def test_idempotent(self):
        nums = [4, 1, 3, 2, 3, 1, 0, -2]
        insertion_sort(nums)
        once_sorted = nums.copy()
        insertion_sort(nums)
        self.assertEqual(nums, once_sorted)

    def test_randomized_against_builtin_sorted(self):
        rng = random.Random(123456789)
        for case_id in range(300):
            size = rng.randint(0, 128)
            nums = [rng.randint(-1000, 1000) for _ in range(size)]
            with self.subTest(case_id=case_id):
                self.assert_matches_python_sort(nums)


class TestShellSort(unittest.TestCase):
    def assert_matches_python_sort(self, nums):
        data = nums.copy()
        expected = sorted(nums)
        shell_sort(data)
        self.assertEqual(data, expected, msg=f"input={nums}")

    def test_boundary_and_pattern_cases(self):
        test_inputs = [
            [],
            [42],
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
            [3, -1, 2, -1, 3, 0, 2, -5],
            [0, (2**31) - 1, -1, -(2**31), 42, (2**31) - 1, -(2**31)],
        ]
        for case in test_inputs:
            with self.subTest(input=case):
                self.assert_matches_python_sort(case)

    def test_preserves_multiset(self):
        nums = [5, 1, 5, 2, 9, 2, 2, -7, -7, 0]
        before = Counter(nums)
        shell_sort(nums)
        after = Counter(nums)
        self.assertEqual(before, after)
        self.assertEqual(nums, sorted(nums))

    def test_idempotent(self):
        nums = [4, 1, 3, 2, 3, 1, 0, -2]
        shell_sort(nums)
        once_sorted = nums.copy()
        shell_sort(nums)
        self.assertEqual(nums, once_sorted)

    def test_randomized_against_builtin_sorted(self):
        rng = random.Random(987654321)
        for case_id in range(300):
            size = rng.randint(0, 128)
            nums = [rng.randint(-1000, 1000) for _ in range(size)]
            with self.subTest(case_id=case_id):
                self.assert_matches_python_sort(nums)


class TestMergeSort(unittest.TestCase):
    def assert_matches_python_sort(self, nums):
        input_data = nums.copy()
        result = merge_sort(input_data)
        expected = sorted(nums)
        self.assertEqual(result, expected, msg=f"input={nums}")

    def test_boundary_and_pattern_cases(self):
        test_inputs = [
            [],
            [42],
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
            [3, -1, 2, -1, 3, 0, 2, -5],
            [0, (2**31) - 1, -1, -(2**31), 42, (2**31) - 1, -(2**31)],
        ]
        for case in test_inputs:
            with self.subTest(input=case):
                self.assert_matches_python_sort(case)

    def test_preserves_multiset(self):
        nums = [5, 1, 5, 2, 9, 2, 2, -7, -7, 0]
        result = merge_sort(nums.copy())
        self.assertEqual(Counter(nums), Counter(result))
        self.assertEqual(result, sorted(nums))

    def test_idempotent(self):
        nums = [4, 1, 3, 2, 3, 1, 0, -2]
        once_sorted = merge_sort(nums.copy())
        twice_sorted = merge_sort(once_sorted.copy())
        self.assertEqual(twice_sorted, once_sorted)

    def test_does_not_modify_input(self):
        nums = [9, 4, 1, 7, 3]
        original = nums.copy()
        _ = merge_sort(nums)
        self.assertEqual(nums, original)

    def test_randomized_against_builtin_sorted(self):
        rng = random.Random(42424242)
        for case_id in range(300):
            size = rng.randint(0, 128)
            nums = [rng.randint(-1000, 1000) for _ in range(size)]
            with self.subTest(case_id=case_id):
                self.assert_matches_python_sort(nums)


if __name__ == "__main__":
    unittest.main(verbosity=2)
