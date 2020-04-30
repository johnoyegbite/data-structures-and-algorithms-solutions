# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 22:11:41 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Return the root node of a binary search tree that matches the given
    preorder traversal.

    (Recall that a binary search tree is a binary tree where for every node,
    any descendant of node.left has a value < node.val, and any descendant of
    node.right has a value > node.val.  Also recall that a preorder traversal
    displays the value of the node first, then traverses node.left,
    then traverses node.right.)

Example 1:
    Input: [8,5,1,7,10,12]
    Output: [8,5,10,1,7,null,12]

             8
            / \
           5   10
          / \    \
         1   7    12

Note:
    1 <= preorder.length <= 100
    The values of preorder are distinct.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def insert(self, node: TreeNode, val: int):
        if val < node.val:
            # Go left
            if node.left:
                self.insert(node.left, val)
            else:
                node.left = TreeNode(val)
        else:
            # Go right
            if node.right:
                self.insert(node.right, val)
            else:
                node.right = TreeNode(val)
        return

    def bstFromPreorder(self, preorder: list[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        for i, val in enumerate(preorder):
            if i > 0:
                self.insert(root, val)

        return root
