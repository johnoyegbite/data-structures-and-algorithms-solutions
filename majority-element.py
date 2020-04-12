# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 01:58:00 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given an array of size n, find the majority element.
    The majority element is the element that appears more than ⌊ n/2 ⌋ times.

    You may assume that the array is non-empty and the majority element always
    exist in the array.

Example 1:
    Input: [3,2,3]
    Output: 3

Example 2:
    Input: [2,2,1,1,1,2,2]
    Output: 2
"""


def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    num_dict = {}
    for n in nums:
        num_dict[n] = num_dict.get(n, 0) + 1

    for num in num_dict:
        if num_dict[num] > len(nums)//2:
            return num
