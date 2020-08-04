# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 01:50:54 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Implement atoi which converts a string to an integer.

    The function first discards as many whitespace characters as necessary 
    until the first non-whitespace character is found. 
    Then, starting from this character, takes an optional initial plus or minus
    sign followed by as many numerical digits as possible, and interprets them
    as a numerical value.
    
    The string can contain additional characters after those that form the 
    integral number, which are ignored and have no effect on the behavior of 
    this function.
    
    If the first sequence of non-whitespace characters in str is not a valid 
    integral number, or if no such sequence exists because either str is empty
    or it contains only whitespace characters, no conversion is performed.
    
    If no valid conversion could be performed, a zero value is returned.
    
    Note:
    
    Only the space character ' ' is considered as whitespace character.
    Assume we are dealing with an environment which could only store integers 
    within the 32-bit signed integer range: [−2**31,  2**31 − 1]. If the numerical
    value is out of the range of representable values, 
    INT_MAX (2**31 − 1) or INT_MIN (−2**31) is returned.

Example 1:
    Input: "42"
    Output: 42

Example 2:
    Input: "   -42"
    Output: -42
    Explanation: The first non-whitespace character is '-', which is the minus sign.
                 Then take as many numerical digits as possible, which gets 42.

Example 3:
    Input: "4193 with words"
    Output: 4193
    Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Example 4:
    Input: "words and 987"
    Output: 0
    Explanation: The first non-whitespace character is 'w', which is not a numerical 
                 digit or a +/- sign. Therefore no valid conversion could be performed.
Example 5:
    Input: "-91283472332"
    Output: -2147483648
    Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
                 Thefore INT_MIN (−231) is returned.
"""

def myAtoi(s):
    """
    :type str: str
    :rtype: int
    """
    s = s.lstrip()
    if len(s) < 1:
        return 0

    # Perform operation if s begins with a '-', '+' or a digit
    if s[0].isdigit() or s[0] == "-" or s[0] == "+":
        # Get all the starting valid digits 'x'
        x = s[0]
        for i in range(1, len(s)):
            if s[i].isdigit():
                x += s[i]
            else:
                break
        # If the starting valid digits is just '-' or '+' then return 0
        if x == "-" or x == "+":
            return 0
        x = int(x)
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if x < INT_MIN: return INT_MIN
        if x > INT_MAX: return INT_MAX
        return x

    return 0


if __name__ == "__main__":
    s = "42" # 42
    # s = "    -42" # 42
    # s = "-4193 with words" # 4193
    # s = "words and 987" # 0
    # s = ""
    # s = "5"
    # s = "-91283472332"
    
    print(myAtoi(s))
    