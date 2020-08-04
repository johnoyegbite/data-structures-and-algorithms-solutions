# -*- coding: utf-8 -*-
"""
Created on Fri May  1 12:47:57 2020

@author: johnoyegbite
"""

"""
Problem:
    You are a product manager and currently leading a team to develop a new
    product.
    Unfortunately, the latest version of your product fails the quality check.
    Since each version is developed based on the previous version, all the
    versions after a bad version are also bad.

    Suppose you have n versions [1, 2, ..., n] and you want to find out the
    first bad one, which causes all the following ones to be bad.

    You are given an API bool isBadVersion(version) which will return whether
    version is bad. Implement a function to find the first bad version.
    You should minimize the number of calls to the API.

Example:
    Given n = 5, and version = 4 is the first bad version.

    call isBadVersion(3) -> false
    call isBadVersion(5) -> true
    call isBadVersion(4) -> true

    Then 4 is the first bad version.
"""


# This is to simulate the isBadVersion API
def isBadVersion(bad):
    global n
    return n >= bad


def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    """
    :type n: int
    :rtype: int
    """
    start = 1
    end = n
    mid = (start + end)//2
    is_last_bad = isBadVersion(mid)

    while start <= end:
        mid = (start + end)//2
        is_last_bad = isBadVersion(mid)
        if is_last_bad:
            end = mid - 1
        else:
            start = mid + 1

    # if the last call is not bad then the next would surely be bad (bad ass)
    return mid if is_last_bad else mid + 1


if __name__ == "__main__":
    n = 3
    bad = 1
    print(firstBadVersion(n))
