cmake_minimum_required(VERSION 3.15)
project(bubble_sort_test)

set(CMAKE_CXX_STANDARD 17)

find_package(GTest CONFIG REQUIRED)

add_executable(test
    bubble_sort.cpp
    test.cpp
)

target_link_libraries(test
    GTest::gtest
    GTest::gtest_main
)
