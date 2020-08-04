# -*- coding: utf-8 -*-
"""
Created on Sat May  9 11:59:59 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a positive integer num, write a function which returns
    True if num is a perfect square else False.

    Note: Do not use any built-in library function such as sqrt.

Example 1:
    Input: 16
    Output: true

Example 2:
    Input: 14
    Output: false
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num in (0, 1):
            return True

        guess = num/2
        epsilon = 0.01
        count = 0
        while abs(guess**2 - num) >= epsilon:
            guess = guess - ((guess**2 - num)/(2*guess))
            count += 1

        print("No. of Guesses: {}".format(count))
        print("Guess: {}".format(guess))
        return int(guess)**2 == num


if __name__ == "__main__":
    s = Solution()
    num = 14798678562
    num = 15763530163289
    num = 16
    print(s.isPerfectSquare(num))
