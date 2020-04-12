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
    for i, num in enumerate(nums):
        if num > target or num == target:
            break
    if nums[i] >= target:
        return i
    if nums[i] < target:
        return i+1


if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 2
    print(searchInsert(nums, target))
    