# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 16:01:59 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given an array of non-negative integers, you are initially positioned at
    the first index of the array.

    Each element in the array represents your maximum jump length at that
    position.

    Determine if you are able to reach the last index.

Example 1:
    Input: [2,3,1,1,4]
    Output: true
    Explanation:
        Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
    Input: [3,2,1,0,4]
    Output: false
    Explanation:
        You will always arrive at index 3 no matter what. Its maximum
        jump length is 0, which makes it impossible to reach the last index.
"""


class Solution:
    def canJump(self, nums) -> bool:
        last_index = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= last_index:
                last_index = i

        return last_index == 0


if __name__ == "__main__":
    s = Solution()
    nums = [0]  # True
    # nums = [2, 3, 1, 1, 4]  # True
    # nums = [3, 0, 1, 0, 4]  # False
    # nums = [3, 2, 1, 0, 4]  # False
    # nums = [2, 0, 0]  # True
    # nums = [2, 5, 0, 0]  # True
    # nums = [3, 0, 8, 2, 0, 0, 1]  # True
    nums = [3, 0, 1, 0, 8, 2, 0, 0, 1]  # False
    # nums = [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]  # True

    print(s.canJump(nums))
