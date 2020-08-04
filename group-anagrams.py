# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 00:27:30 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given an array of strings, group anagrams together.

Example:
    Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
    Output:
        [
            ["ate","eat","tea"],
            ["nat","tan"],
            ["bat"]
        ]

Note:
    All inputs will be in lowercase.
    The order of your output does not matter.
"""


def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    anagram_group = {}

    for s in strs:
        s_order = tuple(sorted(s))
        if s_order in anagram_group:
            anagram_group[s_order].append(s)
        else:
            anagram_group[s_order] = [s]

    return anagram_group.values()


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs))
