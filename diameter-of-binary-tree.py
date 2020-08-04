# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 19:18:35 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a binary tree, you need to compute the length of the diameter
    of the tree.
    The diameter of a binary tree is the length of the longest path between
    any two nodes in a tree. This path may or may not pass through the root.

Example:
    Given a binary tree
              1
             / \
            2   3
           / \
          4   5
    Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of
      edges between them.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, node):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not node:
            return -1

        max_left = self.maxDepth(node.left)
        max_right = self.maxDepth(node.right)

        # Remember that the diameter of a leaf node must be zero.
        # So because max_left or max_right would return -1 in the base case
        # scenario,
        # I have to add 1 to both the max_left and max_right to give me '0'
        # for leaf nodes.
        # => for a leaf node:
        # max_left = -1
        # max_right = -1
        # new_diameter = (-1 + 1) + (-1 + 1) = 0
        # => "0" diameter for leaf nodes.

        new_diameter = (max_left + 1) + (max_right + 1)

        self.diameter = max(self.diameter, new_diameter)

        return max(max_left, max_right) + 1

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter = 0
        self.maxDepth(root)

        return self.diameter
