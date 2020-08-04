# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 02:51:57 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given two arrays, write a function to compute their intersection.

Example 1:
    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2,2]

Example 2:
    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [4,9]

Note:
    Each element in the result should appear as many times as it shows in both
    arrays.
    The result can be in any order.

Follow up:
    What if the given array is already sorted? How would you optimize your
    algorithm?
    What if nums1's size is small compared to nums2's size? Which algorithm
    is better?
    What if elements of nums2 are stored on disk, and the memory is limited
    such that you cannot load all elements into the memory at once?
"""


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1_d = {}
        nums2_d = {}

        nums = []
        # get nums1 freq
        for num in nums1:
            nums1_d[num] = nums1_d.get(num, 0) + 1
        # get nums2 freq
        for num in nums2:
            nums2_d[num] = nums2_d.get(num, 0) + 1
        # pick the smaller freq, this would be the number of times the current
        # number is appended to the arrya.
        for num in nums1_d:
            if num in nums2_d:
                nums.extend(min(nums1_d[num], nums2_d[num])*[num])

        return nums
