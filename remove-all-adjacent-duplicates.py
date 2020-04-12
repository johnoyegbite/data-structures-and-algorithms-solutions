# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 13:07:58 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a string S of lowercase letters, a duplicate removal consists of
    choosing two adjacent and equal letters, and removing them.

    We repeatedly make duplicate removals on S until we no longer can.

    Return the final string after all such duplicate removals have been made.
    It is guaranteed the answer is unique.


Example 1:
    Input: "abbaca"
    Output: "ca"
    Explanation:
        For example, in "abbaca" we could remove "bb" since the letters are
        adjacent and equal, and this is the only possible move.
        The result of this move is that the string is "aaca", of which only
        "aa" is possible, so the final string is "ca".

Note:
    1 <= S.length <= 20000
    S consists only of English lowercase letters.
"""


def compress(s, stack):
    compressed = False
    while len(stack) and stack[-1] == s:
        compressed = True
        stack.pop()

    if not compressed:
        stack.append(s)


def removeDuplicates(S):
    """
    :type S: str
    :rtype: str
    """
    if not len(S):
        return ''

    stack = []

    for s in S:
        compress(s, stack)

    return ''.join(stack)


if __name__ == "__main__":
    S = "abbaca"
    S = "deeedbbcccbdaa"
    print(removeDuplicates(S))
