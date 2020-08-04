# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 21:45:05 2019

@author: USER
"""
# SOLVED!


def flatten(l):
    d=[]
    for e in l:
        if hasattr(e, '__iter__'):
            d.extend(flatten(e))
        else:
            d.append(e)
    return d

l = [1, 4, [44, [22, [10, [0], 3, 7]], 2], 5, [6]]
print(flatten(l))