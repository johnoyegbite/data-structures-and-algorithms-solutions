# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 01:33:18 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a string, sort the string with the first keyword which is the most 
    commonly used characters and the second keyword which is the dictionary order.

Example1
    Input:  s = "bloomberg"
    Output: "bbooeglmr"
    Explanation:
        'b' and 'o' appear the most frequently, but the dictionary sequence of 'b' is the smaller than 'o', so 'b' is ranked first, followed by 'o', and so on.

Example2
    Input:  s = "lintcode"
    Output: "cdeilnot"
    Explanation:
        All characters appear the same number of times, so directly in accordance with the dictionary order.

Notice:
    The length of string is less than 10000.
    All characters are lowercase

"""

def get_char_freq(s):
    char_freq = {}
    for char in s:
        char_freq[char] = char_freq.get(char, 0) + 1
    return char_freq
    
def get_chars_best(char_freq, best):
    best_chars = []
    for char in char_freq:
        if char_freq[char] == best:
            best_chars.extend(list(char*best))
            char_freq[char] = 0 # mark character frequency as "0" to denote visited
    best_chars.sort()
    return best_chars
    
"""
@param s: the string that needs to be sorted
@return: sorted string
"""
def stringSort(s):
    # Write your code here
    char_freq = get_char_freq(s)
    
    sorted_list = []
    
    while len(sorted_list) < len(s):
        best = max(char_freq.values())
        if best != 0: # make sure the frequency is '1' or greater
            sorted_list.extend(get_chars_best(char_freq, best))
            
    return ''.join(sorted_list)