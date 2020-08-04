# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 06:21:02 2020

@author: johnoyegbite
"""
# SOLVED!
"""
A prisoner died in cell 13, How can his corpse be taken out through cell 4
in such a way that it goes through every cell letting other inmates take a
glimpse. No inmate should see the corpse more than once.

[1]  [2]  [3]  [4 ->
[5]  [6]  [7]  [8]
[9]  [10] [11] [12]
[13] [14] [15] [16]

Use recursion.
There are eight solutions to the problem. Find them all.
One solution is [13, 9, 13, 14, 10, 6, 5, 1, 2, 3, 7, 11, 15, 16, 12, 8, 4]

"""


def dfs_visit(cell_coord, cell_end_coord, prison, visited, results, path):
    row, col = cell_coord
    visited[cell_coord] = True
    path.append(prison[row][col])

    cell_13_coord = (3, 0)
    # print(path)
    if cell_coord == cell_end_coord:
        # print()
        # print("--------------")
        if len(path) >= 16:
            # I had to make a copy because path is mutable object
            results.append(path[:])

    for r in range(-1, 2):
        for c in range(-1, 2):
            if r == c or r == -c:
                continue
            new_row, new_col = row + r, col + c
            if 0 <= new_row < len(prison) and 0 <= new_col < len(prison[0]):
                new_coord = new_row, new_col
                if new_coord not in visited or new_coord == cell_13_coord:
                    dfs_visit(new_coord, cell_end_coord,
                              prison, visited, results, path)

    path.pop()
    # we don't want to delete cell with 13 as its value because it would
    # always be there.
    if cell_coord != cell_13_coord:
        del visited[cell_coord]


def prison_dfs(prison):
    results = []
    cell_13_coord = (3, 0)
    cell_4_coord = (0, 3)
    visited = {cell_13_coord: True}
    dfs_visit(cell_13_coord, cell_4_coord, prison, visited, results, [])

    print(results)
    print()
    return len(results)


if __name__ == "__main__":
    prison = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    print(prison_dfs(prison))
