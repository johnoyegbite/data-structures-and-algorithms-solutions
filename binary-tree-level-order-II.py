# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 21:17:13 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a binary tree, return the bottom-up level order traversal of its
    nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
    Given binary tree [3,9,20,null,null,15,7],
        3
       / \
      9  20
        /  \
       15   7
    return its bottom-up level order traversal as:
    [
      [15,7],
      [9,20],
      [3]
    ]
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        level_order = [[root]]
        level_order_vals = [[root.val]]

        curr_level = [root]
        curr_level_vals = [root.val]

        while curr_level:
            curr_level = []
            curr_level_vals = []
            for node in level_order[-1]:
                if node.left:
                    curr_level.append(node.left)
                    curr_level_vals.append(node.left.val)
                if node.right:
                    curr_level.append(node.right)
                    curr_level_vals.append(node.right.val)
            if curr_level:
                level_order.append(curr_level)
                level_order_vals.append(curr_level_vals)

        return level_order_vals[::-1]
