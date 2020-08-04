# -*- coding: utf-8 -*-
"""
Created on Wed May  6 18:38:04 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    In a N x N grid representing a field of cherries, each cell is one of three
    possible integers.

    0 means the cell is empty, so you can pass through;
    1 means the cell contains a cherry, that you can pick up and pass through;
    -1 means the cell contains a thorn that blocks your way.

    Your task is to collect maximum number of cherries possible by following
    the rules below:

        Starting at the position (0, 0) and reaching (N-1, N-1) by moving right
        or down through valid path cells (cells with value 0 or 1);
        After reaching (N-1, N-1), returning to (0, 0) by moving left or up
        through valid path cells;
        When passing through a path cell containing a cherry, you pick it up
        and the cell becomes an empty cell (0);
        If there is no valid path between (0, 0) and (N-1, N-1), then no
        cherries can be collected.

Example 1:
    Input: grid =
        [[0, 1, -1],
         [1, 0, -1],
         [1, 1,  1]]
    Output: 5
    Explanation:
        The player started at (0, 0) and went down, down, right right to reach
        (2, 2). 4 cherries were picked up during this single trip, and the
        matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
        Then, the player went left, up, up, left to return home, picking up one
        more cherry. The total number of cherries picked up is 5, and this is
        the maximum possible.

Note:
    grid is an N by N 2D array, with 1 <= N <= 50.
    Each grid[i][j] is an integer in the set {-1, 0, 1}.
    It is guaranteed that grid[0][0] and grid[N-1][N-1] are not -1.
"""


class Solution:
    def dfs(self, r1, c1, r2, c2, grid, N, memo):
        # if we have already calculated the maximum cherry of both pointer in
        # their respective cell (this is done by adding values in both pointer
        # cell and the maximum values returned by the two pointers),
        # just return its value to avoid overlapping subproblems.
        key = (r1, c1, r2, c2)
        if key in memo:
            return memo[key]

        # Base cases:

        # 1. if we meet an invalid coordinate
        if r1 > N-1 or c1 > N-1 or r2 > N-1 or c2 > N-1:
            return float("-inf")
        # 2. if we meet an obstacle in the grid
        #    (obstacle is having -1 in the cell)
        if grid[r1][c1] == -1 or grid[r2][c2] == -1:
            return float("-inf")
        # 3. if any of the pointers have reached the bottom right
        if r1 == N-1 and c1 == N-1:
            return grid[r1][c1]
        if r2 == N-1 and c2 == N-1:
            return grid[r2][c2]

        # Assign the maximum cherry for a particular cell
        max_cherries = 0
        # if both pointers are in the same cell, just count it once else
        # get the cherries from both pointers
        if r1 == r2 and c1 == c2:
            max_cherries = grid[r2][c2]
        else:
            max_cherries = grid[r1][c1] + grid[r2][c2]

        # Both pointers can take the maximum cherries by either
        # going in the same direction or going in different direction.
        # There are 4 possible movement combinations.
        # 1. Pointer 1 and 2 goes right
        # 2. Pointer 1 and 2 goes down
        # 3. Pointer 1 goes right and Pointer 2 goes down
        # 4. Pointer 1 goes down and Pointer 2 goes right
        p1_right_p2_down = self.dfs(r1, c1+1, r2+1, c2, grid, N, memo)
        p1_right_p2_right = self.dfs(r1, c1+1, r2, c2+1, grid, N, memo)
        p1_down_p2_down = self.dfs(r1+1, c1, r2+1, c2, grid, N, memo)
        p1_down_p2_right = self.dfs(r1+1, c1, r2, c2+1, grid, N, memo)

        # add to the existing cherry the maximum returned from both pointers
        max_cherries += max(p1_right_p2_down,
                            p1_right_p2_right,
                            p1_down_p2_down,
                            p1_down_p2_right
                            )

        memo[key] = max_cherries

        return memo[key]

    def cherryPickup(self, grid):
        """
        type grid: List[List[int]]
        rtype: int
        """
        # Using two pointers to pick up the maximum cherry
        memo = {}
        pointer_1_row = 0
        pointer_1_col = 0
        pointer_2_row = 0
        pointer_2_col = 0
        N = len(grid)
        maximum = self.dfs(pointer_1_row,
                           pointer_1_col,
                           pointer_2_row,
                           pointer_2_col,
                           grid, N, memo)
        return max(maximum, 0)
