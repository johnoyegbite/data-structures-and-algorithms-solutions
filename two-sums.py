# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 02:04:18 2019

@author: USER
"""
# SOLVED!
"""
Problem Description:
    Given an array of integers, return indices of the two numbers such that
    they add up to a specific target.

    You may assume that each input would have exactly one solution, 
    and you may not use the same element twice.

Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
"""


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype
    """
    nums_dict = {}
    for i, num in enumerate(nums):
        compliment = target - num
        if compliment not in nums_dict:
            nums_dict[num] = i
        else:
            return (nums_dict[compliment], i)
    return None


if __name__ == "__main__":        
    nums = [2, 15, 11, 7]
    target = 9
    
    # nums = [-1,-2,-3,-4,-5]
    # target = -8
    
    # nums = [-10,-1,-18,-19]
    # target = -19
    
    print(twoSum(nums, target))