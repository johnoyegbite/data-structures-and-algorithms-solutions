# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 01:25:08 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
    Input: 123
    Output: 321

Example 2:
    Input: -123
    Output: -321

Example 3:
    Input: 120
    Output: 21
"""
def reverse(n):
    """
    :type x: int
    :rtype: int
    """
    is_neg = n < 0

    reverse_int = 0
    n = abs(n)      
    
    while n > 0:
        rem, n = n % 10, n // 10
        reverse_int = reverse_int * 10 + rem
    
    if reverse_int > 2**31-1: # check if "reversed_int" is 32-bit signed return 0 if not
        return 0
    if is_neg:
        return -reverse_int
    return reverse_int
    

if __name__ == "__main__":
    n = 123 # 321
    n = -123 # -321
    n = 120 # 21
    # n = 0
    # n = 1534236469 # 0

print(reverse(n))