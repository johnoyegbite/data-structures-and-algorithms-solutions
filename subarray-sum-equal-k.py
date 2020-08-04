# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 14:42:34 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given an array of integers and an integer k, you need to find the total
    number of continuous subarrays whose sum equals to k.

Example 1:
    Input:nums = [1,1,1], k = 2
    Output: 2

Note:
    The length of the array is in range [1, 20,000].
    The range of numbers in the array is [-1000, 1000]
    and the range of the integer k is [-1e7, 1e7].
"""


class Solution:  # O(N^2) solution
    def moveContiguously(self, i: int, count: int,
                         k: int, nums):
        if i >= len(nums):
            return
        count += nums[i]
        if count == k:
            self.total += 1
        self.moveContiguously(i+1, count, k, nums)
        return

    def subarraySum(self, nums, k: int) -> int:
        self.total = 0
        for i, num in enumerate(nums):
            self.moveContiguously(i, 0, k, nums)
        return self.total


def subarraySum(nums, k: int) -> int:  # O(N) solution
    count = 0
    total = 0
    cummulative = {total: 1}

    for i, num in enumerate(nums):
        total += num
        if total-k in cummulative:
            count += cummulative[total-k]
        cummulative[total] = cummulative.get(total, 0) + 1

    return count


if __name__ == "__main__":
    s = Solution()
    nums = [1, 1, 1]
    k = 2
    nums = [1, 2, 0, -1, -2, 1]
    k = 0
    # nums = [1, 2, 3]
    # k = 3
    # print(s.subarraySum(nums, k))
    print(subarraySum(nums, k))
