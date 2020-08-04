# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 01:37:47 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Write a function that reverses a string.
    The input string is given as an array of characters char[].

    Do not allocate extra space for another array, you must do this by
    modifying the input array in-place with O(1) extra memory.

    You may assume all the characters consist of printable ascii characters.

Example 1:
    Input: ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]

Example 2:
    Input: ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]
"""


class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        end = len(s)//2
        for i in range(0, end):
            s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]
