# 排序

## 复杂度

| 排序 | 平均时间 | 最坏时间 | 空间复杂度 | 稳定性 |
| --- | --- | --- | --- | --- |
| 冒泡排序 | `O(n^2)` | `O(n^2)` | `O(1)` | 稳定 |
| 选择排序 | `O(n^2)` | `O(n^2)` | `O(1)` | 不稳定 |
| 插入排序 | `O(n^2)` | `O(n^2)` | `O(1)` | 稳定 |
| 希尔排序 | `O(n^1.3)` ~ `O(n^2)` | `O(n^2)` | `O(1)` | 不稳定 |
| 归并排序 | `O(n log n)` | `O(n log n)` | `O(n)` | 稳定 |
| 快速排序 | `O(n log n)` | `O(n^2)` | `O(log n)` | 不稳定 |
| 堆排序 | `O(n log n)` | `O(n log n)` | `O(1)` | 不稳定 |

## 模板

冒泡排序

```python
def bubble_sort(nums):
    nums = nums[:]
    n = len(nums)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums
```

选择排序

```python
def selection_sort(nums):
    nums = nums[:]
    n = len(nums)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums
```

插入排序

```python
def insertion_sort(nums):
    nums = nums[:]
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums
```

希尔排序

```python
def shell_sort(nums):
    nums = nums[:]
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
        gap //= 2
    return nums
```

归并排序

```python
def merge_sort(nums):
    if len(nums) <= 1:
        return nums[:]

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

快速排序

```python
def quick_sort(nums):
    if len(nums) <= 1:
        return nums[:]

    pivot = nums[len(nums) // 2]
    left = [x for x in nums if x < pivot]
    mid = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]

    return quick_sort(left) + mid + quick_sort(right)
```

堆排序

```python
def heap_sort(nums):
    nums = nums[:]

    def sift_down(root, heap_size):
        while True:
            left = 2 * root + 1
            right = left + 1
            largest = root

            if left < heap_size and nums[left] > nums[largest]:
                largest = left
            if right < heap_size and nums[right] > nums[largest]:
                largest = right
            if largest == root:
                return

            nums[root], nums[largest] = nums[largest], nums[root]
            root = largest

    n = len(nums)
    for i in range(n // 2 - 1, -1, -1):
        sift_down(i, n)

    for end in range(n - 1, 0, -1):
        nums[0], nums[end] = nums[end], nums[0]
        sift_down(0, end)

    return nums
```
