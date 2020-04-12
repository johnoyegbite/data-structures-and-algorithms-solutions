# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 12:03:12 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    You are climbing a stair case. It takes n steps to reach to the top.

    Each time you can either climb 1 or 2 steps. 

    In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer
  
  if n=4, we have
  1 + 1 + 1 + 1
  2 + 2
  1 + 2 + 1
  1 + 1 + 2
  2 + 1 + 1
  
  Tree visiualization for n=3:
  n = 3: 


                      3
                    /   \
                  1        2
                /   \    /   \
               0    -1  1     0
                       / \  
                      0  -1
  Tree visiualization for n=3:
  n = 4: 
            
                              4
                      /              \
                     3                2
                    /   \           /    \
                  1        2       1       0
                /   \    /   \    /  \
               0    -1  1     0  0    -1
                       / \  
                      0  -1
                      
    when the leaf node is 0 (that is a valid path), so return 1
    when the lead node is -1 (negative) (the path is not valid), so return 0
  							  
"""

                
def climb_stair(n, memo={}):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if n in memo:
        return memo[n]
    num_of_path = climb_stair(n-1, memo) + climb_stair(n-2, memo)
    memo[n] = num_of_path
    return num_of_path


if __name__ == "__main__":
    n = 1
    print(climb_stair(n))