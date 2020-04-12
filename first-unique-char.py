# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 23:54:44 2019

@author: USER
"""
# SOLVED!

# Method 1
# from collections import OrderedDict
# def first_unique_char(string):
#     string_dict = OrderedDict()
    
#     for s in string.lower():
#         if s != " ":
#             string_dict[s] = string_dict.get(s, 0) + 1
            
#     for k in string_dict:
#         if string_dict[k] == 1:
#             return k.lower()
  
  
# Method 2
# def first_unique_char(s):
#   char_dict = {}
#   for i, char in enumerate(s):
#     if char not in char_dict:
#       char_dict[char] = [1, i]
#     else:
#       char_dict[char][0] += 1
  
#   min_unique_idx = len(s)
#   for char in char_dict:
#     freq, idx = char_dict[char]
#     if freq < 2:
#       min_unique_idx = min(min_unique_idx, idx)
      
#   if min_unique_idx == len(s):
#     return -1
#   return min_unique_idx


# Method 3
def first_unique_char(s):
    char_dict = {}
    for char in s:
        char_dict[char] = char_dict.get(char, 0) + 1
    
    min_unique_idx = len(s)
    for i, char in enumerate(s):
        if char_dict[char] == 1:
            min_unique_idx = i
            break # Seen, so stop early
        
    if min_unique_idx == len(s): # if no unique character
        return -1
    return min_unique_idx
  
if __name__ == "__main__":
    string = "racecars"
    string = "blloommbeerrgg"
    print(first_unique_char(string))