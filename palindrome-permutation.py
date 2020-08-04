# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 11:07:41 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a string, determine if a permutation of the string could form a palindrome.

Example1
    Input: s = "code"
    Output: False
    Explanation: 
        No solution

Example2
    Input: s = "aab"
    Output: True
    Explanation: 
        "aab" --> "aba"

Example3
    Input: s = "carerac"
    Output: True
    Explanation: 
        "carerac" --> "carerac"
"""
def can_permute_palindrome(s):
    # write your code here
    """
    for a string to be a palindrome, the occurrence of each character must be 
    EVEN when the length of the string is EVEN and if the length of the 
    string is odd, at most one character occurrence is permitted to be odd.
    """
    s_freq = {}
    
    count_odd = 0
    
    for char in s:
        if char in s_freq:
            s_freq[char] += 1
            if s_freq[char] % 2 == 0:
                count_odd -= 1
            else:
                count_odd += 1
        else:
            s_freq[char] = 1
            count_odd += 1
            
    return count_odd <= 1


if __name__ == "__main__":
    s = "llamam"
    print(can_permute_palindrome(s))