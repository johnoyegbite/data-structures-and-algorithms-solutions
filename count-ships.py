# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 06:30:29 2020

@author: johnoyegbite
"""
# SOLVED!
"""
5. Count Ships
Given two points, which are the top right and bottom left corners of a rectangle,
find the number of ships present in between the two points
(more specifically, ships present inside the rectangle formed by these two points).

You have a function hasShips(A: Point, B: Point) -> bool which takes two Points as arguments and returns a boolean.
If there are ships in between the two points, it returns true, else false.

If you want to check whether a ship is present at a point, say A(2, 2),
you can pass the same point twice into the function above as so: hasShips(A, A)
which returns true if there's a ship at point A, and aliter.

The Point class looks like:
class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y

Consider the sea to be a cartesian plane.
There are ships at different places in the sea.

    x, y                          x, y
   (0, 6) ______________________ (7, 6)
          |  |  |  |  |  |  |  |
    x, y  |  |  |  |  |  |  |  |  x, y
   (0, 3) |  |  |  |  |  |  |  | (7, 3)
          |  |  |  |  |  |  |  |
    x, y  |  |  |  |  |  |  |  |
   (0, 0) |__|__|__|__|__|__|__| (7, 0)

topRight = (0, 7)
bottomLeft = (6, 0)

Solution 1:
    Loop through all the points one after the order and check if it contains
    a ship

Note: x is vertical and y is horizontal (we must use the normal coordinate system)
countShip = 0
--> (0, 0) and (7, 6)
--> y - row loop (i: FROM bottomLeft.y TO topRight.y+1) (from 0 to 6)
  --> x - col loop (j: FROM bottomLeft.x TO topRight.x+1) (from 0 to 7)
                          x, y
            point = Point(j, i)
            if hasShips(point, point):
              countShip += 1

Solution 2: Divide and Conquer
  - IF WE HAVE A RECTANGLE (BOX), DIVIDE INTO TWO:
      - check the bottom half if it hasShip, if true,
          recurse and count the total ships otherwise return 0
      - check the top half if it hasShip, if true,
          recurse and count the total ships otherwise return 0
      - base case occurs when we have a line
          (all point has the same y coordinate)

  - IF WE HAVE A LINE, DIVIDE INTO TWO:
	  - check the left half if it hasShip, if true,
          recurse and count the total ships otherwise return 0
      - chekc the right half if it hasShip, if true,
          recurse and count the total ships otherwise return 0
      - base case, if we have point,
          return 1 if it has hasShips and 0 otherwise

           x, y                x, y                        x, y
         (0, 6) (1, 6) (2, 6) (3, 6) (4, 6) (5, 6) (6, 6) (7, 6)
   				_      _      _      _      _      _      _      _
          |      |      |      |      |      |      |      |
def countLineShip(startPoint, endPoint):
		# base case
		if startPoint == endPoint:
    		return 1 if hasShips(startPoint, endPoint) else 0

    count = 0
    # recursive case
    modifiedX = (startPoint.x+endPoint.x) // 2
    midPoint = Point(modifiedX, startPoint.y)

    if hasShips(startPoint, midPoint):
    		count = countLineShip(startPoint, midPoint)

    if hasShips(midPoint, endPoint):
    		count = countLineShip(midPoint, endPoint)

    return count

"""

"""

    x, y                          x, y
   (0, 6) ______________________ (7, 6)
          |  |  |  |  |  |  |  |
    x, y  |  |  |  |  |  |  |  |  x, y
   (0, 3) |  |  |  |  |  |  |  | (7, 3)
          |  |  |  |  |  |  |  |
    x, y  |  |  |  |  |  |  |  |
   (0, 0) |__|__|__|__|__|__|__| (7, 0)


--> count_ship_line() function Visualization
start                 mid                          end
  A      B      C      D      E      F      G       H   x, y
(0, 6) (1, 6) (2, 6) (3, 6) (4, 6) (5, 6) (6, 6) (7, 6)
  |      |      |      |      |      |      |      |
  -                    -                           -
We have ships only at point A, D and H which are the start, mid and end points
as denoted by the UNDERSCORE below the PIPE "|" symbol

Now, I believe hasShips(start_pt(A), mid_pt_left(D)) would return False also
would hasShips(mid_pt_right(E), end_pt(H)), because hasShips(point_1, point_2)
checks if ships exists only between the points 1 and 2 and NOT INCLUDING the
points.
This means that count_ship_line(start(A), end(B)) would return 0 whereas,
it should return 3 as described in the diagram above

I think it should be modified to -->
(just to make sure it also checks start_pt and mid_pt_left as boundaries till
it reaches its base case)

i.e.
if hasShips(start_point, mid_point_left) or\
            hasShips(start_point, start_point) or\
            hasShips(mid_point_left, mid_point_left):
      count_ship += count_ship_line(start_point, mid_point_left)

AS OPPOSED TO

if hasShips(start_point, mid_point_left):
      count_ship += count_ship_line(start_point, mid_point_left)

Similar logic goes for the second if statement just below.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def hasShips(point1, point2):
    pass


def count_ship_line(start_point, end_point):
    """
    start                 mid                          end
      A      B      C      D      E      F      G       H   x, y
    (0, 6) (1, 6) (2, 6) (3, 6) (4, 6) (5, 6) (6, 6) (7, 6)
      |      |      |      |      |      |      |      |
      -                    -                           -
    We have ships only at point A, D and H which are the
    start, mid and end points as denoted by the UNDERSCORE
    below the PIPE "|" symbol.
    """
    if start_point.x == end_point.x:
        return 1 if hasShips(start_point, end_point) else 0
    count_ship = 0
    midPointX = (start_point.x + end_point.x) // 2
    mid_point_left = Point(midPointX, start_point.y)
    mid_point_right = Point(midPointX + 1, start_point.y)
    # Go Left
    if hasShips(start_point, mid_point_left) or\
            hasShips(start_point, start_point) or\
            hasShips(mid_point_left, mid_point_left):
	    count_ship += count_ship_line(start_point, mid_point_left)

    # Go right
    if hasShips(mid_point_right, end_point) or\
            hasShips(mid_point_right, mid_point_right) or\
            hasShips(end_point, end_point):
    	count_ship += count_ship_line(mid_point_right, end_point)

    return count_ship


def count_ship_box(bottom_left, upper_right):
    """
    # Divide into two BOX and Recurse

    ### ORIGINAL BOX
    x, y                          x, y
   (0, 6) ______________________ (7, 6)
          |  |  |  |  |  |  |  |
    x, y  |  |  |  |  |  |  |  |  x, y
   (0, 3) |  |  |  |  |  |  |  | (7, 3)
          |  |  |  |  |  |  |  |
    x, y  |  |  |  |  |  |  |  |  x, y
   (0, 0) |__|__|__|__|__|__|__| (7, 0)


   ### BOX 1
     x, y                          x, y
   (0, 6) ______________________ (7, 6)
          |  |  |  |  |  |  |  |
   (0, 4) |__|__|__|__|__|__|__| (7, 4)


   ### BOX 2
   (0, 3) ______________________ (7, 3)
          |  |  |  |  |  |  |  |
    x, y  |  |  |  |  |  |  |  |  x, y
   (0, 0) |__|__|__|__|__|__|__| (7, 0)
    """

    if bottom_left.y == upper_right.y:
        return count_ship_line(bottom_left, upper_right)

    mid_y = (bottom_left.y + upper_right.y) // 2

    top_box_upper_right = upper_right
    top_box_bottom_left = Point(bottom_left.x, mid_y + 1)
    top_box_count = 0
    if hasShips(top_box_bottom_left, top_box_upper_right):
        top_box_count = count_ship_box(top_box_bottom_left,
                                       top_box_upper_right)

    btm_box_bottom_left = bottom_left
    btm_box_upper_right = Point(upper_right.x, mid_y)
    btm_box_count = 0
    if hasShips(btm_box_bottom_left, btm_box_upper_right):
        btm_box_count = count_ship_box(btm_box_bottom_left,
                                       btm_box_upper_right)

    return top_box_count + btm_box_count
