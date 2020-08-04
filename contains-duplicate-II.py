# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 23:52:57 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given an array of integers and an integer k,
    find out whether there are two distinct indices i and j in the array
    such that nums[i] = nums[j] and the absolute difference between i and j
    is at most k.

Example 1:
    Input: nums = [1,2,3,1], k = 3
    Output: true

Example 2:
    Input: nums = [1,0,1,1], k = 1
    Output: true

Example 3:
    Input: nums = [1,2,3,1,2,3], k = 2
    Output: false
"""


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        nums_dict = {}

        for i, num in enumerate(nums):
            if num in nums_dict:
                if abs(nums_dict[num][-1] - i) <= k:
                    return True
                nums_dict[num].append(i)
            else:
                nums_dict[num] = [i]

        return False
