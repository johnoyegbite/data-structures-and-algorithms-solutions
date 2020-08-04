# -*- coding: utf-8 -*-
"""
Created on Sun May  3 04:14:39 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Check If All 1's Are at Least Length K Places Away
    Given an array nums of 0s and 1s and an integer k,
    return True if all 1's are at least k places away from each other,
    otherwise return False.

Example 1:
    Input: nums = [1,0,0,0,1,0,0,1], k = 2
    Output: true
    Explanation: Each of the 1s are at least 2 places away from each other.

Example 2:
    Input: nums = [1,0,0,1,0,1], k = 2
    Output: false
    Explanation: The second 1 and third 1 are only one apart from each other.

Example 3:
    Input: nums = [1,1,1,1,1], k = 0
    Output: true

Example 4:
    Input: nums = [0,1,0,1], k = 1
    Output: true

Constraints:
    1 <= nums.length <= 10^5
    0 <= k <= nums.length
    nums[i] is 0 or 1
"""


class Solution:
    def kLengthApart(self, nums, k: int) -> bool:
        """
        type nums: List[int]
                k: int
        rtype: bool
        """
        last = -1
        for i, num in enumerate(nums):
            if num == 1 and last == -1:
                last = i
            elif num == 1:
                if i - 1 - last < k:
                    return False
                last = i
        return True
