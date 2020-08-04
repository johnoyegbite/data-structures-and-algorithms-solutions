# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 18:58:36 2020

@author: johnoyegbite
"""
# SOLVED!

"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to
 you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2]
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
"""


class Solution:
    def findMin(self, nums) -> int:  # O(log n)
        """
          if mid greater than start and less than end // go left
          if mid is less than start // go left
          else (=> mid greater than or equal to start) // go right

          OR

          IF mid less than end // go left
          else // go right

          type nums: List[int]
          rtype: int
        """
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if ((nums[mid] > nums[start] and nums[mid] < nums[end])
                    or
                    (nums[mid] <= nums[start] and nums[mid] <= nums[end])):
                end = mid
            else:
                start = mid + 1
        return nums[start]


if __name__ == "__main__":
    s = Solution()
    nums = [3, 4, 5, 1, 2]
    print(s.findMin(nums))
