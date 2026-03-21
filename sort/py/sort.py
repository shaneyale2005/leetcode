"""
Source code for all kinds of sorting algorithms.
"""

def bubble_sort(nums):
    """
    冒泡排序
    """
    n = len(nums)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

def selection_sort(nums):
    """
    选择排序
    """
    n = len(nums)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j

        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums

def insertion_sort(nums):
    """
    插入排序
    """
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums

def shell_sort(nums):
    """
    希尔排序
    """
    n = len(nums)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = nums[i]
            j = i
            while j >= gap and nums[j - gap] > temp:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = temp
        gap = gap // 2
    return nums

def merge_sort(nums):
    """
    归并排序，核心的思想是分而治之，这里用递归来实现
    """
    n = len(nums)
    if n <= 1:
        return nums
    
    mid = n // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    def merge(left, right):
        res = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
            
        return res + left[i:] + right[j:]

    return merge(left, right)

def quick_sort(nums):
    """
    快速排序
    """
    n = len(nums)
    if n <= 1:
        return nums
    pivot = nums[n // 2]
    left = [x for x in nums if x < pivot]
    middle = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
