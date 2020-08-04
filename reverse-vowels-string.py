# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 02:21:35 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Write a function that takes a string as input and reverse only the vowels
    of a string.

Example 1:
    Input: "hello"
    Output: "holle"

Example 2:
    Input: "leetcode"
    Output: "leotcede"

Note:
The vowels does not include the letter "y".
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        left = 0
        right = len(s_list)-1
        while left < right:
            if s_list[left] in vowels and s_list[right] in vowels:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
            if s_list[right] not in vowels:
                right -= 1
            if s_list[left] not in vowels:
                left += 1

        return ''.join(s_list)
