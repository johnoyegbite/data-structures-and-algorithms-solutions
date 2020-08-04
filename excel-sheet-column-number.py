# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 01:43:37 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a column title as appear in an Excel sheet,
    return its corresponding column number.

    For example:
        A -> 1
        B -> 2
        C -> 3
        ...
        Z -> 26
        AA -> 27
        AB -> 28
    ...
Example 1:
    Input: "A"
    Output: 1

Example 2:
    Input: "AB"
    Output: 28

Example 3:
    Input: "ZY"
    Output: 701
"""


def titleToNumber(s):
    """
    :type s: str
    :rtype: int
    """
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    title = {s: i+1 for i, s in enumerate(alpha)}
    i = len(s)-1
    j = 0
    col_num = 0
    while i >= 0:
        col_num += title[s[j]] * (26**i)
        i -= 1
        j += 1

    return col_num
