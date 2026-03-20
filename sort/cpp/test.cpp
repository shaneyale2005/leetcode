#include <gtest/gtest.h>

#include <algorithm>
#include <limits>
#include <random>
#include <string>
#include <unordered_map>
#include <vector>

void bubble_sort(std::vector<int>& v);
void selection_sort(std::vector<int>& v);

using SortFn = void (*)(std::vector<int>&);

struct SortImplementation {
    const char* name;
    SortFn fn;
};

std::unordered_map<int, int> BuildFrequencyMap(const std::vector<int>& values) {
    std::unordered_map<int, int> freq;
    for (int value : values) {
        ++freq[value];
    }
    return freq;
}

void ExpectSortedMatchesStd(const SortImplementation& impl, const std::vector<int>& input) {
    std::vector<int> actual = input;
    std::vector<int> expected = input;

    impl.fn(actual);
    std::sort(expected.begin(), expected.end());

    EXPECT_EQ(actual, expected) << impl.name;
}

class SortingAlgorithmsTest : public ::testing::TestWithParam<SortImplementation> {};

TEST_P(SortingAlgorithmsTest, HandlesEmptyInput) {
    ExpectSortedMatchesStd(GetParam(), {});
}

TEST_P(SortingAlgorithmsTest, HandlesSingleElementInput) {
    ExpectSortedMatchesStd(GetParam(), {42});
}

TEST_P(SortingAlgorithmsTest, HandlesAlreadySortedInput) {
    ExpectSortedMatchesStd(GetParam(), {-5, -1, 0, 2, 9, 13});
}

TEST_P(SortingAlgorithmsTest, HandlesReverseSortedInput) {
    ExpectSortedMatchesStd(GetParam(), {9, 7, 5, 3, 1, -1, -3});
}

TEST_P(SortingAlgorithmsTest, HandlesDuplicatesAndNegatives) {
    ExpectSortedMatchesStd(GetParam(), {3, -1, 2, -1, 3, 0, 2, -5});
}

TEST_P(SortingAlgorithmsTest, HandlesExtremeIntegerValues) {
    const int kMin = std::numeric_limits<int>::min();
    const int kMax = std::numeric_limits<int>::max();
    ExpectSortedMatchesStd(GetParam(), {0, kMax, -1, kMin, 42, kMax, kMin});
}

TEST_P(SortingAlgorithmsTest, PreservesElementMultiset) {
    const SortImplementation impl = GetParam();
    std::vector<int> input = {5, 1, 5, 2, 9, 2, 2, -7, -7, 0};

    const auto before = BuildFrequencyMap(input);
    impl.fn(input);
    const auto after = BuildFrequencyMap(input);

    EXPECT_EQ(before, after) << impl.name;
    EXPECT_TRUE(std::is_sorted(input.begin(), input.end())) << impl.name;
}

TEST_P(SortingAlgorithmsTest, IsIdempotent) {
    const SortImplementation impl = GetParam();
    std::vector<int> input = {4, 1, 3, 2, 3, 1, 0, -2};

    impl.fn(input);
    const std::vector<int> once_sorted = input;

    impl.fn(input);

    EXPECT_EQ(input, once_sorted) << impl.name;
}

TEST_P(SortingAlgorithmsTest, RandomizedAgainstStdSort) {
    const SortImplementation impl = GetParam();
    std::mt19937 rng(123456789);
    std::uniform_int_distribution<int> size_dist(0, 128);
    std::uniform_int_distribution<int> value_dist(-1000, 1000);

    for (int case_id = 0; case_id < 300; ++case_id) {
        const int size = size_dist(rng);
        std::vector<int> input;
        input.reserve(size);

        for (int i = 0; i < size; ++i) {
            input.push_back(value_dist(rng));
        }

        std::vector<int> actual = input;
        std::vector<int> expected = input;

        impl.fn(actual);
        std::sort(expected.begin(), expected.end());

        EXPECT_EQ(actual, expected) << impl.name << ", case_id=" << case_id;
    }
}

std::string ParameterName(const ::testing::TestParamInfo<SortImplementation>& info) {
    return info.param.name;
}

INSTANTIATE_TEST_SUITE_P(
    AllSortImplementations,
    SortingAlgorithmsTest,
    ::testing::Values(
        SortImplementation{"BubbleSort", bubble_sort},
        SortImplementation{"SelectionSort", selection_sort}),
    ParameterName);
