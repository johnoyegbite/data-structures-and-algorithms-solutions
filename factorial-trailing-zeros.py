# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 19:06:15 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given an integer n, return the number of trailing zeroes in n!.

Example1
    Input: n = 5
    Output: 1
    Explanation:
        1*2*3*4*5=120

Example2
    Input: n = 10
    Output: 2
    Explanation:
        1*2*3*4*5*6*7*8*9*10=3628800

Notice:
    Your solution should be in logarithmic time complexity.
    
"""

"""
Through research, the total number of trailing zeroes is the sum of the
geometric series:
    n/5^1 + n/5^2 + n/5^3 + ... + n/5^x
    
    where x is the power of 5 such that 5^x <= n.
    i.e. if n = 15 => x = 1
         if n = 25 => x = 2
         if n = 30 => x = 2
    
"""


def trailingZeroes(n):
    # write your code here
    n_per_fives = 0
    five_power = 1
    while (n // 5**five_power) > 0:
        n_per_fives += (n // 5**five_power)
        five_power += 1
        
    return n_per_fives


if __name__ == "__main__":
    n = 454543
    print(trailingZeroes(n))