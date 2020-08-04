# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 13:53:59 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given two strings S and T, return if they are equal when both are typed
    into empty text editors. # means a backspace character.

Example 1:
    Input: S = "ab#c", T = "ad#c"
    Output: true
    Explanation: Both S and T become "ac".

Example 2:
    Input: S = "ab##", T = "c#d#"
    Output: true
    Explanation: Both S and T become "".

Example 3:
    Input: S = "a##c", T = "#a#c"
    Output: true
    Explanation: Both S and T become "c".

Example 4:
    Input: S = "a#c", T = "b"
    Output: false
    Explanation: S becomes "c" while T becomes "b".

Note:
    1 <= S.length <= 200
    1 <= T.length <= 200
    S and T only contain lowercase letters and '#' characters.

Follow up:
    Can you solve it in O(N) time and O(1) space?
"""


# def compress(S):  # O(1) space
#     s = 0
#     num_back_space = 0
#     idx = len(S)-1
#     while idx >= 0:
#         if S[idx] != "#":
#             if num_back_space == 0:
#                 s += ord(S[idx])
#             else:
#                 num_back_space -= 1
#         else:
#             num_back_space += 1
#         idx -= 1
#     return s


def compress(S):  # O(n) space
    stack = []
    for s in S:
        if s == "#":
            if len(stack):
                stack.pop()
        else:
            stack.append(s)
    return stack


def backspaceCompare(S, T):
    """
    :type S: str
    :type T: str
    :rtype: bool
    """
    return compress(S) == compress(T)


if __name__ == "__main__":
    S = "ab##"
    T = "c#d#"
    
    S = "a##c"
    T = "#a#c"
    
    S = "ab#c"
    T = "ad#c"
    
    S = "a#c"
    T = "b"
    
    S = "ab#c#c"
    T = "cb#a#a"
    
    print(backspaceCompare(S, T))
