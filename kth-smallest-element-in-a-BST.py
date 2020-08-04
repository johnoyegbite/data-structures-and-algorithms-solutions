# -*- coding: utf-8 -*-
"""
Created on Wed May 20 16:53:46 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a binary search tree, write a function kthSmallest to find the kth
    smallest element in it.

    Note:
        You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:
    Input: root = [3,1,4,null,2], k = 1
          3
         / \
        1   4
         \
          2
    Output: 1

Example 2:
    Input: root = [5,3,6,2,4,null,null,1], k = 3
               5
              / \
             3   6
            / \
           2   4
          /
         1
     Output: 3

Follow up:
    What if the BST is modified (insert/delete operations) often and you need
    to find the kth smallest frequently? How would you optimize the kthSmallest
    routine?
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inOrder(self, node: TreeNode) -> None:
        if not node:
            return
        # keep traversing till we meet the left most node
        self.inOrder(node.left)

        # after meeting the **left most** node, then that node is definitely
        # the 1st smallest element,
        # according to the properties of Binary Search Tree.
        # 1. update the self.kth_smallest
        # 2. reduce self.k so as to know how many element we have to visit
        #     before we stop our search for kth smallest.
        if self.k > 0:
            self.kth_smallest = node.val
            self.k -= 1
        # if we have traversed thorugh the total smallest element with lenght k
        # we are done!
        if self.k <= 0:
            return
        # if self.k >0, this means that we haven't seen our kth smallest and
        # we need to traverse.
        self.inOrder(node.right)

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # Make the root value the kth smallest (as default)
        self.kth_smallest = root.val

        # Store k to keep track of the total number of smallest element we have
        # meet so far k would be reduce till it get to 0
        # (k, k-1, k-2, ..., 2, 1)
        self.k = k

        # Modifies the kth smallest.
        # Inorder traversal makes sure we start at the left most node before
        # we start reducing k.
        self.inOrder(root)

        return self.kth_smallest
