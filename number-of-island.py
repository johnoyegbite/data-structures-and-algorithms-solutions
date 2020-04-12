# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 21:39:46 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a 2d grid map of '1's (land) and '0's (water), count the
    number of islands.
    An island is surrounded by water and is formed by connecting adjacent
    lands horizontally or vertically. You may assume all four edges of the
    grid are all surrounded by water.

Example 1:
    Input:
        11110
        11010
        11000
        00000

    Output: 1

Example 2:
    Input:
        11000
        11000
        00100
        00011

    Output: 3
"""


def dfs_visit(cell, grid):
    x, y = cell

    if grid[x][y] == "0":
        return

    grid[x][y] = "0"

    for i in range(-1, 2):
        for j in range(-1, 2):
            # neglects the diagonal cells and the cell itself
            if i == j or i == -j:
                continue
            x_n, y_n = x + i, y + j
            # ensures valid cell
            if 0 <= x_n < len(grid) and 0 <= y_n < len(grid[0]):
                new_cell = (x_n, y_n)
                dfs_visit(new_cell, grid)


def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    if not len(grid):
        return 0

    row_count = len(grid)
    col_count = len(grid[0])

    num_island = 0
    for x in range(row_count):
        for y in range(col_count):
            cell = (x, y)
            if grid[x][y] == "1":
                num_island += 1
                dfs_visit(cell, grid)

    return num_island


if __name__ == "__main__":
    grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
            ]
    
    grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
            ]
    print(numIslands(grid))
