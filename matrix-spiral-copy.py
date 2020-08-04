# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 20:40:02 2020

@author: johnoyegbite
"""
# SOLVED
"""
Problem:
    Matrix Spiral Copy
    Given a 2D array (matrix) inputMatrix of integers, create a function
    spiralCopy that copies inputMatrix’s values into a 1D array in a spiral
    order, clockwise. Your function then should return that array.
    Analyze the time and space complexities of your solution.

Example:
    input:  inputMatrix  = [ [1,    2,   3,  4,    5],
                         [6,    7,   8,  9,   10],
                         [11,  12,  13,  14,  15],
                         [16,  17,  18,  19,  20] ]

    output: [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16,
             11, 6, 7, 8, 9, 14, 13, 12]

See the illustration below to understand better what a clockwise spiral order
looks like. like an altClockwise spiral order

Constraints:

[time limit] 5000ms

[input] array.array.integer inputMatrix

1 ≤ inputMatrix[0].length ≤ 100
1 ≤ inputMatrix.length ≤ 100
[output] array.integer




input:  inputMatrix  = [

        0,0      0,1   0,2   0,3   0,4
        [1,       2,    3,    4,     5],

        1,0     1,1    1,2   1,3    1,4
        [6,      7,     8,    9,    10],

        2,0      2,1   2,2   2,3   2,4
        [11,     12,    13,  14,    15],

        3,0     3,1    3,2   3,3   3,4
        [16,    17,     18,   19,   20]
]

"""


def spiral_copy(inputMatrix):
    M = len(inputMatrix)
    N = len(inputMatrix[0])

    """
    if M == 1:
        return inputMatrix[0]

    if N == 1:
        return [inputMatrix[r][c] for r in range(M) for c in range(N)]
    """
    top_x = 0

    btm_x = M - 1

    left_y = 0

    right_y = N - 1

    spiral_cpy = []

    """
    # col matrix
    inputMatrix = [
      [1],
      [2],
      [3],
    ]

    # row matrix
    inputMatrix = [[1, 2, 3]]
    """
    """
        inputMatrix = [[1, 2, 3]]
        top_x = 0
        btm_x = 0
        left_y = 0
        right_y = 2
        spiral = []
    """
    while top_x <= btm_x and left_y <= right_y and len(spiral_cpy) < (M * N):
        # To get top edge, inputMatrix[top_x][left_y to right_y]
        # top_x stays constant, loop from left_y to right_y
        for c in range(left_y, right_y + 1):
            spiral_cpy.append(inputMatrix[top_x][c])

        # To get right edge, inputMatrix[top_x to btm_x][right_y]
        # right_y stays constant, loop from top_x to btm_x
        # also increase the index of top_x to avoid a double copy of the
        # top-right element and also to be used for the inner box if any.
        top_x += 1
        """
        inputMatrix = [[1, 2, 3]]
        top_x = 1
        btm_x = 0
        left_y = 0
        right_y = 2
        spiral = [1, 2, 3]
        """
        if top_x <= btm_x:
            for r in range(top_x, btm_x + 1):
                spiral_cpy.append(inputMatrix[r][right_y])

        # To get bottom edge, inputMatrix[btm_x][right_y to left_y]
        # btm_x stays constant, loop from right_y to left_y (right_y > left_y)
        # also decrease the index of right_y to avoid a double copy of the
        # bottom-right element and also to be used for the inner box if any.
        right_y -= 1
        ######
        """
        inputMatrix = [[1, 2, 3]]
        top_x = 1
        btm_x = 0
        left_y = 0
        right_y = 1
        spiral = [1, 2, 3]
        """
        ######
        if top_x <= btm_x:
            for c in range(right_y, left_y - 1, -1):
                spiral_cpy.append(inputMatrix[btm_x][c])

        # To get left edge, inputMatrix[btm_x to top_x][left_y]
        # left_y stays constant, loop from btm_x to top_x (where btm_x > top_x)
        # also decrease the index of btm_x to avoid a double copy of the
        # bottom-left element and also to be used for the inner box if any.
        btm_x -= 1
        if left_y <= right_y:
            for r in range(btm_x, top_x - 1, -1):
                spiral_cpy.append(inputMatrix[r][left_y])

        # also increase the index of left_y to avoid a double copy of the
        # top-left element in the next inner box.
        # and also to be used for the inner box if any.
        left_y += 1

    return spiral_cpy


if __name__ == "__main__":
    # General Matrix
    inputMatrix = [
        [1,       2,    3,    4,     5],
        [6,      7,     8,    9,    10],
        [11,     12,    13,  14,    15],
        [16,    17,     18,   19,   20]
    ]

    # col matrix
    inputMatrix = [
      [1],
      [2],
      [3],
    ]

    # row matrix
    inputMatrix = [[1, 2, 3]]

    print(spiral_copy(inputMatrix))
