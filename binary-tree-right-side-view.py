# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 02:09:12 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a binary tree, imagine yourself standing on the right side of it,
    return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

           1            <---
         /   \
        2     3         <---
         \     \
          5     4       <---
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
        """
        type root: TreeNode
        rtype: List[int]
        """
        # Traverse level by level and append the last element in the level
        # since the level would be appended from left to right and we need
        # the right value.
        if not root:
            return []
        levelNodes = [root]
        sideView = []
        while levelNodes:
            sideView.append(levelNodes[-1].val)
            newLevelNodes = []
            for parent in levelNodes:
                if parent.left:
                    newLevelNodes.append(parent.left)
                if parent.right:
                    newLevelNodes.append(parent.right)
            levelNodes = newLevelNodes
        return sideView
