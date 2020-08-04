# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 16:54:57 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
    find the one that is missing from the array.

Example 1:
    Input: [3,0,1]
    Output: 2

Example 2:
    Input: [9,6,4,2,3,5,7,0,1]
    Output: 8

Note:
    Your algorithm should run in linear runtime complexity. 
    Could you implement it using only constant extra space complexity?
    
"""

def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    seen = set(nums)
    for i in range(len(nums)+1):
        if i not in seen:
            return i

if __name__ == "__main__":
    nums = [3,0,1] # 2
    nums = [9,6,4,2,3,5,7,0,1] # 8
    print(missingNumber(nums))
    