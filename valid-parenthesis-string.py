# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 14:46:06 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a string containing only three types of characters: '(', ')' and
    '*', write a function to check whether this string is valid.

    We define the validity of a string by these rules:
        1. Any left parenthesis '(' must have a corresponding right
            parenthesis ')'.
        2. Any right parenthesis ')' must have a corresponding left
            parenthesis '('.
        3. Left parenthesis '(' must go before the corresponding
            right parenthesis ')'.
        4. '*' could be treated as a single right parenthesis ')' or a single
            left parenthesis '(' or an empty string.
        5. An empty string is also valid.

Example 1:
    Input: "()"
    Output: True

Example 2:
    Input: "(*)"
    Output: True

Example 3:
    Input: "(*))"   "(*())"   "(**)"   "*)"
    Output: True

Note:
    The string size will be in the range [1, 100].
"""


# def tree(i, s, count):
#     # if we have reached the end of string and string is balanced.
#     if i >= len(s) and count == 0:
#         return True
#     # if we have reached the end of string and string has more ")" or "(".
#     if i >= len(s) and (count < 0 or count > 0):
#         return False
#     # if we haven't reached the end of the string but string is unbalanced,
#     # stop early and dont go through this path.
#     if count < 0 or count >= len(s):
#         return False

#     if s[i] == "(":
#         count += 1
#     if s[i] == ")":
#         count -= 1
#     if s[i] == "*":
#         closed_bracket = tree(i+1, s, count-1)  # simulates s[i] == ")"
#         empty = tree(i+1, s, count)  # simulates s[i] == ""
#         open_bracket = tree(i+1, s, count+1)  # simulates s[i] == "("
#         return closed_bracket or empty or open_bracket

#     return tree(i+1, s, count)


# def checkValidString(s):
#     """
#     :type s: str
#     :rtype: bool
#     """
#     i = 0
#     count = 0
#     return tree(i, s, count)


def checkValidString(s):
    """
    :type s: str
    :rtype: bool
    """
    low_count = 0
    high_count = 0
    for i, char in enumerate(s):
        if char == "(":
            low_count += 1
            high_count += 1
        if char == ")":
            if low_count > 0:
                low_count -= 1
            high_count -= 1
        if char == "*":
            if low_count > 0:
                low_count -= 1
            high_count += 1
        if high_count < 0:
            return False

    return low_count == 0


if __name__ == "__main__":
    import time
    t1 = time.time()
    s = "(*)))"  # True
    # s = "*)**())"  # True "( ) ( ( ) ) "
    # s = "(*))"  # True "( ( ) )"
    # s = '(***)'
    # s = "*()"  # True "( )"
    # s = "(**((*())*"  # True "( ) ( ( ( ) ) )"

    # s = "(*)"  # True "( )"
    # s = "***)"  # True "( )" or "( ( ) )"
    # s = "()((()()))"
    # s = "(*())"  # True "( ( ) )"
    # s = "(**)"  # True "( )" or "( ) ( )"
    # s = "*)"  # True "( )"
    # s = "()((())())"
    s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(())\
)())((*()()(((()((()*(())*(()**)()(())"
    print(checkValidString(s))
    t2 = time.time()
    print(t2 - t1)
