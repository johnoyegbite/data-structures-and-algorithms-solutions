#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 22:56:28 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a string s, find the longest palindromic substring in s.
    You may assume that the maximum length of s is 1000.

Example 1:
    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.

Example 2:
    Input: "cbbd"
    Output: "bb"
"""


class Solution:
    def getCharLongestSubstring(self, s: str, indexes) -> str:
        # Given list of indexes in s,
        # check the last index with all the indexes from the beginning,
        # if the substring composed of curr index and the last index is a
        # palindrome, return its length and substring early since the length of
        # the next substring composed of the next index and last index
        # (if palindrome) won't be larger.
        if not indexes or len(indexes) < 2:
            return -1, ""
        for index in indexes:
            # note that if curr index is 0 and want to get the substring
            # of the reverse then you must go all the way to the beginning.
            if index == 0:
                if s[:indexes[-1]+1] == s[indexes[-1]::-1]:
                    return indexes[-1] - index + 1, s[:indexes[-1]+1]
            else:
                if s[index:indexes[-1]+1] == s[indexes[-1]:index-1:-1]:
                    return indexes[-1] - index + 1, s[index:indexes[-1]+1]
        return -1, ""
        
    def longestPalindrome(self, s: str) -> str:
        # Idea is when you have any start and end index with the "same character",
        # then you can check the substring that the start and end index denotes,
        # if they are palindrome. Then update if longest_substring if it exceeds
        # the previous palindromic substring.
        # Example
        # s = mallamp    
        # longest = 1
        # longest_sub = "m"
        # chars = {
        #     m: [0, 5], max3 = 6, "mallam"
        #     a: [1, 4], max2 = 4, "alla"
        #     l: [2, 3], max1 = 2, "ll"
        #     p: [6]   
        # }
        
        longest = len(s[:1])
        longest_sub = s[:1]  # initialize the longest substring
        chars = {}  # to store all the char and the index they occur
        
        # loop through all the char,
        # the moment you see the char again, get all the index of the char
        # check all the indexes that the current char has occur so far using
        # the getCharLongestSubstring().
        # getCharLongestSubstring:
        #   check the last index with all the indexes from the beginning,
        #   if the substring composed of curr index and the last index is a
        #   palindrome, return its length and substring early since the length
        #   of the next substring composed of the next index and last index
        #   (if palindrome) won't be larger.
        for index, char in enumerate(s):
            # seeing the character the 1st time.
            if char not in chars:
                chars[char] = [index]
                continue

            # seeing the character more than 1ce.
            chars[char].append(index)
            curr_char_indexes_so_far = chars[char]
            curr_longest, curr_longest_sub = self.getCharLongestSubstring(s, curr_char_indexes_so_far)
            if curr_longest > longest:
                longest_sub = curr_longest_sub
                longest = max(longest, curr_longest)

        return longest_sub
                
            
        
