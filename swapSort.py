# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 01:23:43 2017

@author: Oyelson J
"""
# SOLVED!

def swapSort(L): # sort in increasing order
    print("Original L:", L)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                L[j], L[i] = L[i], L[j]
                print(L)
    return "Final L:", L
 
def swapSort1(L): # sort in decreasing order
    print("Original L:", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                L[j], L[i] = L[i], L[j]
                print(L)
    return "Final L:", L


L = [6, 4, 7, 29, 31, 3, 5, 2, 8, 1, 0, 23, 18]
# L = []
print(swapSort1(L))