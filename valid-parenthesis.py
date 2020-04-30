# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 20:54:23 2020

@author: johnoyegbite
"""
# SOLVED! 
"""
Problem:
    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
    determine if the input string is valid.

    The brackets must close in the correct order, "()" and "()[]{}" are all 
    valid but "(]" and "([)]" are not.

Example 1:
    Input: "([)]"
    Output: False

Example 2:
    Input: "()[]{}"
    Output: True

Challenge:
    Use O(n) time, n is the number of parentheses.
"""


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    closed_b = {"(": ")", "{": "}", "[": "]"}

    for b in s:
        if b == "(" or b == "[" or b == "{":
            stack.append(b)
        else:
            if not len(stack) or closed_b[stack.pop()] != b:
                return False

    if len(stack):
        return False
    return True


if __name__ == "__main__":
    s = "(])"
    s = "()[]{}"
    print(isValid(s))
