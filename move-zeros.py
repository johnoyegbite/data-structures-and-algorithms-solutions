# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 18:17:25 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given an array nums, write a function to move all 0's to the end of it 
    while maintaining the relative order of the non-zero elements.

Example:
    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]

Note:
    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.
"""

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    j = 0
    for i, num in enumerate(nums):
        if num != 0:
           # order of line 1 and line 2 matters
           nums[i] = 0  #line 1
           nums[j] = num  #line 2
           j += 1


if __name__ == "__main__":
    nums = [0,1,0,3,12]
    print(moveZeroes(nums))
    print(nums)
    