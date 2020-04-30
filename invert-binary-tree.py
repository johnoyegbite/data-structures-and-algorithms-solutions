# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 01:20:21 2020

@author: johnoyegbite
"""
# SOLVED! Faster than 90.88%
"""
Problem:
    Invert a binary tree.

Example:
    Input:

         4
       /   \
      2     7
     / \   / \
    1   3 6   9

    Output:

        4
       /   \
      7     2
     / \   / \
    9   6 3   1

Trivia:
    This problem was inspired by this original tweet by Max Howell:

Google:
    90% of our engineers use the software you wrote (Homebrew),
    but you can’t invert a binary tree on a whiteboard so f*** off.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invert(self, node: TreeNode) -> None:
        if not node:
            return
        node.left, node.right = node.right, node.left
        self.invert(node.left)
        self.invert(node.right)
        return

    def invertTree(self, root: TreeNode) -> TreeNode:
        self.invert(root)
        return root
