# -*- coding: utf-8 -*-
"""
Created on Mon May 11 12:13:25 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    An image is represented by a 2-D array of integers, each integer
    representing the pixel value of the image (from 0 to 65535).

    Given a coordinate (sr, sc) representing the starting pixel
    (row and column) of the flood fill, and a pixel value newColor,
    "flood fill" the image.

    To perform a "flood fill", consider the starting pixel, plus any pixels
    connected 4-directionally to the starting pixel of the same color as the
    starting pixel, plus any pixels connected 4-directionally to those pixels
    (also with the same color as the starting pixel), and so on.
    Replace the color of all of the aforementioned pixels with the newColor.

    At the end, return the modified image.

    ###
    sr = 1 | sc = 1 | newColor = 2
    [
         [1, 1, 1],
         [1, 1, 0],
         [1, 0, 1]
    ]

    [
         [2, 2, 2],
         [2, 2, 0],
         [2, 0, 1]
    ]
    ###

Example 1:
    Input:
        image = [[1,1,1],[1,1,0],[1,0,1]]
        sr = 1, sc = 1, newColor = 2
    Output: [[2,2,2],[2,2,0],[2,0,1]]
    Explanation:
        From the center of the image (with position (sr, sc) = (1, 1)), all
        pixels connected by a path of the same color as the starting pixel are
        colored with the new color.
        Note the bottom corner is not colored 2, because it is not
        4-directionally connected to the starting pixel.
Note:
    The length of image and image[0] will be in the range [1, 50].
    The given starting pixel will satisfy:
    0 <= sr < image.length and 0 <= sc < image[0].length.
    The value of each color in image[i][j] and newColor will be an integer in
    [0, 65535].
"""


class Solution:
    def dfs_visit(self, sr, sc, cell_val, image, newColor, visited):
        """
        type sr: int
        type sc: int
        type cell_val: int
        type image: List[List[int]]
        type newColor: int
        type visited: Dict
        """
        # Don't go through a cell that its value differs from
        # the starting pixel's.
        if image[sr][sc] != cell_val:
            return

        visited[(sr, sc)] = True  # keep track of visited cells
        image[sr][sc] = newColor  # modify the visited cell

        # Generate all possible coordinates map from the center O(1)
        # (max of 9 values)
        # (-1, -1)| -1, 0  | (-1, 1)
        #             |
        #  0, -1  | (0, 0) |  0, 1
        #             |
        # (1, -1) |  1, 0  | ( 1, 1)
        for i in range(-1, 2):
            for j in range(-1, 2):
                # Neglect center coordinate map (itself) and the diagonal
                # coordinates map. i.e, all coordinates map in bracket above
                if i == j or i == -j:
                    continue

                # Get the new coordinate from coordinate map
                nsr = sr + i
                nsc = sc + j

                # make sure the new coordinates are valid
                # (i.e, within boundary)
                if 0 <= nsr < len(image) and 0 <= nsc < len(image[0]):
                    new_coord = nsr, nsc

                    # only visit its neighbours if we haven't encountered it
                    if new_coord not in visited:
                        self.dfs_visit(nsr, nsc, cell_val, image,
                                       newColor, visited)
        # allows backtracking
        del visited[(sr, sc)]

    def floodFill(self, image, sr, sc, newColor):
        """
        type image: List[List[int]]
        type sr: int
        type sc: int
        type newColor: int
        rtype: List[List[int]]
        """
        visited = {}
        cell_val = image[sr][sc]
        self.dfs_visit(sr, sc, cell_val, image, newColor, visited)
        return image


if __name__ == "__main__":
    s = Solution()
    image = [
         [1, 1, 1],
         [1, 1, 0],
         [1, 0, 1]
    ]
    sr = 1
    sc = 1
    newColor = 2
    print(s.floodFill(image, sr, sc, newColor))
