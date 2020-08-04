# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 23:54:01 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given n non-negative integers a1, a2, ..., an , where each represents a 
    point at coordinate (i, ai). n vertical lines are drawn such that the two 
    endpoints of line i is at (i, ai) and (i, 0). Find two lines, which 
    together with x-axis forms a container, such that the container contains 
    the most water.

    Note: You may not slant the container and n is at least 2.

 
    PS: There is a picture for this problem


    The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
    In this case, the max area of water (blue section) the container can 
    contain is 49.

Example:
    Input: [1,8,6,2,5,4,8,3,7]
    Output: 49
"""


import sys


def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    max_area = - sys.maxsize - 1
    i = 0
    j = len(height) - 1
    while i != j:
        first_boundary = height[i]
        second_boundary = height[j]
        container_height = min(first_boundary, second_boundary)
        container_width = j - i
        area = container_height * container_width
        max_area = max(max_area, area)
        if first_boundary < second_boundary:
            i += 1
        else:
            j -= 1
    return max_area


if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    print(maxArea(height))
