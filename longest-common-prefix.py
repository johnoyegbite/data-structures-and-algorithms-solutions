# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:38:28 2020

@author: johnoyegbite
"""
# SOLVED!


def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not len(strs):
        return ""
    if len(strs) <= 1:
        return strs[-1]
    
    done = False
    major_prefix = ""
    longest = [major_prefix]
    for i in range(len(strs[0])):
        prefix = strs[0][i]
        for j in range(1, len(strs)):
            if i < len(strs[j]) and strs[j][i] == prefix and j < len(strs)-1:
                continue
            elif i < len(strs[j]) and strs[j][i] == prefix and j < len(strs):
                major_prefix += prefix
                longest.append(major_prefix)
            else: 
                major_prefix = ""
                done = True
                break
        if done:
            break
        
    return longest[-1]
                

if __name__ == "__main__":
    strs = ["flower", "flower", "flightwer", "fleewer", "floorwer"] # fl
    # strs = ["dog","racecar","car"] # ""
    strs = ['flower','glow','floor'] # ""
    # strs = ["aca","cba"] ""
    # strs = [] # ""
    # strs = ["race"] # "race"
    
    print(longestCommonPrefix(strs))


