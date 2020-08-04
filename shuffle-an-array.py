# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 00:24:00 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Shuffle a set of numbers without duplicates.

Example:
// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();

"""
from random import randint


class Solution:
    def __init__(self, nums):
        """
        type nums: List[int]
        """
        self.orig = nums.copy()
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        rtype: List[int]
        """
        return self.orig

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        rtype: List[int]
        """
        # for every index, generate a random index
        # then swap the number at the current index with the random index
        for i in range(len(self.nums)):
            randIdx = randint(0, len(self.nums) - 1)
            self.nums[i], self.nums[randIdx] = self.nums[randIdx], self.nums[i]
        return self.nums


# Your Solution object will be instantiated and called as such:
if __name__ == "__main__":
    nums = [1, 2, 3]
    obj = Solution(nums)
    param_1 = obj.reset()
    param_2 = obj.shuffle()
