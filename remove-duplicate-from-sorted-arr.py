# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 21:21:22 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a sorted array nums, remove the duplicates in-place such that each 
    element appear only once and return the new length.

    Do not allocate extra space for another array, 
    you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
    Given nums = [1,1,2],
    Your function should return length = 2, with the first two elements of nums
    being 1 and 2 respectively.

    It doesn't matter what you leave beyond the returned length.

Example 2:
    Given nums = [0,0,1,1,1,2,2,3,3,4],
    Your function should return length = 5, with the first five elements of nums
    being modified to 0, 1, 2, 3, and 4 respectively.

    It doesn't matter what values are set beyond the returned length.

Clarification:
    Confused why the returned value is an integer but your answer is an array?

    Note that the input array is passed in by reference, which means modification
    to the input array will be known to the caller as well.

    Internally you can think of this:
        // nums is passed in by reference. (i.e., without making a copy)
        len = removeDuplicates(nums);

    // any modification to nums in your function would be known by the caller.
    // using the length returned by your function, it prints the first len elements.
    for i in range(len):
        print(nums[i])
"""
def removeDuplicates(nums):
    # write your code here
    if not len(nums):
        return 0
    
    length = 0
    len_nums = len(nums)
    
    for i in range(1, len_nums):
        if nums[i] != nums[length]:
            nums[length] = nums[i]
            length += 1
            
    return length


if __name__ == "__main__":
    nums = [
        -14,-14,-13,-13,-13,-13,-13,-13,-13,-12,-12,-12,-12,-11,-10,
        -9,-9,-9,-8,-7,-5,-5,-5,-5,-4,-3,-3,-2,-2,-2,-2,-1,-1,-1,-1,
        -1,0,1,1,1,1,2,2,2,3,3,3,4,4,4,4,5,5,5,6,6,6,6,7,8,8,8,9,9,9,
        10,10,10,11,11,11,12,12,12,13,14,14,14,14,15,16,16,16,18,18,18,
        19,19,19,19,20,20,20,21,21,21,21,21,21,22,22,22,22,22,23,23,24,25,25
        ]
    
    nums = [1,1,2]
    
    print(removeDuplicates(nums))
    print(nums)


