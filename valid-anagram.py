# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 09:15:28 2019

@author: John Oyegbite
"""
# SOLVED!
"""
Problem:
    Given two strings s and t , write a function to determine if t is an anagram of s.
    
Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true
    
Example 2:
    Input: s = "rat", t = "car"
    Output: false
    
Note:
    You may assume the string contains only lowercase alphabets.

Follow up:
    What if the inputs contain unicode characters? 
    How would you adapt your solution to such case?
"""

def isAnagram(s:str, t:str)->bool:
    """
    :type s: str
    :type t: str
    :rtype: bool
                    s = "an!%agram"
                    t = "n#agara*m"
    """
    if len(s) != len(t):
        return False
    return sorted(list(s)) == sorted(list(t))
    

if __name__ == "__main__":
    # s = "an!%agram"
    # t = "n#agara*m"
    s = "a"
    t = "b"
    print(isAnagram(s, t))