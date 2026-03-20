#include <vector>
#include <iostream>
#include <algorithm>

/**
 * 冒泡排序
 */
void bubble_sort(std::vector<int> &v) {
    int n = v.size();
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (v[j] > v[j + 1]) {
                std::swap(v[j], v[j + 1]);
            }
        }
    }
}

/**
 * 选择排序
 * 核心思想是把列表分为已经排序和没有排序的两个部分
 * 在没有排序的部分中找最小的元素
 * 找到的最小的元素和没有排序部分的第一个元素交换
 * 然后将没有排序的部分向后移动一位，扩大已经排序的部分的范围
 */
void selection_sort(std::vector<int> &v) {
    int n = v.size();
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (v[j] < v[min_idx]) {
                min_idx = j;
            }
        }
        std::swap(v[i], v[min_idx]);
    }
}

/**
 * 插入排序
 * 核心思想是将当前元素插入到已排序部分的正确位置
 * 首先 key 作为是待插入的元素，然后 j 作为一个指针，从后往前遍历
 */
void insertion_sort(std::vector<int> &v) {
    int n = v.size();
    for (int i = 1; i < n; ++i) {
        int key = v[i];
        int j = i - 1;
        while (j >= 0 && v[j] > key) {
            v[j + 1] = v[j];
            --j;
        }
        v[j + 1] = key;
    }
}