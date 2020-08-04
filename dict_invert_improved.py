# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 23:04:07 2017

@author: Oyelson J
"""
# SOLVED!


def dict_invert(d):
    '''
    d: a dictionary with immutables values
    returns: the inverse of the dictionary
            (The inverse of d is another dictionary whose keys are the unique dictionary values in d.
             The value for a key in the inverse dictionary is a sorted list of all keys in d that have the same value in d)
            if d = {1: 10, 6: True, 2: 20, 5: 30, 8: True, 3: 20, 7: True, 4: 30}
               d_invert = {10: [1], True: [6, 7, 8], 20: [2, 3], 30: [4, 5]}
    '''
    d_invert = {}
    for key in d:
        value = d[key]
        d_invert[value] = [key] if value not in d_invert else sorted(d_invert[value] + [key])
    return d_invert
        
dic = {1: 10, 6: True, 2: 20, 5: 30, 8: True, 3: 20, 7: True, 4: 30}
#dic = {4: True, 2: True, 0: True}

if __name__ == "__main__":
    print(dict_invert(dic))
