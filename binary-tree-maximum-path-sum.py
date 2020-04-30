# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 23:44:39 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a non-empty binary tree, find the maximum path sum.

    For this problem, a path is defined as any sequence of nodes from some
    starting node to any node in the tree along the parent-child connections.
    The path must contain at least one node and does not need to go through
    the root.

Example 1:
    Input: [1,2,3]

           1
          / \
         2   3

    Output: 6

Example 2:
    Input: [-10,9,20,null,null,15,7]

       -10
       / \
      9  20
        /  \
       15   7

    Output: 42
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxSum(self, node):
        """
        :type node: TreeNode
        :rtype: int
        """
        if not node:
            return 0

        max_sum_left = self.maxSum(node.left)
        max_sum_right = self.maxSum(node.right)

        # Remember that the maxPathSum of a leaf node must be its value.

        # So because max_sum_left or max_sum_right would return 0 in the
        # base case scenario,
        # I would just add its value to get the maxPathSum for a leaf node
        # for leaf nodes.
        # 1. => for a leaf node with value = x:
        # max_left = 0
        # max_right = 0
        # new_sum = 0 + 0 + x
        # => 'x' sum for a leaf nodes.
        # 2. => for a any node with value = y:
        # max_left = %must be non-negative%
        # max_right = %must be non-negative%
        # new_sum = (Z+) + (Z+) + y.
        max_sum_left = max_sum_left if max_sum_left >= 0 else 0
        max_sum_right = max_sum_right if max_sum_right >= 0 else 0

        new_sum = max_sum_left + max_sum_right + node.val

        self.max_sum = max(self.max_sum, new_sum)

        return max(max_sum_left, max_sum_right) + node.val

    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')
        self.maxSum(root)

        return self.max_sum


if __name__ == "__main__":
    s = Solution()
    root = TreeNode(2, TreeNode(-1))
    print(s.maxPathSum(root))
