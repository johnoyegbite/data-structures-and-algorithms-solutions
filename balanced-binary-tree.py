# -*- coding: utf-8 -*-
"""
@author: johnoyegbite
"""

# SOLVED!
"""
Problem:
    Given a binary tree, determine if it is height-balanced.

    For this problem, a height-balanced binary tree is defined as:

        a binary tree in which the left and right subtrees of every node
        differ in height by no more than 1.

Example 1:
    Given the following tree [3,9,20,null,null,15,7]:

        3
       / \
      9  20
        /  \
       15   7
    Return true.

Example 2:
    Given the following tree [1,2,2,3,3,null,null,4,4]:

           1
          / \
         2   2
        / \
       3   3
      / \
     4   4
    Return false.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def height(self, node):
        if not node:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        if abs(left_height-right_height) > 1:
            self.balanced = False

        return max(left_height, right_height) + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.balanced = True
        self.height(root)
        return self.balanced
