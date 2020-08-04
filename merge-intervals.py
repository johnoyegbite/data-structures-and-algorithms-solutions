# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 00:16:31 2019

@author: USER
"""
# SOLVED!
"""
Problem Desciption:
    Given a collection of intervals, merge all overlapping intervals.

Example 1:
    Input: [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
    Input: [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""


def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merge = [intervals[0]]
    for interval in intervals:
        if merge[-1][1] < interval[0]:
            merge.append(interval)
        else:
            merge[-1][1] = max(merge[-1][1], interval[1])
    return merge


if __name__ == "__main__":
    intervals = [[8,10], [1,3], [15,18], [2,6]]

    intervals = [[1, 9], [2, 5], [19, 20], [10, 11],
                 [12, 20], [0, 1], [0, 3], [0, 2]]
    
    print(merge(intervals))
    
