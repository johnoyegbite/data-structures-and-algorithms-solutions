# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 13:07:28 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a binary tree where each path going from the root to any leaf form a
    valid sequence, check if a given string is a valid sequence in such binary
    tree.

    We get the given string from the concatenation of an array of integers arr
    and the concatenation of all values of the nodes along a path results in a
    sequence in the given binary tree.


Example 1:

           0
          / \
       1       0
      / \     /
    0     1  0
     \   / \
      1 0   0

    Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,0,1]
    Output: true
    Explanation:
        The path 0 -> 1 -> 0 -> 1 is a valid sequence
        (green color in the figure).
        Other valid sequences are:
            0 -> 1 -> 1 -> 0
            0 -> 0 -> 0

Example 2:
           0
          / \
       1       0
      / \     /
    0     1  0
     \   / \
      1 0   0

    Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,0,1]
    Output: false
    Explanation: The path 0 -> 0 -> 1 does not exist,
    therefore it is not even a sequence.

Example 3:
           0
          / \
       1       0
      / \     /
    0     1  0
     \   / \
      1 0   0

    Input: root = [0,1,0,0,1,0,null,null,1,0,0], arr = [0,1,1]
    Output: false
    Explanation: The path 0 -> 1 -> 1 is a sequence,
    but it is not a valid sequence.

Constraints:
    1 <= arr.length <= 5000
    0 <= arr[i] <= 9
    Each node's value is between [0 - 9].
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def traverseTree(self, node: TreeNode, i: int, arr: list[int]) -> bool:
        # if arr is longer or shorter than path
        if (not node and i < len(arr)) or (node and i >= len(arr)):
            return False

        # if node is empty or if we meet a node and its value different
        # from the value at the arr current index
        if not node or node.val != arr[i]:
            return False

        # if we have completed the path and it's a leaf node
        if not node.left and not node.right and i == len(arr)-1:
            return True

        is_left_valid = self.traverseTree(node.left, i+1, arr)
        is_left_valid = self.traverseTree(node.right, i+1, arr)

        return is_left_valid or is_left_valid

    def isValidSequence(self, root: TreeNode, arr: list[int]) -> bool:
        # starting from the first element in the array
        first_idx = 0
        return self.traverseTree(root, first_idx, arr)
