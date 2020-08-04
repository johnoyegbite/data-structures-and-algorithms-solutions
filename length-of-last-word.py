# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 23:13:09 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a string s consists of upper/lower-case alphabets and empty space 
    characters ' ', return the length of last word 
    (last word means the last appearing word if we loop from left to right) 
    in the string.

    If the last word does not exist, return 0.

Note: 
    A word is defined as a maximal substring consisting of non-space characters only.

Example:
    Input: "Hello World"
    Output: 5
"""


def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    i = len(s) - 1 # start indexing from the end of the string

    # Check to see if there are spaces at the end of the string.
    # if there are spaces, move index (i) to the position of the first 
    # occurrence of a non-space character from the end of the string.
    while i >= 0:
        if s[i] == " ":
            i -= 1
        else:
            break
            
    # From the first occurence of a non-space character from the end of the 
    # string, number of characters upto the point of space occurence.
    # if there is no space occurrence and i = 0, this implies the string 
    # just contain a word.
    word_len = 0
    while i >= 0:
        if s[i] == " ":
            return word_len
        else:
            word_len += 1
        i -= 1
    
    return word_len


if __name__ == "__main__":
    s = "Hello World"
    s= "I am a boy      "
    print(lengthOfLastWord(s))
    