# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 00:58:35 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a sorted array and a target value, return the index if the target is
    found.
    If not, return the index where it would be if it were inserted in order.

    You may assume no duplicates in the array.

Example 1:
    Input: [1,3,5,6], 5
    Output: 2

Example 2:
    Input: [1,3,5,6], 2
    Output: 1

Example 3:
    Input: [1,3,5,6], 7
    Output: 4

Example 4:
    Input: [1,3,5,6], 0
    Output: 0
"""


def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # METHOD 1: O(logN)
    # start = 0
    # end = len(nums)-1
    # while start < end:
    #     mid = (start + end) // 2
    #     if nums[mid] == target:
    #         return mid
    #     if nums[mid] > target:
    #         end = mid
    #     else:
    #         start = mid + 1
    # if end == len(nums) - 1:
    #     return end if nums[end] >= target else len(nums)
    # return end

    # METHOD 2: O(N)
    for i, num in enumerate(nums):
        if num >= target:
            return i
    return len(nums)


if __name__ == "__main__":
    nums = [1, 3, 5, 6]  # 2
    target = 5
    nums = [1]  # 0
    target = 0
    # nums = [1, 3, 5, 6]  # 1
    # target = 2
    # nums = [1, 3, 5, 6]  # 4
    # target = 7
    # nums = [1, 3, 5, 6]  # 0
    # target = 0
    print(searchInsert(nums, target))
