# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 02:33:08 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given two arrays, write a function to compute their intersection.

Example 1:
    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2]

Example 2:
    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [9,4]

Note:
    Each element in the result must be unique.
    The result can be in any order.

"""


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1).intersection(set(nums2)))
