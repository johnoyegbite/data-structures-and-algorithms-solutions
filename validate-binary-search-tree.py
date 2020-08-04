# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 10:51:56 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:
    1. The left subtree of a node contains only nodes with keys less than
        the node's key.
    2. The right subtree of a node contains only nodes with keys greater
        than the node's key.
    3. Both the left and right subtrees must also be binary search trees.
    4. A single node tree is a BST

Example 1:
    Input:  {-1}
    Output：true
    Explanation：
        For the following binary tree（only one node）:
            -1
          This is a binary search tree.

Example 2:
    Input:  {2,1,4,#,#,3,5}
    Output: true
    For the following binary tree:
          2
         / \
        1   4
           / \
          3   5
    This is a binary search tree.
"""

"""
Definition of TreeNode:
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def isValidBST(root, mininum=None, maximum=None):
    """
    type root: The root of binary tree.
    rtype: Boolean, True if the binary tree is BST, or false
    """
    # write your code here
    if not root:
        return True

    # The root node value must be greater than the minimum node value
    if mininum and root.val <= mininum.val:
        return False

    # The root node value must be lesser than the maximum node value
    if maximum and root.val >= maximum.val:
        return False

    # Make sure the left subtree of the root and the right subtree of the root
    # satisfies the same condition as stated above.
    # Furthermore, to determine the mininum and maximum:
    # 1. for the left subtree, the root node (parent node)
    #    should be the maximum.
    # 2. and for the right subtree, the root node
    #    (parent node would be the minimum
    return isValidBST(root.left, mininum, root) and\
        isValidBST(root.right, root, maximum)


# Method 2
# Using Inorder Traversal (left -> Root -> Right)
# This would create a sorted list.
def isValid_BST(root):
    # 1. Use inorder traversal and store all the element in a list
    # 2. loop through the list an return false if the list is not sorted
    #    Else return True
    pass
