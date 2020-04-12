# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 11:50:06 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem Description:
    There are two sorted arrays nums1 and nums2 of size m and n respectively.

    Find the median of the two sorted arrays. 
    The overall run time complexity should be O(log(m+n)).

    You may assume nums1 and nums2 cannot be both empty.

Example 1:
    nums1 = [1, 3]
    nums2 = [2]
    The median is 2.0

Example 2:
    nums1 = [1, 2]
    nums2 = [3, 4]
    The median is (2 + 3)/2 = 2.5
"""


def findMedianSortedArrays(nums1, nums2):
    arr_size = len(nums1) + len(nums2)
    seen_inorder = []
    
    i, j = 0, 0 # index for nums1, index for nums2
    middle = (arr_size // 2.0) + 1
    
    while middle > len(seen_inorder):
        if i < len(nums1) and j < len(nums2):
            smaller = min(nums1[i], nums2[j])
            if smaller == nums1[i] and middle > len(seen_inorder):
                seen_inorder.append(nums1[i])
                i += 1
            if smaller == nums2[j] and middle > len(seen_inorder):
                seen_inorder.append(nums2[j])
                j += 1
        elif i < len(nums1) and middle > len(seen_inorder):
            seen_inorder.append(nums1[i])
            i += 1
        elif j < len(nums2) and middle > len(seen_inorder):
            seen_inorder.append(nums2[j])
            j += 1
    # for the median value, pick last value in seen_inorder if the total arr 
    # arr_size is odd else the average of the last two value if total arr arr_size is even
    median = (seen_inorder[-1] + seen_inorder[-2]) / 2.0 if arr_size % 2 == 0 else seen_inorder[-1]
    
    return median


if __name__ == "__main__":
    nums1 = [1, 2, 3, 4]
    nums2 = [6, 7, 8, 9]
    
    # nums1 = [1, 3]
    # nums2 = [2]
    
    print(findMedianSortedArrays(nums1, nums2))
