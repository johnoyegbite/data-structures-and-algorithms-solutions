# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 21:57:43 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Suppose a sorted array is rotated at some pivot unknown to you beforehand.

    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

    You are given a target value to search.
    If found in the array return its index, otherwise return -1.

    You may assume no duplicate exists in the array.

Example 1:
    Input: [4, 5, 1, 2, 3] and target=1,
    Output: 2.

Example 2:
    Input: [4, 5, 1, 2, 3] and target=0,
    Output: -1.

Challenge:
    O(logN) time

"""


def search(nums, target):
    """
    type A: List[int]
    type target: int
    rtype: int
    """
    if not len(nums):
        return -1
    start = 0
    end = len(nums)-1

    while start <= end:
        # mid = (start + end)//2
        mid = start + (end - start)//2

#       arr = [0,1,2,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1] target = -9

        if nums[start] == target:
            return start  # return index
        if nums[end] == target:
            return end
        if nums[mid] == target:
            return mid

        # right half keeps sorted in ascending order after rotation
        if nums[start] < nums[mid]:
            if nums[start] < target < nums[mid]:  # Search target in left half
                end = mid - 1
            else:  # Search target in right half
                start = mid + 1
        # left half keeps sorted in ascending order after rotation
        else:
            if nums[mid] < target < nums[end]:  # Search target in right half
                start = mid + 1
            else:  # Search target in left half
                end = mid - 1
    return -1


if __name__ == "__main__":
    nums = [4, 5, 1, 2, 3]
    target = 5
    
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 1
    
    # nums = [0, 1, 2, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
    # target = -9
    
    print(search(nums, target))
