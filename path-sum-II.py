# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 02:16:44 2020

@author: johnoyegbite
"""
# SOLVED!
"""
Problem:
    Given a binary tree and a sum, find all root-to-leaf paths where each 
    path's sum equals the given sum.

Example 1:
    Input: root = {5,4,8,11,#,13,4,7,2,#,#,5,1}, sum = 22
                  5
                 / \
                4   8
               /   / \
              11  13  4
             /  \    / \
            7    2  5   1
    Output: [[5,4,11,2],[5,8,4,5]]
    Explanation:
        The sum of the two paths is 22：
        5 + 4 + 11 + 2 = 22
        5 + 8 + 4 + 5 = 22

Example 2:
    Input: root = {10,6,7,5,2,1,8,#,9}, sum = 18
                  10
                 /  \
                6    7
              /  \   / \
              5  2   1  8
               \ 
                9  
    Output: [[10,6,2],[10,7,1]]
    Explanation:
        The sum of the two paths is 18：
        10 + 6 + 2 = 18
        10 + 7 + 1 = 18

Notice:
    A leaf is a node with no children.
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

def dfs_visit(root, result, visited, path, given_sum):
    visited.add(root)
    path.append(root.val)
    if not root.left and not root.right:
        if sum(path) == given_sum:
            result.append(path.copy())
    children = []    
    if root.left:
        children.append(root.left)
    if root.right:
        children.append(root.right)
    for child in children:
        if child not in visited:
            dfs_visit(child, result, visited, path, given_sum)
            
    visited.remove(root)
    path.pop()
            
"""
@param root: a binary tree
@param sum: the sum
@return: the scheme
"""
def pathSum(root, sum):
    # Write your code here.
    result = []
    visited = set()
    dfs_visit(root, result, visited, [], sum)
    return result