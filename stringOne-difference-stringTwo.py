# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 23:40:14 2019

@author: John Oyegbite
"""
# SOLVED!
"""
Problem Description:
    Given two words, return all the characters that are in the first one 
    but not in the second one.
    
    sample inputs => expected output
    
    "abcdefg" "hzmp" => "abcdefg"
    
    "ab" "b" => "a"
    
    "bb" "b" => ""
    
    "a" "z" => "a"
"""

def difference(s1, s2):
    s1 = set(s1)
    s2 = set(s2)
    
    diff = ""
    for s in s1:
        if s not in s2:
            diff += s
    return diff

    return s1.difference(s2)


if __name__ == "__main__":
    s1 = "abcdefg"
    s2 = "hzmp"
    
    # s1 = "ab"
    # s2 = "b"
    
    # s1 = "bb"
    # s2 = "b"
    
    s1 = "a"
    s2 = "z"
    
    print(difference(s1, s2))
    

