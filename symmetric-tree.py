# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 22:09:28 2020

@author: johnoyegbite
"""
# SOLVED! 
"""
Problem:
    Given a binary tree, check whether it is a mirror of itself 
    (ie, symmetric around its center).

Example1
    Input: {1,2,2,3,4,4,3}
    Output: true
    Explanation:
        1
       / \
      2   2
     / \ / \
    3  4 4  3
    This binary tree {1,2,2,3,4,4,3} is symmetric
Example2
    Input: {1,2,2,#,3,#,3}
    Output: false
    Explanation:
        1
       / \
      2   2
       \   \
       3    3
    This is not a symmetric tree

Challenge:
    Could you solve it both recursively and iteratively?
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

def is_palind(level, start, end):
    if not level:
        return True
    if start == end:
        return level[start] == level[end]
    if start == end-1:
        return level[start] == level[end]
    return level[start] == level[end] and is_palind(level, start+1, end-1)

def isSymmetric(root):
    """
    type root: root of the given tree
    rtype: Boolean (whether it is a mirror of itself)
    """
    # Write your code here
    """The trick is to check each level of the tree one after the other
    if they are palindrome. If at any point, one level is not palindrome, 
    return False
    
    PS: check the "val"s of current level and not the objects
    """
    if not root:
        return True

    queue = [root]
    while len(queue):
        new_queue = []
        curr_level_val = []
        for node in queue:
            if node.left:
                new_queue.append(node.left)
                curr_level_val.append(node.left.val)
            else:
                curr_level_val.append(None)
            if node.right:
                new_queue.append(node.right)
                curr_level_val.append(node.right.val)
            else:
                curr_level_val.append(None)
                
        if not is_palind(curr_level_val, 0, len(curr_level_val)-1):
            return False
            
        queue = new_queue
    return True

# Recursive Method!
"""
A tree is symmetric if the left subtree is a mirror reflection of the right subtree.

Therefore, the question is: 
    when are two trees a mirror reflection of each other?

Two trees are a mirror reflection of each other if:
    1. Their two roots have the same value.
    2. The right subtree of each tree is a mirror reflection of the left 
       subtree of the other tree.

This is like a person looking at a mirror. 
The reflection in the mirror has the same head, but the reflection's right arm 
corresponds to the actual person's left arm, and vice versa.

The explanation above translates naturally to a recursive function as follows.
"""
# def isSymmetric(root) {
#     return isMirror(root, root)
# }

# def isMirror(t1, t2) {
#     if t1 == null and t2 == null:
#         return true
#     if t1 == null or t2 == null:
#         return false
#     return t1.val == t2.val \
#         and isMirror(t1.right, t2.left) \
#         and isMirror(t1.left, t2.right)
# }