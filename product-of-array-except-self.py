# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 23:33:55 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given an array nums of n integers where n > 1,
    return an array output such that output[i] is equal to the product of all
    the elements of nums except nums[i].

Example:
    Input:  [1,2,3,4]
    Output: [24,12,8,6]

    Constraint: It's guaranteed that the product of the elements of any prefix
    or suffix of the array (including the whole array) fits in a 32 bit integer

Note: Please solve it without division and in O(n).

Follow up:
    Could you solve it with constant space complexity?
    (The output array does not count as extra space for the purpose of space
    complexity analysis.)
"""
import math


def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    product = 1
    num_of_zeros = 0
    zero_idx = -1
    output = []

    for i, num in enumerate(nums):
        if num == 0:
            num_of_zeros += 1
            zero_idx = i
        if num != 0:
            product *= num

    # 1. if there are more than one zeros in the list,
    #    then automatically, for every number the product
    #    of other numbers would be zero since other numbers
    #    would contain at least one zero.
    if num_of_zeros > 1:
        return [0]*len(nums)

    # 2. if we have only one zero, then for every other
    #    number apart from the zero itself, would have a product
    #    equal to zero. The zero itself would have a product of
    #    other numbers.
    #    Else: replace every number with the product of other numbers
    if num_of_zeros == 1:
        output = [0]*len(nums)
        output[zero_idx] = product
    else:
        for i in range(len(nums)):
            num = nums[i]  # just for default assignment of num
            # num (number to replace)
            # Default is num = product // nums[i]. But we don't want to use the
            # division operator.
            # Hence, let product = x and nums[i] = y
            # num = x / y
            # x / y == x * (1 / y)
            # but 1 / y = y^(-1)
            # take log base 10 of both sides; let log10 = ln
            # ln(1/y) = ln(y^(-1))
            # 1/y = 10^ln(y^(-1))
            # 1/y = 10^(-ln(y))
            # or 1/y = (-1) * 10^(-ln(-y)) if y is negative,
            # since 1/(-y) = (-1) * (1/y) with y positive in the log function.
            # Hence x/y = x * 10^(-ln(y)) or
            #     or x/y = x * (-1) * 10^(-ln(-y)) if y is negative
            # Notice how we didn't use the division operator.
            if nums[i] < 0:
                num = int(round(-product * 10**((-1)*math.log10(-1*nums[i]))))
            else:
                num = int(round(product * 10**((-1)*math.log10(nums[i]))))
            output.append(num)

    return output


nums = [1, 2, 3, 4]
print(productExceptSelf(nums))
