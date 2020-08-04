# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:15:15 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given an array S of n integers, are there elements a, b, c in S such that
    a + b + c = 0?
    Find all unique triplets in the array which gives the sum of zero.

Example 1:
    Input:[2,7,11,15]
    Output:[]

Example 2:
    Input:[-1,0,1,2,-1,-4]
    Output:	[[-1, 0, 1],[-1, -1, 2]]

Notice:
    Elements in a triplet (a,b,c) must be in non-descending order.
    (ie, a ≤ b ≤ c)

The solution set must not contain duplicate triplets.
"""


def twoSum(numbers, target, target_idx):
    """
    type numbers: List[int]
    type target: int
    type target_idx: int
    rtype : List[List[int]]
    """
    two_sum_help = set()
    two_sum = []
    compliment_dict = {}
    for i in range(len(numbers)):
        if i != target_idx:  # Neglect the target idx
            num = numbers[i]
            compliment = - target - num
            if compliment in compliment_dict:
                if (compliment, num, target) not in two_sum_help:
                    two_sum_help.add((compliment, num, target))
                    two_sum.append(sorted([compliment, num, target]))
            else:
                compliment_dict[num] = i
    return two_sum


def threeSum(self, numbers):
    """
    type numbers: List[int]
    Give an array numbers of n integer
    rtype : List[List[int]],
    Find all unique triplets in the array which gives the sum of zero.
    """
    triplets_help = []
    if not len(numbers) or numbers[-1] < 0:
        return triplets_help

    # sort so as to loop only through the negative numbers and zeros
    numbers.sort()
    for i, num in enumerate(numbers):
        # Since all the triplets must have at least one
        # negative number or [0, 0, 0],
        # Just loop through only the non-negative numbers and zeros
        if num > 0:
            break
        # for a particular num (a), find the corresponding b and c such that
        # a + b + c = 0
        # The index is also passed as an argument so as not to consider the
        # number in the function "twoSum()"
        triplet = tuple(twoSum(numbers, num, i))
        triplets_help.extend(triplet)

    triplet_set = set()
    triplets = []
    # Remove duplicate from "triplets_help"
    for triplet in triplets_help:
        if tuple(triplet) not in triplet_set:
            triplet_set.add(tuple(triplet))
            triplets.append(triplet)

    return triplets
