# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:21:12 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    (This problem is an interactive problem.)

    A binary matrix means that all elements are 0 or 1.
    For each individual row of the matrix, this row is sorted in
    non-decreasing order.

    Given a row-sorted binary matrix binaryMatrix,
    return leftmost column index(0-indexed) with at least a 1 in it.
    If such index doesn't exist, return -1.

    You can't access the Binary Matrix directly.
    You may only access the matrix using a BinaryMatrix interface:

        BinaryMatrix.get(x, y) returns the element of the matrix at index
        (x, y) (0-indexed).
        BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which
        means the matrix is n * m.

    Submissions making more than 1000 calls to BinaryMatrix.get will be judged
    Wrong Answer.
    Also, any solutions that attempt to circumvent the judge will result in
    disqualification.

    For custom testing purposes you're given the binary matrix mat as input
    in the following four examples.
    You will not have access the binary matrix directly.

The required column would be identified with " * " on it.
Example 1:

      *
    | 0 | 0 |
    | 1 | 1 |

    Input: mat = [[0,0],[1,1]]
    Output: 0

Example 2:

          *
    | 0 | 0 |
    | 0 | 1 |
    Input: mat = [[0,0],[0,1]]
    Output: 1

Example 3:

    | 0 | 0 |
    | 0 | 0 |
    Input: mat = [[0,0],[0,0]]
    Output: -1

Example 4:

          *
    | 0 | 0 | 0 | 1 |
    | 0 | 0 | 1 | 1 |
    | 0 | 1 | 1 | 1 |
    Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
    Output: 1

Constraints:
    1 <= mat.length, mat[i].length <= 100
    mat[i][j] is either 0 or 1.
    mat[i] is sorted in a non-decreasing way.


Hint:
    1.
    (Binary Search) For each row do a binary search to find the leftmost
    one on that row and update the answer.

    2.
    (Optimal Approach) Imagine there is a pointer p(x, y) starting from top
    right corner. p can only move left or down.
    If the value at p is 0, move down. If the value at p is 1, move left.
    Try to figure out the correctness and time complexity of this algorithm.
"""


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
class BinaryMatrix(object):
    def get(self, x: int, y: int) -> int:
        pass

    def dimensions(self) -> list[int]:
        pass


class Solution:
    def binarySearch(self, i: int, m: int, binaryMatrix) -> None:
        start = 0
        end = m

        while start <= end:
            mid = (start + end)//2
            cell = binaryMatrix.get(i, mid)  # to reduce no of API calls
            if cell == 0:
                start = mid + 1
            elif cell == 1:
                self.column = min(self.column, mid)
                end = mid - 1

    # def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
    #     """Hint 1 Solution"""
    #     n, m = binaryMatrix.dimensions()

    #     self.column = m

    #     for i in range(n):
    #         self.binarySearch(i, m-1, binaryMatrix)

    #     if self.column == m:
    #         return -1

    #     return self.column

    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        """Hint 2 Solution"""
        n, m = binaryMatrix.dimensions()

        column_idx = m

        x, y = [0, m-1]

        while x < n and y >= 0:
            cell = binaryMatrix.get(x, y)
            if cell == 0:
                x += 1
            elif cell == 1:
                column_idx = min(column_idx, y)
                y -= 1

        if column_idx == m:
            return -1

        return column_idx
