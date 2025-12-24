#include <gtest/gtest.h>
#include <vector>

void bubble_sort(std::vector<int>& v);

TEST(BubbleSortTest, NormalCase) {
    std::vector<int> v = {5, 3, 8, 4, 2};
    bubble_sort(v);
    EXPECT_EQ(v, (std::vector<int>{2, 3, 4, 5, 8}));
}

TEST(BubbleSortTest, EmptyVector) {
    std::vector<int> v;
    bubble_sort(v);
    EXPECT_TRUE(v.empty());
}

TEST(BubbleSortTest, SingleElement) {
    std::vector<int> v = {1};
    bubble_sort(v);
    EXPECT_EQ(v, (std::vector<int>{1}));
}

TEST(BubbleSortTest, Duplicates) {
    std::vector<int> v = {3, 1, 2, 1, 3};
    bubble_sort(v);
    EXPECT_EQ(v, (std::vector<int>{1, 1, 2, 3, 3}));
}
