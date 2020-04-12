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


# METHOD 1
def dfs_visit(cell_coord, cell_end_coord, prison, visited, results, path):
    x, y = cell_coord
    visited[cell_coord] = True
    path.append(prison[x][y])

    cell_13_coord = (3, 0)
    if cell_coord == cell_end_coord:
        if len(path) >= 16:
            # I had to make a copy because path is mutable object
            results.append(path[:])

    row_max, col_max = len(prison), len(prison[0])
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j or i == -j:
                continue
            x_n, y_n = x + i, y + j
            if 0 <= x_n < row_max and 0 <= y_n < col_max:
                new_coord = x_n, y_n
                if new_coord not in visited or new_coord == cell_13_coord:
                    dfs_visit(new_coord, cell_end_coord,
                              prison, visited, results, path)

    path.pop()
    try:  # cell (3, 0) would raise a KeyError when backtracking.
        del visited[cell_coord]
    except KeyError:
        return


def prison_dfs(prison):
    results = []
    cell_13_coord = (3, 0)
    cell_4_coord = (0, 3)
    visited = {cell_13_coord: True}

    dfs_visit(cell_13_coord, cell_4_coord, prison, visited, results, [])
    print(results)
    return len(results)

# METHOD 2
# def dfs_visit(start, end, graph, visited, results, path):
#     visited.add(start)
#     path.append(start)

#     if start == end:
#         if len(path) >= 16:
            # I had to tuple it because path is mutable object
#            results.append(tuple(path))

#     for children in graph[start]:
#         if children not in visited or children == 13:
#             dfs_visit(children, end, graph, visited, results, path)

    # path.pop()
    # try:
    #     visited.remove(start)
    # except KeyError:
    #     return


# def prison_dfs(prison):
#     graph = {1: [2, 5], 2: [1, 3, 6], 3: [2, 4, 7], 4: [3, 8],
#               5: [1, 6, 9], 6: [2, 5, 7, 10], 7: [3, 6, 8, 11],
#               8: [4, 7, 12], 9: [5, 10, 13], 10:[6, 9, 14, 11],
#               11: [7, 10, 12, 15], 12: [8, 11, 16], 13: [9, 14],
#               14: [10, 13, 15], 15: [11, 14, 16], 16: [12, 15]
#     }
#     results = []
#     cell_13, cell_4 = 13, 4
#     visited = set()
#     dfs_visit(cell_13, cell_4, graph, visited, results, [])
    # print(results)
    # return len(results)


if __name__ == "__main__":
    prison = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
        ]
    
    print(prison_dfs(prison))
