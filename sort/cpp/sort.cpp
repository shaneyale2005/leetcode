#include <vector>
#include <iostream>
#include <algorithm>

/**
 * 冒泡排序
 */
std::vector<int> bubble_sort(std::vector<int> nums) {
    int n = nums.size();
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (nums[j] > nums[j + 1]) {
                std::swap(nums[j], nums[j + 1]);
            }
        }
    }
    return nums;
}

/**
 * 选择排序
 * 核心思想是把列表分为已经排序和没有排序的两个部分
 * 在没有排序的部分中找最小的元素
 * 找到的最小的元素和没有排序部分的第一个元素交换
 * 然后将没有排序的部分向后移动一位，扩大已经排序的部分的范围
 */
std::vector<int> selection_sort(std::vector<int> nums) {
    int n = nums.size();
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (nums[j] < nums[min_idx]) {
                min_idx = j;
            }
        }
        std::swap(nums[i], nums[min_idx]);
    }
    return nums;
}

/**
 * 插入排序
 * 核心思想是将当前元素插入到已排序部分的正确位置
 * 首先 key 作为是待插入的元素，然后 j 作为一个指针，从后往前遍历
 */
std::vector<int> insertion_sort(std::vector<int> nums) {
    int n = nums.size();
    for (int i = 1; i < n; ++i) {
        int key = nums[i];
        int j = i - 1;
        while (j >= 0 && nums[j] > key) {
            nums[j + 1] = nums[j];
            --j;
        }
        nums[j + 1] = key;
    }
    return nums;
}

std::vector<int> shell_sort(std::vector<int> nums) {
    int n = nums.size();
    for (int gap = n / 2; gap > 0; gap /= 2) {
        for (int i = gap; i < n; i++) {
            int temp = nums[i];
            int j = i;
            while (j >= gap && nums[j - gap] > temp) {
                nums[j] = nums[j - gap];
                j -= gap;
            }
            nums[j] = temp;
        }
    }
    return nums;
}

std::vector<int> merge_sort(std::vector<int> nums) {
    int n = nums.size();

    if (n <= 1) {
        return nums;
    }

    int mid = n / 2;
    std::vector<int> left(nums.begin(), nums.begin() + mid);
    std::vector<int> right(nums.begin() + mid, nums.end());

    left = merge_sort(left);
    right = merge_sort(right);

    std::vector<int> result(n);
    std::merge(left.begin(), left.end(), right.begin(), right.end(), result.begin());
    return result;
}

std::vector<int> quick_sort(std::vector<int> nums) {
    int n = nums.size();
    if (n <= 1) return nums;
    int pivot = nums[n / 2];
    std::vector<int> left, right, middle;
    for (int x : nums) {
        if (x < pivot) {
            left.push_back(x);
        } else if (x == pivot) {
            middle.push_back(x);
        } else if (x > pivot) {
            right.push_back(x);
        }
    }

    left = quick_sort(left);
    right = quick_sort(right);
    left.insert(left.end(), middle.begin(), middle.end());
    left.insert(left.end(), right.begin(), right.end());
    return left;
}
