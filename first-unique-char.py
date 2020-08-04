# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 23:54:44 2019

@author: USER
"""
# SOLVED!
"""
Problem:
    Given a string, find the first non-repeating character in it and return
    it's index. If it doesn't exist, return -1.

Examples:
    s = "leetcode"
    return 0.

    s = "loveleetcode",
    return 2.

Note: You may assume the string contain only lowercase letters.
"""


def first_unique_char(s):
    char_dict = {}
    for char in s:
        char_dict[char] = char_dict.get(char, 0) + 1

    for i, char in enumerate(s):
        if char_dict[char] == 1:
            return i

    return -1


if __name__ == "__main__":
    string = "racecars"
    string = "blloommbeerrgg"
    print(first_unique_char(string))
