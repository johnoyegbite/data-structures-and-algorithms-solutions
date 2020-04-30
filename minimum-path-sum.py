# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 18:47:58 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a m x n grid filled with non-negative numbers, 
    find a path from top left to bottom right which minimizes the sum of all
    numbers along its path.

    Note: You can only move either down or right at any point in time.

Example:
    Input:
        [
            [1,3,1],
            [1,5,1],
            [4,2,1]
        ]
    Output: 7
    Explanation: Because the path 1→3→1→1→1 minimizes the sum.

"""
"""
Solution:
    It can be reduced to the problem statement below.

    Check the "Unique Paths" problem!

"""


class Solution(object):
    def binary_tree_DP(self, n, m, grid, memo):
        if n == 0 and m == 0:
            return grid[n][m]
        if n < 0 or m < 0:
            return float("inf")
        if (n, m) in memo:
            return memo[(n, m)]

        upper = self.binary_tree_DP(n-1, m-0, grid, memo)
        left = self.binary_tree_DP(n-0, m-1, grid, memo)

        memo[(n, m)] = min(upper, left) + grid[n][m]

        return memo[(n, m)]

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not len(grid):
            return 0
        n = len(grid)
        m = len(grid[0])
        memo = {}
        min_sum = self.binary_tree_DP(n-1, m-1, grid, memo)
        return min_sum


if __name__ == "__main__":
    grid = [
            [1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]
    ]

    grid = [
        [1, 2],
        [1, 1]
    ]
    s = Solution()
    print(s.minPathSum(grid))
