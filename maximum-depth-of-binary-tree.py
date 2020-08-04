# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 03:49:37 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a binary tree, find its maximum depth.

    The maximum depth is the number of nodes along the longest path from the
    root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:
    Given binary tree [3,9,20,null,null,15,7],
        3
       / \
      9  20
        /  \
       15   7
    return its depth = 3.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1
