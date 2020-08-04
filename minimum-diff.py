# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 14:06:59 2019

@author: USER
"""
# SOLVED!
"""
l => 61, 111, 71, 59, 
minimum difference is 2 and its the difference between 59 and 61



l sorted => 59, 61, 71, 93, 111
        
min_diff = None

59-61 = 2 -> min_diff

61-71 = 10

71-93 = 22

93-111 = 18

"""

def minium_diff(l):
    l = sorted(l)
    min_diff = None
    for i in range(len(l)):
        if i == len(l)-1:
            break
        curr = l[i]
        next_ = l[i+1] 
        diff = abs(curr - next_)
        min_diff = min(min_diff, diff) if min_diff else diff
    return min_diff


if __name__ == "__main__":
    l = [59, 61, 71, 93, 111]
    print(minium_diff(l))