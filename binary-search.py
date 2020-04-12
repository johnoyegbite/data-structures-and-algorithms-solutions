# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 14:41:12 2019

@author: USER
"""
# SOLVED!
"""
1, 2, 3, 4, 5, 6, 7
"""


def binary_search(l, num):
    start = 0
    end = len(l)-1
    
    while start < end:
        mid = (end + start)//2
        if l[mid] == num:
            return True
        elif num > l[mid]:
            start = mid+1
        else:
            end = mid
    
    return False


def binary_recur(l, num):
    half = len(l) // 2
    if len(l) == 1 and l[half] != num:
        return False
    elif l[half]==num:
        return True
    else:
        left = l[:half]
        right = l[half:]
        return binary_recur(left, num) or binary_recur(right, num)

if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 6, 7, 9]
    # print(binary_recur(l, 10))
    print(binary_search(l, -7))