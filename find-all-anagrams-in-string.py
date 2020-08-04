# -*- coding: utf-8 -*-
"""
Created on Sun May 17 10:39:13 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a string s and a non-empty string p, find all the start indices of
    p's anagrams in s.

    Strings consists of lowercase English letters only and the length of both
    strings s and p will not be larger than 20,100.

    The order of output does not matter.

Example 1:
    Input:
        s: "cbaebabacd" p: "abc"
    Output:
        [0, 6]

Explanation:
    The substring with start index = 0 is "cba", which is an anagram of "abc".
    The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
    Input:
        s: "abab" p: "ab"
    Output:
        [0, 1, 2]

Explanation:
    The substring with start index = 0 is "ab", which is an anagram of "ab".
    The substring with start index = 1 is "ba", which is an anagram of "ab".
    The substring with start index = 2 is "ab", which is an anagram of "ab".
"""
from collections import Counter


class Solution:
    def freqEqual(self, s, p_freq):
        s_freq = {}
        for char in s:
            s_freq[char] = s_freq.get(char, 0) + 1

        for char in p_freq:
            if (char not in s_freq) or (p_freq[char] != s_freq[char]):
                return False
        return True

    # TIME LIMIT EXCEEDED (34/36 test cases passed)
    def findAnagrams(self, s: str, p: str):
        # s = "abcabcabcabcabc", p = "abc"
        # output = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        anag_len = len(p)
        str_len = len(s)
        start_indices = []
        p_freq = {}
        for char in p:
            p_freq[char] = p_freq.get(char, 0) + 1

        for i, char in enumerate(s):
            # total no. of chars above this index and the subsequent
            # indices would be lesser than the no. of chars in p
            # hence no need to check
            if i > str_len - anag_len:
                break
            if self.freqEqual(s[i:i+anag_len], p_freq):
                start_indices.append(i)

        return start_indices


def findAnagrams(s: str, p: str):
    # s = "abcabcabcabcabc", p = "abc"
    # output = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    anag_len = len(p)
    str_len = len(s)
    start_indices = []
    p_freq = Counter(p)  # Counter() convert p to a dictionary

    for i, char in enumerate(s):
        # total no. of chars above this index and the subsequent
        # indices would be lesser than the no. of chars in p
        # hence no need to check
        if i > str_len - anag_len:
            break

        # Using Counter for dictionary comparison,
        # returns True if both dictionary are equal in terms of
        # characters and frequencies of those characters.
        if Counter(s[i:i+anag_len]) == p_freq:
            start_indices.append(i)

    return start_indices


"""
Better Version of Counter:
    https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss
    /92009/Python-Sliding-Window-Solution-using-Counter
"""
