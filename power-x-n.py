# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 15:44:42 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:
    Input: 2.00000, 10
    Output: 1024.00000

Example 2:
    Input: 2.10000, 3
    Output: 9.26100

Example 3:
    Input: 2.00000, -2
    Output: 0.25000
    Explanation: 2-2 = 1/22 = 1/4 = 0.25

Note:
    -100.0 < x < 100.0
    n is a 32-bit signed integer, within the range [−231, 231 − 1]
"""

"""
SOLUTION: 
    1. x = 3, n = 8 => x^n = 3^8 (Power is even)


                              3^8
              3^4              x              3^4
      3^2      x      3^2      x      3^2      x      3^2
  3^1  x  3^1  x  3^1  x  3^1  x  3^1  x  3^1  x  3^1  x  3^1
  
  
    2. x = 3, n = 7 => x^n = 3^7 (Power is odd)


                              3^7
              3^3              x              3^4
      3^1      x      3^2      x      3^2      x      3^2
                  3^1  x  3^1  x  3^1  x  3^1  x  3^1  x  3^1
"""
def pow_recur(x, n, memo):
    if n == 1:
        return x
    if n in memo:
        return memo[n]
    left_pow = n//2
    rigth_pow = n - left_pow
    ans = pow_recur(x, left_pow, memo) * pow_recur(x, rigth_pow, memo)
    memo[n] = ans
    return ans

def my_pow(x, n):
    if n == 0: 
        return 1
    
    if n < 0:
        return 1 / pow_recur(x, -n, {})
    return pow_recur(x, n, {})


if __name__ == "__main__":
    x = 3
    n = 8
    
    x = 2.00000
    n = -2147483648
    print(my_pow(x, n))