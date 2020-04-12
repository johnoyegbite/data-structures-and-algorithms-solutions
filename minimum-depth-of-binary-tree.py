# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 16:10:45 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a binary tree, find its minimum depth.

    The minimum depth is the number of nodes along the shortest path from the
    root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example 1:
    Given binary tree [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7
    return its minimum depth = 2.

Example 2:
    Given binary tree [1, 2],

        1
         \
          2
    return its minimum depth = 2.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def minDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0

    min_left = self.minDepth(root.left)
    min_right = self.minDepth(root.right)

    if not root.left or not root.right:
        # Here, min_left or min_right would be zero or both
        return min_left + min_right + 1
    return min(min_left, min_right) + 1
