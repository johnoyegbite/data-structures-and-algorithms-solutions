# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 20:29:41 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a collection of intervals, merge all overlapping intervals.

Example 1:
    Input: [(1,3)]
    Output: [(1,3)]

Example 2:
    Input:  [(1,3),(2,6),(8,10),(15,18)]
    Output: [(1,6),(8,10),(15,18)]

Challeng:
    O(n log n) time and O(1) extra space.
"""


"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

def sort_intervals(intervals):
    intervals_dict = {}
    
    # Store a tuple of (start, end) as keys and the corresponding objects as values
    for interval in intervals:
        key = interval.start, interval.end
        intervals_dict[key] = interval
        
    # Create list of all the keys 
    # (Remember to convert from tuple to list so it can be sorted)
    sorted_keys = [list(key) for key in intervals_dict]
    
    # Sort the list according to the first element
    sorted_keys.sort(key=lambda x: x[0])

    sorted_intervals = []
    # Create a list of sorted intervals using the sorted keys above
    for key in sorted_keys:
        sorted_intervals.append(intervals_dict[tuple(key)])
        
    return sorted_intervals
        

def merge(intervals):
    # write your code here
    if not intervals:
        return []
    
    intervals = sort_intervals(intervals)
    
    merged = [intervals[0]]
    for interval in intervals:
        
        if merged[-1].end < interval.start:
            merged.append(interval)
        else:
            merged[-1].end = max(merged[-1].end, interval.end)
            
    return merged