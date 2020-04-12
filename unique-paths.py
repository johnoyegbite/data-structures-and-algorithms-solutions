# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 18:58:08 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem: let s rep start and f represent finish
    A robot is located at the top-left corner of a m x n grid 
    (marked 'Start' in the diagram below).
    
    [s][ ][ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ][ ][ ]
    [ ][ ][ ][ ][ ][ ][f]

    The robot can only move either down or right at any point in time. 
    The robot is trying to reach the bottom-right corner of the grid 
    (marked 'Finish' in the diagram below).

    How many possible unique paths are there?

    Above is a 7 x 3 grid. How many possible unique paths are there?

    Note: m and n will be at most 100.

Example 1:
    Input: m = 3, n = 2
    [s][ ][ ]
    [ ][ ][f]
    Output: 3
    Explanation:
        [s][-][-]
        [ ][ ][f]
        
        [s][-][ ]
        [ ][-][f]
        
        [s][ ][ ]
        [-][-][f]
        From the top-left corner, there are a total of 3 ways to reach the 
        bottom-right corner:
            1. Right -> Right -> Down
            2. Right -> Down -> Right
            3. Down -> Right -> Right
Example 2:
    Input: m = 7, n = 3
    Output: 28

"""

# EXPLANATION
"""
    Say we have n = 2 and m = 3,
    
    This problem can be simulated as binary tree (do this or that).
    
    1st interpretation:
        Starting from the top-left corner, we have two options: 
            1. move right or 2. move down. 
            Hence you start at (0, 0) and end at (1, 2).
            Note:
                You will always end at one(1) less in both direction i.e (2-1, 3-1), 
                
                n=2, m=3
                         m
                |(0,0)|(0,1)|(0,2)|
              n -------------------      n x m grid
                |(1,0)|(1,1)|(1,2)|
                
                so you can't end at (2, 3)
    
    2nd interpretation:
        Starting from the bottom-right, we have two options:
            1. move up or 2. move left.
            Hence you start at (1, 2) and end at (0, 0)
    
    I will work with the 2nd interpretation.
    
    So using the 2nd interpretation:
        if you are at a coordinate say (1, 2), 
        To determine:
            1. upper coordinate:
                --> subtract (1, 0) from that coordinate => (1-1, 2-0) = (0, 2)
            2. left coordinate:
                --> subtract (0, 1) from that coordinate => (1-0, 2-1) = (1, 1)
    
    Let IP rep Invalid path
    Let VP rep Valid path
    
    By exploring the 2 options: either to move up or right, we must reach a base
    case which is when we reach an IP or VP:
        1. When we reach a VP, we reach is a vailid path hence return 1
        2. When we reach an IP, we reach an invalid path hence return 0
        
    Also notice that we have some overlapping subproblems (some coordinate
    repeats at a point), hence we can use Dynamic programming to achieve 
    speed of computation.

                                               n, m
                                              (2, 3)
                                                 |
                                             (n-1, m-1)
                                                 |
                                              (1, 2)
                                       -(1, 0)/    \-(0, 1)
                                             /      \
                     (0, 2)                                          (1, 1)
             -(1, 0) /    \-(0, 1)                           -(1, 0)/      \-(0, 1)
                    /      \                                       /        \
          (-1, 2)              (0, 1)                 (0, 1)                       (1, 0)
             IP       - (1, 0) /    \-(0, 1)  -(1, 0) /    \-(0, 1)         -(1, 0) /    \-(0, 1)
                              /      \               /      \                      /      \
                        (-1, 1)       (0, 0)   (-1, 1)       (0, 0)          (0, 0)       (0, -1)
                           IP            VP       IP            VP             VP            IP
   
    We have 3 VP in total which is our answer.

"""
def dfs_normal(n, m):
    if n == 0 and m == 0:
        return 1
    if n < 0 or m < 0:
        return 0
    return dfs_normal(n-1, m-0) + dfs_normal(n-0, m-1)
    
def dfs_DP(n, m, memo={}):
    if n == 0 and m == 0:
        return 1
    if n < 0 or m < 0:
        return 0
    if (n, m) in memo:
        return memo[(n, m)]
    memo[(n, m)] = dfs_DP(n-1, m-0) + dfs_DP(n-0, m-1)
    return memo[(n, m)]
    
def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    return dfs_DP(n-1, m-1)


if __name__ == "__main__":
    m = 7 # column
    n = 3 # row
    
    # m = 3 # column
    # n = 2 # row
    
    # m = 23 # column
    # n = 12 # row
    
    # m = 15
    # n = 10
    print(uniquePaths(m, n))