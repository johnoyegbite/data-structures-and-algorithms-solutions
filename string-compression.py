# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 23:54:51 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Implement a method to perform basic string compression using the counts of 
    repeated characters. For example, the string aabcccccaaa would become a2b1c5a3.

    If the "compressed" string would not become smaller than the original string,
    your method should return the original string.

    You can assume the string has only upper and lower case letters (a-z).

Example 1:
    Input: str = "aabcccccaaa"
    Output: "a2b1c5a3"

Example 2:
    Input: str = "aabbcc"
    Output: "aabbcc"
"""


def compress(originalString):
    # write your code here
    if not len(originalString):
        return ""
    
    new_string = ""
    
    prev_char = originalString[0]
    count = 1
    
    for i in range(1, len(originalString)):
        curr_char = originalString[i]
        if curr_char == prev_char:
            count += 1
        else:
            new_string += prev_char + str(count)
            prev_char = curr_char
            count = 1
    new_string += prev_char + str(count)
    
    if len(new_string) < len(originalString):
        return new_string
    else:
        return originalString


if __name__ == "__main__":
    originalString = "aabcccccaaa"
    # originalString = ""
    
    print(compress(originalString))