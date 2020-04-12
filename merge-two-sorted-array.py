# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 17:30:02 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
    

Example 1:
    Input：[1, 2, 3] 3  [4,5]  2
    Output：[1,2,3,4,5]
    Explanation:
    After merge, nums1 will be filled as [1, 2, 3, 4, 5]

Example 2:
    Input：[1,2,5] 3 [3,4] 2
    Output：[1,2,3,4,5]
    Explanation:
    After merge, nums1 will be filled as [1, 2, 3, 4, 5]

Notice:
    You may assume that nums1 has enough space (size that is greater or equal to m + n) 
    to hold additional elements from nums2. The number of elements initialized
    in nums1 and nums2 are m and n respectively.

"""
def merge_sorted_array(nums1, m, nums2, n): # O(m*n + nlogn + n)
    """
    [1,2,5] 3 
    
    [3,4] 2
    """
    for j, j_nums in enumerate(nums2):
        for i, i_nums in enumerate(nums1[:m]):
            if nums1[i] > nums2[j]:
                nums1[i], nums2[j] = nums2[j], nums1[i]
                
    nums2.sort()
            
    for j, j_nums in enumerate(nums2):
        nums1[m] = nums2[j]
        m += 1

def mergeSortedArray(nums1, m, nums2, n): # Time: O(m+n); Space: O(m+n)
    # write your code here
    merged = []
    
    i, j = 0, 0
    
    while i < m and j < n:
        num_a = nums1[i]
        num_b = nums2[j]
        
        smaller = min(num_a, num_b)
        
        if num_a == smaller:
            merged.append(num_a)
            i += 1
        if num_b == smaller:
            merged.append(num_b)
            j += 1
            
    while i < m:
        num_a = nums1[i]
        merged.append(num_a)
        i += 1
        
    while j < n:
        num_b = nums2[j]
        merged.append(num_b)
        j += 1
        
    for k, k_num in enumerate(merged):
        nums1[k] = merged[k]
    return nums1

def merge_sorted_array_2(nums1, m, nums2, n): # 0(m+n)
    i, j, k = m-1, n-1, m+n-1
    # Start operation from the end of nums1 and nums2 using i, j
    # Since array is sorted then either of the element at the end of nums1 or 
    # nums2 would be the largest.
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    if j >= 0:
        nums1[:k+1] = nums2[:j+1]

        
if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    print(mergeSortedArray(nums1, m, nums2, n))
