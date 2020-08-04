# -*- coding: utf-8 -*-
"""
Created on Thu May  7 15:56:10 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    In a binary tree, the root node is at depth 0, and children of each depth
    k node are at depth k+1.

    Two nodes of a binary tree are cousins if they have the same depth, but
    have different parents.

    We are given the root of a binary tree with unique values, and the values
    x and y of two different nodes in the tree.

    Return true if and only if the nodes corresponding to the values x and y
    are cousins.

Example 1:
    Input: root = [1,2,3,4], x = 4, y = 3
    Output: false

Example 2:
    Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
    Output: true

Example 3:
    Input: root = [1,2,3,null,4], x = 2, y = 3
    Output: false

Note:
    The number of nodes in the tree will be between 2 and 100.
    Each node has a unique integer value from 1 to 100.
"""
from queue import Queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def storeParent(self, node, level, x, y, parent, curr_parent=None):
        if not node:
            return False

        if node.val in (x, y):
            parent[node.val] = (curr_parent.val, level)

        if x in parent and y in parent:
            parent_idx = 0
            level_idx = 1
            parent_not_equal = parent[x][parent_idx] != parent[y][parent_idx]
            level_equal = parent[x][level_idx] == parent[y][level_idx]
            return parent_not_equal and level_equal
        else:
            left = self.storeParent(node.left, level+1, x, y, parent, node)
            right = self.storeParent(node.right, level+1, x, y, parent, node)

        return left or right

    # Recusive solution
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root or root.val == x or root.val == y:
            return False
        parent = {}
        level = 0
        return self.storeParent(root, level, x, y, parent)

    # Iterative solution
    # def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
    #     if not root or root.val == x or root.val == y:
    #         return False

    #     q = Queue()
    #     parent = {}
    #     level = 0
    #     q.put(root)
    #     while not q.empty():
    #         level += 1
    #         level_size = q.qsize()
    #         for _ in range(level_size):
    #             node = q.get()
    #             if node.left:
    #                 q.put(node.left)
    #                 if node.left.val in (x, y):
    #                     parent[node.left.val] = (node.val, level)

    #             if node.right:
    #                 q.put(node.right)
    #                 if node.right.val in (x, y):
    #                     parent[node.right.val] = (node.val, level)

    #             if x in parent and y in parent:
    #                 parent_not_equal = parent[x][0] != parent[y][0]
    #                 level_equal = parent[x][1] == parent[y][1]
    #                 return parent_not_equal and level_equal

    #     return False
