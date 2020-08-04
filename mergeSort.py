# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 00:49:29 2017

@author: Oyelson J
"""


def merge(left, right):
    '''
    left, right: sorted list of integers
    return     : list of left and right in a sorted conditions
    '''
    res = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1

    return res


# insertion-sort time is 0.2*n^2 microseconds
# merge-sort     time is 2.2*n*log(n) microseconds
def merge_sort(L):
    global count
    count += 1
#    print(L)
#    print("Lenght of L is: " + str(len(L)))
    if len(L) < 2:
        return L[:]

    half = len(L) // 2  # log n complexity
    left = merge_sort(L[:half])  # n*log n complexity
    right = merge_sort(L[half:])
#    print(merge(left, right))
    return merge(left, right)


if __name__ == "__main__":
    count = 0
    print(merge_sort(["Unilag", "Oyegbite", "Python",
                      "Civil", "JetO", "JOhn"]))
    print(merge_sort([6, 4, 7, 29, 31, 3, 5, 2, 8, 1, 0, 23, 18]))
    print("Total no of function call is:", count)
