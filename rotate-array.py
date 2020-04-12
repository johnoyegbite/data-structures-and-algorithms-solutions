# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 11:33:00 2020

@author: johnoyegbite
"""
# SOLVED !
"""
Problem:
    Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
    Input: [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]
    Explanation:
        rotate 1 steps to the right: [7,1,2,3,4,5,6]
        rotate 2 steps to the right: [6,7,1,2,3,4,5]
        rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
    Input: [-1,-100,3,99], k = 2
    Output: [3,99,-1,-100]
    Explanation: 
        rotate 1 steps to the right: [99,-1,-100,3]
        rotate 2 steps to the right: [3,99,-1,-100]

Challenge:
    1.Try to come up as many solutions as you can, there are at least 3 
      different ways to solve this problem.
    2.Could you do it in-place with O(1) extra space?
"""

def rotate(nums, k):
    # Write your code here
    k = k % len(nums)
    boundary = len(nums) - k
    return nums[boundary: ] + nums[ :boundary]


if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    
    nums = [-1,-100,3,99]
    k = 2
    print(rotate(nums, k))