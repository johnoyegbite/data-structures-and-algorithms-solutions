# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 19:14:56 2017

@author: Oyelson J
"""

def selSort(L):
     curr = 0
     global count
     while curr != len(L):
         for i in range(curr, len(L)):
             if L[curr] > L[i]:
                 L[curr], L[i] = L[i], L[curr]
             count += 1
         curr += 1
         count += 1
     return L
 
def selSort1(L):
    global count
    for i in range(len(L) - 1):                
        print(L)
        minIndx = i
        minVal = L[i]
        j = i + 1
        while j < len(L):
            count += 1
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        L[i], L[minIndx]= L[minIndx], L[i]
        count += 1
    return L
        
        
count = 0   
L = [6, 4, 7, 29, 31, 3, 5, 2, 8, 1, 0, 23, 18]
print(selSort(["Adebola", "Oyegbite", "Mayowa", "Toni", "Chizoba", "JOhn"]))
#print(selSort1(L))
print(count)