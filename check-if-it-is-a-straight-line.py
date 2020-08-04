# -*- coding: utf-8 -*-
"""
Created on Fri May  8 10:20:33 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    You are given an array coordinates, coordinates[i] = [x, y], where [x, y]
    represents the coordinate of a point.
    Check if these points make a straight line in the XY plane.


Example 1:
    y-axis  ^
          7 |                              (6,7)
            |
          6 |                        (5,6)
            |
          5 |                  (4,5)
            |
          4 |            (3,4)
            |
          3 |      (2,3)
            |
          2 |(1,2)
            |
          1 |
            |
            |_____________________________________________>
               1     2     3     4     5     6     7       x-axis


    Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    Output: true

Example 2:
    Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
    Output: false

Constraints:
    2 <= coordinates.length <= 1000
    coordinates[i].length == 2
    -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
    coordinates contains no duplicate point.
"""


class Solution:
    def checkStraightLine(self, coordinates) -> bool:
        """
        type coordinates: List[List[int]]
        rtype: bool
        Equation is (y - y1) / (x - x1) = (y2 - y1) / (x2 - x1)
        """
        (x1, y1), (x2, y2) = coordinates[0], coordinates[1]

        for coord in coordinates:
            x, y = coord
            if (y - y1)*(x2 - x1) != (x - x1)*(y2 - y1):
                return False
        return True
