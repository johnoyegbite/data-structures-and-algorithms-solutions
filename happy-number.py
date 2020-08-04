# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 17:19:07 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Write an algorithm to determine if a number is happy.

    A happy number is a number defined by the following process: 
        Starting with any positive integer, replace the number by the sum of 
        the squares of its digits, and repeat the process until the number 
        equals 1 (where it will stay), or it loops endlessly in a cycle which 
        does not include 1. 
        Those numbers for which this process ends in 1 are happy numbers.

Example 1:
    Input:19
    Output:true
    Explanation:
        19 is a happy number

        1^2 + 9^2 = 82
        8^2 + 2^2 = 68
        6^2 + 8^2 = 100
        1^2 + 0^2 + 0^2 = 1

Example 2:
    Input:5
    Output:false
    Explanation:
        5 is not a happy number
        
        25->29->85->89->145->42->20->4->16->37->58->89
        89 appears again.

"""


def isHappy(n):
    # write your code here
    seen = set()
    new_n = 0
    
    while n > 0:
        rem, n = n % 10, n//10
        new_n += rem**2
        if n == 0: # Done with a number and pick another new one
            if new_n == 1:
                return True
            if new_n in seen:
                return False
            seen.add(new_n)
            n = new_n
            new_n = 0
            
if __name__ == "__main__":
    n = 5
    print(isHappy(n))