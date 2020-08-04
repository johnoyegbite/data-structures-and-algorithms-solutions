# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 00:24:37 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a binary tree, return the zigzag level order traversal of its 
    nodes' values. (ie, from left to right, then right to left for the next 
    level and alternate between).

For example:
    Given binary tree [3,9,20,null,null,15,7],
        3
       / \
      9  20
        /  \
       15   7
    return its zigzag level order traversal as:
    [
      [3],
      [20,9],
      [15,7]
    ]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def zigzagLevelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root:
        return []

    queue = [root]
    zig_zag_order = [[root.val]]

    i = 1  # Keep track of when to reverse a level to denote zig-zag
    while len(queue):
        new_queue = []
        new_level_val = []
        for node in queue:
            if node.left:
                new_queue.append(node.left)
                new_level_val.append(node.left.val)
            if node.right:
                new_queue.append(node.right)
                new_level_val.append(node.right.val)
        if len(new_level_val):  # To avoid empty level
            if i % 2 == 0:
                zig_zag_order.append(new_level_val)
            else:
                zig_zag_order.append(new_level_val[::-1])
            i += 1
        queue = new_queue

    return zig_zag_order
